// Exact dart combinatorics; the accompanying prose proves the topology.
export function dessinCellModel(m,filled=false){
 if(![3,5,9].includes(m))throw Error('Use the specified odd-valence dessin families');
 const sigma=Array.from({length:2*m},(_,i)=>Math.floor(i/m)*m+(i+1)%m),alpha=Array.from({length:2*m},(_,i)=>(i+m)%(2*m)),inverse=Array(2*m);sigma.forEach((v,i)=>inverse[v]=i);
 const face=inverse.map(i=>alpha[i]),seen=new Set(),cycles=[];
 for(let i=0;i<2*m;i++)if(!seen.has(i)){const c=[];let j=i;while(!seen.has(j)){seen.add(j);c.push(j);j=face[j];}cycles.push(c);}
 const genus=(m-1)/2,rank=m-1,word=Array.from({length:genus},(_,i)=>`[a${i+1},b${i+1}]`).join(' ');
 return {m,vertices:m+2,edges:2*m,faces:cycles.length,genus,rank,sigma,alpha,face,cycles,filled,euler:filled?3-m:2-m,H1:rank,H2:filled?1:0,
 fundamental:filled?(genus===1?'Z²':`surface group ⟨a₁,b₁,… | ${word}=1⟩`):`free group F${rank}`,word,
 cover:filled?(genus===1?'plane with lifted 2-cells':'hyperbolic disk with lifted 2-cells'):'tree of the original dessin (not a filled-surface cover)'};
}
