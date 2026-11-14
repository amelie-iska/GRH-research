/* Finite numerical references for the typed diagram and language laboratory.
 * Qubit 0 is the most-significant basis bit. No remote services or dependencies.
 * General identities are proved in the manuscript; residuals here are instances.
 */
(function (root) {
  'use strict';
  const names = ['H','X','Z','S','SDG','T','TDG','CX','SWAP'];
  const inverse = {H:'H',X:'X',Z:'Z',S:'SDG',SDG:'S',T:'TDG',TDG:'T',CX:'CX',SWAP:'SWAP'};
  function validate(n, gates) {
    if (!Number.isInteger(n)||n<1||n>6) throw new Error('Use one to six qubits.');
    if (!Array.isArray(gates)||gates.length>80) throw new Error('Use at most 80 gates.');
    for (const g of gates) {
      const arity=(g.name==='CX'||g.name==='SWAP')?2:1;
      if (!names.includes(g.name)||!Array.isArray(g.q)||g.q.length!==arity||new Set(g.q).size!==arity||g.q.some(q=>!Number.isInteger(q)||q<0||q>=n)) throw new Error('Ill-typed gate record.');
    }
    return true;
  }
  function apply(re,im,n,g) {
    const bit=1<<(n-1-g.q[0]),d=re.length;
    if(g.name==='CX'||g.name==='SWAP') {
      const b=1<<(n-1-g.q[1]);
      for(let i=0;i<d;i++) {
        const select=g.name==='CX'?((i&bit)&&!(i&b)):(!(i&bit)&&(i&b));
        if(select) {const j=g.name==='CX'?i^b:i^bit^b;[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}
      }
      return;
    }
    let c=1,s=0;
    if(g.name==='S') {c=0;s=1;}
    if(g.name==='SDG') {c=0;s=-1;}
    if(g.name==='T') {c=Math.SQRT1_2;s=Math.SQRT1_2;}
    if(g.name==='TDG') {c=Math.SQRT1_2;s=-Math.SQRT1_2;}
    for(let i=0;i<d;i++) if(!(i&bit)) {
      const j=i|bit,a=re[i],b=im[i],x=re[j],y=im[j];
      if(g.name==='H') {re[i]=(a+x)*Math.SQRT1_2;im[i]=(b+y)*Math.SQRT1_2;re[j]=(a-x)*Math.SQRT1_2;im[j]=(b-y)*Math.SQRT1_2;}
      else if(g.name==='X') {re[i]=x;im[i]=y;re[j]=a;im[j]=b;}
      else if(g.name==='Z') {re[j]=-x;im[j]=-y;}
      else {re[j]=c*x-s*y;im[j]=s*x+c*y;}
    }
  }
  function circuitMatrix(n,gates) {
    validate(n,gates);const d=2**n,re=new Float64Array(d*d),im=new Float64Array(d*d);
    for(let col=0;col<d;col++) {
      const r=new Float64Array(d),s=new Float64Array(d);r[col]=1;
      for(const g of gates)apply(r,s,n,g);
      for(let row=0;row<d;row++) {re[row*d+col]=r[row];im[row*d+col]=s[row];}
    }
    return {n:d,re,im};
  }
  function cancel(gates) {
    const stack=[],events=[];
    for(let index=0;index<gates.length;index++) {
      const g=gates[index],last=stack[stack.length-1];
      if(last&&inverse[g.name]===last.g.name&&g.q.length===last.g.q.length&&g.q.every((q,i)=>q===last.g.q[i])) {
        stack.pop();events.push({left:last.index,right:index,rule:g.name+'⁻¹·'+g.name+' = I'});
      } else stack.push({g:{name:g.name,q:[...g.q]},index});
    }
    return {gates:stack.map(x=>x.g),events};
  }
  function maxDifference(a,b) {
    if(a.n!==b.n)throw new Error('Matrix types differ.');
    let error=0;for(let i=0;i<a.re.length;i++)error=Math.max(error,Math.hypot(a.re[i]-b.re[i],a.im[i]-b.im[i]));return error;
  }
  function compare(n,gates) {
    validate(n,gates);const simplified=cancel(gates),a=circuitMatrix(n,gates),b=circuitMatrix(n,simplified.gates);
    return {...simplified,error:maxDifference(a,b),dimension:a.n,probabilities:Array.from({length:a.n},(_,i)=>a.re[i*a.n]**2+a.im[i*a.n]**2)};
  }
  function preset(n,kind='echo') {
    if(n<2||n>6)throw new Error('Preset needs two to six wires.');
    const core=[{name:'H',q:[0]},{name:'T',q:[1]},{name:'CX',q:[0,1]}];
    if(kind==='bell')return [{name:'H',q:[0]},{name:'CX',q:[0,1]}];
    if(kind==='nested')return [...core,{name:'S',q:[0]},{name:'H',q:[n-1]},{name:'H',q:[n-1]},{name:'SDG',q:[0]},{name:'CX',q:[0,1]},{name:'TDG',q:[1]},{name:'H',q:[0]}];
    return [...core,{name:'H',q:[n-1]},{name:'H',q:[n-1]},{name:'S',q:[0]},{name:'SDG',q:[0]},{name:'CX',q:[0,1]},{name:'CX',q:[0,1]}];
  }
  function generators(N) {
    if(!Number.isInteger(N)||N<2||N>8)throw new Error('Use dimension two to eight.');
    const out=[];
    for(let i=0;i<N;i++)for(let j=i+1;j<N;j++) {
      let re=new Float64Array(N*N),im=new Float64Array(N*N);re[i*N+j]=re[j*N+i]=.5;out.push({re,im});
      re=new Float64Array(N*N);im=new Float64Array(N*N);im[i*N+j]=-.5;im[j*N+i]=.5;out.push({re,im});
    }
    for(let k=1;k<N;k++) {const re=new Float64Array(N*N),im=new Float64Array(N*N),f=1/Math.sqrt(2*k*(k+1));for(let i=0;i<k;i++)re[i*N+i]=f;re[k*N+k]=-k*f;out.push({re,im});}
    return out;
  }
  function fierz(N,i,j,k,l) {
    if([i,j,k,l].some(x=>!Number.isInteger(x)||x<0||x>=N))throw new Error('Index outside representation space.');
    let re=0,im=0;for(const t of generators(N)) {const a=i*N+j,b=k*N+l;re+=t.re[a]*t.re[b]-t.im[a]*t.im[b];im+=t.re[a]*t.im[b]+t.im[a]*t.re[b];}
    const rhs=.5*((i===l&&k===j?1:0)-(i===j&&k===l?1/N:0));return {re,im,rhs,error:Math.hypot(re-rhs,im),casimir:(N*N-1)/(2*N)};
  }
  function alternatingProjector(d) {
    if(!Number.isInteger(d)||d<1||d>8)throw new Error('Use dimension one to eight.');
    const n=d*d,P=new Float64Array(n*n);for(let i=0;i<d;i++)for(let j=0;j<d;j++){const a=i*d+j,b=j*d+i;P[a*n+a]+=.5;P[b*n+a]-=.5;}
    let trace=0,error=0;for(let a=0;a<n;a++){trace+=P[a*n+a];for(let b=0;b<n;b++){let sum=0;for(let c=0;c<n;c++)sum+=P[a*n+c]*P[c*n+b];error=Math.max(error,Math.abs(sum-P[a*n+b]));}}
    return {trace,rank:d*(d-1)/2,idempotenceError:error,loop:d,P};
  }
  function dyck(word) {
    if(typeof word!=='string'||word.length>256||/[^()]/.test(word))throw new Error('Enter at most 256 opening or closing parentheses, with no other characters.');
    const relu=x=>Math.max(0,x),trace=[{step:0,count:0,error:0,symbol:''}];let count=0,error=0;
    for(const symbol of word){count+=symbol==='('?1:-1;const r=relu(-count)-relu(-count-1);error=relu(error-r)+r;trace.push({step:trace.length,count,error,symbol});}
    const accepted=relu(relu(1-Math.abs(count))-error);
    return {accepted:!!accepted,count,error,trace,maxDepth:Math.max(...trace.map(x=>x.count)),firstBad:trace.find(x=>x.error)?.step??null};
  }
  function booleanNetwork(bits,truth) {
    if(bits.some(x=>x!==0&&x!==1)||truth.length!==2**bits.length)throw new Error('Boolean truth table required.');
    let out=0;for(let b=0;b<truth.length;b++)if(truth[b]) {let matches=0;for(let i=0;i<bits.length;i++)matches+=((b>>(bits.length-1-i))&1)?bits[i]:1-bits[i];out+=Math.max(0,matches-bits.length+1);}return out;
  }
  function counterfactual(model,u,intervention=null) {
    if(!['causal','confounded'].includes(model)||![0,1].includes(u)||![null,0,1].includes(intervention))throw new Error('Invalid causal model input.');
    const x=intervention===null?u:intervention;
    const parent=model==='causal'?x:u;
    return {x,y:booleanNetwork([parent],[0,1]),u};
  }
  function graphYield(n) {
    if(!Number.isInteger(n)||n<1||n>12)throw new Error('Use one to twelve replacements.');
    return {tuple:['a'.repeat(n),'b'.repeat(n),'c'.repeat(n)],yield:'a'.repeat(n)+'#'+'b'.repeat(n)+'#'+'c'.repeat(n),erased:'a'.repeat(n)+'b'.repeat(n)+'c'.repeat(n),vertices:3*(n+1),edges:3*n+2,treewidth:1};
  }
  const api={validate,apply,circuitMatrix,cancel,maxDifference,compare,preset,generators,fierz,alternatingProjector,dyck,booleanNetwork,counterfactual,graphYield,inverse};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;root.GrammarMath=api;
})(typeof globalThis!=='undefined'?globalThis:this);
