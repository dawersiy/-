"""使用本地TeXLive将LaTeX公式渲染为SVG"""

import os, subprocess, hashlib, tempfile, shutil
from config import CACHE_DIR

SVG_CACHE = os.path.join(CACHE_DIR, 'svg')
os.makedirs(SVG_CACHE, exist_ok=True)

# 已知的amsmath多字母命令 (不在\xxx中拆分)
AMS_COMMANDS = {
    'nabla', 'partial', 'infty', 'rightarrow', 'leftarrow', 'Rightarrow', 'Leftarrow',
    'langle', 'rangle', 'langle', 'rangle', 'cdot', 'times', 'circ', 'oplus', 'otimes',
    'varepsilon', 'epsilon', 'varphi', 'phi', 'kappa', 'lambda', 'Lambda', 'mu',
    'sigma', 'Sigma', 'omega', 'Omega', 'gamma', 'Gamma', 'delta', 'Delta',
    'theta', 'Theta', 'alpha', 'beta', 'eta', 'rho', 'tau', 'xi', 'Xi', 'pi', 'Pi',
    'psi', 'Psi', 'zeta', 'chi', 'nu', 'iota', 'mathbb', 'mathcal', 'mathfrak',
    'mathbf', 'mathrm', 'mathit', 'mathsf', 'mathtt', 'operatorname', 'text',
    'textbf', 'textit', 'textsf', 'texttt', 'widehat', 'widetilde', 'widetilde',
    'overline', 'underline', 'overrightarrow', 'overleftarrow', 'sqrt',
    'frac', 'sum', 'prod', 'int', 'oint', 'bigcap', 'bigcup', 'bigoplus',
    'lim', 'sup', 'inf', 'max', 'min', 'argmin', 'argmax', 'det', 'dim', 'ker',
    'exp', 'log', 'ln', 'sin', 'cos', 'tan', 'cot', 'gcd', 'hom', 'Pr',
    'forall', 'exists', 'nexists', 'emptyset', 'varnothing', 'in', 'notin',
    'subset', 'supset', 'subseteq', 'supseteq', 'equiv', 'approx', 'sim',
    'propto', 'cong', 'neq', 'leq', 'geq', 'll', 'gg', 'perp', 'parallel',
    'mid', 'nmid', 'pm', 'mp', 'cdot', 'bullet', 'diamond', 'star', 'ast',
    'oplus', 'ominus', 'otimes', 'oslash', 'odot', 'bigcirc',
    'hat', 'tilde', 'bar', 'vec', 'dot', 'ddot', 'check', 'breve', 'acute',
    'grave', 'mathring', 'widetilde', 'widehat',
    'left', 'right', 'big', 'Big', 'bigg', 'Bigg', 'middle',
    'longrightarrow', 'longmapsto', 'hookrightarrow', 'iff',
    'varepsilon', 'vartheta', 'varpi', 'varrho', 'varsigma', 'varphi',
    'ell', 'wp', 'Re', 'Im', 'aleph', 'hbar', 'imath', 'jmath', 'partial',
    'infty', 'Box', 'Diamond', 'triangle', 'triangledown', 'triangleleft',
    'triangleright', 'angle', 'measuredangle', 'sphericalangle',
    'lVert', 'rVert', 'lvert', 'rvert', 'Vert', 'vert',
    'setminus', 'cap', 'cup', 'wedge', 'vee', 'neg', 'lnot',
    'square', 'blacksquare', 'lozenge', 'blacklozenge', 'maltese',
    'diagup', 'diagdown', 'bowtie', 'ltimes', 'rtimes',
    'leqslant', 'geqslant', 'gtrless', 'lessgtr', 'nleq', 'ngeq',
    'risingdotseq', 'fallingdotseq', 'circeq', 'triangleq', 'thickapprox',
    'thicksim', 'backsim', 'backsimeq', 'Bumpeq', 'bumpeq', 'doteq',
    'coloneqq', 'Coloneqq', 'eqcolon', 'Eqqcolon', 'eqcirc', 'circeq',
    'fallingdotseq', 'multimap', 'rightrightarrows', 'leftleftarrows',
    'rightleftarrows', 'Lleftarrow', 'Rrightarrow', 'twoheadrightarrow',
    'twoheadleftarrow', 'rightarrowtail', 'leftarrowtail', 'looparrowleft',
    'looparrowright', 'curvearrowleft', 'curvearrowright', 'circlearrowleft',
    'circlearrowright', 'Lsh', 'Rsh', 'downdownarrows', 'upuparrows',
    'upharpoonright', 'downharpoonright', 'upharpoonleft', 'downharpoonleft',
    'rightsquigarrow', 'leftrightsquigarrow', 'nleftarrow', 'nrightarrow',
    'nLeftarrow', 'nRightarrow', 'multimap', 'pitchfork', 'lessdot',
    'gtrdot', 'risingdotseq', 'fallingdotseq', 'varpropto', 'therefore',
    'because', 'between', 'measuredangle', 'sphericalangle',
    'digamma', 'varkappa', 'beth', 'daleth', 'gimel',
    'mathbb', 'mathbf', 'mathcal', 'mathfrak', 'mathscr', 'mathsf',
    'mathtt', 'mathrm', 'mathbf', 'boldsymbol',
}

