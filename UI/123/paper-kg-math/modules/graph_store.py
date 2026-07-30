"""
图谱 CRUD 封装（JSON 文件存储版）
---------------------------------
使用内存字典 + JSON 文件持久化，零外部依赖，替代 Neo4j。
提供知识图谱的增删改查操作，包括：
- Paper / Chapter / Theorem 节点的创建
- 关系边的创建
- 图谱查询（全量、搜索、路径 BFS）
"""

import json
import threading
from pathlib import Path
from collections import deque
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from config import get_settings

# ---------- 路由 ----------
router = APIRouter()


# ---------- 图谱存储 ----------

class GraphStore:
    """
    基于 JSON 文件 + 内存字典的图谱存储（替代 Neo4j）。

    所有数据存于单一 JSON 文件中，每次变更自动持久化。
    线程安全（读写锁）。

    使用方式：
        store = GraphStore()
        store.create_theorem_node(...)
        store.create_relation(...)
        store.get_full_graph()
    """

    def __init__(self):
        settings = get_settings()
        self._file = Path(settings.app.data_dir) / "graph_data.json"
        self._file.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

        # 内存数据结构
        # nodes: dict[name] = {name, type, theorem_no, content, has_proof,
        #                       proof_text, paper_filename, chapter_id}
        # edges: list[{source, target, relation, description}]
        # papers: dict[filename] = {filename, title, path}
        # chapters: dict[chapter_id] = {chapter_id, title, paper_filename, level}
        self._data = {"nodes": {}, "edges": [], "papers": {}, "chapters": {}}
        self._load()

    # --------------------------------------------------
    # 持久化
    # --------------------------------------------------

    def _load(self):
        """从 JSON 文件加载数据到内存。"""
        if self._file.exists():
            try:
                with open(self._file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                with self._lock:
                    self._data["nodes"] = loaded.get("nodes", {})
                    self._data["edges"] = loaded.get("edges", [])
                    self._data["papers"] = loaded.get("papers", {})
                    self._data["chapters"] = loaded.get("chapters", {})
            except Exception as e:
                print(f"[WARN] 图谱数据加载失败: {e}，使用空数据")

    def _save(self):
        """将内存数据序列化到 JSON 文件。"""
        with self._lock:
            try:
                with open(self._file, "w", encoding="utf-8") as f:
                    json.dump(self._data, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"[WARN] 图谱数据保存失败: {e}")

    # ============================================================
    # 节点创建
    # ============================================================

    def create_paper_node(self, filename: str, title: str, path: str):
        """创建或更新 Paper 节点。"""
        with self._lock:
            self._data["papers"][filename] = {
                "filename": filename,
                "title": title,
                "path": path,
            }
        self._save()

    def create_chapter_node(self, chapter_id: str, title: str,
                            paper_filename: str, level: int):
        """创建或更新 Chapter 节点。"""
        with self._lock:
            self._data["chapters"][chapter_id] = {
                "chapter_id": chapter_id,
                "title": title,
                "paper_filename": paper_filename,
                "level": level,
            }
        self._save()

    def create_theorem_node(
        self,
        name: str,
        theorem_type: str,
        theorem_no: str,
        content: str,
        has_proof: bool,
        proof_text: str,
        paper_filename: str,
        chapter_id: str,
    ) -> str:
        """
        创建或更新定理节点（Definition | Theorem | Lemma | Corollary）。

        Returns:
            str: 节点名称（即 name）
        """
        valid_types = {"Definition", "Theorem", "Lemma", "Corollary"}
        if theorem_type not in valid_types:
            theorem_type = "Theorem"

        with self._lock:
            self._data["nodes"][name] = {
                "name": name,
                "type": theorem_type,
                "theorem_no": theorem_no,
                "content": content,
                "has_proof": has_proof,
                "proof_text": proof_text,
                "paper_filename": paper_filename,
                "chapter_id": chapter_id,
            }
        self._save()
        return name

    # ============================================================
    # 关系创建
    # ============================================================

    def create_relation(self, source_name: str, target_name: str,
                        relation_type: str, description: str = ""):
        """
        创建两个定理节点之间的关系边。

        支持的关系类型：
            PROVES, IMPLIES, SPECIAL_CASE_OF, GENERALIZATION_OF,
            EQUIVALENT_TO, DEPENDS_ON
        """
        valid = {"PROVES", "IMPLIES", "SPECIAL_CASE_OF",
                 "GENERALIZATION_OF", "EQUIVALENT_TO", "DEPENDS_ON"}
        if relation_type not in valid:
            return

        with self._lock:
            # 检查源和目标节点是否存在
            if source_name not in self._data["nodes"]:
                return
            if target_name not in self._data["nodes"]:
                return

            # 避免重复边
            for e in self._data["edges"]:
                if (e["source"] == source_name and e["target"] == target_name
                        and e["relation"] == relation_type):
                    e["description"] = description  # 更新描述
                    self._save()
                    return

            self._data["edges"].append({
                "source": source_name,
                "target": target_name,
                "relation": relation_type,
                "description": description,
            })
        self._save()

    # ============================================================
    # 查询
    # ============================================================

    def get_full_graph(self) -> dict:
        """
        获取全量图谱数据（节点 + 边），供前端力导向图渲染。

        Returns:
            dict: {"nodes": [...], "edges": [...]}
        """
        with self._lock:
            nodes = []
            for name, n in self._data["nodes"].items():
                # 关联论文信息
                pfn = n.get("paper_filename", "")
                paper = self._data["papers"].get(pfn, {})
                nodes.append({
                    "name": name,
                    "type": n["type"],
                    "content": (n.get("content", "") or "")[:200],
                    "theorem_no": n.get("theorem_no", "") or "",
                    "paper_filename": pfn,
                    "paper_title": paper.get("title", pfn),
                    "paper_path": paper.get("path", ""),
                })

            edges = []
            for e in self._data["edges"]:
                edges.append({
                    "source": e["source"],
                    "target": e["target"],
                    "relation": e["relation"],
                    "description": e.get("description", "") or "",
                })

        return {"nodes": nodes, "edges": edges}

    def search_nodes(self, keyword: str) -> list[dict]:
        """
        按关键词搜索定理节点（模糊匹配名称和内容）。

        Args:
            keyword: 搜索关键词

        Returns:
            list[dict]: 匹配的节点列表（最多 20 个）
        """
        keyword_lower = keyword.lower()
        results = []
        with self._lock:
            for name, n in self._data["nodes"].items():
                if (keyword_lower in name.lower()
                        or keyword_lower in n.get("content", "").lower()):
                    results.append({
                        "name": name,
                        "type": n["type"],
                        "content": (n.get("content", "") or "")[:300],
                        "theorem_no": n.get("theorem_no", "") or "",
                        "has_proof": n.get("has_proof", False),
                    })
                if len(results) >= 20:
                    break
        return results

    def find_proof_dependencies(self, theorem_name: str,
                                max_depth: int = 5) -> list[dict]:
        """
        多跳回溯查询某个定理的证明依赖链（BFS）。

        沿着 PROVES 和 DEPENDS_ON 关系反向追溯，
        找到证明该定理所需的所有前置定理/定义。

        Args:
            theorem_name: 目标定理名称
            max_depth: 最大追溯深度

        Returns:
            list[dict]: 依赖路径列表
        """
        with self._lock:
            if theorem_name not in self._data["nodes"]:
                return []

            # 构建"依赖链"邻接表：adj[X] = X 直接依赖的前置节点列表
            # PROVES:    A -[PROVES]-> B  → B 的证明用了 A → B 依赖 A → adj[B] += A
            # DEPENDS_ON: A -[DEPENDS_ON]-> B → A 依赖 B         → adj[A] += B
            adj = {}  # node_name -> [(neighbor_name, relation_type, description)]
            for e in self._data["edges"]:
                if e["relation"] == "PROVES":
                    adj.setdefault(e["target"], []).append(
                        (e["source"], e["relation"], e.get("description", ""))
                    )
                elif e["relation"] == "DEPENDS_ON":
                    adj.setdefault(e["source"], []).append(
                        (e["target"], e["relation"], e.get("description", ""))
                    )

            # BFS
            visited = {theorem_name}
            queue = deque([(theorem_name, [], [])])  # (node, node_path, rel_path)
            paths = []

            while queue and len(paths) < 30:
                node, node_path, rel_path = queue.popleft()
                depth = len(rel_path)

                if depth >= max_depth:
                    continue

                for neighbor, rel_type, desc in adj.get(node, []):
                    if neighbor in visited and depth + 1 > 0:
                        pass  # 允许重复访问不同路径
                    new_node_path = node_path + [neighbor]
                    new_rel_path = rel_path + [{
                        "type": rel_type,
                        "description": desc,
                        "source": node,
                        "target": neighbor,
                    }]

                    node_info = self._data["nodes"].get(neighbor, {})
                    path_nodes = []
                    # 起点
                    start_info = self._data["nodes"].get(theorem_name, {})
                    path_nodes.append({
                        "name": theorem_name,
                        "type": start_info.get("type", ""),
                    })
                    # 中间节点
                    for np_name in new_node_path:
                        ni = self._data["nodes"].get(np_name, {})
                        path_nodes.append({
                            "name": np_name,
                            "type": ni.get("type", ""),
                        })

                    paths.append({
                        "nodes": path_nodes,
                        "relations": [
                            {"type": r["type"],
                             "description": r["description"]}
                            for r in new_rel_path
                        ],
                        "depth": len(new_rel_path),
                    })

                    # 将邻居也加入 BFS（控制深度防止爆炸）
                    new_visited = set()
                    new_visited.add(theorem_name)
                    new_visited.update(new_node_path)
                    if neighbor not in new_visited:
                        queue.append((neighbor, new_node_path, new_rel_path))

                if len(paths) >= 30:
                    break

        return paths

    def find_path_between(self, source: str, target: str,
                          max_depth: int = 4) -> list[dict]:
        """
        查询两个定理之间的最短推导路径（BFS）。

        Args:
            source: 起点定理名称
            target: 终点定理名称
            max_depth: 最大搜索深度

        Returns:
            list[dict]: 路径列表
        """
        with self._lock:
            if source not in self._data["nodes"]:
                return []
            if target not in self._data["nodes"]:
                return []

            # 构建无向邻接表（因为路径查询不区分关系方向）
            adj = {}
            for e in self._data["edges"]:
                adj.setdefault(e["source"], []).append(
                    (e["target"], e["relation"], e.get("description", ""))
                )
                adj.setdefault(e["target"], []).append(
                    (e["source"], e["relation"], e.get("description", ""))
                )

            # BFS 最短路径
            queue = deque([(source, [source], [])])  # (node, node_path, rel_path)
            visited = {source}
            paths = []

            while queue and len(paths) < 5:
                node, node_path, rel_path = queue.popleft()

                if len(rel_path) >= max_depth:
                    continue

                for neighbor, rel_type, desc in adj.get(node, []):
                    if neighbor == target:
                        # 找到路径
                        final_node_path = node_path + [neighbor]
                        final_rel_path = rel_path + [{
                            "type": rel_type,
                            "description": desc,
                            "source": node,
                            "target": neighbor,
                        }]
                        path_nodes = []
                        for np_name in final_node_path:
                            ni = self._data["nodes"].get(np_name, {})
                            path_nodes.append({
                                "name": np_name,
                                "type": ni.get("type", ""),
                            })
                        path_rels = []
                        for r in final_rel_path:
                            path_rels.append({
                                "type": r["type"],
                                "source": r["source"],
                                "target": r["target"],
                                "description": r["description"],
                            })
                        paths.append({
                            "nodes": path_nodes,
                            "relations": path_rels,
                            "depth": len(final_rel_path),
                        })
                        if len(paths) >= 5:
                            break
                    elif neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((
                            neighbor,
                            node_path + [neighbor],
                            rel_path + [{
                                "type": rel_type,
                                "description": desc,
                                "source": node,
                                "target": neighbor,
                            }],
                        ))

                if len(paths) >= 5:
                    break

        return paths

    def clear_all(self):
        """清空图谱中所有节点和关系。"""
        with self._lock:
            self._data = {"nodes": {}, "edges": [], "papers": {}, "chapters": {}}
        self._save()


# ============================================================
# API 接口
# ============================================================

@router.get("/kg/graph")
async def get_graph():
    """获取全量图谱数据（节点 + 边）"""
    store = GraphStore()
    return store.get_full_graph()


@router.get("/kg/search")
async def search_theorems(q: str = Query("", description="搜索关键词")):
    """搜索定理节点"""
    if not q.strip():
        return {"nodes": []}
    store = GraphStore()
    nodes = store.search_nodes(q.strip())
    return {"nodes": nodes}


@router.get("/kg/dependencies")
async def get_dependencies(name: str = Query(..., description="定理名称")):
    """获取定理的证明依赖链"""
    store = GraphStore()
    return {"paths": store.find_proof_dependencies(name)}


@router.get("/kg/path")
async def get_path(source: str = Query(...), target: str = Query(...)):
    """查询两个定理之间的推导路径"""
    store = GraphStore()
    return {"paths": store.find_path_between(source, target)}


@router.post("/kg/clear")
async def clear_graph():
    """清空图谱"""
    store = GraphStore()
    store.clear_all()
    return {"status": "ok", "message": "图谱已清空"}


@router.post("/kg/merge-definitions")
async def merge_definitions():
    """
    AI 语义去重：找出所有 Definition 节点中语义相同的，合并为唯一公理。
    只发送定义名称到 LLM 进行语义分组（不发送内容以减少 token 和避免 LaTeX 转义问题）。
    超过 200 个定义时分批处理。
    """
    from modules.llm_client import LLMClient

    store = GraphStore()

    # 收集所有 Definition 节点名称
    with store._lock:
        defs = [
            {"name": name, "content": n.get("content", "")[:300]}
            for name, n in store._data["nodes"].items()
            if n.get("type") == "Definition"
        ]

    if len(defs) < 2:
        return {"status": "ok", "message": "定义节点不足 2 个，无需合并", "groups": [], "count": len(defs)}

    # 分批处理：每批最多 200 个定义名
    BATCH_SIZE = 200
    def_names = [d["name"] for d in defs]
    all_groups = []
    seen = set()

    system_prompt = """你是一位数学知识图谱专家。分析以下数学定义（公理）名称列表，
找出语义相同的定义并分组。

## 输出格式（纯 JSON，不要 markdown 包裹）

{
  "groups": [
    {
      "canonical_name": "统一规范名称",
      "members": ["相同定义1", "相同定义2"],
      "reason": "一句话理由"
    }
  ],
  "singletons": ["独一无二的名称"]
}

## 规则
1. 只合并语义完全相同的概念（如不同论文中的"连续函数"定义）
2. canonical_name 取最通用的表述
3. 不要强行合并不同概念"""

    for batch_start in range(0, len(def_names), BATCH_SIZE):
        batch = def_names[batch_start:batch_start + BATCH_SIZE]
        if len(batch) < 2 and batch_start == 0:
            continue

        batch_list = "\n".join(f"- {n}" for n in batch)
        user_message = f"定义名称列表（只根据名称语义判断，不要补充内容）：\n\n{batch_list}"

        llm = LLMClient()
        # 临时增大 max_tokens 以便返回完整的 JSON
        llm.max_tokens = 16384
        result = llm.chat_json(system_prompt, user_message)
        llm.max_tokens = 4096  # 恢复默认

        if not result:
            # 该批失败 → 全部当作 singletons
            for n in batch:
                if n not in seen:
                    all_groups.append({
                        "canonical_name": n,
                        "members": [n],
                        "reason": "",
                    })
                    seen.add(n)
            continue

        for g in result.get("groups", []):
            for m in g.get("members", []):
                seen.add(m)
            all_groups.append(g)

        for s in result.get("singletons", []):
            if s not in seen:
                all_groups.append({
                    "canonical_name": s,
                    "members": [s],
                    "reason": "",
                })
                seen.add(s)

    # 确保所有定义都被覆盖
    for n in def_names:
        if n not in seen:
            all_groups.append({
                "canonical_name": n,
                "members": [n],
                "reason": "",
            })
            seen.add(n)

    # 为每个 group 补充完整信息（论文、内容等）
    merged = []
    merge_count = 0
    for g in all_groups:
        papers = []
        contents = []
        for m in g.get("members", []):
            node = store._data["nodes"].get(m, {})
            pfn = node.get("paper_filename", "")
            paper = store._data["papers"].get(pfn, {})
            if paper.get("title") and paper["title"] not in papers:
                papers.append(paper["title"])
            contents.append(node.get("content", "")[:150])

        mc = len(g.get("members", []))
        if mc > 1:
            merge_count += 1

        merged.append({
            "name": g.get("canonical_name", g["members"][0]),
            "type": "Definition",
            "merged_count": mc,
            "members": g.get("members", []),
            "reason": g.get("reason", ""),
            "papers": papers,
            "content": max(contents, key=len) if contents else "",
        })

    # 按合并数降序排列，合并多的在前面
    merged.sort(key=lambda x: -x["merged_count"])

    return {
        "status": "ok",
        "message": f"合并完成：{len(def_names)} 个定义 → {len(merged)} 个唯一公理（{merge_count} 组合并）",
        "groups": merged,
        "original_count": len(def_names),
        "merged_count": len(merged),
    }
