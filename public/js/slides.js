/**
 * AI 暑期学校 — 知识管理智能体幻灯片
 * 12 页 · 3 部分 · 白底 PPT 风格
 */

const CM={theorem:'#dc2626',lemma:'#2563eb',corollary:'#059669',definition:'#7c3aed',proposition:'#d97706'};
const TCN={theorem:'定理',lemma:'引理',corollary:'推论',definition:'定义',proposition:'命题'};
const RCM={derives:'#dc2626',generalizes:'#2563eb',equivalent:'#059669',depends:'#9ca3af'};
const RCN={derives:'推导',generalizes:'推广',equivalent:'等价',depends:'依赖'};
const SZ={theorem:14,lemma:12,corollary:10,definition:13,proposition:12};

let graphData=null,currentSlide=0;
const TOTAL=12;

async function init(){
  try{
    const r=await fetch('/api/graph');
    if(!r.ok){showErr('加载失败');return;}
    graphData=await r.json();
  }catch(e){showErr('无法连接服务器。<br>请运行 <code>npm start</code>。');return;}

  // 为每页插入 logo
  document.querySelectorAll('.slide').forEach(s=>{
    if(!s.querySelector('.slide-logo')){
      const logo=document.createElement('img');logo.src='/png/sjtu_logo.png';logo.className='slide-logo';logo.alt='SJTU';s.appendChild(logo);
    }
  });

  const R={0:r0,1:r1,2:r2,3:r3,4:r4,5:r5,6:r6,7:r7,8:r8,9:r9,10:r10,11:r11};
  let rendered=0;
  for(let i=0;i<TOTAL;i++){
    setTimeout(()=>{
      if(R[i]&&graphData){try{R[i]();rendered++;}catch(e){console.error('Slide '+i+':',e);}}
      if(i===TOTAL-1)setTimeout(()=>{document.getElementById('loading-overlay').classList.add('hidden');setupNav();goToSlide(0);},200);
    },i*60);
  }
}

function showErr(m){
  const o=document.getElementById('loading-overlay');
  o.querySelector('.spinner').style.display='none';
  o.querySelector('.msg').textContent='加载失败';
  o.querySelector('.error-msg').innerHTML=m;
}

function setupNav(){
  document.getElementById('prev-btn').addEventListener('click',()=>{if(currentSlide>0)goToSlide(currentSlide-1);});
  document.getElementById('next-btn').addEventListener('click',()=>{if(currentSlide<TOTAL-1)goToSlide(currentSlide+1);});
  const dots=document.getElementById('slide-dots');
  for(let i=0;i<TOTAL;i++){const d=document.createElement('div');d.className='slide-dot';d.addEventListener('click',()=>goToSlide(i));dots.appendChild(d);}
  document.addEventListener('keydown',e=>{
    if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' '){e.preventDefault();if(currentSlide<TOTAL-1)goToSlide(currentSlide+1);}
    else if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();if(currentSlide>0)goToSlide(currentSlide-1);}
    else if(e.key==='Home'){e.preventDefault();goToSlide(0);}
    else if(e.key==='End'){e.preventDefault();goToSlide(TOTAL-1);}
  });
  let tx=0;document.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;});
  document.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50){if(dx<0&&currentSlide<TOTAL-1)goToSlide(currentSlide+1);else if(dx>0&&currentSlide>0)goToSlide(currentSlide-1);}});
}
function goToSlide(n){
  document.querySelectorAll('.slide').forEach((s,i)=>{s.classList.remove('active','prev');if(i===n)s.classList.add('active');else if(i<n)s.classList.add('prev');});
  document.querySelectorAll('.slide-dot').forEach((d,i)=>d.classList.toggle('active',i===n));
  currentSlide=n;
  if(n===6&&graphState)setTimeout(()=>resizeGraph(),200);
}

function I(){return graphData.items||[];}
function Rels(){return graphData.relations_summary||[];}
function P(){return graphData.papers||[];}

// ════════════════ Slide 0: Title ════════════════
function r0(){
  const items=I(),s=graphData.statistics||{};
  document.getElementById('title-stats').innerHTML=[
    {n:'26',l:'篇论文'},{n:items.length,l:'知识条目'},
    {n:s.total_relations||5162,l:'条关系'},{n:'2',l:'大模块'}
  ].map(x=>`<div class="title-stat"><div class="number">${x.n}</div><div class="label">${x.l}</div></div>`).join('');
}

