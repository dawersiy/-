"""轻量HTML生成器 — 专业版: 完整图例, 联动隐线, 论文切换"""

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
            'id': item['id'], 't': item['type'], 'n': item.get('name',''),
            'k': (item.get('keywords',[]) or [])[:5],
            's': len(item.get('sources', [item['id'].split('_')[0]])),
            'p': item.get('sources', [item['id'].split('_')[0]]),
            'x': item.get('x', 400), 'y': item.get('y', 300)
        })

    compact_links = []
    for rel in relations:
        si = id_to_idx.get(rel.get('source_id',''))
        ti = id_to_idx.get(rel.get('target_id',''))
        if si is not None and ti is not None:
            compact_links.append({'s': si, 't': ti,
                'tp': rel.get('type',''), 'nt': (rel.get('note','') or '')[:80]})

    # 同论文边
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
        formulas = item.get('formulas', [])
        if item.get('latex'): formulas.insert(0, item['latex'])
        if formulas: d['fm'] = [f[:800] for f in list(dict.fromkeys(formulas))[:6]]
        if d: detail_map[str(idx)] = d

    data_js = f'''const PAPERS={json.dumps(papers,ensure_ascii=False,separators=(',',':'))};
const SPL={json.dumps(same_paper_links,ensure_ascii=False,separators=(',',':'))};
const GRAPH={json.dumps({"nd":compact_nodes,"ln":compact_links,"dt":detail_map},ensure_ascii=False,separators=(',',':'))};'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Math Knowledge Graph — Optimization Theory</title>
<style>
:root{{--bg:#0d1520;--panel:#131e2a;--border:#1e3040;--text:#b0c0d0;--acc:#5b9bd5;--gold:#e2b04a;--dim:#506070}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);overflow:hidden;height:100vh;font-size:12px}}
#container{{display:flex;height:100vh}}
#graph{{flex:1;position:relative;background:radial-gradient(ellipse at center,#162435 0%,var(--bg) 70%);contain:layout style}}
#graph svg{{width:100%;height:100%;contain:layout style}}
#sidebar{{width:340px;background:var(--panel);border-left:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}}
#sb-head{{padding:14px 16px 10px;border-bottom:1px solid var(--border)}}
#sb-head h1{{font-size:14px;font-weight:600;color:#e0e8f0;letter-spacing:0.3px}}
#sb-head .sub{{font-size:10px;color:var(--dim);margin-top:2px}}
#sb-body{{flex:1;overflow-y:auto;padding:10px 16px;display:flex;flex-direction:column;gap:10px}}
.sb-sec{{}}
.sb-sec h2{{font-size:10px;font-weight:600;color:var(--acc);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}}
select,input[type=text]{{width:100%;padding:7px 10px;background:#0a121c;border:1px solid var(--border);border-radius:4px;color:var(--text);font-size:11px;outline:none}}
select:focus,input:focus{{border-color:var(--acc)}}
#filter-row{{display:flex;gap:3px;flex-wrap:wrap}}
.fbtn{{padding:3px 9px;border-radius:10px;border:1px solid var(--border);background:transparent;color:#708090;font-size:9px;cursor:pointer;transition:all 0.15s}}
.fbtn:hover,.fbtn.active{{background:#1a2e40;color:#d0d8e0;border-color:var(--acc)}}
#stats{{display:flex;flex-wrap:wrap;gap:4px}}
.chip{{background:#111d2a;border:1px solid var(--border);border-radius:4px;padding:3px 8px;font-size:10px;display:flex;align-items:center;gap:5px}}
.chip .dot{{width:7px;height:7px;border-radius:50%;flex-shrink:0}}
#legend{{display:flex;flex-direction:column;gap:3px}}
.lgd-item{{display:flex;align-items:center;gap:8px;font-size:10px;padding:2px 0;color:#8090a0}}
.lgd-node{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
.lgd-line{{width:22px;height:0;flex-shrink:0;border-radius:1px}}
.lgd-line.solid{{border-top:2px solid}}
.lgd-line.dashed{{border-top:1.5px dashed}}
.lgd-line.dotted{{border-top:1px dotted}}
#detail{{flex:1;min-height:80px;background:#0e1822;border:1px solid var(--border);border-radius:6px;padding:10px;overflow-y:auto;font-size:10px;line-height:1.5}}
#detail h3{{color:#d0d8e0;font-size:12px;margin-bottom:4px;font-weight:600}}
#detail .badge{{display:inline-block;padding:1px 6px;border-radius:3px;font-size:9px;color:#fff;font-weight:500}}
#detail .summary{{background:#122016;border:1px solid #1e3a20;border-radius:4px;padding:7px 9px;margin:5px 0;font-size:10px;color:#8cb88c;line-height:1.5}}
#detail .latex{{background:#0a121c;border:1px solid var(--border);border-radius:4px;padding:9px;margin:3px 0;overflow-x:auto;font-size:12px;color:var(--gold);font-family:'Cascadia Code','Fira Code',Consolas,monospace;white-space:pre-wrap}}
#detail .meta{{margin:3px 0;font-size:9px;color:var(--dim)}}
#detail .kw{{display:inline-block;background:#111d2a;padding:1px 6px;border-radius:8px;margin:2px;font-size:9px;color:#7ba4cc}}
#rel-list{{font-size:10px;max-height:120px;overflow-y:auto}}
.rel-item{{padding:4px 6px;border-bottom:1px solid var(--border);cursor:pointer}}
.rel-item:hover{{background:#111d2a}}
.rel-item .rtype{{font-weight:600}}
.tooltip{{position:absolute;background:var(--panel);border:1px solid var(--acc);border-radius:5px;padding:7px 10px;pointer-events:none;font-size:10px;max-width:280px;box-shadow:0 6px 20px rgba(0,0,0,0.5);z-index:100;opacity:0}}
.node{{cursor:pointer}}
.node circle{{stroke-width:1.5;stroke-opacity:0.7}}
.node text{{font-size:8px;fill:#8090a0;pointer-events:none;text-anchor:middle;font-weight:500}}
.link{{stroke-opacity:0.28;transition:stroke-opacity 0.1s;pointer-events:none}}
.link:hover{{stroke-opacity:0.85}}
.link-sp{{pointer-events:none;will-change:opacity}}
.zoom-ctl{{position:absolute;bottom:14px;right:14px;display:flex;flex-direction:column;gap:3px;z-index:50}}
.zbtn{{width:30px;height:30px;border-radius:5px;background:var(--panel);border:1px solid var(--border);color:var(--dim);font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.15s}}
.zbtn:hover{{background:#1a2e40;color:#d0d8e0;border-color:var(--acc)}}
</style>
</head>
<body>
<div id="container">
<div id="graph">
<svg></svg>
<div class="tooltip" id="tooltip"></div>
<div class="zoom-ctl">
<button class="zbtn" id="zin">+</button><button class="zbtn" id="zout">−</button><button class="zbtn" id="zfit">⊡</button>
</div>
</div>
<div id="sidebar">
<div id="sb-head"><h1>Mathematical Knowledge Graph</h1><div class="sub">Optimization Theory · 26 Papers · {len(items)} Items</div></div>
<div id="sb-body">
<div class="sb-sec">
<h2>Paper View</h2>
<select id="paper-select"><option value="all">All Papers</option></select>
</div>
<div class="sb-sec">
<h2>Search</h2>
<input type="text" id="search" placeholder="Theorem name, keyword...">
</div>
<div class="sb-sec">
<h2>Type Filter</h2>
<div id="filter-row">
<button class="fbtn active" data-type="all">All</button>
<button class="fbtn" data-type="theorem">Theorem</button>
<button class="fbtn" data-type="lemma">Lemma</button>
<button class="fbtn" data-type="corollary">Corollary</button>
<button class="fbtn" data-type="definition">Definition</button>
<button class="fbtn" data-type="proposition">Proposition</button>
</div>
</div>
<div class="sb-sec"><h2>Statistics</h2><div id="stats"></div></div>
<div class="sb-sec"><h2>Legend</h2><div id="legend"></div></div>
<div class="sb-sec" style="flex:1;display:flex;flex-direction:column;min-height:0">
<h2>Detail</h2>
<div id="detail"><p style="color:var(--dim)">Click a node to inspect</p></div>
</div>
<div class="sb-sec">
<h2>Related</h2>
<div id="rel-list"></div>
</div>
</div>
</div>
</div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>{data_js}</script>
<script>
// ===== Color Scheme =====
const CM={{theorem:'#ff5252',lemma:'#448aff',corollary:'#69f0ae',definition:'#e040fb',proposition:'#ffab40'}};
const TCN={{theorem:'Theorem',lemma:'Lemma',corollary:'Corollary',definition:'Definition',proposition:'Proposition'}};
const RCM={{derives:'#ff5252',generalizes:'#448aff',equivalent:'#69f0ae',depends:'#ffab40',same_paper:'#b388ff'}};
const RCN={{derives:'Derives',generalizes:'Generalizes',equivalent:'Equivalent',depends:'Depends',same_paper:'Same Paper'}};
const SZ={{theorem:14,lemma:12,corollary:10,definition:13,proposition:12}};

// ===== Init =====
const container=document.getElementById('graph');
const svg=d3.select('#graph svg');
const W=container.clientWidth,H=container.clientHeight;
const g=svg.append('g').attr('style','will-change:transform');
const zoom=d3.zoom().scaleExtent([0.08,5.5]).on('zoom',e=>{{g.attr('transform',e.transform);onZoom(e);}});
svg.call(zoom);

const nodes=GRAPH.nd,links=GRAPH.ln,detailMap=GRAPH.dt;
nodes.forEach((n,i)=>n._i=i);

// Layer 0: same-paper edges (bottom)
const splG=g.append('g');
const splSel=splG.selectAll('line').data(SPL).join('line')
.attr('class','link-sp').attr('stroke',RCM.same_paper).attr('stroke-width',0.5)
.attr('stroke-dasharray','2,8').attr('stroke-opacity',0.15)
.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
.attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);

// Layer 1: relation edges
const linkG=g.append('g');
const linkSel=linkG.selectAll('line').data(links).join('line')
.attr('class','link')
.attr('stroke',d=>RCM[d.tp]||'#7a8a9a')
.attr('stroke-width',d=>d.tp==='derives'?2:d.tp==='generalizes'?1.5:d.tp==='equivalent'?1.5:d.tp==='depends'?1:0.5)
.attr('stroke-dasharray',d=>d.tp==='depends'?'3,4':d.tp==='equivalent'?'8,4':d.tp==='generalizes'?'6,3':'none')
.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y)
.attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);

// Layer 2: nodes
const nodeG=g.append('g');
const nodeSel=nodeG.selectAll('g').data(nodes).join('g')
.attr('class','node').attr('transform',d=>`translate(${{d.x}},${{d.y}})`)
.call(d3.drag().on('drag',function(e,d){{d.x=e.x;d.y=e.y;d3.select(this).attr('transform',`translate(${{d.x}},${{d.y}})`);updateAllLinks();}}));

nodeSel.append('circle').attr('r',d=>SZ[d.t]+Math.min(d.s*2,6))
.attr('fill',d=>CM[d.t])
.attr('stroke',d=>d3.color(CM[d.t]).darker(0.6))
.on('click',(e,d)=>showDetail(d))
.on('mouseover',function(e,d){{
    const r=SZ[d.t]+Math.min(d.s*2,6);d3.select(this).transition().duration(80).attr('r',r+3);
    const conn=new Set();links.forEach(l=>{{if(l.s===d._i)conn.add(l.t);if(l.t===d._i)conn.add(l.s);}});
    nodeSel.selectAll('circle').attr('opacity',n=>n._i===d._i||conn.has(n._i)?1:0.12);
    linkSel.attr('opacity',l=>l.s===d._i||l.t===d._i?0.85:0.02);
    showTooltip(e,d);
}})
.on('mouseout',function(e,d){{
    d3.select(this).transition().duration(80).attr('r',SZ[d.t]+Math.min(d.s*2,6));
    nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.28);splSel.attr('opacity',0.12);
    hideTooltip();
}});

nodeSel.append('text').text(d=>{{const n=d.n||d.id;return n.length>12?n.slice(0,10)+'..':n;}})
.attr('y',d=>-SZ[d.t]-6).attr('opacity',0);

function updateAllLinks(){{
    linkSel.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y).attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);
    splSel.attr('x1',d=>nodes[d.s].x).attr('y1',d=>nodes[d.s].y).attr('x2',d=>nodes[d.t].x).attr('y2',d=>nodes[d.t].y);
}}

// ===== Visibility State =====
let paperVisible=null, typeFilter='all', searchQuery='';

function isNodeVisible(i){{
    const n=nodes[i];
    if(paperVisible && !paperVisible.has(i)) return false;
    if(typeFilter!=='all' && n.t!==typeFilter) return false;
    if(searchQuery && !(n.n+' '+(n.k||[]).join(' ')).toLowerCase().includes(searchQuery)) return false;
    return true;
}}

function applyAllFilters(){{
    const vis=new Set();
    for(let i=0;i<nodes.length;i++) if(isNodeVisible(i)) vis.add(i);
    nodeSel.style('display',n=>vis.has(n._i)?null:'none');
    linkSel.style('display',l=>vis.has(l.s)&&vis.has(l.t)?null:'none');
    splSel.style('display',l=>paperVisible?vis.has(l.s)&&vis.has(l.t)?null:'none':'none');
    updateVis();
}}

// ===== Viewport Culling + LOD =====
let vt;
function onZoom(e){{clearTimeout(vt);vt=setTimeout(updateVis,40);}}
function updateVis(){{
    const t=d3.zoomTransform(svg.node()),s=t.k,vx=-t.x/s,vy=-t.y/s,vw=W/s,vh=H/s,pad=50;
    const lo=s<0.35,mid=s<0.75,hi=s>1.8;
    // 极远: 跳过详细渲染
    if(lo){{nodeSel.each(function(d){{d3.select(this).style('display',isNodeVisible(d._i)?null:'none');}});nodeSel.selectAll('text').attr('opacity',0);nodeSel.selectAll('circle').attr('r',3);linkSel.style('display','none');splSel.style('display','none');return;}}
    nodeSel.each(function(d){{
        const inP=isNodeVisible(d._i);
        const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;
        d3.select(this).style('display',(inP&&inV)?null:'none');
    }});
    nodeSel.selectAll('text').attr('opacity',function(d){{const inP=isNodeVisible(d._i);const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;return(inP&&inV&&s>1.2)?1:0;}});
    nodeSel.selectAll('circle').attr('r',function(d){{if(lo)return 3;if(mid)return SZ[d.t]*0.7;if(hi)return SZ[d.t]+Math.min(d.s*2,6);return SZ[d.t];}});
    linkSel.style('display',function(d){{
        if(lo)return'none';if(!isNodeVisible(d.s)||!isNodeVisible(d.t))return'none';
        const ns=nodes[d.s],nt=nodes[d.t];return(ns.x>vx-pad&&ns.x<vx+vw+pad||nt.x>vx-pad&&nt.x<vx+vw+pad)?null:'none';
    }});
    splSel.style('display',function(d){{if(paperVisible||s<0.5)return'none';return isNodeVisible(d.s)&&isNodeVisible(d.t)?null:'none';}});
}}

// ===== Paper Selector =====
let activePaper='all';
const ps=document.getElementById('paper-select');
PAPERS.forEach(p=>{{const o=document.createElement('option');o.value=p.id;o.textContent=`[${{p.year}}] ${{p.title.slice(0,48)}}`;ps.appendChild(o);}});
ps.addEventListener('change',function(){{
    activePaper=this.value;
    paperVisible=(activePaper==='all')?null:new Set(nodes.filter(n=>(n.p||[]).includes(activePaper)).map(n=>n._i));
    applyAllFilters();
}});

// ===== Type Filter =====
document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',function(){{
    document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));
    this.classList.add('active');typeFilter=this.dataset.type;applyAllFilters();
}}));

// ===== Search =====
document.getElementById('search').addEventListener('input',function(e){{
    searchQuery=e.target.value.toLowerCase();applyAllFilters();
}});

// ===== Detail Panel =====
function showDetail(d){{
    const dt=detailMap[String(d._i)]||{{}},det=document.getElementById('detail');
    let h=`<h3>${{d.n}}</h3><span class="badge" style="background:${{CM[d.t]}}">${{TCN[d.t]}}</span>`;
    h+=`<span style="margin-left:5px;font-size:9px;color:var(--dim)">${{d.s}} paper(s)`;
    if(d.p&&d.p.length)h+=` · ${{d.p[0]}}`;h+='</span>';
    if(dt.sm)h+=`<div class="summary">${{dt.sm}}</div>`;
    if(dt.fm)dt.fm.forEach(fx=>h+=`<div class="latex">${{fx}}</div>`);
    if(dt.st)h+=`<div style="background:#0a121c;border:1px solid var(--border);border-radius:4px;padding:7px;margin:3px 0;font-size:9px;color:#708090;max-height:120px;overflow-y:auto;line-height:1.5">${{dt.st}}</div>`;
    if(dt.pr)h+=`<div class="meta" style="color:#7ba4cc">Premise: ${{dt.pr}}</div>`;
    if(dt.cl)h+=`<div class="meta" style="color:#8cb88c">Conclusion: ${{dt.cl}}</div>`;
    if(d.k&&d.k.length)h+='<div style="margin-top:3px">'+d.k.map(k=>`<span class="kw">${{k}}</span>`).join('')+'</div>';
    det.innerHTML=h;
    const rl=document.getElementById('rel-list');
    const related=links.filter(l=>l.s===d._i||l.t===d._i);
    if(related.length){{
        rl.innerHTML=related.map(l=>{{const oi=l.s===d._i?l.t:l.s,on=nodes[oi];return`<div class="rel-item" onclick="flyTo(${{oi}})">
        <span class="rtype" style="color:${{RCM[l.tp]}}">${{RCN[l.tp]}}</span> → ${{on?on.n:'?'}}</div>`;}}).join('');
    }}else rl.innerHTML='<p style="color:var(--dim);font-size:9px">No direct relations</p>';
}}

function showTooltip(e,d){{d3.select('#tooltip').html(`<div style="color:#d0d8e0;font-weight:600">${{d.n}}</div><div style="font-size:9px;color:var(--dim)">${{TCN[d.t]}} · ${{(d.p||[]).join(',')}}</div>`).style('left',(e.pageX+12)+'px').style('top',(e.pageY-12)+'px').style('opacity',1);}}
function hideTooltip(){{d3.select('#tooltip').style('opacity',0);}}

// ===== Init UI =====
(function(){{
    // Stats
    const tc={{}};nodes.forEach(n=>tc[n.t]=(tc[n.t]||0)+1);
    const sd=document.getElementById('stats');
    Object.entries(tc).forEach(([t,c])=>sd.innerHTML+=`<div class="chip"><span class="dot" style="background:${{CM[t]}}"></span>${{TCN[t]}} ${{c}}</div>`);
    sd.innerHTML+=`<div class="chip">Edges ${{links.length}}</div><div class="chip">Same-paper ${{SPL.length}}</div>`;

    // Legend
    const ld=document.getElementById('legend');
    Object.entries(CM).forEach(([t,c])=>ld.innerHTML+=`<div class="lgd-item"><span class="lgd-node" style="background:${{c}}"></span>${{TCN[t]}}</div>`);
    ld.innerHTML+=`<div class="lgd-item"><span class="lgd-line solid" style="border-color:${{RCM.derives}};border-width:2px"></span>Derives</div>`;
    ld.innerHTML+=`<div class="lgd-item"><span class="lgd-line solid" style="border-color:${{RCM.generalizes}};border-top-style:dashed;border-top-width:1.5px"></span>Generalizes</div>`;
    ld.innerHTML+=`<div class="lgd-item"><span class="lgd-line solid" style="border-color:${{RCM.equivalent}};border-top-style:dashed;border-top-width:1.5px"></span>Equivalent</div>`;
    ld.innerHTML+=`<div class="lgd-item"><span class="lgd-line solid" style="border-color:${{RCM.depends}};border-top-style:dotted;border-top-width:1.5px"></span>Depends</div>`;
    ld.innerHTML+=`<div class="lgd-item"><span class="lgd-line solid" style="border-color:${{RCM.same_paper}};border-top-width:0.5px"></span>Same Paper</div>`;

    // Zoom
    document.getElementById('zin').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,1.3));
    document.getElementById('zout').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,0.7));
    document.getElementById('zfit').addEventListener('click',()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity));
    updateVis();
}})();

window.flyTo=function(idx){{const n=nodes[idx];if(!n)return;showDetail(n);svg.transition().duration(500).call(zoom.transform,d3.zoomIdentity.translate(W/2,H/2).scale(1.4).translate(-n.x,-n.y));}};
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
