export const elementColors={1:'#FFFFFF',6:'#909090',7:'#3050F8',8:'#FF0D0D',16:'#FFFF30',9:'#90E050',11:'#AB5CF2',12:'#8AFF00',13:'#BFA6A6',14:'#F0C8A0',15:'#FF8000',17:'#1FF01F',19:'#8F40D4',20:'#3DFF00',22:'#BFC2C7',26:'#E06633',27:'#F090A0',28:'#50D050',29:'#C88033',30:'#7D80B0',35:'#A62929',53:'#940094'};
export const radii={1:1.2,6:1.7,7:1.55,8:1.52,16:1.8};
export function graphWavelet(spectrum,center,scale){
 if(!Number.isInteger(center)||center<0||center>=spectrum.eigenvalues.length||!(scale>0))throw Error('Valid graph center and positive scale required');
 const {eigenvalues:e,eigenvectors:v}=spectrum;
 return v.map(row=>row.reduce((sum,value,k)=>sum+value*scale*e[k]*Math.exp(-scale*e[k])*v[center][k],0));
}
const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],conj=a=>[a[0],-a[1]];
export function circuitOccupation(example,steps){
 const circuit=example.circuit,c=example.electronic?.conditions;
 if(!circuit?.kind.includes('adjacent-Givens')||!c)throw Error('Number-conserving Givens replay unavailable');
 const n=circuit.modes;if(!Number.isInteger(steps)||steps<0||steps>circuit.gates.length)throw Error('Circuit step out of range');
 const P=c.initial_occupation_matrix_real.map((r,i)=>r.map((v,j)=>[v,c.initial_occupation_matrix_imag[i][j]]));
 for(const gate of circuit.gates.slice(0,steps)){
  if(gate.kind==='orbital phase'){
   const i=gate.wires[0],phase=[Math.cos(gate.angle),Math.sin(gate.angle)];
   for(let j=0;j<n;j++)P[i][j]=mul(phase,P[i][j]);for(let j=0;j<n;j++)P[j][i]=mul(P[j][i],conj(phase));
  }else{
   const [i,j]=gate.wires,B=gate.matrix_real.map((r,a)=>r.map((x,b)=>[x,gate.matrix_imag[a][b]]));
   for(let k=0;k<n;k++){const a=P[i][k],b=P[j][k];P[i][k]=add(mul(B[0][0],a),mul(B[0][1],b));P[j][k]=add(mul(B[1][0],a),mul(B[1][1],b));}
   for(let k=0;k<n;k++){const a=P[k][i],b=P[k][j];P[k][i]=add(mul(a,conj(B[0][0])),mul(b,conj(B[0][1])));P[k][j]=add(mul(a,conj(B[1][0])),mul(b,conj(B[1][1])));}
  }
 }
 return P.map((r,i)=>r[i][0]);
}
export function fieldColor(value,extent=1){const a=Math.max(-1,Math.min(1,value/Math.max(extent,1e-10))),t=Math.abs(a);return a<0?`rgb(${Math.round(170-120*t)},${Math.round(210-95*t)},${Math.round(230+20*t)})`:`rgb(${Math.round(220+35*t)},${Math.round(220-115*t)},${Math.round(200-150*t)})`;}
