"""配置 — 纯本地处理, 无外部API依赖"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 输入输出
PAPERS_DIR = os.path.join(BASE_DIR, 'papers')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
OUTPUT_JSON = os.path.join(OUTPUT_DIR, 'knowledge_network.json')
OUTPUT_HTML = os.path.join(OUTPUT_DIR, 'knowledge_network.html')

# 布局
LAYOUT_WIDTH = 1600
LAYOUT_HEIGHT = 1200

os.makedirs(OUTPUT_DIR, exist_ok=True)
