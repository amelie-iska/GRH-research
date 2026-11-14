'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const Q=require('./quantum-core.js');
const model=Q.normalizeModel(JSON.parse(fs.readFileSync(path.join(__dirname,'data/torus3x3.json'),'utf8')));
const close=(a,b,tol=2e-10)=>assert.ok(Math.abs(a-b)<=tol,`${a} differs from ${b}`);
const started=performance.now();
// A Bell state checks bit ordering, H and controlled-X without relying on topology.
const bell=new Q.StateVector(2).apply({gate:'H',qubits:[0]}).apply({gate:'CX',qubits:[0,1]});
close(bell.re[0],Math.SQRT1_2);close(bell.re[3],Math.SQRT1_2);close(bell.expectationX([0,1]),1);close(bell.expectationZ([0,1]),1);
// Complex phases and inverse rotations check both real and imaginary arrays.
const phase=new Q.StateVector(1).apply({gate:'H',qubits:[0]}).apply({gate:'RZ',qubits:[0],angle:Math.PI/2});
close(phase.re[0],.5);close(phase.im[0],-.5);close(phase.re[1],.5);close(phase.im[1],.5);
phase.apply({gate:'RZ',qubits:[0],angle:-Math.PI/2}).apply({gate:'H',qubits:[0]});close(phase.re[0],1);close(phase.re[1],0);
const rotated=new Q.StateVector(2).apply({gate:'RY',qubits:[1],angle:.713}).apply({gate:'RY',qubits:[1],angle:-.713});close(rotated.re[0],1);
const base=new Q.StateVector(18).applyCircuit(model.prepare_circuit),scratch=new Q.StateVector(18);
const stats=base.statistics();close(stats.norm2,1);assert.equal(stats.support,2**model.metadata.rankX);close(stats.entropy,model.metadata.rankX);
let maxStabilizerResidual=0,maxErrorResidual=0;
for(const c of model.x_checks)maxStabilizerResidual=Math.max(maxStabilizerResidual,Math.abs(base.expectationX(c.qubits)-1));
for(const c of model.z_checks)maxStabilizerResidual=Math.max(maxStabilizerResidual,Math.abs(base.expectationZ(c.qubits)-1));
assert.ok(maxStabilizerResidual<2e-10);
// Every single-qubit X/Z error is checked against every relevant syndrome.
for(let q=0;q<18;q++) {
 scratch.copyFrom(base).apply({gate:'X',qubits:[q]});
 for(const c of model.z_checks)maxErrorResidual=Math.max(maxErrorResidual,Math.abs(scratch.expectationZ(c.qubits)-(c.qubits.includes(q)?-1:1)));
 scratch.copyFrom(base).apply({gate:'Z',qubits:[q]});
 for(const c of model.x_checks)maxErrorResidual=Math.max(maxErrorResidual,Math.abs(scratch.expectationX(c.qubits)-(c.qubits.includes(q)?-1:1)));
}
assert.ok(maxErrorResidual<2e-10);
const patch=Q.qnnPatch(model);assert.deepEqual(patch,[0,2,9,15]);
let maxQnnResidual=0;
for(const signs of Q.allSigns()) {
 const measured=Q.qnnPredict(base,scratch,patch,signs,Q.initialTheta),reference=Q.parityLabel(signs)*Q.initialTheta.reduce((s,x)=>s*Math.cos(x),1);
 maxQnnResidual=Math.max(maxQnnResidual,Math.abs(measured-reference));
}
assert.ok(maxQnnResidual<2e-10);
const first=Q.qnnGradient(base,scratch,patch,Q.initialTheta),product=Q.initialTheta.reduce((s,x)=>s*Math.cos(x),1);
let maxGradientResidual=0;
for(let j=0;j<4;j++) {
 const d=-Math.sin(Q.initialTheta[j])*Q.initialTheta.reduce((s,x,i)=>i===j?s:s*Math.cos(x),1),reference=2*(product-1)*d;
 maxGradientResidual=Math.max(maxGradientResidual,Math.abs(first.gradient[j]-reference));
}
assert.ok(maxGradientResidual<2e-10);
const updated=Q.initialTheta.map((x,j)=>x-.2*first.gradient[j]),after=Q.mse(Q.qnnBatch(base,scratch,patch,updated));assert.ok(after<first.loss);
const result={status:'passed',execution:'Node.js, same kernel imported by browser worker',n:18,dimension:2**18,bytesPerState:base.re.byteLength+base.im.byteLength,encoderGates:model.prepare_circuit.length,preparedSupport:stats.support,normSquared:stats.norm2,maxStabilizerResidual,maxSingleErrorSyndromeResidual:maxErrorResidual,qnnInputPatterns:16,maxQnnReferenceResidual:maxQnnResidual,maxParameterShiftGradientResidual:maxGradientResidual,initialMSE:first.loss,afterOneUpdateMSE:after,elapsedSeconds:(performance.now()-started)/1000,scope:'Finite classical state-vector implementation checks; not quantum hardware execution or a fault-tolerance proof.'};
console.log(JSON.stringify(result,null,2));
