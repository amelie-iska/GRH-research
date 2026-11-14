/** Standalone full forward pass for the selected small graph model.
 * Uses JS doubles and an erf approximation; independently checked against
 * stored PyTorch float32 GPU predictions. This is a classical simulation.
 */
import {simulateWeylToken} from './reference.js';

const sum = x => x.reduce((a,b)=>a+b,0);
const dot = (a,b) => sum(a.map((v,i)=>v*b[i]));
const add = (a,b) => a.map((v,i)=>v+b[i]);
const scale = (a,c) => a.map(v=>c*v);
const sigmoid = x => 1/(1+Math.exp(-x));
const softplus = x => Math.max(x,0)+Math.log1p(Math.exp(-Math.abs(x)));
const softmax = x => {const m=Math.max(...x),e=x.map(v=>Math.exp(v-m)),s=sum(e);return e.map(v=>v/s);};
const normalize = a => scale(a,1/Math.max(1e-6,Math.sqrt(dot(a,a))));
function erf(x) {
  // Abramowitz--Stegun 7.1.26: maximum absolute error <1.5e-7.
  const sign=x<0?-1:1, t=1/(1+.3275911*Math.abs(x));
  const poly=(((((1.061405429*t-1.453152027)*t)+1.421413741)*t-.284496736)*t+.254829592)*t;
  return sign*(1-poly*Math.exp(-x*x));
}
const gelu = x => .5*x*(1+erf(x/Math.SQRT2));
function linear(rows,w,b) {return rows.map(row=>w.map((r,j)=>dot(row,r)+b[j]));}
function layerNorm(rows,w,b) {return rows.map(row=>{
  const m=sum(row)/row.length,v=sum(row.map(x=>(x-m)**2))/row.length;
  return row.map((x,j)=>(x-m)/Math.sqrt(v+1e-5)*w[j]+b[j]);
});}

export function encodeGraph(graph) {
  const n=graph.text.length;
  if(!Number.isInteger(n)||n<1||n>12||!Number.isFinite(graph.control))throw Error('Expected a nonempty string of at most12 bytes and finite control.');
  if(!/^[a-d]+$/.test(graph.text))throw Error('This benchmark uses the ASCII alphabet a,b,c,d.');
  const features=[],ends=[],tokenInfo=[];
  for(let i=0;i<=n;i++){
    features.push([1,0,i/12,i/12,0,0,graph.control/2,0]);ends.push([i,i]);tokenInfo.push({kind:'vertex',position:i});
  }
  graph.edges.forEach((e,j)=>{
    if(!Number.isInteger(e.source)||!Number.isInteger(e.target)||e.source<0||e.source>=e.target||e.target>n||!Number.isSafeInteger(e.cost)||!Number.isFinite(e.slope)||e.token!==graph.text.slice(e.source,e.target))throw Error('Invalid token-DAG edge.');
    features.push([0,1,e.source/12,e.target/12,(e.target-e.source)/12,e.cost/32,graph.control/2,e.slope/2]);
    ends.push([e.source,e.target]);tokenInfo.push({kind:'edge',edge_index:j,source:e.source,target:e.target});
  });
  const incidence=ends.map(a=>ends.map(b=>sum(a.flatMap(u=>b.map(v=>+(u===v))))/4));
  return {features,incidence,tokenInfo};
}

function expertLayer(rows,w,prefix) {
  const p=prefix+'.experts',keys=w[p+'.keys'].map(normalize),s=Math.exp(w[p+'.scale']);
  const logits=rows.map(normalize).map(row=>keys.map(key=>s*dot(row,key)));
  const dispatch=rows.map(()=>Array(8).fill(0));
  for(let j=0;j<8;j++){const col=softmax(logits.map(r=>r[j]));col.forEach((v,i)=>dispatch[i][j]=v);}
  const slots=keys.map((_,j)=>rows[0].map((_,k)=>sum(rows.map((r,i)=>dispatch[i][j]*r[k]))));
  const processed=slots.map((slot,j)=>{
    const e=p+'.experts.'+Math.floor(j/2);
    const hidden=linear([slot],w[e+'.0.weight'],w[e+'.0.bias'])[0].map(gelu);
    return linear([hidden],w[e+'.2.weight'],w[e+'.2.bias'])[0];
  });
  const combine=logits.map(softmax),res=w[p+'.residual'];
  const out=combine.map(r=>rows[0].map((_,k)=>res*sum(r.map((v,j)=>v*processed[j][k]))));
  return {out,routing:{dispatch,combine,slots}};
}

