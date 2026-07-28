"""论文解析器 — 正则回退 + LLM精炼, 支持增量处理"""

import os, re, hashlib
from config import PAPERS_DIR
from pipeline.cache_manager import get_cache, set_cache

# ---- 正则回退解析 (从原build_knowledge_graph.py移植) ----
THM_RE = re.compile(
    r'(?:^|\n)\s*(THEOREM|Theorem|LEMMA|Lemma|COROLLARY|Corollary|'
    r'DEFINITION|Definition|PROPOSITION|Proposition)\s*(\d+(?:\.\d+)*)?\.?\s*',
    re.MULTILINE)
DISPLAY_RE = re.compile(r'\$\$\s*(.+?)\s*\$\$', re.DOTALL)
SECT_RE = re.compile(r'(?:^|\n)#{1,3}\s+')
PROOF_RE = re.compile(r'(?:^|\n)(?:Proof|PROOF)\.?\s')
REF_RE = re.compile(r'(?:^|\n)#{1,3}\s+REFERENCE', re.IGNORECASE)

TYPE_MAP = {'theorem':'theorem','lemma':'lemma','corollary':'corollary',
            'definition':'definition','proposition':'proposition'}

def parse_paper_regex(filepath: str) -> list[dict]:
    """正则回退解析 (旧版逻辑, 用于LLM不可用时)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    dirname = os.path.basename(os.path.dirname(filepath))
    pid = dirname.split('-')[0] if '-' in dirname else dirname

    boundaries = []
    for m in SECT_RE.finditer(content): boundaries.append(m.start())
    for m in PROOF_RE.finditer(content): boundaries.append(m.start())
    for m in REF_RE.finditer(content): boundaries.append(m.start())
    boundaries.sort()

    items = []
    for i, m in enumerate(THM_RE.finditer(content)):
        itype = TYPE_MAP.get(m.group(1).lower(), 'theorem')
        num = m.group(2) or ''
        name = f"{itype.capitalize()} {num}".strip()
        item_id = f"{pid}_{itype}_{num}" if num else f"{pid}_{itype}_{i}"
        start = m.end()
        end = len(content)
        for b in boundaries:
            if b > start: end = b; break
        statement = content[start:end].strip()[:3000]
        formulas = [f.strip() for f in DISPLAY_RE.findall(statement)]
        latex = formulas[0] if formulas else ''

        items.append({
            'id': item_id, 'type': itype, 'number': num, 'name': name,
            'statement': statement[:2000], 'latex': latex,
            'premises': '', 'conclusion': '',
            'proof_technique': '', 'confidence': 0.5
        })

    # Tagged formulas
    for i, m in enumerate(re.finditer(r'\$\$\s*(.+?)\s*\\tag\s*\{(.+?)\}\s*\$\$', content, re.DOTALL)):
        latex_str = m.group(1).strip()
        if len(latex_str) > 20:
            tag = m.group(2).strip()
            items.append({
                'id': f"{pid}_eq_{i}", 'type': 'formula', 'number': tag,
                'name': f"Eq ({tag})",
                'statement': latex_str, 'latex': latex_str,
                'premises': '', 'conclusion': '',
                'proof_technique': '', 'confidence': 0.5
            })
    return items

# ---- LLM增强解析 ----

def parse_paper_llm(filepath: str) -> list[dict]:
    """LLM优先解析, 失败时回退到正则"""
    from llm.extractor import extract_from_paper

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取标题和年份
    title = ''
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m: title = m.group(1).strip()

    dirname = os.path.basename(os.path.dirname(filepath))
    pid = dirname.split('-')[0] if '-' in dirname else dirname
    year = pid[:4]

    meta = {'id': pid, 'title': title, 'year': year}

    # 尝试LLM提取
    try:
        llm_items = extract_from_paper(content, pid)
        if llm_items:
            # 给每个item附加来源信息和ID
            for i, item in enumerate(llm_items):
                num = item.get('number', '')
                itype = item.get('type', 'theorem')
                if not item.get('id'):
                    item['id'] = f"{pid}_{itype}_{num}" if num else f"{pid}_{itype}_llm_{i}"
                item['source_paper'] = pid
                item['source_year'] = year
                item['source_title'] = title
            return meta, llm_items
    except Exception as e:
        print(f"  LLM提取失败 ({pid}): {e}, 使用正则回退")

    # 回退到正则
    regex_items = parse_paper_regex(filepath)
    for item in regex_items:
        item['source_paper'] = pid
        item['source_year'] = year
        item['source_title'] = title
    return meta, regex_items

def parse_paper(filepath: str, use_llm: bool = True) -> tuple[dict, list[dict]]:
    """解析单篇论文, 返回 (meta, items)"""
    if use_llm:
        return parse_paper_llm(filepath)
    else:
        # 仅正则模式
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        title = ''
        m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if m: title = m.group(1).strip()
        dirname = os.path.basename(os.path.dirname(filepath))
        pid = dirname.split('-')[0] if '-' in dirname else dirname
        year = pid[:4]
        meta = {'id': pid, 'title': title, 'year': year}
        items = parse_paper_regex(filepath)
        for item in items:
            item['source_paper'] = pid
            item['source_year'] = year
            item['source_title'] = title
        return meta, items

def load_all_papers(use_llm: bool = True) -> tuple[list[dict], list[dict]]:
    """加载全部论文, 返回 (papers_meta, all_items)"""
    papers = []
    all_items = []

    for root, dirs, files in os.walk(PAPERS_DIR):
        for f in files:
            if f.endswith('.correction.md'):
                filepath = os.path.join(root, f)
                meta, items = parse_paper(filepath, use_llm=use_llm)
                papers.append(meta)
                all_items.extend(items)
                short_t = meta['title'][:50].encode('ascii', errors='replace').decode('ascii')
                print(f"  [{meta['year']}] {short_t} -> {len(items)} items")

    return papers, all_items

def compute_paper_hash(filepath: str) -> str:
    """计算论文内容的SHA256哈希"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return hashlib.sha256(f.read().encode()).hexdigest()[:16]
