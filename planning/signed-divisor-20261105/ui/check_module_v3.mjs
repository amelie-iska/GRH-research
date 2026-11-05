import assert from'node:assert/strict';
import{webcrypto}from'node:crypto';globalThis.crypto=webcrypto;
import{readFileSync,writeFileSync}from'node:fs';
import{fileURLToPath}from'node:url';
import{resolve,dirname}from'node:path';
import * as M from'../../../web/signed-divisor.mjs';
const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),'../../..'),base=ROOT+'/web/data/signed-divisor/',index=JSON.parse(readFileSync(base+'index-v1.json')),results=[];
assert.equal(await M.sha256(readFileSync(base+'index-v1.json')),M.INDEX_SHA256);
for(const entry of index.cases){const bytes=readFileSync(base+entry.file),d=await M.decodeCase(bytes,entry),a=M.aggregate(d);let states=0;const ids=entry.D===60000?[0,1,23,151,999,3333,7777,12345,16952]:Array.from({length:entry.columns},(_,i)=>i),ds=entry.D===60000?[0,1,25,144,576,999,3333,9999,15000,21749]:Array.from({length:entry.divisors},(_,i)=>i);
for(const di of ds)for(let r=0;r<entry.rows;r++){const v=d.divisors[di];for(let x=0;x<3;x++)for(let y=0;y<3;y++){const state=M.readState(d,{column:ids[(di+r)%ids.length],divisor:di,row:r,x,y});assert.deepEqual(state.Z,v[10].slice(2*(3*x+y),2*(3*x+y)+2));assert.deepEqual(state.rowProduct,M.oMul(state.F[x],M.oConj(state.F[y])));states++;}}
for(let k=0;k<9;k++)assert.deepEqual(a.net[k],d.summary.divisor_budget[d.pairOrder[k]].signed_numerator_omega);
for(const ci of ids)assert(M.findRecords(d.columns,'id:'+ci).includes(ci));
const zero=d.phases.flatMap((row,r)=>row.map((p,c)=>p===null?[r,c]:null).filter(Boolean))[0],one=d.phases.flatMap((row,r)=>row.map((p,c)=>p===0?[r,c]:null).filter(Boolean))[0];assert(zero&&one);assert.deepEqual(M.readState(d,{row:zero[0],column:zero[1]}).rawValue,[0,0]);assert.deepEqual(M.readState(d,{row:one[0],column:one[1]}).rawValue,[1,0]);assert.notDeepEqual(M.restoredZeroF(d,0,zero[0]),M.readState(d,{row:zero[0]}).F);assert.notDeepEqual(M.oAdd(a.even[0],a.odd[0]),a.net[0]);const wrongConj=[4,4];assert.notDeepEqual(M.oMul([4,-4],wrongConj),M.oMul([4,-4],M.oConj([4,-4])));
const tampered=Buffer.from(bytes);tampered[10]^=1;await assert.rejects(()=>M.decodeCase(tampered,entry),/SHA256/);assert.throws(()=>M.validateCase({...d,phases:[]},entry),/Raw phase/);const saved=d.divisors[0][4];d.divisors[0][4]=-saved;assert.throws(()=>M.validateCase(d,entry),/Mobius/);d.divisors[0][4]=saved;
results.push({D:entry.D,passed:true,states,negativeControls:5,zero,one,all9Aggregate:true});}
const value={passed:true,moduleSHA256:await M.sha256(readFileSync(ROOT+'/web/signed-divisor.mjs')),checkerSHA256:await M.sha256(readFileSync(fileURLToPath(import.meta.url))),cases:results};writeFileSync(ROOT+'/outputs/checks/2026-11-05-signed-divisor/ui/module-check-v3.json',JSON.stringify(value,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(value));