// ════════════════ Slide 1: 项目缘起 ════════════════
function r1(){
  const area=document.getElementById('vision-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#vision-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Central hub: AI Knowledge Agent
  const cx=W/2,cy=H/2;
  // Hub
  svg.append('circle').attr('cx',cx).attr('cy',cy).attr('r',0).attr('fill','#2563eb').attr('opacity',0.12)
    .transition().duration(800).attr('r',60);
  svg.append('text').attr('x',cx).attr('y',cy-6).attr('text-anchor','middle').attr('fill','#2563eb').attr('font-size','14px').attr('font-weight','700')
    .attr('opacity',0).text('AI 知识').transition().duration(500).delay(400).attr('opacity',1);
  svg.append('text').attr('x',cx).attr('y',cy+14).attr('text-anchor','middle').attr('fill','#2563eb').attr('font-size','14px').attr('font-weight','700')
    .attr('opacity',0).text('管理智能体').transition().duration(500).delay(500).attr('opacity',1);

  // Satellite nodes
  const sats=[
    {a:-Math.PI/2,r:130,l:'论文',c:'#1e40af'},
    {a:0,r:130,l:'企业文档',c:'#1e40af'},
    {a:Math.PI/2,r:130,l:'菜谱',c:'#1e40af'},
    {a:Math.PI,r:130,l:'法律文书',c:'#1e40af'},
  ];
  sats.forEach((s,i)=>{
    const sx=cx+s.r*Math.cos(s.a),sy=cy+s.r*Math.sin(s.a);
    // Connection
    svg.append('line').attr('x1',cx).attr('y1',cy).attr('x2',sx).attr('y2',sy)
      .attr('stroke','#dde1e6').attr('stroke-width',1.5).attr('stroke-dasharray','6,3');
    // Node
    const ng=svg.append('g');
    ng.append('circle').attr('cx',sx).attr('cy',sy).attr('r',0).attr('fill',s.c).attr('opacity',0.15)
      .transition().duration(500).delay(600+i*150).attr('r',32);
    ng.append('circle').attr('cx',sx).attr('cy',sy).attr('r',0).attr('fill','none').attr('stroke',s.c).attr('stroke-width',2)
      .transition().duration(400).delay(700+i*150).attr('r',32);
    ng.append('text').attr('x',sx).attr('y',sy-3).attr('text-anchor','middle').attr('font-size','16px')
      .attr('opacity',0).transition().duration(400).delay(800+i*150).attr('opacity',1);
    ng.append('text').attr('x',sx).attr('y',sy+16).attr('text-anchor','middle').attr('fill','#333840').attr('font-size','10px').attr('font-weight','600')
      .attr('opacity',0).text(s.l).transition().duration(400).delay(850+i*150).attr('opacity',1);
  });

  // Bottom note
  svg.append('text').attr('x',cx).attr('y',H-18).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','10px')
    .text('构建一次知识图谱 → 持续对话问答 → 适用于任何结构化知识');
}

// ════════════════ Slide 2: 两大模块总览 ════════════════
function r2(){
  const area=document.getElementById('overview-dual');area.innerHTML='';
  const W=area.clientWidth||1000,H=area.clientHeight||400;
  const svg=d3.select('#overview-dual').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Two big panels
  const panels=[
    {x:60,w:W/2-90,title:'Part 1: 知识图谱提取',sub:'从论文到结构化知识网络',color:'#2563eb',
     items:['26 篇论文自动解析','315 个定理/引理/推论提取','5,162 条关系自动发现','D3.js 交互式可视化']},
    {x:W/2+30,w:W/2-90,title:'Part 2: 论文问答智能体',sub:'上传论文 → 知识问答',color:'#7c3aed',
     items:['用户上传论文自动扫描','知识图谱实时构建','自然语言问答 + 图谱联动','AI 自动合并等价定义']},
  ];

  panels.forEach((p,i)=>{
    const g=svg.append('g');
    // Panel bg
    g.append('rect').attr('x',p.x).attr('y',30).attr('width',p.w).attr('height',H-60).attr('rx',12)
      .attr('fill','#fafbfc').attr('stroke',p.color).attr('stroke-width',2).attr('opacity',0);
    // Title
    g.append('text').attr('x',p.x+p.w/2).attr('y',70).attr('text-anchor','middle')
      .attr('fill',p.color).attr('font-size','18px').attr('font-weight','700').text(p.title);
    g.append('text').attr('x',p.x+p.w/2).attr('y',95).attr('text-anchor','middle')
      .attr('fill','#8893a0').attr('font-size','12px').text(p.sub);
    // Separator
    g.append('line').attr('x1',p.x+30).attr('y1',110).attr('x2',p.x+p.w-30).attr('y2',110)
      .attr('stroke','#dde1e6').attr('stroke-width',1);
    // Items
    p.items.forEach((t,j)=>{
      g.append('circle').attr('cx',p.x+40).attr('cy',140+j*45).attr('r',5).attr('fill',p.color);
      g.append('text').attr('x',p.x+55).attr('y',140+j*45).attr('dy','0.35em')
        .attr('fill','#333840').attr('font-size','13px').text(t);
    });

    g.select('rect').transition().duration(600).delay(i*300).attr('opacity',1);
  });

  // Arrow between
  const arrow=svg.append('g');
  arrow.append('line').attr('x1',W/2-20).attr('y1',H/2).attr('x2',W/2+20).attr('y2',H/2)
    .attr('stroke','#8893a0').attr('stroke-width',2).attr('marker-end','url(#arr2)');
  svg.append('defs').append('marker').attr('id','arr2').attr('viewBox','0 0 10 10').attr('refX',8).attr('refY',5)
    .attr('markerWidth',6).attr('markerHeight',6).attr('orient','auto')
    .append('path').attr('d','M 0 0 L 10 5 L 0 10 z').attr('fill','#8893a0');
}

// ════════════════ Slide 3: AI Workflow ════════════════
function r3(){
  const area=document.getElementById('ai-workflow');area.innerHTML='';
  const W=area.clientWidth||1000,H=area.clientHeight||400;
  const svg=d3.select('#ai-workflow').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  const cols=[
    {x:70,l:'我们',items:[{t:'设计 Prompt',y:90},{t:'设计架构',y:160},{t:'编写正则',y:230},{t:'审查调试',y:300}],c:'#1e40af'},
    {x:W/2-50,l:'AI',items:[{t:'生成管道代码',y:90},{t:'提取定理信息',y:160},{t:'分类关键词',y:230},{t:'写中文摘要',y:300}],c:'#2563eb'},
    {x:W-170,l:'产出',items:[{t:'Python 管道',y:90},{t:'315条结构化数据',y:160},{t:'关键词+领域标签',y:230},{t:'可读的中文解释',y:300}],c:'#1e40af'},
  ];

  cols.forEach(col=>{
    svg.append('text').attr('x',col.x).attr('y',40).attr('fill','#333840').attr('font-size','13px').attr('font-weight','600').text(col.l);
    col.items.forEach((it,i)=>{
      const g=svg.append('g');
      g.append('rect').attr('x',col.x-8).attr('y',it.y-10).attr('width',145).attr('height',38).attr('rx',6)
        .attr('fill','#fafbfc').attr('stroke',col.c).attr('stroke-width',1.5).attr('opacity',0);
      g.append('text').attr('x',col.x+65).attr('y',it.y+12).attr('text-anchor','middle').attr('fill','#333840').attr('font-size','12px').text(it.t);
      g.select('rect').transition().duration(500).delay(i*100).attr('opacity',1);
    });
  });

  // Arrows
  [{x1:215,y1:110,x2:W/2-65,y2:110},{x1:215,y1:180,x2:W/2-65,y2:180},{x1:215,y1:250,x2:W/2-65,y2:250},{x1:215,y1:320,x2:W/2-65,y2:320}].forEach(a=>{
    svg.append('line').attr('x1',a.x1).attr('y1',a.y1).attr('x2',a.x2).attr('y2',a.y2).attr('stroke','#dde1e6').attr('stroke-width',1.5).attr('stroke-dasharray','5,3');
  });
  [{x1:W/2+95,y1:110,x2:W-185,y2:110},{x1:W/2+95,y1:180,x2:W-185,y2:180},{x1:W/2+95,y1:250,x2:W-185,y2:250},{x1:W/2+95,y1:320,x2:W-185,y2:320}].forEach(a=>{
    svg.append('line').attr('x1',a.x1).attr('y1',a.y1).attr('x2',a.x2).attr('y2',a.y2).attr('stroke','#dde1e6').attr('stroke-width',1.5).attr('stroke-dasharray','5,3');
  });

  svg.append('text').attr('x',W/2).attr('y',H-15).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','10px').text('人负责决策和架构 · AI 负责执行和生成 · 双方互相迭代');
}

// ════════════════ Slide 4: Prompt Engineering ════════════════
function r4(){
  const area=document.getElementById('prompt-demo');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#prompt-demo').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Code editor mock
  svg.append('rect').attr('x',15).attr('y',15).attr('width',W-30).attr('height',H-30).attr('rx',8)
    .attr('fill','#f8f9fb').attr('stroke','#dde1e6').attr('stroke-width',1);
  svg.append('rect').attr('x',15).attr('y',15).attr('width',W-30).attr('height',22).attr('rx',8)
    .attr('fill','#eef2ff');
  svg.append('circle').attr('cx',30).attr('cy',26).attr('r',4).attr('fill','#dc2626');
  svg.append('circle').attr('cx',42).attr('cy',26).attr('r',4).attr('fill','#ea580c');
  svg.append('circle').attr('cx',54).attr('cy',26).attr('r',4).attr('fill','#059669');
  svg.append('text').attr('x',W/2).attr('y',28).attr('text-anchor','middle').attr('fill','#667080').attr('font-size','9px').text('prompts/classify.txt');

  const lines=[
    {t:'你是一位数学分类专家。',c:'#333840'},
    {t:'为给定的数学定理分配',c:'#333840'},
    {t:'关键词和领域标签。',c:'#333840'},
    {t:'',c:'#8893a0'},
    {t:'输出JSON格式:',c:'#b45309'},
    {t:'{',c:'#667080'},
    {t:'  "keywords": [...],',c:'#667080'},
    {t:'  "domain": [...],',c:'#667080'},
    {t:'  "confidence": 0.9',c:'#667080'},
    {t:'}',c:'#667080'},
    {t:'',c:'#8893a0'},
    {t:'领域标签(30+个可选):',c:'#333840'},
    {t:'proximal_point, gradient_',c:'#5a6070'},
    {t:'method, accelerated_method...',c:'#5a6070'},
    {t:'',c:'#8893a0'},
    {t:'→ AI 返回结构化结果 ✅',c:'#059669'},
  ];
  lines.forEach((l,i)=>{
    if(!l.t)return;
    svg.append('text').attr('x',28).attr('y',56+i*17).attr('fill',l.c).attr('font-size','11px')
      .attr('font-family',"'Cascadia Code',Consolas,monospace").attr('opacity',0)
      .text(l.t).transition().duration(300).delay(300+i*30).attr('opacity',1);
  });
}

// ════════════════ Slide 5: Pipeline + Results ════════════════
function r5(){
  // Mini pipeline
  const area=document.getElementById('pipeline-mini');area.innerHTML='';
  const pW=area.clientWidth||1000,pH=120;
  const pSvg=d3.select('#pipeline-mini').append('svg').attr('viewBox',`0 0 ${pW} ${pH}`);
  const stages=[
    {l:'① 解析',c:'#dc2626'},{l:'② 关键词',c:'#ea580c'},
    {l:'③ AI 增强',c:'#7c3aed',ai:true},{l:'④ 去重',c:'#2563eb'},
    {l:'⑤ 关系',c:'#2563eb'},{l:'⑥ 可视化',c:'#059669'},
  ];
  const startX=(pW-(stages.length*130+(stages.length-1)*20))/2;
  stages.forEach((s,i)=>{
    const x=startX+i*150;
    const g=pSvg.append('g');
    if(s.ai){
      g.append('rect').attr('x',x+30).attr('y',8).attr('width',24).attr('height',12).attr('rx',6)
        .attr('fill','#7c3aed').attr('opacity',0);
      g.append('text').attr('x',x+42).attr('y',16).attr('text-anchor','middle').attr('fill','#fff').attr('font-size','7px').attr('font-weight','700').text('AI');
      g.select('rect').transition().duration(400).delay(200).attr('opacity',1);
    }
    g.append('rect').attr('x',x).attr('y',30).attr('width',110).attr('height',50).attr('rx',8)
      .attr('fill','#fafbfc').attr('stroke',s.c).attr('stroke-width',2).attr('opacity',0);
    g.append('text').attr('x',x+55).attr('y',60).attr('text-anchor','middle').attr('fill',s.c).attr('font-size','13px').attr('font-weight','700').text(s.l);
    g.select('rect').transition().duration(500).delay(i*120).attr('opacity',1);
    if(i<stages.length-1){
      pSvg.append('line').attr('x1',x+110).attr('y1',55).attr('x2',x+150).attr('y2',55)
        .attr('stroke','#dde1e6').attr('stroke-width',2);
      pSvg.append('polygon').attr('points',`${x+147},51 ${x+155},55 ${x+147},59`).attr('fill','#8893a0');
    }
  });
  pSvg.append('text').attr('x',pW/2).attr('y',pH-8).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','9px').text('~8 秒 · Python 标准库 + Claude API · 零外部依赖');

  // Stats
  const items=I(),rels=Rels(),papers=P();
  document.getElementById('results-stats').innerHTML=[
    {n:papers.length,l:'篇论文',c:'#b45309'},{n:items.length,l:'知识条目',c:'#2563eb'},
    {n:rels.length,l:'条关系',c:'#059669'},{n:'~8s',l:'构建耗时',c:'#7c3aed'}
  ].map(s=>`<div class="result-card"><div class="num" style="color:${s.c}">${s.n}</div><div class="lbl">${s.l}</div></div>`).join('');

  // Type bar
  const tc={};items.forEach(it=>{tc[it.type]=(tc[it.type]||0)+1;});
  const a1=document.getElementById('type-bar-chart');a1.innerHTML='';
  const W1=a1.clientWidth||500,H1=a1.clientHeight||300;
  const m1={top:30,right:20,bottom:40,left:70},iw1=W1-m1.left-m1.right,ih1=H1-m1.top-m1.bottom;
  const types=Object.keys(CM).filter(t=>tc[t]);
  const svg1=d3.select('#type-bar-chart').append('svg').attr('viewBox',`0 0 ${W1} ${H1}`);
  const g1=svg1.append('g').attr('transform',`translate(${m1.left},${m1.top})`);
  const x1=d3.scaleLinear().domain([0,d3.max(types,t=>tc[t])+5]).range([0,iw1]);
  const y1=d3.scaleBand().domain(types).range([0,ih1]).padding(0.4);
  g1.append('text').attr('class','chart-title-text').attr('x',iw1/2).attr('y',-10).attr('text-anchor','middle').text('知识条目类型分布');
  g1.append('g').call(d3.axisLeft(y1).tickFormat(t=>TCN[t]||t)).selectAll('text').attr('fill','#5a6070').attr('font-size','11px');
  g1.selectAll('.domain,.tick line').attr('stroke','#dde1e6');
  g1.append('g').attr('transform',`translate(0,${ih1})`).call(d3.axisBottom(x1).ticks(5).tickFormat(d3.format('d'))).selectAll('text').attr('fill','#8893a0').attr('font-size','9px');
  g1.selectAll('.domain,.tick line').attr('stroke','#dde1e6');
  g1.selectAll('rect').data(types).join('rect').attr('y',d=>y1(d)).attr('height',y1.bandwidth()).attr('x',0).attr('width',0)
    .attr('fill',d=>CM[d]).attr('rx',3).transition().duration(600).delay((d,i)=>i*80).attr('width',d=>x1(tc[d]));
  g1.selectAll('.vl').data(types).join('text').attr('x',d=>x1(tc[d])+5).attr('y',d=>y1(d)+y1.bandwidth()/2)
    .attr('dy','0.35em').attr('fill','#333840').attr('font-size','11px').attr('font-weight','600').text(d=>tc[d]);

  // Keyword top
  const kw={};items.forEach(it=>{(it.keywords||[]).forEach(k=>{kw[k]=(kw[k]||0)+1;});});
  const kwS=Object.entries(kw).filter(([k])=>!['theorem','lemma','corollary','definition','proposition'].includes(k)).sort((a,b)=>b[1]-a[1]).slice(0,10);
  const a2=document.getElementById('kw-top-chart');a2.innerHTML='';
  const W2=a2.clientWidth||500,H2=a2.clientHeight||300;
  const m2={top:30,right:20,bottom:10,left:90},iw2=W2-m2.left-m2.right,ih2=H2-m2.top-m2.bottom;
  const svg2=d3.select('#kw-top-chart').append('svg').attr('viewBox',`0 0 ${W2} ${H2}`);
  const g2=svg2.append('g').attr('transform',`translate(${m2.left},${m2.top})`);
  const maxK=d3.max(kwS,d=>d[1]);
  g2.append('text').attr('class','chart-title-text').attr('x',iw2/2).attr('y',-10).attr('text-anchor','middle').text('Top 10 高频关键词');
  const bh=Math.min(18,ih2/kwS.length-4);
  kwS.forEach(([k,v],i)=>{
    const y=i*(ih2/kwS.length);
    g2.append('text').attr('x',-6).attr('y',y+bh/2).attr('dy','0.35em').attr('text-anchor','end').attr('fill','#5a6070').attr('font-size','9px').text(k.replace(/_/g,' '));
    g2.append('rect').attr('x',0).attr('y',y+1).attr('height',bh-2).attr('rx',2).attr('fill',d3.interpolateBlues(v/maxK*0.7+0.3)).attr('width',0)
      .transition().duration(500).delay(i*35).attr('width',(v/maxK)*iw2*0.9);
    g2.append('text').attr('x',(v/maxK)*iw2*0.9+5).attr('y',y+bh/2).attr('dy','0.35em').attr('fill','#8893a0').attr('font-size','8px').text(v);
  });
}

// ════════════════ Slide 6: Interactive Graph ════════════════
let graphState=null;
function r6(){renderGraph();}
function renderGraph(){
  const container=document.getElementById('graph-canvas');
  const W=container.clientWidth,H=container.clientHeight;
  const items=I(),relations=Rels();
  if(!items.length)return;

  const nodes=items.map((it,idx)=>({
    id:it.id,type:it.type,name:it.name,
    keywords:(it.keywords||[]).slice(0,5),
    sources:it.sources||[it.id.split('_')[0]],
    papers:it.sources||[it.id.split('_')[0]],
    x:it.x||(400+Math.random()*800),y:it.y||(300+Math.random()*600),_i:idx
  }));
  const idMap={};nodes.forEach(n=>idMap[n.id]=n._i);
  const linkData=[];
  relations.forEach(r=>{const si=idMap[r.source_id],ti=idMap[r.target_id];if(si!==undefined&&ti!==undefined)linkData.push({source:si,target:ti,type:r.type,note:(r.note||'').slice(0,80)});});

  const spLinks=[],pg={};
  nodes.forEach((n,i)=>{(n.papers||[]).forEach(pid=>{pg[pid]=pg[pid]||[];pg[pid].push(i);});});
  Object.values(pg).forEach(ix=>{for(let a=0;a<ix.length;a++)for(let b=a+1;b<Math.min(a+5,ix.length);b++)spLinks.push({source:ix[a],target:ix[b]});});

  const detailMap={};
  items.forEach((it,idx)=>{
    const d={};if(it.summary)d.sm=it.summary;if(it.statement&&it.statement.length>20)d.st=it.statement.slice(0,400);if(it.latex)d.fm=[it.latex.slice(0,500)];if(Object.keys(d).length)detailMap[String(idx)]=d;
  });

  const svg=d3.select('#graph-canvas svg');svg.selectAll('*').remove();
  const zoom=d3.zoom().scaleExtent([0.08,5.5]).on('zoom',e=>{g.attr('transform',e.transform);updVis(e.transform);});
  svg.call(zoom);
  const g=svg.append('g');
  const splG=g.append('g');
  splG.selectAll('line').data(spLinks).join('line').attr('class','link-sp').attr('stroke','#cbd5e1').attr('stroke-width',0.6).attr('stroke-dasharray','2,6').attr('stroke-opacity',0.3);
  const linkG=g.append('g');
  const linkSel=linkG.selectAll('line').data(linkData).join('line').attr('class','link')
    .attr('stroke',d=>RCM[d.type]||'#6b7280').attr('stroke-width',d=>d.type==='derives'?2.2:d.type==='generalizes'?1.6:1.1)
    .attr('stroke-dasharray',d=>d.type==='depends'?'5,3':d.type==='equivalent'?'6,3':d.type==='generalizes'?'8,2':'none');
  const nodeG=g.append('g');
  const nodeSel=nodeG.selectAll('g').data(nodes).join('g').attr('class','node').attr('transform',d=>`translate(${d.x},${d.y})`)
    .call(d3.drag().on('drag',function(e,d){d.x=e.x;d.y=e.y;d3.select(this).attr('transform',`translate(${d.x},${d.y})`);updLinks();}));
  nodeSel.append('circle').attr('r',d=>(SZ[d.type]||10)+Math.min((d.sources||[]).length*2,6)).attr('fill',d=>CM[d.type]||'#666').attr('stroke',d=>d3.color(CM[d.type]||'#666').darker(0.6));
  nodeSel.append('text').text(d=>{const n=d.name||d.id;return n.length>10?n.slice(0,9)+'…':n;}).attr('y',d=>-(SZ[d.type]||10)-6).attr('opacity',0);

  nodeSel.on('mouseover',function(e,d){
    const r=(SZ[d.type]||10)+Math.min((d.sources||[]).length*2,6);
    d3.select(this).select('circle').transition().duration(120).attr('r',r+3);
    const conn=new Set();linkData.forEach(l=>{if(l.source===d._i)conn.add(l.target);if(l.target===d._i)conn.add(l.source);});
    nodeSel.selectAll('circle').attr('opacity',n=>n._i===d._i||conn.has(n._i)?1:0.15);
    linkSel.attr('opacity',l=>l.source===d._i||l.target===d._i?0.9:0.04);
    d3.select('#tooltip').html(`<div style="color:#1a1e26;font-weight:600">${d.name}</div><div style="font-size:9px;color:#8893a0">${TCN[d.type]} · ${d.sources.length} 来源</div>`).style('left',(e.pageX+12)+'px').style('top',(e.pageY-12)+'px').style('opacity',1);
  }).on('mouseout',function(e,d){
    d3.select(this).select('circle').transition().duration(120).attr('r',(SZ[d.type]||10)+Math.min((d.sources||[]).length*2,6));
    nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.25);d3.select('#tooltip').style('opacity',0);
  }).on('click',(e,d)=>{
    const dt=detailMap[String(d._i)]||{};
    let h=`<div style="color:#1a1e26;font-weight:600;font-size:11px">${d.name}</div><div style="font-size:9px;color:#8893a0;margin-top:2px">${TCN[d.type]} · ${d.sources.length} 来源</div>`;
    if(dt.sm)h+=`<div style="font-size:9px;color:#1e40af;margin-top:3px;max-width:240px;line-height:1.4">${dt.sm}</div>`;
    if(dt.fm)h+=`<div style="font-size:10px;color:#b45309;margin-top:3px;font-family:monospace;max-width:240px;overflow:hidden">${dt.fm[0].slice(0,200)}</div>`;
    d3.select('#tooltip').html(h).style('left',(e.pageX+12)+'px').style('top',(e.pageY-12)+'px').style('opacity',1);
    setTimeout(()=>d3.select('#tooltip').style('opacity',0),4000);
  });

  function updLinks(){linkSel.attr('x1',d=>nodes[d.source].x).attr('y1',d=>nodes[d.source].y).attr('x2',d=>nodes[d.target].x).attr('y2',d=>nodes[d.target].y);splG.selectAll('line').attr('x1',d=>nodes[d.source].x).attr('y1',d=>nodes[d.source].y).attr('x2',d=>nodes[d.target].x).attr('y2',d=>nodes[d.target].y);}
  updLinks();

  function updVis(t){
    if(!t)t=d3.zoomTransform(svg.node());
    const s=t.k,vx=-t.x/s,vy=-t.y/s,vw=W/s,vh=H/s,pad=50,lo=s<0.35;
    nodeSel.each(function(d){const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;d3.select(this).style('display',inV?null:'none');});
    nodeSel.selectAll('text').attr('opacity',function(d){const inV=d.x>vx-pad&&d.x<vx+vw+pad&&d.y>vy-pad&&d.y<vy+vh+pad;return(inV&&s>1.2)?1:0;});
    nodeSel.selectAll('circle').attr('r',function(d){const base=SZ[d.type]||10;if(lo)return 3;if(s<0.75)return base*0.7;if(s>1.8)return base+Math.min((d.sources||[]).length*2,8);return base;});
    linkSel.style('display',d=>{if(lo)return'none';const ns=nodes[d.source],nt=nodes[d.target];return(ns.x>vx-pad&&ns.x<vx+vw+pad||nt.x>vx-pad&&nt.x<vx+vw+pad)?null:'none';});
  }

  graphState={svg,zoom,updVis};

  document.getElementById('graph-legend').innerHTML=Object.entries(CM).map(([t,c])=>`<div class="gl-item"><span class="gl-dot" style="background:${c}"></span>${TCN[t]}</div>`).join('')
    +'<span style="margin:0 4px;color:#8893a0">|</span>'+Object.entries(RCN).slice(0,4).map(([t,l])=>`<div class="gl-item"><span class="gl-line solid" style="border-color:${RCM[t]}"></span>${l}</div>`).join('');

  document.getElementById('graph-search-input').addEventListener('input',function(){
    const q=this.value.toLowerCase();if(!graphState)return;
    if(!q){nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.25);return;}
    const m=new Set();nodes.forEach(n=>{if((n.name+' '+(n.keywords||[]).join(' ')).toLowerCase().includes(q))m.add(n._i);});
    nodeSel.selectAll('circle').attr('opacity',n=>m.has(n._i)?1:0.06);linkSel.attr('opacity',l=>m.has(l.source)&&m.has(l.target)?1:0.02);
  });
  document.getElementById('zin').onclick=()=>svg.transition().duration(200).call(zoom.scaleBy,1.3);
  document.getElementById('zout').onclick=()=>svg.transition().duration(200).call(zoom.scaleBy,0.7);
  document.getElementById('zfit').onclick=()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity);
  setTimeout(()=>graphState&&graphState.updVis(),200);
}
function resizeGraph(){if(graphState){graphState.svg.selectAll('*').remove();renderGraph();}}

