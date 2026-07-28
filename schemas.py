"""Pydantic数据模型 — 知识图谱Item和Network"""

from pydantic import BaseModel, Field
from typing import Literal, Optional

ItemType = Literal["theorem", "lemma", "corollary", "definition", "proposition", "formula"]
RelationType = Literal["derives", "generalizes", "depends", "equivalent", "none"]

class Relation(BaseModel):
    target_id: str
    type: RelationType
    note: str = ""
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)

class SourceDetail(BaseModel):
    paper_id: str
    title: str = ""
    year: str = ""

class KnowledgeItem(BaseModel):
    id: str
    type: ItemType
    name: str
    latex: str = ""
    statement: str = ""
    sources: list[str] = []
    source_detail: list[SourceDetail] = []
    keywords: list[str] = []
    relations: list[Relation] = []

    # --- LLM enriched fields ---
    summary: str = ""               # 1-3句中文摘要
    premises: str = ""              # 定理前提条件 (自然语言)
    conclusion: str = ""            # 核心结论 (自然语言)
    domain: list[str] = []          # 层级领域标签
    confidence: float = 0.0         # 提取置信度 0-1
    proof_technique: str = ""       # 证明技巧

class PaperMeta(BaseModel):
    id: str
    title: str
    year: str

class NetworkStatistics(BaseModel):
    total_papers: int = 0
    total_items: int = 0
    total_relations: int = 0
    items_by_type: dict[str, int] = {}
    relations_by_type: dict[str, int] = {}
    merge_count: int = 0

class KnowledgeNetwork(BaseModel):
    network_name: str = "Optimization Theory Knowledge Network"
    description: str = ""
    statistics: NetworkStatistics = NetworkStatistics()
    papers: list[PaperMeta] = []
    items: list[KnowledgeItem] = []
    merge_records: list[dict] = []
    relations_summary: list[dict] = []
