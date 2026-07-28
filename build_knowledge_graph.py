#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学知识图谱构建系统 — LLM增强版
===================================
8阶段流水线:
  [1] 解析论文 (LLM提取 + 正则回退)
  [2] 语义关键词 (LLM标签 + 领域分类)
  [3] 语义去重 (结构预筛 + LLM等价判断)
  [4] 中文摘要 (LLM生成1-3句摘要)
  [5] 智能关系 (关键词预筛 + LLM关系判断)
  [6] 组装网络
  [7] 预计算布局
  [8] 输出JSON + HTML

用法:
  python build_knowledge_graph.py              # 完整处理
  python build_knowledge_graph.py --no-llm     # 仅正则模式
  python build_knowledge_graph.py --incremental # 增量模式
"""

import os, sys, re, time, argparse
from collections import defaultdict

if sys.platform == 'win32':
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

from config import *
from schemas import KnowledgeItem, KnowledgeNetwork, Relation, NetworkStatistics
from pipeline.cache_manager import invalidate_cache
from pipeline.layout import compute_layout
from visualize.generator import generate_html, save_network_json

# 正则表达式
THM_RE = re.compile(
    r'(?:^|\n)\s*(THEOREM|Theorem|LEMMA|Lemma|COROLLARY|Corollary|'
    r'DEFINITION|Definition|PROPOSITION|Proposition)\s*(\d+(?:\.\d+)*)?\.?\s*',
    re.MULTILINE)
DISPLAY_RE = re.compile(r'\$\$\s*(.+?)\s*\$\$', re.DOTALL)
SECT_RE = re.compile(r'(?:^|\n)#{1,3}\s+')
PROOF_RE = re.compile(r'(?:^|\n)(?:Proof|PROOF)\.?\s')
REF_RE = re.compile(r'(?:^|\n)#{1,3}\s+REFERENCE', re.IGNORECASE)

def latex_signature(latex):
    """结构签名用于快速去重预筛"""
    if not latex: return ''
    norm = re.sub(r'\s+',' ',latex).strip()
    norm = re.sub(r'\b([a-zA-Z])\b(?=\s*[=+\-*/<>()[\]{}^_\\,;.])','X',norm)
    norm = re.sub(r'\b([a-zA-Z])_\{[^}]+}','XS',norm)
    norm = re.sub(r'\\[a-zA-Z]+','G',norm)
    norm = re.sub(r'\b\d+(?:\.\d+)?\b','N',norm)
    return re.sub(r'\s+','',norm)

# =============================================================================
# 第1阶段: 解析论文
# =============================================================================

def parse_papers(use_llm=True):
    """解析所有论文, 返回 (papers_meta, items)"""
    print("\n[1/8] 解析论文...")
    from pipeline.parser import parse_paper

    papers = []
    all_items = []
    for root, dirs, files in os.walk(PAPERS_DIR):
        for f in sorted(files):
            if f.endswith('.correction.md'):
                filepath = os.path.join(root, f)
                meta, items = parse_paper(filepath, use_llm=use_llm)
                papers.append(meta)
                all_items.extend(items)
                short = meta['title'][:55].encode('ascii', errors='replace').decode('ascii')
                print(f"  [{meta['year']}] {short} -> {len(items)} items")
    print(f"  共 {len(papers)} 篇论文, {len(all_items)} 原始items")

    # 过滤: 移除formula类型(已合并到定理中)
    formula_count = sum(1 for it in all_items if it.get('type') == 'formula')
    items = [it for it in all_items if it.get('type') != 'formula']
    print(f"  去除 {formula_count} 公式项, 保留 {len(items)} 定理/引理项")
    return papers, items

# =============================================================================
# 第2阶段: 关键词
# =============================================================================

def assign_keywords(items, use_llm=True):
    """语义关键词分配 (LLM或正则回退)"""
    print("\n[2/8] 分配关键词...")

    if use_llm:
        try:
            from llm.keywords import assign_keywords_llm
            for item in items:
                result = assign_keywords_llm(
                    item.get('name',''), item.get('type',''),
                    item.get('statement',''), item.get('latex',''))
                if result:
                    item['keywords'] = result.get('keywords', [item['type']])
                    item['domain'] = result.get('domain', [])
            print(f"  LLM关键词分配完成")
            return items
        except Exception as e:
            print(f"  LLM关键词失败: {e}, 回退到正则")

    # 正则回退
    kw_patterns = [
        (r'convex','convex'),(r'monotone','monotone'),(r'proximal','proximal_point'),
        (r'gradient','gradient'),(r'minimiz|optimiz','optimization'),(r'convergen','convergence'),
        (r'Hilbert','hilbert_space'),(r'Banach','banach_space'),(r'Lipschitz','lipschitz'),
        (r'dissipat','dissipative'),(r'inertial','inertial'),(r'accelerat','accelerated'),
        (r'splitting','splitting'),(r'operator','operator_theory'),(r'subdifferential','subdifferential'),
        (r'nonexpansive','nonexpansive'),(r'resolvent','resolvent'),(r'heavy.ball','heavy_ball'),
        (r'second.order','second_order'),(r'differential','differential_eq'),
        (r'variational','variational'),(r'Newton','newton'),(r'fixed.point','fixed_point'),
        (r'saddle','saddle_point'),(r'Lyapunov','lyapunov'),(r'Opial','opial'),
        (r'variable.metric','variable_metric'),(r'enlargement','enlargement'),
        (r'quasi','quasi'),(r'interior','interior_point'),(r'barrier','barrier'),
        (r'quadratic','quadratic'),(r'strongly.convex','strong_convexity'),
        (r'coercive','coercive'),(r'weak.convergence','weak_convergence'),
        (r'strong.convergence','strong_convergence'),(r'convergence.rate','convergence_rate'),
        (r'damping|friction','damping'),(r'energy','energy'),(r'duality|Fenchel|conjugate','duality'),
        (r'projection','projection'),(r'extragradient','extragradient'),
        (r'Douglas.Rachford','douglas_rachford'),(r'forward.backward','forward_backward'),
        (r'HPE|hybrid.proximal','hpe'),(r'Bregman','bregman'),(r'penalty|augmented','penalty'),
        (r'Lagrangian','lagrangian'),(r'regularization|Tikhonov','regularization'),
    ]
    for item in items:
        text = (item.get('statement','')+' '+item.get('latex','')+' '+
                item.get('name','')+' '+item.get('source_title','')).lower()
        kws = {item['type']}
        for pat, kw in kw_patterns:
            if re.search(pat, text): kws.add(kw)
        item['keywords'] = list(kws)[:12]
        item['domain'] = []
    print(f"  正则关键词分配完成")
    return items

# =============================================================================
# 第3阶段: 去重
# =============================================================================

def deduplicate(items, use_llm=True):
    """语义去重: 结构预筛 + LLM等价判断"""
    print("\n[3/8] 去重合并...")

    if use_llm:
        try:
            from pipeline.deduplication import deduplicate_with_llm
            merged, merge_records = deduplicate_with_llm(items)
            print(f"  合并后: {len(merged)} items, {len(merge_records)} 合并记录")
            return merged, merge_records
        except Exception as e:
            print(f"  LLM去重失败: {e}, 回退到结构模式")

    # 结构回退
    from collections import defaultdict
    from difflib import SequenceMatcher
    buckets = defaultdict(list)
    for item in items:
        sig = latex_signature(item.get('latex',''))
        buckets[sig[:40] if sig else 'nolx'].append(item)

    merge_records = []
    final = []
    for bk, bitems in buckets.items():
        if len(bitems) == 1:
            final.extend(bitems)
        else:
            n = len(bitems)
            parent = list(range(n))
            def find(x):
                while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
                return x
            def union(x,y):
                px,py=find(x),find(y)
                if px!=py: parent[px]=py

            for i in range(n):
                for j in range(i+1,n):
                    si = latex_signature(bitems[i].get('latex',''))
                    sj = latex_signature(bitems[j].get('latex',''))
                    if not si or not sj: continue
                    if si == sj: union(i,j)
                    elif len(si)>25 and len(sj)>25:
                        if SequenceMatcher(None,si,sj).ratio()>0.92: union(i,j)

            groups = defaultdict(list)
            for i in range(n): groups[find(i)].append(i)

            for root, indices in groups.items():
                if len(indices)==1:
                    final.append(bitems[indices[0]])
                else:
                    merged = bitems[indices[0]].copy()
                    mids = [merged.get('id','')]
                    srcs = {merged.get('source_paper','')}
                    for idx in indices[1:]:
                        it = bitems[idx]
                        mids.append(it.get('id',''))
                        srcs.add(it.get('source_paper',''))
                        if len(it.get('statement',''))>len(merged.get('statement','')):
                            merged['statement']=it['statement']
                        if len(it.get('latex',''))>len(merged.get('latex','')):
                            merged['latex']=it['latex']
                    merged['sources']=list(srcs)
                    merge_records.append({'kept_id':merged.get('id',''),'merged_ids':mids,
                        'reason':f'结构等价 ({len(mids)} items)'})
                    final.append(merged)

    print(f"  合并后: {len(final)} items, {len(merge_records)} 合并记录")
    return final, merge_records

# =============================================================================
# 第4阶段: LaTeX公式渲染
# =============================================================================

def render_formulas(items):
    """使用本地TeXLive将所有LaTeX渲染为SVG"""
    print("\n[4/8] 渲染LaTeX公式为SVG...")
    try:
        from pipeline.latex_renderer import render_latex_svg
        count = 0
        for item in items:
            all_latex = []
            if item.get('latex'):
                all_latex.append(item['latex'])
            for f in item.get('formulas', []):
                if f not in all_latex:
                    all_latex.append(f)

            svgs = {}
            for lx in all_latex:
                svg = render_latex_svg(lx)
                if svg:
                    svgs[lx] = svg
                    count += 1
            if svgs:
                item['_svgs'] = svgs

        print(f"  渲染了 {count} 个SVG公式")
    except Exception as e:
        print(f"  SVG渲染跳过: {e}")
    return items

# =============================================================================
# 第5阶段: 中文摘要
# =============================================================================

def generate_summaries(items, use_llm=True):
    """为每个item生成1-3句中文摘要"""
    print("\n[4/8] 生成中文摘要...")

    if use_llm:
        try:
            from llm.summarizer import summarize_item
            count = 0
            for item in items:
                if not item.get('summary'):
                    summary = summarize_item(
                        item.get('name',''), item.get('type',''),
                        item.get('statement',''), item.get('latex',''))
                    if summary:
                        item['summary'] = summary
                        count += 1
            print(f"  生成了 {count} 条摘要")
            return items
        except Exception as e:
            print(f"  LLM摘要失败: {e}")
    print(f"  跳过摘要生成")
    return items

# =============================================================================
# 第5阶段: 关系发现
# =============================================================================

def discover_relations(items, use_llm=True):
    """智能关系发现"""
    print("\n[5/8] 发现关系...")

    if use_llm:
        try:
            from pipeline.relations import discover_relations_with_llm
            items, relations = discover_relations_with_llm(items, max_pairs=300)
            return items, relations
        except Exception as e:
            print(f"  LLM关系发现失败: {e}, 回退到启发式")

    # 启发式回退
    from pipeline.relations import discover_relations_with_llm as heuristic_discover
    items, relations = heuristic_discover(items, max_pairs=0)
    return items, relations

# =============================================================================
# 第6阶段: 组装网络
# =============================================================================

def build_network(papers, items, merge_records, relations):
    """组装KnowledgeNetwork"""
    print("\n[6/8] 组装知识网络...")

    std_items = []
    for it in items:
        # 清理内部字段
        it.pop('source_paper', None)
        it.pop('source_year', None)
        it.pop('source_title', None)
        it.pop('_idx', None)
        it.pop('chunk_index', None)

        std_item = {
            'id': it.get('id',''),
            'type': it.get('type',''),
            'name': it.get('name',''),
            'latex': it.get('latex',''),
            'statement': it.get('statement',''),
            'sources': it.get('sources', [it.get('id','').split('_')[0]]),
            'keywords': it.get('keywords',[]),
            'relations': it.get('relations',[]),
            # 增强字段
            'summary': it.get('summary',''),
            'premises': it.get('premises',''),
            'conclusion': it.get('conclusion',''),
            'domain': it.get('domain',[]),
            'confidence': it.get('confidence',0.0),
            'proof_technique': it.get('proof_technique',''),
            # 公式子项
            'formulas': it.get('formulas', []),
            '_svgs': it.get('_svgs', {}),
        }
        std_items.append(std_item)

    tc = defaultdict(int)
    for it in std_items: tc[it['type']] += 1
    rtc = defaultdict(int)
    for r in relations: rtc[r['type']] += 1

    network = {
        'network_name': 'Optimization Theory & Proximal Algorithms Knowledge Network',
        'description': 'LLM-enhanced knowledge network from 27 optimization theory papers',
        'statistics': {
            'total_papers': len(papers),
            'total_items': len(std_items),
            'total_relations': len(relations),
            'items_by_type': dict(tc),
            'relations_by_type': dict(rtc),
            'merge_count': len(merge_records)
        },
        'papers': [{'id':p['id'],'title':p['title'],'year':p['year']} for p in papers],
        'items': std_items,
        'merge_records': merge_records,
        'relations_summary': relations
    }
    return network

# =============================================================================
# 第7阶段: 布局
# =============================================================================

def compute_graph_layout(network):
    """预计算力导向布局"""
    print("\n[7/8] 预计算布局...")
    items = network['items']
    relations = network['relations_summary']

    # 构建id→index映射
    id_to_idx = {}
    for idx, item in enumerate(items):
        id_to_idx[item['id']] = idx

    # 构建links (with index)
    links_with_idx = []
    for rel in relations:
        si = id_to_idx.get(rel.get('source_id',''))
        ti = id_to_idx.get(rel.get('target_id',''))
        if si is not None and ti is not None:
            links_with_idx.append({'source_index': si, 'target_index': ti,
                                    'type': rel.get('type','')})

    # 预计算坐标
    items = compute_layout(items, links_with_idx)
    network['items'] = items
    print(f"  布局完成: {len(items)} 节点")
    return network

# =============================================================================
# 第8阶段: 输出
# =============================================================================

def output_results(network):
    """保存JSON和HTML"""
    print("\n[8/8] 生成输出...")
    save_network_json(network)
    generate_html(network)

# =============================================================================
# 主入口
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='数学知识图谱构建系统')
    parser.add_argument('--no-llm', action='store_true', help='禁用LLM, 仅使用正则回退')
    parser.add_argument('--no-cache', action='store_true', help='清除LLM缓存并重新计算')
    parser.add_argument('--llm-only', type=str, default='',
                        help='仅运行指定LLM阶段: extract,keywords,dedup,summarize,relations')
    args = parser.parse_args()

    use_llm = not args.no_llm

    if use_llm:
        api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not api_key:
            print("警告: ANTHROPIC_API_KEY 未设置, 将使用正则回退模式")
            use_llm = False

    if args.no_cache:
        print("清除LLM缓存...")
        invalidate_cache()

    print("=" * 60)
    print("数学知识图谱构建系统 (LLM增强版)" if use_llm else "数学知识图谱构建系统 (正则模式)")
    print("=" * 60)

    t0 = time.time()

    # [1] 解析
    papers, items = parse_papers(use_llm=use_llm)

    # [2] 关键词
    items = assign_keywords(items, use_llm=use_llm)

    # [3] 去重
    items, merge_records = deduplicate(items, use_llm=use_llm)

    # [4] 摘要
    items = generate_summaries(items, use_llm=use_llm)

    # [5] 关系
    items, relations = discover_relations(items, use_llm=use_llm)

    # [6] 组装
    network = build_network(papers, items, merge_records, relations)

    # [7] 布局
    network = compute_graph_layout(network)

    # [8] 输出
    output_results(network)

    elapsed = time.time() - t0
    stats = network['statistics']
    print("\n" + "=" * 60)
    print(f"✅ 完成! 耗时: {elapsed:.1f}s")
    print(f"  论文: {stats['total_papers']} | Items: {stats['total_items']} | 关系: {stats['total_relations']}")
    for t, c in sorted(stats['items_by_type'].items()):
        print(f"    {t}: {c}")
    print(f"\n  输出: {OUTPUT_JSON}")
    print(f"  可视化: {OUTPUT_HTML}")
    print(f"  启动HTTP服务器查看: python -m http.server 8000")

if __name__ == '__main__':
    main()
