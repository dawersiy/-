"""LLM语义等价判断 — 判断两个定理/公式是否陈述同一数学结果"""

from llm.client import call_llm_structured
from difflib import SequenceMatcher

DEDUP_SYSTEM = """你是一位数学专家，专门判断两个数学定理或公式是否在数学上等价。

判断标准：
- "identical": 完全相同的定理 — 相同的假设、相同的结论、仅在表述上有微小差异
- "equivalent": 数学等价 — 可以相互推导，核心数学内容相同
- "generalization": 一个是另一个的推广（一个包含另一个作为特例）
- "different": 不同的定理 — 陈述不同的数学事实

请给出:
1. relationship: "identical" | "equivalent" | "generalization" | "different"
2. confidence: 0.0-1.0 的信心分数
3. reasoning: 简短解释你的判断

输出格式: {result: {relationship, confidence, reasoning}}"""

DEDUP_SCHEMA = {
    "type": "object",
    "properties": {
        "relationship": {"type": "string", "enum": ["identical", "equivalent", "generalization", "different"]},
        "confidence": {"type": "number"},
        "reasoning": {"type": "string"}
    },
    "required": ["relationship", "confidence", "reasoning"],
    "additionalProperties": False
}

def check_equivalence(item_a: dict, item_b: dict) -> dict:
    """判断两个item是否等价"""
    prompt = f"""比较以下两个数学条目：

条目A:
  名称: {item_a.get('name', '')}
  类型: {item_a.get('type', '')}
  公式: {item_a.get('latex', '')[:500]}
  陈述: {item_a.get('statement', '')[:1000]}

条目B:
  名称: {item_b.get('name', '')}
  类型: {item_b.get('type', '')}
  公式: {item_b.get('latex', '')[:500]}
  陈述: {item_b.get('statement', '')[:1000]}

它们是否陈述了相同的数学结果？"""

    result = call_llm_structured(
        DEDUP_SYSTEM, prompt, DEDUP_SCHEMA,
        cache_stage="dedup"
    )

    if not result:
        # 回退：使用基于结构的相似度
        from build_knowledge_graph import latex_signature
        sig_a = latex_signature(item_a.get('latex', ''))
        sig_b = latex_signature(item_b.get('latex', ''))
        if sig_a == sig_b:
            return {"relationship": "identical", "confidence": 0.8, "reasoning": "结构签名完全相同"}
        elif len(sig_a) > 25 and len(sig_b) > 25:
            sim = SequenceMatcher(None, sig_a, sig_b).ratio()
            if sim > 0.9:
                return {"relationship": "equivalent", "confidence": 0.7, "reasoning": f"结构相似度 {sim:.2f}"}
        return {"relationship": "different", "confidence": 0.5, "reasoning": "回退判断"}

    return result
