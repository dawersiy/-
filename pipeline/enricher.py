"""
Claude Code 自动富化: 正则解析后用Claude API对item进行关键词/摘要/领域标注
依赖: ANTHROPIC_API_KEY (从.env自动加载)
"""

import os, json, hashlib, time
from config import BASE_DIR

PROMPTS_DIR = os.path.join(BASE_DIR, 'prompts')
CACHE_DIR = os.path.join(BASE_DIR, 'llm_cache')
os.makedirs(CACHE_DIR, exist_ok=True)

def _get_client():
    """获取Anthropic客户端 (延迟导入)"""
    try:
        from anthropic import Anthropic
        api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not api_key:
            return None
        return Anthropic(api_key=api_key)
    except ImportError:
        return None

def _load_prompt(name: str) -> str:
    """加载提示词模板"""
    path = os.path.join(PROMPTS_DIR, f'{name}.txt')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def _cache_key(stage: str, text: str) -> str:
    h = hashlib.md5((stage + text).encode()).hexdigest()[:16]
    return os.path.join(CACHE_DIR, f'{stage}_{h}.json')

def _cache_get(stage: str, text: str) -> dict | None:
    path = _cache_key(stage, text)
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if time.time() - data.get('_ts', 0) < 86400 * 30:
                return data.get('result')
        except:
            pass
    return None

def _cache_set(stage: str, text: str, result: dict):
    path = _cache_key(stage, text)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'_ts': time.time(), 'result': result}, f, ensure_ascii=False)

def _call_claude(system_prompt: str, user_prompt: str, model: str = "claude-sonnet-5") -> str:
    """调用Claude API, 返回文本响应"""
    client = _get_client()
    if not client:
        raise RuntimeError("Anthropic client不可用")

    response = client.messages.create(
        model=model,
        max_tokens=2048,
        system=[{"type": "text", "text": system_prompt,
                 "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.content[0].text

# ============================================================================
# 富化入口
# ============================================================================

def enrich_items(items: list[dict]) -> list[dict]:
    """
    使用Claude API自动富化所有item:
    - 关键词 (classify prompt)
    - 中文摘要 (summarize prompt)
    已缓存的item会跳过
    """
    client = _get_client()
    if not client:
        print("  [enricher] ANTHROPIC_API_KEY未设置, 跳过富化")
        return items

    classify_prompt = _load_prompt('classify')
    summarize_prompt = _load_prompt('summarize')

    if not classify_prompt:
        print("  [enricher] prompts/classify.txt 缺失, 跳过")
        return items

    enriched = 0
    cached = 0
    total = len(items)

    for i, item in enumerate(items):
        # 构建输入文本
        item_text = f"Name: {item.get('name','')}\nType: {item.get('type','')}\n"
        if item.get('latex'):
            item_text += f"LaTeX: {item['latex'][:400]}\n"
        item_text += f"Statement: {item.get('statement','')[:1500]}"

        # 1. 关键词分类 (带缓存)
        kw_result = _cache_get('classify', item_text)
        if kw_result:
            item['keywords'] = kw_result.get('keywords', item.get('keywords', []))
            item['domain'] = kw_result.get('domain', item.get('domain', []))
            cached += 1
        else:
            try:
                resp = _call_claude(classify_prompt, item_text)
                # 提取JSON
                json_match = resp[resp.find('{'):resp.rfind('}')+1] if '{' in resp else resp
                result = json.loads(json_match) if isinstance(json_match, str) else {}
                item['keywords'] = result.get('keywords', item.get('keywords', []))
                item['domain'] = result.get('domain', item.get('domain', []))
                _cache_set('classify', item_text, result)
                enriched += 1
                time.sleep(0.3)  # 速率限制
            except Exception as e:
                pass  # 保持原有keywords

        # 2. 中文摘要 (带缓存, 仅对theorem/lemma/proposition)
        if item.get('type') in ('theorem', 'lemma', 'proposition') and not item.get('summary'):
            sum_result = _cache_get('summarize', item_text)
            if sum_result:
                item['summary'] = sum_result.get('summary', '')
            elif summarize_prompt:
                try:
                    resp = _call_claude(summarize_prompt, item_text)
                    summary = resp.strip()
                    if summary:
                        item['summary'] = summary
                        _cache_set('summarize', item_text, {'summary': summary})
                    time.sleep(0.3)
                except:
                    pass

        if (i + 1) % 20 == 0:
            print(f"  [enricher] {i+1}/{total} (新:{enriched} 缓存:{cached})")

    print(f"  [enricher] 完成: {enriched} 项新富化, {cached} 项命中缓存, {total-enriched-cached} 项跳过")
    return items
