"""布局引擎 — 中心辐射 + 关系距离 + 无重叠"""

import math, random
from collections import deque
from config import LAYOUT_WIDTH, LAYOUT_HEIGHT

CX, CY = LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2
MAX_RADIUS = min(LAYOUT_WIDTH, LAYOUT_HEIGHT) / 2 - 40

# 类型对应的节点视觉大小
NODE_SIZE = {'theorem': 14, 'lemma': 12, 'corollary': 10, 'definition': 13, 'proposition': 12}
MIN_GAP = 8  # 节点间最小额外间距

def compute_layout(nodes: list[dict], links: list[dict]) -> list[dict]:
    """中心辐射布局: 关系近的节点距离近, 无重叠"""
    n = len(nodes)
    if n == 0:
        return nodes

    # ---- 1. 构建邻接表 + 计算度 ----
    adj = [[] for _ in range(n)]
    degree = [0] * n
    for lk in links:
        si, ti = lk.get('source_index', 0), lk.get('target_index', 0)
        if 0 <= si < n and 0 <= ti < n and si != ti:
            adj[si].append(ti); adj[ti].append(si)
            degree[si] += 1; degree[ti] += 1

    # ---- 2. BFS 计算每个节点到"核心"的图距离 ----
    # 核心 = 度最高的 top 5 节点
    sorted_idx = sorted(range(n), key=lambda i: degree[i], reverse=True)
    cores = sorted_idx[:max(5, n // 20)]

    depth = [-1] * n
    q = deque()
    for c in cores:
        depth[c] = 0
        q.append(c)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                q.append(v)

    # 未连通的节点给最大深度
    max_depth = max(depth) if any(d >= 0 for d in depth) else 1
    for i in range(n):
        if depth[i] == -1:
            depth[i] = max_depth + 1

    # ---- 3. 按深度分组, 每组均匀分布在一个环上 ----
    rings = {}
    for i in range(n):
        d = depth[i]
        rings.setdefault(d, []).append(i)

    max_ring = max(rings.keys()) if rings else 0
    positions = [[0.0, 0.0] for _ in range(n)]

    for d, members in rings.items():
        if max_ring == 0:
            radius_frac = 0
        else:
            radius_frac = d / max_ring
        radius = 40 + radius_frac * (MAX_RADIUS - 40)  # 内环留空给核心
        m = len(members)

        # 环形均匀分布, 加微小随机偏移
        for k, node_idx in enumerate(members):
            angle = (2 * math.pi * k / m) + random.uniform(-0.05, 0.05)
            # 核心节点略微随机化角度避免整齐排列
            if d == 0:
                angle = random.uniform(0, 2 * math.pi)
                radius = random.uniform(30, MAX_RADIUS * 0.15)
            positions[node_idx] = [CX + radius * math.cos(angle),
                                   CY + radius * math.sin(angle)]

    # ---- 4. 弹簧精调: 加权边, 权重高则距离近 ----
    # 将links转为带权重的边列表
    weighted_edges = []
    for lk in links:
        u, v = lk.get('source_index', 0), lk.get('target_index', 0)
        w = lk.get('weight', 1.0)
        if 0 <= u < n and 0 <= v < n and u != v:
            weighted_edges.append((u, v, w))

    for _ in range(120):
        forces = [[0.0, 0.0] for _ in range(n)]

        # 引力: 权重越高目标距离越近
        for u, v, w in weighted_edges:
            dx = positions[v][0] - positions[u][0]
            dy = positions[v][1] - positions[u][1]
            dist = max(math.sqrt(dx*dx + dy*dy), 1.0)
            # 权重映射: w=1.0→40px, w=0.5→100px, w=0.15→180px
            target = 40 + (1.0 - w) * 200
            f = 0.012 * w * (dist - target)
            fx, fy = (dx/dist)*f, (dy/dist)*f
            forces[u][0] += fx; forces[u][1] += fy
            forces[v][0] -= fx; forces[v][1] -= fy

        # 斥力: 仅防重叠 (网格加速)
        grid = {}
        gs = 100
        for i in range(n):
            gx, gy = int(positions[i][0]/gs), int(positions[i][1]/gs)
            grid.setdefault((gx,gy), []).append(i)

        for i in range(n):
            gx, gy = int(positions[i][0]/gs), int(positions[i][1]/gs)
            sz_i = NODE_SIZE.get(nodes[i]['type'], 12) + MIN_GAP
            for dgx in (-1,0,1):
                for dgy in (-1,0,1):
                    for j in grid.get((gx+dgx, gy+dgy), []):
                        if j <= i: continue
                        dx = positions[i][0] - positions[j][0]
                        dy = positions[i][1] - positions[j][1]
                        dist = max(math.sqrt(dx*dx + dy*dy), 1.0)
                        sz_j = NODE_SIZE.get(nodes[j]['type'], 12) + MIN_GAP
                        min_d = sz_i + sz_j
                        if dist < min_d:
                            f = 3.0 * (min_d - dist) / dist
                            forces[i][0] += (dx/dist)*f
                            forces[i][1] += (dy/dist)*f
                            forces[j][0] -= (dx/dist)*f
                            forces[j][1] -= (dy/dist)*f

        # 弱中心引力, 保持辐射结构
        for i in range(n):
            dx = CX - positions[i][0]
            dy = CY - positions[i][1]
            dist = max(math.sqrt(dx*dx + dy*dy), 1.0)
            # 根据深度确定目标半径
            d = depth[i]
            if max_ring > 0:
                target_r = 40 + (d / max_ring) * (MAX_RADIUS - 40)
            else:
                target_r = 0
            actual_r = math.sqrt((positions[i][0]-CX)**2 + (positions[i][1]-CY)**2)
            if actual_r > 10:
                f = 0.01 * (target_r - actual_r)
                positions[i][0] += (positions[i][0]-CX)/actual_r * f
                positions[i][1] += (positions[i][1]-CY)/actual_r * f

        # 更新位置
        for i in range(n):
            positions[i][0] += forces[i][0]
            positions[i][1] += forces[i][1]
            positions[i][0] = max(20, min(LAYOUT_WIDTH-20, positions[i][0]))
            positions[i][1] = max(20, min(LAYOUT_HEIGHT-20, positions[i][1]))

    # ---- 5. 最终硬去重 ----
    _hard_fix(nodes, positions)

    for i, node in enumerate(nodes):
        node['x'] = round(positions[i][0], 2)
        node['y'] = round(positions[i][1], 2)

    return nodes

def _hard_fix(nodes, positions):
    """最后一轮: 暴力推开所有重叠节点"""
    n = len(nodes)
    for _ in range(50):
        moved = False
        for i in range(n):
            sz_i = NODE_SIZE.get(nodes[i]['type'], 12) + MIN_GAP
            for j in range(i+1, n):
                dx = positions[i][0] - positions[j][0]
                dy = positions[i][1] - positions[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                sz_j = NODE_SIZE.get(nodes[j]['type'], 12) + MIN_GAP
                if dist < sz_i + sz_j and dist > 0.001:
                    overlap = (sz_i + sz_j - dist) / 2
                    nx, ny = (dx/dist)*overlap, (dy/dist)*overlap
                    positions[i][0] += nx; positions[i][1] += ny
                    positions[j][0] -= nx; positions[j][1] -= ny
                    moved = True
        if not moved:
            break

    for i in range(n):
        positions[i][0] = max(20, min(LAYOUT_WIDTH-20, positions[i][0]))
        positions[i][1] = max(20, min(LAYOUT_HEIGHT-20, positions[i][1]))
