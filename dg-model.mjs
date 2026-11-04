// Exact index data for finite subcomplexes of the infinite polynomial model.
export function windowModel(mode,N){
 if(!['node','unit','zero'].includes(mode)||!Number.isInteger(N)||N<0||N>8)throw Error('Invalid DG window');
 const even=[],odd=[],arrows=[],bound=mode==='node'?N-1:N;
 for(let i=0;i<=N;i++)for(let j=0;j<=N;j++)even.push([i,j,0]);
 for(let i=0;i<=bound;i++)for(let j=0;j<=bound;j++){
  const p=[i,j,-1];odd.push(p);if(mode!=='zero')arrows.push([p,[i+(mode==='node'?1:0),j+(mode==='node'?1:0),0]]);
 }
 const rank=arrows.length;
 return {mode,N,even,odd,arrows,rank,homology:[odd.length-rank,even.length-rank]};
}
export function thetaExt(kind,n){
 if(!['elliptic','spherical'].includes(kind)||!Number.isInteger(n)||n<0||n>100)throw Error('Invalid theta input');
 return Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>n===0?Number(i===j):kind==='elliptic'?2*Number(j===((i-n)%3+3)%3):n%2===0?2*Number(i===j):Number(i!==j)));
}
