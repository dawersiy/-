/**
 * 数学知识图谱 — 轻量D3.js可视化引擎
 * 功能: 外部数据加载、视口裁剪、LOD缩放、预计算布局、延迟详情加载
 */

// 颜色映射
const CM = {theorem:'#e74c3c',lemma:'#3498db',corollary:'#2ecc71',definition:'#9b59b6',proposition:'#e67e22',formula:'#1abc9c'};
const TCN = {theorem:'定理',lemma:'引理',corollary:'推论',definition:'定义',proposition:'命题',formula:'公式'};
const RCM = {derives:'#e74c3c',generalizes:'#3498db',equivalent:'#2ecc71',depends:'#95a5a6'};
const RCN = {derives:'推导',generalizes:'推广',equivalent:'等价',depends:'依赖'};
const SIZES = {theorem:13,lemma:10,corollary:9,definition:11,proposition:10,formula:7};

let data, svg, g, zoom, nodeG, linkG;
let nodeSel, linkSel;
let detailCache = {}; // 按需加载的详情缓存
let W, H;

// ========= 初始化 =========
async function init() {
    const container = document.getElementById('graph');
    W = container.clientWidth;
    H = container.clientHeight;

    svg = d3.select('#graph svg');
    g = svg.append('g');

    // 缩放
    zoom = d3.zoom().scaleExtent([0.08, 6]).on('zoom', onZoom);
    svg.call(zoom);

    // 加载数据
    document.getElementById('loading').style.display = 'block';
    try {
        const resp = await fetch('knowledge_network.json');
        const json = await resp.json();
        data = buildGraphData(json);
    } catch(e) {
        // 如果fetch失败，尝试内联数据
        if (typeof INLINE_DATA !== 'undefined') {
            data = buildGraphData(INLINE_DATA);
        } else {
            document.getElementById('loading').textContent = '加载失败: 需要HTTP服务器运行';
            return;
        }
    }
    document.getElementById('loading').style.display = 'none';

    if (!data.nodes.length) return;

    // 渲染
    renderGraph();
    buildUI();
}

// ========= 从JSON构建图数据 =========
function buildGraphData(json) {
    const nodes = (json.items || []).map((it, idx) => ({
        id: it.id, type: it.type, name: it.name,
        keywords: (it.keywords||[]).slice(0,5),
        sources: (it.sources||[]).length || 1,
        domain: (it.domain||[]).slice(0,3),
        x: it.x || (400 + Math.random()*800),
        y: it.y || (300 + Math.random()*600),
        _idx: idx
    }));

    // 构建ID→索引映射
    const idMap = {};
    nodes.forEach(n => idMap[n.id] = n._idx);

    const links = [];
    (json.relations_summary || []).forEach(r => {
        const si = idMap[r.source_id];
        const ti = idMap[r.target_id];
        if (si !== undefined && ti !== undefined) {
            links.push({source: si, target: ti, type: r.type, note: (r.note||'').slice(0,100)});
        }
    });

    return {nodes, links, items: json.items || [], idMap};
}

// ========= 渲染图 =========
function renderGraph() {
    linkG = g.append('g');
    nodeG = g.append('g');

    linkSel = linkG.selectAll('line').data(data.links).join('line')
        .attr('class', 'link')
        .attr('stroke', d => RCM[d.type] || '#666')
        .attr('stroke-width', d => d.type === 'derives' ? 2 : d.type === 'generalizes' ? 1.5 : 1)
        .attr('stroke-dasharray', d => d.type === 'depends' ? '4,3' : d.type === 'equivalent' ? '5,2' : 'none');

    nodeSel = nodeG.selectAll('g').data(data.nodes).join('g')
        .attr('class', 'node')
        .attr('transform', d => `translate(${d.x},${d.y})`)
        .call(d3.drag()
            .on('start', function(e,d) { if(!e.active) e.subject.fx=d.x; e.subject.fy=d.y; })
            .on('drag', function(e,d) { d.x=e.x; d.y=e.y; d3.select(this).attr('transform',`translate(${d.x},${d.y})`); updateLinks(); })
            .on('end', function(e,d) { d.fx=null; d.fy=null; }));

    nodeSel.append('circle')
        .attr('r', d => SIZES[d.type] + Math.min(d.sources*2, 6))
        .attr('fill', d => CM[d.type])
        .attr('stroke', d => d3.color(CM[d.type]).darker(0.5))
        .on('click', (e,d) => showDetail(d))
        .on('mouseover', onNodeOver)
        .on('mouseout', onNodeOut);

    nodeSel.append('text')
        .text(d => { const n = d.name||d.id; return n.length>16?n.slice(0,14)+'..':n; })
        .attr('y', d => -(SIZES[d.type])-6)
        .attr('text-anchor', 'middle');

    updateLinks();
    updateVisibility();
}

