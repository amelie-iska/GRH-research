import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {staircase,standard,rankMap,cwAt,specialized,flagComplex,inclusionRanks,gfRank,kernel} from '../web/persistence-model.mjs';
for(const gens of [[[2,0],[1,1],[0,2]],[[3,0],[2,1],[1,2],[0,3]],[[5,0],[3,1],[1,3],[0,5]]]){
 const m=staircase(gens);assert.equal(m.betti[1].length,gens.length);assert.equal(m.betti[2].length,gens.length-1);
 for(let a=0;a<=7;a++)for(let b=0;b<=7;b++){
  const cw=cwAt(m,[a,b]);assert.equal(cw.h1,Number(standard(m,[a,b])));assert.equal(cw.h2,m.betti[2].filter(([x,y])=>x<=a&&y<=b).length);
  assert.equal(rankMap(m,[a,b],[a,b]),cw.h1);
 }
 assert.deepEqual(specialized(m,0,0).homology,[1,gens.length,gens.length-1]);
 for(const p of [[1,0],[0,1],[1,1]])assert.deepEqual(specialized(m,...p).homology,[0,0,0]);
}
assert.throws(()=>staircase([[2,0],[3,1],[0,2]]));assert.throws(()=>rankMap(staircase([[2,0],[0,2]]),[1,0],[0,1]));
assert.equal(gfRank([3n,5n,6n]),2);assert.equal(kernel([3n,5n,6n]).length,1);
const manifest=JSON.parse(readFileSync('web/data/persistence/manifest.json'));const data=JSON.parse(readFileSync('web/data/persistence/'+manifest.file));
for(const channel of ['input','output']){
 const a=flagComplex(data,channel,400,500),b=flagComplex(data,channel,800,1000);
 const r=inclusionRanks(a,b);assert(r.h0<=a.betti[0]&&r.h1<=a.betti[1]);
 assert.deepEqual(inclusionRanks(a,a),{h0:a.betti[0],h1:a.betti[1]});
}
const emptyData={points:[{id:0,birth:2}],input_labels:[[0]],output_labels:[[0]]},empty=flagComplex(emptyData,'input',0,0);assert.deepEqual(empty.betti,[0,0]);assert.deepEqual(inclusionRanks(empty,empty),{h0:0,h1:0});assert.deepEqual(inclusionRanks(empty,flagComplex(emptyData,'input',0,2)),{h0:0,h1:0});
const cycle=flagComplex(data,'input',400,500);assert.equal(cycle.betti[1],1);
assert.equal(inclusionRanks(cycle,flagComplex(data,'input',600,500)).h1,1);
assert.equal(inclusionRanks(cycle,flagComplex(data,'input',800,1000)).h1,0);
let maps=0;
for(const r of [0,200,400,600,800,1000])for(const e of [0,500,1000]){
 const input=flagComplex(data,'input',r,e),output=flagComplex(data,'output',r,e);inclusionRanks(input,output);
 for(const s of [r,1000])for(const f of [e,1000]){inclusionRanks(input,flagComplex(data,'input',s,f));maps++;}
}
console.log(JSON.stringify({passed:true,quantum_maps:maps,nontrivial_H1_birth_persistence_death:true,staircase_CW_and_fiber:true}));
