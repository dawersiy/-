"""LLM语义关键词和领域标签分配"""

from llm.client import call_llm_structured

KEYWORD_SYSTEM = """你是一位数学分类专家。请为给定的数学定理/命题/公式分配关键词和领域标签。

领域标签从以下层级本体中选择:
顶级领域:
- optimization_theory (优化理论)
- operator_theory (算子理论)
- numerical_methods (数值方法)
- convergence_theory (收敛理论)
- variational_analysis (变分分析)
- dynamical_systems (动力系统)
- convex_analysis (凸分析)
- functional_analysis (泛函分析)

子领域标签 (可选):
- proximal_point, gradient_method, accelerated_method, heavy_ball, inertial, splitting,
- monotone_operators, maximal_monotone, nonexpansive, resolvent, subdifferential,
- weak_convergence, strong_convergence, convergence_rate, linear_convergence,
- dissipative_system, second_order, damping, lyapunov,
- projection, extragradient, forward_backward, douglas_rachford,
- bregman, entropy, interior_point, barrier, penalty, augmented_lagrangian,
- variable_metric, quasi_newton, newton_method,
- saddle_point, minimax, duality, fenchel,
- fixed_point, contraction, averaged_operator,
- regularization, tikhonov, viscosity

请分配:
1. 3-8个关键词 (从上述标签中选择最合适的)
2. 1-3个领域标签 (顶级或子领域)
3. 置信度 (0-1)

输出格式: {result: {keywords: [...], domain: [...], confidence: 0.0}}"""

KEYWORD_SCHEMA = {
    "type": "object",
    "properties": {
        "keywords": {"type": "array", "items": {"type": "string"}},
        "domain": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "number"}
    },
    "required": ["keywords", "domain", "confidence"],
    "additionalProperties": False
}

def assign_keywords_llm(name: str, item_type: str, statement: str, latex: str = "") -> dict:
    """LLM分配关键词和领域标签"""
    stmt_short = statement[:2000]
    prompt = f"""请为以下数学条目分配关键词:

名称: {name}
类型: {item_type}
核心公式: {latex[:400] if latex else "无"}
陈述: {stmt_short}"""

    result = call_llm_structured(
        KEYWORD_SYSTEM, prompt, KEYWORD_SCHEMA,
        cache_stage="keywords"
    )

    if result:
        return result
    return {"keywords": [item_type], "domain": [], "confidence": 0.0}
