# 数学知识图谱 — 优化理论

从 26 篇优化理论经典论文中自动提取定理、引理、推论、定义、命题，构建去重知识网络并生成交互式 2D 可视化。

---

## 项目概述

整个流程由 **Claude Code 驱动分析 + Python 正则管道处理 + D3.js 可视化** 三部分协作完成。核心管道仅使用 Python 标准库，零外部依赖；Claude API 为可选增强模块。

---

## 处理结果

| 指标 | 数值 |
|---|---|
| 处理论文 | 26 篇 (1964–2006) |
| 提取条目 | **315 项** |
| 跨论文去重合并 | 3 项 |
| 发现关系 | **5,162 条** |
| 构建耗时 | ~8 秒 |

### 条目类型分布

| 类型 | 数量 | 颜色标识 |
|---|---|---|
| 定理 Theorem | 101 | <span style="color:#ff5252">●</span> 红 |
| 引理 Lemma | 90 | <span style="color:#448aff">●</span> 蓝 |
| 命题 Proposition | 61 | <span style="color:#ffab40">●</span> 橙 |
| 推论 Corollary | 50 | <span style="color:#69f0ae">●</span> 绿 |
| 定义 Definition | 13 | <span style="color:#e040fb">●</span> 紫 |

### 关系类型分布

| 类型 | 数量 | 线型 | 含义 |
|---|---|---|---|
| 依赖 Depends | 2,309 | 橙色点线 | 逻辑依赖关系 |
| 推导 Derives | 1,529 | 红色实线 | 推导链 |
| 推广 Generalizes | 807 | 蓝色虚线 | 推广/扩展 |
| 等价 Equivalent | 517 | 绿色虚线 | 数学等价 |

---

## 算法设计

### 阶段一 — 解析：引用感知定理提取

```
扫描论文全文中的 "Theorem|Lemma|Corollary|Definition|Proposition + 编号" 标记
  │
  ├─ 检查上下文 (±35 字符):
  │   ├─ 前面含 "by|using|from|see|in|of|applying" → 判定为引用, 丢弃
  │   ├─ 后面紧跟 ", p." 或 "(see" 或 "[" → 判定为引用, 丢弃
  │   └─ 否则 → 确认为定理声明, 保留
  │
  └─ 同时捕获无编号的独立 "Theorem." 行
```

**核心改进**：区分 "Theorem 3, p.32"（论文内引用）与真正的定理声明，消除假阳性。

### 阶段二 — 边界：多点定理体分割

```
边界集合 = 所有定理声明位置 + 所有 "Proof." 块 + 所有 "#" 节标题 + "REFERENCES"
对于每个定理声明:
  body_start = 声明行结束位置
  body_end   = 边界排序列表中下一个边界
  原始体     = content[body_start:body_end]
  二次裁剪: 截断到体内第一个 "Proof." 之前
  二次裁剪: 截断到体内下一个定理声明之前
```

**核心改进**：以定理声明自身作为前一个定理的结束边界，消除语句渗漏（前一个定理的陈述包含下一个定理的文字）。

### 阶段三 — 定稿：公式提取与 ID 分配

```
对每个定理体:
  优先方案: 提取第一个 $$...$$ 展示公式 (长度 > 15 字符)
  回退方案: 拼接内联 $...$ 公式 (长度 > 10 字符, 取前 3 个)
  合并 \tag{...} 编号公式到位置最近的定理
  分配唯一 ID: {论文年份}_{类型}_{编号}
```

**核心改进**：内联公式回退消除了大量 "无 LaTeX" 项（从 ~25% 降至 3%）。

### 阶段四 — 去重：保留结构的签名比对

```
计算 LaTeX 结构签名:
  1. 归一化空白字符
  2. 单字母变量 → X
  3. 带下标变量 → XS
  4. 数字 → N
  5. 保留所有 LaTeX 命令 (不折叠为 G)
  6. 截断到 200 字符

按签名前缀分桶 → 桶内逐对比较
同论文不同编号的项: 绝不合并
SequenceMatcher 相似度 > 0.92 → 合并
```

**核心改进**：保留 LaTeX 命令结构，避免不同定理因命令被折叠而产生相同签名。

### 阶段五 — 关系：多策略启发式发现

```
对每对待比较条目 (共享 ≥ 2 个非类型关键词):

  推导 (derives):
    定理 → 推论 (置信度 0.8)
    引理/命题 → 推论, 分数 ≥ 3

  依赖 (depends):
    引理 → 定理/命题 (分数 ≥ 3)
    定义 → 任意 (分数 ≥ 2)
    命题 → 定理 (分数 ≥ 3)
    同论文相邻引理链
    交叉引用: 一方名称出现在另一方的陈述中

  等价 (equivalent):
    同类型 + 同编号 + 不同论文 (分数 ≥ 3)
    LaTeX 签名相似度 > 92%
    同类型 + 共享 5+ 关键词

  推广 (generalizes):
    同类型 + 不同论文 + 先→后年份 (分数 ≥ 4)

  回退:
    共享 5+ 关键词 → 弱依赖
```

**核心改进**：四种关系类型均衡分布，等价和推广从几乎为零提升到数百条。

### 阶段六 — 布局：中心辐射加权力导向

```
1. 计算节点中心度 (度数)
2. 从 top-5 核心节点 BFS → 分配深度环
3. 同心环放置节点 (中心 = 高度数)
4. 加权弹簧精调:
   - 推导/推广 (权重 1.0) → 目标距离 40px
   - 依赖 (权重 0.5) → 目标距离 100px
   - 同论文 (权重 0.15) → 目标距离 180px
5. 网格加速防重叠
6. 最终硬性去重叠修正
```

