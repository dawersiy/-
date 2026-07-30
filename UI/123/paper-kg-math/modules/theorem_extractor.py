"""
数学定理与关系抽取引擎
----------------------
使用 LLM 从数学论文正文中抽取：
1. 定义、定理、引理、推论等结构化节点
2. 定理之间的逻辑推导关系（边）
"""

import json
from typing import Optional

from modules.llm_client import LLMClient


# ---------- LLM 提示词模板 ----------

EXTRACTION_SYSTEM_PROMPT = """你是一位数学逻辑专家。你的任务是从数学论文的正文片段中，提取出
其中的定义、定理、引理、推论等数学节点，以及它们之间的逻辑关系。

## 输出格式（严格 JSON）

请严格按照以下 JSON Schema 输出，不要包含任何其他内容：

```json
{
  "theorems": [
    {
      "name": "定理简称（如：微积分第一基本定理）",
      "type": "Definition | Theorem | Lemma | Corollary",
      "theorem_no": "编号（如：定理 3.1，若没有则留空字符串）",
      "content": "定理/定义的具体陈述内容，尽量完整",
      "has_proof": true,
      "proof_text": "证明文本（如果有证明，否则为空字符串）"
    }
  ],
  "relations": [
    {
      "source_name": "源定理名称（必须与 theorems[].name 一致）",
      "target_name": "目标定理名称（必须与 theorems[].name 一致）",
      "relation": "PROVES | IMPLIES | SPECIAL_CASE_OF | GENERALIZATION_OF | EQUIVALENT_TO | DEPENDS_ON",
      "description": "关系描述（一句话）"
    }
  ]
}
```

## 关系类型说明

- PROVES：A 用于证明 B（A 是 B 证明中的关键步骤）
- IMPLIES：A 推导出 B
- SPECIAL_CASE_OF：A 是 B 的特例
- GENERALIZATION_OF：A 是 B 的推广
- EQUIVALENT_TO：A 与 B 等价
- DEPENDS_ON：A 依赖某个定义或前置定理

## 注意事项

1. 类型名称必须从给定的 6 种中选取，不要自创
2. 每条关系的 source_name 和 target_name 必须能在 theorems 列表中找到对应节点
3. 如果一个定理用于证明另一个定理，请用 PROVES 关系
4. 如果正文中没有明确的定理或关系，请返回空的 theorems 和 relations 数组
5. 即使正文片段不完整，也请尽力提取其中的信息"""


# ---------- 抽取引擎 ----------

class TheoremExtractor:
    """
    定理抽取引擎。

    接收论文正文片段，调用 LLM 进行分析，返回结构化的定理与关系数据。

    使用方式：
        extractor = TheoremExtractor(llm_client)
        result = extractor.extract(chapter_body, chapter_title="第1章")
    """

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm = llm_client or LLMClient()

    def extract(self, chapter_body: str, chapter_title: str = "") -> Optional[dict]:
        """
        从章节正文中抽取定理和关系。

        Args:
            chapter_body:  章节正文文本
            chapter_title: 章节标题（用于 LLM 理解的上下文）

        Returns:
            dict | None: 包含 theorems 和 relations 的字典，
                        格式: {"theorems": [...], "relations": [...]}
        """
        if not chapter_body or len(chapter_body.strip()) < 20:
            # 正文太短，不太可能包含结构化定理
            return {"theorems": [], "relations": []}

        user_message = f"章节标题：{chapter_title}\n\n正文：\n{chapter_body}"

        result = self.llm.chat_json(EXTRACTION_SYSTEM_PROMPT, user_message)

        if result is None:
            print(f"[WARN] LLM 抽取失败，章节：「{chapter_title}」")
            return {"theorems": [], "relations": []}

        # 确保字段存在
        result.setdefault("theorems", [])
        result.setdefault("relations", [])

        # 基本校验
        self._validate(result)
        return result

    @staticmethod
    def _validate(result: dict):
        """
        校验 LLM 返回结果的合理性。

        - 过滤掉空的定理（无 name 或 name 为空）
        - 过滤掉两端不存在的关系
        """
        # 收集定理名称集合
        names = {th["name"] for th in result.get("theorems", []) if th.get("name")}

        # 过滤无效定理
        result["theorems"] = [
            th for th in result.get("theorems", [])
            if th.get("name") and th.get("type") in {
                "Definition", "Theorem", "Lemma", "Corollary"
            }
        ]

        # 过滤无效关系
        valid_types = {"PROVES", "IMPLIES", "SPECIAL_CASE_OF",
                       "GENERALIZATION_OF", "EQUIVALENT_TO", "DEPENDS_ON"}
        result["relations"] = [
            r for r in result.get("relations", [])
            if (r.get("source_name") in names and
                r.get("target_name") in names and
                r.get("relation") in valid_types)
        ]
