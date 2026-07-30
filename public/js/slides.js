/**
 * AI 暑期学校 — 知识图谱幻灯片引擎
 * 11 页 · 中文 · 聚焦 AI 辅助开发
 */

// ════════════════ Constants ════════════════
const CM={theorem:'#e05560',lemma:'#4da6d9',corollary:'#43b884',definition:'#9b6cc4',proposition:'#e8963e'};
const TCN={theorem:'定理',lemma:'引理',corollary:'推论',definition:'定义',proposition:'命题'};
const RCM={derives:'#e05560',generalizes:'#4da6d9',equivalent:'#43b884',depends:'#7a8a9a'};
const RCN={derives:'推导',generalizes:'推广',equivalent:'等价',depends:'依赖'};
const SZ={theorem:14,lemma:12,corollary:10,definition:13,proposition:12};

// ════════════════ State ════════════════
let graphData=null,currentSlide=0;
const TOTAL=11;

// ════════════════ Init ════════════════
async function init(){
  try{
    const r=await fetch('/api/graph');
    if(!r.ok){const e=await r.json();showErr(e.message||'加载失败');return;}
    graphData=await r.json();
  }catch(e){showErr('无法连接服务器。<br>请运行 <code>npm start</code> 并确保已生成数据。');return;}

  // 分批渲染所有幻灯片，每批间隔 50ms 避免阻塞
  const R={0:r0,1:r1,2:r2,3:r3,4:r4,5:r5,6:r6,7:renderGraph,8:r8,9:r9,10:r10};
  let rendered=0;
  for(let i=0;i<TOTAL;i++){
    setTimeout(() => {
      if(R[i]&&graphData){
        try{
          R[i]();
          rendered++;
        }catch(e){
          console.error('Slide '+i+' render error:',e);
        }
      }
      // 全部渲染完成后隐藏 loading
      if(i===TOTAL-1){
        setTimeout(()=>{
          console.log('Rendered '+rendered+'/'+TOTAL+' slides');
          document.getElementById('loading-overlay').classList.add('hidden');
          setupNav();goToSlide(0);
        },200);
      }
    }, i*80);
  }
}
function showErr(m){
  const o=document.getElementById('loading-overlay');
  o.querySelector('.spinner').style.display='none';
  o.querySelector('.msg').textContent='加载失败';
  o.querySelector('.error-msg').innerHTML=m;
}

// ════════════════ Navigation ════════════════
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
  // 图谱页需要 resize（因为 SVG 需要实际尺寸）
  if(n===7&&graphState)setTimeout(()=>resizeGraph(),200);
}
function renderSlide(n){} // 已废弃，所有 slide 在 init 时预渲染

// ════════════════ Helpers ════════════════
function I(){return graphData.items||[];}
function Rels(){return graphData.relations_summary||[];}
function P(){return graphData.papers||[];}

// ════════════════ Slide 0: Title ════════════════
function r0(){
  const items=I(),s=graphData.statistics||{};
  document.getElementById('title-stats').innerHTML=[
    {n:26,l:'篇论文'},{n:items.length,l:'知识条目'},
    {n:s.total_relations||5162,l:'条关系'},{n:'4',l:'个 AI Prompt'}
  ].map(x=>`<div class="title-stat"><div class="number">${x.n}</div><div class="label">${x.l}</div></div>`).join('');
}

