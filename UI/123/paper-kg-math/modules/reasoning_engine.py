"""
推理引擎：图谱路径 + LLM 协同
------------------------------
结合 Neo4j 图结构查询和 LLM 语义理解，实现：
1. 定理证明依赖链推理
2. 两个定理之间的推导路径发现
3. 数学知识问答
"""

from typing import Optional

from modules.graph_store import GraphStore
from modules.llm_client import LLMClient


# ---------- 推理提示词 ----------

REASONING_SYSTEM_PROMPT = """你是一位数学推理专家。你将收到一个关于数学定理的问题，
以及从知识图谱中查询到的相关定理节点和推导路径。

请根据图谱中的结构化信息，用自然语言回答用户的问题。

## 回答要求

1. **回答结构清晰**：先给出结论，再解释推理过程
2. **引用定理**：在回答中使用 【定理名】 标注引用的定理，例如：
   "根据【微积分第一基本定理】，变上限积分是其原函数..."
3. **说明推导关系**：如果有推导路径，请清晰说明每一步的关系类型
4. **诚实**：如果图谱中没有足够信息，请明确说明并给出建议

## 输出格式

请用 markdown 格式回答，方便前端渲染。
在你引用的每个定理上，使用 HTML 标签包裹：
<span class="theorem-ref" data-name="定理名称">定理名称</span>

这样前端可以自动高亮对应节点。"""


# ---------- 推理引擎 ----------

class ReasoningEngine:
    """
    推理引擎：图谱结构查询 + LLM 语义理解。

    工作流程：
        1. 解析用户问题中的数学实体
        2. 在图谱中查询相关节点和路径
        3. 将图谱结果交给 LLM 进行语义理解和推理
        4. 返回带标注的回答文本

    使用方式：
        engine = ReasoningEngine()
        answer = engine.reason("微积分第一基本定理的证明依赖哪些前置定理？")
    """

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm = llm_client or LLMClient()
        self.store = GraphStore()

    def reason(self, question: str) -> dict:
        """
        对用户问题进行图谱增强推理。

        Args:
            question: 用户自然语言问题

        Returns:
            dict: {
                "answer": "markdown 格式的回答",
                "highlight_nodes": ["节点名1", "节点名2", ...],
                "graph_context": {...}  # 相关的图谱子图数据
            }
        """
        # Step 1: 搜索相关节点
        keywords = self._extract_keywords(question)
        related_nodes = []
        for kw in keywords:
            nodes = self.store.search_nodes(kw)
            related_nodes.extend(nodes)

        # 去重
        seen = set()
        unique_nodes = []
        for n in related_nodes:
            if n["name"] not in seen:
                seen.add(n["name"])
                unique_nodes.append(n)

        # Step 2: 查询节点间的路径（如果问题涉及多个实体）
        paths = []
        if len(unique_nodes) >= 2:
            try:
                paths = self.store.find_path_between(
                    unique_nodes[0]["name"],
                    unique_nodes[-1]["name"],
                )
            except Exception:
                pass  # 路径查询失败时忽略，不影响回答

        # Step 3: 构建 LLM 提示，让模型综合图谱信息给出回答
        context_text = self._build_context(unique_nodes, paths)
        user_message = f"""## 用户问题

{question}

## 知识图谱查询结果

{context_text}

请根据以上图谱信息回答用户问题。"""

        answer = self.llm.chat(REASONING_SYSTEM_PROMPT, user_message)

        # Step 4: 提取高亮节点列表
        highlight_nodes = [n["name"] for n in unique_nodes]

        # 也从回答中提取带 data-name 属性的节点引用
        import re
        refs = re.findall(r'data-name="([^"]+)"', answer or "")
        for ref in refs:
            if ref not in highlight_nodes:
                highlight_nodes.append(ref)

        # 构建子图上下文供前端联动
        graph_context = {
            "nodes": unique_nodes,
            "paths": paths,
        }

        return {
            "answer": answer or "抱歉，暂时无法回答这个问题。请确保已扫描并导入了论文。",
            "highlight_nodes": highlight_nodes,
            "graph_context": graph_context,
        }

    # --------------------------------------------------
    # 内部方法
    # --------------------------------------------------

    @staticmethod
    def _extract_keywords(question: str) -> list[str]:
        """
        从问题中提取可能的关键词。用 LLM 识别数学实体名称。

        简单的英文单词和短中文词也用正则辅助提取（fallback）。
        """
        import re
        # 提取英文单词作为基础关键词
        english_words = re.findall(r"[A-Za-z][A-Za-z\s\-]+[A-Za-z]", question)

        # 用 LLM 提取数学实体名称
        entity_names: list[str] = []
        try:
            from modules.llm_client import LLMClient
            llm = LLMClient()
            llm.temperature = 0.0
            llm.max_tokens = 256
            # 使用简短的提示让 LLM 快速提取
            result = llm.chat_json(
                system_prompt="""从用户问题中提取数学概念/定理/定义的名称。
输出 JSON: {"entities": ["名称1", "名称2"]}
只提取实际的数学实体名词，不提取"讲解"、"是什么"等通用词。如无明确实体则返回空数组。""",
                user_message=question,
            )
            if result and isinstance(result.get("entities"), list):
                entity_names = result["entities"]
            llm.temperature = 0.3  # 恢复默认
            llm.max_tokens = 4096
        except Exception:
            pass

        # Fallback: 正则提取 2-4 字中文词组（与 LLM 结果合并）
        chinese_words = re.findall(r"[一-鿿]{2,4}", question)
        # 过滤掉常见疑问词
        stop_words = {"讲解", "一下", "是什么", "怎么样", "如何", "为什么", "解释", "说明", "介绍", "请问", "帮我"}
        chinese_words = [w for w in chinese_words if w not in stop_words]

        # LLM 结果优先，正则结果补充
        all_keywords = entity_names + [w for w in chinese_words if w not in entity_names]
        return all_keywords[:8]  # 最多 8 个关键词

    @staticmethod
    def _build_context(nodes: list[dict], paths: list[dict]) -> str:
        """将图谱查询结果格式化为 LLM 可理解的文本。"""
        parts = []

        if nodes:
            parts.append("### 相关定理节点")
            for n in nodes[:10]:  # 最多 10 个
                parts.append(
                    f"- **[{n['type']}] {n['name']}**"
                    + (f" ({n.get('theorem_no', '')})" if n.get('theorem_no') else "")
                    + f"\n  {n.get('content', '')[:200]}"
                )

        if paths:
            parts.append("\n### 推导路径")
            for i, path in enumerate(paths[:5], 1):
                node_names = " → ".join(
                    n["name"] for n in path["nodes"]
                )
                parts.append(f"\n**路径 {i}** (深度 {path['depth']}):")
                parts.append(f"  {node_names}")
                for r in path["relations"]:
                    parts.append(
                        f"  - {r.get('source', '?')} "
                        f"--[{r['type']}]--> "
                        f"{r.get('target', '?')}"
                        + (f": {r['description']}" if r.get('description') else "")
                    )

        return "\n".join(parts) if parts else "（未找到相关信息）"
