"""服务端预计算力导向布局 — 使用简单弹簧-电荷模型"""

import math, random
from config import LAYOUT_WIDTH, LAYOUT_HEIGHT

# 类型中心 (与HTML中一致)
TYPE_CENTERS = {
    'theorem': (LAYOUT_WIDTH * 0.30, LAYOUT_HEIGHT * 0.30),
    'lemma': (LAYOUT_WIDTH * 0.15, LAYOUT_HEIGHT * 0.55),
    'corollary': (LAYOUT_WIDTH * 0.45, LAYOUT_HEIGHT * 0.20),
    'definition': (LAYOUT_WIDTH * 0.10, LAYOUT_HEIGHT * 0.30),
    'proposition': (LAYOUT_WIDTH * 0.45, LAYOUT_HEIGHT * 0.60),
    'formula': (LAYOUT_WIDTH * 0.70, LAYOUT_HEIGHT * 0.45),
}

def compute_layout(nodes: list[dict], links: list[dict], iterations: int = 300) -> list[dict]:
    """预计算力导向布局的x,y坐标"""
    n = len(nodes)
    if n == 0:
        return nodes

    # 初始化位置
    positions = []
    for node in nodes:
        cx, cy = TYPE_CENTERS.get(node['type'], (LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2))
        positions.append([cx + random.uniform(-50, 50), cy + random.uniform(-50, 50)])

    # 构建邻接表
    adj = [[] for _ in range(n)]
    for link in links:
        si = link.get('source_index', -1)
        ti = link.get('target_index', -1)
        if 0 <= si < n and 0 <= ti < n:
            adj[si].append(ti)
            adj[ti].append(si)

    # 力参数
    repulsion_strength = 5000.0
    attraction_strength = 0.01
    center_strength = 0.02
    damping = 0.85

    for iteration in range(iterations):
        forces = [[0.0, 0.0] for _ in range(n)]

        # 斥力 (仅对相近节点, O(n) bucket近似)
        for i in range(n):
            cx, cy = TYPE_CENTERS.get(nodes[i]['type'], (LAYOUT_WIDTH / 2, LAYOUT_HEIGHT / 2))
            forces[i][0] += center_strength * (cx - positions[i][0])
            forces[i][1] += center_strength * (cy - positions[i][1])

        # 采样斥力 (随机采样减少计算)
        sample_size = min(100, n)
        for i in range(n):
            for _ in range(sample_size):
                j = random.randrange(n)
                if i == j:
                    continue
                dx = positions[i][0] - positions[j][0]
                dy = positions[i][1] - positions[j][1]
                dist = max(math.sqrt(dx * dx + dy * dy), 1.0)
                force = repulsion_strength / (dist * dist)
                forces[i][0] += (dx / dist) * force
                forces[i][1] += (dy / dist) * force

        # 引力 (仅对相邻节点)
        for i in range(n):
            for j in adj[i]:
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                dist = max(math.sqrt(dx * dx + dy * dy), 1.0)
                target_dist = 90.0
                force = attraction_strength * (dist - target_dist)
                forces[i][0] += (dx / dist) * force
                forces[i][1] += (dy / dist) * force

        # 更新位置
        for i in range(n):
            positions[i][0] += forces[i][0] * damping
            positions[i][1] += forces[i][1] * damping
            positions[i][0] = max(0, min(LAYOUT_WIDTH, positions[i][0]))
            positions[i][1] = max(0, min(LAYOUT_HEIGHT, positions[i][1]))

        # 逐步降温
        damping *= 0.995

    # 写回nodes
    for i, node in enumerate(nodes):
        node['x'] = round(positions[i][0], 2)
        node['y'] = round(positions[i][1], 2)

    return nodes

def prepare_visualization_data(items: list[dict], relations: list[dict]) -> tuple[list[dict], list[dict]]:
    """准备可视化数据: 分离紧凑节点和详情"""
    # 构建id到index的映射
    id_to_idx = {}
    for idx, item in enumerate(items):
        iid = item.get('id', '')
        if iid:
            id_to_idx[iid] = idx

    # 紧凑节点: 仅渲染所需字段
    compact_nodes = []
    for item in items:
        compact_nodes.append({
            'id': item.get('id', ''),
            'type': item.get('type', ''),
            'name': item.get('name', ''),
            'keywords': item.get('keywords', [])[:5],
            'sources': len(item.get('sources', [item.get('source_paper', '')])),
            'domain': item.get('domain', [])[:3],
            'x': item.get('x', 0),
            'y': item.get('y', 0)
        })

    # 链接: 含index
    compact_links = []
    for rel in relations:
        sid = rel.get('source_id', '')
        tid = rel.get('target_id', '')
        if sid in id_to_idx and tid in id_to_idx:
            compact_links.append({
                'source': id_to_idx[sid],
                'target': id_to_idx[tid],
                'type': rel.get('type', ''),
                'note': rel.get('note', '')[:100]
            })

    # 为layout添加index
    for idx, item in enumerate(items):
        item['_idx'] = idx

    return compact_nodes, compact_links