// ════════════════ Slide 1: What We Did ════════════════
function r1(){
  const area=document.getElementById('overview-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;

  // Simple process flow: Papers → AI → Code → Graph
  const steps=[
    {x:60,y:80,t:'📄\n26篇论文',c:'#4da6d9'},
    {x:60,y:180,t:'🤖\nAI 分析',c:'#e8963e'},
    {x:60,y:280,t:'⚙️\n代码管道',c:'#43b884'},
    {x:60,y:370,t:'🔗\n知识图谱',c:'#e05560'},
  ];

  const svg=d3.select('#overview-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Arrows between steps
  for(let i=0;i<steps.length-1;i++){
    svg.append('line').attr('x1',steps[i].x+15).attr('y1',steps[i].y+30).attr('x2',steps[i+1].x+15).attr('y2',steps[i+1].y-5)
      .attr('stroke','#dde1e6').attr('stroke-width',2).attr('marker-end','url(#arrow)');
  }

  // Arrow marker
  svg.append('defs').append('marker').attr('id','arrow').attr('viewBox','0 0 10 10').attr('refX',5).attr('refY',5)
    .attr('markerWidth',6).attr('markerHeight',6).attr('orient','auto-start-reverse')
    .append('path').attr('d','M 0 0 L 10 5 L 0 10 z').attr('fill','#3a5060');

  steps.forEach((s,i)=>{
    const bg=svg.append('g');
    bg.append('rect').attr('x',s.x-12).attr('y',s.y-12).attr('width',56).attr('height',56).attr('rx',12)
      .attr('fill','#fafbfc').attr('stroke',s.c).attr('stroke-width',2).attr('opacity',0);
    bg.append('text').attr('x',s.x+15).attr('y',s.y+8).attr('text-anchor','middle')
      .attr('fill','#1a1e26').attr('font-size','11px');
    bg.select('rect').transition().duration(500).delay(i*200).attr('opacity',1);
  });

  // Right side: key numbers appearing
  const nums=[{n:'315',l:'提取的定理/引理',y:120},{n:'5,162',l:'发现的知识关联',y:220},{n:'~8s',l:'全流程耗时',y:320}];
  nums.forEach((x,i)=>{
    svg.append('text').attr('x',W-60).attr('y',x.y).attr('text-anchor','end')
      .attr('fill','#e0e8f0').attr('font-size','28px').attr('font-weight','700').attr('opacity',0)
      .text(x.n).transition().duration(600).delay(600+i*200).attr('opacity',1);
    svg.append('text').attr('x',W-60).attr('y',x.y+22).attr('text-anchor','end')
      .attr('fill','#8893a0').attr('font-size','11px').attr('opacity',0)
      .text(x.l).transition().duration(400).delay(800+i*200).attr('opacity',1);
  });
}

// ════════════════ Slide 2: AI Workflow ════════════════
function r2(){
  const area=document.getElementById('ai-workflow');area.innerHTML='';
  const W=area.clientWidth||1000,H=area.clientHeight||420;
  const svg=d3.select('#ai-workflow').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Three columns: 人, AI, 成果
  const cols=[{x:80,l:'👤 我们做什么',items:[
    {t:'设计 Prompt',c:'#e05560',y:90},{t:'设计架构',c:'#e05560',y:160},{t:'编写正则',c:'#e05560',y:230},{t:'审查 & 调试',c:'#e05560',y:300}
  ]},{x:W/2-60,l:'🤖 AI 做什么',items:[
    {t:'生成管道代码',c:'#4da6d9',y:90},{t:'提取定理信息',c:'#4da6d9',y:160},{t:'分类关键词',c:'#4da6d9',y:230},{t:'写中文摘要',c:'#4da6d9',y:300}
  ]},{x:W-160,l:'📦 产出',items:[
    {t:'Python 管道',c:'#43b884',y:90},{t:'315条结构化数据',c:'#43b884',y:160},{t:'关键词+领域标签',c:'#43b884',y:230},{t:'可读的中文解释',c:'#43b884',y:300}
  ]}];

  cols.forEach(col=>{
    svg.append('text').attr('x',col.x).attr('y',40).attr('text-anchor','start')
      .attr('fill','#5a6070').attr('font-size','13px').attr('font-weight','600').text(col.l);
    col.items.forEach((it,i)=>{
      const g=svg.append('g');
      g.append('rect').attr('x',col.x-8).attr('y',it.y-10).attr('width',150).attr('height',38)
        .attr('rx',6).attr('fill','#fafbfc').attr('stroke',it.c).attr('stroke-width',1.5).attr('opacity',0);
      g.append('text').attr('x',col.x+67).attr('y',it.y+12).attr('text-anchor','middle')
        .attr('fill','#333840').attr('font-size','12px').text(it.t);
      g.select('rect').transition().duration(500).delay(i*120).attr('opacity',1);
    });
  });

  // Connecting arrows
  [{x1:230,y1:110,x2:W/2-68,y2:110},{x1:230,y1:180,x2:W/2-68,y2:180},{x1:230,y1:250,x2:W/2-68,y2:250},{x1:230,y1:320,x2:W/2-68,y2:320}].forEach(a=>{
    svg.append('line').attr('x1',a.x1).attr('y1',a.y1).attr('x2',a.x2).attr('y2',a.y2)
      .attr('stroke','#dde1e6').attr('stroke-width',1.5).attr('stroke-dasharray','5,3');
  });
  [{x1:W/2+82,y1:110,x2:W-168,y2:110},{x1:W/2+82,y1:180,x2:W-168,y2:180},{x1:W/2+82,y1:250,x2:W-168,y2:250},{x1:W/2+82,y1:320,x2:W-168,y2:320}].forEach(a=>{
    svg.append('line').attr('x1',a.x1).attr('y1',a.y1).attr('x2',a.x2).attr('y2',a.y2)
      .attr('stroke','#dde1e6').attr('stroke-width',1.5).attr('stroke-dasharray','5,3');
  });

  // Bottom note
  svg.append('text').attr('x',W/2).attr('y',H-15).attr('text-anchor','middle')
    .attr('fill','#8893a0').attr('font-size','10px').text('人负责决策和架构 · AI 负责执行和生成 · 双方互相迭代');
}

// ════════════════ Slide 3: Prompt Engineering ════════════════
function r3(){
  const area=document.getElementById('prompt-demo');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#prompt-demo').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Show prompt template snippet
  const promptLines=[
    {t:'你是一位数学分类专家。',c:'#1a1e26'},
    {t:'为给定的数学定理分配',c:'#1a1e26'},
    {t:'关键词和领域标签。',c:'#1a1e26'},
    {t:'',c:'#8893a0'},
    {t:'输出JSON格式:',c:'#e2b04a'},
    {t:'{',c:'#5a6070'},
    {t:'  "keywords": [...],',c:'#5a6070'},
    {t:'  "domain": [...],',c:'#5a6070'},
    {t:'  "confidence": 0.9',c:'#5a6070'},
    {t:'}',c:'#5a6070'},
    {t:'',c:'#8893a0'},
    {t:'领域标签(30+个可选):',c:'#1a1e26'},
    {t:'proximal_point, gradient_',c:'#667080'},
    {t:'method, accelerated_method...',c:'#667080'},
    {t:'',c:'#8893a0'},
    {t:'→ AI 返回结构化结果 ✅',c:'#43b884'},
  ];

  // Code editor mock
  svg.append('rect').attr('x',20).attr('y',20).attr('width',W-40).attr('height',H-40).attr('rx',8)
    .attr('fill','#fff').attr('stroke','#dde1e6').attr('stroke-width',1);
  // Title bar
  svg.append('rect').attr('x',20).attr('y',20).attr('width',W-40).attr('height',24).attr('rx',8)
    .attr('fill','#fafbfc');
  svg.append('circle').attr('cx',36).attr('cy',32).attr('r',4).attr('fill','#e05560');
  svg.append('circle').attr('cx',48).attr('cy',32).attr('r',4).attr('fill','#e2b04a');
  svg.append('circle').attr('cx',60).attr('cy',32).attr('r',4).attr('fill','#43b884');
  svg.append('text').attr('x',W/2).attr('y',34).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','9px').text('prompts/classify.txt');

  // Lines
  promptLines.forEach((l,i)=>{
    if(!l.t)return;
    svg.append('text').attr('x',35).attr('y',62+i*17).attr('fill',l.c).attr('font-size','11px').attr('font-family',"'Cascadia Code',Consolas,monospace")
      .attr('opacity',0).text(l.t).transition().duration(300).delay(300+i*40).attr('opacity',1);
  });
}

// ════════════════ Slide 4: Hybrid Strategy ════════════════
function r4(){
  const area=document.getElementById('hybrid-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#hybrid-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // Pie: Regex vs AI workload
  const data=[{l:'正则提取 (80%)',v:80,c:'#43b884'},{l:'AI 增强 (20%)',v:20,c:'#4da6d9'}];
  const cx=W/2,cy=H/2-20,radius=Math.min(W,H)/2-60;
  const arc=d3.arc().innerRadius(radius*0.5).outerRadius(radius).cornerRadius(4);
  const pie=d3.pie().value(d=>d.v).sort(null);

  const g=svg.append('g').attr('transform',`translate(${cx},${cy})`);

  svg.append('text').attr('class','chart-title-text').attr('x',W/2).attr('y',20).attr('text-anchor','middle').text('任务分工比例');

  pie(data).forEach((a,i)=>{
    g.append('path').attr('d',arc(a)).attr('fill',data[i].c).attr('stroke','#0a1118').attr('stroke-width',2).attr('opacity',0)
      .transition().duration(600).delay(i*200).attr('opacity',1);
  });

  // Legend
  [{c:'#43b884',l:'正则：快速稳定免费',y:cy+radius+25},{c:'#4da6d9',l:'AI：理解判断生成',y:cy+radius+45}].forEach(x=>{
    svg.append('circle').attr('cx',cx-40).attr('cy',x.y).attr('r',5).attr('fill',x.c);
    svg.append('text').attr('x',cx-28).attr('y',x.y).attr('dy','0.35em').attr('fill','#5a6070').attr('font-size','11px').text(x.l);
  });

  // Bottom benefit
  svg.append('text').attr('x',cx).attr('y',H-15).attr('text-anchor','middle').attr('fill','#8893a0').attr('font-size','10px').text('优势：快 10 倍 · 省 90% API 费用 · 结果可复现');
}

// ════════════════ Slide 5: Pipeline ════════════════
function r5(){
  const area=document.getElementById('pipeline-diagram');area.innerHTML='';
  const W=area.clientWidth||1000,H=area.clientHeight||420;
  const svg=d3.select('#pipeline-diagram').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  const stages=[
    {l:'① 解析',s:'正则提取\n定理声明',c:'#e05560',ai:false},
    {l:'② 关键词',s:'正则匹配\n33个模式',c:'#e8963e',ai:false},
    {l:'③ AI 增强',s:'Claude API\n分类+摘要',c:'#9b6cc4',ai:true},
    {l:'④ 去重',s:'结构签名\n相似度合并',c:'#4da6d9',ai:false},
    {l:'⑤ 关系发现',s:'多策略\n启发式规则',c:'#4da6d9',ai:false},
    {l:'⑥ 可视化',s:'D3.js\n交互图谱',c:'#43b884',ai:false},
  ];

  const totalW=stages.length*130+(stages.length-1)*30;
  const startX=(W-totalW)/2;
  const cy=H/2;

  stages.forEach((s,i)=>{
    const x=startX+i*160;
    const g=svg.append('g');

    // AI badge
    if(s.ai){
      g.append('rect').attr('x',x+15).attr('y',cy-68).attr('width',30).attr('height',14).attr('rx',7)
        .attr('fill','#9b6cc4').attr('opacity',0);
      g.append('text').attr('x',x+30).attr('y',cy-56).attr('text-anchor','middle')
        .attr('fill','#fff').attr('font-size','8px').attr('font-weight','700').text('AI');
      g.select('rect').transition().duration(400).delay(i*150+200).attr('opacity',1);
    }

    // Box
    g.append('rect').attr('x',x).attr('y',cy-40).attr('width',110).attr('height',80).attr('rx',10)
      .attr('fill','#fafbfc').attr('stroke',s.c).attr('stroke-width',2).attr('opacity',0);
    g.append('text').attr('x',x+55).attr('y',cy-14).attr('text-anchor','middle')
      .attr('fill',s.c).attr('font-size','14px').attr('font-weight','700').text(s.l);
    g.append('text').attr('x',x+55).attr('y',cy+12).attr('text-anchor','middle')
      .attr('fill','#8893a0').attr('font-size','9px').text(s.s.split('\n').join(' · '));
    g.select('rect').transition().duration(500).delay(i*150).attr('opacity',1);

    // Arrow
    if(i<stages.length-1){
      svg.append('line').attr('x1',x+110).attr('y1',cy).attr('x2',x+160).attr('y2',cy)
        .attr('stroke','#dde1e6').attr('stroke-width',2).attr('stroke-dasharray','5,3');
      svg.append('polygon').attr('points',`${x+157},${cy-4} ${x+167},${cy} ${x+157},${cy+4}`)
        .attr('fill','#3a5060');
    }
  });

  // Bottom note
  svg.append('text').attr('x',W/2).attr('y',H-20).attr('text-anchor','middle')
    .attr('fill','#8893a0').attr('font-size','10px').text('总耗时 ~8 秒 · Python 标准库 + Claude API(可选) · 零外部依赖');
}

// ════════════════ Slide 6: Results ════════════════
function r6(){
  const items=I(),rels=Rels(),papers=P();
  document.getElementById('results-stats').innerHTML=[
    {n:papers.length,l:'篇论文',c:'var(--gold)'},
    {n:items.length,l:'知识条目',c:'var(--acc)'},
    {n:rels.length,l:'条关系',c:'var(--c-corollary)'},
    {n:'~8s',l:'构建耗时',c:'var(--c-definition)'}
  ].map(s=>`<div class="result-card"><div class="num" style="color:${s.c}">${s.n}</div><div class="lbl">${s.l}</div></div>`).join('');

  // Type bar chart
  const tc={};items.forEach(it=>{tc[it.type]=(tc[it.type]||0)+1;});
  const a1=document.getElementById('type-bar-chart');a1.innerHTML='';
  const W1=a1.clientWidth||500,H1=a1.clientHeight||350;
  const m1={top:30,right:30,bottom:40,left:70},iw1=W1-m1.left-m1.right,ih1=H1-m1.top-m1.bottom;
  const types=Object.keys(CM).filter(t=>tc[t]);
  const svg1=d3.select('#type-bar-chart').append('svg').attr('viewBox',`0 0 ${W1} ${H1}`);
  const g1=svg1.append('g').attr('transform',`translate(${m1.left},${m1.top})`);
  const x1=d3.scaleLinear().domain([0,d3.max(types,t=>tc[t])+5]).range([0,iw1]);
  const y1=d3.scaleBand().domain(types).range([0,ih1]).padding(0.4);

  g1.append('text').attr('class','chart-title-text').attr('x',iw1/2).attr('y',-10).attr('text-anchor','middle').text('各类知识条目数量');
  g1.append('g').call(d3.axisLeft(y1).tickFormat(t=>TCN[t]||t)).selectAll('text').attr('fill','#5a6070').attr('font-size','11px');
  g1.selectAll('.domain,.tick line').attr('stroke','#dde1e6');
  g1.append('g').attr('transform',`translate(0,${ih1})`).call(d3.axisBottom(x1).ticks(5).tickFormat(d3.format('d'))).selectAll('text').attr('fill','#8893a0').attr('font-size','9px');
  g1.selectAll('.domain,.tick line').attr('stroke','#dde1e6');
  g1.selectAll('rect').data(types).join('rect').attr('y',d=>y1(d)).attr('height',y1.bandwidth()).attr('x',0).attr('width',0)
    .attr('fill',d=>CM[d]).attr('rx',3).transition().duration(700).delay((d,i)=>i*100).attr('width',d=>x1(tc[d]));
  g1.selectAll('.vl').data(types).join('text').attr('class','vl').attr('x',d=>x1(tc[d])+6).attr('y',d=>y1(d)+y1.bandwidth()/2)
    .attr('dy','0.35em').attr('fill','#1a1e26').attr('font-size','11px').attr('font-weight','600').text(d=>tc[d]);

  // Keyword top chart
  const kw={};items.forEach(it=>{(it.keywords||[]).forEach(k=>{kw[k]=(kw[k]||0)+1;});});
  const kwSorted=Object.entries(kw).filter(([k])=>!['theorem','lemma','corollary','definition','proposition'].includes(k)).sort((a,b)=>b[1]-a[1]).slice(0,10);
  const a2=document.getElementById('kw-top-chart');a2.innerHTML='';
  const W2=a2.clientWidth||500,H2=a2.clientHeight||350;
  const m2={top:30,right:30,bottom:10,left:90},iw2=W2-m2.left-m2.right,ih2=H2-m2.top-m2.bottom;
  const svg2=d3.select('#kw-top-chart').append('svg').attr('viewBox',`0 0 ${W2} ${H2}`);
  const g2=svg2.append('g').attr('transform',`translate(${m2.left},${m2.top})`);
  const maxK=d3.max(kwSorted,d=>d[1]);
  g2.append('text').attr('class','chart-title-text').attr('x',iw2/2).attr('y',-10).attr('text-anchor','middle').text('Top 10 高频关键词 (AI 分类)');
  const bh=Math.min(20,ih2/kwSorted.length-4);
  kwSorted.forEach(([k,v],i)=>{
    const y=i*(ih2/kwSorted.length);
    g2.append('text').attr('x',-6).attr('y',y+bh/2).attr('dy','0.35em').attr('text-anchor','end').attr('fill','#667080').attr('font-size','9px').text(k.replace(/_/g,' '));
    g2.append('rect').attr('x',0).attr('y',y+1).attr('height',bh-2).attr('rx',2).attr('fill',d3.interpolateBlues(v/maxK*0.7+0.3)).attr('width',0)
      .transition().duration(600).delay(i*40).attr('width',(v/maxK)*iw2*0.9);
    g2.append('text').attr('x',(v/maxK)*iw2*0.9+5).attr('y',y+bh/2).attr('dy','0.35em').attr('fill','#8893a0').attr('font-size','8px').text(v);
  });
}

// ════════════════ Slide 7: Interactive Graph ════════════════
let graphState=null;
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

  // Same-paper edges
  const spLinks=[],pg={};
  nodes.forEach((n,i)=>{(n.papers||[]).forEach(pid=>{pg[pid]=pg[pid]||[];pg[pid].push(i);});});
  Object.values(pg).forEach(ix=>{for(let a=0;a<ix.length;a++)for(let b=a+1;b<Math.min(a+5,ix.length);b++)spLinks.push({source:ix[a],target:ix[b]});});

  // Detail map
  const detailMap={};
  items.forEach((it,idx)=>{
    const d={};if(it.summary)d.sm=it.summary;if(it.statement&&it.statement.length>20)d.st=it.statement.slice(0,400);if(it.latex)d.fm=[it.latex.slice(0,500)];if(Object.keys(d).length)detailMap[String(idx)]=d;
  });

  const svg=d3.select('#graph-canvas svg');svg.selectAll('*').remove();
  const zoom=d3.zoom().scaleExtent([0.08,5.5]).on('zoom',e=>{g.attr('transform',e.transform);updVis(e.transform);});
  svg.call(zoom);
  const g=svg.append('g');
  const splG=g.append('g');
  splG.selectAll('line').data(spLinks).join('line').attr('class','link-sp').attr('stroke','#3a4a60').attr('stroke-width',0.6).attr('stroke-dasharray','2,6').attr('stroke-opacity',0.12);
  const linkG=g.append('g');
  const linkSel=linkG.selectAll('line').data(linkData).join('line').attr('class','link')
    .attr('stroke',d=>RCM[d.type]||'#7a8a9a').attr('stroke-width',d=>d.type==='derives'?2.2:d.type==='generalizes'?1.6:1.1)
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
    d3.select('#tooltip').html(`<div style="color:#d0d8e0;font-weight:600">${d.name}</div><div style="font-size:9px;color:#506070">${TCN[d.type]} · ${d.sources.length} 来源</div>`).style('left',(e.pageX+12)+'px').style('top',(e.pageY-12)+'px').style('opacity',1);
  }).on('mouseout',function(e,d){
    d3.select(this).select('circle').transition().duration(120).attr('r',(SZ[d.type]||10)+Math.min((d.sources||[]).length*2,6));
    nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.28);d3.select('#tooltip').style('opacity',0);
  }).on('click',(e,d)=>{
    const dt=detailMap[String(d._i)]||{};
    let h=`<div style="color:#d0d8e0;font-weight:600;font-size:11px">${d.name}</div><div style="font-size:9px;color:#506070;margin-top:2px">${TCN[d.type]} · ${d.sources.length} 来源</div>`;
    if(dt.sm)h+=`<div style="font-size:9px;color:#8cb88c;margin-top:3px;max-width:240px;line-height:1.4">💡 ${dt.sm}</div>`;
    if(dt.fm)h+=`<div style="font-size:10px;color:#e2b04a;margin-top:3px;font-family:monospace;max-width:240px;overflow:hidden">${dt.fm[0].slice(0,200)}</div>`;
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
    linkSel.style('display',d=>{if(lo)return'none';const ns=nodes[d.source],nt=nodes[d.target];const sv=ns.x>vx-pad&&ns.x<vx+vw+pad&&ns.y>vy-pad&&ns.y<vy+vh+pad;return(sv||(nt.x>vx-pad&&nt.x<vx+vw+pad&&nt.y>vy-pad&&nt.y<vy+vh+pad))?null:'none';});
  }

  graphState={svg,zoom,updVis};

  // Legend
  document.getElementById('graph-legend').innerHTML=Object.entries(CM).map(([t,c])=>`<div class="gl-item"><span class="gl-dot" style="background:${c}"></span>${TCN[t]}</div>`).join('')
    +'<span style="margin:0 4px;color:#3a5060">|</span>'+Object.entries(RCN).slice(0,4).map(([t,l])=>`<div class="gl-item"><span class="gl-line solid" style="border-color:${RCM[t]}"></span>${l}</div>`).join('');

  // Search
  document.getElementById('graph-search-input').addEventListener('input',function(){
    const q=this.value.toLowerCase();if(!graphState)return;
    if(!q){nodeSel.selectAll('circle').attr('opacity',1);linkSel.attr('opacity',0.28);return;}
    const m=new Set();nodes.forEach(n=>{if((n.name+' '+(n.keywords||[]).join(' ')).toLowerCase().includes(q))m.add(n._i);});
    nodeSel.selectAll('circle').attr('opacity',n=>m.has(n._i)?1:0.06);
    linkSel.attr('opacity',l=>m.has(l.source)&&m.has(l.target)?1:0.02);
  });

  document.getElementById('zin').onclick=()=>svg.transition().duration(200).call(zoom.scaleBy,1.3);
  document.getElementById('zout').onclick=()=>svg.transition().duration(200).call(zoom.scaleBy,0.7);
  document.getElementById('zfit').onclick=()=>svg.transition().duration(400).call(zoom.transform,d3.zoomIdentity);
  setTimeout(()=>graphState&&graphState.updVis(),200);
}
function resizeGraph(){if(graphState){graphState.svg.selectAll('*').remove();renderGraph();}}

