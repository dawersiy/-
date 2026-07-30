"""
配置管理模块
-----------
从 .env 文件读取所有配置项，提供统一的 Settings 单例。
禁止在代码中硬编码密钥、URL 等敏感信息。
"""

import os
from pathlib import Path
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# 自动加载项目根目录的 .env 文件
ENV_FILE = Path(__file__).parent / ".env"
load_dotenv(ENV_FILE)


class LLMConfig(BaseModel):
    """云端大模型连接配置（兼容 OpenAI 接口）"""
    base_url: str = Field(
        default_factory=lambda: os.getenv("LLM_BASE_URL", "https://api.openai.com/v1"),
        description="LLM API 地址（兼容 OpenAI 格式）"
    )
    api_key: str = Field(
        default_factory=lambda: os.getenv("LLM_API_KEY", "sk-placeholder"),
        description="LLM API 密钥"
    )
    model: str = Field(
        default_factory=lambda: os.getenv("LLM_MODEL", "gpt-4o"),
        description="模型名称"
    )
    temperature: float = 0.3
    max_tokens: int = 4096
    timeout_seconds: int = 120
    max_retries: int = 3
    retry_delay_seconds: float = 2.0


class AppConfig(BaseModel):
    """应用全局配置"""
    paper_dir: str = Field(
        default_factory=lambda: os.getenv("PAPER_DIR", r"D:\AI\文献资料"),
        description="论文池本地目录"
    )
    data_dir: str = Field(
        default_factory=lambda: os.getenv("DATA_DIR",
                                          str(Path(__file__).parent / "data")),
        description="图谱 JSON 数据存储目录"
    )
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: list[str] = ["*"]


class Settings(BaseModel):
    """统一配置入口"""
    llm: LLMConfig = LLMConfig()
    app: AppConfig = AppConfig()


@lru_cache()
def get_settings() -> Settings:
    """
    获取全局配置单例。

    使用 lru_cache 确保全局只初始化一次，类似单例模式。

    Returns:
        Settings: 包含所有配置项的 Settings 实例
    """
    return Settings()
