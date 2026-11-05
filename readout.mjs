const $ = id => document.getElementById(id);
const cyan = '#45c7c9', gold = '#d9ae66';
const ink = () => document.documentElement.dataset.theme==='biomech'?'#d2e1e6':'#17363a';
let dataset, run, model, timer, themeTimer;
const fmt = x => Number(x).toExponential(5);
function canvas(id) {
  const el=$(id), rect=el.getBoundingClientRect(), dpr=devicePixelRatio || 1;
  el.width=Math.round(rect.width*dpr);el.height=Math.round(rect.height*dpr);
  const c=el.getContext('2d');c.scale(dpr,dpr);c.font='12px ui-monospace, monospace';
  c.fillStyle=ink();c.strokeStyle=c.fillStyle;
  return [c,rect.width,rect.height];
}
function line(c, points, color, width=2) {
  c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.strokeStyle=color;c.lineWidth=width;c.stroke();
}
function stop() { clearInterval(timer);timer=undefined;$('play').textContent='Play updates'; }
function setup() {
  stop();const unsupported=$('tolerance').value==='1e-18';
  $('refusal').hidden=!unsupported;document.querySelector('.readout-grid').hidden=unsupported;
  for(const id of ['iteration','coefficient','play'])$(id).disabled=unsupported;
  if(unsupported) {
    const floor=dataset.runs[0].readouts.find(r=>r.q===Number($('family').value)).minimum_base_budget;
    $('refusal').textContent=`Not certified: the minimum base budget over all 64 admissible degrees is approximately ${fmt(floor)}, already greater than the requested 1e-18. No optimizer step can remove that fixed-data budget. This is a refusal by this certificate, not an approximation impossibility theorem.`;
    $('status').textContent='Requested tolerance declined. Choose a certified tolerance to replay an actual run.';
    return;
  }
  run=dataset.runs.find(r=>r.requested_tolerance===$('tolerance').value);
  model=run.readouts.find(r=>r.q===Number($('family').value));
  $('iteration').max=model.steps;$('iteration').value=model.steps;
  $('coefficient').replaceChildren(...model.targets.map((_,n)=>new Option(String(n),String(n))));
  $('certificate').href=`https://github.com/amelie-iska/GRH-research/blob/main/${run.certificate_path}`;
  $('provenance').textContent=`Full exact certificate SHA-256: ${run.certificate_sha256}. Figures use its display-only decimal projections.`;
  $('status').textContent=`Conductor ${model.q}: degree ${model.degree}, ${model.steps} executed updates; final certified uniform bound ≈ ${fmt(model.compact_uniform_bound)} ≤ ${run.requested_tolerance}.`;
  draw();
}
function convergence(k,base) {
  const [c,w,h]=canvas('convergence'), left=48,right=w-14,top=18,bottom=h-32;
  const X=i=>left+i/model.steps*(right-left),Y=x=>bottom-(Math.log10(Math.max(x,1e-34))+34)/35*(bottom-top);
  c.globalAlpha=.22;
  for(let e=-32;e<=0;e+=8){const y=Y(10**e);line(c,[[left,y],[right,y]],c.fillStyle,1);c.globalAlpha=1;c.fillText(`10^${e}`,2,y+4);c.globalAlpha=.22;}c.globalAlpha=1;
  line(c,model.trace.map(s=>[X(s.iteration),Y(base+s.residual)]),cyan);
  line(c,model.trace.map(s=>[X(s.iteration),Y(s.objective)]),gold);
  c.setLineDash([5,5]);line(c,[[left,Y(model.requested_tolerance)],[right,Y(model.requested_tolerance)]],c.fillStyle,1);c.setLineDash([]);
  line(c,[[X(k),top],[X(k),bottom]],c.fillStyle,1);c.fillText('0',left,bottom+22);c.fillText(`update ${model.steps}`,Math.max(left,right-100),bottom+22);
}
function budgets(step) {
  const [c,w,h]=canvas('budget'), parts={...model.budget,optimization:step.residual};
  Object.entries(parts).forEach(([name,value],i)=>{
    const y=30+i*52;c.fillText(`${name}: ${fmt(value)}`,8,y);
    c.fillStyle=name==='optimization'?gold:cyan;c.fillRect(8,y+10,Math.max(1,(Math.log10(Math.max(value,1e-70))+70)/71*(w-20)),9);
    c.fillStyle=ink();
  });
}
function poly(coefficients,z) {
  let x=0,y=0;
  for(let n=coefficients.length-1;n>=0;n--){const [a,b]=coefficients[n];[x,y]=[x*z[0]-y*z[1]+a,x*z[1]+y*z[0]+b];}
  return [x,y];
}
function boundary(step) {
  const [c,w,h]=canvas('boundary'), circles=coeff=>Array.from({length:129},(_,j)=>{const t=2*Math.PI*j/128;return poly(coeff,[7/12*Math.cos(t),7/12*Math.sin(t)]);});
  const reference=circles(model.coefficients), selected=circles(step.coefficients);
  const all=[...reference,...selected],xs=all.map(p=>p[0]),ys=all.map(p=>p[1]);
  const xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
  const cx=(xmin+xmax)/2,cy=(ymin+ymax)/2,span=Math.max(xmax-xmin,ymax-ymin,1e-6),scale=Math.min(w-90,h-80)/span;
  const project=([x,y])=>[w/2+(x-cx)*scale,h/2-(y-cy)*scale];
  c.globalAlpha=.35;line(c,reference.map(project),c.fillStyle,2);c.globalAlpha=1;
  line(c,selected.map(project),cyan,2.5);
  selected.forEach((p,j)=>{if(j%8)return;const [x,y]=project(p);c.fillStyle=`hsl(${j/128*360} 65% 60%)`;c.beginPath();c.arc(x,y,3,0,2*Math.PI);c.fill();});
  c.fillStyle=ink();c.fillText('Re P(s) →',w-95,h-10);c.fillText('Im P(s)',8,18);
  if(step.iteration===0){c.fillText('Zero initialization; image P₀(s)=0',12,h-32);}
}
function draw() {
  if(!model || $('tolerance').value==='1e-18')return;
  const k=Number($('iteration').value),step=model.trace[k],n=Number($('coefficient').value);
  const base=Object.entries(model.budget).filter(([key])=>key!=='optimization').reduce((sum,[,v])=>sum+v,0);
  $('stepLabel').value=`${k} / ${model.steps}`;
  const b=step.coefficients[n],t=model.targets[n];
  $('values').textContent=`q = ${model.q}   degree = ${model.degree}\n64 validated circle labels\nStep = ${k}; gradient step = 1/4\nJ(b) ≈ ${fmt(step.objective)}\nOptimization residual ≈ ${fmt(step.residual)}\nCompact uniform bound ≈ ${fmt(base+step.residual)}\nRequested error = ${run.requested_tolerance}\n\nCoefficient n = ${n}\nb_n ≈ ${fmt(b[0])} + i (${fmt(b[1])})\nt_n ≈ ${fmt(t[0])} + i (${fmt(t[1])})\nReal gradient b_n − t_n:\n(${fmt(b[0]-t[0])}, ${fmt(b[1]-t[1])})\n\nOnly q3/q4/q5; |s−1/2| ≤ 7/10.\nAll displayed decimals are approximate.\nNo zero-location or GRH conclusion.`;
  convergence(k,base);budgets(step);boundary(step);
}
$('family').addEventListener('change',setup);$('tolerance').addEventListener('change',setup);
$('iteration').addEventListener('input',()=>{stop();draw();});$('coefficient').addEventListener('change',draw);
$('play').addEventListener('click',()=>{
  if(timer){stop();return;}
  if(Number($('iteration').value)>=model.steps)$('iteration').value=0;
  $('play').textContent='Pause updates';timer=setInterval(()=>{let k=Number($('iteration').value);if(k>=model.steps){stop();return;}$('iteration').value=k+1;draw();},90);
});
window.addEventListener('resize',draw);new MutationObserver(()=>{draw();clearTimeout(themeTimer);themeTimer=setTimeout(draw,3100);}).observe(document.documentElement,{attributes:true});
try{const response=await fetch('/data/adaptive-readout/summary-v3.json');if(!response.ok)throw Error(`HTTP ${response.status}`);dataset=await response.json();setup();}
catch(e){$('status').textContent=`Unable to load certificate replay: ${e.message}`;for(const id of ['play','iteration','family','tolerance','coefficient'])$(id).disabled=true;}
