"""轻量HTML生成器 — 外部加载数据, 视口裁剪, LOD缩放"""

import os, json
from config import OUTPUT_JSON, OUTPUT_HTML

def generate_html(network: dict = None):
    """生成优化的HTML可视化 (从外部JSON加载数据)"""

    # 如果提供了network且节点已有预计算坐标, 写入JSON
    if network:
        items = network.get('items', [])
        # 确保坐标存在
        for item in items:
            if 'x' not in item:
                item['x'] = 400 + (hash(item.get('id','')) % 800)
                item['y'] = 300 + (hash(item.get('id','')+'y') % 600)

    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>数学知识图谱 — 优化理论</title>
<link rel="stylesheet" href="visualize/static/styles.css">
</head>
<body>
<div id="container">
<div id="graph">
    <svg></svg>
    <div class="tooltip" id="tooltip"></div>
    <div id="loading">加载知识网络数据...</div>
    <div class="zoom-ctl">
        <button class="zbtn" id="zin">+</button>
        <button class="zbtn" id="zout">-</button>
        <button class="zbtn" id="zfit">F</button>
    </div>
</div>
<div id="sidebar">
    <h2>📊 知识图谱控制台</h2>
    <input type="text" id="search" placeholder="🔍 搜索定理、公式、关键词...">
    <div id="filter-row">
        <button class="fbtn active" data-type="all">全部</button>
        <button class="fbtn" data-type="theorem">定理</button>
        <button class="fbtn" data-type="lemma">引理</button>
        <button class="fbtn" data-type="corollary">推论</button>
        <button class="fbtn" data-type="definition">定义</button>
        <button class="fbtn" data-type="proposition">命题</button>
        <button class="fbtn" data-type="formula">公式</button>
    </div>
    <div id="stats"></div>
    <h2>🎨 图例</h2>
    <div id="legend"></div>
    <h2>📝 节点详情</h2>
    <div id="detail"><p style="color:#607d8b">点击图中节点查看详细信息</p></div>
    <h2>🔗 关联关系</h2>
    <div id="rel-list"></div>
</div>
</div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="visualize/static/graph.js"></script>
</body>
</html>'''

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  HTML: {OUTPUT_HTML} ({os.path.getsize(OUTPUT_HTML)} bytes)")

def save_network_json(network: dict):
    """保存知识网络JSON"""
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(network, f, ensure_ascii=False, indent=2)
    size_kb = os.path.getsize(OUTPUT_JSON) / 1024
    print(f"  JSON: {OUTPUT_JSON} ({size_kb:.1f} KB)")
