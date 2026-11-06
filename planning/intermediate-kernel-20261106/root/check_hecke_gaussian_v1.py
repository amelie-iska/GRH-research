from pathlib import Path
from fractions import Fraction
import math,json,hashlib,sys
import mpmath as mp
mp.mp.dps=65
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
OUT=ROOT/"outputs/checks/2026-11-06-intermediate-kernel/root/hecke-gaussian-v1";OUT.mkdir(parents=True,exist_ok=True)
omega=mp.mpc(-mp.mpf(1)/2,mp.sqrt(3)/2);eps=1+omega;delta=1+2*omega
zeta=[eps**j for j in range(6)]
checks=[];rows=[]
def ck(n,v):
 checks.append({"name":n,"passed":bool(v)})
 if not v:raise AssertionError(n)
def norm(g):a,b=g;return a*a-a*b+b*b
def mul(g,h):
 a,b=g;c,d=h;return (a*c-b*d,a*d+b*c-b*d)
def val(g):a,b=g;return mp.mpf(a)+b*omega
def theta_p(a,b,p,t,conj=False):
 v=(a+b*t)%p
 if not v:return None
 v=pow(v,(p-1)//6,p);e=(1+t)%p
 j=next(j for j in range(6) if pow(e,j,p)==v)
 return (-j if conj else j)%6
def t7(a,b):return theta_p(a,b,7,2)
def tb19(a,b):return theta_p(a,b,19,7,True)
def t2(a,b):
 a%=2;b%=2
 if(a,b)==(0,0):return None
 return {(1,0):0,(1,1):2,(0,1):4}[(a,b)]
def tp(a,b):
 q=[t7(a,b),tb19(a,b),t2(a,b)]
 return None if None in q else sum(q)%6
items=[("xi7",(1,3),-1,t7),("barxi19",(-2,3),3,tb19),("sigma2",(2,0),-2,t2)]
gam=mul(mul(items[0][1],items[1][1]),items[2][1])
items.append(("product",gam,0,tp))
units=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def gauss(g,th):
 c,d=g;N=norm(g);h=math.gcd(abs(c),abs(d));w=N//h
 seen=set();s=mp.mpc(0);zeros=0
 for a in range(w):
  for b in range(h):
   # independent residue-class witness via inverse multiplication coordinates
   key=(((c-d)*a+d*b)%N,(-d*a+c*b)%N);seen.add(key)
   ex=th(a,b)
   if ex is None:zeros+=1;continue
   phase=mp.exp(2j*mp.pi*mp.mpf(c*b-d*a)/N)
   s+=zeta[ex]*phase
 ck(f"quotient_representatives_N{N}",len(seen)==N)
 return s,zeros
def unit(z):return z/abs(z)
def root(g,k,th):
 tau,zeros=gauss(g,th);return mp.j**(-abs(k))*unit(delta*val(g))**k*tau/mp.sqrt(norm(g)),tau,zeros
roots=[]
for name,g,k,th in items:
 for j,u in enumerate(units):
  ex=th(*u);ck(name+f"_global_unit_compatibility_{j}",ex is not None and (ex+k*j)%6==0)
 er,tau,zeros=root(g,k,th);roots.append(er)
 ck(name+"_primitive_gauss_magnitude",abs(abs(tau)**2-norm(g))<mp.mpf("1e-55"))
 ck(name+"_root_modulus_one",abs(abs(er)-1)<mp.mpf("1e-55"))
 gu=mul(g,(1,1));eru,_,_=root(gu,k,th)
 ck(name+"_generator_change_compensates",abs(eru-er)<mp.mpf("1e-55"))
 rows.append({"name":name,"gamma":g,"norm":norm(g),"k":k,"Gauss":[mp.nstr(tau.real,45),mp.nstr(tau.imag,45)],"root":[mp.nstr(er.real,45),mp.nstr(er.imag,45)],"raw_zero_residues":zeros})
def chi(g,k,th):
 j=th(*g)
 assert j is not None
 return zeta[j]*unit(val(g))**k
cross=mp.mpc(1)
for i,(_,g,k,th) in enumerate(items[:3]):
 for j,(_,gj,_,_) in enumerate(items[:3]):
  if i!=j:cross*=chi(gj,k,th)
arch=mp.j**(sum(abs(q[2]) for q in items[:3])-abs(sum(q[2] for q in items[:3])))
rhs=arch*mp.fprod(roots[:3])*cross
ck("nontrivial_triple_arch_correction_minus_one",abs(arch+1)<mp.mpf("1e-60"))
ck("primitive_global_triple_root_identity",abs(roots[3]-rhs)<mp.mpf("1e-53"))
ck("omitting_triple_arch_correction_is_rejected",abs(roots[3]-rhs/arch)>mp.mpf("1.9"))
rad=[Fraction(3,7),Fraction(-2,5),Fraction(-1,35)]
ck("radial_types_sum_exactly_zero",sum(rad)==0)
radroots=mp.mpc(1);radcross=mp.mpc(1)
for i,(_,g,k,th) in enumerate(items[:3]):
 t=mp.mpf(rad[i].numerator)/rad[i].denominator
 radroots*=roots[i]*mp.exp(mp.j*t*mp.log(3*norm(g)))
 for j,(_,gj,_,_) in enumerate(items[:3]):
  if i!=j:radcross*=chi(gj,k,th)*mp.exp(mp.j*t*mp.log(norm(gj)))
ck("nonzero_radial_twists_cancel_in_actual_triple_law",abs(roots[3]-arch*radroots*radcross)<mp.mpf("1e-53"))
def tail(c,R):
 # r<=3 and R>=max(1,r/(2c)); count of nonzero Eisenstein elements <=12X
 return 12*mp.exp(-c*R)*(R**3+3*R**2/c+6*R/c**2+6/c**3)
def theta_sum(th,k,g,t,R):
 r=abs(k);N=norm(g);c=2*mp.pi*t/mp.sqrt(3*N)
 weights=[mp.exp(-c*n) for n in range(R+1)]
 m=math.ceil(2*math.sqrt(R/3))+1;s=mp.mpc(0);terms=0
 for a in range(-m,m+1):
  for b in range(-m,m+1):
   n=a*a-a*b+b*b
   if n==0 or n>R:continue
   ex=th(a,b)
   if ex is None:continue
   q=val((a,b));harm=q**r if k>=0 else mp.conj(q)**r
   s+=zeta[ex]*harm*weights[n];terms+=1
 return s,terms,c
for idx,(name,g,k,th) in enumerate(items):
 for ts in [Fraction(7,10),Fraction(13,10)]:
  t=mp.mpf(ts.numerator)/ts.denominator;r=abs(k);N=norm(g)
  c1=2*mp.pi*t/mp.sqrt(3*N);c2=2*mp.pi/t/mp.sqrt(3*N)
  R=math.ceil(max(130/c1,130/c2,1,r/(2*c1)+1,r/(2*c2)+1))
  lhs,n1,_=theta_sum(th,k,g,t,R)
  oth,n2,_=theta_sum(th,k,g,1/t,R)
  pred=roots[idx]*t**(-r-1)*mp.conj(oth)
  err=abs(lhs-pred);budget=tail(c1,R)+t**(-r-1)*tail(c2,R)
  ck(name+f"_Gaussian_theta_FE_t{ts}",err<mp.mpf("1e-45")+budget)
  if idx==0 and ts==Fraction(7,10):
   wrong=mp.j**(-abs(k))*rows[idx]["norm"]**0 # diagnostic below uses actual tau
   tau=mp.mpc(*[mp.mpf(x) for x in rows[idx]["Gauss"]])
   wrongroot=mp.j**(-abs(k))*tau/mp.sqrt(N)
   ck("omitting_angular_different_factor_fails_Gaussian_FE",abs(lhs-wrongroot*t**(-r-1)*mp.conj(oth))>mp.mpf("0.01"))
  rows[idx].setdefault("theta_controls",[]).append({"t":str(ts),"norm_cutoff":R,"nonzero_character_lattice_terms":[n1,n2],"theta":[mp.nstr(lhs.real,40),mp.nstr(lhs.imag,40)],"FE_residual":mp.nstr(err,10),"analytic_Gaussian_tail_budget_evaluated":mp.nstr(budget,10)})
d={"passed":True,"scope":"NEW explicit unitary Hecke Gaussian functional-equation/CRT/radial consistency fixtures, NOT original arithmetic-family data or an analytic proof by numerical output","interval_enclosures":False,"mpmath":mp.__version__,"dps":mp.mp.dps,"checks":checks,"count":len(checks),"fixtures":rows,"triple_arch_correction":-1,"radial_types":[str(t) for t in rad],"no_randomness":True,"no_old_phase_law_tables_rerun":True,"inverse_different_pairing":"Tr((a+b omega)/(delta*(c+d omega)))=(c*b-d*a)/N(c+d omega)","existing_approved_pure_python_mpmath_readonly":True}
p=OUT/"controls-v1.json"
with p.open("x") as f:f.write(json.dumps(d,indent=2)+"\n")
print(json.dumps({"passed":True,"checks":len(checks),"Gauss_norms":[norm(q[1]) for q in items],"theta_FE_controls":8,"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}))