// ════════════════ Slide 7: Q&A Interface Intro ════════════════
function r7(){
  const area=document.getElementById('qa-demo');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#qa-demo').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Mock UI: left chat panel, right graph panel
  // Left: chat mock
  svg.append('rect').attr('x',20).attr('y',20).attr('width',W/2-30).attr('height',H-40).attr('rx',8)
    .attr('fill','#fafbfc').attr('stroke','#dde1e6').attr('stroke-width',1);
  svg.append('rect').attr('x',20).attr('y',20).attr('width',W/2-30).attr('height',28).attr('rx',8)
    .attr('fill','#eef2ff');
  svg.append('text').attr('x',W/4+5).attr('y',38).attr('text-anchor','middle').attr('fill','#333840').attr('font-size','10px').attr('font-weight','600').text('对话面板');

  // Chat bubbles
  [{y:70,t:'微积分基本定理是什么？',role:'user',c:'#dbeafe'},{y:120,t:'根据知识图谱，微积分第一基本定理指出...',role:'bot',c:'#f0fdf4'}].forEach(b=>{
    const bx=b.role==='user'?W/2-120:30;
    svg.append('rect').attr('x',bx).attr('y',b.y).attr('width',W/2-70).attr('height',30).attr('rx',6)
      .attr('fill',b.c).attr('stroke','#dde1e6').attr('stroke-width',0.5);
    svg.append('text').attr('x',bx+8).attr('y',b.y+20).attr('fill','#333840').attr('font-size','9px').text(b.t.slice(0,28)+'…');
  });

  // Input
  svg.append('rect').attr('x',20).attr('y',H-55).attr('width',W/2-60).attr('height',26).attr('rx',5)
    .attr('fill','#fff').attr('stroke','#dde1e6');
  svg.append('text').attr('x',30).attr('y',H-40).attr('fill','#8893a0').attr('font-size','9px').text('输入问题...');
  svg.append('rect').attr('x',W/2-38).attr('y',H-55).attr('width',30).attr('height',26).attr('rx',5).attr('fill','#2563eb');
  svg.append('text').attr('x',W/2-23).attr('y',H-40).attr('text-anchor','middle').attr('fill','#fff').attr('font-size','8px').text('发送');

  // Right: graph mock
  svg.append('rect').attr('x',W/2+10).attr('y',20).attr('width',W/2-30).attr('height',H-40).attr('rx',8)
    .attr('fill','#fafbfc').attr('stroke','#dde1e6').attr('stroke-width',1);
  svg.append('rect').attr('x',W/2+10).attr('y',20).attr('width',W/2-30).attr('height',28).attr('rx',8)
    .attr('fill','#fef3c7');
  svg.append('text').attr('x',W*3/4-5).attr('y',38).attr('text-anchor','middle').attr('fill','#333840').attr('font-size','10px').attr('font-weight','600').text('知识图谱联动');

  // Mock nodes in graph
  const gx=W*3/4-5,gy=H/2+10;
  [{dx:0,dy:-30,c:'#7c3aed'},{dx:25,dy:15,c:'#2563eb'},{dx:-25,dy:15,c:'#dc2626'},{dx:0,dy:50,c:'#059669'}].forEach(n=>{
    svg.append('circle').attr('cx',gx+n.dx).attr('cy',gy+n.dy).attr('r',14).attr('fill',n.c).attr('opacity',0.7);
    // Highlight ring on one node
    if(n.dx===0&&n.dy===-30){
      svg.append('circle').attr('cx',gx+n.dx).attr('cy',gy+n.dy).attr('r',20).attr('fill','none').attr('stroke','#f59e0b').attr('stroke-width',2.5).attr('stroke-dasharray','3,2');
    }
  });
  // Edges
  [{x1:gx,y1:gy-30,x2:gx+25,y2:gy+15},{x1:gx,y1:gy-30,x2:gx-25,y2:gy+15},{x1:gx,y1:gy-30,x2:gx,y2:gy+50}].forEach(e=>{
    svg.append('line').attr('x1',e.x1).attr('y1',e.y1).attr('x2',e.x2).attr('y2',e.y2).attr('stroke','#cbd5e1').attr('stroke-width',1);
  });

  // Labels
  svg.append('text').attr('x',W/2+10).attr('y',H-16).attr('fill','#8893a0').attr('font-size','8px').text('图谱自动高亮关联节点');
}