function updateLinks() {
    linkSel.attr('x1', d => data.nodes[d.source].x)
        .attr('y1', d => data.nodes[d.source].y)
        .attr('x2', d => data.nodes[d.target].x)
        .attr('y2', d => data.nodes[d.target].y);
}

// ========= 视口裁剪 =========
function updateVisibility() {
    const t = d3.zoomTransform(svg.node());
    const s = t.k;
    const vx = -t.x / s, vy = -t.y / s;
    const vw = W / s, vh = H / s;
    const pad = 80;

    // LOD缩放级别
    const lodLow = s < 0.3;    // 极远: 仅圆点
    const lodMid = s < 0.6;    // 中远: 隐藏公式和标签
    const lodHigh = s > 1.5;   // 极近: 全量

    nodeSel.each(function(d) {
        const vis = d.x > vx-pad && d.x < vx+vw+pad && d.y > vy-pad && d.y < vy+vh+pad;
        const show = vis && !(lodMid && d.type === 'formula');
        d3.select(this).style('display', show ? null : 'none');
    });

    // 标签可见性
    nodeSel.selectAll('text').style('display', function(d) {
        const vis = d.x > vx-pad && d.x < vx+vw+pad && d.y > vy-pad && d.y < vy+vh+pad;
        return (vis && !lodLow && !(lodMid && d.type === 'formula')) ? null : 'none';
    });

    // 调整节点大小
    nodeSel.selectAll('circle').attr('r', function(d) {
        if (lodLow) return 3;
        if (lodMid && d.type === 'formula') return 4;
        if (lodHigh) return SIZES[d.type] + Math.min(d.sources*2, 8) + 3;
        return SIZES[d.type] + Math.min(d.sources*2, 6);
    });

    linkSel.style('display', function(d) {
        const ns = data.nodes[d.source], nt = data.nodes[d.target];
        const svis = ns.x > vx-pad && ns.x < vx+vw+pad && ns.y > vy-pad && ns.y < vy+vh+pad;
        const tvis = nt.x > vx-pad && nt.x < vx+vw+pad && nt.y > vy-pad && nt.y < vy+vh+pad;
        return (svis || tvis) && !lodLow ? null : 'none';
    });
}

let visibilityTimer;
function onZoom(e) {
    g.attr('transform', e.transform);
    clearTimeout(visibilityTimer);
    visibilityTimer = setTimeout(updateVisibility, 50);
}

// ========= 交互 =========
function onNodeOver(e, d) {
    d3.select(e.currentTarget).select('circle').transition().duration(150).attr('r', SIZES[d.type]+Math.min(d.sources*2,8)+3);

    const conn = new Set();
    data.links.forEach(l => {
        if (l.source === d._idx) conn.add(l.target);
        if (l.target === d._idx) conn.add(l.source);
    });
    nodeSel.selectAll('circle').attr('opacity', n => n._idx===d._idx||conn.has(n._idx)?1:0.12);
    linkSel.attr('opacity', l => l.source===d._idx||l.target===d._idx?1:0.03);
    showTooltip(e, d);
}

function onNodeOut(e, d) {
    d3.select(e.currentTarget).select('circle').transition().duration(150).attr('r', SIZES[d.type]+Math.min(d.sources*2,6));
    nodeSel.selectAll('circle').attr('opacity', 1);
    linkSel.attr('opacity', 0.35);
    hideTooltip();
}

function showTooltip(e, d) {
    d3.select('#tooltip')
        .html(`<div style="color:#64b5f6;font-weight:bold">${d.name}</div>
               <div style="font-size:10px;color:#90a4ae">${TCN[d.type]||d.type} | ${d.sources} sources</div>`)
        .style('left',(e.pageX+14)+'px').style('top',(e.pageY-14)+'px').style('opacity',1);
}
function hideTooltip() { d3.select('#tooltip').style('opacity',0); }

