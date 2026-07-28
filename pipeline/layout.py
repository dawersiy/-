"""服务端预计算力导向布局 — 网格加速斥力, 多阶段退火确保节点均匀分布"""

import math, random
from config import LAYOUT_WIDTH, LAYOUT_HEIGHT

# 类型中心 — 分布在画布中央周围, 避免偏向角落
CX, CY = LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2
TYPE_CENTERS = {
    'theorem':     (CX + 100, CY - 80),
    'lemma':       (CX - 120, CY + 60),
    'corollary':   (CX + 80,  CY + 120),
    'definition':  (CX - 100, CY - 100),
    'proposition': (CX - 60,  CY + 20),
}

MIN_DIST = {
    'theorem': 55, 'lemma': 45, 'corollary': 40,
    'definition': 50, 'proposition': 45,
}

def compute_layout(nodes: list[dict], links: list[dict], iterations: int = 800) -> list[dict]:
    """预计算力导向布局 — 多阶段退火, 防止角落聚集"""
    n = len(nodes)
    if n == 0:
        return nodes

    # 初始化: 类型中心 + 随机偏移
    positions = []
    for node in nodes:
        cx, cy = TYPE_CENTERS.get(node['type'], (CX, CY))
        positions.append([cx + random.uniform(-80, 80), cy + random.uniform(-80, 80)])

    # 邻接表
    adj = [[] for _ in range(n)]
    for link in links:
        si = link.get('source_index', 0)
        ti = link.get('target_index', 0)
        if 0 <= si < n and 0 <= ti < n and si != ti:
            adj[si].append(ti)
            adj[ti].append(si)

    grid_size = 80

    # ---- 阶段1: 高温扩散 (200轮) ----
    _run_phase(positions, nodes, adj, grid_size, iterations=200,
               repulsion=6000, attraction=0.003, center=0.08,
               global_center=0.02, damping=0.9)

    # ---- 阶段2: 中期平衡 (300轮) ----
    _run_phase(positions, nodes, adj, grid_size, iterations=300,
               repulsion=4000, attraction=0.01, center=0.12,
               global_center=0.03, damping=0.82)

    # ---- 阶段3: 低温精调 (300轮) ----
    _run_phase(positions, nodes, adj, grid_size, iterations=300,
               repulsion=2500, attraction=0.02, center=0.15,
               global_center=0.04, damping=0.75)

    # 写回坐标
    for i, node in enumerate(nodes):
        node['x'] = round(positions[i][0], 2)
        node['y'] = round(positions[i][1], 2)

    # 最终硬性去重叠
    fix_overlaps(nodes)

    return nodes