// ════════════════ Slide 8: Q&A Flow ════════════════
function r8(){
  const area=document.getElementById('qa-flow');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#qa-flow').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  const steps=[
    {y:50,t:'用户输入问题',s:'"微积分基本定理是什么？"',c:'#dc2626'},
    {y:130,t:'关键词提取',s:'微积分、基本定理',c:'#ea580c'},
    {y:210,t:'图谱检索',s:'匹配相关定理节点 + 邻居',c:'#2563eb'},
    {y:290,t:'LLM 推理生成',s:'注入 Context → 综合推理 → 回答',c:'#7c3aed'},
  ];

  steps.forEach((s,i)=>{
    const g=svg.append('g');
    // Node
    g.append('circle').attr('cx',60).attr('cy',s.y+12).attr('r',18).attr('fill',s.c).attr('opacity',0.15);
    g.append('circle').attr('cx',60).attr('cy',s.y+12).attr('r',18).attr('fill','none').attr('stroke',s.c).attr('stroke-width',2);
    g.append('text').attr('x',60).attr('y',s.y+16).attr('text-anchor','middle').attr('fill','#fff').attr('font-size','14px').attr('font-weight','700').text(i+1);
    // Label
    g.append('text').attr('x',95).attr('y',s.y+6).attr('fill','#1a1e26').attr('font-size','13px').attr('font-weight','600').text(s.t);
    g.append('text').attr('x',95).attr('y',s.y+24).attr('fill','#8893a0').attr('font-size','10px').text(s.s);
    // Arrow
    if(i<steps.length-1){
      svg.append('line').attr('x1',60).attr('y1',s.y+30).attr('x2',60).attr('y2',steps[i+1].y-6)
        .attr('stroke','#dde1e6').attr('stroke-width',2);
      svg.append('polygon').attr('points',`56,${steps[i+1].y-12} 60,${steps[i+1].y-6} 64,${steps[i+1].y-12}`).attr('fill','#8893a0');
    }
  });

  // Right side: RAG comparison
  svg.append('text').attr('x',W-30).attr('y',H-40).attr('text-anchor','end').attr('fill','#8893a0').attr('font-size','10px')
    .text('图谱检索 > 向量搜索：结构化的层级关系更精准');
}

