/**
 * 数学知识图谱 — 幻灯片引擎 + D3.js 可视化
 * 小组汇报 PPT 风格 · 9 页幻灯片
 */

// ═══════════════════════════════════════════
// Constants
// ═══════════════════════════════════════════
const CM = {
  theorem: '#e05560', lemma: '#4da6d9', corollary: '#43b884',
  definition: '#9b6cc4', proposition: '#e8963e'
};
const TCN = {
  theorem: 'Theorem', lemma: 'Lemma', corollary: 'Corollary',
  definition: 'Definition', proposition: 'Proposition'
};
const RCM = {
  derives: '#e05560', generalizes: '#4da6d9',
  equivalent: '#43b884', depends: '#7a8a9a'
};
const RCN = {
  derives: 'Derives', generalizes: 'Generalizes',
  equivalent: 'Equivalent', depends: 'Depends'
};
const SZ = { theorem: 14, lemma: 12, corollary: 10, definition: 13, proposition: 12 };

// ═══════════════════════════════════════════
// Global State
// ═══════════════════════════════════════════
let graphData = null;   // raw JSON from /api/graph
let currentSlide = 0;
const TOTAL_SLIDES = 9;
let slidesRendered = new Set();

// ═══════════════════════════════════════════
// Initialization
// ═══════════════════════════════════════════
async function init() {
  // Load data
  try {
    const resp = await fetch('/api/graph');
    if (!resp.ok) {
      const err = await resp.json();
      showError(err.message || 'Failed to load graph data');
      return;
    }
    graphData = await resp.json();
  } catch (e) {
    showError(`Cannot connect to server.<br>Make sure <code>npm start</code> is running and <code>output/knowledge_network.json</code> exists.`);
    return;
  }

  // Hide loading
  document.getElementById('loading-overlay').classList.add('hidden');

  // Setup navigation
  setupNav();

  // Render first slide
  goToSlide(0);
}

function showError(msg) {
  const overlay = document.getElementById('loading-overlay');
  overlay.querySelector('.spinner').style.display = 'none';
  overlay.querySelector('.msg').textContent = 'Failed to load';
  overlay.querySelector('.error-msg').innerHTML = msg;
}

// ═══════════════════════════════════════════
// Navigation
// ═══════════════════════════════════════════
function setupNav() {
  document.getElementById('prev-btn').addEventListener('click', () => {
    if (currentSlide > 0) goToSlide(currentSlide - 1);
  });
  document.getElementById('next-btn').addEventListener('click', () => {
    if (currentSlide < TOTAL_SLIDES - 1) goToSlide(currentSlide + 1);
  });

  // Dot indicators
  const dots = document.getElementById('slide-dots');
  for (let i = 0; i < TOTAL_SLIDES; i++) {
    const dot = document.createElement('div');
    dot.className = 'slide-dot';
    dot.addEventListener('click', () => goToSlide(i));
    dots.appendChild(dot);
  }

  // Keyboard
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
      e.preventDefault();
      if (currentSlide < TOTAL_SLIDES - 1) goToSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (currentSlide > 0) goToSlide(currentSlide - 1);
    } else if (e.key === 'Home') {
      e.preventDefault();
      goToSlide(0);
    } else if (e.key === 'End') {
      e.preventDefault();
      goToSlide(TOTAL_SLIDES - 1);
    }
  });

  // Touch swipe
  let touchStartX = 0;
  document.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) {
      if (dx < 0 && currentSlide < TOTAL_SLIDES - 1) goToSlide(currentSlide + 1);
      else if (dx > 0 && currentSlide > 0) goToSlide(currentSlide - 1);
    }
  });
}

function goToSlide(n) {
  // Update slide classes
  document.querySelectorAll('.slide').forEach((s, i) => {
    s.classList.remove('active', 'prev');
    if (i === n) s.classList.add('active');
    else if (i < n) s.classList.add('prev');
  });

  // Update dots
  document.querySelectorAll('.slide-dot').forEach((d, i) => {
    d.classList.toggle('active', i === n);
  });

  currentSlide = n;

  // Lazy render
  if (!slidesRendered.has(n)) {
    renderSlide(n);
    slidesRendered.add(n);
  }

  // Resize graph if entering slide 3
  if (n === 3 && slidesRendered.has(3)) {
    setTimeout(() => resizeGraph(), 100);
  }
}

