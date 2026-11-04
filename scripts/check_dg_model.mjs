import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {gfRank} from '../web/persistence-model.mjs';
import {windowModel,thetaExt} from '../web/dg-model.mjs';
for(const N of [0,1,3,6])for(const mode of ['node','unit','zero']){
 const m=windowModel(mode,N),index=new Map(m.even.map((p,i)=>[p.join(','),i]));assert.equal(gfRank(m.arrows.map(([,p])=>1n<<BigInt(index.get(p.join(','))))),m.rank);assert.equal(m.even.length,(N+1)**2);
 if(mode==='node'){assert.equal(m.odd.length,N*N);assert.deepEqual(m.homology,[0,2*N+1]);}
 if(mode==='unit')assert.deepEqual(m.homology,[0,0]);
 if(mode==='zero')assert.deepEqual(m.homology,[(N+1)**2,(N+1)**2]);
 for(const [from,to] of m.arrows){assert.equal(from[2],-1);assert.equal(to[2],0);assert.equal(from[0]-from[1],to[0]-to[1]);}
}
const data=JSON.parse(readFileSync('web/data/dg/theta.json'));
for(const kind of ['elliptic','spherical'])for(let n=0;n<=12;n++)assert.deepEqual(thetaExt(kind,n),data[kind].ext_dimensions[n]);
assert.throws(()=>windowModel('node',-1));assert.throws(()=>thetaExt('unknown',1));
console.log(JSON.stringify({passed:true,windows:12,theta_matrices:26,chain_weights_equal:true}));
