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
  return {a,dLog,D,H,A,B,R,Aj:[A,A,B,1,1,1],M:A,capacity:A*A**2*B**3,
    oldPowers,quadPowers,oldTerms,quadTerms,oldPower,quadPower,refinedPower,
    oldSum,quadSum,refinedSum:Math.min(oldSum,quadSum),saving:oldPower-refinedPower,
    targetGap:refinedPower-.75,strictSaving:a<.125};
}
const shortPower = x => Number(x.toFixed(6)).toString();
const decimal = x => x.toExponential(3).replace('e+','e');
const exponentLabel = x => ({0:'0',0.0625:'1/16',0.125:'1/8',0.1875:'3/16',0.25:'1/4'})[x] ?? shortPower(x);
const NS = 'http://www.w3.org/2000/svg';
function element(name, attributes = {}, text) {
  const e = document.createElementNS(NS,name);
  for (const [key,value] of Object.entries(attributes)) e.setAttribute(key,String(value));
  if (text!==undefined) e.textContent=text;
  return e;
}
function drawPlot(state, detail) {
  const svg=document.getElementById('exponentPlot');
  const width=Math.max(250,Math.round(svg.getBoundingClientRect().width)),height=width<560?370:430;
  svg.setAttribute('viewBox',`0 0 ${width} ${height}`);
  const left=49,right=width-19,top=62,bottom=height-52;
  const floor=detail==='terms'?.15:.65;
  const X=a=>left+(right-left)*a/.25, Y=b=>bottom-(b-floor)/(1.6-floor)*(bottom-top);
  const colors=getComputedStyle(document.documentElement);
  const color=name=>colors.getPropertyValue('--pivot-'+name).trim();
  const line=(points,stroke,strokeWidth=2,dash='',extra={})=>element('polyline',{points:points.map(([x,y])=>`${x},${y}`).join(' '),fill:'none',stroke,'stroke-width':strokeWidth,'stroke-dasharray':dash,'stroke-linejoin':'round',...extra});
  const nodes=[element('title',{id:'plot-title'},'Old, quadratic and refined powers across the full saturation face'),element('desc',{id:'plot-desc'},`At a=${shortPower(state.a)}, the old leading power is 1.25, the quadratic power is ${shortPower(state.quadPower)}, and the refined power is ${shortPower(state.refinedPower)}. The target is 0.75. Strict saving occurs only below a=1/8; the complete face from 0 to 1/4 remains visible.`)];
  const defs=element('defs'),pattern=element('pattern',{id:'openHatch',patternUnits:'userSpaceOnUse',width:10,height:10});
  pattern.append(line([[0,10],[10,0]],colors.getPropertyValue('--pivot-stripe').trim(),1));defs.append(pattern);nodes.push(defs);
  nodes.push(element('rect',{x:left,y:top,width:X(.125)-left,height:bottom-top,fill:colors.getPropertyValue('--pivot-improved').trim()}));
  nodes.push(element('rect',{x:X(.125),y:top,width:right-X(.125),height:bottom-top,fill:colors.getPropertyValue('--pivot-open').trim()}));
  nodes.push(element('rect',{x:X(.125),y:top,width:right-X(.125),height:bottom-top,fill:'url(#openHatch)'}));
  for(const b of detail==='terms'?[.25,.5,.75,1,1.25,1.5]:[.75,1,1.25,1.5]) {
    nodes.push(line([[left,Y(b)],[right,Y(b)]],'var(--line)',1));
    nodes.push(element('text',{x:left-9,y:Y(b)+4,'text-anchor':'end'},shortPower(b)));
  }
  nodes.push(line([[left,top],[left,bottom],[right,bottom]],'var(--muted)',1));
  for(const a of [0,.0625,.125,.1875,.25]) {
    nodes.push(line([[X(a),bottom],[X(a),bottom+5]],'var(--muted)',1));
    nodes.push(element('text',{x:X(a),y:bottom+21,'text-anchor':'middle'},exponentLabel(a)));
  }
  nodes.push(element('text',{x:13,y:24,class:'axis-title'},'β in D^β'));
  nodes.push(element('text',{x:(left+right)/2,y:height-9,'text-anchor':'middle',class:'axis-title'},'a · full saturation face'));
  nodes.push(element('text',{x:(left+X(.125))/2,y:43,'text-anchor':'middle',class:'sector-label'},width<420?'strict saving':'strict power saving'));
  nodes.push(element('text',{x:(X(.125)+right)/2,y:43,'text-anchor':'middle',class:'sector-label'},width<420?'old face survives':'old power survives'));
  nodes.push(line([[X(.125),top],[X(.125),bottom]],'var(--muted)',1,'3 5'));
  if(detail==='terms') {
    nodes.push(line([[X(0),Y(.25)],[X(.25),Y(.5)]],'var(--muted)',1.8,'2 5'));
    nodes.push(line([[X(0),Y(11/12)],[X(.25),Y(13/12)]],color('old'),1.8,'9 4 2 4'));
  }
  const y=Y;
  nodes.push(line([[left,y(.75)],[right,y(.75)]],color('target'),2,'2 5'));
  nodes.push(line([[left,y(1.25)],[right,y(1.25)]],color('old'),2.5));
  nodes.push(line([[left,y(1)],[right,y(1.5)]],color('quad'),2.3,'7 5'));
  nodes.push(line([[left,y(1)],[X(.125),y(1.25)],[right,y(1.25)]],color('refined'),5));
  nodes.push(line([[X(state.a),top],[X(state.a),bottom]],'var(--ink)',1.2,'2 3'));
  for(const [p,c] of [[state.oldPower,color('old')],[state.quadPower,color('quad')],[state.refinedPower,color('refined')]])nodes.push(element('circle',{cx:X(state.a),cy:y(p),r:4.8,fill:'var(--pivot-panel)',stroke:c,'stroke-width':2}));
  nodes.push(element('text',{x:Math.max(left+34,Math.min(right-34,X(state.a))),y:top-8,'text-anchor':'middle',class:'selection-label'},`a = ${exponentLabel(state.a)}`));
  svg.replaceChildren(...nodes);
  svg.dataset.refinedPower=String(state.refinedPower);svg.dataset.fullFace='0,0.25';
}
function init() {
  const $=id=>document.getElementById(id);
  let current;
  function render() {
    const a=Number($('aValue').value)/4000,detail=$('plotView').value;
    current=pivotState(a,Number($('dScale').value));
    $('aLabel').value=`a = ${exponentLabel(a)} ≈ ${a.toFixed(5)}`;
    $('aValue').setAttribute('aria-valuetext',`a equals ${exponentLabel(a)}; refined power ${shortPower(current.refinedPower)}`);
    $('sectorStatus').textContent=current.strictSaving?'A₃ dominates by a D-power. The quadratic pivot strictly improves the leading power.':a===.125?'Crossover: A₁ = A₃. Both bounds have leading power 5/4; no strict power saving.':'A₁ ≥ A₃. The old bound retains leading power 5/4 throughout this sector.';
    for(const [id,value] of [['oldPower',current.oldPower],['quadPower',current.quadPower],['refinedPower',current.refinedPower]])$(id).textContent=value.toFixed(3);
    const saving=$('savingPower');saving.replaceChildren();
    if(current.saving>0){saving.append('D');const sup=document.createElement('sup');sup.textContent=shortPower(current.saving);saving.append(sup);}else saving.textContent='No power gain';
    $('gapTarget').textContent=`Refined power is still ${shortPower(current.targetGap)} above the target; the displayed power gap is D^${shortPower(current.targetGap)}.`;
    const rows=[['R','shared',current.oldPowers[0],current.R],['DR/M','old middle',current.oldPowers[1],current.oldTerms[1]],['D<sup>2/3</sup>R/M<sup>1/3</sup>','old third',current.oldPowers[2],current.oldTerms[2]],['DR/A₃','quadratic second',current.quadPowers[1],current.quadTerms[1]],['H','target',.75,current.H]];
    $('termRows').replaceChildren(...rows.map(([name,label,power,value])=>{const tr=document.createElement('tr'),nameCell=document.createElement('td'),small=document.createElement('small');nameCell.innerHTML=name;small.textContent=label;nameCell.append(small);tr.append(nameCell);for(const v of [shortPower(power),decimal(value)]){const td=document.createElement('td');td.textContent=v;tr.append(td);}return tr;}));
    for(const [id,value] of [['oldSum',current.oldSum],['quadSum',current.quadSum],['refinedSum',current.refinedSum]])$(id).textContent=decimal(value);
    const geometry=[['A₁ = A₂ = M',decimal(current.A)],['A₃',decimal(current.B)],['A₄ = A₅ = A₆','1'],['H = D^(3/4)',decimal(current.H)],['R = A₁A₂A₃',decimal(current.R)],['A₁A₃ = A₂A₃ = H^(1/3)',decimal(current.A*current.B)],['∏ⱼ Aⱼ^j',decimal(current.capacity)],['A₃ / A₁',decimal(current.B/current.A)]];
    $('geometryValues').replaceChildren(...geometry.map(([name,value])=>{const div=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=name;dd.textContent=value;div.append(dt,dd);return div;}));
    const valid=Math.abs(Math.log(current.capacity/current.H))<1e-10;
    $('capacityStatus').textContent=valid?'Capacity saturated: ∏ⱼ Aⱼ^j = (A₁A₃)³ = H. The complete selected point is admissible at the scale level.':'Capacity check failed; inspect numerical precision.';
    $('capacityStatus').dataset.valid=String(valid);
    $('termLegend').hidden=detail!=='terms';drawPlot(current,detail);
    document.body.dataset.ready='true';
  }
  for(const id of ['aValue','dScale','plotView'])$(id).addEventListener(id==='aValue'?'input':'change',render);
  let frame;const redraw=()=>{cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>drawPlot(current,$('plotView').value));};
  new ResizeObserver(redraw).observe($('exponentPlot'));
  new MutationObserver(redraw).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  render();
}
if(typeof document!=='undefined')init();
