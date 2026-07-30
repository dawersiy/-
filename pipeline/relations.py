"""关系发现 — 多策略启发式, 高连通性"""

from collections import defaultdict
from difflib import SequenceMatcher
import re as _re

def latex_signature(latex):
    if not latex: return ''
    norm = _re.sub(r'\s+',' ',latex).strip()
    norm = _re.sub(r'\b([a-zA-Z])\b(?=\s*[=+\-*/<>()[\]{}^_\\,;.])','X',norm)
    norm = _re.sub(r'\b([a-zA-Z])_\{[^}]+}','XS',norm)
    norm = _re.sub(r'\b\d+(?:\.\d+)?\b','N',norm)
    return _re.sub(r'\s+','',norm)[:200]

# 收敛相关的结论关键词
CONVERGENCE_KW = {'convergence','convergence_rate','weak_convergence','strong_convergence',
                   'linear_convergence','converges','limit'}

def discover_relations(items: list[dict]) -> tuple[list[dict], list[dict]]:
    """多策略关系发现 — 降低阈值, 扩展匹配"""

    # 关键词索引
    kw_index = defaultdict(set)
    for idx, item in enumerate(items):
        for kw in item.get('keywords', []):
            kw_index[kw].add(idx)

    relations = []
    rel_set = set()

    for i, item_a in enumerate(items):
        type_a = item_a['type']
        kw_a = set(item_a.get('keywords', []))
        paper_a = (item_a.get('source_paper','') or item_a.get('sources',[''])[0])
        year_a = item_a.get('source_year','0')
        name_a = item_a.get('name','')

        # 候选集: 共享>=1个关键词 (降低阈值)
        candidates = set()
        for kw in kw_a:
            candidates |= kw_index.get(kw, set())
        candidates.discard(i)

        for j in candidates:
            if j <= i: continue
            item_b = items[j]
            pair = (item_a.get('id',''), item_b.get('id',''))
            if pair in rel_set: continue

            type_b = item_b['type']
            kw_b = set(item_b.get('keywords', []))
            common = kw_a & kw_b
            score = len(common)
            paper_b = (item_b.get('source_paper','') or item_b.get('sources',[''])[0])
            year_b = item_b.get('source_year','0')
            name_b = item_b.get('name','')

            # 至少共享2个关键词 (不包含类型自身)
            non_type_common = common - {type_a, type_b}
            if len(non_type_common) < 2: continue

            rel = _detect_relation(
                item_a, item_b, type_a, type_b, score, common,
                paper_a, paper_b, year_a, year_b, name_a, name_b)

            if rel:
                rel_set.add(pair)
                item_a.setdefault('relations', []).append({
                    'target_id': item_b['id'],
                    'type': rel['type'], 'note': rel.get('note',''),
                    'confidence': rel.get('confidence', 0.6)
                })
                relations.append({
                    'source_id': item_a['id'], 'target_id': item_b['id'],
                    'type': rel['type'], 'note': rel.get('note',''),
                    'confidence': rel.get('confidence', 0.6)
                })

    # 统计
    rtc = defaultdict(int)
    for r in relations: rtc[r['type']] += 1
    rpt = ', '.join(f'{k}:{v}' for k,v in sorted(rtc.items()))
    print(f"  关系发现: {len(relations)}条 ({rpt})")
    return items, relations


def _detect_relation(a, b, ta, tb, score, common, pa, pb, ya, yb, na, nb):
    """检测两个item之间的关系"""
    stmt_a = a.get('statement','').lower()
    stmt_b = b.get('statement','').lower()
    latex_a = a.get('latex','')
    latex_b = b.get('latex','')
    sig_a = latex_signature(latex_a)
    sig_b = latex_signature(latex_b)
    same_paper = (pa == pb)

    # ====== derives (推导) ======
    if ta == 'theorem' and tb == 'corollary':
        return {'type':'derives','note':'定理推导出推论','confidence':0.8}
    if ta == 'lemma' and tb == 'corollary' and score >= 3:
        return {'type':'derives','note':'引理支撑推论','confidence':0.65}
    if ta == 'proposition' and tb == 'corollary' and score >= 3:
        return {'type':'derives','note':'命题推导推论','confidence':0.65}

    # ====== depends (依赖) ======
    # lemma支撑theorem/proposition (核心关系)
    if ta == 'lemma' and tb in ('theorem','proposition') and score >= 3:
        return {'type':'depends','note':f'引理{na}支撑{_type_cn(tb)}{nb}','confidence':0.7}
    # definition是基础
    if ta == 'definition' and tb in ('theorem','lemma','proposition','corollary') and score >= 2:
        return {'type':'depends','note':f'定义是{_type_cn(tb)}基础','confidence':0.7}
    # proposition支撑theorem
    if ta == 'proposition' and tb == 'theorem' and score >= 3:
        return {'type':'depends','note':'命题支撑定理','confidence':0.6}
    # 同论文lemma→lemma链 (仅相邻编号)
    if ta == 'lemma' and tb == 'lemma' and same_paper and score >= 2:
        num_a = _extract_number(na); num_b = _extract_number(nb)
        if num_a and num_b and num_b[0] == num_a[0] + 1:
            return {'type':'depends','note':f'引理链: {na}→{nb}','confidence':0.5}
    # 引用关系
    if na and na in stmt_b and score >= 3:
        return {'type':'depends','note':f'{nb}引用{na}','confidence':0.6}

    # ====== equivalent (等价) ======
    # 同类型, 跨论文, 同名编号
    if ta == tb and not same_paper and na == nb and na and score >= 3:
        return {'type':'equivalent','note':f'同编号{na},跨论文','confidence':0.65}
    # LaTeX结构高度相似
    if sig_a and sig_b and len(sig_a)>30 and len(sig_b)>30:
        sim = SequenceMatcher(None, sig_a, sig_b).ratio()
        if sim > 0.92:
            return {'type':'equivalent','note':f'公式相似({sim:.0%})','confidence':sim}
    # 共享5+关键词 + 同类型
    if ta == tb and score >= 5:
        return {'type':'equivalent','note':f'高重叠{score}词','confidence':0.5}

    # ====== generalizes (推广) ======
    # 同类型, 跨论文, 后来推广
    if ta == tb and ta in ('theorem','lemma','proposition') and not same_paper and score >= 4:
        if ya != yb and ya != '0' and yb != '0' and int(ya) < int(yb):
            return {'type':'generalizes','note':f'{ya}→{yb}推广','confidence':0.55}

    # ====== 回退: 强主题相关 ======
    if score >= 5:
        return {'type':'depends','note':f'强相关({score}词)','confidence':0.35}

    return None


def _type_cn(t):
    m = {'theorem':'定理','lemma':'引理','corollary':'推论','definition':'定义','proposition':'命题'}
    return m.get(t, t)

def _extract_number(name):
    """从名称中提取数字: Theorem 2.1 -> (2,1)"""
    import re
    m = re.search(r'(\d+(?:\.\d+)?)', name)
    if m:
        parts = m.group(1).split('.')
        return tuple(int(p) for p in parts)
    return None
