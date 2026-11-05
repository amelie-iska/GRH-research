#!/usr/bin/env python3
"""Fresh exact orientation/profile/raw-mask controls. No old Gauss/training reruns."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,math,subprocess
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');B=R/'planning/signed-profile-20261105/joint-attempt';O=R/'outputs/checks/2026-11-05-signed-profile/joint-attempt'
ZERO=(0,0);ONE=(1,0);ZETA=[ONE,(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def za(a,b):return(a[0]+b[0],a[1]+b[1])
def zm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def zc(a):return(a[0]+a[1],-a[1])
def zs(n,a):return(n*a[0],n*a[1])
def zn(a):return a[0]**2+a[0]*a[1]+a[1]**2
def en(a):return a[0]**2-a[0]*a[1]+a[1]**2
def em(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def epow(a,n):
 out=(1,0)
 for _ in range(n):out=em(out,a)
 return out
primes=[(1,3),(4,3),(7,-3),(7,9),(-8,3)];PN=[en(p) for p in primes];assert PN==[7,13,79,67,97]
D,U=4000,63;assert F(2*D,7)<=U*U<=D
checks=0;fields=[]
for a,b in primes:
 p=en((a,b));w=(-a*pow(b,-1,p))%p;roots=[pow(1+w,j,p) for j in range(6)];assert (w*w+w+1)%p==0 and len(set(roots))==6;fields.append((p,w,{z:j for j,z in enumerate(roots)}));checks+=1

def symbol(mask,u):
 exponent=0
 for j,(p,w,roots) in enumerate(fields):
  if mask>>j&1:
   z=(u[0]+u[1]*w)%p
   if not z:return None
   exponent+=roots[pow(z,(p-1)//6,p)]
 return exponent%6

def ideals(mask):return [primes[j] for j in range(5) if mask>>j&1]
def normmask(mask):return math.prod(PN[j] for j in range(5) if mask>>j&1)
def genmask(mask):
 out=(1,0)
 for pi in ideals(mask):out=em(out,pi)
 return out

def count_r(mask):
 N=normmask(mask)
 return sum(normmask(s)>U and N//normmask(s)>U for s in range(32) if s&~mask==0)
allmask=31;active=[]
for mask in range(32):
 t=allmask^mask;Nm,Nn=normmask(mask),normmask(t)
 if D<=Nm<=2*D and D<=Nn<=2*D:
  r=count_r(mask);rr=count_r(t);mu=(-1)**mask.bit_count();mut=(-1)**t.bit_count();AU=mu*(r-1);AN=mut*(rr-1);e=symbol(mask,(1,1));ee=symbol(t,(1,1));assert e==(Nm-1)//6%6 and ee==(Nn-1)//6%6;assert en(genmask(mask))==Nm
  W=zs(1 if AU>0 else -1,ZETA[-e%6]);WN=zs(1 if AN>0 else -1,ZETA[-ee%6]);a0=zs((r-1)*(rr-1),zm(W,zc(WN)));a=zm(a0,ZETA[(e-ee)%6]);muq=(-1)**5;aligned=zs(muq,a)
  assert r==rr==2 and aligned==(abs(AU*AN),0)==ONE
  active.append(dict(mask=mask,tmask=t,Nm=Nm,Nn=Nn,generator=genmask(mask),r_U=r,A_U=AU,epsilon_phase=e,theta_epsilon_phase=(e-ee)%6,W=W,a_AA=a,a_without_unit_phase=a0,signs=[1 if mask>>j&1 else -1 for j in range(5)]));checks+=4
assert len(active)==4 and sorted((a['Nm'],a['Nn']) for a in active)==[(6097,7663),(6499,7189),(7189,6499),(7663,6097)];checks+=1
right=ZERO;wrong=ZERO
for a in active:right=za(right,zs(-1,a['a_AA']));wrong=za(wrong,zs(-1,a['a_without_unit_phase']))
assert right==(4,0) and wrong==(-1,0);checks+=1
# The complete norm[10,20] good primary ideal set; r6 is NOT squarefree-restricted.
V=sorted((a,b) for a in range(-12,13) for b in range(-12,13) if a%3==1 and b%3==0 and 10<=en((a,b))<=20 and en((a,b))%2 and en((a,b))%3)
assert len(V)==4 and sorted(en(v) for v in V)==[13,13,19,19];checks+=1
survivors=[];direct=ZERO;Gammas=[]
for a in active:
 gamma=ZERO
 for v in V:
  beta6=epow(v,6);u=em((1,1),beta6);x=symbol(a['mask'],u);y=symbol(a['tmask'],u);x6=symbol(a['mask'],beta6);y6=symbol(a['tmask'],beta6)
  if x6 is not None and y6 is not None:gamma=za(gamma,ZETA[(x6-y6)%6])
  if x is not None and y is not None:
   Wm=a['W'];t=next(t for t in active if t['mask']==a['tmask']);val=zm(zm(zs(a['A_U'],zm(ZETA[x],Wm)),zc(zs(t['A_U'],zm(ZETA[y],t['W'])))),ONE);assert val==ONE;direct=za(direct,val)
  else:assert x6 is None or y6 is None
  checks+=1
 Gammas.append(gamma)
assert Gammas==[(3,0)]*4 and direct==(12,0);checks+=2
mean=zs(F(1,4),tuple(map(sum,zip(*Gammas))));variance=sum(zn((g[0]-mean[0],g[1]-mean[1])) for g in Gammas);assert variance==0 and F(direct[0],D)==F(3,1000);checks+=1
# Exact finite phase group; not the huge residue group and not the old joint Gauss check.
J=len(active);k=5;N=6**k;coherent=0;total_energy=coherent_energy=0;gram=[[ZERO for _ in active] for _ in active];cutgram=[[ZERO for _ in active] for _ in active]
for phase in product(range(6),repeat=k):
 vals=[ZETA[sum(s*e for s,e in zip(a['signs'],phase))%6] for a in active];A=ZERO
 for a,theta in zip(active,vals):A=za(A,zm(a['a_AA'],zc(theta)))
 total_energy+=zn(A);isc=all(e in (0,3) for e in phase)
 if isc:coherent+=1;coherent_energy+=zn(A);assert len(set(vals))==1
 for i in range(J):
  for j in range(J):
   z=zm(vals[i],zc(vals[j]));gram[i][j]=za(gram[i][j],z)
   if isc:cutgram[i][j]=za(cutgram[i][j],z)
 checks+=1
assert coherent==2**k and total_energy==N*J and F(coherent_energy,total_energy)==F(J,3**k);checks+=3
for i in range(J):
 for j in range(J):assert gram[i][j]==(N if i==j else 0,0) and cutgram[i][j]==(2**k,0);checks+=1
lam=F(J,3**k);T=[[F(1,3**k) for _ in active] for _ in active];T2=[[sum(T[i][a]*T[a][j] for a in range(J)) for j in range(J)] for i in range(J)];assert all(T2[i][j]==lam*T[i][j] for i in range(J) for j in range(J));assert lam*(1-lam)==F(956,59049);checks+=2
# Exact fresh bookkeeping for the two NEW remaining sectors, not an old exponent sweep.
assert (F(7,6)+F(7,12)+1)/2==F(11,8) and (F(7,6)+F(3,4)+1)/2==F(35,24);assert F(11,8)>F(7,6) and F(35,24)>F(7,6);assert 1+F(3,4)/6==F(9,8) and F(7,6)-F(9,8)==F(1,24);checks+=3
pins=json.loads((B/'source-pins-v1.json').read_text())
for n,v in pins['files'].items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==v['sha256'];checks+=1
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()==pins['source_HEAD'];idx=Path(subprocess.check_output(['git','rev-parse','--git-path','index'],cwd=R,text=True).strip());assert hashlib.sha256(idx.read_bytes()).hexdigest()==pins['source_index_sha256'];checks+=2
report={'passed':True,'new_exact_control_units':checks,'D':D,'U':U,'good_column_prime_generators':primes,'prime_norms':PN,'q_ideal_norm':math.prod(PN),'mu_q':-1,'active_orientations':active,'r6_generator_set':V,'r6_surviving_correlation_per_orientation':3,'Gamma_orientation_variance':str(variance),'exact_selected_h1_AA_contribution':str(F(direct[0],D)),'signed_coefficient_sum_with_unit_phase':right,'wrong_sum_omitting_unit_phase':wrong,'phase_group_size':N,'coherent_phase_tuples':coherent,'coherent_A_energy_fraction':str(F(coherent_energy,total_energy)),'compression_eigenvalue':str(lam),'coherent_projection_leakage_squared':str(lam*(1-lam)),'source_HEAD':pins['source_HEAD'],'source_index_sha256':pins['source_index_sha256'],'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Fresh finite signs/orientation/rawmask/projection bookkeeping only. No old991 Gauss or accepted learning traces rerun. No varying-family upper bound, fullh1lower bound, fixedWcounterexample or GRH claim.'}
p=O/'projection-profile-v1.json'
with p.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({k:report[k] for k in ['passed','new_exact_control_units','active_orientations','r6_surviving_correlation_per_orientation','Gamma_orientation_variance','exact_selected_h1_AA_contribution','wrong_sum_omitting_unit_phase','coherent_A_energy_fraction','coherent_projection_leakage_squared']},indent=2))