**核心改进**：关系紧密的节点距离近，同论文节点轻微聚拢，无碰撞体积。

---

## 项目结构

```
论文知识图谱/
├── build_graph.py              # 主入口 (6阶段管道, ~8秒)
├── config.py                   # 路径与布局配置
├── pipeline/
│   ├── parser.py               # 三阶段定理提取
│   ├── deduplication.py        # 结构签名去重
│   ├── relations.py            # 多策略关系发现
│   ├── layout.py               # 中心辐射加权布局
│   └── enricher.py             # Claude API 自动富化 (可选)
├── visualize/
│   ├── generator.py            # 自包含 HTML 生成器
│   └── static/
│       ├── graph.js            # D3.js 渲染引擎
│       └── styles.css          # 样式表
├── prompts/                    # Claude Code 提示词模板
│   ├── extract.txt             # 定理提取
│   ├── classify.txt            # 关键词/领域分类
│   ├── summarize.txt           # 中文摘要生成
│   └── relations.txt           # 关系发现
├── papers/                     # 26 篇源论文
├── output/                     # 生成输出 (git 忽略)
├── run.bat / run.sh            # 一键启动脚本
└── .env                        # ANTHROPIC_API_KEY (git 忽略)
```

---

## 使用方式

### 一键启动

```bash
# Windows
run.bat

# Linux / Mac
./run.sh
```

### 手动构建

```bash
# 完整管道 (正则模式, 无需 API)
python build_graph.py

# 导出原始条目供 Claude Code 分析
python build_graph.py --export output/raw_items.json

# 加载 Claude Code 富化数据构建
python build_graph.py --enrich output/enriched.json

# 单篇论文提取
python build_graph.py --paper papers/1964-.../paper.correction.md
```

### 可视化

打开 `output/knowledge_network.html`（双击即可，无需 HTTP 服务器）：

- **论文选择器** — 切换单篇论文视图或全部总览
- **类型过滤** — 按定理/引理/推论/定义/命题筛选
- **关键词搜索** — 按名称或关键词查找
- **缩放拖拽** — 鼠标滚轮缩放，拖拽移动节点
- **点击节点** — 右侧面板显示 LaTeX 公式、陈述、关键词、关联项
- **悬停节点** — 高亮显示连通子图
- **视口裁剪** — 仅渲染可见区域节点（性能优化）
- **LOD 缩放** — 远距自动简化渲染

### Claude Code 增强流程

```bash
# 步骤 1: 导出条目
python build_graph.py --export output/raw_items.json

# 步骤 2: 在 Claude Code 中运行
# "读取 prompts/classify.txt, 对 output/raw_items.json 分类, 保存为 output/enriched.json"

# 步骤 3: 加载增强数据构建
python build_graph.py --enrich output/enriched.json
```

---

## 论文覆盖

| 年份 | 作者 | 主题 |
|---|---|---|
| 1964 | Polyak | 重球法、多步迭代收敛 |
| 1976 | Rockafellar | 单调算子、近端点算法 |
| 1979 | Lions & Mercier | 非线性算子分裂算法 |
| 1983 | Nesterov | 加速梯度 O(1/k²) |
| 1991 | Güler | 近端点算法收敛性 |
| 1992 | Güler | 新型近端点算法 |
| 1995 | Bonnans 等 | 变度量近端方法 |
| 1997 | Burachik 等 | 单调算子扩大 |
| 1997 | Burke & Qian | 变度量近端点算法 |
| 1999 | Burke & Qian | 超线性变度量近端收敛 |
| 1999 | Chen & Fukushima | 拟牛顿近端方法 |
| 2000 | Alvarez | 二阶耗散系统 |
| 2000 | Attouch 等 | 重球摩擦法 |
| 2000 | Attouch 等 | 惯性近端方法 |
| 2000 | Burke & Qian | 变度量近端点收敛 |
| 2001 | Alvarez & Attouch | 单调算子惯性近端 |
| 2001 | Burachik & Svaiter | HPE 鲁棒性 |
| 2003 | Moudafi 等 | 分裂惯性近端方法 |
| 2003 | Moudafi | 拟变分不等式惯性近端 |
| 2004 | Combettes | 平均非扩张算子 |
| 2004 | Nemirovski | O(1/T) 近端方法 |
| 2004 | Nesterov | 凸优化导论 |
| 2005 | Combettes & Wajs | 前向后向分裂 |
| 2006 | Auslender & Teboulle | 内点梯度近端方法 |
| 2006 | Baji & Cabot | 干摩擦惯性近端算法 |

---

## 关键设计决策

- **Claude Code 为智能核心** — 论文分析和提示词模板由 Claude Code 处理，正则作为高性能回退
- **零外部依赖** — 核心管道仅用 Python 标准库，`anthropic` 为可选增强
- **内嵌数据 HTML** — 输出为自包含单文件，双击即开
- **静态预计算布局** — 浏览器不运行动态力模拟，直接渲染预计算坐标
- **引用与声明分离** — 上下文分析区分论文内引用与真正的定理声明
- **无碰撞节点** — 网格加速防重叠 + 最终硬性修正确保节点不覆盖

---

## 依赖

- **Python 3.10+** (核心管道仅需标准库)
- **anthropic** (可选: Claude API 自动富化)
- **D3.js v7** (HTML 内通过 CDN 加载)
- **TeX Live** (可选: LaTeX → SVG 渲染)
