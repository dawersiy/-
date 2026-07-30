"""论文解析器 — 多阶段提取算法 v2"""

import os, re
from config import PAPERS_DIR

# ============================================================================
# 阶段0: 定义正则模式
# ============================================================================

# 定理声明: 行首 + TYPE + 编号 + 可选的句点
THM_DECLARE = re.compile(
    r'(?:^|\n)[ \t]*(THEOREM|Theorem|LEMMA|Lemma|COROLLARY|Corollary|'
    r'DEFINITION|Definition|PROPOSITION|Proposition)[ \t]+(\d+(?:\.\d+)*)\.?\s',
    re.MULTILINE)

# 定理无编号: 行首 + TYPE (无编号)
THM_UNNUMBERED = re.compile(
    r'(?:^|\n)[ \t]*(THEOREM|Theorem|LEMMA|Lemma|COROLLARY|Corollary|'
    r'DEFINITION|Definition|PROPOSITION|Proposition)\.?\s*\n',
    re.MULTILINE)

# 引用模式: 前面有特定词 或 后面紧跟逗号/页码 → 这是引用不是声明
CITATION_BEFORE = re.compile(
    r'(?:by|using|from|see|in|of|applying|to|and)\s+$', re.IGNORECASE)
CITATION_AFTER = re.compile(r'^[,\s]*p\.?\s*\d|^[,\s]*\[|^[,\s]*\(see')

# Proof/证明标记
PROOF_START = re.compile(r'(?:^|\n)\s*(?:Proof|PROOF)\.?\s')

# 公式提取
DISPLAY_MATH = re.compile(r'\$\$\s*(.+?)\s*\$\$', re.DOTALL)
INLINE_MATH = re.compile(r'(?<!\$)\$(?!\$)([^$]+?)\$(?!\$)', re.DOTALL)
TAG_FORMULA = re.compile(r'\$\$\s*(.+?)\s*\\tag\s*\{(.+?)\}\s*\$\$', re.DOTALL)

# 节标题 / 参考文献
SECTION = re.compile(r'(?:^|\n)#{1,3}\s+')
REFERENCES = re.compile(r'(?:^|\n)#{1,3}\s+REFERENCE', re.IGNORECASE)

# 类型映射
TYPE_MAP = {'theorem':'theorem','lemma':'lemma','corollary':'corollary',
            'definition':'definition','proposition':'proposition'}

# ============================================================================
# 阶段1: 扫描所有候选定理标记 + 区分声明vs引用
# ============================================================================

def _scan_candidates(content: str) -> list[dict]:
    """扫描所有定理标记, 分类为声明或引用"""
    candidates = []

    # 有编号的标记
    for m in THM_DECLARE.finditer(content):
        candidates.append({
            'type_raw': m.group(1),
            'number': m.group(2),
            'start': m.start(),
            'end': m.end(),
            'matched_text': m.group(0)
        })

    # 无编号的标记 (独立的 Theorem. 行)
    for m in THM_UNNUMBERED.finditer(content):
        # 去重: 不要与已匹配的编号标记重叠
        if not any(abs(c['start'] - m.start()) < 5 for c in candidates):
            candidates.append({
                'type_raw': m.group(1),
                'number': '',
                'start': m.start(),
                'end': m.end(),
                'matched_text': m.group(0)
            })

    candidates.sort(key=lambda c: c['start'])

    # 分类: 声明 vs 引用
    declarations = []
    for c in candidates:
        # 检查前文: 前面30个字符
        pre_start = max(0, c['start'] - 35)
        pre_text = content[pre_start:c['start']].rstrip()

        # 检查后文: 后面10个字符
        post_text = content[c['end']:c['end'] + 15].lstrip()

        is_citation = False

        # 规则1: 前面以引用词结尾 → 引用
        if CITATION_BEFORE.search(pre_text):
            is_citation = True

        # 规则2: 后面紧跟逗号+页码/括号 → 引用
        if CITATION_AFTER.match(post_text):
            is_citation = True

        # 规则3: 前面不在行首 (不是换行后) → 很可能是引用
        if c['start'] > 0 and content[c['start'] - 1] != '\n':
            # 如果在行中间, 检查是否是真正的声明 (偶尔有格式问题)
            pre_line = pre_text.split('\n')[-1] if '\n' in pre_text else pre_text
            if len(pre_line) > 40:
                is_citation = True

        if not is_citation:
            declarations.append(c)

    return declarations

# ============================================================================
# 阶段2: 确定边界 → 提取定理体
# ============================================================================

