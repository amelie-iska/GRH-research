// Original trace-driven layout and cell explanations. Inspired by the interaction
// vocabulary of Brendan Bycroft's MIT-licensed llm-viz; no upstream code/assets.
import {tensorAt,maskReason} from './architecture-model.mjs';
const product=a=>a.reduce((x,y)=>x*y,1);
export function familyOf(trace){
 if(trace.id.includes('continuous-gfn'))return 'gflownet';
 if(trace.id.includes('concept-critic'))return 'critic';
 if(trace.category==='photonic-gaussian')return 'gaussian';
 if(trace.category==='computed-clock')return 'carrier';
 if(trace.nodes.some(n=>/(^|\.)query$/.test(n.id)))return 'attention';
 if(trace.nodes.some(n=>n.gate))return 'quantum';
 return 'dataflow';
}
export function tensorGeometry(t){
 const rank=t.shape.length,total=product(t.shape);
 // Vectors retain exact basis order; long vectors are explicitly folded rows.
 const columns=rank<2?Math.min(16,total):t.shape.at(-1),rows=rank<2?Math.ceil(total/columns):t.shape.at(-2);
 const planes=rank>2?product(t.shape.slice(0,-2)):1;
 const displayColumns=Math.min(columns,32),displayRows=Math.min(rows,24);
 return {rows,columns,planes,total,displayColumns,displayRows,width:Math.max(12,displayColumns*14),height:Math.max(12,displayRows*14),depth:Math.min(32,5+Math.log2(planes)*5),folded:rank===1&&rows>1,lod:rows>24||columns>32};
}
function laneOf(node,family){
 const id=node.id;
 if(id.startsWith('weight.')||['parameters','head','physical_parameters','couplings'].includes(id))return -3;
 if(family==='attention'){
  if(/(^|\.)(q_raw|query)$/.test(id))return -1;
  if(/(^|\.)(k_raw|key)$/.test(id))return 0;
  if(/(^|\.)value$/.test(id))return 1;
  if(/legal|mask|valid/.test(id))return 2;
  if(/residual|layer_output/.test(id))return 2;
  if(/moe.*(dispatch|slots)/.test(id))return -1;
  if(/moe.*(combine|expert)/.test(id))return 1;
  if(/node_logits/.test(id))return -1;
  if(/edge_logits/.test(id))return 1;
 }
 if(family==='quantum'||family==='attention'){
  const patch=id.match(/^patch(\d+)\./);if(patch)return Number(patch[1])-1;
 }
 if(family==='critic'){
  if(id.startsWith('basis.')||id.startsWith('direction_')||id==='intervention')return -1;
  if(id.startsWith('base.'))return -1;
  if(id.startsWith('steered.'))return 1;
  if(id.startsWith('heldout.'))return 2;
 }
 if(family==='gflownet'){
  if(/backward/.test(id))return 1;
  if(/sigma|innovation/.test(id))return -1;
 }
 if(family==='gaussian'&&id.includes('symplectic'))return -1;
 if(/exact_target/.test(id))return 2;
 return 0;
}
function sectionOf(node,family){
 const id=node.id,layer=id.match(/layer(\d+)/);
 if(node.gate)return `${id.split('.')[0]} · ${layer?'unitary layer '+layer[1]:'state preparation / gates'}`;
 if(family==='gflownet')return id.match(/^step\d+/)?.[0]??(id.startsWith('terminal')?'Terminal reward':id.startsWith('trajectory')||id.includes('TB')?'Trajectory balance':'Root / saved path');
 if(family==='critic')return id.startsWith('heldout')||id.startsWith('empirical')?'Held-out evaluation':id.includes('critic')||id.includes('entropy')?'Code critic':id.startsWith('basis')||id.includes('penalty')?'Direction geometry':'Latent intervention';
 if(family==='gaussian')return id.startsWith('trained')?'Trained symplectic pooling':'Gaussian preparation';
 if(layer)return `Layer ${Number(layer[1])+1} · ${/moe/.test(id)?'expert routing':/ff_|hidden|layer_output/.test(id)?'feed-forward / residual':'attention'}`;
 if(/query|key|value|scores|weights|winners|context|legal/.test(id)&&family==='attention')return 'Classical attention on measured features';
 if(/input|token|feature|endpoints|torus/.test(id))return 'Input / encoding';
 if(id.startsWith('weight.')||id==='parameters')return 'Saved parameters';
 return family==='quantum'?'Measurement / retained state':family==='carrier'?'Finite Weyl carrier':'Readout / objective';
}
export function architectureLayout(trace,nodes=trace.nodes){
 const family=familyOf(trace),ranks=new Map(),stages=new Map(),items=[];
 for(const node of nodes){
  const parentRanks=node.inputs.map(p=>ranks.get(p)).filter(x=>x!==undefined);
  const rank=parentRanks.length?Math.max(...parentRanks)+1:0;ranks.set(node.id,rank);
  if(!stages.has(rank))stages.set(rank,[]);stages.get(rank).push(node);
 }
 const maxHeight=Math.max(90,...nodes.map(n=>tensorGeometry(n.tensor).height+65)),stride=maxHeight+40;
 for(const [rank,list] of stages){
  const occupied=new Set();
  for(const node of list){
   let lane=laneOf(node,family);while(occupied.has(lane))lane+=1;occupied.add(lane);
   const geometry=tensorGeometry(node.tensor);
   items.push({id:node.id,node,rank,lane,x:lane*295,y:rank*stride,z:0,...geometry,section:sectionOf(node,family)});
  }
 }
 const byId=new Map(items.map(n=>[n.id,n]));
 return {family,items,byId,links:items.flatMap(n=>n.node.inputs.filter(p=>byId.has(p)).map(p=>({from:p,to:n.id}))),stride};
}
export function neighborhood(layout,id){
 const node=layout.byId.get(id);if(!node)return layout.items;
 const ids=new Set([id,...node.node.inputs]);
 for(const l of layout.links)if(l.from===id)ids.add(l.to);
 return layout.items.filter(n=>ids.has(n.id));
}
export function operationLayout(layout,id){
 const selected=layout.byId.get(id);if(!selected)return layout;
 const items=neighborhood(layout,id),parents=items.filter(n=>selected.node.inputs.includes(n.id)),children=items.filter(n=>n.id!==id&&!selected.node.inputs.includes(n.id));
 const maxWidth=Math.max(140,...items.map(n=>n.width)),maxHeight=Math.max(70,...items.map(n=>n.height));
 const spread=(list,y)=>list.map((n,i)=>({...n,x:(i-(list.length-1)/2)*(maxWidth+85),y,z:0}));
 const focused=[...spread(parents,0),{...selected,x:0,y:maxHeight+115,z:0},...spread(children,2*(maxHeight+115))];
 return {...layout,items:focused,byId:new Map(focused.map(n=>[n.id,n])),links:layout.links.filter(l=>focused.some(n=>n.id===l.from)&&focused.some(n=>n.id===l.to))};
}
export function planeSlices(t,leading=[],limit=3){
 const prefix=t.shape.slice(0,-2).map((d,i)=>Math.max(0,Math.min(d-1,leading[i]??0)));
 const head=t.axes.findIndex(a=>/^heads?$/.test(a));
 if(head<0||head>=prefix.length)return [{prefix,label:prefix.length?prefix.map((v,i)=>`${t.axes[i]} ${v}`).join(' · '):''}];
 const values=Array.from({length:Math.min(t.shape[head],limit)},(_,i)=>i);
 if(!values.includes(prefix[head]))values[values.length-1]=prefix[head];
 return values.map(h=>{const p=[...prefix];p[head]=h;return {prefix:p,label:`head ${h}`};});
}
export function planeCells(t,prefix=[],rowStart=0,colStart=0){
 const g=tensorGeometry(t),r0=Math.max(0,Math.min(g.rows-1,rowStart)),c0=Math.max(0,Math.min(g.columns-1,colStart));
 const rstep=Math.max(1,Math.ceil((g.rows-r0)/24)),cstep=Math.max(1,Math.ceil((g.columns-c0)/32)),cells=[];
 for(let r=r0;r<g.rows;r+=rstep)for(let c=c0;c<g.columns;c+=cstep){
  const indices=t.shape.length===0?[]:t.shape.length===1?[r*g.columns+c]:[...prefix,r,c];
  if(t.shape.length===1&&indices[0]>=g.total)continue;
  cells.push({r,c,indices,...tensorAt(t,indices)});
 }
 return {cells,r0,c0,rstep,cstep,rows:Math.ceil((g.rows-r0)/rstep),columns:Math.ceil((g.columns-c0)/cstep),sampled:rstep>1||cstep>1};
}
export function aggregationMode(trace,node){
 return node.mode??(trace.category==='quantum-tokengt-rg'&&['quantum-tokengt-rg-softmax','quantum-tokengt-rg-tropical','quantum-tokengt-rg-hybrid','quantum-tokengt-rg-classical-hybrid'].includes(trace.id)?trace.id.endsWith('softmax')?'softmax':trace.id.endsWith('tropical')?'tropical':'hybrid':null);
}
export function operationRole(trace,node){
 const mode=aggregationMode(trace,node),tail=node.id.split('.').at(-1);
 if(['winners','block_contexts','block_valid'].includes(tail)&&mode==='softmax')return {diagnostic:true,label:'comparison diagnostic',reason:'This saved max-plus / block witness is a comparison diagnostic; the softmax context uses weights × values.'};
 if(tail==='weights'&&mode?.startsWith('tropical'))return {diagnostic:true,label:'comparison diagnostic',reason:'These softmax weights are a comparison diagnostic; this context aggregates by max-plus.'};
 if(tail==='winners')return {diagnostic:true,label:'witness diagnostic',reason:'The saved winner mask exposes exact floating-point ties; the context is computed directly from scores and values.'};
 return {diagnostic:false,label:'forward operation',reason:''};
}
export function coordinateMask(trace,node,indices){
 const existing=maskReason(trace,node,indices);if(existing)return existing;
 if(['scores','weights'].includes(node.id)){
  const legal=trace.nodes.find(n=>n.id==='legal');if(legal&&indices.length===legal.tensor.shape.length&&!tensorAt(legal.tensor,indices).real)return 'Masked query/key pair; raw value is retained separately';
 }
 return null;
}
export function cellDependencies(trace,node,indices){
 const byId=new Map(trace.nodes.map(n=>[n.id,n])),refs=[],terms=[];
 const ref=(id,ix)=>{const n=byId.get(id);if(!n)return 0;const v=tensorAt(n.tensor,ix);refs.push({id,indices:ix,...v});return v.real;};
 const out=tensorAt(node.tensor,indices),prefix=node.id.includes('.')?node.id.slice(0,node.id.lastIndexOf('.')+1):'',tail=node.id.split('.').at(-1);
 let formula=node.formula,result=null,resultImag=0,verified=false;
 const mode=aggregationMode(trace,node);
 if(node.gate&&indices.length===1&&['RY','RZ','RX','CZ','CNOT'].includes(node.gate)){
  const parent=byId.get(node.inputs[0]),j=indices[0],qubits=Math.round(Math.log2(node.tensor.shape[0])),bit=q=>2**(qubits-1-q),angle=node.angle,c=Math.cos(angle/2),s=Math.sin(angle/2),q=node.wires[0],one=Boolean(j&bit(q));
  const add=(k,cr,ci=0)=>{const value=tensorAt(parent.tensor,[k]);refs.push({id:parent.id,indices:[k],...value});result=(result??0)+cr*value.real-ci*value.imag;resultImag+=cr*value.imag+ci*value.real;terms.push({label:`basis ${k} · Re`,a:value.real,b:cr,value:cr*value.real});if(ci)terms.push({label:`basis ${k} · Im→Re`,a:value.imag,b:-ci,value:-ci*value.imag});};
  if(node.gate==='RY'){add(j,c);add(j^bit(q),one?s:-s);formula=`RY(${angle}): c ψ[j] ${one?'+':'−'} s ψ[j⊕${bit(q)}], c=cos(θ/2), s=sin(θ/2)`;}
  if(node.gate==='RX'){add(j,c);add(j^bit(q),0,-s);formula=`RX(${angle}): c ψ[j] − i s ψ[j⊕${bit(q)}]`;}
  if(node.gate==='RZ'){add(j,c,one?s:-s);formula=`RZ(${angle}): exp(${one?'+':'−'}i θ/2) ψ[j]`;}
  if(node.gate==='CZ'){const sign=one&&(j&bit(node.wires[1]))?-1:1;add(j,sign);formula=`CZ: ψ[j] × ${sign}, from the recorded two wire bits`;}
  if(node.gate==='CNOT'){const k=one?j^bit(node.wires[1]):j;add(k,1);formula=`CNOT: output ψ[${j}] = input ψ[${k}] (qubit 0 most significant)`;}
  verified=true;
 }else if(tail==='scores'&&byId.has(prefix+'query')&&byId.has(prefix+'key')){
  const q=byId.get(prefix+'query'),d=q.tensor.shape.at(-1),qix=indices.slice(0,-1),kix=[...indices.slice(0,-2),indices.at(-1)];
  for(let c=0;c<d;c++){const a=ref(q.id,[...qix,c]),b=ref(prefix+'key',[...kix,c]);terms.push({label:`channel ${c}`,a,b,value:a*b/Math.sqrt(d)});}
  result=terms.reduce((s,t)=>s+t.value,0);formula=`Σc Q[…,q,c] K[…,k,c] / √${d}`;verified=true;
 }else if(tail==='context'&&mode==='softmax'&&byId.has(prefix+'weights')){
  const value=byId.get(prefix+'value'),pre=indices.slice(0,-2),query=indices.at(-2),channel=indices.at(-1);
  for(let k=0;k<value.tensor.shape.at(-2);k++){const a=ref(prefix+'weights',[...pre,query,k]),b=ref(value.id,[...pre,k,channel]);terms.push({label:`key ${k}`,a,b,value:a*b});}
  result=terms.reduce((s,t)=>s+t.value,0);formula='Σk weight[…,q,k] × V[…,k,c]';verified=true;
 }else if(tail==='context'&&mode?.startsWith('tropical')&&byId.has(prefix+'legal')){
  const v=byId.get(prefix+'value'),pre=indices.slice(0,-2),q=indices.at(-2),c=indices.at(-1);
  for(let k=0;k<v.tensor.shape.at(-2);k++)if(tensorAt(byId.get(prefix+'legal').tensor,[...pre,q,k]).real){const a=ref(prefix+'scores',[...pre,q,k]),b=ref(v.id,[...pre,k,c]);terms.push({label:`legal key ${k}`,a,b,value:a+b});}
  result=terms.length?Math.max(...terms.map(t=>t.value)):0;formula='max legal k (score[…,q,k] + V[…,k,c])';verified=true;
 }else if(tail==='context'&&mode==='hybrid'&&byId.has(prefix+'weights')&&byId.has(prefix+'legal')){
  const v=byId.get(prefix+'value'),pre=indices.slice(0,-2),q=indices.at(-2),c=indices.at(-1);let soft=0;
  for(let k=0;k<v.tensor.shape.at(-2);k++)if(tensorAt(byId.get(prefix+'legal').tensor,[...pre,q,k]).real){const a=ref(prefix+'scores',[...pre,q,k]),b=ref(v.id,[...pre,k,c]),weight=ref(prefix+'weights',[...pre,q,k]);terms.push({label:`max-plus key ${k}`,a,b,value:a+b});soft+=weight*b;}
  result=.5*(soft+(terms.length?Math.max(...terms.map(t=>t.value)):0));formula='½ (Σ legal k weight[q,k] V[k,c] + max legal k (score[q,k] + V[k,c])); empty = 0';verified=true;
 }else if(tail==='weights'&&byId.has(prefix+'scores')&&byId.has(prefix+'legal')){
  const score=byId.get(prefix+'scores'),legal=byId.get(prefix+'legal'),pre=indices.slice(0,-1),entries=[];
  for(let k=0;k<score.tensor.shape.at(-1);k++)if(tensorAt(legal.tensor,[...pre,k]).real)entries.push({k,value:ref(score.id,[...pre,k])});
  const max=entries.length?Math.max(...entries.map(e=>e.value)):0,denom=entries.reduce((s,e)=>s+Math.exp(e.value-max),0),entry=entries.find(e=>e.k===indices.at(-1));
  result=entry?Math.exp(entry.value-max)/denom:0;for(const e of entries)terms.push({label:`legal key ${e.k}`,a:e.value,b:max,value:Math.exp(e.value-max)});
  formula='exp(score[q,k] − max legal score) / Σ legal j exp(score[q,j] − max); masked or empty = 0';verified=true;
 }else if(['residual','layer_output','delta','prediction_error','single_code_objective'].includes(tail)&&node.inputs.length===2){
  const parents=node.inputs.map(id=>byId.get(id));
  if(parents.every(p=>p&&JSON.stringify(p.tensor.shape)===JSON.stringify(node.tensor.shape))){
   const a=ref(parents[0].id,indices),b=ref(parents[1].id,indices),subtract=['delta','prediction_error'].includes(tail);result=subtract?tail==='delta'?b-a:a-b:a+b;
   terms.push({label:subtract?'difference':'sum',a,b,value:result});verified=true;
  }
 }
 return {formula,refs,terms,result,resultImag,verified,error:verified?Math.hypot(result-out.real,resultImag-out.imag):null,actual:out,parents:node.inputs.map(id=>({id,shape:byId.get(id)?.tensor.shape}))};
}
export function narrative(trace,node){
 const family=familyOf(trace),g=tensorGeometry(node.tensor),role=operationRole(trace,node),mode=aggregationMode(trace,node);
 let sentence=node.gate?`Apply ${node.gate} on wire${node.wires.length>1?'s':''} ${node.wires.join(', ')}. The solid stores the output amplitudes in the recorded basis order.`:
 /(^|\.)scores$/.test(node.id)?'Each query meets every key. Select a score cell to see its channel-by-channel dot product.':
 /(^|\.)context$/.test(node.id)?(mode?.startsWith('tropical')?'For each output coordinate, compare score + value over legal keys. Exact floating-point ties remain visible.':'Inspect the stored context and its declared aggregation rule; measured quantum features feed a classical operation.'):
 /moe/.test(node.id)?'Routing tensors retain their actual token, expert and slot axes. Dispatch and combination normalize along different axes.':
 family==='gaussian'?'Follow covariance transport through the stored symplectic matrices. These are quadratures and second moments, not token attention.':
 family==='gflownet'?'Follow the saved continuous trajectory, forward/backward densities and terminal physical reward. No new path is sampled.':
 family==='critic'?'Follow the saved latent intervention and trained code critic. Held-out estimates retain their recorded statistical scope.':
 'Follow the highlighted incoming dependencies, then inspect an individual stored coordinate.';
 if(role.diagnostic)sentence=role.reason+' '+sentence;
 return {title:node.gate?`${node.gate} · wire ${node.wires.join(', ')}`:node.id.replaceAll('_',' '),sentence,detail:`${role.diagnostic?role.label+' · ':''}${g.total.toLocaleString()} literal elements · ${node.inputs.length} recorded inputs${g.planes>1?` · ${g.planes} leading-axis planes`:''}`};
}
