// Finite endomorphisms in the explicitly specified full branch subcategory.
export const jordan=(lambda,n)=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?lambda:Number(i===j+1)));
export const identity=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>Number(i===j)));
export function multiply(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((t,a,k)=>t+a*B[k][j],0)));}
export function power(A,p){let out=identity(A.length);for(let k=0;k<p;k++)out=multiply(A,out);return out;}
export function rank(A){const B=A.map(row=>row.slice());let r=0;for(let j=0;j<(B[0]?.length??0)&&r<B.length;j++){const pivot=B.findIndex((row,i)=>i>=r&&Math.abs(row[j])>1e-10);if(pivot<0)continue;[B[r],B[pivot]]=[B[pivot],B[r]];const d=B[r][j];B[r]=B[r].map(x=>x/d);for(let i=0;i<B.length;i++)if(i!==r){const c=B[i][j];B[i]=B[i].map((x,k)=>x-c*B[r][k]);}r++;}return r;}
export function matrix(kind,lambda,n){if(kind!=='mixed')return jordan(lambda,n);const blocks=[jordan(0,3),jordan(0,1),jordan(1,2)],out=Array.from({length:6},()=>Array(6).fill(0));let off=0;for(const b of blocks){b.forEach((row,i)=>row.forEach((x,j)=>out[i+off][j+off]=x));off+=b.length;}return out;}
export function filtration(T){const n=T.length,kernel=Array.from({length:n+2},(_,p)=>n-rank(power(T,p)));return {kernel,image:kernel.map(k=>n-k),blocks:kernel.slice(1,n+1).map((_,i)=>({size:i+1,count:2*kernel[i+1]-kernel[i]-kernel[i+2]})).filter(x=>x.count>0),nilpotent:rank(power(T,n))===0};}
export function basisSupport(T,p,mode){const A=power(T,p);return A.map((_,j)=>mode==='kernel'?A.every(row=>Math.abs(row[j])<1e-10):rank(A.map((row,i)=>[...row,Number(i===j)]))===rank(A));}
export function monodromyDet(kind,lambda,n,m,z){return kind==='mixed'?(1-z**m)**2:(1-lambda*z**m)**n;}
