"""服务端预计算力导向布局 — 网格加速斥力, 高迭代确保节点不重叠"""

import math, random
from config import LAYOUT_WIDTH, LAYOUT_HEIGHT

TYPE_CENTERS = {
    'theorem': (LAYOUT_WIDTH * 0.30, LAYOUT_HEIGHT * 0.30),
    'lemma': (LAYOUT_WIDTH * 0.15, LAYOUT_HEIGHT * 0.55),
    'corollary': (LAYOUT_WIDTH * 0.45, LAYOUT_HEIGHT * 0.20),
    'definition': (LAYOUT_WIDTH * 0.10, LAYOUT_HEIGHT * 0.30),
    'proposition': (LAYOUT_WIDTH * 0.45, LAYOUT_HEIGHT * 0.60),
    'formula': (LAYOUT_WIDTH * 0.70, LAYOUT_HEIGHT * 0.45),
}

# 节点最小间距 (不同类型的node有不同的最小间距)
MIN_DIST = {
    'theorem': 45, 'lemma': 35, 'corollary': 30,
    'definition': 40, 'proposition': 35, 'formula': 22
}

def compute_layout(nodes: list[dict], links: list[dict], iterations: int = 600) -> list[dict]:
    """预计算力导向布局 — 网格加速, 确保节点不重叠"""
    n = len(nodes)
    if n == 0:
        return nodes

    # 初始化: 类型中心 + 小随机偏移
    positions = []
    for node in nodes:
        cx, cy = TYPE_CENTERS.get(node['type'], (LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2))
        positions.append([cx + random.uniform(-60, 60), cy + random.uniform(-60, 60)])

    # 邻接表
    adj = [[] for _ in range(n)]
    for link in links:
        si = link.get('source_index', 0)
        ti = link.get('target_index', 0)
        if 0 <= si < n and 0 <= ti < n and si != ti:
            adj[si].append(ti)
            adj[ti].append(si)

    # 力参数
    repulsion = 8000.0
    attraction = 0.008
    center = 0.025
    damping = 0.9
    grid_size = 80  # 空间哈希网格大小

    for it in range(iterations):
        # 构建空间哈希网格 (每轮重建)
        grid = {}
        for i in range(n):
            gx = int(positions[i][0] / grid_size)
            gy = int(positions[i][1] / grid_size)
            key = (gx, gy)
            if key not in grid:
                grid[key] = []
            grid[key].append(i)

        forces = [[0.0, 0.0] for _ in range(n)]

        for i in range(n):
            # 向心力: 拉向类型中心
            cx, cy = TYPE_CENTERS.get(nodes[i]['type'], (LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2))
            forces[i][0] += center * (cx - positions[i][0])
            forces[i][1] += center * (cy - positions[i][1])

            # 斥力: 只检查相邻网格
            gx = int(positions[i][0] / grid_size)
            gy = int(positions[i][1] / grid_size)
            checked = set()
            for dgx in (-1, 0, 1):
                for dgy in (-1, 0, 1):
                    key = (gx + dgx, gy + dgy)
                    if key in grid:
                        for j in grid[key]:
                            if i == j or j in checked:
                                continue
                            checked.add(j)
                            dx = positions[i][0] - positions[j][0]
                            dy = positions[i][1] - positions[j][1]
                            dist_sq = dx * dx + dy * dy
                            min_d = MIN_DIST.get(nodes[i]['type'], 25) + MIN_DIST.get(nodes[j]['type'], 25)
                            if dist_sq < 1.0:
                                dist_sq = 1.0
                                dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)
                            dist = math.sqrt(dist_sq)
                            if dist < min_d:
                                # 强斥力防止重叠
                                f = repulsion * (min_d - dist) / dist
                                forces[i][0] += (dx / dist) * f
                                forces[i][1] += (dy / dist) * f

        # 引力: 相邻节点
        for i in range(n):
            for j in adj[i]:
                if j <= i:  # 每条边处理一次
                    continue
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                dist = max(math.sqrt(dx * dx + dy * dy), 1.0)
                target = 100.0
                f = attraction * (dist - target)
                fx = (dx / dist) * f
                fy = (dy / dist) * f
                forces[i][0] += fx
                forces[i][1] += fy
                forces[j][0] -= fx
                forces[j][1] -= fy

        # 更新位置 + 边界约束
        for i in range(n):
            positions[i][0] += forces[i][0] * damping
            positions[i][1] += forces[i][1] * damping
            md = MIN_DIST.get(nodes[i]['type'], 25)
            positions[i][0] = max(md, min(LAYOUT_WIDTH - md, positions[i][0]))
            positions[i][1] = max(md, min(LAYOUT_HEIGHT - md, positions[i][1]))

        # 降温
        damping *= 0.996

    # 写回
    for i, node in enumerate(nodes):
        node['x'] = round(positions[i][0], 2)
        node['y'] = round(positions[i][1], 2)

    # 最终去重检查: 对仍然重叠的节点做硬性推开
    fix_overlaps(nodes)

    return nodes

def fix_overlaps(nodes: list[dict]):
    """最后一遍硬性去重叠: 移动仍然重叠的节点"""
    n = len(nodes)
    moved = True
    max_iter = 200
    it = 0
    while moved and it < max_iter:
        moved = False
        it += 1
        # 简单网格
        grid = {}
        for i in range(n):
            gx = int(nodes[i]['x'] / 80)
            gy = int(nodes[i]['y'] / 80)
            key = (gx, gy)
            grid.setdefault(key, []).append(i)

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
                            min_d = MIN_DIST.get(nodes[i]['type'], 25) + MIN_DIST.get(nodes[j]['type'], 25)
                            if dist < min_d * 0.7 and dist > 0.001:
                                overlap = (min_d * 0.7 - dist) / 2
                                nx = (dx / dist) * overlap
                                ny = (dy / dist) * overlap
                                nodes[i]['x'] += nx
                                nodes[i]['y'] += ny
                                nodes[j]['x'] -= nx
                                nodes[j]['y'] -= ny
                                moved = True

    # 边界约束
    for node in nodes:
        node['x'] = max(10, min(LAYOUT_WIDTH - 10, node['x']))
        node['y'] = max(10, min(LAYOUT_HEIGHT - 10, node['y']))
