"""论文解析器 — 正则回退 + LLM精炼, 公式合并到最近定理"""

import os, re, hashlib
from config import PAPERS_DIR

THM_RE = re.compile(
    r'(?:^|\n)\s*(THEOREM|Theorem|LEMMA|Lemma|COROLLARY|Corollary|'
    r'DEFINITION|Definition|PROPOSITION|Proposition)\s*(\d+(?:\.\d+)*)?\.?\s*',
    re.MULTILINE)
DISPLAY_RE = re.compile(r'\$\$\s*(.+?)\s*\$\$', re.DOTALL)
SECT_RE = re.compile(r'(?:^|\n)#{1,3}\s+')
PROOF_RE = re.compile(r'(?:^|\n)(?:Proof|PROOF)\.?\s')
REF_RE = re.compile(r'(?:^|\n)#{1,3}\s+REFERENCE', re.IGNORECASE)
TAG_FORMULA_RE = re.compile(r'\$\$\s*(.+?)\s*\\tag\s*\{(.+?)\}\s*\$\$', re.DOTALL)

TYPE_MAP = {'theorem':'theorem','lemma':'lemma','corollary':'corollary',
            'definition':'definition','proposition':'proposition'}

def _merge_formulas_into_theorems(theorem_items: list[dict], formula_items: list[dict]) -> list[dict]:
    """将公式合并到位置最近的定理中"""
    for fi in formula_items:
        fi['_formula_pos'] = fi.get('position', 0)

    # 按位置排序
    all_ordered = sorted(theorem_items + formula_items,
                         key=lambda x: x.get('position', x.get('_formula_pos', 0)))

    result = []
    current_theorem = None

    for item in all_ordered:
        if item.get('type') != 'formula':
            result.append(item)
            current_theorem = item
        else:
            # 合并到最近的定理
            if current_theorem is not None:
                formulas = current_theorem.setdefault('formulas', [])
                formulas.append(item['latex'])
                # 如果定理没有主latex, 使用第一个公式
                if not current_theorem.get('latex'):
                    current_theorem['latex'] = item['latex']

    return result

def parse_paper_regex(filepath: str) -> list[dict]:
    """正则解析: 定理提取 + 公式合并到最近定理"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    dirname = os.path.basename(os.path.dirname(filepath))
    pid = dirname.split('-')[0] if '-' in dirname else dirname

    boundaries = []
    for m in SECT_RE.finditer(content): boundaries.append(m.start())
    for m in PROOF_RE.finditer(content): boundaries.append(m.start())
    for m in REF_RE.finditer(content): boundaries.append(m.start())
    boundaries.sort()

    theorem_items = []
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

        theorem_items.append({
            'id': item_id, 'type': itype, 'number': num, 'name': name,
            'statement': statement[:2000], 'latex': latex,
            'formulas': formulas[1:] if len(formulas) > 1 else [],
            'premises': '', 'conclusion': '',
            'proof_technique': '', 'confidence': 0.5,
            'position': m.start()
        })

    # 带tag公式
    formula_items = []
    for i, m in enumerate(TAG_FORMULA_RE.finditer(content)):
        latex_str = m.group(1).strip()
        if len(latex_str) > 20:
            formula_items.append({
                'id': f"{pid}_eq_{i}", 'type': 'formula', 'number': m.group(2).strip(),
                'name': f"Eq ({m.group(2).strip()})",
                'statement': latex_str, 'latex': latex_str,
                'premises': '', 'conclusion': '',
                'proof_technique': '', 'confidence': 0.5,
                'position': m.start()
            })

    # 合并公式到定理
    return _merge_formulas_into_theorems(theorem_items, formula_items)

def parse_paper(filepath: str) -> tuple[dict, list[dict]]:
    """解析单篇论文 — 纯正则提取"""
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

def load_all_papers() -> tuple[list[dict], list[dict]]:
    papers, all_items = [], []
    for root, dirs, files in os.walk(PAPERS_DIR):
        for f in files:
            if f.endswith('.correction.md'):
                filepath = os.path.join(root, f)
                meta, items = parse_paper(filepath)
                papers.append(meta)
                all_items.extend(items)
                short_t = meta['title'][:50].encode('ascii', errors='replace').decode('ascii')
                n_theorems = sum(1 for it in items if it.get('type') != 'formula')
                n_formulas = sum(1 for it in items if it.get('type') == 'formula')
                print(f"  [{meta['year']}] {short_t} -> {n_theorems} thm + {n_formulas} eq")
    return papers, all_items
