# Mathematical Knowledge Graph — Optimization Theory

从 26 篇优化理论经典论文中自动提取定理/引理/推论/定义/命题，构建去重知识网络并生成交互式 2D 可视化。

---

## Processing Results

| Metric | Value |
|---|---|
| Papers processed | 26 (1964–2006) |
| Total items extracted | **315** |
| Cross-paper merges | 3 |
| Relations discovered | **5,162** |
| Build time | ~8 seconds |

### Items by Type

| Type | Count | Color |
|---|---|---|
| Theorem | 101 | <span style="color:#ff5252">●</span> Red |
| Lemma | 90 | <span style="color:#448aff">●</span> Blue |
| Proposition | 61 | <span style="color:#ffab40">●</span> Orange |
| Corollary | 50 | <span style="color:#69f0ae">●</span> Green |
| Definition | 13 | <span style="color:#e040fb">●</span> Purple |

### Relations by Type

| Type | Count | Line Style | Meaning |
|---|---|---|---|
| Depends | 2,309 | Orange dotted | Logical dependency |
| Derives | 1,529 | Red solid | Deduction chain |
| Generalizes | 807 | Blue dashed | Generalization / extension |
| Equivalent | 517 | Green dashed | Mathematical equivalence |

---

## Algorithm

### Stage 1 — Parse: Citation-Aware Theorem Extraction

```
Scan paper for all "Theorem|Lemma|Corollary|Definition|Proposition + number" markers
  │
  ├─ Check context (±35 chars):
  │   ├─ Preceded by "by|using|from|see|in|of|applying" → Citation, discard
  │   ├─ Followed by ", p." or "(see" or "[" → Citation, discard
  │   └─ Otherwise → Confirmed declaration, keep
  │
  └─ Also capture unnumbered standalone "Theorem." lines
```

### Stage 2 — Boundary: Multi-Point Body Delimitation

```
Boundary set = all declarations + all "Proof." blocks + all "# section" headers + "REFERENCES"
For each declaration:
  body_start = end of declaration line
  body_end   = next boundary in sorted list
  Raw body   = content[body_start:body_end]
  Trim: stop at first "Proof." within body
  Trim: stop at next declaration within body
```

### Stage 3 — Finalize: Formula Extraction + ID Assignment

```
For each theorem body:
  Priority 1: Extract first $$...$$ display formula (length > 15 chars)
  Fallback:  Concatenate inline $...$ formulas (length > 10 chars, top 3)
  Merge tagged formulas (\tag{...}) into nearest preceding theorem
  Assign unique ID: {paper_year}_{type}_{number}
```

### Stage 4 — Deduplicate: Structure-Preserving Signature

```
Compute LaTeX structural signature:
  1. Normalize whitespace
  2. Replace single-letter variables → X
  3. Replace subscripted variables → XS
  4. Replace numbers → N
  5. Keep all LaTeX commands intact (no collapse to G)
  6. Truncate to 200 chars

Bucket items by signature prefix → compare within bucket
Same-paper items with different names: NEVER merge
SequenceMatcher ratio > 0.92 → merge
```

### Stage 5 — Relations: Multi-Strategy Heuristic Discovery

```
For each item pair sharing ≥ 2 non-type keywords:

  derives:
    theorem → corollary (confidence 0.8)
    lemma/proposition → corollary with score ≥ 3

  depends:
    lemma → theorem/proposition (score ≥ 3)
    definition → any (score ≥ 2)
    proposition → theorem (score ≥ 3)
    same-paper adjacent lemma chain
    cross-reference: one item's name appears in other's statement

  equivalent:
    same type + same number + different papers (score ≥ 3)
    LaTeX similarity > 92%
    same type + 5+ shared keywords

  generalizes:
    same type + different papers + earlier → later year (score ≥ 4)

  fallback:
    5+ shared keywords → weak depends
```

### Stage 6 — Layout: Center-Radial Weighted Force

```
1. Compute node centrality (degree)
2. BFS from top-5 central nodes → assign depth rings
3. Place nodes in concentric rings (center = high degree)
4. Weighted spring refinement:
   - derives/generalizes (weight 1.0) → target distance 40px
   - depends (weight 0.5) → target distance 100px
   - same_paper (weight 0.15) → target distance 180px
5. Grid-accelerated overlap prevention
6. Final hard overlap fix
```

