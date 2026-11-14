// Dependency-free exact combinatorics and saved-record crosswalk checks.
import assert from 'node:assert/strict';
import {readFileSync,mkdirSync,writeFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {dessin,permutation,surfaceProfile,selectionMapping,relationAudit,checkRepresentation,oddDessin,architectureCollection} from '../../web/surface-bridge-model.mjs';
import {clockTrace,validateTrace} from '../../web/architecture-model.mjs';
const manifest=JSON.parse(readFileSync('web/data/architecture/manifest.json'));
const records=manifest.traces.map(e=>{const b=readFileSync('web/data/architecture/'+e.file);assert.equal(createHash('sha256').update(b).digest('hex'),e.sha256);return JSON.parse(b);});
let nodes=0,relations=0;const summaries=[];
for(const trace of [...records,clockTrace(7,2)]){
 const p=surfaceProfile(trace),d=p.d;
 for(const a of d.arrows){assert.equal(a.target,d.arrows[a.forbidden].source);assert.equal(a.target,d.arrows[a.permitted].source);const audit=relationAudit(d,a.dart);assert.equal(audit.failures,0);relations+=audit.checked;}
 for(const node of trace.nodes){
  for(const indices of [node.tensor.shape.map(()=>0),node.tensor.shape.map(n=>n-1)]){
   const m=selectionMapping(trace,node,indices);assert(m.edges.every(e=>e>=0&&e<d.edges.length));assert(m.arrows.every(a=>a>=0&&a<d.arrows.length));
  }nodes++;
 }
 summaries.push({id:trace.id,kind:p.kind,genus:d.genus,edges:d.edges.length,arrows:d.arrows.length,rank:d.rank,passport:d.passport});
}
const square=surfaceProfile(records.find(t=>t.id==='qcnn-4-0'));assert.equal(square.d.edges.length,2);assert.equal(square.d.arrows.length,4);assert.equal(square.d.rank,16);assert.equal(square.d.genus,1);
const nine=surfaceProfile(records.find(t=>t.id==='qcnn-9-0'));assert.equal(nine.d.edges.length,9);assert.equal(nine.d.genus,4);assert.equal(nine.d.rank,162);assert.equal(nine.d.faces.length,1);
const token=records.find(t=>t.id==='tokengt-softmax'),scores=token.nodes.find(n=>n.id==='layer0.scores');
assert.deepEqual(selectionMapping(token,scores,[0,0,0,1]).edges,[0,2]);
assert.deepEqual(selectionMapping(token,scores,[0,0,3,3]).edges,[],'Padding must not acquire an edge');
for(const t of [0,1,2]){
 const context=token.nodes.find(n=>n.id==='tokens'),m=selectionMapping(token,context,[0,t+4,0]),a=surfaceProfile(token).d.arrows[m.arrows[0]];
 const endpoints=token.nodes.find(n=>n.id==='endpoints').tensor.values[t],relabel=[0,2,1];assert.equal(a.source,relabel[endpoints[0]]);assert.equal(a.target,relabel[endpoints[1]]);
}
const q=records.find(t=>t.id==='qcnn-9-0'),gate=q.nodes.find(n=>n.gate==='CZ');assert.deepEqual(selectionMapping(q,gate,[0]).edges,gate.wires);
const photon=records.find(t=>t.id==='photonic-0'),cov=photon.nodes.find(n=>n.id==='source.covariance');assert.deepEqual(selectionMapping(photon,cov,[2,3]).arrows,[0,1]);assert.equal(relationAudit(surfaceProfile(photon).d,0).centralZero,false);
const att=records.find(t=>t.id==='quantum-attention-0'),attgate=att.nodes.find(n=>n.id==='patch2.layer0.ry1');assert.deepEqual(selectionMapping(att,attgate,[0]).edges,[0]);
const harp=records.find(t=>t.id==='toricgt-quantum-hybrid-0');assert.deepEqual(selectionMapping(harp,harp.nodes.find(n=>n.id==='U'),[1,2]).sites,[1,2]);
const nodal=surfaceProfile(photon).d,identity=[[1,0],[0,1]];assert.equal(checkRepresentation(nodal,[identity],[identity,identity]).relationFailures.length,2,'Invertible nodal branch matrices fail xy=yx=0');
assert.throws(()=>permutation([[0,2]]));assert.throws(()=>dessin([[0,1]],[[0],[1]]));
// Synthetic schema fixtures exercise optional collections without creating records.
const rgTrace={schema_version:1,id:'full-action-rg-fixture',title:'RG feature fixture',category:'quantum-full-action-rg',input:{surface_m:5},provenance:{kind:'trained-checkpoint-replay'},nodes:[
 {id:'couplings',formula:'J+, J−, b',inputs:[],tensor:{shape:[3],axes:['coupling'],dtype:'float64',values:[.2,.3,.1]}},
 {id:'feature.ry2',formula:'RY on feature register b',inputs:['couplings'],gate:'RY',wires:[2],tensor:{shape:[8],axes:['basis'],dtype:'complex128',real:[1,0,0,0,0,0,0,0],imag:Array(8).fill(0)}},
 {id:'prediction',formula:'Full boundary action',inputs:['feature.ry2'],tensor:{shape:[32],axes:['boundary_configuration'],dtype:'float64',values:Array(32).fill(0)}}],checks:{fixture:{error:0,tolerance:0}}};
validateTrace(rgTrace);const rgProfile=surfaceProfile(rgTrace);
assert.equal(rgProfile.kind,'rg');assert.equal(rgProfile.d.genus,2);assert.equal(rgProfile.d.rank,50);assert.equal(rgProfile.d.edges.length,5);assert.deepEqual(rgProfile.d.passport,[[5,5],[2,2,2,2,2],[10]]);
assert(rgProfile.limit.includes('7 physical spins'));assert(rgProfile.limit.includes('three-qubit'));assert(rgProfile.limit.includes('0.6 b s−'));assert(selectionMapping(rgTrace,rgTrace.nodes[0],[2]).note.includes('two black spins'));
assert.deepEqual(selectionMapping(rgTrace,rgTrace.nodes[0],[0]).roles,['J+']);assert.deepEqual(selectionMapping(rgTrace,rgTrace.nodes[0],[1]).roles,['J−']);assert.deepEqual(selectionMapping(rgTrace,rgTrace.nodes[0],[2]).roles,['b']);
const registerMapping=selectionMapping(rgTrace,rgTrace.nodes[1],[7]);assert.deepEqual(registerMapping.edges,[],'Feature register must not invent quiver vertices');assert.deepEqual(registerMapping.roles,['b']);assert(registerMapping.labels.some(s=>s.includes('|111⟩')));
assert.deepEqual(selectionMapping(rgTrace,rgTrace.nodes[2],[31]).edges,[0,1,2,3,4]);
const qtoken={...rgTrace,id:'qtoken-fixture',category:'quantum-tokengt-rg'};assert.equal(surfaceProfile(qtoken).kind,'rg-token');assert.equal(surfaceProfile(qtoken).d.rank,50);assert.deepEqual(selectionMapping(qtoken,rgTrace.nodes[1],[0]).edges,[]);assert.deepEqual(selectionMapping(qtoken,rgTrace.nodes[1],[0]).roles,[]);
for(const m of [3,5,9]){const d=oddDessin(m);assert.equal(d.genus,(m-1)/2);assert.equal(d.rank,2*m*m);assert.equal(d.faces.length,1);for(const a of d.arrows)assert.equal(relationAudit(d,a.dart).failures,0);}
assert.throws(()=>oddDessin(4));assert.throws(()=>oddDessin(1));
assert.deepEqual(architectureCollection('rg'),{id:'rg',base:'/data/rg/',manifest:'/data/rg/manifest.json'});assert.equal(architectureCollection('qtoken').manifest,'/data/quantum-tokengt/manifest.json');
for(const key of [null,undefined,'https://example.invalid/manifest.json','../rg','__proto__','constructor'])assert.equal(architectureCollection(key).manifest,'/data/architecture/manifest.json');
const optionalSavedCollections=[];
for(const collection of ['rg','qtoken']){
 const base=architectureCollection(collection).base,path='web'+base+'manifest.json';if(!existsSync(path))continue;
 const extra=JSON.parse(readFileSync(path));let extraNodes=0;
 for(const entry of extra.traces){assert(/^records\/[a-zA-Z0-9_-]+\.json$/.test(entry.file));const bytes=readFileSync('web'+base+entry.file);assert.equal(createHash('sha256').update(bytes).digest('hex'),entry.sha256);const trace=validateTrace(JSON.parse(bytes)),p=surfaceProfile(trace);assert.equal(p.d.genus,2);assert.equal(p.d.rank,50);
  for(const node of trace.nodes){for(const indices of [node.tensor.shape.map(()=>0),node.tensor.shape.map(n=>n-1)]){const mapping=selectionMapping(trace,node,indices);assert(mapping.edges.every(e=>e>=0&&e<5));}extraNodes++;}
 }
 optionalSavedCollections.push({id:collection,cases:extra.traces.length,nodes:extraNodes,hashes_verified:true});
}
const report={passed:true,cases:summaries.length,nodes,exact_forbidden_products:relations,checks:['record SHA256 unchanged','all saved nodes at first and last coordinate','square has two quiver vertices','genus-four passport and rank','token endpoint relabelling and padding','gate wire support','attention patch support','quadrature branches','auxiliary Weyl sites','nodal central nilpotence','whitelisted optional collection paths','genus-two m5 profile/rank/passport','physical spins vs quiver vertices vs parameter registers','full boundary configurations','new qtoken avoids old theta dictionary'],optional_collection_schema_fixtures:2,optionalSavedCollections,profiles:summaries};
const out=process.argv[2]??'outputs/checks/2026-11-03-actual-rg/architecture';mkdirSync(out,{recursive:true});writeFileSync(out+'/surface-bridge-model.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,profiles:undefined}));
