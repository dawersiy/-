"""
论文知识图谱构建和应用 — FastAPI 启动入口
==========================================
提供 RESTful API，包括：
- 论文扫描导入
- 知识图谱查询
- 自然语言定理问答
"""

import sys
from pathlib import Path

# 将项目根目录加入 sys.path，确保模块可导入
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import get_settings

# ---------- 导入各模块 ----------
from modules.paper_loader import PaperLoader, router as paper_router
from modules.graph_store import GraphStore, router as kg_router
from modules.chat_service import ChatService, router as chat_router

# ---------- 初始化 ----------
settings = get_settings()

app = FastAPI(
    title="论文知识图谱构建和应用",
    description="本地部署的数学论文知识图谱系统 — Hello World 版",
    version="0.1.0",
)

# CORS 跨域（本地前端可直接调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.app.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- 注册路由 ----------
app.include_router(paper_router, prefix="/api", tags=["论文管理"])
app.include_router(kg_router, prefix="/api", tags=["知识图谱"])
app.include_router(chat_router, prefix="/api", tags=["智能问答"])

# ---------- 静态文件（前端） ----------
web_dir = Path(__file__).parent / "web"
if web_dir.exists():
    app.mount("/", StaticFiles(directory=str(web_dir), html=True), name="web")


# ---------- 启动入口 ----------
if __name__ == "__main__":
    import io, uvicorn
    # Windows GBK 终端不支持 emoji，强制 UTF-8 输出
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    print("=" * 55)
    print("  论文知识图谱构建和应用  启动中...")
    print(f"  图谱存储: JSON 文件 ({settings.app.data_dir})")
    print(f"  LLM    : {settings.llm.model} @ {settings.llm.base_url}")
    print(f"  论文池  : {settings.app.paper_dir}")
    print(f"  访问    : http://localhost:{settings.app.port}")
    print("=" * 55)
    uvicorn.run(app, host=settings.app.host, port=settings.app.port)