def _latex_hash(latex: str) -> str:
    return hashlib.md5(latex.encode('utf-8')).hexdigest()[:16]

def render_latex_svg(latex: str) -> str:
    """将LaTeX公式渲染为SVG字符串。失败时返回空字符串。"""
    if not latex or not latex.strip():
        return ''

    latex_clean = latex.strip()

    # 检查缓存
    h = _latex_hash(latex_clean)
    cache_path = os.path.join(SVG_CACHE, f'{h}.svg')
    if os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            return f.read()

    # 判断是display还是inline
    is_display = latex_clean.startswith('\\[') or latex_clean.startswith('$$') or '\n' in latex_clean
    if latex_clean.startswith('$$'): latex_clean = latex_clean[2:]
    if latex_clean.endswith('$$'): latex_clean = latex_clean[:-2]
    if latex_clean.startswith('\\['): latex_clean = latex_clean[2:]
    if latex_clean.endswith('\\]'): latex_clean = latex_clean[:-2]

    # 转义XML/HTML特殊字符
    latex_safe = latex_clean.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#')
    # 注意：_ ^ 等已在LaTeX中有意义，不需要转义

    math_env = '\\[\\displaystyle ' if is_display else '$\\displaystyle '
    math_close = '\\]' if is_display else '$'

    tex_content = f'''\\documentclass[border=2pt]{{standalone}}
\\usepackage{{amsmath,amssymb,amsfonts,amsthm,mathrsfs,mathtools}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{lmodern}}
\\begin{{document}}
{math_env}
{latex_safe}
{math_close}
\\end{{document}}'''

    tmpdir = tempfile.mkdtemp(prefix='latex_')
    tex_path = os.path.join(tmpdir, 'formula.tex')

    try:
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)

        # 运行latex (不是pdflatex, 因为dvisvgm需要DVI)
        result = subprocess.run(
            ['latex', '-interaction=nonstopmode', '-halt-on-error',
             '-output-directory', tmpdir, 'formula.tex'],
            capture_output=True, text=True, timeout=30, cwd=tmpdir
        )

        dvi_path = os.path.join(tmpdir, 'formula.dvi')
        svg_path = os.path.join(tmpdir, 'formula.svg')

        if os.path.exists(dvi_path):
            subprocess.run(
                ['dvisvgm', '--no-fonts', '--exact', '-o', svg_path, dvi_path],
                capture_output=True, text=True, timeout=30, cwd=tmpdir
            )

            if os.path.exists(svg_path):
                with open(svg_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()

                # 清理SVG: 提取<svg>标签内的内容
                svg_match = svg_content[svg_content.find('<svg'):svg_content.rfind('</svg>')+6] if '<svg' in svg_content else svg_content

                # 缓存
                with open(cache_path, 'w', encoding='utf-8') as f:
                    f.write(svg_match)

                return svg_match

    except subprocess.TimeoutExpired:
        pass
    except Exception:
        pass
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    return ''

def render_latex_batch(latex_list: list[str]) -> dict[str, str]:
    """批量渲染LaTeX公式, 返回 {latex: svg} 映射"""
    results = {}
    for latex in latex_list:
        if latex:
            svg = render_latex_svg(latex)
            if svg:
                results[latex] = svg
    return results
