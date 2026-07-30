"""
自然语言问答服务
----------------
前端对话接口的后端实现。接收用户自然语言问题，
调用推理引擎，返回带图谱联动的回答。
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from modules.reasoning_engine import ReasoningEngine

# ---------- 路由 ----------
router = APIRouter()


# ---------- 数据模型 ----------

class ChatRequest(BaseModel):
    """对话请求"""
    question: str = Field(..., min_length=1, max_length=2000,
                          description="用户的自然语言问题")
    stream: bool = Field(False, description="是否使用流式返回（Hello World 版暂不实现）")


class ChatResponse(BaseModel):
    """对话响应"""
    answer: str = Field(..., description="markdown 格式的回答")
    highlight_nodes: list[str] = Field(
        default_factory=list,
        description="需要在图谱中高亮的节点名称列表"
    )
    graph_context: dict = Field(
        default_factory=dict,
        description="相关的图谱子图数据（供前端联动）"
    )


# ---------- 对话服务 ----------

class ChatService:
    """
    自然语言问答服务。

    封装了推理引擎调用，提供统一的问答接口。

    使用方式：
        service = ChatService()
        response = service.ask("微积分第一基本定理是什么？")
    """

    def __init__(self):
        self.engine = ReasoningEngine()

    def ask(self, question: str) -> ChatResponse:
        """
        回答用户的数学问题。

        处理流程：
            1. 关键词提取
            2. 图谱查询
            3. LLM 推理

        Args:
            question: 用户自然语言问题

        Returns:
            ChatResponse: 包含回答、高亮节点和图谱上下文
        """
        result = self.engine.reason(question)
        return ChatResponse(
            answer=result["answer"],
            highlight_nodes=result["highlight_nodes"],
            graph_context=result["graph_context"],
        )


# ============================================================
# API 接口
# ============================================================

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """
    自然语言问答接口。

    接收用户问题，返回 LLM + 图谱增强的回答。

    请求示例:
        POST /api/chat
        {
            "question": "微积分基本定理是什么？",
            "stream": false
        }

    响应示例:
        {
            "answer": "微积分基本定理...",
            "highlight_nodes": ["微积分第一基本定理", ...],
            "graph_context": {...}
        }
    """
    try:
        service = ChatService()
        return service.ask(req.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"问答处理失败: {str(e)}")