// ═══════════════════════════════════════════
// Slide Renderers
// ═══════════════════════════════════════════
function renderSlide(n) {
  const renderers = {
    0: renderTitle,
    1: renderPapers,
    2: renderTypes,
    3: renderGraph,
    4: renderKeywords,
    5: renderRelations,
    6: renderKeyTheorems,
    7: renderTimeline,
    8: renderSummary
  };
  if (renderers[n]) renderers[n]();
}

// ── Slide 0: Title ──────────────────────────
function renderTitle() {
  const items = graphData.items || [];
  const stats = graphData.statistics || {};
  const container = document.getElementById('title-stats');
  container.innerHTML = [
    { n: stats.total_papers || 0, l: 'Papers' },
    { n: stats.total_items || items.length, l: 'Items' },
    { n: stats.total_relations || 0, l: 'Relations' },
    { n: Object.keys(CM).length, l: 'Types' }
  ].map(s => `<div class="title-stat"><div class="number">${s.n}</div><div class="label">${s.l}</div></div>`).join('');
}

// ── Slide 1: Papers Overview ────────────────
function renderPapers() {
  const papers = graphData.papers || [];
  const container = document.getElementById('papers-grid');
  container.innerHTML = papers.map(p => `
    <div class="paper-card">
      <div class="year">${p.year || '?'}</div>
      <div class="title">${(p.title || '').slice(0, 100)}</div>
      <div class="authors">ID: ${p.id}</div>
    </div>
  `).join('');
}

// ── Slide 2: Type Distribution ──────────────
function renderTypes() {
  const items = graphData.items || [];

  // Count by type
  const counts = {};
  items.forEach(it => { counts[it.type] = (counts[it.type] || 0) + 1; });

  // ── Bar Chart ──
  const area = document.getElementById('type-chart');
  area.innerHTML = '';
  const W = area.clientWidth || 500, H = area.clientHeight || 400;
  const margin = { top: 40, right: 40, bottom: 50, left: 100 };
  const iw = W - margin.left - margin.right, ih = H - margin.top - margin.bottom;

  const svg = d3.select('#type-chart').append('svg').attr('viewBox', `0 0 ${W} ${H}`);
  const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

  const types = Object.keys(CM).filter(t => counts[t]);
  const maxC = d3.max(types, t => counts[t]);

  const x = d3.scaleLinear().domain([0, maxC]).range([0, iw]);
  const y = d3.scaleBand().domain(types).range([0, ih]).padding(0.4);

  // Title
  g.append('text').attr('class', 'chart-title-text')
    .attr('x', iw / 2).attr('y', -20).attr('text-anchor', 'middle')
    .text('Items by Type');

  // Axes
  g.append('g').call(d3.axisLeft(y).tickFormat(t => TCN[t] || t))
    .selectAll('text').attr('fill', '#8090a0').attr('font-size', '12px');
  g.selectAll('.domain,.tick line').attr('stroke', '#1e3040');

  g.append('g').attr('transform', `translate(0,${ih})`)
    .call(d3.axisBottom(x).ticks(5).tickFormat(d3.format('d')))
    .selectAll('text').attr('fill', '#506070').attr('font-size', '10px');
  g.selectAll('.domain,.tick line').attr('stroke', '#1e3040');

  // Bars with animation
  g.selectAll('rect').data(types).join('rect')
    .attr('y', d => y(d))
    .attr('height', y.bandwidth())
    .attr('x', 0).attr('width', 0)
    .attr('fill', d => CM[d])
    .attr('rx', 3)
    .transition().duration(800).delay((d, i) => i * 100)
    .attr('width', d => x(counts[d]));

  // Value labels
  g.selectAll('.val').data(types).join('text')
    .attr('class', 'val')
    .attr('y', d => y(d) + y.bandwidth() / 2)
    .attr('dy', '0.35em')
    .attr('fill', '#b0c0d0').attr('font-size', '12px').attr('font-weight', '600')
    .attr('x', d => x(counts[d]) + 8)
    .text(d => counts[d]);

  // ── Examples ──
  const examplesDiv = document.getElementById('type-examples');
  const topByType = {};
  types.forEach(t => {
    topByType[t] = items
      .filter(it => it.type === t)
      .sort((a, b) => (b.sources || []).length - (a.sources || []).length)
      .slice(0, 3);
  });

  examplesDiv.innerHTML = types.map(t => {
    const examples = topByType[t] || [];
    return examples.map(it => `
      <div class="example-card">
        <span class="badge" style="background:${CM[t]}">${TCN[t]}</span>
        <div class="name">${it.name || it.id}</div>
        <div class="stmt">${(it.statement || it.summary || '').slice(0, 200)}</div>
      </div>
    `).join('');
  }).join('');
}

