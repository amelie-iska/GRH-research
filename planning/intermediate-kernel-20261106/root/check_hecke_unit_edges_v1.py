from pathlib import Path
import math,json,hashlib
import mpmath as mp
mp.mp.dps=65
r=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
w=mp.mpc(-mp.mpf(1)/2,mp.sqrt(3)/2);delta=1+2*w
rows=[];tests=[]
def ck(n,p):
 tests.append({"name":n,"passed":bool(p)})
 if not p:raise AssertionError(n)
def tail(c,R):
 return 12*mp.exp(-c*R)*sum(mp.factorial(4)/mp.factorial(4-j)*R**(4-j)/c**j for j in range(5))
def theta(k,t,R):
 c=2*mp.pi*t/mp.sqrt(3);a=math.ceil(2*math.sqrt(R/3))+1;total=mp.mpc(0);count=0
 weights=[mp.exp(-c*n) for n in range(R+1)]
 for x in range(-a,a+1):
  for y in range(-a,a+1):
   N=x*x-x*y+y*y
   if N>R:continue
   if N==0:
    if k==0:total+=1
    continue
   z=x+y*w;P=z**k if k>=0 else mp.conj(z)**(-k)
   total+=P*weights[N];count+=1
 return total,count
for k in [0,6,-6]:
 root=mp.j**(-abs(k))*(delta/abs(delta))**k
 ck(f"unitconductor_root_k{k}",abs(root-1)<mp.mpf("1e-60"))
 for p,q in [(7,10),(13,10)]:
  t=mp.mpf(p)/q;c=2*mp.pi*t/mp.sqrt(3);d=2*mp.pi/t/mp.sqrt(3)
  R=math.ceil(max(130/c,130/d,1,abs(k)/(2*c)+1,abs(k)/(2*d)+1))
  v,n=theta(k,t,R);u,m=theta(k,1/t,R)
  expected=root*t**(-abs(k)-1)*mp.conj(u)
  budget=tail(c,R)+t**(-abs(k)-1)*tail(d,R)
  ck(f"unitconductor_Gaussian_FE_k{k}_t{p}over{q}",abs(v-expected)<budget+mp.mpf("1e-48"))
  if k==0:
   meromorphic_difference=(v-1)-t**-1*(u-1)
   ck(f"principal_zero_term_required_t{p}over{q}",abs(meromorphic_difference-(1/t-1))<budget+mp.mpf("1e-48"))
   ck(f"negative_omitted_polar_correction_t{p}over{q}",abs(meromorphic_difference)>mp.mpf("0.1"))
  rows.append({"k":k,"t":f"{p}/{q}","norm_cutoff":R,"nonzero_lattice_terms":[n,m],"residual":mp.nstr(abs(v-expected),12),"analytic_tail_budget_evaluated":mp.nstr(budget,12)})
note=r/"planning/intermediate-kernel-20261106/lane-c/GLOBAL_ROOT_MULTIPLICATION-v2.md"
d={"passed":True,"scope":"NEW unitconductor nonfinite-order angular plus principal meromorphic-zero-term consistency controls only; no old58 or old projectphase controls rerun","interval_enclosures":False,"mpmath":mp.__version__,"dps":mp.mp.dps,"count":len(tests),"checks":tests,"cases":rows,"proof_note_sha256":hashlib.sha256(note.read_bytes()).hexdigest(),"no_new_dependencies":True}
p=r/"outputs/checks/2026-11-06-intermediate-kernel/root/hecke-unit-edges-v1/controls-v1.json";p.parent.mkdir(parents=True,exist_ok=True)
with p.open("x") as f:f.write(json.dumps(d,indent=2)+"\n")
print(json.dumps({"passed":True,"checks":len(tests),"new_Gaussian_edge_cases":len(rows),"path":str(p.relative_to(r)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}))