// ════════════════ Slide 9: Applications ════════════════
function r9(){
  const area=document.getElementById('applications-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#applications-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  const apps=[
    {y:40,i:'',t:'企业培训',s:'上传公司手册，新员工直接提问',c:'#1e40af'},
    {y:140,i:'',t:'智能菜谱',s:'导入菜谱 PDF，食材知识网络查询',c:'#1e40af'},
    {y:240,i:'',t:'法律检索',s:'上传法规文档，自然语言法律咨询',c:'#1e40af'},
    {y:340,i:'',t:'课程体系',s:'导入课件教材，构建学科知识图谱',c:'#1e40af'},
  ];

  apps.forEach((a)=>{
    const g=svg.append('g');
    g.append('rect').attr('x',20).attr('y',a.y).attr('width',W-40).attr('height',80).attr('rx',10)
      .attr('fill','#fafbfc').attr('stroke',a.c).attr('stroke-width',1.5).attr('opacity',0);
    g.append('text').attr('x',55).attr('y',a.y+30).attr('font-size','22px').text(a.i);
    g.append('text').attr('x',90).attr('y',a.y+24).attr('fill','#1a1e26').attr('font-size','14px').attr('font-weight','600').text(a.t);
    g.append('text').attr('x',90).attr('y',a.y+48).attr('fill','#5a6070').attr('font-size','10px').text(a.s.split('\n').join(' · '));
    // Arrow showing "same architecture"
    g.append('text').attr('x',W-40).attr('y',a.y+44).attr('text-anchor','end').attr('fill',a.c).attr('font-size','10px').attr('font-weight','600').text('同一架构');
    g.select('rect').transition().duration(500).delay(100).attr('opacity',1);
  });

  // Bottom note
  svg.append('text').attr('x',W/2).attr('y',H-10).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','10px')
    .text('核心不变：知识提取 → 图谱构建 → 自然语言问答。换数据 = 换领域');
}