// ── Slide 3: Interactive Graph ──────────────
let graphState = null;

function renderGraph() {
  const container = document.getElementById('graph-canvas');
  const W = container.clientWidth, H = container.clientHeight;
  const items = graphData.items || [];
  const relations = graphData.relations_summary || [];
  const papers = graphData.papers || [];

  if (!items.length) return;

  // Build graph data
  const nodes = items.map((it, idx) => ({
    id: it.id, type: it.type, name: it.name,
    keywords: (it.keywords || []).slice(0, 5),
    sources: it.sources || [it.id.split('_')[0]],
    papers: it.sources || [it.id.split('_')[0]],
    x: it.x || (400 + Math.random() * 800),
    y: it.y || (300 + Math.random() * 600),
    _i: idx
  }));

  const idMap = {};
  nodes.forEach(n => idMap[n.id] = n._i);

  const linkData = [];
  relations.forEach(r => {
    const si = idMap[r.source_id], ti = idMap[r.target_id];
    if (si !== undefined && ti !== undefined) {
      linkData.push({ source: si, target: ti, type: r.type, note: (r.note || '').slice(0, 80) });
    }
  });

  // Same-paper edges
  const spLinks = [];
  const paperGroups = {};
  nodes.forEach((n, i) => {
    (n.papers || []).forEach(pid => {
      paperGroups[pid] = paperGroups[pid] || [];
      paperGroups[pid].push(i);
    });
  });
  Object.values(paperGroups).forEach(indices => {
    for (let a = 0; a < indices.length; a++) {
      for (let b = a + 1; b < Math.min(a + 5, indices.length); b++) {
        spLinks.push({ source: indices[a], target: indices[b] });
      }
    }
  });

  // Detail map
  const detailMap = {};
  items.forEach((it, idx) => {
    const d = {};
    if (it.summary) d.sm = it.summary;
    if (it.statement && it.statement.length > 20) d.st = it.statement.slice(0, 600);
    if (it.premises) d.pr = it.premises.slice(0, 300);
    if (it.conclusion) d.cl = it.conclusion.slice(0, 300);
    if (it.domain) d.dm = it.domain.slice(0, 5);
    if (it.latex) d.fm = [it.latex.slice(0, 600)];
    if (Object.keys(d).length) detailMap[String(idx)] = d;
  });

  // ── D3 Rendering ──
  const svg = d3.select('#graph-canvas svg');
  svg.selectAll('*').remove();

  const zoom = d3.zoom().scaleExtent([0.08, 5.5]).on('zoom', e => {
    g.attr('transform', e.transform);
    updateVis(e.transform);
  });
  svg.call(zoom);

  const g = svg.append('g');

  // Same-paper edges (bottom layer)
  const splG = g.append('g');
  splG.selectAll('line').data(spLinks).join('line')
    .attr('class', 'link-sp')
    .attr('stroke', RCM.same_paper || '#3a4a60')
    .attr('stroke-width', 0.6)
    .attr('stroke-dasharray', '2,6')
    .attr('stroke-opacity', 0.15);

  // Relation edges
  const linkG = g.append('g');
  const linkSel = linkG.selectAll('line').data(linkData).join('line')
    .attr('class', 'link')
    .attr('stroke', d => RCM[d.type] || '#7a8a9a')
    .attr('stroke-width', d => d.type === 'derives' ? 2.2 : d.type === 'generalizes' ? 1.6 : 1.1)
    .attr('stroke-dasharray', d =>
      d.type === 'depends' ? '5,3' : d.type === 'equivalent' ? '6,3' :
      d.type === 'generalizes' ? '8,2' : 'none');

  // Nodes
  const nodeG = g.append('g');
  const nodeSel = nodeG.selectAll('g').data(nodes).join('g')
    .attr('class', 'node')
    .attr('transform', d => `translate(${d.x},${d.y})`)
    .call(d3.drag()
      .on('drag', function (e, d) {
        d.x = e.x; d.y = e.y;
        d3.select(this).attr('transform', `translate(${d.x},${d.y})`);
        updateAllLinks();
      }));

  nodeSel.append('circle')
    .attr('r', d => (SZ[d.type] || 10) + Math.min((d.sources || []).length * 2, 6))
    .attr('fill', d => CM[d.type] || '#666')
    .attr('stroke', d => d3.color(CM[d.type] || '#666').darker(0.6));

  nodeSel.append('text')
    .text(d => { const n = d.name || d.id; return n.length > 10 ? n.slice(0, 9) + '…' : n; })
    .attr('y', d => -(SZ[d.type] || 10) - 6)
    .attr('opacity', 0);

  // ── Interaction ──
  nodeSel.on('mouseover', function (e, d) {
    const r = (SZ[d.type] || 10) + Math.min((d.sources || []).length * 2, 6);
    d3.select(this).select('circle').transition().duration(120).attr('r', r + 3);
    const conn = new Set();
    linkData.forEach(l => {
      if (l.source === d._i) conn.add(l.target);
      if (l.target === d._i) conn.add(l.source);
    });
    nodeSel.selectAll('circle').attr('opacity', n => n._i === d._i || conn.has(n._i) ? 1 : 0.15);
    linkSel.attr('opacity', l => l.source === d._i || l.target === d._i ? 0.9 : 0.04);
    showGraphTooltip(e, d);
  }).on('mouseout', function (e, d) {
    d3.select(this).select('circle').transition().duration(120)
      .attr('r', (SZ[d.type] || 10) + Math.min((d.sources || []).length * 2, 6));
    nodeSel.selectAll('circle').attr('opacity', 1);
    linkSel.attr('opacity', 0.28);
    hideGraphTooltip();
  }).on('click', (e, d) => showGraphDetail(e, d));

  // ── Update functions ──
  function updateAllLinks() {
    linkSel.attr('x1', d => nodes[d.source].x).attr('y1', d => nodes[d.source].y)
      .attr('x2', d => nodes[d.target].x).attr('y2', d => nodes[d.target].y);
    splG.selectAll('line')
      .attr('x1', d => nodes[d.source].x).attr('y1', d => nodes[d.source].y)
      .attr('x2', d => nodes[d.target].x).attr('y2', d => nodes[d.target].y);
  }
  updateAllLinks();

  function updateVis(t) {
    if (!t) t = d3.zoomTransform(svg.node());
    const s = t.k, vx = -t.x / s, vy = -t.y / s, vw = W / s, vh = H / s, pad = 50;
    const lo = s < 0.35;
    nodeSel.each(function (d) {
      const inV = d.x > vx - pad && d.x < vx + vw + pad && d.y > vy - pad && d.y < vy + vh + pad;
      d3.select(this).style('display', inV ? null : 'none');
    });
    nodeSel.selectAll('text').attr('opacity', function (d) {
      const inV = d.x > vx - pad && d.x < vx + vw + pad && d.y > vy - pad && d.y < vy + vh + pad;
      return (inV && s > 1.2) ? 1 : 0;
    });
    nodeSel.selectAll('circle').attr('r', function (d) {
      const base = SZ[d.type] || 10;
      if (lo) return 3;
      if (s < 0.75) return base * 0.7;
      if (s > 1.8) return base + Math.min((d.sources || []).length * 2, 8);
      return base;
    });
    linkSel.style('display', d => {
      if (lo) return 'none';
      const ns = nodes[d.source], nt = nodes[d.target];
      const sv = ns.x > vx - pad && ns.x < vx + vw + pad && ns.y > vy - pad && ns.y < vy + vh + pad;
      const tv = nt.x > vx - pad && nt.x < vx + vw + pad && nt.y > vy - pad && nt.y < vy + vh + pad;
      return (sv || tv) ? null : 'none';
    });
  }

  // ── Store state ──
  graphState = { nodes, nodeSel, linkSel, splG, linkData, detailMap, svg, zoom, updateAllLinks, updateVis };

  // ── Legend ──
  const legendDiv = document.getElementById('graph-legend');
  legendDiv.innerHTML = Object.entries(CM).map(([t, c]) =>
    `<div class="gl-item"><span class="gl-dot" style="background:${c}"></span>${TCN[t]}</div>`
  ).join('') + Object.entries(RCM).slice(0, 4).map(([t, c]) =>
    `<div class="gl-item"><span class="gl-line solid" style="border-color:${c}"></span>${RCN[t]}</div>`
  ).join('');

  // ── Search ──
  document.getElementById('graph-search-input').addEventListener('input', function () {
    const q = this.value.toLowerCase();
    if (!graphState) return;
    if (!q) {
      graphState.nodeSel.selectAll('circle').attr('opacity', 1);
      graphState.linkSel.attr('opacity', 0.28);
      return;
    }
    const match = new Set();
    graphState.nodes.forEach(n => {
      if ((n.name + ' ' + (n.keywords || []).join(' ')).toLowerCase().includes(q)) match.add(n._i);
    });
    graphState.nodeSel.selectAll('circle').attr('opacity', n => match.has(n._i) ? 1 : 0.06);
    graphState.linkSel.attr('opacity', l => match.has(l.source) && match.has(l.target) ? 1 : 0.02);
  });

  // ── Zoom buttons ──
  document.getElementById('zin').onclick = () => svg.transition().duration(200).call(zoom.scaleBy, 1.3);
  document.getElementById('zout').onclick = () => svg.transition().duration(200).call(zoom.scaleBy, 0.7);
  document.getElementById('zfit').onclick = () => svg.transition().duration(400).call(zoom.transform, d3.zoomIdentity);

  // ── Tooltip ──
  window.showGraphTooltip = function (e, d) {
    d3.select('#tooltip')
      .html(`<div style="color:#d0d8e0;font-weight:600">${d.name}</div><div style="font-size:9px;color:var(--dim)">${TCN[d.type]} · ${d.sources.length} paper(s)</div>`)
      .style('left', (e.pageX + 12) + 'px').style('top', (e.pageY - 12) + 'px').style('opacity', 1);
  };
  window.hideGraphTooltip = function () { d3.select('#tooltip').style('opacity', 0); };

  // ── Detail ──
  window.showGraphDetail = function (e, d) {
    // We use a simple floating detail for the graph slide
    const dt = detailMap[String(d._i)] || {};
    // Just flash the tooltip with more info
    let html = `<div style="color:#d0d8e0;font-weight:600;font-size:11px">${d.name}</div>`;
    html += `<div style="font-size:9px;color:#8090a0;margin-top:2px">${TCN[d.type]} · ${d.sources.length} sources</div>`;
    if (dt.sm) html += `<div style="font-size:9px;color:#8cb88c;margin-top:3px;max-width:240px;line-height:1.4">${dt.sm}</div>`;
    if (dt.fm) html += `<div style="font-size:10px;color:#e2b04a;margin-top:3px;font-family:monospace;max-width:240px;overflow:hidden;text-overflow:ellipsis">${dt.fm[0].slice(0, 200)}</div>`;
    d3.select('#tooltip')
      .html(html)
      .style('left', (e.pageX + 12) + 'px')
      .style('top', (e.pageY - 12) + 'px')
      .style('opacity', 1);
    setTimeout(() => d3.select('#tooltip').style('opacity', 0), 3000);
  };

  // Initial viewport
  setTimeout(() => graphState && graphState.updateVis(), 200);
}

