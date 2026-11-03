import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {validateTrace,sliceTensor,tensorAt,maskReason,tropicalWitness,clockTrace} from '../web/architecture-model.mjs';
const manifest=JSON.parse(readFileSync('web/data/architecture/manifest.json'));
let cases=0;
for(const entry of manifest.traces){
 const trace=JSON.parse(readFileSync('web/data/architecture/'+entry.file));validateTrace(trace);
 for(const node of trace.nodes){
  const t=node.tensor,s=sliceTensor(t,[],0,0,8);
  assert(s.cells.length>0);
  for(const row of s.cells)for(const cell of row)if(cell){
   let ref=t.real??t.values,imag=t.imag;
   for(const i of cell.indices){ref=ref[i];if(imag)imag=imag[i];}
   assert.equal(cell.real,typeof ref==='boolean'?Number(ref):ref);assert.equal(cell.imag,imag??0);
  }
 }
 cases++;
}
const base={schema_version:1,id:'test',provenance:{kind:'fixed-weight-reference'},nodes:[{id:'x',inputs:[],tensor:{shape:[2],axes:['i'],values:[1,2]}}]};
assert.throws(()=>validateTrace({...base,nodes:[{...base.nodes[0],inputs:['missing']}]}));
assert.throws(()=>validateTrace({...base,nodes:[{...base.nodes[0],tensor:{shape:[3],axes:['i'],values:[1,2]}}]}));
assert.throws(()=>validateTrace({...base,nodes:[{...base.nodes[0],tensor:{shape:[2],axes:['i'],values:[NaN,2]}}]}));
const vector={shape:[19],axes:['basis'],values:Array.from({length:19},(_,i)=>i)};
const tail=sliceTensor(vector,[],2,0,8);assert.equal(tail.cells[0][2].real,18);assert.equal(tail.cells[0][3],null);
assert.throws(()=>tensorAt(vector,[19]));
const ring=JSON.parse(readFileSync('web/data/architecture/'+manifest.traces.find(t=>t.id==='tropical-ring').file));
const blocks=ring.nodes.find(n=>n.id==='layer0.block_contexts');
assert(maskReason(ring,blocks,[0,0,0,3,0])); // padded query
const context=ring.nodes.find(n=>n.id==='layer0.context');
const w=tropicalWitness(ring,context,[0,0,0,0]);assert(w.keys.length>=1&&w.margin>=0);
const scores=ring.nodes.find(n=>n.id==='layer0.scores');assert(maskReason(ring,scores,[0,0,3,0]));
for(const d of [3,4,5,8,12])for(const ticks of [0,1,7,16]){
 const trace=clockTrace(d,ticks);validateTrace(trace);
 assert(trace.checks.weyl.error<1e-10);assert(trace.checks.state_norm.error<1e-10);
 const state=trace.nodes.at(-1).tensor;
 assert.equal(state.shape[0],d);
}
assert.throws(()=>clockTrace(1,1));assert.throws(()=>clockTrace(4,-1));
console.log(JSON.stringify({passed:true,cases,all_exported_tensors_indexed:true,clock_cases:20,masks_and_ties:true}));