// ════════════════ Slide 8: Key Findings ════════════════
function r8(){
  const items=I(),rels=Rels(),papers=P();
  const pm={};papers.forEach(p=>{pm[p.id]=p;});
  const cc={};rels.forEach(r=>{cc[r.source_id]=(cc[r.source_id]||0)+1;cc[r.target_id]=(cc[r.target_id]||0)+1;});
  const scored=items.map(it=>({...it,score:(cc[it.id]||0)*3+(it.sources||[]).length*2+(it.confidence||0)*5}));
  scored.sort((a,b)=>b.score-a.score);

  document.getElementById('key-theorems').innerHTML=scored.slice(0,8).map((it,i)=>{
    const pid=(it.sources||[])[0]||it.id.split('_')[0],p=pm[pid];
    let summary=it.summary||'';
    if(!summary&&it.statement)summary=it.statement.slice(0,150)+'…';
    return`<div class="key-item"><div class="rank">${i+1}</div><div style="flex:1">
      <span class="badge" style="background:${CM[it.type]||'#666'}">${TCN[it.type]||it.type}</span>
      <div class="name">${it.name}</div>
      <div class="desc">${summary.slice(0,250)}</div>
      <div class="paper-ref">📄 ${p?`[${p.year}] ${(p.title||'').slice(0,45)}`:pid}</div>
      <div class="kw-row">${(it.keywords||[]).slice(0,5).map(k=>`<span class="kw-tag">${k}</span>`).join('')}</div>
    </div></div>`;
  }).join('');
}

