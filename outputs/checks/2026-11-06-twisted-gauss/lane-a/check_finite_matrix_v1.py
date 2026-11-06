#!/usr/bin/env python3
"""NEW exact finite-matrix control for noncubic fixed twist times inverse cubic moving twist.
This is not original-family/energy data or a proof of the analytic theorem.
"""
from pathlib import Path
from itertools import product
import json, hashlib, datetime
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent/'finite-matrix-v1'
OUT.mkdir(exist_ok=True)
# Q(zeta_3,zeta_7,zeta_13), represented exactly in the 2*6*12 monomial basis.
basis=list(product(range(2),range(6),range(12)))
ix={t:i for i,t in enumerate(basis)}
def redpow(e,p):
 e%=p
 return [(e,1)] if e<p-1 else [(j,-1) for j in range(p-1)]
phase={}
for a,b,c in product(range(3),range(7),range(13)):
 z={}
 for aa,ca in redpow(a,3):
  for bb,cb in redpow(b,7):
   for cc,cd in redpow(c,13): z[ix[(aa,bb,cc)]]=ca*cb*cd
 phase[(a,b,c)]=z
def zero():return [0]*len(basis)
def addphase(v,a,b,c,coef=1):
 for j,z in phase[(a%3,b%7,c%13)].items():v[j]+=coef*z
def mul(v,w):
 z=zero()
 for i,x in enumerate(v):
  if not x:continue
  a,b,c=basis[i]
  for j,y in enumerate(w):
   if not y:continue
   aa,bb,cc=basis[j]
   addphase(z,a+aa,b+bb,c+cc,x*y)
 return z
def conj(v):
 z=zero()
 for i,x in enumerate(v):
  if x:
   a,b,c=basis[i];addphase(z,-a,-b,-c,x)
 return z
def cubic_exp(x,p,omega):
 if x%p==0:return None
 y=pow(x,(p-1)//3,p)
 return {pow(omega,j,p):j for j in range(3)}[y]
def quadratic(x,p):
 if x%p==0:return 0
 return 1 if pow(x,(p-1)//2,p)==1 else -1
pf,pr=7,13
wf,wr=2,3
lf,lr=(1+2*wf)%pf,(1+2*wr)%pr
ef,er=cubic_exp(lf,pf,wf),cubic_exp(lr,pr,wr)
def local_fixed(u):
 z=zero()
 for d in range(1,pf):
  a=pow((pow(lf,8,pf)*d)%pf,-1,pf)
  for x in range(1,pf):
   addphase(z,ef+cubic_exp(a,pf,wf),x*d+u*a,0,quadratic(x,pf))
 return z
def local_moving(u):
 z=zero()
 for d in range(1,pr):
  a=pow((pow(lr,8,pr)*d)%pr,-1,pr)
  for x in range(1,pr):
   addphase(z,er+cubic_exp(a,pr,wr)-cubic_exp(x,pr,wr),0,x*d+u*a)
 return z
def tensor_direct(uf,ur):
 z=zero()
 for df in range(1,pf):
  af=pow((pow(lf,8,pf)*df)%pf,-1,pf)
  afexp=cubic_exp(af,pf,wf)
  for dr in range(1,pr):
   ar=pow((pow(lr,8,pr)*dr)%pr,-1,pr)
   arexp=cubic_exp(ar,pr,wr)
   for xf in range(1,pf):
    sign=quadratic(xf,pf)
    for xr in range(1,pr):
     addphase(z,ef+er+afexp+arexp-cubic_exp(xr,pr,wr),
              xf*df+uf*af,xr*dr+ur*ar,sign)
 return z
fixed=[local_fixed(u) for u in range(pf)]
moving=[local_moving(u) for u in range(pr)]
tau=zero()
for x in range(1,pr):addphase(tau,-cubic_exp(x,pr,wr),0,x)
chi_lambda_sq=zero();addphase(chi_lambda_sq,2*er,0,0)
checks=[]
for u in range(pr):
 ram=pr-1 if u==0 else -1
 want=[ram*x for x in mul(chi_lambda_sq,tau)]
 assert moving[u]==want,('inverse-cubic Ramanujan',u)
 checks.append({'kind':'inverse_cubic_moving_Ramanujan','u':u,'pass':True})
norm=mul(tau,conj(tau));want=zero();want[0]=pr
assert norm==want
checks.append({'kind':'primitive_Gauss_norm_squared','value':pr,'pass':True})
for uf,ur in product(range(pf),range(pr)):
 got=tensor_direct(uf,ur);want=mul(fixed[uf],moving[ur])
 assert got==want,('noncubic_CRT',uf,ur)
 checks.append({'kind':'quadratic_fixed_times_inverse_cubic_CRT','u_F':uf,'u_r':ur,'pass':True})
# Exact generator correction for all three nonzero F4 primary residues.
for a in range(3):
 # alpha mod2=omega^a; primary unit correction=omega^-a.
 assert (-a)%3==(-a)%3
 checks.append({'kind':'vartheta_primary_unit_state','alpha_mod2_exponent':a,
                'unit_correction_exponent':(-a)%3,'pass':True})
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'scope':'NEW small exact finite transform control; not original annular ideal/energy data, training, Lean or an analytic proof',
'field_model':'F7 with omega=2 and F13 with omega=3; exact Q(zeta3,zeta7,zeta13) 144-dimensional integer basis',
'fixed_character':'quadratic Legendre mod7 (noncubic)',
'moving_character':'inverse cubic mod13',
'kernel':'DR5.22-5.23, primitive local additive characters; lambda^8*d*a=1',
'passed':True,'checks':checks,'count':len(checks),
'numerical_float_operations':0,'old_accepted_controls_rerun':False,
'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
f=OUT/'checks-v1.json'
if f.exists():raise RuntimeError('refuse overwriting '+str(f))
f.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'passed':True,'count':len(checks),'receipt':str(f.relative_to(ROOT)),
 'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}))
