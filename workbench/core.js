/* Exact, bounded browser contracts. Arithmetic is BigInt; never Number coercion. */
(function(root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.GRHWorkbench = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function() {
  'use strict';
  const SCHEMA = 'grh.workbench.certificate.v1', MAX_DIM = 12, MAX_DIGITS = 96;
  const SCOPES = {
    heat: 'Exact five-point stencil coefficients; not floating-point execution or a continuum PDE proof.',
    gain: 'Exact weighted comparison-matrix contraction; the model-to-matrix comparison remains an assumption.',
    rank: 'Exact finite Monte Carlo rank; probability validity additionally requires exchangeability of the complete frozen search statistic.',
    risk: 'Exact union-bound budget with a supplied null-model discrepancy allowance; individual event bounds and discrepancy are assumptions.',
    mutation: 'Exact skew-symmetric exchange-matrix and positive rational seed mutation; not a categorical or spectral equivalence certificate.'
  };
  const abs = a => a < 0n ? -a : a;
  function gcd(a,b) { a=abs(a); b=abs(b); while(b) [a,b]=[b,a%b]; return a; }
  function rat(n,d=1n) {
    if(d===0n) throw new Error('Zero denominator');
    if(d<0n) {n=-n;d=-d;}
    const g=gcd(n,d); return [n/g,d/g];
  }
  function parse(s) {
    if(typeof s!=='string'||s.length>2*MAX_DIGITS+2||!/^\-?(?:0|[1-9][0-9]*)(?:\/[1-9][0-9]*)?$/.test(s)) throw new Error('Use an integer or p/q string');
    const a=s.split('/');
    if(a.some(v=>v.replace('-','').length>MAX_DIGITS)) throw new Error('Rational digit budget exceeded');
    return rat(BigInt(a[0]),a.length===2?BigInt(a[1]):1n);
  }
  function str(a) {
    if(abs(a[0]).toString().length>MAX_DIGITS||a[1].toString().length>MAX_DIGITS) throw new Error('Result digit budget exceeded');
    return `${a[0]}/${a[1]}`;
  }
  const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
  const le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
  const zero=[0n,1n],one=[1n,1n];
  function pow(a,n) { let v=one; for(let i=0;i<n;i++) {v=mul(v,a);str(v);} return v; }
  function integer(v,lo,hi) {
    if(!Number.isSafeInteger(v)||v<lo||v>hi) throw new Error('Integer outside allowed range');
    return v;
  }
  function keys(x,expected) {
    if(!x||Object.getPrototypeOf(x)!==Object.prototype||Object.keys(x).sort().join(',')!==[...expected].sort().join(',')) throw new Error('Unexpected or missing fields');
  }
  function matrix(b) {
    if(!Array.isArray(b)||b.length<1||b.length>MAX_DIM||b.some(row=>!Array.isArray(row)||row.length!==b.length)) throw new Error('Invalid square matrix');
    for(let i=0;i<b.length;i++) for(let j=0;j<b.length;j++) {
      integer(b[i][j],-1000000,1000000);
      if(b[i][j]!==-b[j][i]) throw new Error('Matrix must be skew-symmetric');
    }
    return b.map(row=>row.slice());
  }
  function mutate(raw,k) {
    const b=matrix(raw),n=b.length;integer(k,0,n-1);
    const p=x=>x>0n?x:0n;
    return matrix(b.map((row,i)=>row.map((v,j)=> {
      if(i===k||j===k) return -v;
      const a=BigInt(b[i][k]),c=BigInt(b[k][j]);
      const result=BigInt(v)+p(a)*p(c)-p(-a)*p(-c);
      if(abs(result)>1000000n) throw new Error('Mutation output exceeds budget');
      return Number(result);
    })));
  }
  function seedStep(raw,x,k) {
    const b=matrix(raw);integer(k,0,b.length-1);
    if(!Array.isArray(x)||x.length!==b.length||x.some(v=>v[0]<=0n)) throw new Error('Positive rational seed required');
    if(b.some(row=>Math.abs(row[k])>64)) throw new Error('Exponent budget exceeded');
    let a=one,c=one;
    for(let i=0;i<x.length;i++) {a=mul(a,pow(x[i],Math.max(b[i][k],0)));c=mul(c,pow(x[i],Math.max(-b[i][k],0)));str(a);str(c);}
    const y=x.slice();y[k]=div(add(a,c),x[k]);str(y[k]);
    return {matrix:mutate(b,k),seed:y};
  }
  function tropicalStep(raw,u,k) {
    const b=matrix(raw);integer(k,0,b.length-1);
    if(!Array.isArray(u)||u.length!==b.length) throw new Error('Valuation dimension mismatch');
    u.forEach(v=>integer(v,-1000000,1000000));
    const a=u.reduce((s,v,i)=>s+BigInt(Math.max(b[i][k],0))*BigInt(v),0n);
    const c=u.reduce((s,v,i)=>s+BigInt(Math.max(-b[i][k],0))*BigInt(v),0n);
    const y=u.slice(),v=(a<c?a:c)-BigInt(u[k]);
    if(abs(v)>BigInt(Number.MAX_SAFE_INTEGER)) throw new Error('Valuation output overflow');
    y[k]=Number(v);return y;
  }
  function certificate(kind,inputs) {
    if(!Object.hasOwn(SCOPES,kind)) throw new Error('Unknown contract');
    let normalized,claim;
    if(kind==='heat') {
      keys(inputs,['r']);const r=parse(inputs.r);
      if(!le(zero,r)||!le(r,[1n,4n])) throw new Error('Positive-stencil boundary: 0 <= r <= 1/4');
      normalized={r:str(r)};claim={weights:[str(sub(one,mul([4n,1n],r))),...Array(4).fill(str(r))],sum:'1/1'};
    } else if(kind==='gain') {
      keys(inputs,['matrix','weights','rate']);
      if(!Array.isArray(inputs.weights)||inputs.weights.length<1||inputs.weights.length>MAX_DIM) throw new Error('Invalid weights');
      const n=inputs.weights.length;
      if(!Array.isArray(inputs.matrix)||inputs.matrix.length!==n||inputs.matrix.some(row=>!Array.isArray(row)||row.length!==n)) throw new Error('Gain dimension mismatch');
      const g=inputs.matrix.map(row=>row.map(parse)),w=inputs.weights.map(parse),q=parse(inputs.rate);
      if(g.some(row=>row.some(v=>!le(zero,v)))||w.some(v=>v[0]<=0n)||!le(zero,q)||le(one,q)) throw new Error('Invalid gain domain');
      const slack=g.map((row,i)=>sub(mul(q,w[i]),row.reduce((s,v,j)=>add(s,mul(v,w[j])),zero)));
      if(slack.some(v=>!le(zero,v))) throw new Error('Weighted gain inequality fails');
      normalized={matrix:g.map(row=>row.map(str)),weights:w.map(str),rate:str(q)};claim={row_slack:slack.map(str)};
    } else if(kind==='rank') {
      keys(inputs,['draws','exceedances']);const n=integer(inputs.draws,1,10000000),e=integer(inputs.exceedances,0,n);
      normalized={draws:n,exceedances:e};claim={p:str(rat(BigInt(e+1),BigInt(n+1))),resolution:str(rat(1n,BigInt(n+1)))};
    } else if(kind==='risk') {
      keys(inputs,['tests','per_test','drift','alpha']);const n=integer(inputs.tests,1,10000000);
      const p=parse(inputs.per_test),d=parse(inputs.drift),a=parse(inputs.alpha);
      if([p,d,a].some(v=>!le(zero,v)||!le(v,one))) throw new Error('Probabilities outside [0,1]');
      const total=add(mul([BigInt(n),1n],p),d);
      if(!le(total,a)) throw new Error('Family-wise risk budget exceeded');
      normalized={tests:n,per_test:str(p),drift:str(d),alpha:str(a)};claim={upper_bound:str(total),slack:str(sub(a,total))};
    } else {
      keys(inputs,['matrix','seed','vertex']);const b=matrix(inputs.matrix),k=integer(inputs.vertex,0,b.length-1);
      if(!Array.isArray(inputs.seed)) throw new Error('Seed must be a list');
      const x=inputs.seed.map(parse),y=seedStep(b,x,k);
      normalized={matrix:b,seed:x.map(str),vertex:k};claim={matrix:y.matrix,seed:y.seed.map(str)};
    }
    return {schema:SCHEMA,kind,inputs:normalized,claim,scope:SCOPES[kind]};
  }
  function canonical(x) {
    if(x===null||typeof x!=='object') return JSON.stringify(x);
    if(Array.isArray(x)) return '['+x.map(canonical).join(',')+']';
    return '{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+canonical(x[k])).join(',')+'}';
  }
  function replay(c) {
    keys(c,['schema','kind','inputs','claim','scope']);
    if(c.schema!==SCHEMA) throw new Error('Unknown schema');
    const expected=certificate(c.kind,c.inputs);
    if(canonical(c)!==canonical(expected)) throw new Error('Noncanonical or altered certificate');
    return expected;
  }
  function binary64(value) {
    if(!Number.isFinite(value)) throw new Error('A finite binary64 value is required');
    if(value===0) return '0/1';
    const b=new ArrayBuffer(8),v=new DataView(b);v.setFloat64(0,value,false);
    const bits=v.getBigUint64(0,false),sign=(bits>>63n)?-1n:1n;
    const exponent=Number((bits>>52n)&2047n),mantissa=bits&((1n<<52n)-1n);
    let n=sign*(exponent===0?mantissa:mantissa+(1n<<52n)),d=1n;
    const power=(exponent===0?-1022:exponent-1023)-52;
    if(power>=0) n<<=BigInt(power);else d<<=BigInt(-power);
    return str(rat(n,d));
  }
  async function digest(c) {
    replay(c);const bytes=new TextEncoder().encode(canonical(c));
    return Array.from(new Uint8Array(await globalThis.crypto.subtle.digest('SHA-256',bytes)),x=>x.toString(16).padStart(2,'0')).join('');
  }
  return {SCHEMA,SCOPES,parse,str,add,sub,mul,div,le,mutate,seedStep,tropicalStep,certificate,replay,canonical,binary64,digest};
});