// ════════════════ Slide 9: Lessons Learned ════════════════
function r9(){
  const area=document.getElementById('learn-chart');area.innerHTML='';
  const W=area.clientWidth||500,H=area.clientHeight||400;
  const svg=d3.select('#learn-chart').append('svg').attr('viewBox',`0 0 ${W} ${H}`);

  // A simple "recipe" diagram: what worked
  svg.append('text').attr('class','chart-title-text').attr('x',W/2).attr('y',22).attr('text-anchor','middle').text('AI 辅助开发「配方」');

  const items=[
    {y:60,icon:'📝',t:'写好 Prompt',s:'像写代码一样\n反复迭代优化'},
    {y:155,icon:'🔀',t:'混合策略',s:'正则 + AI 各取所长\n80% 规则 20% 模型'},
    {y:250,icon:'💾',t:'加缓存',s:'AI 结果存下来\n省钱 + 加速 + 稳定'},
    {y:340,icon:'✅',t:'人把关',s:'AI 生成的代码\n必须审查和测试'},
  ];

  items.forEach((x,i)=>{
    const g=svg.append('g');
    g.append('circle').attr('cx',50).attr('cy',x.y+12).attr('r',22).attr('fill','#fafbfc').attr('stroke','var(--acc)').attr('stroke-width',2).attr('opacity',0);
    g.append('text').attr('x',50).attr('y',x.y+16).attr('text-anchor','middle').attr('font-size','18px').text(x.icon);
    g.append('text').attr('x',90).attr('y',x.y+6).attr('fill','#1a1e26').attr('font-size','14px').attr('font-weight','600').text(x.t);
    g.append('text').attr('x',90).attr('y',x.y+28).attr('fill','#8893a0').attr('font-size','10px').text(x.s.split('\n').join(' · '));
    g.select('circle').transition().duration(500).delay(i*150).attr('opacity',1);
    if(i<items.length-1){
      svg.append('line').attr('x1',50).attr('y1',x.y+34).attr('x2',50).attr('y2',items[i+1].y-10)
        .attr('stroke','#dde1e6').attr('stroke-width',2).attr('stroke-dasharray','4,4');
    }
  });
}

// ════════════════ Slide 10: Thanks ════════════════
function r10(){
  const items=I(),rels=Rels(),papers=P();
  document.getElementById('thank-stats').innerHTML=[
    {n:papers.length,l:'篇论文',c:'var(--gold)'},{n:items.length,l:'知识条目',c:'var(--acc)'},
    {n:rels.length,l:'条关系',c:'var(--c-corollary)'},{n:'4',l:'个 Prompt',c:'var(--c-definition)'}
  ].map(s=>`<div class="summary-card"><div class="num" style="color:${s.c}">${s.n}</div><div class="lbl">${s.l}</div></div>`).join('');
}

// ════════════════ Boot ════════════════
document.addEventListener('DOMContentLoaded',init);
window.addEventListener('resize',()=>{if(currentSlide===7&&graphState){clearTimeout(window._rt);window._rt=setTimeout(()=>resizeGraph(),300);}});
