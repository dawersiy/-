"""轻量HTML生成器 — 单论文/总览视图切换, 同论文节点弱链接"""

import os, json
from config import OUTPUT_JSON, OUTPUT_HTML

def generate_html(network: dict = None):
    items = network.get('items', []) if network else []
    relations = network.get('relations_summary', []) if network else []
    papers = network.get('papers', []) if network else []

    for item in items:
        if 'x' not in item:
            item['x'] = 400 + (hash(item.get('id','')) % 800)
            item['y'] = 300 + (hash(item.get('id','')+'y') % 600)

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
            'p': item.get('sources', [item['id'].split('_')[0]]),  # 来源论文
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

    # 同论文边 (低权重视觉)
    same_paper_links = []
    paper_groups = {}
    for i, node in enumerate(compact_nodes):
        for pid in node['p']:
            paper_groups.setdefault(pid, []).append(i)
    for pid, indices in paper_groups.items():
        for a in range(len(indices)):
            for b in range(a+1, min(a+4, len(indices))):
                same_paper_links.append({'s': indices[a], 't': indices[b], 'pid': pid})

    detail_map = {}
    for idx, item in enumerate(items):
        d = {}
        if item.get('summary'): d['sm'] = item['summary']
        if item.get('statement') and len(item.get('statement','')) > 20:
            d['st'] = item['statement'][:800]
        if item.get('premises'): d['pr'] = item['premises'][:300]
        if item.get('conclusion'): d['cl'] = item['conclusion'][:300]
        if item.get('domain'): d['dm'] = item['domain'][:3]
        if item.get('confidence'): d['cf'] = item['confidence']
        formulas = item.get('formulas', [])
        if item.get('latex'):
            formulas.insert(0, item['latex'])
        if formulas:
            d['fm'] = [f[:800] for f in list(dict.fromkeys(formulas))[:6]]
        if d:
            detail_map[str(idx)] = d

    data_js = f'''const PAPERS={json.dumps(papers,ensure_ascii=False)};
const SPL={json.dumps(same_paper_links,ensure_ascii=False)};
const GRAPH={json.dumps({"nd":compact_nodes,"ln":compact_links,"dt":detail_map},ensure_ascii=False)};'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>数学知识图谱</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0f1923;color:#e0e0e0;overflow:hidden;height:100vh}}
#container{{display:flex;height:100vh}}
#graph{{flex:1;position:relative;background:radial-gradient(ellipse at center,#1a3040 0%,#0f1923 70%)}}
#graph svg{{width:100%;height:100%}}
#sidebar{{width:340px;background:#1a2a36;border-left:1px solid #2a3a46;padding:14px;overflow-y:auto;display:flex;flex-direction:column;gap:8px;font-size:11px}}
#sidebar h2{{color:#64b5f6;font-size:12px;border-bottom:1px solid #2a3a46;padding-bottom:3px;text-transform:uppercase;letter-spacing:1px;font-weight:500}}
#stats{{display:flex;flex-wrap:wrap;gap:4px}}
.stat-chip{{background:#1e3a4a;border:1px solid #2a4a5a;border-radius:4px;padding:2px 7px;font-size:10px;display:flex;align-items:center;gap:4px}}
.stat-chip .dot{{width:6px;height:6px;border-radius:50%}}
#legend{{display:flex;flex-wrap:wrap;gap:4px}}
.legend-item{{display:flex;align-items:center;gap:4px;font-size:10px;padding:2px 5px;background:#1e3a4a;border-radius:3px}}
.legend-dot{{width:8px;height:8px;border-radius:50%}}
.legend-line{{width:14px;height:2px;border-radius:1px}}
#detail{{flex:1;background:#15232e;border-radius:6px;padding:10px;overflow-y:auto;font-size:10px;border:1px solid #2a3a46;min-height:80px}}
#detail h3{{color:#64b5f6;margin-bottom:3px;font-size:12px}}
#detail .type-badge{{display:inline-block;padding:2px 5px;border-radius:3px;font-size:9px;margin-bottom:3px;color:#fff}}
#detail .summary-block{{background:#1a2e1a;border:1px solid #2a4a2a;border-radius:4px;padding:6px;margin:4px 0;font-size:10px;color:#a5d6a7;line-height:1.4}}
#detail .formula-block{{background:#0d1a22;border:1px solid #2a3a46;border-radius:4px;padding:8px;margin:3px 0;overflow-x:auto;font-size:12px;color:#ffd54f;font-family:monospace;white-space:pre-wrap}}
#search{{width:100%;padding:7px 10px;background:#0d1a22;border:1px solid #2a4a46;border-radius:4px;color:#e0e0e0;font-size:11px;outline:none}}
#search:focus{{border-color:#64b5f6}}
#paper-select{{width:100%;padding:7px 10px;background:#0d1a22;border:1px solid #2a4a46;border-radius:4px;color:#e0e0e0;font-size:11px;outline:none}}
#paper-select:focus{{border-color:#64b5f6}}
#filter-row{{display:flex;gap:2px;flex-wrap:wrap}}
.fbtn{{padding:2px 7px;border-radius:10px;border:1px solid #2a4a46;background:transparent;color:#90a4ae;font-size:9px;cursor:pointer;transition:all 0.2s}}
.fbtn:hover,.fbtn.active{{background:#1e3a4a;color:#fff;border-color:#64b5f6}}
#rel-list{{font-size:10px;max-height:120px;overflow-y:auto}}
.rel-item{{padding:4px 5px;border-bottom:1px solid #2a3a46;cursor:pointer;border-radius:2px}}
.rel-item:hover{{background:#1e3a4a}}
.tooltip{{position:absolute;background:#1a2a36;border:1px solid #64b5f6;border-radius:5px;padding:6px 10px;pointer-events:none;font-size:10px;max-width:280px;box-shadow:0 4px 14px rgba(0,0,0,0.4);z-index:100;opacity:0}}
.node{{cursor:pointer}}
.node circle{{stroke-width:1.5;stroke-opacity:0.8}}
.node text{{font-size:8px;fill:#b0bec5;pointer-events:none;text-anchor:middle}}
.link{{stroke-opacity:0.3}}
.link:hover{{stroke-opacity:0.9}}
.link-sp{{stroke-opacity:0.08;pointer-events:none}}
.zoom-ctl{{position:absolute;bottom:14px;right:14px;display:flex;flex-direction:column;gap:2px;z-index:50}}
.zbtn{{width:28px;height:28px;border-radius:4px;background:#1a2a36;border:1px solid #2a4a46;color:#90a4ae;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center}}
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
    <select id="paper-select"><option value="all">🌐 全部论文总览</option></select>
    <input type="text" id="search" placeholder="🔍 搜索定理、关键词...">
    <div id="filter-row">
        <button class="fbtn active" data-type="all">全部</button>
        <button class="fbtn" data-type="theorem">定理</button>
        <button class="fbtn" data-type="lemma">引理</button>
        <button class="fbtn" data-type="corollary">推论</button>
        <button class="fbtn" data-type="definition">定义</button>
        <button class="fbtn" data-type="proposition">命题</button>
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
// ====== 知识图谱引擎 ======
const CM={{theorem:'#e74c3c',lemma:'#3498db',corollary:'#2ecc71',definition:'#9b59b6',proposition:'#e67e22'}};
const TCN={{theorem:'定理',lemma:'引理',corollary:'推论',definition:'定义',proposition:'命题'}};
const RCM={{derives:'#e74c3c',generalizes:'#3498db',equivalent:'#2ecc71',depends:'#95a5a6'}};
const RCN={{derives:'推导',generalizes:'推广',equivalent:'等价',depends:'依赖'}};
const SZ={{theorem:14,lemma:12,corollary:10,definition:13,proposition:12}};

const container=document.getElementById('graph');
const svg=d3.select('#graph svg');
const W=container.clientWidth,H=container.clientHeight;
const g=svg.append('g');
const zoom=d3.zoom().scaleExtent([0.08,5]).on('zoom',e=>{{g.attr('transform',e.transform);onZoom(e);}});
svg.call(zoom);

const nodes=GRAPH.nd,links=GRAPH.ln,detailMap=GRAPH.dt;
nodes.forEach((n,i)=>{{n._i=i;}});

// 同论文边
const splG=g.append('g');
const splSel=splG.selectAll('line').data(SPL).join('line')
    .attr('class','link-sp').attr('stroke','#445566').attr('stroke-width',0.6)
    .attr('stroke-dasharray','2,6')
    .attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
    .attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);

// 关系边
const linkG=g.append('g');
const linkSel=linkG.selectAll('line').data(links).join('line')
    .attr('class','link').attr('stroke',d=>RCM[d.tp]||'#666')
    .attr('stroke-width',d=>d.tp==='derives'?2:d.tp==='generalizes'?1.5:1)
    .attr('stroke-dasharray',d=>d.tp==='depends'?'4,3':d.tp==='equivalent'?'5,2':'none')
    .attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
    .attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);

// 节点
const nodeG=g.append('g');
const nodeSel=nodeG.selectAll('g').data(nodes).join('g')
    .attr('class','node').attr('transform',d=>`translate(${{d.x}},${{d.y}})`)
    .call(d3.drag().on('drag',function(e,d){{d.x=e.x;d.y=e.y;d3.select(this).attr('transform',`translate(${{d.x}},${{d.y}})`);updateAllLinks();}}));

nodeSel.append('circle').attr('r',d=>SZ[d.t]+Math.min(d.s*2,6))
    .attr('fill',d=>CM[d.t]).attr('stroke',d=>d3.color(CM[d.t]).darker(0.5))
    .on('click',(e,d)=>showDetail(d))
    .on('mouseover',function(e,d){{
        d3.select(this).transition().duration(150).attr('r',SZ[d.t]+Math.min(d.s*2,6)+3);
        const conn=new Set();links.forEach(l=>{{if(l.s===d._i)conn.add(l.t);if(l.t===d._i)conn.add(l.s);}});
        nodeSel.selectAll('circle').attr('opacity',n=>n._i===d._i||conn.has(n._i)?1:0.12);
        linkSel.attr('opacity',l=>l.s===d._i||l.t===d._i?1:0.03);
        showTooltip(e,d);
    }})
    .on('mouseout',function(e,d){{d3.select(this).transition().duration(150).attr('r',SZ[d.t]+Math.min(d.s*2,6));nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.3);hideTooltip();}});

nodeSel.append('text').text(d=>{{const n=d.n||d.id;return n.length>12?n.slice(0,10)+'..':n;}}).attr('y',d=>-SZ[d.t]-6).attr('opacity',0);

function updateAllLinks(){{
    linkSel.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y).attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);
    splSel.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y).attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);
}}

// 当前论文过滤的可见节点集合
let paperVisible=null;  // null=全部可见

// 视口裁剪 + LOD (同时尊重论文过滤)
let vt;
function onZoom(e){{clearTimeout(vt);vt=setTimeout(updateVis,80);}}
function updateVis(){{
    const t=d3.zoomTransform(svg.node()),s=t.k,vx=-t.x/s,vy=-t.y/s,vw=W/s,vh=H/s,pad=40;
    const lo=s<0.35,mid=s<0.75,hi=s>1.8;
    nodeSel.each(function(d){{const inP=!paperVisible||paperVisible.has(d._i);const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;d3.select(this).style('display',(inP&&inV)?null:'none');}});
    nodeSel.selectAll('text').attr('opacity',function(d){{const inP=!paperVisible||paperVisible.has(d._i);const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;return(inP&&inV&&s>1.2)?1:0;}});
    nodeSel.selectAll('circle').attr('r',function(d){{if(lo)return 3;if(mid)return SZ[d.t]*0.7;if(hi)return SZ[d.t]+Math.min(d.s*2,6);return SZ[d.t];}});
    linkSel.style('display',function(d){{if(lo)return'none';const inP=!paperVisible||(paperVisible.has(d.s)&&paperVisible.has(d.t));if(!inP)return'none';const ns=nodes[d.s],nt=nodes[d.t];return(ns.x>vx-pad&&ns.x<vx+vw+pad||nt.x>vx-pad&&nt.x<vx+vw+pad)?null:'none';}});
    splSel.style('display',function(d){{if(paperVisible)return'none';if(s<0.5)return'none';return'none';}});
}}

// ====== 论文选择器 ======
let activePaper='all';
const paperSelect=document.getElementById('paper-select');
PAPERS.forEach(p=>{{const opt=document.createElement('option');opt.value=p.id;opt.textContent=p.year+' '+p.title.slice(0,50);paperSelect.appendChild(opt);}});
paperSelect.addEventListener('change',function(){{
    activePaper=this.value;
    if(activePaper==='all'){{
        paperVisible=null;
    }}else{{
        paperVisible=new Set();
        nodes.forEach(n=>{{if((n.p||[]).includes(activePaper))paperVisible.add(n._i);}});
    }}
    updateVis();
}});

// ====== 详情 ======
function showDetail(d){{
    const det=document.getElementById('detail');
    const dt=detailMap[String(d._i)]||{{}};
    let h=`<h3>${{d.n}}</h3>`;
    h+=`<span class="type-badge" style="background:${{CM[d.t]}}">${{TCN[d.t]}}</span>`;
    h+=`<span style="margin-left:4px;font-size:9px;color:#78909c">${{d.s}} papers`;
    if(d.p&&d.p.length)h+=` · ${{d.p[0]}}</span>`;
    if(dt.sm)h+=`<div class="summary-block">📝 ${{dt.sm}}</div>`;
    if(dt.fm){{dt.fm.forEach(fx=>{{h+=`<div class="formula-block">${{fx}}</div>`;}});}}
    if(dt.st)h+=`<div style="background:#0d1a22;border:1px solid #2a3a46;border-radius:4px;padding:6px;margin:3px 0;font-size:9px;color:#9e9e9e;max-height:120px;overflow-y:auto;line-height:1.4">${{dt.st}}</div>`;
    if(dt.pr)h+=`<div style="margin:3px 0;font-size:9px;color:#90caf9">前提: ${{dt.pr}}</div>`;
    if(dt.cl)h+=`<div style="margin:3px 0;font-size:9px;color:#a5d6a7">结论: ${{dt.cl}}</div>`;
    if(d.k&&d.k.length)h+='<div style="margin-top:3px">'+d.k.map(k=>`<span style="display:inline-block;background:#1e3a4a;padding:1px 5px;border-radius:6px;margin:2px;font-size:9px;color:#90caf9">${{k}}</span>`).join('')+'</div>';
    det.innerHTML=h;
    const rl=document.getElementById('rel-list');
    const related=links.filter(l=>l.s===d._i||l.t===d._i);
    if(related.length){{rl.innerHTML=related.map(l=>{{const oi=l.s===d._i?l.t:l.s;return`<div class="rel-item" onclick="flyTo(${{oi}})"><span style="color:${{RCM[l.tp]}};font-weight:bold">${{RCN[l.tp]}}</span> → <span style="color:#64b5f6">${{nodes[oi]?nodes[oi].n:'?'}}</span></div>`;}}).join('');}}else rl.innerHTML='<p style="color:#607d8b;font-size:9px">无直接关联</p>';
}}

function showTooltip(e,d){{d3.select('#tooltip').html(`<div style="color:#64b5f6;font-weight:bold">${{d.n}}</div><div style="font-size:9px;color:#90a4ae">${{TCN[d.t]}} | ${{(d.p||[]).join(',')}}</div>`).style('left',(e.pageX+12)+'px').style('top',(e.pageY-12)+'px').style('opacity',1);}}
function hideTooltip(){{d3.select('#tooltip').style('opacity',0);}}

// UI
(function initUI(){{
    const tc={{}};nodes.forEach(n=>tc[n.t]=(tc[n.t]||0)+1);
    const sd=document.getElementById('stats');
    Object.entries(tc).forEach(([t,c])=>sd.innerHTML+=`<div class="stat-chip"><span class="dot" style="background:${{CM[t]}}"></span>${{TCN[t]}}: ${{c}}</div>`);
    sd.innerHTML+=`<div class="stat-chip">🔗 ${{links.length}}</div>`;
    const ld=document.getElementById('legend');
    Object.entries(CM).forEach(([t,c])=>ld.innerHTML+=`<div class="legend-item"><span class="legend-dot" style="background:${{c}}"></span>${{TCN[t]}}</div>`);
    Object.entries(RCM).forEach(([t,c])=>ld.innerHTML+=`<div class="legend-item"><span class="legend-line" style="background:${{c}}"></span>${{RCN[t]}}</div>`);
    ld.innerHTML+=`<div class="legend-item"><span class="legend-line" style="background:#445566"></span>同论文</div>`;
    document.getElementById('search').addEventListener('input',function(e){{const q=e.target.value.toLowerCase();if(!q){{nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.3);return;}}const m=new Set();nodes.forEach(n=>{{if((n.n+' '+(n.k||[]).join(' ')).toLowerCase().includes(q))m.add(n._i);}});nodeSel.selectAll('circle').attr('opacity',n=>m.has(n._i)?1:0.06);linkSel.attr('opacity',l=>m.has(l.s)&&m.has(l.t)?1:0.02);}});
    let af='all';
    document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',function(){{document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));this.classList.add('active');af=this.dataset.type;if(af==='all'){{nodeSel.style('display',null);linkSel.style('display',null);}}else{{const m=new Set();nodes.forEach(n=>{{if(n.t===af)m.add(n._i);}});nodeSel.style('display',n=>m.has(n._i)?null:'none');linkSel.style('display',l=>m.has(l.s)||m.has(l.t)?null:'none');}}}}));
    document.getElementById('zin').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,1.3));
    document.getElementById('zout').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,0.7));
    document.getElementById('zfit').addEventListener('click',()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity));
    updateVis();
}})();
window.flyTo=function(idx){{const n=nodes[idx];if(!n)return;showDetail(n);const t=d3.zoomIdentity.translate(W/2,H/2).scale(1.4).translate(-n.x,-n.y);svg.transition().duration(500).call(zoom.transform,t);}};
</script>
</body>
</html>'''

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  HTML: {OUTPUT_HTML} ({os.path.getsize(OUTPUT_HTML)} bytes)")

def save_network_json(network: dict):
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(network, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {OUTPUT_JSON} ({os.path.getsize(OUTPUT_JSON)/1024:.1f} KB)")
