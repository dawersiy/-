"""轻量HTML生成器 — 内嵌紧凑数据, 静态布局, 无需HTTP服务器"""

import os, json
from config import OUTPUT_JSON, OUTPUT_HTML

def generate_html(network: dict = None):
    """生成优化的HTML可视化 (内嵌紧凑数据, 无需HTTP)"""

    items = network.get('items', []) if network else []
    relations = network.get('relations_summary', []) if network else []

    # 确保坐标存在
    for item in items:
        if 'x' not in item:
            item['x'] = 400 + (hash(item.get('id','')) % 800)
            item['y'] = 300 + (hash(item.get('id','')+'y') % 600)

    # 构建紧凑数据
    id_to_idx = {}
    compact_nodes = []
    for idx, item in enumerate(items):
        id_to_idx[item['id']] = idx
        compact_nodes.append({
            'id': item['id'],
            't': item['type'],
            'n': item.get('name',''),
            'k': (item.get('keywords',[]) or [])[:5],
            's': len(item.get('sources', [item['id'].split('_')[0]])),
            'x': item.get('x', 400),
            'y': item.get('y', 300)
        })

    compact_links = []
    for rel in relations:
        si = id_to_idx.get(rel.get('source_id',''))
        ti = id_to_idx.get(rel.get('target_id',''))
        if si is not None and ti is not None:
            compact_links.append({
                's': si, 't': ti,
                'tp': rel.get('type',''),
                'nt': (rel.get('note','') or '')[:80]
            })

    # 构建详情数据 (按需查找)
    detail_map = {}
    for idx, item in enumerate(items):
        d = {}
        if item.get('summary'): d['sm'] = item['summary']
        if item.get('latex'): d['lx'] = item['latex'][:600]
        if item.get('statement') and len(item.get('statement','')) > 20:
            d['st'] = item['statement'][:800]
        if item.get('premises'): d['pr'] = item['premises'][:300]
        if item.get('conclusion'): d['cl'] = item['conclusion'][:300]
        if item.get('domain'): d['dm'] = item['domain'][:3]
        if item.get('confidence'): d['cf'] = item['confidence']
        if d:
            detail_map[str(idx)] = d

    data_js = f'const GRAPH={json.dumps({"nd":compact_nodes,"ln":compact_links,"dt":detail_map},ensure_ascii=False)};'

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>数学知识图谱 — 优化理论</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0f1923;color:#e0e0e0;overflow:hidden;height:100vh}}
#container{{display:flex;height:100vh}}
#graph{{flex:1;position:relative;background:radial-gradient(ellipse at center,#1a3040 0%,#0f1923 70%)}}
#graph svg{{width:100%;height:100%}}
#sidebar{{width:360px;background:#1a2a36;border-left:1px solid #2a3a46;padding:16px;overflow-y:auto;display:flex;flex-direction:column;gap:10px;font-size:12px}}
#sidebar h2{{color:#64b5f6;font-size:13px;border-bottom:1px solid #2a3a46;padding-bottom:4px;text-transform:uppercase;letter-spacing:1px;font-weight:500}}
#stats{{display:flex;flex-wrap:wrap;gap:5px}}
.stat-chip{{background:#1e3a4a;border:1px solid #2a4a5a;border-radius:5px;padding:3px 8px;font-size:10px;display:flex;align-items:center;gap:5px}}
.stat-chip .dot{{width:7px;height:7px;border-radius:50%}}
#legend{{display:flex;flex-wrap:wrap;gap:5px}}
.legend-item{{display:flex;align-items:center;gap:5px;font-size:10px;padding:2px 6px;background:#1e3a4a;border-radius:4px}}
.legend-dot{{width:8px;height:8px;border-radius:50%}}
.legend-line{{width:16px;height:2px;border-radius:1px}}
#detail{{flex:1;background:#15232e;border-radius:8px;padding:12px;overflow-y:auto;font-size:11px;border:1px solid #2a3a46;min-height:100px}}
#detail h3{{color:#64b5f6;margin-bottom:4px;font-size:13px}}
#detail .type-badge{{display:inline-block;padding:2px 6px;border-radius:3px;font-size:10px;margin-bottom:4px;color:#fff}}
#detail .latex-block{{background:#0d1a22;border:1px solid #2a3a46;border-radius:5px;padding:10px;margin:6px 0;overflow-x:auto;font-size:12px;color:#ffd54f;font-family:monospace;white-space:pre-wrap}}
#detail .summary-block{{background:#1a2e1a;border:1px solid #2a4a2a;border-radius:5px;padding:8px;margin:6px 0;font-size:11px;color:#a5d6a7;line-height:1.5}}
#search{{width:100%;padding:8px 12px;background:#0d1a22;border:1px solid #2a4a46;border-radius:5px;color:#e0e0e0;font-size:12px;outline:none}}
#search:focus{{border-color:#64b5f6}}
#filter-row{{display:flex;gap:3px;flex-wrap:wrap}}
.fbtn{{padding:3px 8px;border-radius:12px;border:1px solid #2a4a46;background:transparent;color:#90a4ae;font-size:10px;cursor:pointer;transition:all 0.2s}}
.fbtn:hover,.fbtn.active{{background:#1e3a4a;color:#fff;border-color:#64b5f6}}
#rel-list{{font-size:10px;max-height:150px;overflow-y:auto}}
.rel-item{{padding:5px 6px;border-bottom:1px solid #2a3a46;cursor:pointer;border-radius:3px}}
.rel-item:hover{{background:#1e3a4a}}
.tooltip{{position:absolute;background:#1a2a36;border:1px solid #64b5f6;border-radius:6px;padding:8px 12px;pointer-events:none;font-size:11px;max-width:300px;box-shadow:0 6px 18px rgba(0,0,0,0.4);z-index:100;opacity:0}}
.node{{cursor:pointer}}
.node circle{{stroke-width:1.5;stroke-opacity:0.8}}
.node text{{font-size:9px;fill:#b0bec5;pointer-events:none;text-anchor:middle}}
.link{{stroke-opacity:0.3}}
.link:hover{{stroke-opacity:0.9}}
.zoom-ctl{{position:absolute;bottom:16px;right:16px;display:flex;flex-direction:column;gap:3px;z-index:50}}
.zbtn{{width:32px;height:32px;border-radius:5px;background:#1a2a36;border:1px solid #2a4a46;color:#90a4ae;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center}}
.zbtn:hover{{background:#2a3a46;color:#fff}}
</style>
</head>
<body>
<div id="container">
<div id="graph">
    <svg></svg>
    <div class="tooltip" id="tooltip"></div>
    <div class="zoom-ctl">
        <button class="zbtn" id="zin">+</button>
        <button class="zbtn" id="zout">-</button>
        <button class="zbtn" id="zfit">F</button>
    </div>
</div>
<div id="sidebar">
    <h2>📊 知识图谱控制台</h2>
    <input type="text" id="search" placeholder="🔍 搜索定理、公式、关键词...">
    <div id="filter-row">
        <button class="fbtn active" data-type="all">全部</button>
        <button class="fbtn" data-type="theorem">定理</button>
        <button class="fbtn" data-type="lemma">引理</button>
        <button class="fbtn" data-type="corollary">推论</button>
        <button class="fbtn" data-type="definition">定义</button>
        <button class="fbtn" data-type="proposition">命题</button>
        <button class="fbtn" data-type="formula">公式</button>
    </div>
    <div id="stats"></div>
    <h2>🎨 图例</h2>
    <div id="legend"></div>
    <h2>📝 节点详情</h2>
    <div id="detail"><p style="color:#607d8b">点击图中节点查看详细信息</p></div>
    <h2>🔗 关联关系</h2>
    <div id="rel-list"></div>
</div>
</div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
{data_js}
</script>
<script>
// ====== 静态布局知识图谱 ======
const CM={{theorem:'#e74c3c',lemma:'#3498db',corollary:'#2ecc71',definition:'#9b59b6',proposition:'#e67e22',formula:'#1abc9c'}};
const TCN={{theorem:'\\u5b9a\\u7406',lemma:'\\u5f15\\u7406',corollary:'\\u63a8\\u8bba',definition:'\\u5b9a\\u4e49',proposition:'\\u547d\\u9898',formula:'\\u516c\\u5f0f'}};
const RCM={{derives:'#e74c3c',generalizes:'#3498db',equivalent:'#2ecc71',depends:'#95a5a6'}};
const RCN={{derives:'\\u63a8\\u5bfc',generalizes:'\\u63a8\\u5e7f',equivalent:'\\u7b49\\u4ef7',depends:'\\u4f9d\\u8d56'}};
const SZ={{theorem:13,lemma:10,corollary:9,definition:11,proposition:10,formula:7}};

const container=document.getElementById('graph');
const svg=d3.select('#graph svg');
const W=container.clientWidth,H=container.clientHeight;
const g=svg.append('g');

// Zoom
const zoom=d3.zoom().scaleExtent([0.08,5]).on('zoom',e=>{{g.attr('transform',e.transform);onZoom(e);}});
svg.call(zoom);

// ===== 渲染 (静态位置, 无碰撞, 无力模拟) =====
const nodes=GRAPH.nd;
const links=GRAPH.ln;
const detailMap=GRAPH.dt;

// 无节点位置时初始散布
nodes.forEach(n=>{{
    if(n.x===undefined||n.y===undefined){{n.x=400+Math.random()*800;n.y=300+Math.random()*600;}}
}});

// 构建快速查找
const nodeById={{}};
nodes.forEach((n,i)=>{{n._i=i;nodeById[n.id]=n;}});

// 渲染links
const linkG=g.append('g');
const linkSel=linkG.selectAll('line').data(links).join('line')
    .attr('class','link')
    .attr('stroke',d=>RCM[d.tp]||'#666')
    .attr('stroke-width',d=>d.tp==='derives'?2:d.tp==='generalizes'?1.5:1)
    .attr('stroke-dasharray',d=>d.tp==='depends'?'4,3':d.tp==='equivalent'?'5,2':'none')
    .attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
    .attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);

// 渲染nodes
const nodeG=g.append('g');
const nodeSel=nodeG.selectAll('g').data(nodes).join('g')
    .attr('class','node')
    .attr('transform',d=>`translate(${{d.x}},${{d.y}})`)
    .call(d3.drag()
        .on('drag',function(e,d){{
            d.x=e.x;d.y=e.y;
            d3.select(this).attr('transform',`translate(${{d.x}},${{d.y}})`);
            updateLinkPositions();
        }})
    );

nodeSel.append('circle')
    .attr('r',d=>SZ[d.t]+Math.min(d.s*2,6))
    .attr('fill',d=>CM[d.t])
    .attr('stroke',d=>d3.color(CM[d.t]).darker(0.5))
    .on('click',(e,d)=>showDetail(d))
    .on('mouseover',function(e,d){{
        d3.select(this).transition().duration(150).attr('r',SZ[d.t]+Math.min(d.s*2,6)+3);
        const conn=new Set();
        links.forEach(l=>{{if(l.s===d._i)conn.add(l.t);if(l.t===d._i)conn.add(l.s);}});
        nodeSel.selectAll('circle').attr('opacity',n=>n._i===d._i||conn.has(n._i)?1:0.12);
        linkSel.attr('opacity',l=>l.s===d._i||l.t===d._i?1:0.03);
        showTooltip(e,d);
    }})
    .on('mouseout',function(e,d){{
        d3.select(this).transition().duration(150).attr('r',SZ[d.t]+Math.min(d.s*2,6));
        nodeSel.selectAll('circle').attr('opacity',1);
        linkSel.attr('opacity',0.3);
        hideTooltip();
    }});

// 标签 (仅中等缩放时显示)
nodeSel.append('text')
    .text(d=>{{const n=d.n||d.id;return n.length>14?n.slice(0,12)+'..':n;}})
    .attr('y',d=>-SZ[d.t]-6);

// 更新连线位置
function updateLinkPositions(){{
    linkSel.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
        .attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);
}}

// ===== 视口裁剪 + LOD =====
let visTimer;
function onZoom(e){{
    clearTimeout(visTimer);
    visTimer=setTimeout(updateVisibility,80);
}}

function updateVisibility(){{
    const t=d3.zoomTransform(svg.node());
    const s=t.k,vx=-t.x/s,vy=-t.y/s,vw=W/s,vh=H/s,pad=60;
    const lo=s<0.3, mid=s<0.6, hi=s>1.5;

    nodeSel.each(function(d){{
        const vis=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;
        const show=vis&&!(mid&&d.t==='formula');
        d3.select(this).style('display',show?null:'none');
    }});

    // 标签: 缩放<0.3或中距公式时隐藏
    nodeSel.selectAll('text').style('display',function(d){{
        const vis=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;
        return(vis&&!lo&&!(mid&&d.t==='formula'))?null:'none';
    }});

    // 节点大小
    nodeSel.selectAll('circle').attr('r',function(d){{
        if(lo)return 3;
        if(mid&&d.t==='formula')return 4;
        if(hi)return SZ[d.t]+Math.min(d.s*2,8)+2;
        return SZ[d.t]+Math.min(d.s*2,6);
    }});

    // 连线: 极远时隐藏
    linkSel.style('display',function(d){{
        if(lo)return'none';
        const ns=nodes[d.s],nt=nodes[d.t];
        const sv=ns.x>vx-pad&&ns.x<vx+vw+pad&&ns.y>vy-pad&&ns.y<vy+vh+pad;
        const tv=nt.x>vx-pad&&nt.x<vx+vw+pad&&nt.y>vy-pad&&nt.y<vy+vh+pad;
        return(sv||tv)?null:'none';
    }});
}}

// ===== 详情面板 =====
function showDetail(d){{
    const det=document.getElementById('detail');
    const dt=detailMap[String(d._i)]||{{}};
    const badge=CM[d.t];

    let h=`<h3>${{d.n}}</h3>`;
    h+=`<span class="type-badge" style="background:${{badge}}">${{TCN[d.t]}}</span>`;
    h+=`<span style="margin-left:6px;font-size:10px;color:#78909c">${{d.s}} papers</span>`;

    if(dt.sm)h+=`<div class="summary-block">\\ud83d\\udcdd ${{dt.sm}}</div>`;
    if(dt.lx)h+=`<div class="latex-block">${{dt.lx}}</div>`;
    if(dt.st)h+=`<div style="background:#0d1a22;border:1px solid #2a3a46;border-radius:5px;padding:8px;margin:4px 0;font-size:10px;color:#9e9e9e;max-height:150px;overflow-y:auto;line-height:1.5">${{dt.st}}</div>`;
    if(dt.pr)h+=`<div style="margin:4px 0;font-size:10px;color:#90caf9">\\u524d\\u63d0: ${{dt.pr}}</div>`;
    if(dt.cl)h+=`<div style="margin:4px 0;font-size:10px;color:#a5d6a7">\\u7ed3\\u8bba: ${{dt.cl}}</div>`;
    if(d.k&&d.k.length)h+='<div style="margin-top:4px">'+d.k.map(k=>`<span style="display:inline-block;background:#1e3a4a;padding:1px 6px;border-radius:8px;margin:2px;font-size:10px;color:#90caf9">${{k}}</span>`).join('')+'</div>';
    if(dt.dm&&dt.dm.length)h+='<div style="margin-top:2px">'+dt.dm.map(x=>`<span style="display:inline-block;background:#2a1e3a;padding:1px 6px;border-radius:8px;margin:2px;font-size:10px;color:#ce93d8">${{x}}</span>`).join('')+'</div>';
    det.innerHTML=h;

    // 关联列表
    const rl=document.getElementById('rel-list');
    const related=links.filter(l=>l.s===d._i||l.t===d._i);
    if(related.length){{
        rl.innerHTML=related.map(l=>{{
            const oi=l.s===d._i?l.t:l.s;
            const on=nodes[oi];
            return`<div class="rel-item" onclick="flyTo(${{oi}})">
                <span style="color:${{RCM[l.tp]}};font-weight:bold">${{RCN[l.tp]}}</span>
                \\u2192 <span style="color:#64b5f6">${{on?on.n:'?'}}</span>
                <div style="color:#78909c;font-size:9px">${{l.nt||''}}</div></div>`;
        }}).join('');
    }}else rl.innerHTML='<p style="color:#607d8b;font-size:10px">\\u65e0\\u76f4\\u63a5\\u5173\\u8054</p>';
}}

// ===== 交互 =====
function showTooltip(e,d){{
    d3.select('#tooltip')
        .html(`<div style="color:#64b5f6;font-weight:bold">${{d.n}}</div><div style="font-size:10px;color:#90a4ae">${{TCN[d.t]}} | ${{d.s}} papers</div>`)
        .style('left',(e.pageX+14)+'px').style('top',(e.pageY-14)+'px').style('opacity',1);
}}
function hideTooltip(){{d3.select('#tooltip').style('opacity',0);}}

// ===== UI =====
(function buildUI(){{
    const tc={{}};
    nodes.forEach(n=>tc[n.t]=(tc[n.t]||0)+1);
    const sd=document.getElementById('stats');
    Object.entries(tc).forEach(([t,c])=>{{
        sd.innerHTML+=`<div class="stat-chip"><span class="dot" style="background:${{CM[t]}}"></span>${{TCN[t]}}: ${{c}}</div>`;
    }});
    sd.innerHTML+=`<div class="stat-chip">\\ud83d\\udd17 ${{links.length}}</div>`;

    const ld=document.getElementById('legend');
    Object.entries(CM).forEach(([t,c])=>ld.innerHTML+=`<div class="legend-item"><span class="legend-dot" style="background:${{c}}"></span>${{TCN[t]}}</div>`);
    Object.entries(RCM).forEach(([t,c])=>ld.innerHTML+=`<div class="legend-item"><span class="legend-line" style="background:${{c}}"></span>${{RCN[t]}}</div>`);

    // 搜索
    document.getElementById('search').addEventListener('input',function(e){{
        const q=e.target.value.toLowerCase();
        if(!q){{nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.3);return;}}
        const m=new Set();
        nodes.forEach(n=>{{if((n.n+' '+(n.k||[]).join(' ')).toLowerCase().includes(q))m.add(n._i);}});
        nodeSel.selectAll('circle').attr('opacity',n=>m.has(n._i)?1:0.06);
        linkSel.attr('opacity',l=>m.has(l.s)&&m.has(l.t)?1:0.02);
    }});

    // 类型过滤
    let af='all';
    document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',function(){{
        document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));
        this.classList.add('active');
        af=this.dataset.type;
        if(af==='all'){{nodeSel.style('display',null);linkSel.style('display',null);}}
        else{{
            const m=new Set();
            nodes.forEach(n=>{{if(n.t===af)m.add(n._i);}});
            nodeSel.style('display',n=>m.has(n._i)?null:'none');
            linkSel.style('display',l=>m.has(l.s)||m.has(l.t)?null:'none');
        }}
    }}));

    document.getElementById('zin').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,1.3));
    document.getElementById('zout').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,0.7));
    document.getElementById('zfit').addEventListener('click',()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity));

    updateVisibility();
}})();

// 飞向节点
window.flyTo=function(idx){{
    const n=nodes[idx];
    if(!n)return;
    showDetail(n);
    const t=d3.zoomIdentity.translate(W/2,H/2).scale(1.4).translate(-n.x,-n.y);
    svg.transition().duration(500).call(zoom.transform,t);
}};
</script>
</body>
</html>'''

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  HTML: {OUTPUT_HTML} ({os.path.getsize(OUTPUT_HTML)} bytes)")

def save_network_json(network: dict):
    """保存知识网络JSON"""
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(network, f, ensure_ascii=False, indent=2)
    size_kb = os.path.getsize(OUTPUT_JSON) / 1024
    print(f"  JSON: {OUTPUT_JSON} ({size_kb:.1f} KB)")