function graphBlock(rows,incidence,w,layer) {
  const p='blocks.'+layer,width=rows[0].length,heads=2,hd=width/heads,t=rows.length;
  const normalized=layerNorm(rows,w[p+'.norm1.weight'],w[p+'.norm1.bias']);
  const qkv=linear(normalized,w[p+'.qkv.weight'],w[p+'.qkv.bias']);
  const qs=[],ks=[],vs=[];
  for(let h=0;h<heads;h++){
    const centered=x=>normalize(x.map(v=>v-Math.max(...x)));
    qs.push(qkv.map(x=>centered(x.slice(h*hd,(h+1)*hd))));
    ks.push(qkv.map(x=>centered(x.slice(width+h*hd,width+(h+1)*hd))));
    vs.push(qkv.map(x=>x.slice(2*width+h*hd,2*width+(h+1)*hd)));
  }
  const bias=softplus(w[p+'.incidence_scale']),mix=sigmoid(w[p+'.mix']);
  const scores=qs.map((q,h)=>q.map((v,i)=>ks[h].map((k,j)=>dot(v,k)/Math.sqrt(hd)+bias*incidence[i][j])));
  const weights=scores.map(a=>a.map(softmax));
  const tropical=scores.map((a,h)=>a.map(s=>Array.from({length:hd},(_,k)=>Math.max(...s.map((v,j)=>v+vs[h][j][k])))));
  const merged=Array.from({length:t},(_,i)=>Array.from({length:heads},(_,h)=>Array.from({length:hd},(_,k)=>
    mix*sum(weights[h][i].map((v,j)=>v*vs[h][j][k]))+(1-mix)*tropical[h][i][k])).flat());
  rows=rows.map((r,i)=>add(r,linear([merged[i]],w[p+'.output.weight'],w[p+'.output.bias'])[0]));
  const moe=expertLayer(layerNorm(rows,w[p+'.norm2.weight'],w[p+'.norm2.bias']),w,p);
  rows=rows.map((r,i)=>add(r,moe.out[i]));
  return {rows,detail:{scores,softmax_weights:weights,tropical_context:tropical,softmax_mix:mix,routing:moe.routing}};
}

const roundEven = x => {const a=Math.floor(x),d=x-a;return d===.5?(a%2===0?a:a+1):Math.round(x);};
export function certifyPath(graph,path,potential) {
  const n=graph.text.length;let vertex=0,cost=0,text='',valid=true;
  for(const j of path){const e=graph.edges[j];if(!e||e.source!==vertex){valid=false;break;}vertex=e.target;cost+=e.cost;text+=e.token;}
  valid=valid&&vertex===n&&text===graph.text;
  const dual=potential.length===n+1&&potential.every(Number.isSafeInteger)&&potential[n]===0&&graph.edges.every(e=>potential[e.source]-potential[e.target]<=e.cost);
  return {path_valid:valid,dual_feasible:dual,path_cost_units:cost,lower_bound_units:potential[0],gap_units:cost-potential[0],optimality_certified:valid&&dual&&cost===potential[0]};
}
export function proposePath(graph,prediction) {
  const n=graph.text.length,values=prediction.slice(0,n+1).map(v=>32*v),outgoing=Array.from({length:n+1},()=>[]);
  if(values.length!==n+1||!values.every(Number.isFinite))throw Error('Invalid per-node predictions.');
  values[n]=0;graph.edges.forEach((e,j)=>outgoing[e.source].push(j));
  const choose=(u,costs)=>{if(!outgoing[u].length)throw Error('Every nonterminal vertex must reach the terminal.');return outgoing[u].reduce((best,j)=>graph.edges[j].cost+costs[graph.edges[j].target]<graph.edges[best].cost+costs[graph.edges[best].target]?j:best);};
  const path=[];let u=0;while(u<n){const j=choose(u,values);path.push(j);u=graph.edges[j].target;}
  const potential=values.map(roundEven);potential[n]=0;
  const distances=Array(n+1).fill(0),chosen=Array(n).fill(0);
  for(u=n-1;u>=0;u--){const j=choose(u,potential);potential[u]=Math.min(potential[u],graph.edges[j].cost+potential[graph.edges[j].target]);chosen[u]=choose(u,distances);const e=graph.edges[chosen[u]];distances[u]=e.cost+distances[e.target];}
  const exactPath=[];u=0;while(u<n){const j=chosen[u];exactPath.push(j);u=graph.edges[j].target;}
  const initial=certifyPath(graph,path,potential),final=certifyPath(graph,exactPath,distances);
  return {proposed_path:path,proposal_certificate:initial,proposal_regret_units:initial.path_cost_units-distances[0],repair_required:!initial.optimality_certified,certified_path:initial.optimality_certified?path:exactPath,final_certificate:initial.optimality_certified?initial:final};
}

export function runGraph(graph,weights,thetaOverride=null) {
  if(weights.schema!=='quantum-toricgt-browser-weights-v1'||weights.configuration.mode!=='quantum')throw Error('Expected selected quantum model weights.');
  const w=weights.state_dict,encoded=encodeGraph(graph),theta=thetaOverride??w.theta;
  const angles=linear(encoded.features,w['angle_map.weight'],w['angle_map.bias']).map(row=>row.map(x=>Math.PI*Math.tanh(x)));
  const features=angles.map(a=>simulateWeylToken(a,theta).features);
  let rows=linear(encoded.features,w['input_map.weight'],w['input_map.bias']);
  const lifted=linear(features,w['feature_map.weight'],w['feature_map.bias']);rows=rows.map((r,i)=>add(r,lifted[i]));
  const blocks=[];for(let layer=0;layer<weights.configuration.layers;layer++){const result=graphBlock(rows,encoded.incidence,w,layer);rows=result.rows;blocks.push(result.detail);}
  rows=layerNorm(rows,w['norm.weight'],w['norm.bias']);
  rows=linear(rows,w['readout.0.weight'],w['readout.0.bias']).map(row=>row.map(gelu));
  const predictionsNormalized=linear(rows,w['readout.2.weight'],w['readout.2.bias']).map(r=>r[0]);
  return {predictionsNormalized,predictedDistancesUnits:predictionsNormalized.slice(0,graph.text.length+1).map(x=>32*x),angles,features,tokenInfo:encoded.tokenInfo,blocks,pathResult:proposePath(graph,predictionsNormalized)};
}
