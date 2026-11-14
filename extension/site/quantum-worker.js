'use strict';
importScripts('quantum-core.js');
const Q=QuantumCore;
let model=null,state=null,base=null,scratch=null,circuit=[],cursor=0,busy=false,stop=false;
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
function send(type,data={}) { self.postMessage({type,...data}); }
function snapshot(extra={}) {
  if (!state) return;
  const checks=[];
  for (const c of model.x_checks) checks.push({id:c.id,kind:'X',qubits:c.qubits,value:state.expectationX(c.qubits)});
  for (const c of model.z_checks) checks.push({id:c.id,kind:'Z',qubits:c.qubits,value:state.expectationZ(c.qubits)});
  send('snapshot',{cursor,total:circuit.length,circuit,checks,stats:state.statistics(),fidelity:state.fidelity(base),...extra});
}
async function runCircuit(animated) {
  if (busy) return;
  busy=true;stop=false;send('busy',{mode:animated?'play':'run'});
  const started=performance.now();
  try {
    while(cursor<circuit.length&&!stop) {
      state.apply(circuit[cursor++]);
      if (animated || cursor%8===0 || cursor===circuit.length) snapshot();
      await pause(animated?260:0);
    }
    snapshot({elapsedMs:performance.now()-started});
  } finally { busy=false;send('idle'); }
}
async function train(steps,theta) {
  if (busy) return;
  busy=true;stop=false;send('busy',{mode:'train'});
  const patch=Q.qnnPatch(model),started=performance.now(),history=[];
  try {
    for(let epoch=0;epoch<=steps;epoch++) {
      const r=Q.qnnGradient(base,scratch,patch,theta);
      history.push({epoch,loss:r.loss});
      send('training',{epoch,steps,theta:theta.slice(),loss:r.loss,rows:r.rows,history:history.slice(),gradient:r.gradient});
      if(epoch===steps||stop) break;
      theta=theta.map((x,j)=>x-0.2*r.gradient[j]);
      await pause(0);
    }
    const all=Q.qnnBatch(base,scratch,patch,theta,Q.allSigns());
    for(const r of all) r.training=Q.trainingSigns.some(s=>s.every((v,i)=>v===r.signs[i]));
    send('trained',{theta,history,rows:all,elapsedMs:performance.now()-started,stopped:stop});
  } finally {busy=false;send('idle');}
}
self.onmessage=async event=>{
  const m=event.data;
  try {
    if(m.type==='stop') {stop=true;return;}
    if(busy) return;
    if(m.type==='init') {
      model=Q.normalizeModel(m.model);
      if(model.n!==18) throw new Error('Live browser simulation is restricted to the verified 18-qubit case. Larger cases use recorded runs.');
      state=new Q.StateVector(model.n);base=new Q.StateVector(model.n);scratch=new Q.StateVector(model.n);
      circuit=model.prepare_circuit.slice();cursor=0;
      base.applyCircuit(circuit);
      const baseChecks=model.x_checks.map(c=>base.expectationX(c.qubits)).concat(model.z_checks.map(c=>base.expectationZ(c.qubits)));
      const residual=Math.max(...baseChecks.map(x=>Math.abs(1-x)),Math.abs(base.statistics().norm2-1));
      if(residual>1e-8) throw new Error('Preparation failed its stabilizer or normalization check: '+residual);
      send('ready',{n:model.n,memoryPerStateBytes:16*2**model.n,allocatedStateBytes:3*16*2**model.n,baseResidual:residual,patch:Q.qnnPatch(model)});
      snapshot();return;
    }
    if(!state) throw new Error('Load a live surface case first.');
    if(m.type==='reset') {state.reset();cursor=0;snapshot();}
    if(m.type==='prepare') {circuit=model.prepare_circuit.slice();state.reset();cursor=0;await runCircuit(false);}
    if(m.type==='step') {if(cursor<circuit.length) state.apply(circuit[cursor++]);snapshot();}
    if(m.type==='run') await runCircuit(false);
    if(m.type==='play') await runCircuit(true);
    if(m.type==='append') {
      const g=m.gate;state.apply(g);circuit.splice(cursor,0,g);cursor++;snapshot();
    }
    if(m.type==='qnnRun') {
      const theta=m.theta.map(Number),signs=m.signs.map(Number);
      if(theta.some(x=>!Number.isFinite(x))||signs.some(x=>x!==1&&x!==-1)) throw new Error('Invalid QNN parameters or feature signs.');
      const patch=Q.qnnPatch(model);
      circuit=model.prepare_circuit.concat(Q.qnnCircuit(patch,signs,theta));state.reset();cursor=0;
      await runCircuit(false);
      send('prediction',{value:state.expectationZ([patch[0]]),target:Q.parityLabel(signs),signs,theta});
    }
    if(m.type==='train') {
      const steps=Math.max(1,Math.min(24,Math.round(m.steps))),theta=m.theta.map(Number);
      if(theta.length!==4||theta.some(x=>!Number.isFinite(x))) throw new Error('Invalid trainable parameters.');
      await train(steps,theta);
    }
  } catch(error) {busy=false;send('error',{message:error.message});send('idle');}
};
