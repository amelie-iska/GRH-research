"""Independent exact diagnostics; no import of author arithmetic implementation."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/review-production/independent-check-v1.json'
assert not OUT.exists(),'Preserve every receipt'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
core=ROOT/'planning/signed-profile-20261105/root/profile-uniformity-core.tex'
detail=ROOT/'planning/signed-profile-20261105/root/profile-uniformity-details.tex'
expected=['0ffb58dbfb5d17dc32f7e3ab5c121007e90d975c9f792c5e5c8f2f94b117d0c3','8d9297584f5d0a93aaec614e6a339e5fc0e0d7784d9f84931125f5c0cf9810c4']
assert [sha(core),sha(detail)]==expected
assert core.read_bytes()==(ROOT/'papers/profile-uniformity-core.tex').read_bytes()
assert detail.read_bytes()==(ROOT/'papers/profile-uniformity-details.tex').read_bytes()
texts=[core.read_text(),detail.read_text()]
labels={m.group(1) for p in (ROOT/'papers').glob('*.tex') for m in re.finditer(r'\\label\{([^}]+)\}',p.read_text())}
refs=[m.group(1) for t in texts for m in re.finditer(r'\\(?:eqref|ref)\{([^}]+)\}',t)]
assert set(refs)<=labels,(set(refs)-labels)
assert not re.search(r'\\(?:eqref|ref)\{prf:details\}',texts[0])
assert '\\mathscr' not in ''.join(texts)
def mul(z,w):
 a,b=z;c,d=w;return a*c-b*d,a*d+b*c-b*d
def power(z,k):
 q=(1,0)
 for _ in range(k):q=mul(q,z)
 return q
def norm(z):a,b=z;return a*a-a*b+b*b
z=(1,1);delta=(1,2)
assert power(z,6)==(1,0) and power(z,2)==(0,1)
assert power(delta,2)==(-3,0)
assert mul((0,2),power(delta,3))==(12,6)
assert mul((4,0),power(delta,2))==(-12,0)
assert norm((13,6))==127 and norm((-11,0))==121
assert power(z,(127-1)//6)==(-1,0)
assert power(z,(121-1)//6)==(0,1)
assert power(z,2*((121-1)//6))==(-1,-1)
primes=[7,13,79,67,97];D=4000;U=63
prod=lambda xs:__import__('functools').reduce(lambda a,b:a*b,xs,1)
q=prod(primes);assert q==46721311
def divisor_norms(ps):return [prod(ps[i] for i in range(len(ps)) if mask>>i&1) for mask in range(1<<len(ps))]
def ru(ps):
 n=prod(ps);return sum(d>U and n>U*d for d in divisor_norms(ps))
orient=[];coeff=(0,0);dropped=(0,0)
for mask in range(32):
 mp=[p for i,p in enumerate(primes) if mask>>i&1];np=[p for i,p in enumerate(primes) if not(mask>>i&1)]
 m,n=prod(mp),prod(np)
 if not(D<m<2*D and D<n<2*D):continue
 rm,rn=ru(mp),ru(np);assert(rm,rn)==(2,2)
 am=(-1)**len(mp)*(rm-1);an=(-1)**len(np)*(rn-1)
 e,f=((m-1)//6)%6,((n-1)//6)%6
 wm=((3 if am<0 else 0)-e)%6;wn=((3 if an<0 else 0)-f)%6
 signed_exp=(3+wm-wn+e-f)%6;assert signed_exp==0
 drop=power(z,(3+wm-wn)%6)
 coeff=(coeff[0]+1,coeff[1]);dropped=(dropped[0]+drop[0],dropped[1]+drop[1])
 orient.append({'m':m,'n':n,'r_m':rm,'r_n':rn,'A_m':am,'A_n':an,'unit_phase':(e-f)%6})
assert len(orient)==4 and coeff==(4,0) and dropped==(-1,0)
assert {(x['m'],x['n']) for x in orient}=={(6097,7663),(7663,6097),(7189,6499),(6499,7189)}
# Ideals are associates in this PID. Enumerate exact small generators independently.
def canon(a):return min(mul(a,power(z,k)) for k in range(6))
v=sorted({canon((a,b)) for a in range(-6,7) for b in range(-6,7) if 10<=norm((a,b))<=20 and norm((a,b))%6==1})
assert sorted(norm(a) for a in v)==[13,13,19,19]
roots={p:min(t for t in range(p) if(t*t+t+1)%p==0) for p in primes}
def evalp(a,p):return(a[0]+a[1]*roots[p])%p
allowed=[a for a in v if all(evalp(a,p)!=0 for p in primes)]
assert len(allowed)==3
# Actual Euler symbols at the literal epsilon beta_v^6, not norm-only masking.
raw_checks=0
for beta in v:
 u=mul(z,power(beta,6))
 for item in orient:
  for N in [item['m'],item['n']]:
   ps=[p for p in primes if N%p==0];phase=0;zero=False
   for p in ps:
    a=evalp(u,p)
    if a==0:zero=True;break
    val=pow(a,(p-1)//6,p);epsilon=evalp(z,p)
    phase+=next(k for k in range(6) if pow(epsilon,k,p)==val)
   expected_zero=any(evalp(beta,p)==0 for p in ps)
   assert zero==expected_zero
   if not zero:assert phase%6==((N-1)//6)%6
   raw_checks+=1
# Expand the local Euler factor without relying on symbolic libraries.
def polymul(a,b):
 r=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return r
assert polymul([1,-2,1],[1,2,-2])==[1,0,-5,6,-2]
lam=Fraction(4,243);leak=lam*(1-lam)
assert leak==Fraction(956,59049)
assert Fraction(3*4,D)==Fraction(3,1000)
assert Fraction(3*-1,D)==Fraction(-3,4000)
record={'passed':True,'scope':'Independent finite identities and source/label diagnostics, not a substitute for the analytic proof review','source_sha256':{str(x.relative_to(ROOT)):sha(x) for x in [core,detail]},'production_matches':True,'references_checked':refs,'exact_local_witnesses':True,'local_euler_polynomial':[1,0,-5,6,-2],'fixture':{'D':D,'U':U,'q_norm':q,'orientations':orient,'good_v_generators_omega':v,'Z':len(allowed),'raw_symbol_checks':raw_checks,'signed_coefficient_sum':coeff,'without_literal_unit_phase':dropped,'selected_h1':'3/1000','wrong_without_unit_h1':'-3/4000','coherent_point_density':'1/243','coherent_A_energy_fraction':'4/243','squared_leakage':'956/59049'},'code_sha256':sha(Path(__file__))}
OUT.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'receipt':str(OUT.relative_to(ROOT)),'sha256':sha(OUT)}))
