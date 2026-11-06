from pathlib import Path
from fractions import Fraction
import math,json,hashlib
import mpmath as mp
mp.mp.dps=65
r=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
tests=[];rows=[]
def ck(n,p):
 tests.append({"name":n,"passed":bool(p)})
 if not p:raise AssertionError(n)
def sig(t):
 if t<=0:return mp.mpf(0)
 if t>=1:return mp.mpf(1)
 a=mp.exp(-1/t);b=mp.exp(-1/(1-t));return a/(a+b)
def sd(t):
 if t<=0 or t>=1:return mp.mpf(0),mp.mpf(0)
 v=sig(t);g=t**-2+(1-t)**-2;g2=-2*t**-3+2*(1-t)**-3
 return v*(1-v)*g,v*(1-v)*((1-2*v)*g*g+g2)
h0=2*mp.sqrt(2);h1=mp.sqrt(2)+2*mp.sqrt(mp.mpf(5)/2)
h2=mp.sqrt(2)/2+4*mp.sqrt(mp.mpf(5)/2)+832*(mp.mpf(5)/2)**mp.mpf("1.5")
C=3/(4*mp.pi**2)
for f,b in [(Fraction(1),1),(Fraction(7,3),4),(Fraction(37),41)]:
 A=mp.mpf(f.numerator)/f.denominator;a=math.ceil(f)
 cuts=[(a-mp.mpf(1)/2)/A,(a-mp.mpf(1)/4)/A,(b+mp.mpf(1)/4)/A,(b+mp.mpf(1)/2)/A]
 vc=[mp.log(q) for q in cuts]
 def G(y):return sig(4*(A*y-a+mp.mpf(1)/2))*sig(4*(b+mp.mpf(1)/2-A*y))
 def deriv(y):
  u=4*(A*y-a+mp.mpf(1)/2);v=4*(b+mp.mpf(1)/2-A*y);su=sig(u);sv=sig(v);du,ddu=sd(u);dv,ddv=sd(v)
  return 4*A*(du*sv-su*dv),(4*A)**2*(ddu*sv-2*du*dv+su*ddv)
 def H(v):y=mp.exp(v);return mp.exp(v/2)*G(y)
 def Hpp(v):
  y=mp.exp(v);gp,gpp=deriv(y)
  return mp.exp(v/2)*(G(y)/4+2*y*gp+y*y*gpp)
 for T in [0,1,3,17,79]:
  t=mp.mpf(T)
  direct=mp.quad(lambda y:G(y)*y**(-mp.mpf(1)/2-mp.j*t),cuts)
  fourier=mp.quad(lambda v:H(v)*mp.exp(-mp.j*t*v),vc)
  ck(f"log_substitution_A{f}_t{T}",abs(direct-fourier)<mp.mpf("1e-45"))
  ck(f"H0_bound_A{f}_t{T}",abs(direct)<=h0)
  gamma=C**(mp.j*t)*mp.gamma(mp.mpf(1)/2+mp.j*t)/mp.gamma(mp.mpf(1)/2-mp.j*t)
  ck(f"critical_gamma_unimodular_A{f}_t{T}",abs(abs(gamma)-1)<mp.mpf("1e-60"))
  er=None
  if T:
   byparts=-mp.quad(lambda v:Hpp(v)*mp.exp(-mp.j*t*v),vc)/(t*t)
   er=abs(direct-byparts)
   ck(f"critical_Hsecond_IBP_A{f}_t{T}",er<mp.mpf("1e-43"))
   ck(f"critical_TV_bound_A{f}_t{T}",abs(direct)<=h1/t)
   ck(f"critical_second_derivative_bound_A{f}_t{T}",abs(direct)<=h2*A/(t*t))
  rows.append({"A1":str(f),"a":a,"b":b,"tau":T,"Mellin_real":mp.nstr(direct.real,40),"Mellin_imag":mp.nstr(direct.imag,40),"log_substitution_error":mp.nstr(abs(direct-fourier),10),"second_IBP_error":mp.nstr(er,10) if er is not None else None})
p=r/"outputs/checks/2026-11-06-intermediate-kernel/root/critical-mellin-controls-v1/controls-v1.json";p.parent.mkdir(parents=True,exist_ok=True)
note=r/"planning/intermediate-kernel-20261106/root/CRITICAL_MELLIN_DYADIC-v1.md"
d={"passed":True,"count":len(tests),"checks":tests,"cases":rows,"scope":"NEW critical-line Mellin/log-Fourier consistency controls only; not original arithmetic-family data, interval enclosures or proof by numerics","interval_enclosures":False,"mpmath":mp.__version__,"dps":mp.mp.dps,"governing_note_sha256":hashlib.sha256(note.read_bytes()).hexdigest(),"no_old_250_Bessel_or_58_Hecke_controls_rerun":True}
with p.open("x") as out:out.write(json.dumps(d,indent=2)+"\n")
print(json.dumps({"passed":True,"checks":len(tests),"new_Mellin_cases":len(rows),"path":str(p.relative_to(r)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}))
