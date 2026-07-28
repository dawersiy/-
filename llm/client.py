"""Anthropic Claude API客户端 — 单例 + 速率限制 + 结构化输出辅助"""

import time, os, asyncio
from anthropic import Anthropic
from config import CLAUDE_MODEL, CLAUDE_MODEL_DEEP, MAX_TOKENS, MAX_CONCURRENT, MIN_DELAY
from pipeline.cache_manager import get_cache, set_cache

_client: Anthropic | None = None
_semaphore = asyncio.Semaphore(MAX_CONCURRENT) if asyncio else None
_last_call = 0.0

def get_client() -> Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY 环境变量未设置")
        _client = Anthropic(api_key=api_key)
    return _client

def _rate_limit():
    """同步速率限制"""
    global _last_call
    elapsed = time.time() - _last_call
    if elapsed < MIN_DELAY:
        time.sleep(MIN_DELAY - elapsed)
    _last_call = time.time()

async def _async_rate_limit():
    """异步速率限制"""
    global _last_call
    elapsed = time.time() - _last_call
    if elapsed < MIN_DELAY:
        await asyncio.sleep(MIN_DELAY - elapsed)
    _last_call = time.time()

# ---- 同步API (用于简单脚本) ----

def call_llm_structured(
    system_prompt: str,
    user_prompt: str,
    output_schema: dict,
    model: str = CLAUDE_MODEL,
    use_cache: bool = True,
    cache_stage: str = "llm_structured"
) -> dict:
    """调用LLM并返回结构化JSON输出 (同步, 带缓存)"""

    if use_cache:
        cached = get_cache(cache_stage, system_prompt, user_prompt)
        if cached is not None:
            return cached

    _rate_limit()
    client = get_client()

    response = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        system=[
            {"type": "text", "text": system_prompt,
             "cache_control": {"type": "ephemeral"}}
        ],
        messages=[{"role": "user", "content": user_prompt}],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "result": output_schema
                    },
                    "required": ["result"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = None
    for block in response.content:
        if block.type == "tool_use" and hasattr(block, 'input'):
            result = block.input
            break

    if result is None:
        text = response.content[0].text if response.content else ""
        import json
        try:
            result = json.loads(text)
        except:
            result = {"error": "parse_failed", "raw": text[:500]}

    if use_cache:
        set_cache(cache_stage, result, system_prompt, user_prompt)

    return result

def call_llm_text(
    system_prompt: str,
    user_prompt: str,
    model: str = CLAUDE_MODEL,
    use_cache: bool = True,
    cache_stage: str = "llm_text"
) -> str:
    """调用LLM返回自由文本 (同步, 带缓存)"""

    if use_cache:
        cached = get_cache(cache_stage, system_prompt, user_prompt)
        if cached is not None:
            return cached if isinstance(cached, str) else cached.get('text', '')

    _rate_limit()
    client = get_client()

    response = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        system=[
            {"type": "text", "text": system_prompt,
             "cache_control": {"type": "ephemeral"}}
        ],
        messages=[{"role": "user", "content": user_prompt}]
    )

    text = response.content[0].text if response.content else ""

    if use_cache:
        set_cache(cache_stage, text, system_prompt, user_prompt)

    return text

def call_llm_thinking(
    system_prompt: str,
    user_prompt: str,
    output_schema: dict,
    model: str = CLAUDE_MODEL_DEEP,
    use_cache: bool = True,
    cache_stage: str = "llm_thinking"
) -> dict:
    """调用LLM进行深度推理 (启用thinking, 同步, 带缓存)"""

    if use_cache:
        cached = get_cache(cache_stage, system_prompt, user_prompt)
        if cached is not None:
            return cached

    _rate_limit()
    client = get_client()

    response = client.messages.create(
        model=model,
        max_tokens=8192,
        thinking={"type": "enabled", "budget_tokens": 2048},
        system=[
            {"type": "text", "text": system_prompt,
             "cache_control": {"type": "ephemeral"}}
        ],
        messages=[{"role": "user", "content": user_prompt}],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "result": output_schema
                    },
                    "required": ["result"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = None
    for block in response.content:
        if block.type == "tool_use" and hasattr(block, 'input'):
            result = block.input
            break

    if result is None:
        text = response.content[0].text if response.content else ""
        import json
        try:
            result = json.loads(text)
        except:
            result = {"error": "parse_failed", "raw": text[:500]}

    if use_cache:
        set_cache(cache_stage, result, system_prompt, user_prompt)

    return result
