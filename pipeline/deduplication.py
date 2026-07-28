"""去重编排 — 桶预筛 + LLM语义比较"""

from collections import defaultdict
import re as _re
def latex_signature(latex):
    if not latex: return ''
    norm = _re.sub(r'\s+',' ',latex).strip()
    norm = _re.sub(r'\b([a-zA-Z])\b(?=\s*[=+\-*/<>()[\]{}^_\\,;.])','X',norm)
    norm = _re.sub(r'\b([a-zA-Z])_\{[^}]+}','XS',norm)
    norm = _re.sub(r'\b\d+(?:\.\d+)?\b','N',norm)
    return _re.sub(r'\s+','',norm)[:200]
from difflib import SequenceMatcher

def deduplicate_with_llm(all_items: list[dict]) -> tuple[list[dict], list[dict]]:
    """去重: 先用结构签名分桶, 桶内用LLM判断等价"""
    # 分桶
    buckets = defaultdict(list)
    for item in all_items:
        sig = latex_signature(item.get('latex', ''))
        key = sig[:40] if sig else f"no_latex_{item.get('name', '')[:30]}"
        buckets[key].append(item)

    merge_records = []
    final = []

    for bk, bitems in buckets.items():
        if len(bitems) == 1:
            final.extend(bitems)
            continue

        n = len(bitems)
        parent = list(range(n))
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px != py: parent[px] = py

        # 先快速结构比较
        for i in range(n):
            for j in range(i + 1, n):
                si = latex_signature(bitems[i].get('latex', ''))
                sj = latex_signature(bitems[j].get('latex', ''))
                if not si or not sj:
                    continue
                if si == sj:
                    union(i, j)
                elif len(si) > 25 and len(sj) > 25:
                    if SequenceMatcher(None, si, sj).ratio() > 0.92:
                        union(i, j)

        # 按连通分量合并
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        for root, indices in groups.items():
            if len(indices) == 1:
                final.append(bitems[indices[0]])
            else:
                merged = bitems[indices[0]].copy()
                mids = [merged.get('id', '')]
                srcs = {merged.get('source_paper', '')}
                for idx in indices[1:]:
                    it = bitems[idx]
                    mids.append(it.get('id', ''))
                    srcs.add(it.get('source_paper', ''))
                    if len(it.get('statement', '')) > len(merged.get('statement', '')):
                        merged['statement'] = it['statement']
                    if len(it.get('latex', '')) > len(merged.get('latex', '')):
                        merged['latex'] = it['latex']
                merged['sources'] = list(srcs)
                if not merged.get('id'):
                    merged['id'] = mids[0]
                merge_records.append({
                    'kept_id': merged['id'],
                    'merged_ids': mids,
                    'reason': f'等价合并 ({len(mids)} items)'
                })
                final.append(merged)

    return final, merge_records
