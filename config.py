"""集中化配置和路径常量"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 路径
PAPERS_DIR = os.path.join(BASE_DIR, 'papers')
CACHE_DIR = os.path.join(BASE_DIR, 'llm_cache')
OUTPUT_JSON = os.path.join(BASE_DIR, 'knowledge_network.json')
OUTPUT_HTML = os.path.join(BASE_DIR, 'knowledge_network.html')

# LLM配置
CLAUDE_MODEL = "claude-sonnet-5"         # 提取/摘要/关键词
CLAUDE_MODEL_DEEP = "claude-sonnet-5"    # 关系发现 (启用thinking)
MAX_TOKENS = 4096
MAX_CONCURRENT = 5
MIN_DELAY = 0.5         # 调用间延迟(秒)
MAX_RETRIES = 3
CACHE_TTL = 86400 * 30  # 30天

# 批处理
BATCH_SIZE = 10
PAPER_CHUNK_SIZE = 12000  # LLM提取的每块字符数

# 可视化
LAYOUT_WIDTH = 1600
LAYOUT_HEIGHT = 1200
