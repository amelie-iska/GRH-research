import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {architectureLayout,familyOf,tensorGeometry,planeCells,planeSlices,cellDependencies,operationRole,narrative,neighborhood} from '../../web/architecture-layout.mjs';
import {validateTrace,tensorAt,clockTrace,visibleNodes} from '../../web/architecture-model.mjs';
const report={cases:[],hashes:{},coordinates:0,formulas:0};
for(const base of ['architecture','rg','quantum-tokengt']){
 const path='web/data/'+base+'/',manifest=JSON.parse(readFileSync(path+'manifest.json'));
 report.hashes[path+'manifest.json']=createHash('sha256').update(readFileSync(path+'manifest.json')).digest('hex');
 for(const entry of manifest.traces){
  const bytes=readFileSync(path+entry.file),hash=createHash('sha256').update(bytes).digest('hex');assert.equal(hash,entry.sha256);report.hashes[path+entry.file]=hash;
  const trace=validateTrace(JSON.parse(bytes)),nodes=visibleNodes(trace),layout=architectureLayout(trace,nodes);assert.equal(layout.items.length,nodes.length);for(const n of nodes)assert(narrative(trace,n).sentence);
  if(trace.id==='tokengt-softmax'){assert(operationRole(trace,nodes.find(n=>n.id==='layer0.winners')).diagnostic);assert(!operationRole(trace,nodes.find(n=>n.id==='layer0.weights')).diagnostic);}
  if(trace.id==='tropical-ring'){assert(operationRole(trace,nodes.find(n=>n.id==='layer0.weights')).diagnostic);assert(!operationRole(trace,nodes.find(n=>n.id==='layer0.context')).diagnostic);}
  assert.equal(new Set(layout.items.map(n=>n.id)).size,nodes.length);
  for(const l of layout.links)assert(layout.byId.get(l.to).rank>layout.byId.get(l.from).rank);
  for(const item of layout.items){
   assert(item.width>0&&item.height>0&&Number.isFinite(item.x+item.y));
   for(const other of layout.items)if(other!==item&&other.rank===item.rank)assert(Math.abs(other.x-item.x)>(item.width+other.width)/2,'Tensor solids overlap in one stage');
   for(const plane of planeSlices(item.node.tensor))for(const c of planeCells(item.node.tensor,plane.prefix).cells){
    const direct=tensorAt(item.node.tensor,c.indices);assert.equal(c.real,direct.real);assert.equal(c.imag,direct.imag);report.coordinates++;
    const d=cellDependencies(trace,item.node,c.indices);if(d.verified){assert(d.error<1e-8,`${trace.id}/${item.id}: residual ${d.error}`);report.formulas++;}
   }
  }
  for(const node of nodes)assert(neighborhood(layout,node.id).some(n=>n.id===node.id));
  if(familyOf(trace)==='attention'){
   const q=layout.items.find(n=>/(^|\.)query$/.test(n.id)),k=layout.items.find(n=>/(^|\.)key$/.test(n.id)),v=layout.items.find(n=>/(^|\.)value$/.test(n.id));assert(q.x<k.x&&k.x<v.x,'QKV lanes must stay ordered');
  }
  report.cases.push({id:trace.id,family:layout.family,nodes:nodes.length});
 }
}
const small={shape:[2,3],axes:['row','column'],values:[[1,2,3],[4,5,6]]};assert.equal(planeCells(small).cells.length,6);assert.equal(tensorGeometry(small).width/tensorGeometry(small).height,1.5);
const large={shape:[60,64],axes:['row','column'],values:Array.from({length:60},(_,r)=>Array.from({length:64},(_,c)=>r*64+c))};const lod=planeCells(large);assert(lod.sampled);assert(lod.rows<=24&&lod.columns<=32);assert(lod.cells.every(c=>c.real===c.r*64+c.c));
const clock=clockTrace(8,4);assert.equal(familyOf(clock),'carrier');assert.equal(architectureLayout(clock).items.length,clock.nodes.length);
report.passed=true;writeFileSync('outputs/checks/2026-11-03-reference-inspector/layout-numerics.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,cases:report.cases.length,coordinates:report.coordinates,formulas:report.formulas}));