function resizeGraph() {
  if (!graphState) return;
  graphState.svg.selectAll('*').remove();
  renderGraph();
}

// ── Slide 4: Keyword Analysis ───────────────
function renderKeywords() {
  const items = graphData.items || [];

  // Count keywords
  const kwCounts = {};
  items.forEach(it => {
    (it.keywords || []).forEach(kw => {
      kwCounts[kw] = (kwCounts[kw] || 0) + 1;
    });
  });

  const sorted = Object.entries(kwCounts)
    .filter(([kw]) => !['theorem', 'lemma', 'corollary', 'definition', 'proposition'].includes(kw))
    .sort((a, b) => b[1] - a[1])
    .slice(0, 20);

  const maxC = sorted[0] ? sorted[0][1] : 1;

  // ── Horizontal Bar Chart ──
  const barsDiv = document.getElementById('keyword-bars');
  barsDiv.innerHTML = '';
  const barW = barsDiv.clientWidth || 500, barH = barsDiv.clientHeight || 400;
  const bMargin = { top: 30, right: 40, bottom: 10, left: 110 };

  const bSvg = d3.select('#keyword-bars').append('svg').attr('viewBox', `0 0 ${barW} ${barH}`);
  const bG = bSvg.append('g').attr('transform', `translate(${bMargin.left},${bMargin.top})`);
  const biw = barW - bMargin.left - bMargin.right, bih = barH - bMargin.top - bMargin.bottom;

  bG.append('text').attr('class', 'chart-title-text')
    .attr('x', biw / 2).attr('y', -12).attr('text-anchor', 'middle')
    .text('Top 20 Keywords');

  const barHeight = Math.min(22, bih / sorted.length - 4);
  sorted.forEach(([kw, count], i) => {
    const y = i * (bih / sorted.length);
    const w = (count / maxC) * biw * 0.9;

    bG.append('text').attr('x', -6).attr('y', y + barHeight / 2)
      .attr('dy', '0.35em').attr('text-anchor', 'end')
      .attr('fill', '#8090a0').attr('font-size', '10px')
      .text(kw.replace(/_/g, ' '));

    const bar = bG.append('rect')
      .attr('x', 0).attr('y', y + 1).attr('height', barHeight - 2)
      .attr('fill', d3.interpolateBlues(count / maxC * 0.7 + 0.3))
      .attr('rx', 2).attr('width', 0);

    bar.transition().duration(600).delay(i * 30).attr('width', w);

    bG.append('text').attr('x', w + 6).attr('y', y + barHeight / 2)
      .attr('dy', '0.35em').attr('fill', '#506070').attr('font-size', '9px')
      .text(count);
  });

  // ── Bubble / Cloud (right panel) ──
  const cloudDiv = document.getElementById('keyword-cloud');
  cloudDiv.innerHTML = '';
  const cW = cloudDiv.clientWidth || 400, cH = cloudDiv.clientHeight || 400;

  const cSvg = d3.select('#keyword-cloud').append('svg').attr('viewBox', `0 0 ${cW} ${cH}`);
  const packData = { children: sorted.map(([kw, c]) => ({ name: kw, value: c })) };
  const pack = d3.pack().size([cW - 20, cH - 20]).padding(4);
  const root = d3.hierarchy(packData).sum(d => d.value);
  pack(root);

  const colorScale = d3.scaleSequential(d3.interpolateBlues).domain([0, maxC]);

  cSvg.append('text').attr('class', 'chart-title-text')
    .attr('x', cW / 2).attr('y', 16).attr('text-anchor', 'middle')
    .text('Keyword Density');

  const bubbles = cSvg.append('g').attr('transform', `translate(10,30)`);
  bubbles.selectAll('circle').data(root.leaves()).join('circle')
    .attr('cx', d => d.x).attr('cy', d => d.y)
    .attr('r', 0)
    .attr('fill', d => colorScale(d.data.value))
    .attr('stroke', '#1e3040').attr('stroke-width', 1)
    .attr('opacity', 0.85)
    .transition().duration(800).delay((d, i) => i * 30)
    .attr('r', d => d.r);

  bubbles.selectAll('text').data(root.leaves()).join('text')
    .attr('x', d => d.x).attr('y', d => d.y)
    .attr('text-anchor', 'middle').attr('dy', '0.3em')
    .attr('fill', '#d0d8e0').attr('font-size', d => Math.min(d.r / 2.5, 12) + 'px')
    .attr('opacity', 0)
    .text(d => d.data.name.length > 14 ? d.data.name.slice(0, 12) + '…' : d.data.name)
    .transition().duration(400).delay((d, i) => i * 50 + 400)
    .attr('opacity', 1);
}

