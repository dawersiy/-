"""
论文扫描与 Markdown 数学解析模块
--------------------------------
功能：
1. 扫描本地论文池目录，发现 .md 论文文件
2. 解析 Markdown 结构：识别章节、定义、定理、证明等
3. 将解析结果转化为结构化数据，供 LLM 抽取器使用
"""

import re
import time
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from config import get_settings

# ---------- 路由 ----------
router = APIRouter()


# ---------- 数据模型 ----------
class PaperMeta(BaseModel):
    """论文元信息"""
    filename: str
    title: str
    path: str
    content: str
    size_bytes: int
    modified_at: float


class PaperInfo(BaseModel):
    """返回给前端的论文摘要信息"""
    filename: str
    title: str
    path: str
    size_bytes: int
    chapter_count: int
    modified_at: float


# ---------- 论文加载器 ----------
class PaperLoader:
    """
    论文加载器：扫描本地目录，读取 Markdown 论文，解析基本结构。

    使用方式：
        loader = PaperLoader(paper_dir)
        papers = loader.scan()        # 扫描目录，返回 PaperMeta 列表
        chunks  = loader.parse(paper) # 将论文按章节分块
    """

    # Markdown 标题匹配正则（## 表示章节，### 表示小节）
    HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)

    def __init__(self, paper_dir: Optional[str] = None):
        settings = get_settings()
        self.paper_dir = Path(paper_dir or settings.app.paper_dir)
        if not self.paper_dir.exists():
            self.paper_dir.mkdir(parents=True, exist_ok=True)

    def scan(self) -> list[PaperMeta]:
        """
        扫描论文目录，返回所有 .md 文件的元信息。

        Returns:
            list[PaperMeta]: 论文元信息列表
        """
        papers: list[PaperMeta] = []
        for md_file in self.paper_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                title = self._extract_title(content)
                stat = md_file.stat()
                papers.append(PaperMeta(
                    filename=md_file.name,
                    title=title,
                    path=str(md_file.absolute()),
                    content=content,
                    size_bytes=stat.st_size,
                    modified_at=stat.st_mtime,
                ))
            except Exception as e:
                print(f"[WARN] 读取文件失败: {md_file} — {e}")
        return papers

    @staticmethod
    def parse_chapters(content: str) -> list[dict]:
        """
        将 Markdown 内容按标题拆分为章节块。

        每个章节块包含：
            - level: 标题层级 (1-4)
            - title: 章节标题
            - body:  章节正文
            - start: 在原文字符串中的起始位置

        Args:
            content: 论文 Markdown 全文

        Returns:
            list[dict]: 章节块列表
        """
        heading_pattern = re.compile(
            r"^(#{1,4})\s+(.+)$", re.MULTILINE
        )
        matches = list(heading_pattern.finditer(content))

        if not matches:
            # 全文没有标题 → 整体作为一个块
            return [{"level": 1, "title": "正文", "body": content.strip(), "start": 0}]

        chapters = []
        for i, m in enumerate(matches):
            level = len(m.group(1))
            title = m.group(2).strip()
            start = m.end() + 1  # 换行后开始
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            body = content[start:end].strip()
            chapters.append({
                "level": level,
                "title": title,
                "body": body,
                "start": start,
            })
        return chapters

    @staticmethod
    def _extract_title(content: str) -> str:
        """从 Markdown 中提取论文标题（第一个 # 标题行）"""
        m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        return m.group(1).strip() if m else "（无标题）"


# ---------- API 接口 ----------

@router.get("/papers", response_model=list[PaperInfo])
async def list_papers():
    """获取已扫描到的论文列表"""
    loader = PaperLoader()
    papers = loader.scan()
    return [
        PaperInfo(
            filename=p.filename,
            title=p.title,
            path=p.path,
            size_bytes=p.size_bytes,
            chapter_count=len(PaperLoader.parse_chapters(p.content)),
            modified_at=p.modified_at,
        )
        for p in papers
    ]


@router.post("/papers/scan")
async def scan_and_import(
    max_papers: int = Query(3, description="最多处理论文数（0=全部）"),
):
    """
    扫描论文池并导入图谱。
    核心触发接口：扫描 → LLM 抽取 → 写入图谱。
    LLM 调用失败时跳过该章节，不中断整体流程。
    """
    import sys
    from modules.llm_client import LLMClient
    from modules.theorem_extractor import TheoremExtractor
    from modules.graph_store import GraphStore

    loader = PaperLoader()
    papers = loader.scan()

    if not papers:
        return {"status": "ok", "message": "论文池为空，未发现 .md 文件", "count": 0}

    # 限制数量——先处理短论文，快速看到结果
    papers = sorted(papers, key=lambda p: p.size_bytes)
    if max_papers > 0:
        papers = papers[:max_papers]

    llm = LLMClient()
    extractor = TheoremExtractor(llm)
    store = GraphStore()

    total_theorems = 0
    total_relations = 0
    failed_chapters = 0
    errors: list[str] = []

    for i, paper in enumerate(papers, 1):
        msg = f"[PAPER {i}/{len(papers)}] 处理: {paper.title} ({paper.size_bytes}B)"
        print(msg, flush=True)

        chapters = PaperLoader.parse_chapters(paper.content)
        store.create_paper_node(paper.filename, paper.title, paper.path)

        for ch in chapters:
            # 对每个章节调用 LLM 抽取定理，失败则跳过该章节
            try:
                result = extractor.extract(ch["body"], chapter_title=ch["title"])
            except Exception as e:
                failed_chapters += 1
                err_msg = f"章节「{ch['title']}」抽取失败: {str(e)[:100]}"
                print(f"  [SKIP] {err_msg}", flush=True)
                errors.append(err_msg)
                continue

            if not result:
                continue

            store.create_chapter_node(
                chapter_id=f"{paper.filename}::{ch['title']}",
                title=ch["title"],
                paper_filename=paper.filename,
                level=ch["level"],
            )

            # 写入定理节点
            for th in result.get("theorems", []):
                store.create_theorem_node(
                    name=th["name"],
                    theorem_type=th.get("type", "Theorem"),
                    theorem_no=th.get("theorem_no", ""),
                    content=th.get("content", ""),
                    has_proof=th.get("has_proof", False),
                    proof_text=th.get("proof_text", ""),
                    paper_filename=paper.filename,
                    chapter_id=f"{paper.filename}::{ch['title']}",
                )
                total_theorems += 1

            # 写入关系边
            for rel in result.get("relations", []):
                store.create_relation(
                    source_name=rel["source_name"],
                    target_name=rel["target_name"],
                    relation_type=rel.get("relation", "DEPENDS_ON"),
                    description=rel.get("description", ""),
                )
                total_relations += 1

        print(f"  -> 累计: {total_theorems} 定理, {total_relations} 关系", flush=True)

    msg = f"扫描完成：{len(papers)} 篇论文，{total_theorems} 定理，{total_relations} 关系"
    if failed_chapters:
        msg += f"（{failed_chapters} 个章节因 LLM 失败跳过）"

    print(f"\n{'='*50}\n{msg}\n{'='*50}", flush=True)

    return {
        "status": "ok",
        "message": msg,
        "papers": len(papers),
        "theorems": total_theorems,
        "relations": total_relations,
        "failed_chapters": failed_chapters,
        "errors": errors[:5],
    }
