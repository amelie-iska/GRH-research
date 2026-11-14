// Original numerical inspection helpers. No DOM, training or external runtime.
const flatCache=new WeakMap();
const product=shape=>shape.reduce((a,b)=>a*b,1);
function flatten(a){return Array.isArray(a)?a.flat(Infinity):[a];}
export function flatTensor(t){
 if(!flatCache.has(t))flatCache.set(t,{real:flatten(t.real??t.values).map(Number),imag:t.imag?flatten(t.imag):null});
 return flatCache.get(t);
}
export function validateTrace(trace){
 if(trace.schema_version!==1||!Array.isArray(trace.nodes)||!trace.nodes.length)throw Error('Unsupported or empty trace');
 if(!['trained-checkpoint-replay','fixed-weight-reference','computed-carrier'].includes(trace.provenance?.kind))throw Error('Missing evidence category');
 const seen=new Set();
 const walk=(a,shape)=>shape.length?Array.isArray(a)&&a.length===shape[0]&&a.every(x=>walk(x,shape.slice(1))):typeof a==='boolean'||typeof a==='number'&&Number.isFinite(a);
 for(const n of trace.nodes){
  const t=n.tensor;
  if(seen.has(n.id)||!n.inputs.every(id=>seen.has(id)))throw Error('Invalid dependency graph');
  if(!Array.isArray(t.shape)||t.shape.some(d=>!Number.isInteger(d)||d<1)||t.axes?.length!==t.shape.length)throw Error('Invalid tensor shape/axes');
  if(!walk(t.real??t.values,t.shape)||t.imag&&!walk(t.imag,t.shape))throw Error('Tensor dimensions or finite values disagree');
  seen.add(n.id);
 }
 return trace;
}
export function tensorAt(t,indices){
 if(indices.length!==t.shape.length||indices.some((i,k)=>!Number.isInteger(i)||i<0||i>=t.shape[k]))throw Error('Tensor coordinate outside shape');
 let index=0;for(let k=0;k<indices.length;k++)index=index*t.shape[k]+indices[k];
 const f=flatTensor(t);return {real:f.real[index],imag:f.imag?.[index]??0,index};
}
const integer=(x,lo,hi)=>Math.min(hi,Math.max(lo,Number.isFinite(Number(x))?Math.floor(Number(x)):lo));
export function sliceTensor(t,leading=[],rowStart=0,columnStart=0,limit=8){
 const rank=t.shape.length,n=product(t.shape),cols=rank<2?Math.min(8,n):t.shape.at(-1),rows=rank<2?Math.ceil(n/cols):t.shape.at(-2);
 const prefix=t.shape.slice(0,-2).map((d,k)=>integer(leading[k]??0,0,d-1));
 const r0=integer(rowStart,0,rows-1),c0=integer(columnStart,0,cols-1),height=Math.min(limit,rows-r0),width=Math.min(limit,cols-c0);
 const cells=Array.from({length:height},(_,r)=>Array.from({length:width},(_,c)=>{
  const indices=rank===0?[]:rank===1?[(r+r0)*cols+c+c0]:[...prefix,r+r0,c+c0];
  if(rank===1&&indices[0]>=n)return null;
  return {indices,...tensorAt(t,indices)};
 }));
 return {cells,rows,columns:cols,rowStart:r0,columnStart:c0,leading:prefix,total:n,
  rowAxis:rank<2?'basis row':t.axes.at(-2),columnAxis:rank<2?'basis column':t.axes.at(-1)};
}
function nodeById(trace,id){return trace.nodes.find(n=>n.id===id);}
export function maskReason(trace,node,indices){
 const prefix=node.id.split('.')[0];
 if(/\.(scores|weights)$/.test(node.id)){
  const mask=nodeById(trace,prefix+'.legal');
  if(mask&&tensorAt(mask.tensor,indices).real===0)return 'Masked query/key pair; raw value is retained separately';
 }
 if(node.id.endsWith('.block_contexts')){
  const valid=nodeById(trace,prefix+'.block_valid');
  if(valid&&tensorAt(valid.tensor,indices.slice(0,4)).real===0)return 'No legal key in this block; stored zero is not a maximum';
 }
 return null;
}
export function tropicalWitness(trace,node,indices){
 if(!node.id.endsWith('.context')||node.mode==='softmax'||indices.length!==4)return null;
 const prefix=node.id.split('.')[0];
 const score=nodeById(trace,prefix+'.scores'),value=nodeById(trace,prefix+'.value'),legal=nodeById(trace,prefix+'.legal');
 if(!score||!value||!legal)return null;
 const [b,h,q,c]=indices,terms=[];
 for(let k=0;k<value.tensor.shape[2];k++)if(tensorAt(legal.tensor,[b,h,q,k]).real){
  terms.push({key:k,value:tensorAt(score.tensor,[b,h,q,k]).real+tensorAt(value.tensor,[b,h,k,c]).real});
 }
 if(!terms.length)return {keys:[],margin:null,terms:[],empty:true};
 terms.sort((a,b)=>b.value-a.value||a.key-b.key);
 return {keys:terms.filter(t=>t.value===terms[0].value).map(t=>t.key),margin:terms.length>1?terms[0].value-terms[1].value:null,terms,empty:false};
}
export function visibleNodes(trace,showWeights=false){return trace.nodes.filter(n=>showWeights||!n.id.startsWith('weight.'));}
export function circuitGroups(trace){
 const groups=new Map();
 for(const node of trace.nodes)if(node.gate){const key=node.id.split('.')[0];if(!groups.has(key))groups.set(key,[]);groups.get(key).push(node);}
 return groups;
}
export function covarianceMarginal(t,i,j){
 if(t.shape.length!==2||t.shape[0]!==4||t.shape[1]!==4)throw Error('Expected a four-quadrature covariance');
 const a=tensorAt(t,[i,i]).real,b=tensorAt(t,[i,j]).real,c=tensorAt(t,[j,j]).real;
 const delta=Math.hypot(a-c,2*b),angle=.5*Math.atan2(2*b,a-c);
 return {major:Math.sqrt(Math.max(0,(a+c+delta)/2)),minor:Math.sqrt(Math.max(0,(a+c-delta)/2)),angle,a,b,c};
}
function complexMatrix(real,imag){return {shape:[real.length,real[0].length],axes:['row','column'],dtype:'complex128',real,imag};}
function mv(a,z){
 return a.real.map((row,i)=>row.reduce((sum,r,j)=>{const im=a.imag[i][j];return {r:sum.r+r*z[j].r-im*z[j].i,i:sum.i+r*z[j].i+im*z[j].r};},{r:0,i:0}));
}
export function clockTrace(d=4,ticks=1){
 if(!Number.isInteger(d)||d<3||d>16||!Number.isInteger(ticks)||ticks<0||ticks>16)throw Error('Clock dimension/ticks outside supported range');
 const zero=()=>Array.from({length:d},()=>Array(d).fill(0)),ur=zero(),ui=zero(),vr=zero(),vi=zero();
 for(let j=0;j<d;j++){ur[j][j]=Math.cos(2*Math.PI*j/d);ui[j][j]=Math.sin(2*Math.PI*j/d);vr[(j+1)%d][j]=1;}
 const U=complexMatrix(ur,ui),V=complexMatrix(vr,vi),nodes=[];
 const add=(id,tensor,formula,inputs=[])=>nodes.push({id,tensor,formula,inputs});
 add('U',U,'U e_j = exp(2 pi i j/d) e_j');add('V',V,'Forward shift V e_j = e_(j+1 mod d)');
 let z=Array.from({length:d},(_,j)=>({r:Math.exp(-(Math.min(j,d-j)**2)/2),i:0}));
 const norm=Math.sqrt(z.reduce((s,x)=>s+x.r*x.r,0));z=z.map(x=>({r:x.r/norm,i:0}));
 const state=()=>({shape:[d],axes:['basis'],dtype:'complex128',real:z.map(x=>x.r),imag:z.map(x=>x.i)});
 add('state.input',state(),'Normalized finite periodic packet');let previous='state.input';
 for(let k=0;k<ticks;k++)for(const [name,operator] of [['U',U],['V',V]]){
  z=mv(operator,z);const id=`tick${k}.${name}`;add(id,state(),`${name} applied to the actual carrier state`,[previous,name]);previous=id;
 }
 let residual=0;
 const omega={r:Math.cos(2*Math.PI/d),i:Math.sin(2*Math.PI/d)};
 for(let j=0;j<d;j++){
  const k=(j+1)%d,a={r:ur[k][k],i:ui[k][k]},b={r:omega.r*ur[j][j]-omega.i*ui[j][j],i:omega.i*ur[j][j]+omega.r*ui[j][j]};
  residual=Math.max(residual,Math.hypot(a.r-b.r,a.i-b.i));
 }
 const error=Math.abs(z.reduce((s,x)=>s+x.r*x.r+x.i*x.i,0)-1);
 return validateTrace({schema_version:1,id:'clock-carrier',title:'Computed finite forward clock / shift',category:'computed-clock',
  provenance:{kind:'computed-carrier',backend:'Exact formulas evaluated locally in JavaScript float64; no training or hardware',scope:'Finite carrier, not a faithful formal-DVR order representation or arithmetic operator'},
  conventions:{weyl:'UV = omega VU; V is forward. The trained Harper trace uses backward V instead.',basis:'j = 0,...,d-1'},
  input:{dimension:d,ticks},nodes,checks:{weyl:{error:residual,tolerance:1e-10},state_norm:{error,tolerance:1e-10}}});
}
