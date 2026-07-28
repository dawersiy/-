"""关系发现编排 — 关键词预筛 + LLM pair scoring"""

from collections import defaultdict
from difflib import SequenceMatcher
from build_knowledge_graph import latex_signature

def discover_relations_with_llm(items: list[dict], max_pairs: int = 500) -> tuple[list[dict], list[dict]]:
    """智能关系发现: 优先用LLM, 回退到启发式"""

    # 构建关键词索引
    kw_index = defaultdict(set)
    for idx, item in enumerate(items):
        for kw in item.get('keywords', []):
            kw_index[kw].add(idx)

    relations = []
    rel_set = set()
    llm_count = 0

    for i, item_a in enumerate(items):
        type_a = item_a['type']
        kw_a = set(item_a.get('keywords', []))
        paper_a = item_a.get('source_paper', '') or (item_a.get('sources', [''])[0])
        year_a = item_a.get('source_year', '0')

        # 候选集: 共享>=2个关键词
        candidates = set()
        for kw in kw_a:
            candidates |= kw_index.get(kw, set())
        candidates.discard(i)

        for j in candidates:
            if j <= i:
                continue
            pair = (item_a.get('id', ''), items[j].get('id', ''))
            if pair in rel_set:
                continue

            type_b = items[j]['type']
            kw_b = set(items[j].get('keywords', []))
            common = kw_a & kw_b
            score = len(common)

            if score < 3:
                continue

            rel = None

            # LLM判断 (限制最多max_pairs对)
            if llm_count < max_pairs and score >= 4:
                try:
                    from llm.relations import discover_pair_relation
                    result = discover_pair_relation(item_a, items[j])
                    llm_count += 1
                    if result and result.get('type') != 'none' and result.get('confidence', 0) > 0.6:
                        rel = {
                            'type': result['type'],
                            'note': result.get('note', ''),
                            'confidence': result.get('confidence', 0.7)
                        }
                except Exception as e:
                    pass  # LLM失败, 回退到启发式

            # 启发式回退
            if rel is None:
                rel = heuristic_relation(item_a, items[j], type_a, type_b, score, common)

            if rel:
                rel_set.add(pair)
                item_a.setdefault('relations', []).append({
                    'target_id': items[j]['id'],
                    'type': rel['type'],
                    'note': rel.get('note', ''),
                    'confidence': rel.get('confidence', 0.6)
                })
                relations.append({
                    'source_id': item_a['id'],
                    'target_id': items[j]['id'],
                    'type': rel['type'],
                    'note': rel.get('note', ''),
                    'confidence': rel.get('confidence', 0.6)
                })

    print(f"  关系发现: {len(relations)}条 (其中LLM判断: {llm_count}对)")
    return items, relations

def heuristic_relation(item_a, item_b, type_a, type_b, score, common_kw):
    """启发式回退关系判断"""
    if type_a == 'theorem' and type_b == 'corollary':
        return {'type': 'derives', 'note': '定理推导出推论', 'confidence': 0.7}
    if type_a == 'lemma' and type_b == 'theorem' and score >= 3:
        return {'type': 'depends', 'note': '引理支撑定理', 'confidence': 0.6}
    if type_a == 'definition' and type_b in ('theorem', 'lemma', 'proposition') and score >= 2:
        return {'type': 'depends', 'note': '定义是理论基础', 'confidence': 0.6}
    if type_a == 'proposition' and type_b == 'theorem' and score >= 4:
        return {'type': 'depends', 'note': '命题支撑定理', 'confidence': 0.5}
    if type_a == 'formula' and type_b == 'formula':
        sig_a = latex_signature(item_a.get('latex', ''))
        sig_b = latex_signature(item_b.get('latex', ''))
        if sig_a == sig_b:
            return {'type': 'equivalent', 'note': '结构等价公式', 'confidence': 0.8}
    return None