// ════════════════ Slide 10: Takeaways ════════════════
function r10(){
  const area=document.getElementById('summary-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#summary-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  const items=[
    {y:55,i:'',t:'Prompt 是一种新的编程范式',s:'像编写代码一样迭代优化 Prompt'},
    {y:140,i:'',t:'传统算法与 AI 模型互补',s:'正则负责提取，AI 负责理解'},
    {y:225,i:'',t:'知识图谱 + LLM 优于纯 RAG',s:'结构化检索比向量搜索更精准'},
    {y:310,i:'',t:'方法论通用，场景广泛',s:'数学、企业、菜谱、法律——同一架构'},
  ];
  items.forEach((x,i)=>{
    const g=svg.append('g');
    g.append('circle').attr('cx',45).attr('cy',x.y+14).attr('r',20).attr('fill','#eef2ff').attr('stroke','#2563eb').attr('stroke-width',2);
    g.append('text').attr('x',45).attr('y',x.y+18).attr('text-anchor','middle').attr('font-size','16px').text(x.i);
    g.append('text').attr('x',78).attr('y',x.y+8).attr('fill','#1a1e26').attr('font-size','14px').attr('font-weight','600').text(x.t);
    g.append('text').attr('x',78).attr('y',x.y+28).attr('fill','#5a6070').attr('font-size','10px').text(x.s);
    if(i<items.length-1){
      svg.append('line').attr('x1',45).attr('y1',x.y+34).attr('x2',45).attr('y2',items[i+1].y-6)
        .attr('stroke','#dde1e6').attr('stroke-width',2).attr('stroke-dasharray','4,4');
    }
  });
}

// ════════════════ Slide 11: Thanks ════════════════
function r11(){
  const items=I(),rels=Rels(),papers=P();
  document.getElementById('thank-stats').innerHTML=[
    {n:papers.length,l:'篇论文',c:'#b45309'},{n:items.length,l:'知识条目',c:'#2563eb'},
    {n:rels.length,l:'条关系',c:'#059669'},{n:'4',l:'个 Prompt',c:'#7c3aed'}
  ].map(s=>`<div class="summary-card"><div class="num" style="color:${s.c}">${s.n}</div><div class="lbl">${s.l}</div></div>`).join('');
}

document.addEventListener('DOMContentLoaded',init);
window.addEventListener('resize',()=>{if(currentSlide===6&&graphState){clearTimeout(window._rt);window._rt=setTimeout(()=>resizeGraph(),300);}});
