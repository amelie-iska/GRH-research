// Exact finite RG formulas, evaluated in floating point. No external runtime.
export const spins=n=>Array.from({length:2**n},(_,i)=>Array.from({length:n},(_,q)=>1-2*((i>>(n-1-q))&1)));
export const logsum=v=>{const a=Math.max(...v);return a+Math.log(v.reduce((s,x)=>s+Math.exp(x-a),0));};
export const pop=n=>{let c=0;while(n){c+=n&1;n>>=1;}return c;};
export function walsh(v,normalize=true){const a=v.slice();for(let h=1;h<a.length;h*=2)for(let i=0;i<a.length;i+=2*h)for(let j=0;j<h;j++){const x=a[i+j],y=a[i+h+j];a[i+j]=x+y;a[i+h+j]=x-y;}return normalize?a.map(x=>x/a.length):a;}
export const fields=m=>Array.from({length:m},(_,j)=>.045*Math.cos(1.7*j)+.02*j/m);
export function fineAction(m,[jp,jm,b]){return spins(m+2).map(s=>jp*s[0]*s.slice(2).reduce((x,y)=>x+y,0)+jm*s[1]*s.slice(2).reduce((x,y,j)=>x+y*(-1)**j,0)+b*s[0]-.6*b*s[1]+s.slice(2).reduce((x,y,j)=>x+y*fields(m)[j],0));}
export function marginal(v,keep){const n=Math.round(Math.log2(v.length)),groups=Array.from({length:2**keep.length},()=>[]);v.forEach((x,i)=>{let k=0;for(const q of keep)k=k*2+((i>>(n-1-q))&1);groups[k].push(x);});return groups.map(logsum);}
export function stats(v,sites){const c=walsh(v),z=logsum(v),p=v.map(x=>Math.exp(x-z)),s=spins(sites.length),ct=c.map((x,i)=>pop(i)>2?0:x),vt=walsh(ct,false),zt=logsum(vt);return{sites,v,c,logZ:z,higher:Math.hypot(...c.filter((_,i)=>pop(i)>2)),mag:sites.map((_,q)=>p.reduce((a,x,i)=>a+x*s[i][q],0)),truncation:zt-z,truncationTV:.5*p.reduce((a,x,i)=>a+Math.abs(Math.exp(vt[i]-zt)-x),0)};}
export function flow(m,params,initial=null){let labels=initial?Array.from({length:m},(_,j)=>j+2):Array.from({length:m+2},(_,j)=>j),v=initial??fineAction(m,params);const out=[];while(true){out.push(stats(v,labels));if(labels.length===1)break;const keep=out.length===1&&!initial?labels.map((_,j)=>j).filter(j=>j>=2):labels.map((_,j)=>j).filter(j=>j%2===0);v=marginal(v,keep);labels=keep.map(j=>labels[j]);}return out;}
export function transfer(K,h,C=0){const a=Math.exp(K+h),b=Math.exp(-K),d=Math.exp(K-h),x=a*a+b*b,y=b*(a+d),z=d*d+b*b;return[.25*Math.log(x*z/(y*y)),.5*Math.log(x/z),2*C+.25*Math.log(x*z*y*y)];}
export function chain(K,h,N=64){
 // Carry the exact log eigenratio coordinate: squaring T doubles log(r).
 // Re-diagonalizing rounded late-scale K can spuriously turn r into zero.
 let C=0,spacing=1;const initialA=Math.exp(K+h),initialB=Math.exp(-K),initialD=Math.exp(K-h),initialLp=(initialA+initialD+Math.hypot(initialA-initialD,2*initialB))/2;
 let logRatio=K>0?Math.log(2*Math.sinh(2*K))-2*Math.log(initialLp):-Infinity;
 const out=[];while(N>=1){const a=Math.exp(K+h),b=Math.exp(-K),d=Math.exp(K-h),lp=(a+d+Math.hypot(a-d,2*b))/2,xi=Number.isFinite(logRatio)?-1/logRatio:0;
 out.push({K,h,C,N,spacing,xi,physicalXi:spacing*xi,logZ:N*(C+Math.log(lp))+Math.log1p(Math.exp(N*logRatio))});
 if(N===1)break;[K,h,C]=transfer(K,h,C);N/=2;spacing*=2;logRatio*=2;
 }return out;
}
export function features(theta,x){const re=Array(8).fill(0),im=Array(8).fill(0);re[0]=1;const ry=(q,t)=>{const bit=1<<(2-q),c=Math.cos(t/2),s=Math.sin(t/2);for(let i=0;i<8;i++)if(!(i&bit)){const j=i|bit,a=re[i],b=re[j],u=im[i],v=im[j];re[i]=c*a-s*b;re[j]=s*a+c*b;im[i]=c*u-s*v;im[j]=s*u+c*v;}};const rz=(q,t)=>{for(let i=0;i<8;i++){const a=((i>>(2-q))&1)?t/2:-t/2,c=Math.cos(a),s=Math.sin(a),u=re[i],v=im[i];re[i]=c*u-s*v;im[i]=s*u+c*v;}};x.forEach((t,q)=>ry(q,t*[1.5,1.5,2][q]));for(let l=0;l<2;l++){for(let q=0;q<3;q++){ry(q,theta[l*6+q*2]);rz(q,theta[l*6+q*2+1]);}for(const[a,b]of[[0,1],[1,2],[2,0]])for(let i=0;i<8;i++)if((i&(1<<(2-a)))&&(i&(1<<(2-b)))){re[i]*=-1;im[i]*=-1;}}return Array.from({length:7},(_,k)=>re.reduce((a,r,i)=>a+(r*r+im[i]*im[i])*(-1)**pop(i&(k+1)),0));}
export function predict(model,x){const f=[...features(model.theta,x),1];return Array.from({length:32},(_,j)=>f.reduce((a,v,i)=>a+v*model.head[i][j],0)*model.target_scale+model.target_mean[j]);}
export function errorStats(pred,exact){const zp=logsum(pred),ze=logsum(exact),p=pred.map(x=>Math.exp(x-zp)),q=exact.map(x=>Math.exp(x-ze));return{mse:pred.reduce((a,x,i)=>a+(x-exact[i])**2,0)/pred.length,KL:q.reduce((a,x,i)=>a+x*((exact[i]-ze)-(pred[i]-zp)),0),TV:.5*p.reduce((a,x,i)=>a+Math.abs(x-q[i]),0),logZerror:zp-ze,sup:Math.max(...pred.map((x,i)=>Math.abs(x-exact[i])))};}
