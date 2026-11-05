import assert from'node:assert/strict';
import{readFileSync,writeFileSync}from'node:fs';
import{webcrypto,createHash}from'node:crypto';
globalThis.crypto=webcrypto;
const{unpackDisplay,complexProjection,complexNorm,featureValue,PAYLOAD_SHA256}=await import('../../../web/arithmetic-learning.mjs');
const root=new URL('../../../',import.meta.url),bytes=readFileSync(new URL('web/data/arithmetic-learning.json',root));assert.equal(createHash('sha256').update(bytes).digest('hex'),PAYLOAD_SHA256);
const packed=JSON.parse(bytes),display=await unpackDisplay(packed),baseline=JSON.parse(readFileSync(new URL('outputs/checks/2026-11-05-arithmetic-learning/ui-learning/payload-unpacked-v1.json',root)));
let states=0,coordinates=0,features=0;
const near=(a,b)=>assert(Math.abs(a-b)<=1e-11*Math.max(1,Math.abs(b)),`${a} versus${b}`);
const fraction=s=>{const[a,b='1']=s.split('/');return Number(a)/Number(b);};
for(let ci=0;ci<4;ci++){
 const c=display.cases[ci],original=baseline.cases[ci];assert.equal(c.trajectories.metric.updates,[53,55,53,55][ci]);assert.equal(c.trajectories.ordinary.updates,50);
 for(const method of['metric','ordinary']){
  const t=c.trajectories[method];assert.deepEqual(t.states,original.trajectories[method].states,'Decoded saved states exactly match extractor projections');
  assert.equal(t.states.length,t.updates+1);
  for(const s of t.states){states++;for(let i=0;i<210;i++){coordinates++;const v=s.coordinates[i],e=s.residuals[i],target=c.target[i],[re,im]=complexProjection(e);near(complexNorm(e)**2,re*re+im*im);near(v[0],target[0]+e[0]);near(v[1],target[1]+e[1]);}
   for(const k of['CC','CM']){near(complexNorm(s.errors[k])**2,s.actual_errors_squared[k]);assert(s.actual_errors_squared[k]<=s.bounds_squared[k]*(1+1e-12));near(Math.log10(s.bounds_squared[k]),s.log_bounds_squared[k]);}
   near(Math.log10(s.loss),s.log_loss);
  }
  assert.equal(t.states.at(-1).accepted,method==='metric');
 }
 for(const f of c.features){const block=display.blocks[f.block];for(const sample of f.values){const value=featureValue(block,c.trajectories.metric.states.at(-1).coordinates,sample.phase),target=featureValue(block,c.target,sample.phase);value.forEach((v,i)=>near(v,fraction(sample.prediction[i])));target.forEach((v,i)=>near(v,fraction(sample.target[i])));features++;}}
}
assert.equal(states,424);assert.equal(coordinates,89040);assert.throws(()=>featureValue(display.blocks[0],display.cases[0].target,[]),RangeError);
const tampered=JSON.parse(bytes);tampered.cases[0].trajectories.metric.states_sha256='0'.repeat(64);await assert.rejects(()=>unpackDisplay(tampered),/hash mismatch/);
const report={passed:true,payloadBytes:bytes.length,states,coordinateStates:coordinates,featureSamples:features,checks:['payload and all8 decoded trajectory hashes','exact decoded-object match to source-derived extractor baseline','all saved coordinates and separately extracted residuals','complex basis geometry, signed errors and certificates','all saved feature samples','53/55/53/55 metric and50 ordinary updates','corrupt trajectory refusal'],scope:'Display checks only; source scientific tests and independent mathematical acceptance are separate.'};writeFileSync(new URL('outputs/checks/2026-11-05-arithmetic-learning/ui-learning/display-js.json',root),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
