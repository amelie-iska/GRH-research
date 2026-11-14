/* Pure controller/topology functions shared by the worker, UI and Node tests.
 * Max-plus is a classical, coordinatewise operation. It is not a quantum gate.
 */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.SurfaceCore=api;})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const DEFAULT={qx:.7,qy:-.4,mode:'maxplus',tau:.35,gain:.6,base:[.35,-.2,.25,-.3],signs:[1,1,1,1]};
 function finite(x,low,high,name){if(typeof x!=='number'||!Number.isFinite(x)||x<low||x>high)throw new Error(name+' outside finite domain');return x;}
 function config(raw){
  if(!raw||typeof raw!=='object')throw new Error('Configuration required');
  const c={qx:finite(raw.qx,-3,3,'qx'),qy:finite(raw.qy,-3,3,'qy'),mode:raw.mode,tau:finite(raw.tau,.02,2,'temperature'),gain:finite(raw.gain,0,1,'gain')};
  if(!['maxplus','softmax','hard'].includes(c.mode))throw new Error('Unknown attention operator');
  if(!Array.isArray(raw.base)||raw.base.length!==4||!Array.isArray(raw.signs)||raw.signs.length!==4)throw new Error('Four angles and signs required');
  c.base=raw.base.map(x=>finite(x,-Math.PI,Math.PI,'base angle'));
  c.signs=raw.signs.map(x=>{if(x!==1&&x!==-1)throw new Error('Signs are +1 or -1');return x;});return c;
 }
 function permutation(p,n){if(!Array.isArray(p)||p.length!==n||p.some(x=>!Number.isInteger(x)||x<0||x>=n)||new Set(p).size!==n)throw new Error('Invalid dessin permutation');}
 function cycles(p){const seen=new Set(),out=[];for(let i=0;i<p.length;i++){if(seen.has(i))continue;const c=[];let j=i;while(!seen.has(j)){seen.add(j);c.push(j);j=p[j];}out.push(c);}return out;}
 function binaryRank(rows,n){const basis=new Map();for(const row of rows){let v=0n;for(const q of row){if(!Number.isInteger(q)||q<0||q>=n)throw new Error('Invalid check qubit');v^=1n<<BigInt(q);}while(v){const bit=v.toString(2).length-1;if(basis.has(bit))v^=basis.get(bit);else{basis.set(bit,v);break;}}}return basis.size;}
 function topology(model){
  if(!model||model.n!==18||model.id!=='torus3x3'||model.edges.length!==18)throw new Error('This dense explorer uses the checked 18-qubit torus3x3 only');
  const p=model.permutations,n=36;
  for(const key of ['sigma0','sigma1','sigma_infinity'])permutation(p[key],n);
  for(let i=0;i<n;i++)if(p.sigma1[i]===i||p.sigma1[p.sigma1[i]]!==i||p.sigma0[p.sigma1[p.sigma_infinity[i]]]!==i)throw new Error('Dessin relation failed');
  const orbit=new Set([0]),queue=[0];for(let j=0;j<queue.length;j++)for(const perm of [p.sigma0,p.sigma1]){const k=perm[queue[j]];if(!orbit.has(k)){orbit.add(k);queue.push(k);}}
  if(orbit.size!==n)throw new Error('Disconnected dessin');
  const black=cycles(p.sigma0),white=cycles(p.sigma1),faces=cycles(p.sigma_infinity),chi=black.length+white.length+faces.length-n;
  const xs=model.x_checks.map(x=>x.qubits),zs=model.z_checks.map(x=>x.qubits);
  for(const a of xs)for(const b of zs)if(a.filter(x=>b.includes(x)).length%2)throw new Error('CSS checks anticommute');
  const rx=binaryRank(xs,18),rz=binaryRank(zs,18);
  return {darts:n,physicalQubits:18,blackCycles:black,whiteCycles:white,faceCycles:faces,chi,genus:(2-chi)/2,rankX:rx,rankZ:rz,logicalQubits:18-rx-rz,connected:true,cssCommutes:true};
 }
 function tokenFeatures(model){return model.edges.map(e=>{const u=2*Math.PI*e.x/3,v=2*Math.PI*e.y/3;return {edge:e.id,key:[Math.cos(u),Math.sin(v)],value:[Math.sin(u),Math.cos(u),Math.sin(v),Math.cos(v)]};});}
 function attention(model,raw){
  const c=config(raw),tokens=tokenFeatures(model),scores=tokens.map(t=>(c.qx*t.key[0]+c.qy*t.key[1])/Math.SQRT2),top=Math.max(...scores);
  const exp=scores.map(s=>Math.exp((s-top)/c.tau)),den=exp.reduce((a,b)=>a+b,0),soft=exp.map(x=>x/den);
  const scoreWinners=scores.map((s,i)=>s===top?i:-1).filter(i=>i>=0);
  let mass=soft,y,coordinateWinners;
  if(c.mode==='maxplus'){
   const all=Array.from({length:4},(_,j)=>tokens.map((t,i)=>scores[i]+t.value[j]));
   const maxima=all.map(x=>Math.max(...x));y=maxima.map(x=>x-top);
   coordinateWinners=all.map((x,j)=>x.map((v,i)=>v===maxima[j]?i:-1).filter(i=>i>=0));
   mass=tokens.map((_,i)=>coordinateWinners.reduce((s,w)=>s+(w.includes(i)?1/w.length:0),0)/4);
  }else if(c.mode==='hard'){
   mass=tokens.map((_,i)=>scoreWinners.includes(i)?1/scoreWinners.length:0);
   y=Array.from({length:4},(_,j)=>tokens.reduce((s,t,i)=>s+mass[i]*t.value[j],0));coordinateWinners=Array(4).fill(scoreWinners);
  }else{y=Array.from({length:4},(_,j)=>tokens.reduce((s,t,i)=>s+mass[i]*t.value[j],0));coordinateWinners=Array(4).fill(scoreWinners);}
  const sorted=[...scores].sort((a,b)=>b-a),gap=sorted[0]-sorted[1];
  const theta=y.map((v,i)=>c.base[i]+c.gain*v);
  return {config:c,tokens,scores,mass,output:y,theta,scoreWinners,coordinateWinners,gap,
   logSumExpPotential:top+c.tau*Math.log(den),maxPotential:top,
   lseErrorBound:c.tau*Math.log(tokens.length),
   analyticExpectation:c.signs.reduce((a,b)=>a*b,1)*theta.reduce((a,t)=>a*Math.cos(t),1),
   operator:c.mode==='maxplus'?'max_j(score_j+value_jc)-max_j(score_j)':c.mode==='hard'?'average of value vectors at score maximizers':'softmax(score/temperature) weighted value average'};
 }
 function gates(model,raw){const a=attention(model,raw),patch=model.x_checks[0].qubits.slice();return patch.map((q,i)=>({gate:'RY',target:q,qubits:[q],angle:a.config.signs[i]*Math.PI/2+a.theta[i]})).concat(patch.slice(1).map(q=>({gate:'CX',control:q,target:patch[0],qubits:[q,patch[0]]})));}
 function simulate(Quantum,model,raw,prepared){
  const a=attention(model,raw),patch=model.x_checks[0].qubits,base=prepared||new Quantum.StateVector(18).applyCircuit(model.prepare_circuit),state=base.clone().applyCircuit(gates(model,raw));
  const x=model.x_checks.map(c=>state.expectationX(c.qubits)),z=model.z_checks.map(c=>state.expectationZ(c.qubits));
  const probability=Array(16).fill(0);let norm2=0;
  for(let i=0;i<state.size;i++){const p=state.re[i]**2+state.im[i]**2;norm2+=p;let k=0;for(let j=0;j<4;j++)if(i&(1<<patch[j]))k|=1<<j;probability[k]+=p;}
  const expectation=state.expectationZ([patch[0]]),entropy=probability.reduce((s,p)=>s-(p>0?p*Math.log2(p):0),0);
  if(Math.abs(norm2-1)>1e-9||Math.abs(expectation-a.analyticExpectation)>1e-9)throw new Error('Independent circuit identity failed');
  return {attention:a,patch,expectation,analyticExpectation:a.analyticExpectation,identityError:Math.abs(expectation-a.analyticExpectation),norm2,probability,patchMeasurementEntropy:entropy,xChecks:x,zChecks:z,energy:-x.reduce((s,v)=>s+v,0)-z.reduce((s,v)=>s+v,0),fidelityToPrepared:state.fidelity(base),gates:gates(model,raw),backend:'JavaScript Float64 dense 18-qubit state-vector simulation',scope:'Constructed hybrid controller and spin-code circuit. Not hardware, training, a learned physical correspondence, or quantum advantage.'};
 }
 return {DEFAULT,config,cycles,topology,tokenFeatures,attention,gates,simulate};
});
