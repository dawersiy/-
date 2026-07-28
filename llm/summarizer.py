"""LLM中文摘要生成 — 为每个定理/公式生成1-3句中文摘要"""

from llm.client import call_llm_text

SUMMARIZE_SYSTEM = """你是一位数学专家，擅长用简洁的中文解释数学定理。

请为给定的数学定理或公式生成1-3句中文摘要。摘要应：
1. 用通俗的语言解释定理的核心含义
2. 说明定理的用途或重要性
3. 如果可能，提及该定理与其他理论的关系
4. 严格控制在1-3句之内
5. 使用中文专业术语

请直接输出摘要文本，不要包含任何前缀或标记。"""

def summarize_item(name: str, item_type: str, statement: str, latex: str = "") -> str:
    """为单个item生成中文摘要"""
    if not statement.strip():
        return ""

    # 截断过长的输入
    stmt_short = statement[:3000]

    prompt = f"""请为以下数学{item_type}生成中文摘要：

名称: {name}
类型: {item_type}
核心公式: {latex[:500] if latex else "无"}
内容: {stmt_short}"""

    summary = call_llm_text(
        SUMMARIZE_SYSTEM, prompt,
        cache_stage="summarize"
    )

    return summary.strip()
