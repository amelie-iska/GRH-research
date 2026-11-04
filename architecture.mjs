import {mountTensorViewport} from './architecture-viewport.mjs';
import {architectureLayout,cellDependencies,coordinateMask,aggregationMode,operationRole,narrative} from './architecture-layout.mjs';
import {architectureCollection} from './surface-bridge-model.mjs';
import {mountSurfaceBridge} from './surface-bridge.mjs';
import {validateTrace,flatTensor,sliceTensor,tropicalWitness,visibleNodes,circuitGroups,covarianceMarginal,clockTrace} from './architecture-model.mjs';
const $=id=>document.getElementById(id),state={trace:null,node:null,manifest:null,nodes:[],leading:[],row:0,col:0,request:0,abort:null,timer:null,yaw:-.45,pitch:.9,hits:[],circuitHits:[],generation:0,loading:true,selectedIndices:null};
const surfaceBridge=mountSurfaceBridge(),collection=architectureCollection(new URLSearchParams(location.search).get('collection'));
const viewport=mountTensorViewport({canvas:$('scene'),state,controls:{range:$('sceneRange'),flat:$('flatView'),zoom:$('zoom'),caption:$('sceneCaption'),lens:$('cellLens')},onSelect:step,onCell:selectSceneCell,onHover:showCellHover});
const text=(id,value)=>$(id).textContent=value;
const fmt=(x,d=4)=>Math.abs(x)<1e-14?'0':Number(x).toPrecision(d).replace(/\.0+(?=e|$)/,'');
const compact=x=>x!==0&&(Math.abs(x)<.001||Math.abs(x)>=1000)?x.toExponential(0):fmt(x,3);
const count=t=>t.shape.reduce((a,b)=>a*b,1);
const defaults=trace=>trace.nodes.find(n=>n.id==='retained_density')??trace.nodes.find(n=>n.id==='source.covariance')??trace.nodes.find(n=>n.id==='proposal')??trace.nodes.find(n=>n.id==='layer0.context')??trace.nodes.find(n=>n.id==='prediction')??trace.nodes.at(-1);
function status(message,error=false){text('loadStatus',message);$('loadStatus').classList.toggle('error',error);}
function pause(){if(state.timer)clearInterval(state.timer);state.timer=null;text('play','Play');$('play').setAttribute('aria-pressed','false');}
function busy(value){state.loading=value;document.querySelector('.workspace').setAttribute('aria-busy',String(value));for(const control of document.querySelectorAll('.workspace button,.workspace input,.workspace select'))control.disabled=value;}
function shape(t){return t.shape.length?'['+t.shape.join(' × ')+']':'scalar';}
async function verifiedJSON(url,hash,signal){
 const response=await fetch(url,{signal});if(!response.ok)throw Error(`Cannot load local record (${response.status})`);
 const bytes=await response.arrayBuffer();
 if(hash){const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),v=>v.toString(16).padStart(2,'0')).join('');if(digest!==hash)throw Error('Record checksum mismatch; reload the manifest');}
 return JSON.parse(new TextDecoder().decode(bytes));
}
async function loadTrace(id,nodeId=null){
 const request=++state.request;state.abort?.abort();state.abort=new AbortController();pause();busy(true);document.body.dataset.ready='loading';status('Loading and checking the selected local record…');
 try{
  let trace,entry;
  if(id==='clock-carrier')trace=clockTrace(Number($('clockDimension').value),Number($('clockTicks').value));
  else{
   entry=state.manifest.traces.find(t=>t.id===id);if(!entry)throw Error('Unknown trace');
   if(!/^records\/[a-zA-Z0-9_-]+\.json$/.test(entry.file))throw Error('Unexpected record path');
   trace=validateTrace(await verifiedJSON(collection.base+entry.file,entry.sha256,state.abort.signal));
  }
  if(request!==state.request)return;
  pause();state.trace=trace;state.generation++;state.yaw=-.45;state.pitch=.9;$('zoom').value=1;$('traceSelect').value=id;$('clockControls').hidden=id!=='clock-carrier';
  const trained=trace.provenance.kind==='trained-checkpoint-replay';
  text('evidenceBadge',trained?'TRAINED CHECKPOINT REPLAY':id==='clock-carrier'?'COMPUTED FINITE CARRIER':'FIXED-WEIGHT REFERENCE');$('evidenceBadge').classList.toggle('reference',!trained);
  text('traceSummary',trace.title+' · '+(trace.provenance.split??'A finite reference pass; no optimizer or hardware run'));
  text('conventions',JSON.stringify({input:trace.input,conventions:trace.conventions,surface:trace.surface_context},null,2));
  text('provenance',JSON.stringify(trace.provenance,null,2));text('checks',JSON.stringify(trace.checks,null,2));
  $('recordLink').href=entry?collection.base+entry.file:collection.manifest;text('recordLink',entry?'Hash-verified raw record':'Saved-record manifest');
  const source=trace.provenance.training_source?.path;
  $('codeLink').href=source?.startsWith('examples/')?'/'+source:'/examples/architecture/README.md';
  const groups=circuitGroups(trace);$('circuitGroup').replaceChildren();
  for(const key of groups.keys()){const option=new Option(key,key);$('circuitGroup').add(option);}
  $('circuitPanel').hidden=groups.size===0;$('photonicPanel').hidden=trace.category!=='photonic-gaussian';
  renderCertificate();
  const requested=trace.nodes.find(n=>n.id===nodeId)??defaults(trace);
  if(requested.id.startsWith('weight.'))$('showWeights').checked=true;
  rebuildList();busy(false);selectNode(requested.id,true);
  status(entry?'SHA-256 verified · '+trace.nodes.length+' numerical tensors · '+Object.keys(trace.checks).length+' recorded checks':'Computed locally from the displayed clock formulas; normalization and Weyl residual checked');
  document.body.dataset.ready='true';
 }catch(error){if(error.name!=='AbortError'&&request===state.request){
  pause();busy(!state.trace);
  if(state.trace){$('traceSelect').value=state.trace.id;if(state.trace.id==='clock-carrier'){$('clockDimension').value=state.trace.input.dimension;$('clockTicks').value=state.trace.input.ticks;}}
  status(error.message+(state.trace?' · Showing previous valid case: '+state.trace.title:''),true);document.body.dataset.ready='error';
 }}
}
function rebuildList(){
 state.nodes=visibleNodes(state.trace,$('showWeights').checked);$('nodeList').replaceChildren();text('stepCount',state.nodes.length);
 for(const node of state.nodes){const button=document.createElement('button');button.dataset.node=node.id;
  button.append(document.createTextNode(node.id));const hint=document.createElement('span');hint.className='tiny-shape';hint.textContent=shape(node.tensor);button.append(hint);
  button.onclick=()=>selectNode(node.id);$('nodeList').append(button);
 }
 const sections=new Map();for(const item of architectureLayout(state.trace,state.nodes).items)if(!sections.has(item.section))sections.set(item.section,item.id);$('stageSelect').replaceChildren(...[...sections].map(([label,id])=>new Option(label,id)));
}
function selectNode(id,initial=false){
 if(state.loading)return;
 const node=state.trace.nodes.find(n=>n.id===id);if(!node)return;
 if(!state.nodes.includes(node)){$('showWeights').checked=true;rebuildList();}
 $('cellTooltip').hidden=true;state.node=node;state.selectedIndices=null;state.leading=[];state.row=0;state.col=0;$('rowStart').value=0;$('columnStart').value=0;
  const story=narrative(state.trace,node);text('walkthroughTitle',story.title);text('walkthroughText',story.sentence);text('walkthroughDetail',story.detail);text('walkthroughStage',architectureLayout(state.trace,state.nodes).byId.get(id)?.section??'NUMERICAL DATAFLOW');
  text('nodeTitle',node.id);text('formula',node.formula+(node.angle!==null&&node.angle!==undefined?` · angle ${node.angle.toPrecision(10)} radians`:''));text('shape',shape(node.tensor)+' · '+node.tensor.axes.join(' / ')+' · '+node.tensor.dtype);
 $('parents').replaceChildren();
 for(const parent of node.inputs){const button=document.createElement('button');button.textContent='← '+parent;button.onclick=()=>selectNode(parent);$('parents').append(button);}
 $('sliceAxes').replaceChildren();
 node.tensor.shape.slice(0,-2).forEach((dimension,axis)=>{
  const label=document.createElement('label');label.textContent=node.tensor.axes[axis];const input=document.createElement('input');input.type='number';input.min=0;input.max=dimension-1;input.value=0;input.dataset.axis=axis;input.setAttribute('aria-label',node.tensor.axes[axis]+' index');
  input.oninput=()=>{state.leading[axis]=Number(input.value);renderNumbers();};label.append(input);$('sliceAxes').append(label);
 });
 if(initial)$('component').value=node.tensor.real?'magnitude':'real';
 for(const button of $('nodeList').children)button.setAttribute('aria-current',String(button.dataset.node===id));
 const activeButton=[...$('nodeList').children].find(b=>b.dataset.node===id);
 if(activeButton){const b=activeButton.getBoundingClientRect(),l=$('nodeList').getBoundingClientRect();if(b.top<l.top)$('nodeList').scrollTop+=b.top-l.top;else if(b.bottom>l.bottom)$('nodeList').scrollTop+=b.bottom-l.bottom;}
 $('stageSelect').value=[...$('stageSelect').options].find(o=>o.textContent===$('walkthroughStage').textContent)?.value??$('stageSelect').value;
 const current=state.nodes.indexOf(node);text('position',`${current+1} / ${state.nodes.length}`);$('previousStep').disabled=current===0;$('nextStep').disabled=current===state.nodes.length-1;
 if(node.gate)$('circuitGroup').value=node.id.split('.')[0];
 const f=flatTensor(node.tensor);let squares=0,min=Infinity,max=-Infinity;
 for(let i=0;i<f.real.length;i++){const abs=Math.hypot(f.real[i],f.imag?.[i]??0);squares+=abs*abs;min=Math.min(min,f.real[i]);max=Math.max(max,f.real[i]);}
 const stateVector=node.tensor.real&&node.tensor.shape.length===1;
 text('tensorFacts',`${f.real.length} elements · real range ${fmt(min)} … ${fmt(max)}`+(stateVector?` · Σ |amplitude|² = ${fmt(squares,10)}`:''));
 renderNumbers();renderScene();renderCircuit();renderCovariance();
 const params=new URLSearchParams(location.search);params.set('trace',state.trace.id);params.set('node',id);history.replaceState(null,'','?'+params);
}
function component(cell){switch($('component').value){case'imag':return cell.imag;case'magnitude':return Math.hypot(cell.real,cell.imag);case'power':return cell.real**2+cell.imag**2;case'phase':return Math.atan2(cell.imag,cell.real);default:return cell.real;}}
function renderNumbers(){
 if(!state.node)return;
 const node=state.node,t=node.tensor,slice=sliceTensor(t,state.leading,state.row,state.col,8);state.slice=slice;
 $('rowStart').max=slice.rows-1;$('columnStart').max=slice.columns-1;
 text('sliceLabel',`${slice.rowAxis} ${slice.rowStart}–${slice.rowStart+slice.cells.length-1} / ${slice.rows}; ${slice.columnAxis} ${slice.columnStart}–${slice.columnStart+slice.cells[0].length-1} / ${slice.columns}`);
 const values=slice.cells.flat().filter(Boolean).map(component),scale=Math.max(...values.map(Math.abs),1e-12);
 $('tensorGrid').style.gridTemplateColumns=`repeat(${slice.cells[0].length},minmax(0,1fr))`;$('tensorGrid').replaceChildren();let first;
 for(const row of slice.cells)for(const cell of row){
  if(!cell){const blank=document.createElement('span');blank.className='blank';$('tensorGrid').append(blank);continue;}
  const button=document.createElement('button'),masked=coordinateMask(state.trace,node,cell.indices),value=component(cell);
  button.dataset.indices=cell.indices.join(',');button.dataset.real=cell.real;button.dataset.imag=cell.imag;button.setAttribute('aria-pressed','false');
  button.title=`[${cell.indices.join(', ')}] = ${cell.real}${cell.imag<0?'':'+'}${cell.imag}i`+(masked?' · '+masked:'');
  const zeroPhase=$('component').value==='phase'&&cell.real===0&&cell.imag===0;
  button.textContent=masked?'masked':zeroPhase?'—':compact(value);button.classList.toggle('masked',Boolean(masked));
  if(zeroPhase)button.title+=' · Phase is undefined at zero magnitude';
  const hue=$('component').value==='phase'?(value+Math.PI)*180/Math.PI:value<0?22:157;
  button.style.backgroundColor=`hsl(${hue} 35% ${90-24*Math.abs(value)/scale}%)`;
  button.onclick=()=>inspectCell(cell,button);$('tensorGrid').append(button);if(!first)first=[cell,button];
 }
 text('colorLegend',`${$('component').selectedOptions[0].textContent}; color scale ${fmt(scale)} for this visible window. Cells are rounded; select for numerical precision. Hatched = invalid/masked, not a zero contribution.`+($('component').value==='phase'?' Dash = undefined phase at zero magnitude.':''));
 if(first)inspectCell(...first);
}
function inspectCell(cell,button){
 for(const b of $('tensorGrid').querySelectorAll('button'))b.setAttribute('aria-pressed',String(b===button));
 const exact=`Coordinate [${cell.indices.join(', ')}]\nReal: ${cell.real.toPrecision(12)}\nImag: ${cell.imag.toPrecision(12)}\n|z|²: ${(cell.real**2+cell.imag**2).toPrecision(12)}`;
 const mask=coordinateMask(state.trace,state.node,cell.indices),w=tropicalWitness(state.trace,state.node,cell.indices);
 let extra=mask?'\n'+mask:'';if(cell.real===0&&cell.imag===0)extra+='\nPhase undefined at zero magnitude.';
 if(w)extra+=w.empty?'\nNo legal key: zero context by the explicit guard':`\nMax-plus witness keys: ${w.keys.join(', ')}\nBest/second margin: ${w.margin===null?'single legal key':w.margin.toPrecision(8)}\nTies are equality of computed floats.`;
 if(state.node.id.endsWith('.moe.dispatch'))extra+='\nDispatch sums over TOKENS for each expert-slot.';
 if(state.node.id.endsWith('.moe.combine'))extra+='\nCombine sums over EXPERT-SLOTS for each valid token.';
 if(state.node.id.split('.').at(-1)==='weights'&&aggregationMode(state.trace,state.node)?.startsWith('tropical'))extra+='\nSoftmax comparison diagnostic; this tropical layer uses max-plus aggregation.';
 state.selectedIndices=[...cell.indices];
 if(operationRole(state.trace,state.node).diagnostic)extra+='\n'+operationRole(state.trace,state.node).reason;
 text('selectedCell',exact+extra);renderCellDependencies(cell.indices);renderScene();
 surfaceBridge.update(state.trace,state.node,cell.indices);
}
function canvasContext(canvas){
 const rect=canvas.getBoundingClientRect(),ratio=Math.min(devicePixelRatio||1,2),width=rect.width,height=rect.height;
 if(!width||!height)return null;
 if(canvas.width!==Math.round(width*ratio)||canvas.height!==Math.round(height*ratio)){canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);}
 const ctx=canvas.getContext('2d');ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,width,height);return {ctx,width,height};
}
function renderScene(){viewport.render();}
function renderCellDependencies(indices){
 const d=cellDependencies(state.trace,state.node,indices);text('dependencyFormula',d.formula);$('dependencyTerms').replaceChildren();
 if(d.verified){
  const table=document.createElement('table');table.className='dependency-table';const header=document.createElement('tr');for(const label of ['Term','Input A','Input B','Real term']){const th=document.createElement('th');th.textContent=label;header.append(th);}table.append(header);
  for(const term of d.terms){const tr=document.createElement('tr');for(const value of [term.label,fmt(term.a,6),fmt(term.b,6),fmt(term.value,7)]){const td=document.createElement('td');td.textContent=value;tr.append(td);}table.append(tr);}$('dependencyTerms').append(table);
  text('dependencyCheck',`Recomputed ${fmt(d.result,12)}${d.actual.imag||d.resultImag?' + '+fmt(d.resultImag,12)+'i':''} · stored ${fmt(d.actual.real,12)}${d.actual.imag?' + '+fmt(d.actual.imag,12)+'i':''} · absolute residual ${d.error.toExponential(2)}. Amber cells on inputs are these exact terms.`);
 }else{
  text('dependencyCheck',d.parents.length?'Recorded tensor dependencies below. The trace does not declare a general cell-index map for this operation; use its formula and full input tensors.':'This is a source / parameter tensor; its literal values are recorded directly.');
  for(const parent of d.parents){const b=document.createElement('button');b.textContent='← '+parent.id+' ['+parent.shape.join(' × ')+']';b.onclick=()=>selectNode(parent.id);$('dependencyTerms').append(b);}
 }
}
function selectSceneCell(hit){
 pause();if(state.node.id!==hit.id)selectNode(hit.id);
 const t=state.node.tensor;state.leading=[...hit.prefix];
 for(const input of $('sliceAxes').querySelectorAll('input'))input.value=state.leading[Number(input.dataset.axis)]??0;
 // The sidebar uses its existing 8-column vector fold; the viewport uses 16.
 if(t.shape.length===1){state.row=Math.floor(hit.indices[0]/Math.min(8,count(t)));state.col=hit.indices[0]%Math.min(8,count(t));}
 else{state.row=hit.indices.at(-2)??0;state.col=hit.indices.at(-1)??0;}
 $('rowStart').value=state.row;$('columnStart').value=state.col;renderNumbers();
 const button=[...$('tensorGrid').querySelectorAll('button')].find(b=>b.dataset.indices===hit.indices.join(','));inspectCell({indices:hit.indices,real:hit.real,imag:hit.imag},button);renderScene();
}
function showCellHover(hit){
 const tooltip=$('cellTooltip');tooltip.hidden=!hit;if(!hit)return;
 const n=state.trace.nodes.find(n=>n.id===hit.id),mask=coordinateMask(state.trace,n,hit.indices);
 tooltip.textContent=hit.id+' ['+hit.indices.join(', ')+'] = '+hit.real.toPrecision(8)+(hit.imag?' '+(hit.imag<0?'−':'+')+' '+Math.abs(hit.imag).toPrecision(6)+'i':'')+(mask?' · masked':'')+(hit.sampled?' · exact sampled coordinate':'');
 tooltip.style.left=Math.max(10,Math.min(hit.screen.x+16,$('scene').clientWidth-270))+'px';tooltip.style.top=Math.max(50,hit.screen.y-25)+'px';
}
function renderCircuit(){
 if($('circuitPanel').hidden||!state.node)return;const groups=circuitGroups(state.trace),key=$('circuitGroup').value,gates=groups.get(key);if(!gates)return;
 const input=state.trace.nodes.find(n=>n.id===key+'.input'),n=Math.round(Math.log2(input.tensor.shape[0])),width=95+gates.length*37+90,height=45+n*37,canvas=$('circuit');
 canvas.style.width=width+'px';canvas.style.height=height+'px';const {ctx}=canvasContext(canvas);state.circuitHits=[];
 ctx.font='11px ui-monospace,monospace';ctx.textBaseline='middle';
 for(let q=0;q<n;q++){const y=28+37*q;ctx.fillStyle='#345149';ctx.fillText('q'+q,5,y);ctx.strokeStyle='#b1c1ad';ctx.beginPath();ctx.moveTo(34,y);ctx.lineTo(width-12,y);ctx.stroke();}
 gates.forEach((gate,index)=>{
  const x=62+index*37,ys=gate.wires.map(q=>28+37*q),active=gate.id===state.node.id;ctx.strokeStyle=active?'#c16b37':'#145e4d';ctx.fillStyle=active?'#c16b37':'#145e4d';ctx.lineWidth=active?2:1;
  if(gate.wires.length===1){ctx.fillStyle=active?'#145e4d':'#e0ead8';ctx.fillRect(x-14,ys[0]-12,28,24);ctx.strokeRect(x-14,ys[0]-12,28,24);ctx.fillStyle=active?'white':'#145e4d';ctx.textAlign='center';ctx.font='9px ui-monospace,monospace';ctx.fillText(gate.gate,x,ys[0]);}
  else{ctx.beginPath();ctx.moveTo(x,ys[0]);ctx.lineTo(x,ys[1]);ctx.stroke();ctx.beginPath();ctx.arc(x,ys[0],4,0,2*Math.PI);ctx.fill();ctx.beginPath();ctx.arc(x,ys[1],gate.gate==='CNOT'?8:4,0,2*Math.PI);gate.gate==='CNOT'?ctx.stroke():ctx.fill();if(gate.gate==='CNOT'){ctx.beginPath();ctx.moveTo(x-8,ys[1]);ctx.lineTo(x+8,ys[1]);ctx.moveTo(x,ys[1]-8);ctx.lineTo(x,ys[1]+8);ctx.stroke();}}
  state.circuitHits.push({id:gate.id,x0:x-18,x1:x+18,y0:Math.min(...ys)-16,y1:Math.max(...ys)+16});
 });
 if(state.trace.input?.retained){ctx.font='9px system-ui';ctx.textAlign='left';for(let q=0;q<n;q++){ctx.fillStyle=q<state.trace.input.retained?'#145e4d':'#a66645';ctx.fillText(q<state.trace.input.retained?'retain':'trace out',width-70,28+37*q);}}
}
function renderCovariance(){
 if($('photonicPanel').hidden||!state.node)return;
 const t=state.node.tensor;
 if(t.shape.length!==2||t.shape[0]!==4||t.shape[1]!==4||!state.node.id.includes('covariance')){text('covarianceCaption','Select a covariance tensor to inspect its Gaussian marginal.');const result=canvasContext($('covariance'));return;}
 const [i,j]=$('quadraturePair').value.split(',').map(Number),m=covarianceMarginal(t,i,j),{ctx,width,height}=canvasContext($('covariance')),scale=Math.min(width,height)*.34/Math.max(m.major,.1),cx=width/2,cy=height/2;
 ctx.strokeStyle='#b5c2af';ctx.beginPath();ctx.moveTo(20,cy);ctx.lineTo(width-20,cy);ctx.moveTo(cx,15);ctx.lineTo(cx,height-15);ctx.stroke();
 ctx.save();ctx.translate(cx,cy);ctx.rotate(-m.angle);ctx.beginPath();ctx.ellipse(0,0,m.major*scale,m.minor*scale,0,0,Math.PI*2);ctx.fillStyle='#cddfbd';ctx.fill();ctx.strokeStyle='#145e4d';ctx.lineWidth=2;ctx.stroke();ctx.restore();
 const labels=['x₀','x₁','p₀','p₁'];ctx.font='12px system-ui';ctx.fillStyle='#345149';ctx.fillText(labels[i],width-25,cy-8);ctx.fillText(labels[j],cx+8,18);
 text('covarianceCaption',`1σ contour of the (${labels[i]}, ${labels[j]}) Gaussian marginal. Covariance [[${fmt(m.a)}, ${fmt(m.b)}], [${fmt(m.b)}, ${fmt(m.c)}]]. Ordering x₀,x₁,p₀,p₁; ℏ=2.`);
}
function renderCertificate(){
 const c=state.trace.certificate;$('certificatePanel').hidden=!c;if(!c)return;
 text('certificateStatus',c.proposal_accepted?'The learned rational trial passed the exact PSD test.':'The learned trial failed; exact rational bisection repaired the lower bound.');
 $('certificateFacts').replaceChildren();
 for(const [label,value] of [['λ',c.lambda_rational],['Learned proposal',c.learned_proposal],['Rational trial',c.rational_trial],['Certified lower',c.certified_lower],['Upper bracket',c.certified_upper_bracket]]){const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=label;dd.textContent=value;$('certificateFacts').append(dt,dd);}
 text('principalMinors',c.principal_minors.map((m,i)=>`${i+1}. ${m}`).join('\n'));
}
function step(delta){if(!state.node||state.loading)return;const i=state.nodes.indexOf(state.node);selectNode(state.nodes[Math.max(0,Math.min(state.nodes.length-1,i+delta))].id);}
$('traceSelect').onchange=()=>loadTrace($('traceSelect').value);
$('showWeights').onchange=()=>{if(!state.trace)return;const current=state.node.id;rebuildList();selectNode(state.nodes.some(n=>n.id===current)?current:state.nodes[0].id);};
$('previousStep').onclick=()=>{pause();step(-1);};$('nextStep').onclick=()=>{pause();step(1);};$('resetStep').onclick=()=>{pause();if(state.nodes.length&&!state.loading)selectNode(state.nodes[0].id);};
$('play').onclick=()=>{
 if(state.timer){pause();return;}if(!state.node||state.loading)return;if(state.nodes.indexOf(state.node)===state.nodes.length-1)selectNode(state.nodes[0].id);
 text('play','Pause');$('play').setAttribute('aria-pressed','true');state.timer=setInterval(()=>{if(state.nodes.indexOf(state.node)===state.nodes.length-1){pause();return;}step(1);},Number($('speed').value));
};$('speed').onchange=()=>{if(state.timer){pause();$('play').click();}};
for(const id of ['clockDimension','clockTicks'])$(id).onchange=()=>loadTrace('clock-carrier');
for(const id of ['component','rowStart','columnStart'])$(id).oninput=()=>{state.row=Number($('rowStart').value);state.col=Number($('columnStart').value);renderNumbers();};
for(const id of ['zoom','flatView','sceneRange','cellLens'])$(id).oninput=()=>{$('cellTooltip').hidden=true;renderScene();};
$('rotateLeft').onclick=()=>{state.yaw-=.2;renderScene();};$('rotateRight').onclick=()=>{state.yaw+=.2;renderScene();};$('resetView').onclick=()=>{state.yaw=-.45;state.pitch=.9;viewport.fit();};
$('overview').onclick=()=>{$('sceneRange').value='all';viewport.fit();};$('focusOperation').onclick=()=>{$('sceneRange').value='window';viewport.fit();};$('fitScene').onclick=()=>viewport.fit();$('panLeft').onclick=()=>viewport.pan(50,0);$('panRight').onclick=()=>viewport.pan(-50,0);$('stageSelect').onchange=()=>selectNode($('stageSelect').value);
document.addEventListener('keydown',e=>{if(e.code==='Space'&&!/INPUT|SELECT|BUTTON|TEXTAREA/.test(e.target.tagName)){e.preventDefault();$('play').click();}});
$('circuitGroup').onchange=renderCircuit;$('quadraturePair').onchange=renderCovariance;
$('circuit').onclick=e=>{const r=$('circuit').getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top,hit=state.circuitHits.find(h=>x>=h.x0&&x<=h.x1&&y>=h.y0&&y<=h.y1);if(hit){pause();selectNode(hit.id);}};
new ResizeObserver(()=>{renderScene();renderCircuit();renderCovariance();}).observe($('scene'));
document.addEventListener('visibilitychange',()=>{if(document.hidden)pause();});
const mobileLayout=matchMedia('(max-width:650px)');$('stepPanel').open=!mobileLayout.matches;mobileLayout.addEventListener('change',e=>$('stepPanel').open=!e.matches);
window.architectureSurface=surfaceBridge;
window.architectureInspector={snapshot:()=>({collection:collection.id,trace:state.trace?.id,node:state.node?.id,shape:state.node?.tensor.shape,generation:state.generation,playing:Boolean(state.timer),loading:state.loading,yaw:state.yaw,zoom:Number($('zoom').value),nodes:state.nodes.length,drawOrder:state.hits.map(h=>({id:h.id,depth:h.depth})),checks:state.trace?.checks,selectedIndices:state.selectedIndices,viewport:viewport.snapshot()}),load:loadTrace,select:selectNode,fit:()=>viewport.fit()};
busy(true);
try{
 if(new URLSearchParams(location.search).has('embed'))document.body.classList.add('embed');
 state.manifest=await verifiedJSON(collection.manifest);$('traceSelect').replaceChildren();
 for(const [kind,label] of [['trained-checkpoint-replay','Trained CPU model replay'],['fixed-weight-reference','Fixed-weight miniature reference']]){
  const group=document.createElement('optgroup');group.label=label;
  for(const entry of state.manifest.traces.filter(t=>t.kind===kind)){const option=new Option(entry.title+' · '+entry.id,entry.id);group.append(option);}$('traceSelect').append(group);
 }
 const group=document.createElement('optgroup');group.label='Live computed carrier';group.append(new Option('Forward clock / shift · adjustable dimension','clock-carrier'));$('traceSelect').append(group);
 const p=new URLSearchParams(location.search),id=p.get('trace');await loadTrace(state.manifest.traces.some(t=>t.id===id)||id==='clock-carrier'?id:state.manifest.traces[0].id,p.get('node'));
}catch(error){status(error.message,true);document.body.dataset.ready='error';}