def _run_phase(positions, nodes, adj, grid_size, iterations,
               repulsion, attraction, center, global_center, damping):
    """运行单阶段力导向迭代"""
    n = len(nodes)

    for _ in range(iterations):
        # 空间哈希网格
        grid = {}
        for i in range(n):
            gx = int(positions[i][0] / grid_size)
            gy = int(positions[i][1] / grid_size)
            grid.setdefault((gx, gy), []).append(i)

        forces = [[0.0, 0.0] for _ in range(n)]

        for i in range(n):
            # 向心力: 拉向类型中心
            tcx, tcy = TYPE_CENTERS.get(nodes[i]['type'], (CX, CY))
            forces[i][0] += center * (tcx - positions[i][0])
            forces[i][1] += center * (tcy - positions[i][1])

            # 全局中心引力: 防止飘到角落
            forces[i][0] += global_center * (CX - positions[i][0])
            forces[i][1] += global_center * (CY - positions[i][1])

            # 斥力: 仅检查相邻网格, 距离衰减 (平方反比)
            gx = int(positions[i][0] / grid_size)
            gy = int(positions[i][1] / grid_size)
            for dgx in (-1, 0, 1):
                for dgy in (-1, 0, 1):
                    cell = grid.get((gx + dgx, gy + dgy), [])
                    for j in cell:
                        if j <= i:
                            continue
                        dx = positions[i][0] - positions[j][0]
                        dy = positions[i][1] - positions[j][1]
                        dist_sq = dx * dx + dy * dy
                        min_d = MIN_DIST.get(nodes[i]['type'], 40) + MIN_DIST.get(nodes[j]['type'], 40)
                        min_d_sq = min_d * min_d
                        if dist_sq < min_d_sq and dist_sq > 0.01:
                            # 平方反比斥力: 距离越近力越大, 距离 > min_d 时不发力
                            f = repulsion * (min_d_sq - dist_sq) / (dist_sq + min_d_sq)
                            dist = math.sqrt(dist_sq)
                            forces[i][0] += (dx / dist) * f
                            forces[i][1] += (dy / dist) * f
                            forces[j][0] -= (dx / dist) * f
                            forces[j][1] -= (dy / dist) * f
                        elif dist_sq < 0.01:
                            # 完全重合: 随机方向推开
                            angle = random.uniform(0, 2 * math.pi)
                            f = repulsion * 0.5
                            forces[i][0] += math.cos(angle) * f
                            forces[i][1] += math.sin(angle) * f
                            forces[j][0] -= math.cos(angle) * f
                            forces[j][1] -= math.sin(angle) * f

        # 引力: 有关联的节点互相靠近
        for i in range(n):
            for j in adj[i]:
                if j <= i:
                    continue
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                dist = max(math.sqrt(dx * dx + dy * dy), 1.0)
                target = 130.0  # 目标边长度
                f = attraction * (dist - target)
                forces[i][0] += (dx / dist) * f
                forces[i][1] += (dy / dist) * f
                forces[j][0] -= (dx / dist) * f
                forces[j][1] -= (dy / dist) * f

        # 更新位置 + 边界约束
        for i in range(n):
            positions[i][0] += forces[i][0] * damping
            positions[i][1] += forces[i][1] * damping
            md = MIN_DIST.get(nodes[i]['type'], 25) // 2
            positions[i][0] = max(md, min(LAYOUT_WIDTH - md, positions[i][0]))
            positions[i][1] = max(md, min(LAYOUT_HEIGHT - md, positions[i][1]))


def fix_overlaps(nodes: list[dict]):
    """最后一遍硬性去重叠"""
    n = len(nodes)
    moved = True
    max_iter = 200
    it = 0
    while moved and it < max_iter:
        moved = False
        it += 1
        grid = {}
        for i in range(n):
            gx = int(nodes[i]['x'] / 80)
            gy = int(nodes[i]['y'] / 80)
            grid.setdefault((gx, gy), []).append(i)

        for i in range(n):
            gx = int(nodes[i]['x'] / 80)
            gy = int(nodes[i]['y'] / 80)
            for dgx in (-1, 0, 1):
                for dgy in (-1, 0, 1):
                    key = (gx + dgx, gy + dgy)
                    if key in grid:
                        for j in grid[key]:
                            if i >= j:
                                continue
                            dx = nodes[i]['x'] - nodes[j]['x']
                            dy = nodes[i]['y'] - nodes[j]['y']
                            dist = math.sqrt(dx * dx + dy * dy)
                            min_d = MIN_DIST.get(nodes[i]['type'], 40) + MIN_DIST.get(nodes[j]['type'], 40)
                            if dist < min_d * 0.7 and dist > 0.001:
                                overlap = (min_d * 0.7 - dist) / 2
                                nx = (dx / dist) * overlap
                                ny = (dy / dist) * overlap
                                nodes[i]['x'] += nx
                                nodes[i]['y'] += ny
                                nodes[j]['x'] -= nx
                                nodes[j]['y'] -= ny
                                moved = True

    for node in nodes:
        node['x'] = max(10, min(LAYOUT_WIDTH - 10, node['x']))
        node['y'] = max(10, min(LAYOUT_HEIGHT - 10, node['y']))
