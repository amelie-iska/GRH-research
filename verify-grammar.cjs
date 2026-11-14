/* Independent finite references for the diagram/grammar numerical examples. */
'use strict';
const assert=require('node:assert/strict');
const G=require('./grammar-core.js');
let comparisons=0,gateCases=0,dyckWords=0,truthCases=0,fierzEntries=0,maxError=0;
function close(a,b,tol=2e-12){const e=Math.abs(a-b);maxError=Math.max(maxError,e);assert(e<tol,`${a} != ${b}`);}
// Direct dense reference: a row/output is determined from each basis input.
function referenceGate(n,g){const d=2**n,re=new Float64Array(d*d),im=new Float64Array(d*d);for(let j=0;j<d;j++){
 const bits=Array.from({length:n},(_,q)=>(j>>(n-1-q))&1),q=g.q[0];
 function put(out,r,s=0){const i=out.reduce((x,b)=>2*x+b,0);re[i*d+j]=r;im[i*d+j]=s;}
 if(g.name==='CX'){const z=[...bits];z[g.q[1]]^=bits[q];put(z,1);}
 else if(g.name==='SWAP'){const z=[...bits];[z[q],z[g.q[1]]]=[z[g.q[1]],z[q]];put(z,1);}
 else if(g.name==='H'){for(let b=0;b<2;b++){const z=[...bits];z[q]=b;put(z,(bits[q]&&b?-1:1)/Math.sqrt(2));}}
 else if(g.name==='X'){const z=[...bits];z[q]^=1;put(z,1);}
 else {const angle={Z:Math.PI,S:Math.PI/2,SDG:-Math.PI/2,T:Math.PI/4,TDG:-Math.PI/4}[g.name]*bits[q];put(bits,Math.cos(angle),Math.sin(angle));}
}return{n:d,re,im};}
for(let n=1;n<=5;n++)for(const name of Object.keys(G.inverse))for(let q=0;q<n;q++){
 const two=['CX','SWAP'].includes(name);for(const q2 of two?Array.from({length:n},(_,j)=>j).filter(j=>j!==q):[null]){
  const gate={name,q:two?[q,q2]:[q]},a=G.circuitMatrix(n,[gate]),b=referenceGate(n,gate);close(G.maxDifference(a,b),0);gateCases++;
  const c=G.compare(n,[gate,{name:G.inverse[name],q:gate.q}]);close(c.error,0);assert.equal(c.gates.length,0);comparisons++;
 }
}
for(let n=2;n<=6;n++)for(const kind of ['echo','nested','bell']){const x=G.compare(n,G.preset(n,kind));close(x.error,0);close(x.probabilities.reduce((a,b)=>a+b,0),1);comparisons++;}
assert.throws(()=>G.validate(2,[{name:'CX',q:[0,0]}]));assert.throws(()=>G.validate(2,[{name:'H',q:[2]}]));
for(let n=0;n<=16;n++)for(let mask=0;mask<2**n;mask++){
 let s='',count=0,valid=true;for(let i=0;i<n;i++){const opening=(mask>>i)&1;s+=opening?'(':')';count+=opening?1:-1;if(count<0)valid=false;}
 assert.equal(G.dyck(s).accepted,valid&&count===0);dyckWords++;
}
assert.throws(()=>G.dyck('(a)'));assert.throws(()=>G.dyck('('.repeat(257)));
for(let m=1;m<=3;m++)for(let f=0;f<2**(2**m);f++){
 const truth=Array.from({length:2**m},(_,i)=>(f>>i)&1);
 for(let x=0;x<2**m;x++){const bits=Array.from({length:m},(_,i)=>(x>>(m-1-i))&1);assert.equal(G.booleanNetwork(bits,truth),truth[x]);truthCases++;}
}
for(let u=0;u<=1;u++){assert.deepEqual(G.counterfactual('causal',u),G.counterfactual('confounded',u));for(let doX=0;doX<=1;doX++){assert.equal(G.counterfactual('causal',u,doX).y,doX);assert.equal(G.counterfactual('confounded',u,doX).y,u);}}
for(let N=2;N<=6;N++)for(let i=0;i<N;i++)for(let j=0;j<N;j++)for(let k=0;k<N;k++)for(let l=0;l<N;l++){const f=G.fierz(N,i,j,k,l);close(f.error,0);fierzEntries++;}
for(let d=1;d<=8;d++){const a=G.alternatingProjector(d);assert.equal(a.trace,d*(d-1)/2);assert.equal(a.idempotenceError,0);}
for(let n=1;n<=12;n++){const x=G.graphYield(n);assert.equal(x.edges,x.vertices-1);assert.equal(x.erased,'a'.repeat(n)+'b'.repeat(n)+'c'.repeat(n));}
console.log(JSON.stringify({status:'passed',gateCases,circuitEquivalenceCases:comparisons,exhaustiveDyckWordsThroughLength16:dyckWords,allBooleanFunctionsThroughArity3:truthCases,fierzTensorEntries:fierzEntries,projectorDimensions:[1,2,3,4,5,6,7,8],maximumNumericalError:maxError,scope:'Finite exact-integer and floating-point reference checks; general propositions are proved in the manuscript.'},null,2));