// ── Slide 5: Relation Types ─────────────────
function renderRelations() {
  const relations = graphData.relations_summary || [];
  const items = graphData.items || [];

  const rCounts = {};
  relations.forEach(r => { rCounts[r.type] = (rCounts[r.type] || 0) + 1; });

  // ── Stats (left) ──
  const statsDiv = document.getElementById('relation-stats');
  statsDiv.innerHTML = '';

  const sW = statsDiv.clientWidth || 500, sH = statsDiv.clientHeight || 400;
  const sSvg = d3.select('#relation-stats').append('svg').attr('viewBox', `0 0 ${sW} ${sH}`);

  const pieData = Object.entries(rCounts).map(([t, c]) => ({ type: t, count: c }));
  const total = d3.sum(pieData, d => d.count);
  const radius = Math.min(sW, sH) / 2 - 40;

  const arc = d3.arc().innerRadius(radius * 0.5).outerRadius(radius).cornerRadius(4);
  const pie = d3.pie().value(d => d.count).sort(null);
  const arcs = pie(pieData);

  const pieG = sSvg.append('g').attr('transform', `translate(${sW / 2},${sH / 2})`);

  // Title
  sSvg.append('text').attr('class', 'chart-title-text')
    .attr('x', sW / 2).attr('y', 20).attr('text-anchor', 'middle')
    .text(`Total: ${total} Relations`);

  arcs.forEach((a, i) => {
    const seg = pieG.append('path')
      .attr('d', arc(a))
      .attr('fill', RCM[a.data.type] || '#666')
      .attr('stroke', '#0d1520').attr('stroke-width', 2)
      .attr('opacity', 0);

    seg.transition().duration(600).delay(i * 150).attr('opacity', 1);

    // Label
    const [lx, ly] = arc.centroid(a);
    pieG.append('text')
      .attr('x', lx).attr('y', ly)
      .attr('text-anchor', 'middle').attr('dy', '0.35em')
      .attr('fill', '#fff').attr('font-size', '11px').attr('font-weight', '600')
      .attr('opacity', 0)
      .text(`${a.data.count}`)
      .transition().duration(400).delay(i * 150 + 400).attr('opacity', 1);

    // Legend inside chart
    const la = (a.startAngle + a.endAngle) / 2;
    const lr = radius + 25;
    pieG.append('text')
      .attr('x', Math.cos(la - Math.PI / 2) * lr)
      .attr('y', Math.sin(la - Math.PI / 2) * lr)
      .attr('text-anchor', 'middle').attr('dy', '0.3em')
      .attr('fill', '#8090a0').attr('font-size', '10px')
      .text(RCN[a.data.type] || a.data.type);
  });

  // ── Examples (right) ──
  const examplesDiv = document.getElementById('relation-examples');
  const idToItem = {};
  items.forEach(it => idToItem[it.id] = it);

  // Pick top 8 relations with longest notes
  const sampleRels = relations
    .filter(r => r.note && r.note.length > 10)
    .sort((a, b) => (b.note || '').length - (a.note || '').length)
    .slice(0, 8);

  examplesDiv.innerHTML = sampleRels.map(r => {
    const src = idToItem[r.source_id];
    const tgt = idToItem[r.target_id];
    return `
      <div class="example-card">
        <span style="color:${RCM[r.type] || '#666'};font-weight:600;font-size:11px">${RCN[r.type] || r.type}</span>
        <span style="color:var(--dim);font-size:10px;margin:0 4px">→</span>
        <span style="color:#d0d8e0;font-size:11px">${src ? src.name : r.source_id}</span>
        <span style="color:var(--dim);font-size:10px;margin:0 4px">→</span>
        <span style="color:#d0d8e0;font-size:11px">${tgt ? tgt.name : r.target_id}</span>
        <div style="font-size:9px;color:var(--dim);margin-top:3px">${r.note || ''}</div>
      </div>
    `;
  }).join('') || '<p style="color:var(--dim);text-align:center;padding:40px">No detailed relation notes available</p>';
}

