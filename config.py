"""集中化配置和路径常量"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- 加载 .env 文件 ----
def _load_dotenv():
    env_path = os.path.join(BASE_DIR, '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, val = line.partition('=')
                key, val = key.strip(), val.strip()
                if val and key not in os.environ:
                    os.environ[key] = val

_load_dotenv()

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
