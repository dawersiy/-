# 测试版本
优化算法逻辑 (三阶段)
阶段1 — 扫描 + 区分声明 vs 引用


对论文全文扫描所有 "Theorem|Lemma|... + 编号" 标记
对每个标记检查上下文:
  ├─ 前35字符含 "by|using|from|see|in|of|applying|to|and" → 引用, 丢弃
  ├─ 后15字符含 ", p." 或 "(see" 或 "[" → 引用, 丢弃
  └─ 前后都是正常文本 → 确认为声明, 保留

同时捕获无编号的独立 "Theorem." 行
阶段2 — 边界提取定理体


边界列表 = 所有定理声明位置 + 所有 "Proof." + 所有 "# section" + "REFERENCES"
对于每个定理声明:
  body_start = 声明行结束位置
  body_end   = 下一个边界 (定理/Proof/节/参考文献)
  提取 body_start→body_end 之间的文本
  再次扫描body内部: 截断到第一个Proof之前
阶段3 — 公式提取 + ID分配


对每个定理体:
  优先: 提取第一个 $$...$$ (长度>15)
  回退: 拼接内联 $...$ 公式 (长度>10, 选前3个)
  
分配唯一ID: {论文ID}_{类型}_{编号}
核心改进：引用过滤消除了假定理、内联公式回退消除了无LaTeX项、Proof截断消除了语句渗漏。

//
全自动流程

python build_graph.py
     │
     ├─ [1] 正则解析论文 → 提取定理/引理
     ├─ [2] 正则关键词 (回退)
     ├─ [2.5] Claude API 自动富化 ← 新增
     │       ├─ prompts/classify.txt → 关键词+领域
     │       └─ prompts/summarize.txt → 中文摘要
     ├─ [3] 去重
     ├─ [4] 关系发现
     ├─ [5] 布局
     └─ [6] 输出 HTML/JSON