// ── Slide 6: Key Theorems ───────────────────
function renderKeyTheorems() {
  const items = graphData.items || [];
  const relations = graphData.relations_summary || [];
  const papers = graphData.papers || [];

  // Score items by: connection count + source count + confidence
  const paperMap = {};
  (papers || []).forEach(p => { paperMap[p.id] = p; });

  const connCount = {};
  relations.forEach(r => {
    connCount[r.source_id] = (connCount[r.source_id] || 0) + 1;
    connCount[r.target_id] = (connCount[r.target_id] || 0) + 1;
  });

  const scored = items.map(it => ({
    ...it,
    score: (connCount[it.id] || 0) * 3 + (it.sources || []).length * 2 + (it.confidence || 0) * 5
  }));

  scored.sort((a, b) => b.score - a.score);
  const top = scored.slice(0, 12);

  const container = document.getElementById('key-theorems');
  container.innerHTML = top.map((it, i) => {
    const paperId = (it.sources || [])[0] || it.id.split('_')[0];
    const paper = paperMap[paperId];
    const paperRef = paper ? `[${paper.year}] ${(paper.title || '').slice(0, 60)}` : paperId;
    return `
      <div class="key-item">
        <div class="rank">${i + 1}</div>
        <div style="flex:1">
          <span class="badge" style="background:${CM[it.type] || '#666'}">${TCN[it.type] || it.type}</span>
          <div class="name">${it.name}</div>
          <div class="desc">${(it.summary || it.statement || '').slice(0, 250)}</div>
          <div class="paper-ref">📄 ${paperRef}</div>
          <div class="kw-row">
            ${(it.keywords || []).slice(0, 8).map(k => `<span class="kw-tag">${k}</span>`).join('')}
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// ── Slide 7: Timeline ───────────────────────
function renderTimeline() {
  const papers = graphData.papers || [];
  const items = graphData.items || [];

  // Count items per paper
  const paperItems = {};
  items.forEach(it => {
    (it.sources || [it.id.split('_')[0]]).forEach(pid => {
      paperItems[pid] = (paperItems[pid] || 0) + 1;
    });
  });

  // Sort by year
  const sorted = [...papers].sort((a, b) => (a.year || '0').localeCompare(b.year || '0'));

  const container = document.getElementById('timeline');
  container.innerHTML = sorted.map((p, i) => `
    <div class="timeline-row">
      <div class="timeline-year">${p.year || '?'}</div>
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="t-title">${(p.title || '').slice(0, 120)}</div>
        <div class="t-meta">${paperItems[p.id] || 0} extracted items · ID: ${p.id}</div>
      </div>
    </div>
  `).join('');

  // Add the timeline line
  const firstDot = container.querySelector('.timeline-dot');
  const lastDot = container.querySelector('.timeline-row:last-child .timeline-dot');
  if (firstDot && lastDot) {
    const line = document.createElement('div');
    line.className = 'timeline-line';
    line.style.top = firstDot.offsetTop + 'px';
    line.style.height = (lastDot.offsetTop - firstDot.offsetTop) + 'px';
    container.appendChild(line);
  }
}

// ── Slide 8: Summary ────────────────────────
function renderSummary() {
  const items = graphData.items || [];
  const relations = graphData.relations_summary || [];
  const papers = graphData.papers || [];
  const stats = graphData.statistics || {};

  const tc = {};
  items.forEach(it => { tc[it.type] = (tc[it.type] || 0) + 1; });

  const container = document.getElementById('summary-stats');
  container.innerHTML = [
    { n: papers.length, l: 'Papers', c: 'var(--gold)' },
    { n: items.length, l: 'Items', c: 'var(--acc)' },
    { n: relations.length, l: 'Relations', c: 'var(--c-corollary)' },
    { n: Object.keys(tc).length, l: 'Item Types', c: 'var(--c-definition)' }
  ].map(s => `<div class="summary-card"><div class="num" style="color:${s.c}">${s.n}</div><div class="lbl">${s.l}</div></div>`).join('');
}

// ═══════════════════════════════════════════
// Boot
// ═══════════════════════════════════════════
document.addEventListener('DOMContentLoaded', init);

// Handle window resize for graph slide
window.addEventListener('resize', () => {
  if (currentSlide === 3 && graphState) {
    clearTimeout(window._resizeTimer);
    window._resizeTimer = setTimeout(() => resizeGraph(), 300);
  }
});
