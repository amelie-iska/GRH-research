import {sixthFreePowers,globalPhysicalState} from './physical-sieve-model.mjs';
// Original analytic exponent inspector. No simulation, network data or dependencies.
export function pivotState(a, dLog = 12) {
  if (!Number.isFinite(a) || a < 0 || a > .25) throw new RangeError('a must lie in [0,1/4]');
  if (!Number.isFinite(dLog) || dLog < 0 || dLog > 100) throw new RangeError('log10 D must lie in [0,100]');
  const D = 10 ** dLog, H = D ** .75;
  const A = D ** a, B = D ** (.25-a), R = A*A*B;
  const oldPowers = [.25+a, 1.25, 11/12+2*a/3];
  const quadPowers = [.25+a, 1+2*a];
  const oldTerms = [R, D*R/A, D**(2/3)*R/A**(1/3)];
  const quadTerms = [R, D*R/B];
  const oldPower = Math.max(...oldPowers), quadPower = Math.max(...quadPowers);
  const refinedPower = Math.min(oldPower,quadPower);
  const oldSum = oldTerms.reduce((x,y)=>x+y,0), quadSum = quadTerms.reduce((x,y)=>x+y,0);
  const ordinaryPowers=[1,.5+2*a], ordinaryTerms=[D,R*R];
  const ordinaryPower=Math.max(...ordinaryPowers), ordinarySum=ordinaryTerms.reduce((x,y)=>x+y,0);
  const physicalPowers=sixthFreePowers(.75),physicalPower=Math.max(...physicalPowers),physicalTerms=physicalPowers.map(p=>10**(dLog*p)),physicalSum=physicalTerms.reduce((x,y)=>x+y,0);
  const currentPower=Math.min(refinedPower,ordinaryPower,physicalPower), currentSum=Math.min(oldSum,quadSum,ordinarySum,physicalSum);
  // Historical fields below retain the earlier cube-only semantics for preserved consumers.
  return {physicalPowers,physicalPower,physicalTerms,physicalSum,ordinaryPowers,ordinaryTerms,ordinaryPower,ordinarySum,currentPower,currentSum,
    currentSaving:oldPower-currentPower,currentTargetGap:currentPower-.75,
    globalPower:9/8,globalTargetGap:3/8,previousGlobalPower:7/6,a,dLog,D,H,A,B,R,Aj:[A,A,B,1,1,1],M:A,capacity:A*A**2*B**3,
    oldPowers,quadPowers,oldTerms,quadTerms,oldPower,quadPower,refinedPower,
    oldSum,quadSum,refinedSum:Math.min(oldSum,quadSum),saving:oldPower-refinedPower,
    targetGap:refinedPower-.75,strictSaving:a<.125};
}
export function obstructionState(x1,x2,dLog=12) {
  if(!Number.isFinite(x1)||!Number.isFinite(x2)||x1<0||x2<0||x1+2*x2>.75+1e-12)throw new RangeError('Point must lie in the capacity triangle');
  if(!Number.isFinite(dLog)||dLog<0||dLog>100)throw new RangeError('Invalid log10 D');
  const r=x1+x2,m=Math.max(x1,x2),oldPowers=[r,1+r-m,2/3+r-m/3],ordinaryPowers=[1,2*r];
  const oldPower=Math.max(...oldPowers),ordinaryPower=Math.max(...ordinaryPowers),physicalPowers=sixthFreePowers(x1+2*x2),physicalPower=Math.max(...physicalPowers),previousPower=Math.min(oldPower,ordinaryPower),currentPower=Math.min(previousPower,physicalPower);
  return{physicalPowers,physicalPower,previousPower,x1,x2,r,m,dLog,capacityPower:x1+2*x2,oldPowers,ordinaryPowers,oldPower,ordinaryPower,currentPower,targetGap:currentPower-.75,
    oldTerms:oldPowers.map(p=>10**(dLog*p)),ordinaryTerms:ordinaryPowers.map(p=>10**(dLog*p))};
}
const shortPower=x=>Number(x.toFixed(6)).toString();
const decimal=x=>x.toExponential(3).replace('e+','e');
const exponentLabel=x=>({0:'0',0.0625:'1/16',0.125:'1/8',0.1875:'3/16',0.25:'1/4'})[x]??shortPower(x);
const NS='http://www.w3.org/2000/svg';
function element(name,attributes={},text){const e=document.createElementNS(NS,name);for(const[k,v]of Object.entries(attributes))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=text;return e;}
function polyline(points,stroke,width=2,dash=''){return element('polyline',{points:points.map(p=>p.join(',')).join(' '),fill:'none',stroke,'stroke-width':width,'stroke-dasharray':dash,'stroke-linejoin':'round'});}
function drawPlot(state,detail){
 const svg=document.getElementById('exponentPlot'),width=Math.max(250,Math.round(svg.getBoundingClientRect().width)),height=width<560?370:430;
 svg.setAttribute('viewBox',`0 0 ${width} ${height}`);
 const left=49,right=width-19,top=55,bottom=height-52,floor=detail==='terms'?.15:.65;
 const X=a=>left+(right-left)*a/.25,Y=b=>bottom-(b-floor)/(1.6-floor)*(bottom-top),style=getComputedStyle(document.documentElement),color=n=>style.getPropertyValue('--pivot-'+n).trim();
 const nodes=[element('title',{id:'plot-title'},'Historical and current upper-bound powers on the complete former saturation face'),element('desc',{id:'plot-desc'},`At a=${shortPower(state.a)}, old BGL power 1.25, earlier cube-only minimum${shortPower(state.refinedPower)}, current ordinary-conductor power 1, target 0.75. The entire face from 0 to1/4 is improved by the new comparison.`)];
 nodes.push(element('rect',{x:left,y:Y(1.25),width:right-left,height:Y(1)-Y(1.25),fill:'var(--pivot-improved)'}));
 for(const b of detail==='terms'?[.25,.5,.75,1,1.25,1.5]:[.75,1,1.25,1.5]){nodes.push(polyline([[left,Y(b)],[right,Y(b)]],'var(--line)',1));nodes.push(element('text',{x:left-9,y:Y(b)+4,'text-anchor':'end'},shortPower(b)));}
 nodes.push(polyline([[left,top],[left,bottom],[right,bottom]],'var(--muted)',1));
 for(const a of[0,.0625,.125,.1875,.25]){nodes.push(polyline([[X(a),bottom],[X(a),bottom+5]],'var(--muted)',1));nodes.push(element('text',{x:X(a),y:bottom+21,'text-anchor':'middle'},exponentLabel(a)));}
 nodes.push(element('text',{x:13,y:23,class:'axis-title'},'β in D^β'));
 nodes.push(element('text',{x:(left+right)/2,y:height-9,'text-anchor':'middle',class:'axis-title'},'a · entire former face'));
 if(detail==='terms'){
  nodes.push(polyline([[left,Y(.25)],[right,Y(.5)]],'var(--muted)',1.4,'2 5'));
  nodes.push(polyline([[left,Y(11/12)],[right,Y(13/12)]],color('old'),1.4,'9 4 2 4'));
  nodes.push(polyline([[left,Y(1)],[right,Y(1.5)]],color('quad'),1.2,'3 4'));
  nodes.push(polyline([[left,Y(.5)],[right,Y(1)]],color('old'),1.6,'4 4'));
 }
 nodes.push(polyline([[left,Y(.75)],[right,Y(.75)]],color('target'),2,'2 5'));
 nodes.push(polyline([[left,Y(1.25)],[right,Y(1.25)]],color('old'),2.5));
 nodes.push(polyline([[left,Y(1)],[X(.125),Y(1.25)],[right,Y(1.25)]],color('quad'),3,'7 5'));
 nodes.push(polyline([[left,Y(13/12)],[right,Y(13/12)]],color('physical'),2,'3 4'));
 nodes.push(polyline([[left,Y(1)],[right,Y(1)]],color('refined'),5));
 nodes.push(polyline([[X(state.a),top],[X(state.a),bottom]],'var(--ink)',1.2,'2 3'));
 for(const[p,c]of[[state.oldPower,color('old')],[state.refinedPower,color('quad')],[state.currentPower,color('refined')]])nodes.push(element('circle',{cx:X(state.a),cy:Y(p),r:4.8,fill:'var(--pivot-panel)',stroke:c,'stroke-width':2}));
 nodes.push(element('text',{x:Math.max(left+35,Math.min(right-35,X(state.a))),y:top-10,'text-anchor':'middle',class:'selection-label'},`a = ${exponentLabel(state.a)}`));
 svg.replaceChildren(...nodes);svg.dataset.refinedPower=String(state.currentPower);svg.dataset.historicalPower=String(state.refinedPower);svg.dataset.fullFace='0,0.25';
}
function drawObstruction(s){
 const svg=document.getElementById('obstructionPlot'),width=Math.max(250,Math.round(svg.getBoundingClientRect().width)),height=width<560?330:360;
 svg.setAttribute('viewBox',`0 0 ${width} ${height}`);
 const left=49,right=width-20,top=32,bottom=height-47,X=x=>left+x/.75*(right-left),Y=y=>bottom-y/.375*(bottom-top);
 svg.dataset.plotGeometry=JSON.stringify({left,right,top,bottom,width,height});
 const dark=document.documentElement.dataset.theme==='biomech',low=dark?[17,65,74]:[205,230,218],high=dark?[167,121,48]:[174,115,43];
 const fill=p=>{const t=Math.max(0,Math.min(1,(p-1)*12));return`rgb(${low.map((c,i)=>Math.round(c+(high[i]-c)*t)).join(',')})`;};
 const nodes=[element('title',{id:'obstruction-plot-title'},'Current upper-bound powers in the capacity triangle'),element('desc',{id:'obstruction-plot-desc'},`Selected x1=${shortPower(s.x1)},x2=${shortPower(s.x2)}; combined upper power ${shortPower(s.currentPower)}. Maximum available slice envelope 13/12, target 3/4. Witnesses are not actual energy lower bounds.`)];
 const n=32;
 for(let i=0;i<n;i++)for(let j=0;j<n-i;j++){
  const add=verts=>{const x1=verts.reduce((a,v)=>a+v[0],0)/3,x2=verts.reduce((a,v)=>a+v[1],0)/3,p=obstructionState(x1,x2).currentPower;nodes.push(element('polygon',{points:verts.map(([x,y])=>`${X(x)},${Y(y)}`).join(' '),fill:fill(p),stroke:fill(p),'stroke-width':.5}));};
  add([[.75*i/n,.375*j/n],[.75*(i+1)/n,.375*j/n],[.75*i/n,.375*(j+1)/n]]);
  if(i+j<n-1)add([[.75*(i+1)/n,.375*j/n],[.75*(i+1)/n,.375*(j+1)/n],[.75*i/n,.375*(j+1)/n]]);
 }
 nodes.push(polyline([[left,top],[left,bottom],[right,bottom],[left,top]],'var(--muted)',1.3));
 for(const x of[0,.25,.5,.75])nodes.push(element('text',{x:X(x),y:bottom+20,'text-anchor':'middle'},shortPower(x)));
 for(const y of[.125,.25,.375])nodes.push(element('text',{x:left-8,y:Y(y)+4,'text-anchor':'end'},shortPower(y)));
 nodes.push(element('text',{x:15,y:19},'x₂'));nodes.push(element('text',{x:right-3,y:height-7},'x₁'));
 for(const[x,y]of[[5/12,1/6],[.75,0]])nodes.push(element('circle',{cx:X(x),cy:Y(y),r:4,fill:'var(--pivot-panel)',stroke:'var(--ink)','stroke-width':1.5}));
 nodes.push(element('circle',{cx:X(s.x1),cy:Y(s.x2),r:7,fill:'none',stroke:'var(--ink)','stroke-width':2}));
 svg.replaceChildren(...nodes);svg.dataset.currentPower=String(s.currentPower);svg.dataset.x1=String(s.x1);svg.dataset.x2=String(s.x2);
}
function init(){
 const $=id=>document.getElementById(id);let current,witness={x1:5/12,x2:1/6};
 const dl=(target,rows)=>$(target).replaceChildren(...rows.map(([name,value])=>{const div=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=name;dd.textContent=value;div.append(dt,dd);return div;}));
 function renderWitness(){const s=obstructionState(witness.x1,witness.x2,Number($('dScale').value));drawObstruction(s);
  $('obstructionStatus').textContent=`Selected point: current upper-bound power ${shortPower(s.currentPower)}. Its displayed excess above target 3/4 is ${shortPower(s.targetGap)}. This is an available-bound comparison, not a lower bound for energy.`;
  dl('obstructionValues',[['x₁, x₂',`${shortPower(s.x1)}, ${shortPower(s.x2)}`],['Capacity x₁+2x₂ ≤ 3/4',shortPower(s.capacityPower)],['Old BGL power',shortPower(s.oldPower)],['Ordinary power',shortPower(s.ordinaryPower)],['Previous combined power',shortPower(s.previousPower)],['Sixth-free power',shortPower(s.physicalPower)],['Current minimum',shortPower(s.currentPower)],['Old monomial sum ≈',decimal(s.oldTerms.reduce((a,b)=>a+b,0))],['Ordinary monomial sum ≈',decimal(s.ordinaryTerms.reduce((a,b)=>a+b,0))]]);
  for(const b of document.querySelectorAll('[data-witness]')){const target=b.dataset.witness==='mixed'?[5/12,1/6]:[.75,0];b.setAttribute('aria-pressed',String(Math.abs(s.x1-target[0])<1e-12&&Math.abs(s.x2-target[1])<1e-12));}
 }
 function render(){const a=Number($('aValue').value)/4000;current=pivotState(a,Number($('dScale').value));
  $('aLabel').value=`a = ${exponentLabel(a)} ≈ ${a.toFixed(5)}`;$('aValue').setAttribute('aria-valuetext',`a equals ${exponentLabel(a)}; current power 1, historical cube-only power ${shortPower(current.refinedPower)}`);
  $('sectorStatus').textContent='Current ordinary comparison: power 1 on this entire face. The earlier cube-only curve is retained as a historical comparison.';
  for(const[id,value]of[['oldPower',current.oldPower],['quadPower',current.refinedPower],['refinedPower',current.currentPower]])$(id).textContent=value.toFixed(3);
  $('savingPower').innerHTML='D<sup>1/4</sup>';$('gapTarget').textContent='The current face upper-bound power 1 remains 1/4 above target 3/4. The global envelope is now 9/8.';
  const rows=[['F₆(H,D)','sixth-free comparison',current.physicalPower,current.physicalSum],['R','shared',current.oldPowers[0],current.R],['DR/M','old middle',current.oldPowers[1],current.oldTerms[1]],['D<sup>2/3</sup>R/M<sup>1/3</sup>','old third',current.oldPowers[2],current.oldTerms[2]],['DR/A₃','earlier cube pivot',current.quadPowers[1],current.quadTerms[1]],['D','current ordinary',1,current.D],['R²','current ordinary',current.ordinaryPowers[1],current.ordinaryTerms[1]],['H','target',.75,current.H]];
  $('termRows').replaceChildren(...rows.map(([name,label,power,value])=>{const tr=document.createElement('tr'),td=document.createElement('td'),small=document.createElement('small');td.innerHTML=name;small.textContent=label;td.append(small);tr.append(td);if(label==='current ordinary')tr.dataset.current='true';for(const v of[shortPower(power),decimal(value)]){const e=document.createElement('td');e.textContent=v;tr.append(e);}return tr;}));
  for(const[id,value]of[['oldSum',current.oldSum],['quadSum',current.quadSum],['refinedSum',current.refinedSum],['ordinarySum',current.ordinarySum],['physicalSum',current.physicalSum],['currentSum',current.currentSum]])$(id).textContent=decimal(value);
  dl('geometryValues',[['A₁ = A₂ = M',decimal(current.A)],['A₃',decimal(current.B)],['A₄ = A₅ = A₆','1'],['H = D^(3/4)',decimal(current.H)],['R = A₁A₂A₃',decimal(current.R)],['A₁A₃ = A₂A₃ = H^(1/3)',decimal(current.A*current.B)],['∏ⱼ Aⱼ^j',decimal(current.capacity)],['A₃ / A₁',decimal(current.B/current.A)]]);
  const valid=Math.abs(Math.log(current.capacity/current.H))<1e-10;$('capacityStatus').textContent=valid?'Capacity saturated: ∏ⱼ Aⱼ^j = (A₁A₃)³ = H. The complete face remains admissible.':'Capacity check failed.';$('capacityStatus').dataset.valid=String(valid);
  $('termLegend').hidden=$('plotView').value!=='terms';drawPlot(current,$('plotView').value);renderWitness();renderGlobal();document.body.dataset.ready='true';
 }

 function renderGlobal(){
  const s=globalPhysicalState(Number($('thetaValue').value)/1000);$('thetaLabel').value='θ = '+shortPower(s.theta);
  $('globalStatus').textContent='Global upper power '+shortPower(s.power)+'; previous '+shortPower(s.previousPower)+'; sixth-free slice '+shortPower(s.sixthFreePower)+'. Target H has power '+shortPower(s.theta)+'.';
  dl('globalValues',[['Global power',shortPower(s.power)],['Previous global power',shortPower(s.previousPower)],['Sixth-free A₆=1 power',shortPower(s.sixthFreePower)],['Target H power',shortPower(s.theta)],['Global target gap',shortPower(s.targetGap)]]);
  const svg=$('globalPlot'),width=Math.max(250,Math.round(svg.getBoundingClientRect().width)),height=340,left=49,right=width-20,top=30,bottom=height-43,X=x=>left+x*(right-left),Y=y=>bottom-y/1.5*(bottom-top);
  svg.setAttribute('viewBox','0 0 '+width+' '+height);
  const nodes=[element('title',{},'Global and sixth-power-free upper-bound powers'),element('desc',{},'The global current power is 1 plus theta over 6 for theta between zero and one. At theta three quarters it is 9/8. The sixth-free slice is 13/12.')];
  for(const y of[0,.5,.75,1,1.25,1.5]){nodes.push(polyline([[left,Y(y)],[right,Y(y)]],'var(--line)',1));nodes.push(element('text',{x:left-7,y:Y(y)+4,'text-anchor':'end'},shortPower(y)));}
  for(const x of[0,.25,.5,.75,1])nodes.push(element('text',{x:X(x),y:bottom+22,'text-anchor':'middle'},shortPower(x)));
  const curves=[['previousPower','old','7 5'],['sixthFreePower','quad','3 4'],['power','physical',''],['theta','target','2 5']];
  for(const[key,color,dash]of curves){const points=Array.from({length:101},(_,i)=>{const v=globalPhysicalState(i/100);return[X(v.theta),Y(v[key])];});nodes.push(polyline(points,'var(--pivot-'+color+')',key==='power'?4:2,dash));nodes.push(element('circle',{cx:X(s.theta),cy:Y(s[key]),r:4,fill:'var(--pivot-panel)',stroke:'var(--pivot-'+color+')','stroke-width':2}));}
  nodes.push(polyline([[X(s.theta),top],[X(s.theta),bottom]],'var(--ink)',1,'2 3'));svg.replaceChildren(...nodes);svg.dataset.globalPower=String(s.power);svg.dataset.sixthFreePower=String(s.sixthFreePower);svg.dataset.theta=String(s.theta);
 }
 $('thetaValue').addEventListener('input',renderGlobal);

 for(const id of['aValue','dScale','plotView'])$(id).addEventListener(id==='aValue'?'input':'change',render);
 for(const button of document.querySelectorAll('[data-witness]'))button.addEventListener('click',()=>{witness=button.dataset.witness==='mixed'?{x1:5/12,x2:1/6}:{x1:.75,x2:0};renderWitness();});
 $('obstructionPlot').addEventListener('click',event=>{const svg=$('obstructionPlot'),g=JSON.parse(svg.dataset.plotGeometry),rect=svg.getBoundingClientRect(),x=(event.clientX-rect.left)/rect.width*g.width,y=(event.clientY-rect.top)/rect.height*g.height;const x1=(x-g.left)/(g.right-g.left)*.75,x2=(g.bottom-y)/(g.bottom-g.top)*.375;if(x1>=0&&x2>=0&&x1+2*x2<=.75){witness={x1,x2};renderWitness();}});
 $('obstructionPlot').addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(event.key))return;event.preventDefault();let{x1,x2}=witness;if(event.key==='ArrowLeft')x1=Math.max(0,x1-.00625);if(event.key==='ArrowRight')x1=Math.min(.75-2*x2,x1+.00625);if(event.key==='ArrowDown')x2=Math.max(0,x2-.003125);if(event.key==='ArrowUp')x2=Math.min((.75-x1)/2,x2+.003125);witness={x1,x2};renderWitness();});
 let frame;const redraw=()=>{cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>{drawPlot(current,$('plotView').value);renderWitness();renderGlobal();});};const observer=new ResizeObserver(redraw);observer.observe($('exponentPlot'));observer.observe($('obstructionPlot'));observer.observe($('globalPlot'));new MutationObserver(redraw).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});render();
}
if(typeof document!=='undefined')init();