// ========= 详情面板 (按需加载) =========
async function showDetail(d) {
    const det = document.getElementById('detail');
    const badge = CM[d.type];

    // 从full items获取详情
    const full = data.items[d._idx];
    if (!full) { det.innerHTML = '<p style="color:#607d8b">详情不可用</p>'; return; }

    let h = `<h3>${full.name||d.name}</h3>`;
    h += `<span class="type-badge" style="background:${badge}">${TCN[d.type]}</span>`;
    h += `<span style="margin-left:6px;font-size:10px;color:#78909c">${d.sources} papers</span>`;

    if (full.summary) {
        h += `<div class="summary-block">📝 ${full.summary}</div>`;
    }
    if (full.latex) {
        h += `<div class="latex-block">${full.latex.slice(0,600)}</div>`;
    }
    if (full.statement && full.statement.length > 20) {
        h += `<div style="background:#0d1a22;border:1px solid #2a3a46;border-radius:5px;padding:8px;margin:4px 0;font-size:10px;color:#9e9e9e;max-height:180px;overflow-y:auto;line-height:1.5">${full.statement.slice(0,800)}</div>`;
    }
    if (full.premises) {
        h += `<div style="margin:4px 0;font-size:10px;color:#90caf9">前提: ${full.premises.slice(0,300)}</div>`;
    }
    if (full.conclusion) {
        h += `<div style="margin:4px 0;font-size:10px;color:#a5d6a7">结论: ${full.conclusion.slice(0,300)}</div>`;
    }
    if (full.keywords && full.keywords.length) {
        h += '<div style="margin-top:4px">'+full.keywords.map(k=>`<span style="display:inline-block;background:#1e3a4a;padding:1px 6px;border-radius:8px;margin:2px;font-size:10px;color:#90caf9">${k}</span>`).join('')+'</div>';
    }
    if (full.domain && full.domain.length) {
        h += '<div style="margin-top:2px">'+full.domain.map(d=>`<span style="display:inline-block;background:#2a1e3a;padding:1px 6px;border-radius:8px;margin:2px;font-size:10px;color:#ce93d8">${d}</span>`).join('')+'</div>';
    }
    if (full.confidence) {
        h += `<div style="margin-top:3px;font-size:10px;color:#78909c">置信度: ${(full.confidence*100).toFixed(0)}%</div>`;
    }

    det.innerHTML = h;

    // 关联列表
    const rl = document.getElementById('rel-list');
    const related = data.links.filter(l => l.source===d._idx||l.target===d._idx);
    if (related.length) {
        rl.innerHTML = related.map(l => {
            const oi = l.source===d._idx?l.target:l.source;
            const on = data.nodes[oi];
            return `<div class="rel-item" onclick="flyTo(${oi})">
                <span style="color:${RCM[l.type]};font-weight:bold">${RCN[l.type]}</span>
                → <span style="color:#64b5f6">${on?on.name:'?'}</span>
                <div style="color:#78909c;font-size:9px">${l.note||''}</div></div>`;
        }).join('');
    } else {
        rl.innerHTML = '<p style="color:#607d8b;font-size:10px">无直接关联</p>';
    }
}

// ========= UI =========
function buildUI() {
    // 统计
    const tc = {};
    data.nodes.forEach(n => tc[n.type] = (tc[n.type]||0)+1);
    const sd = document.getElementById('stats');
    Object.entries(tc).forEach(([t,c]) => {
        sd.innerHTML += `<div class="stat-chip"><span class="dot" style="background:${CM[t]}"></span>${TCN[t]}: ${c}</div>`;
    });
    sd.innerHTML += `<div class="stat-chip">🔗 ${data.links.length}</div>`;

    // 图例
    const ld = document.getElementById('legend');
    Object.entries(CM).forEach(([t,c]) => ld.innerHTML+=`<div class="legend-item"><span class="legend-dot" style="background:${c}"></span>${TCN[t]}</div>`);
    Object.entries(RCM).forEach(([t,c]) => ld.innerHTML+=`<div class="legend-item"><span class="legend-line" style="background:${c}"></span>${RCN[t]}</div>`);

    // 搜索
    document.getElementById('search').addEventListener('input', function(e) {
        const q = e.target.value.toLowerCase();
        if (!q) { nodeSel.selectAll('circle').attr('opacity',1); linkSel.attr('opacity',0.35); return; }
        const m = new Set();
        data.nodes.forEach(n => {
            const txt = (n.name+' '+(n.keywords||[]).join(' ')).toLowerCase();
            if (txt.includes(q)) m.add(n._idx);
        });
        nodeSel.selectAll('circle').attr('opacity', n=>m.has(n._idx)?1:0.06);
        linkSel.attr('opacity', l=>m.has(l.source)&&m.has(l.target)?1:0.02);
    });

    // 过滤
    let af = 'all';
    document.querySelectorAll('.fbtn').forEach(b => b.addEventListener('click', function() {
        document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));
        this.classList.add('active');
        af = this.dataset.type;
        if (af==='all') { nodeSel.style('display',null); linkSel.style('display',null); }
        else {
            const m = new Set();
            data.nodes.forEach(n=>{if(n.type===af)m.add(n._idx);});
            nodeSel.style('display',n=>m.has(n._idx)?null:'none');
            linkSel.style('display',l=>m.has(l.source)||m.has(l.target)?null:'none');
        }
    }));

    // 缩放控制
    document.getElementById('zin').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,1.3));
    document.getElementById('zout').addEventListener('click',()=>svg.transition().duration(200).call(zoom.scaleBy,0.7));
    document.getElementById('zfit').addEventListener('click',()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity));

    // 初始视口
    updateVisibility();
}

window.flyTo = function(idx) {
    const n = data.nodes[idx];
    if (!n) return;
    showDetail(n);
    const t = d3.zoomIdentity.translate(W/2,H/2).scale(1.4).translate(-n.x,-n.y);
    svg.transition().duration(500).call(zoom.transform, t);
};

// 启动
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
