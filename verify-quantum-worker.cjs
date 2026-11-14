'use strict';
// Exercise the actual worker message handler in a Node VM. This is a protocol
// check, not a replacement for rendered browser/Worker integration testing.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const Q=require('./quantum-core.js'),messages=[];
const self={postMessage:m=>messages.push(structuredClone(m))};
const context=vm.createContext({QuantumCore:Q,self,importScripts:()=>{},setTimeout,performance,console});
vm.runInContext(fs.readFileSync(path.join(__dirname,'quantum-worker.js'),'utf8'),context);
const send=(type,data={})=>self.onmessage({data:{type,...data}});
const last=type=>messages.filter(m=>m.type===type).at(-1);
(async()=>{
 const model=JSON.parse(fs.readFileSync(path.join(__dirname,'data/torus3x3.json'),'utf8'));
 await send('init',{model});assert.equal(last('ready').n,18);assert.equal(last('snapshot').cursor,0);
 await send('step');assert.equal(last('snapshot').cursor,1);
 await send('prepare');assert.equal(last('snapshot').cursor,42);assert.ok(last('snapshot').checks.every(c=>Math.abs(c.value-1)<1e-10));
 await send('append',{gate:{gate:'X',qubits:[0]}});
 let snap=last('snapshot');assert.equal(snap.cursor,43);assert.equal(snap.checks.filter(c=>c.value<-.9999).length,2);
 await send('reset');assert.equal(last('snapshot').cursor,0);
 const playing=send('play');await send('stop');await playing;assert.equal(last('snapshot').cursor,1);
 await send('qnnRun',{theta:Q.initialTheta,signs:[-1,1,1,1]});assert.ok(last('prediction').value<0);assert.equal(last('snapshot').total,49);
 await send('train',{theta:Q.initialTheta,steps:1});const trained=last('trained');assert.equal(trained.rows.length,16);assert.equal(trained.rows.filter(r=>r.training).length,4);assert.ok(trained.history[1].loss<trained.history[0].loss);
 assert.equal(messages.filter(m=>m.type==='error').length,0);
 console.log(JSON.stringify({status:'passed',scope:'Actual worker handler in a Node VM; browser integration still separate',checks:['initialization','single step','42-gate preparation','Pauli error syndrome','reset','paced playback cancellation','49-gate QNN sample','parameter-shift training and16-input report'],lastLoss:trained.history.at(-1).loss},null,2));
})().catch(error=>{console.error(error);process.exitCode=1;});
