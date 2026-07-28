"""LLM智能关系发现 — 判断两个定理之间的推导/推广/依赖/等价关系"""

from llm.client import call_llm_thinking

RELATION_SYSTEM = """你是一位数学史和方法论专家。请判断两个数学定理或结果之间的关系。

关系类型：
- "derives": 条目A可以从条目B推导出来 (B→A), 或A是B的直接推论
- "generalizes": A推广了B (A是更一般的情况, B是A的特例)
- "depends": A的证明依赖B (B是证明A的关键引理或前置定理)
- "equivalent": A和B在数学上等价
- "none": 两者之间没有直接的逻辑关系

判断时请考虑：
1. 如果A是定理、B是引理且共享核心概念，B很可能支撑A的证明 (depends)
2. 如果A和B是相同类型但A的假设更弱或结论更强，A推广了B (generalizes)
3. 如果A是推论、B是定理，A来源于B (derives)
4. 如果两个结果都描述了相同类型的收敛性但条件不同，可能是一般/特殊关系
5. 如果来自不同论文讨论不同主题，可能无关 (none)

输出: {result: {type, confidence, note}}"""

RELATION_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {"type": "string", "enum": ["derives", "generalizes", "depends", "equivalent", "none"]},
        "confidence": {"type": "number"},
        "note": {"type": "string"}
    },
    "required": ["type", "confidence", "note"],
    "additionalProperties": False
}

def discover_pair_relation(item_a: dict, item_b: dict) -> dict:
    """判断两个item之间的数学关系"""
    prompt = f"""判断以下两个数学结果之间的关系：

条目A:
  来源: {item_a.get('source_paper', '')} ({item_a.get('source_year', '')})
  名称: {item_a.get('name', '')}
  类型: {item_a.get('type', '')}
  公式: {item_a.get('latex', '')[:400]}
  陈述摘要: {item_a.get('statement', '')[:800]}

条目B:
  来源: {item_b.get('source_paper', '')} ({item_b.get('source_year', '')})
  名称: {item_b.get('name', '')}
  类型: {item_b.get('type', '')}
  公式: {item_b.get('latex', '')[:400]}
  陈述摘要: {item_b.get('statement', '')[:800]}

请判断A与B之间的数学关系。"""

    result = call_llm_thinking(
        RELATION_SYSTEM, prompt, RELATION_SCHEMA,
        cache_stage="relation"
    )

    if not result:
        return {"type": "none", "confidence": 0.0, "note": "LLM调用失败"}

    return result
