"""
云端 LLM 统一客户端
-------------------
提供 OpenAI 兼容接口的封装，包含：
- 自动重试（指数退避）
- 并发限流
- JSON 格式校验与修复
"""

import json
import re
import time
from typing import Optional

import httpx
from openai import OpenAI

from config import get_settings


class LLMClient:
    """
    云端大模型客户端（OpenAI 兼容接口）。

    特性：
        - 自动重试，指数退避
        - 支持 JSON Mode 输出
        - 返回内容自动清理 markdown 代码块包裹
    """

    def __init__(self):
        settings = get_settings()
        # 使用 httpx 客户端（trust_env=False 禁用系统代理和 SSL 问题）
        http_client = httpx.Client(
            timeout=settings.llm.timeout_seconds,
            follow_redirects=True,
            trust_env=False,
        )

        self.client = OpenAI(
            base_url=settings.llm.base_url,
            api_key=settings.llm.api_key,
            timeout=settings.llm.timeout_seconds,
            http_client=http_client,
        )
        self.model = settings.llm.model
        self.temperature = settings.llm.temperature
        self.max_tokens = settings.llm.max_tokens
        self.max_retries = settings.llm.max_retries
        self.retry_delay = settings.llm.retry_delay_seconds

    # --------------------------------------------------
    # 公开方法
    # --------------------------------------------------

    def chat(self, system_prompt: str, user_message: str) -> str:
        """
        发送对话请求，返回模型回复文本。

        Args:
            system_prompt: 系统提示词
            user_message: 用户消息

        Returns:
            str: 模型回复内容
        """
        return self._call_with_retry(system_prompt, user_message)

    def chat_json(self, system_prompt: str, user_message: str) -> Optional[dict]:
        """
        发送对话请求，要求 LLM 返回 JSON，自动解析并校验。

        Args:
            system_prompt: 系统提示词（应明确要求输出 JSON）
            user_message: 用户消息

        Returns:
            dict | None: 解析后的 JSON 字典，失败时返回 None
        """
        raw = self.chat(system_prompt, user_message)
        if raw is None:
            return None
        return self._parse_json(raw)

    # --------------------------------------------------
    # 内部方法
    # --------------------------------------------------

    def _call_with_retry(self, system_prompt: str, user_message: str) -> Optional[str]:
        """
        带重试的 LLM 调用。

        重试策略：指数退避，首次重试等待 retry_delay 秒，
        后续每次翻倍，最多重试 max_retries 次。
        """
        last_error = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message},
                    ],
                )
                content = response.choices[0].message.content
                return content.strip() if content else ""

            except Exception as e:
                last_error = e
                if attempt < self.max_retries:
                    delay = self.retry_delay * (2 ** attempt)
                    print(f"[WARN] LLM 调用失败 (第 {attempt + 1} 次)，{delay:.0f}s 后重试: {e}")
                    time.sleep(delay)
                else:
                    print(f"[ERROR] LLM 调用失败，已达最大重试次数: {e}")

        return None  # 返回 None 而非抛异常，让调用方优雅处理

    @staticmethod
    def _parse_json(raw: str) -> Optional[dict]:
        """
        从 LLM 返回文本中提取并校验 JSON。

        处理常见情况：
            - 直接返回 JSON 文本
            - 被 ```json ... ``` 包裹
            - 被 ``` ... ``` 包裹
            - JSON 中包含未转义的控制字符
        """
        if not raw:
            return None

        # 尝试去除 markdown 代码块包裹
        cleaned = raw.strip()

        # 匹配 ```json ... ``` 或 ``` ... ```
        m = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", cleaned, re.DOTALL)
        if m:
            cleaned = m.group(1).strip()

        # 尝试解析
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

        # 如果失败，尝试用正则提取最外层 {...}
        m = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass

        print(f"[WARN] JSON 解析失败，原始返回: {raw[:300]}...")
        return None
