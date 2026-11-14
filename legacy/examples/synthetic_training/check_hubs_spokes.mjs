import assert from 'node:assert/strict';
import {dessinCellModel} from '../../web/hubs-spokes-model.mjs';
for(const m of [3,5,9])for(const filled of [false,true]){
 const a=dessinCellModel(m,filled);assert.equal(a.faces,1);assert.equal(a.cycles[0].length,2*m);assert.equal(a.rank,a.edges-a.vertices+1);assert.equal(a.vertices-a.edges+1,2-2*a.genus);assert.equal(a.euler,2-2*a.genus-(filled?0:1));assert.equal(a.H2,filled?1:0);
 for(let i=0;i<2*m;i++)assert.equal(a.alpha[a.alpha[i]],i);
 assert.equal(a.word.split(' ').length,a.genus);
}
assert.throws(()=>dessinCellModel(4));console.log('Six exact dessin/face cases and unsupported-family negative control pass. Topological consequences have separate prose proofs.');
