"""磁盘缓存层 — 每个LLM调用按SHA256缓存到 llm_cache/"""

import hashlib, json, os, time
from config import CACHE_DIR, CACHE_TTL

os.makedirs(CACHE_DIR, exist_ok=True)

def _cache_key(stage: str, *inputs: str) -> str:
    """生成缓存键: stage + 输入SHA256"""
    combined = stage + "::" + "||".join(inputs)
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()

def _cache_path(key: str) -> str:
    return os.path.join(CACHE_DIR, f"{key}.json")

def get_cache(stage: str, *inputs: str) -> dict | None:
    """读取缓存, 过期返回None"""
    key = _cache_key(stage, *inputs)
    path = _cache_path(key)
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        age = time.time() - data.get('_ts', 0)
        if age > CACHE_TTL:
            os.remove(path)
            return None
        return data.get('result')
    except (json.JSONDecodeError, KeyError):
        return None

def set_cache(stage: str, result, *inputs: str):
    """写入缓存"""
    key = _cache_key(stage, *inputs)
    path = _cache_path(key)
    data = {'_ts': time.time(), '_stage': stage, 'result': result}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def invalidate_cache(stage: str = None):
    """清除缓存, 可选按stage过滤"""
    for fname in os.listdir(CACHE_DIR):
        if not fname.endswith('.json'):
            continue
        path = os.path.join(CACHE_DIR, fname)
        if stage:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if data.get('_stage') == stage:
                    os.remove(path)
            except:
                pass
        else:
            os.remove(path)