---

## Project Structure

```
论文知识图谱/
├── build_graph.py              # Main pipeline (6 stages, ~8s)
├── config.py                   # Paths and layout settings
├── pipeline/
│   ├── parser.py               # 3-stage theorem extraction
│   ├── deduplication.py        # Structure-signature dedup
│   ├── relations.py            # Multi-strategy relation discovery
│   ├── layout.py               # Center-radial weighted force layout
│   └── enricher.py             # Claude API auto-enrichment (optional)
├── visualize/
│   ├── generator.py            # Self-contained HTML generator
│   └── static/
│       ├── graph.js            # D3.js engine
│       └── styles.css          # Stylesheet
├── prompts/                    # Claude Code prompt templates
│   ├── extract.txt             # Theorem extraction prompt
│   ├── classify.txt            # Keyword/domain classification
│   ├── summarize.txt           # Chinese summary generation
│   └── relations.txt           # Relation discovery prompt
├── papers/                     # 26 source papers (*.correction.md)
├── output/                     # Generated output (gitignored)
├── run.bat / run.sh            # One-click launcher scripts
└── .env                        # ANTHROPIC_API_KEY (gitignored)
```

---

## Usage

### Quick Start

```bash
# Windows
run.bat

# Linux/Mac
./run.sh
```

### Manual Build

```bash
# Full pipeline (regex mode, no API needed)
python build_graph.py

# Export raw items for Claude Code analysis
python build_graph.py --export output/raw_items.json

# Build with Claude Code-enriched data
python build_graph.py --enrich output/enriched.json

# Single paper extraction
python build_graph.py --paper papers/1964-.../paper.correction.md
```

### Visualization

Open `output/knowledge_network.html` in any browser. Features:
- **Paper selector**: filter to single paper or view all
- **Type filter**: show/hide by theorem/lemma/corollary/definition/proposition
- **Search**: find by name or keyword
- **Zoom/pan**: mouse wheel + drag
- **Click node**: view LaTeX formulas, statement, keywords, related items
- **Hover node**: highlight connected subgraph
- **Viewport culling**: only render visible nodes (performance)
- **LOD scaling**: simplify rendering at low zoom levels

---

## Papers Covered

| Year | Author(s) | Topic |
|---|---|---|
| 1964 | Polyak | Heavy ball method, multistep convergence |
| 1976 | Rockafellar | Monotone operators, proximal point algorithm |
| 1979 | Lions & Mercier | Splitting algorithms for nonlinear operators |
| 1983 | Nesterov | Accelerated gradient O(1/k²) |
| 1991 | Güler | Proximal point convergence |
| 1992 | Güler | New proximal point algorithms |
| 1995 | Bonnans et al. | Variable metric proximal methods |
| 1997 | Burachik et al. | Enlargements of monotone operators |
| 1997 | Burke & Qian | Variable metric proximal point |
| 1999 | Burke & Qian | Superlinear VM proximal convergence |
| 1999 | Chen & Fukushima | Proximal quasi-Newton methods |
| 2000 | Alvarez | Second-order dissipative systems |
| 2000 | Attouch et al. | Heavy ball with friction |
| 2000 | Attouch et al. | Inertial proximal method |
| 2000 | Burke & Qian | VM proximal point convergence |
| 2001 | Alvarez & Attouch | Inertial proximal for monotone operators |
| 2001 | Burachik & Svaiter | HPE robustness |
| 2003 | Moudafi et al. | Splitting inertial proximal |
| 2003 | Moudafi | Inertial proximal for quasi-variational inequalities |
| 2004 | Combettes | Nonexpansive averaged operators |
| 2004 | Nemirovski | Prox-method O(1/T) |
| 2004 | Nesterov | Introductory lectures on convex optimization |
| 2005 | Combettes & Wajs | Forward-backward splitting |
| 2006 | Auslender & Teboulle | Interior gradient proximal |
| 2006 | Baji & Cabot | Inertial proximal with dry friction |

---

## Dependencies

- **Python 3.10+** (standard library only for core pipeline)
- **anthropic** (optional: Claude API auto-enrichment)
- **D3.js v7** (loaded via CDN in HTML)
- **TeX Live** (optional: LaTeX → SVG rendering)
