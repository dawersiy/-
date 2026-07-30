#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学知识图谱构建系统
====================
纯本地处理: Claude Code 做文献分析, 正则引擎做结构化提取,
去重→关系→布局→可视化 全本地完成。

用法:
  python build_graph.py          # 完整构建
  python build_graph.py --paper  # 仅解析论文 (供 Claude Code 分析)
"""

import os, sys, re, time, argparse
from collections import defaultdict
from difflib import SequenceMatcher

if sys.platform == 'win32':
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

from config import *
from pipeline.parser import parse_paper_regex, load_all_papers
from pipeline.layout import compute_layout
from visualize.generator import generate_html, save_network_json

# ============================================================================
# LaTeX 结构签名 (去重用)
# ============================================================================
def latex_signature(latex):
    """结构签名: 保留关键数学结构, 仅替换变量名和数字"""
    if not latex: return ''
    norm = re.sub(r'\s+', ' ', latex).strip()
    # 替换单字母变量 (但保留关键运算符上下文)
    norm = re.sub(r'\b([a-zA-Z])\b(?=\s*[=+\-*/<>()[\]{}^_\\,;.])', 'X', norm)
    # 替换带下标变量
    norm = re.sub(r'\b([a-zA-Z])_\{[^}]+}', 'XS', norm)
    # 替换数字
    norm = re.sub(r'\b\d+(?:\.\d+)?\b', 'N', norm)
    # 保留前100字符的详细签名 (而非全部压缩为G)
    return re.sub(r'\s+', '', norm)[:200]

# ============================================================================
# 关键词 (正则)
# ============================================================================
KW = [
    (r'convex','convex'),(r'monotone','monotone'),(r'proximal','proximal'),
    (r'gradient','gradient'),(r'minimiz|optimiz','optimization'),(r'convergen','convergence'),
    (r'Hilbert','hilbert'),(r'Banach','banach'),(r'Lipschitz','lipschitz'),
    (r'dissipat','dissipative'),(r'inertial','inertial'),(r'accelerat','accelerated'),
    (r'splitting','splitting'),(r'operator','operator'),(r'subdifferential','subdifferential'),
    (r'nonexpansive','nonexpansive'),(r'resolvent','resolvent'),
    (r'variational','variational'),(r'Newton','newton'),(r'fixed.point','fixed_point'),
    (r'saddle','saddle_point'),(r'Lyapunov','lyapunov'),(r'Opial','opial'),
    (r'variable.metric','variable_metric'),(r'enlargement','enlargement'),
    (r'interior','interior_point'),(r'quadratic','quadratic'),
    (r'strongly.convex','strong_convexity'),(r'coercive','coercive'),
    (r'convergence.rate','convergence_rate'),(r'damping|friction','damping'),
    (r'duality|Fenchel|conjugate','duality'),(r'projection','projection'),
    (r'extragradient','extragradient'),(r'Douglas.Rachford','douglas_rachford'),
    (r'forward.backward','forward_backward'),(r'Bregman','bregman'),
    (r'Lagrangian','lagrangian'),(r'regularization|Tikhonov','regularization'),
]

def assign_keywords(items):
    for item in items:
        text = (item.get('statement','')+' '+item.get('latex','')+' '+
                item.get('name','')+' '+item.get('source_title','')).lower()
        kws = {item['type']}
        for pat, kw in KW:
            if re.search(pat, text): kws.add(kw)
        item['keywords'] = list(kws)[:12]
        item.setdefault('domain', [])
    return items

# ============================================================================
# 去重 (结构签名)
# ============================================================================
def deduplicate(items):
    buckets = defaultdict(list)
    for item in items:
        sig = latex_signature(item.get('latex',''))
        key = sig[:40] if sig else f"nl_{item.get('name','')[:30]}"
        buckets[key].append(item)

    merge_records, final = [], []
    for bk, bitems in buckets.items():
        if len(bitems) == 1:
            final.extend(bitems); continue

        n = len(bitems)
        parent, groups = list(range(n)), defaultdict(list)
        def find(x):
            while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
            return x
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py: parent[px]=py

        for i in range(n):
            for j in range(i+1,n):
                # 同论文的不同编号项不合并
                ni, nj = bitems[i].get('name',''), bitems[j].get('name','')
                pi = bitems[i].get('source_paper','') or bitems[i].get('sources',[''])[0]
                pj = bitems[j].get('source_paper','') or bitems[j].get('sources',[''])[0]
                if pi == pj and ni != nj:
                    continue
                si, sj = latex_signature(bitems[i].get('latex','')), latex_signature(bitems[j].get('latex',''))
                if not si or not sj: continue
                if si == sj: union(i,j)
                elif len(si)>25 and len(sj)>25 and SequenceMatcher(None,si,sj).ratio()>0.92: union(i,j)

        for i in range(n): groups[find(i)].append(i)

        for root, indices in groups.items():
            if len(indices)==1:
                final.append(bitems[indices[0]])
            else:
                m = bitems[indices[0]].copy()
                mids, srcs = [m['id']], {m.get('source_paper','')}
                for idx in indices[1:]:
                    it = bitems[idx]; mids.append(it['id']); srcs.add(it.get('source_paper',''))
                    if len(it.get('statement',''))>len(m.get('statement','')): m['statement']=it['statement']
                    if len(it.get('latex',''))>len(m.get('latex','')): m['latex']=it['latex']
                m['sources']=list(srcs)
                merge_records.append({'kept_id':m['id'],'merged_ids':mids,'reason':f'结构等价({len(mids)}项)'})
                final.append(m)

    return final, merge_records

# ============================================================================
# 关系发现
# ============================================================================
def discover_relations(items):
    from pipeline.relations import discover_relations as _dr
    return _dr(items)

# ============================================================================
# 组装网络
# ============================================================================
def build_network(papers, items, merge_records, relations):
    std_items = []
    for it in items:
        it.pop('_idx',None); it.pop('source_paper',None)
        it.pop('source_year',None); it.pop('source_title',None)
        it.pop('chunk_index',None); it.pop('position',None)
        std_items.append({
            'id':it.get('id',''),'type':it.get('type',''),'name':it.get('name',''),
            'latex':it.get('latex',''),'statement':it.get('statement',''),
            'sources':it.get('sources',[it.get('id','').split('_')[0]]),
            'keywords':it.get('keywords',[]),'relations':it.get('relations',[]),
            'summary':it.get('summary',''),'premises':it.get('premises',''),
            'conclusion':it.get('conclusion',''),'domain':it.get('domain',[]),
            'confidence':it.get('confidence',0.0),'proof_technique':it.get('proof_technique',''),
            'formulas':it.get('formulas',[]),
        })

    tc, rtc = defaultdict(int), defaultdict(int)
    for it in std_items: tc[it['type']]+=1
    for r in relations: rtc[r['type']]+=1

    return {
        'network_name':'Optimization Theory Knowledge Network',
        'description':'From classic optimization papers — built with Claude Code + regex pipeline',
        'statistics':{'total_papers':len(papers),'total_items':len(std_items),
            'total_relations':len(relations),'items_by_type':dict(tc),
            'relations_by_type':dict(rtc),'merge_count':len(merge_records)},
        'papers':[{'id':p['id'],'title':p['title'],'year':p['year']} for p in papers],
        'items':std_items,'merge_records':merge_records,'relations_summary':relations
    }

# ============================================================================
# 主入口
# ============================================================================
def main():
    parser = argparse.ArgumentParser(description='数学知识图谱构建')
    parser.add_argument('--paper', type=str, default='', help='解析单篇论文并输出JSON')
    parser.add_argument('--export', type=str, default='', help='导出原始items到JSON (供Claude Code分析)')
    parser.add_argument('--enrich', type=str, default='', help='加载Claude Code富化后的items JSON')
    args = parser.parse_args()

    # 单篇论文模式
    if args.paper:
        filepath = args.paper
        items = parse_paper_regex(filepath)
        assign_keywords(items)
        import json
        print(json.dumps(items, ensure_ascii=False, indent=2))
        return

    # 导出模式: 输出所有原始items供Claude Code处理
    if args.export:
        print("导出原始items...")
        papers, items = load_all_papers()
        items = [it for it in items if it.get('type')!='formula']
        items = assign_keywords(items)
        # 只导出关键字段
        export = [{'id':it['id'],'type':it['type'],'name':it['name'],
                   'latex':it.get('latex','')[:500],'statement':it.get('statement','')[:1000],
                   'keywords':it.get('keywords',[]),'source_paper':it.get('source_paper','')}
                  for it in items]
        with open(args.export, 'w', encoding='utf-8') as f:
            json.dump(export, f, ensure_ascii=False, indent=2)
        print(f"  已导出 {len(export)} items → {args.export}")
        return

    # 加载Claude Code富化数据
    enriched = {}
    if args.enrich:
        with open(args.enrich, 'r', encoding='utf-8') as f:
            enriched_data = json.load(f)
        for it in enriched_data:
            if it.get('id'):
                enriched[it['id']] = it
        print(f"  加载了 {len(enriched)} 条Claude Code富化数据")

    print("="*60)
    mode = "Claude Code增强" if enriched else "Regex"
    print(f"数学知识图谱构建 ({mode})")
    print("="*60)
    t0 = time.time()

    # [1] 解析
    print("\n[1/6] 解析论文...")
    papers, items = load_all_papers()
    n_f = sum(1 for it in items if it.get('type')=='formula')
    items = [it for it in items if it.get('type')!='formula']
    print(f"  共 {len(papers)} 篇, {len(items)} 项 (去除 {n_f} 公式)")

    # 合并Claude Code富化数据 (Claude Code为权威来源, 完全替换字段)
    if enriched:
        for it in items:
            eid = it.get('id','')
            if eid in enriched:
                e = enriched[eid]
                # Claude Code字段完全替换正则结果
                for key in ('keywords','domain','summary','premises','conclusion',
                           'proof_technique','confidence','name','statement','latex'):
                    if e.get(key):
                        it[key] = e[key]
        print(f"  Claude Code富化: {len(enriched)} 项已权威替换")

    # [2] 关键词 (正则回退)
    print("\n[2/6] 关键词...")
    for it in items:
        if not it.get('keywords'):
            it['keywords'] = [it['type']]
    items = assign_keywords(items)

    # [2.5] Claude Code 自动富化 (如有API Key)
    if not args.enrich:  # 未手动指定enrich文件时, 自动尝试Claude API
        try:
            from pipeline.enricher import enrich_items
            print("\n[2.5/6] Claude Code 自动富化...")
            items = enrich_items(items)
        except Exception as e:
            print(f"  Claude富化跳过: {e}")

    # [3] 去重
    print("\n[3/7] 去重...")
    items, merge_records = deduplicate(items)
    print(f"  合并后: {len(items)} 项, {len(merge_records)} 合并")

    # [4] 关系
    print("\n[4/6] 关系发现...")
    items, relations = discover_relations(items)

    # [5] 组装 + 布局
    print("\n[5/6] 组装 + 布局...")
    network = build_network(papers, items, merge_records, relations)

    # 准备布局数据: 关系链接 + 同论文链接(低权重)
    id_to_idx = {it['id']: i for i, it in enumerate(network['items'])}
    layout_links = []
    for rel in relations:
        si, ti = id_to_idx.get(rel.get('source_id','')), id_to_idx.get(rel.get('target_id',''))
        if si is not None and ti is not None:
            layout_links.append({'source_index': si, 'target_index': ti,
                                 'type': rel.get('type',''), 'weight': 1.0})

    # 同论文节点加低权重边 (让同论文的节点轻微聚拢)
    paper_groups = {}
    for i, it in enumerate(network['items']):
        for src in it.get('sources', []):
            paper_groups.setdefault(src, []).append(i)
    sp_count = 0
    for pid, indices in paper_groups.items():
        for a in range(len(indices)):
            for b in range(a+1, min(a+6, len(indices))):  # 每节点最多连5个同论文节点
                layout_links.append({'source_index': indices[a], 'target_index': indices[b],
                                     'type': 'same_paper', 'weight': 0.15})
                sp_count += 1
    print(f"  关系边: {len(relations)}, 同论文边: {sp_count}")

    network['items'] = compute_layout(network['items'], layout_links)
    print(f"  布局完成: {len(network['items'])} 节点")

    # [6] 输出
    print("\n[6/6] 输出...")
    save_network_json(network)
    generate_html(network)

    elapsed = time.time()-t0
    s = network['statistics']
    print(f"\n{'='*60}")
    print(f"✅ {elapsed:.1f}s | {s['total_papers']} papers | {s['total_items']} items | {s['total_relations']} relations")
    for t,c in sorted(s['items_by_type'].items()): print(f"  {t}: {c}")
    print(f"\n  {OUTPUT_JSON}")
    print(f"  {OUTPUT_HTML}")

if __name__ == '__main__':
    main()
