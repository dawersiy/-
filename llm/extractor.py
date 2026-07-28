"""LLM定理边界检测 — 从论文中精确提取定理/引理/定义/命题/推论"""

from llm.client import call_llm_structured

EXTRACTOR_SYSTEM = """你是一位数学论文解析专家。你的任务是从Markdown格式的数学论文中精确提取所有数学断言。

对于每个定理、引理、推论、定义、命题：
1. 提取精确的类型 (theorem/lemma/corollary/definition/proposition)
2. 提取编号（如果有的话）
3. 提取完整的陈述文本（不含证明部分的文本，但包含所有前提条件和结论）
4. 提取核心LaTeX公式（最重要的1-2个公式，用于标识该定理）
5. 提取前提条件 (premises: 定理所需的假设，自然语言描述)
6. 提取结论 (conclusion: 定理断言的核心结果，自然语言描述)
7. 分配置信度 (0-1: 你对提取边界正确性的信心)
8. 提取证明技巧 (proof_technique: 如 fixed_point, Lyapunov, variational, convergence_analysis, energy_estimate, duality, projection, none)

规则：
- 只提取数学断言，不要提取算法步骤、注释、或证明过程
- 如果遇到非标准标注的定理（如"我们证明以下结果"），也应提取
- 每个定理的statement应该是独立的 —— 不要包含后续其他定理或证明的文本
- LaTeX公式从$$...$$或$...$中提取，选择最具代表性的1-2个

输出格式: {result: {items: [{type, number, name, statement, latex, premises, conclusion, proof_technique, confidence}]}}"""

EXTRACTOR_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "enum": ["theorem", "lemma", "corollary", "definition", "proposition"]},
                    "number": {"type": "string"},
                    "name": {"type": "string"},
                    "statement": {"type": "string"},
                    "latex": {"type": "string"},
                    "premises": {"type": "string"},
                    "conclusion": {"type": "string"},
                    "proof_technique": {"type": "string"},
                    "confidence": {"type": "number"}
                },
                "required": ["type", "name", "statement", "confidence"]
            }
        }
    },
    "required": ["items"],
    "additionalProperties": False
}

def extract_from_paper(paper_text: str, paper_id: str = "") -> list[dict]:
    """从论文文本中LLM提取所有定理等"""
    # 截断过长文本
    if len(paper_text) > 15000:
        # 分块处理
        chunks = []
        chunk_size = 12000
        for i in range(0, len(paper_text), chunk_size):
            chunk = paper_text[i:i + chunk_size]
            if len(chunk) > 500:
                chunks.append(chunk)

        all_items = []
        for ci, chunk in enumerate(chunks):
            prompt = f"以下是一篇数学论文的部分内容 (第{ci+1}/{len(chunks)}段):\n\n{chunk}"
            result = call_llm_structured(
                EXTRACTOR_SYSTEM, prompt, EXTRACTOR_SCHEMA,
                cache_stage="extract"
            )
            if result and 'items' in result:
                for item in result['items']:
                    item['chunk_index'] = ci
                all_items.extend(result['items'])
        return all_items
    else:
        prompt = f"以下是一篇数学论文的完整内容:\n\n{paper_text}"
        result = call_llm_structured(
            EXTRACTOR_SYSTEM, prompt, EXTRACTOR_SCHEMA,
            cache_stage="extract"
        )
        if result and 'items' in result:
            return result['items']
        return []