def _extract_bodies(content: str, declarations: list[dict]) -> list[dict]:
    """为每个声明提取定理体 (从声明结束到下一个边界)"""

    # 收集所有边界位置
    boundaries = set()

    # 节标题
    for m in SECTION.finditer(content):
        boundaries.add(m.start())

    # 参考文献
    for m in REFERENCES.finditer(content):
        boundaries.add(m.start())

    # Proof块 (定理体不应该包含证明文字)
    for m in PROOF_START.finditer(content):
        boundaries.add(m.start())

    # 下一个定理声明的开始 = 当前定理的结束
    for d in declarations:
        boundaries.add(d['start'])

    boundaries = sorted(boundaries)

    items = []
    for i, decl in enumerate(declarations):
        itype = TYPE_MAP.get(decl['type_raw'].lower(), 'theorem')
        num = decl['number']
        name = f"{itype.capitalize()} {num}".strip() if num else f"{itype.capitalize()}"

        body_start = decl['end']

        # 找到下一个边界
        body_end = len(content)
        for b in boundaries:
            if b > body_start:
                body_end = b
                break

        # 提取原始体文本
        raw_body = content[body_start:body_end].strip()

        # 清理: 截断到Proof之前 (如果Proof在体内)
        proof_m = PROOF_START.search(raw_body)
        if proof_m:
            raw_body = raw_body[:proof_m.start()].strip()

        # 截断到下一个定理声明之前
        for d2 in declarations:
            if d2['start'] > body_start and d2['start'] < body_start + len(raw_body):
                raw_body = raw_body[:d2['start'] - body_start].strip()
                break

        statement = raw_body[:3000]

        # 提取LaTeX公式
        display_formulas = [f.strip() for f in DISPLAY_MATH.findall(statement)]

        if display_formulas:
            # 有display公式 → 选第一个非平凡的
            core_latex = ''
            for f in display_formulas:
                if len(f) > 15:
                    core_latex = f
                    break
            if not core_latex:
                core_latex = display_formulas[0]
        else:
            # 无display公式 → 拼接inline公式
            inline_formulas = [f.strip() for f in INLINE_MATH.findall(statement)]
            # 选重要的 (长的, 或者前几个)
            significant = [f for f in inline_formulas if len(f) > 10]
            core_latex = ' ; '.join(significant[:3]) if significant else ''

        items.append({
            'id': '',  # 由调用者填充
            'type': itype,
            'number': num,
            'name': name,
            'statement': statement[:2000],
            'latex': core_latex,
            'formulas': display_formulas[1:] if len(display_formulas) > 1 else [],
            'premises': '', 'conclusion': '',
            'proof_technique': '', 'confidence': 0.5,
            'position': decl['start']
        })

    return items

# ============================================================================
# 阶段3: 公式合并 + ID赋值 + 最终清理
# ============================================================================

def _finalize(items: list[dict], pid: str, content: str) -> list[dict]:
    """分配ID, 合并tag公式, 最终质量检查"""

    # 提取tag公式
    tag_formulas = []
    for i, m in enumerate(TAG_FORMULA.finditer(content)):
        latex_str = m.group(1).strip()
        if len(latex_str) > 20:
            tag_formulas.append({
                'latex': latex_str,
                'position': m.start(),
                'tag': m.group(2).strip()
            })

    # 合并公式到最近的定理 (按position)
    formula_positions = [(f['position'], f) for f in tag_formulas]
    formula_positions.sort()

    for i, item in enumerate(items):
        # 找下一个item的position作为范围上界
        next_pos = items[i+1]['position'] if i+1 < len(items) else len(content)

        # 收集范围内的公式
        for pos, f in formula_positions:
            if item['position'] <= pos < next_pos:
                formulas = item.setdefault('formulas', [])
                if f['latex'] not in formulas:
                    formulas.append(f['latex'])
                if not item.get('latex'):
                    item['latex'] = f['latex']

    # 分配ID
    for i, item in enumerate(items):
        num = item.get('number', '')
        itype = item.get('type', 'theorem')
        item['id'] = f"{pid}_{itype}_{num}" if num else f"{pid}_{itype}_{i}"
        if item['name'] == itype.capitalize() and not num:
            item['name'] = f"{itype.capitalize()} {i+1}"

    return items

# ============================================================================
# 主入口
# ============================================================================

def parse_paper_regex(filepath: str) -> list[dict]:
    """三阶段提取:
    阶段1: 扫描定理标记, 区分声明 vs 引用
    阶段2: 以定理声明+Proof+节标题为边界, 提取定理体
    阶段3: 分配ID, 合并公式, 最终清理
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    dirname = os.path.basename(os.path.dirname(filepath))
    pid = dirname.split('-')[0] if '-' in dirname else dirname

    declarations = _scan_candidates(content)
    items = _extract_bodies(content, declarations)
    items = _finalize(items, pid, content)

    return items


def parse_paper(filepath: str) -> tuple[dict, list[dict]]:
    """解析单篇论文 → (meta, items)"""
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
        for f in sorted(files):
            if f.endswith('.correction.md'):
                filepath = os.path.join(root, f)
                meta, items = parse_paper(filepath)
                papers.append(meta)
                all_items.extend(items)
                short_t = meta['title'][:50].encode('ascii', errors='replace').decode('ascii')
                print(f"  [{meta['year']}] {short_t} -> {len(items)} items")
    return papers, all_items
