'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const base=process.argv[2];if(!base)throw new Error('Pass the generated asset directory');
const P=require('../site/program3-core.js'),Q=require('../../extension/site/quantum-core.js');
const load=name=>JSON.parse(fs.readFileSync(path.join(base,name),'utf8'));
const ecc=load('arithmetic.json'),cmb=load('cmb.json'),vectors=load('replay-vectors.json');let arithmetic=0,qnn=0,sky=0,maxError=0;
for(const c of Object.values(ecc.circuits)){const family=ecc.report.curves.find(r=>r.curve.p===c.curve.p);for(let k=0;k<Math.min(16,2**c.scalar_wires.length);k++)for(const point of [null,...family.points.filter(Boolean).slice(0,4)]){const r=P.execute(c,k,P.encode(point,c));assert.equal(r.clean,true);assert.equal(r.totalGates,c.resources.total_gates);arithmetic++;}const bad=P.execute(c,1,0);assert.equal(bad.invalidInput,true);assert.equal(bad.pointOut,0);}
for(const r of vectors.qnn)r.angles.forEach((a,i)=>{const p=P.qnn(Q,a,r.weights);assert.ok(Math.abs(p.logit-r.predicted[i])<1e-12);assert.ok(Math.abs(p.norm2-1)<1e-12);qnn++;});
for(const r of vectors.sky){const out=P.scan(Q,cmb,r.product,r.center,r.amplitude);for(let m=0;m<3;m++)for(let i=0;i<r.scores[m].length;i++)maxError=Math.max(maxError,Math.abs(out.scores[m][i]-r.scores[m][i]));assert.ok(maxError<1e-9);if(r.amplitude===0)assert.equal(out.joint_rank,cmb.sources[r.product].record.joint_rank_p);sky++;}
assert.throws(()=>P.execute(ecc.circuits['7-binary'],999,64));assert.throws(()=>P.scan(Q,cmb,'unknown',0,0));assert.throws(()=>P.scan(Q,cmb,'ILC',0,-1));
console.log(JSON.stringify({schema:'grh.program3.js-replay.v1',arithmetic_basis_replays:arithmetic,invalid_word_cases:4,qnn_replays:qnn,full_sky_replays:sky,max_sky_score_error:maxError,negative_domains:3,passed:true},null,2));
