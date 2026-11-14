// Exact discrete algebra and F2 chain calculations. BigInt encodes column bits.
const natural=n=>Number.isInteger(n)&&n>=0;
export function staircase(gens){
 if(!Array.isArray(gens)||gens.length<2||gens.some(g=>g.length!==2||g.some(n=>!natural(n)||n>12)))throw Error('Use at least two natural exponent pairs, each at most12');
 if(gens[0][1]!==0||gens.at(-1)[0]!==0||gens[0][0]===0||gens.at(-1)[1]===0)throw Error('First/last generators must be positive pure x/y powers');
 for(let i=1;i<gens.length;i++)if(gens[i][0]>=gens[i-1][0]||gens[i][1]<=gens[i-1][1])throw Error('Minimal staircase needs decreasing x and increasing y exponents');
 const syzygies=gens.slice(0,-1).map((g,i)=>({degree:[g[0],gens[i+1][1]],negativeY:gens[i+1][1]-g[1],positiveX:g[0]-gens[i+1][0]}));
 const model={gens:gens.map(g=>[...g]),syzygies,betti:[[[0,0]],gens.map(g=>[...g]),syzygies.map(s=>s.degree)],bounds:[gens[0][0],gens.at(-1)[1]]};
 model.basis=[];for(let a=0;a<model.bounds[0];a++)for(let b=0;b<model.bounds[1];b++)if(standard(model,[a,b]))model.basis.push([a,b]);
 return model;
}
function grade(g){if(!Array.isArray(g)||g.length!==2||!g.every(natural))throw Error('Grades must have two natural coordinates');}
export function comparable(a,b){return a[0]<=b[0]&&a[1]<=b[1];}
export function standard(model,g){grade(g);return !model.gens.some(m=>comparable(m,g));}
export function rankMap(model,from,to){grade(from);grade(to);if(!comparable(from,to))throw Error('No persistence map between incomparable grades');return Number(standard(model,from)&&standard(model,to));}
export function cwAt(model,g){grade(g);const cells=model.gens.map((m,i)=>comparable(m,g)?i:null).filter(i=>i!==null);return {disks:cells,h1:cells.length?0:1,h2:Math.max(0,cells.length-1)};}
const pivot=n=>n.toString(2).length-1;
export function gfRank(columns){
 const basis=new Map();
 for(const column of columns){let v=BigInt(column);if(v<0n)throw Error('Bit columns must be nonnegative');while(v){const p=pivot(v);if(basis.has(p))v^=basis.get(p);else{basis.set(p,v);break;}}}
 return basis.size;
}
export function kernel(columns){
 const basis=new Map(),result=[];
 columns.forEach((column,j)=>{let v=BigInt(column),combination=1n<<BigInt(j);while(v){const p=pivot(v);if(basis.has(p)){const b=basis.get(p);v^=b.v;combination^=b.c;}else{basis.set(p,{v,c:combination});return;}}result.push(combination);});
 return result;
}
export function specialized(model,x,y){
 if(![0,1].includes(x)||![0,1].includes(y))throw Error('The exact fiber display uses F2 points');
 const d1=model.gens.map(([a,b])=>BigInt((x**a*y**b)%2));
 const d2=model.syzygies.map((s,i)=>(BigInt(y**s.negativeY)<<BigInt(i))^(BigInt(x**s.positiveX)<<BigInt(i+1)));
 for(const column of d2){let v=0n;for(let i=0;i<d1.length;i++)if(column&(1n<<BigInt(i)))v^=d1[i];if(v)throw Error('Specialized maps do not form a complex');}
 const a=gfRank(d1),b=gfRank(d2),m=model.gens.length;
 return {d1:d1.map(Number),d2:d2.map(c=>model.gens.map((_,i)=>Number((c>>BigInt(i))&1n))),ranks:[a,b],homology:[1-a,m-a-b,m-1-b]};
}
export function monomial([a,b]){return (a?'x'+(a===1?'':'^'+a):'')+(a&&b?' ':'')+(b?'y'+(b===1?'':'^'+b):'')||'1';}
function key(simplex){return simplex.join(',');}
export function validateQuantum(data){
 const n=data.points.length;
 if(n>16||data.points.some((p,i)=>p.id!==i||!natural(p.birth)))throw Error('Invalid fixed vertex labels');
 for(const name of ['input_labels','output_labels']){
  const matrix=data[name];if(matrix.length!==n||matrix.some(r=>r.length!==n))throw Error('Invalid graph matrix');
  for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(!natural(matrix[i][j])||matrix[i][j]!==matrix[j][i]||i===j&&matrix[i][j]!==0)throw Error('Need symmetric natural graph labels and zero diagonal');
 }
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(data.output_labels[i][j]>data.input_labels[i][j])throw Error('Frozen output labels fail the stated inclusion condition');
 return data;
}
export function flagComplex(data,channel,r,e){
 if(!['input','output'].includes(channel)||!natural(r)||!natural(e))throw Error('Invalid fixed channel/grade');
 const labels=data[channel+'_labels'],vertices=data.points.filter(p=>p.birth<=e).map(p=>p.id),vi=new Map(vertices.map((v,i)=>[v,i])),edges=[],triangles=[];
 for(let i=0;i<vertices.length;i++)for(let j=i+1;j<vertices.length;j++)if(labels[vertices[i]][vertices[j]]<=r)edges.push([vertices[i],vertices[j]]);
 const ei=new Map(edges.map((edge,i)=>[key(edge),i]));
 for(let i=0;i<vertices.length;i++)for(let j=i+1;j<vertices.length;j++)for(let k=j+1;k<vertices.length;k++)if(ei.has(key([vertices[i],vertices[j]]))&&ei.has(key([vertices[i],vertices[k]]))&&ei.has(key([vertices[j],vertices[k]])))triangles.push([vertices[i],vertices[j],vertices[k]]);
 const d1=edges.map(([a,b])=>(1n<<BigInt(vi.get(a)))^(1n<<BigInt(vi.get(b))));
 const d2=triangles.map(([a,b,c])=>[key([a,b]),key([a,c]),key([b,c])].reduce((v,k)=>v^(1n<<BigInt(ei.get(k))),0n));
 for(const boundary of d2){let image=0n;d1.forEach((column,i)=>{if(boundary&(1n<<BigInt(i)))image^=column;});if(image)throw Error('Boundary square is nonzero');}
 const r1=gfRank(d1),r2=gfRank(d2),cycles=kernel(d1);
 return {vertices,edges,triangles,d1,d2,cycles,betti:[vertices.length-r1,edges.length-r1-r2],ranks:[r1,r2],grade:[r,e],channel};
}
export function inclusionRanks(source,target){
 const vi=new Map(target.vertices.map((v,i)=>[v,i])),ei=new Map(target.edges.map((e,i)=>[key(e),i])),faces=new Set(target.triangles.map(key));
 if(source.vertices.some(v=>!vi.has(v))||source.edges.some(e=>!ei.has(key(e)))||source.triangles.some(f=>!faces.has(key(f))))throw Error('Complexes are not related by the claimed identity inclusion');
 const cycles=source.cycles.map(c=>source.edges.reduce((v,e,i)=>c&(1n<<BigInt(i))?v^(1n<<BigInt(ei.get(key(e)))):v,0n));
 const points=source.vertices.map(v=>1n<<BigInt(vi.get(v)));
 return {h0:gfRank([...target.d1,...points])-gfRank(target.d1),h1:gfRank([...target.d2,...cycles])-gfRank(target.d2)};
}
