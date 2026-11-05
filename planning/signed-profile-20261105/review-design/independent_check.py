"""Fresh exact checks of norm groups and the proposed signed-profile witness.
No production imports, old audit reruns, floating symbols or random seeds.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import defaultdict
import json,hashlib,re,math
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/review-design'
LIMIT=8192
sieve=[True]*(LIMIT+1);sieve[0]=sieve[1]=False
for p in range(2,math.isqrt(LIMIT)+1):
 if sieve[p]:
  for n in range(p*p,LIMIT+1,p):sieve[n]=False
# Prime ideal labels retain both split primes; inert ideals have norm p^2.
primes=[]
for p in range(5,LIMIT+1):
 if not sieve[p]:continue
 if p%3==1:primes.extend([((p,1),p),((p,-1),p)])
 elif p*p<=LIMIT:primes.append(((p,0),p*p))
ideals=[(1,())]
for key,norm in primes:
 ideals.extend((n*norm,fs+((key,norm),)) for n,fs in tuple(ideals) if n*norm<=LIMIT)
assert len({fs for n,fs in ideals})==len(ideals)
groups=defaultdict(list)
for n,fs in ideals:groups[n].append(fs)
def divisors(fs):
 ds=[1]
 for key,norm in fs:ds.extend(x*norm for x in tuple(ds))
 return tuple(sorted(ds))
def raw_minus_one(fs):
 value=1
 for key,norm in fs:
  assert norm%6==1
  value*=(-1)**((norm-1)//6)
 return value
def actual_A(fs,U):
 value=0
 for assignment in product(range(3),repeat=len(fs)):
  a=b=1;sign=1
  for part,(key,norm) in zip(assignment,fs):
   if part==1:a*=norm;sign=-sign
   elif part==2:b*=norm;sign=-sign
  if a<=U and b<=U:value+=sign
 return value
norm_group_checks=0
for n,records in groups.items():
 signatures={( (-1)**len(fs),divisors(fs),raw_minus_one(fs)) for fs in records};assert len(signatures)==1,(n,signatures)
 assert next(iter(signatures))[2]==(-1)**((n-1)//2)
 norm_group_checks+=len(records)
assert divisors(groups[25][0])==(1,25) and (-1)**len(groups[25][0])==-1
assert divisors(groups[49][0])==(1,7,7,49) and (-1)**len(groups[49][0])==1
annuli=[];coefficient_checks=0
for U in [8,10,16,20,32,64]:
 D=U*U;items=[(n,fs) for n,fs in ideals if D<n<2*D];count=len(items);signed=0;epsilon_by_norm={};negative=0
 for n,fs in items:
  A=actual_A(fs,U);ds=divisors(fs);long=sum(d>U and n//d>U for d in ds);assert long%2==0;assert A==(-1)**len(fs)*(long-1);assert abs(A)>=1
  sign=1 if A*raw_minus_one(fs)>0 else -1
  assert n not in epsilon_by_norm or epsilon_by_norm[n]==sign;epsilon_by_norm[n]=sign
  signed+=A*raw_minus_one(fs)*sign;negative+=sign<0;coefficient_checks+=1
 assert signed>=count
 # For integer U, normalized I_-1 is rational exactly, not approximately.
 I=Fraction(signed,U);energy=I*I;assert energy>=Fraction(count*count,D)
 annuli.append(dict(D=D,U=U,all_good_squarefree_ideals=count,norm_groups=len(epsilon_by_norm),negative_weight_columns=negative,absolute_coefficient_sum=signed,I_minus_one=str(I),energy=str(energy),count_squared_over_D=str(Fraction(count*count,D)),nonsquarefree_rational_norm_columns=sum(any(n%(p*p)==0 for p in range(2,math.isqrt(n)+1) if sieve[p]) for n,fs in items)))
# Removing only one split prime of norm7 must not break norm-group constancy.
restricted=defaultdict(list)
for n,fs in ideals:
 if all(key!=(7,1) for key,norm in fs):restricted[n].append(fs)
for n,records in restricted.items():assert len({((-1)**len(fs),divisors(fs),raw_minus_one(fs)) for fs in records})==1
report=dict(passed=True,method='Independent rational-prime splitting enumeration retaining actual split-prime labels; direct ternary A_U computation; exact integer/Fraction arithmetic',maximum_norm=LIMIT,prime_ideal_labels=len(primes),squarefree_ideals=len(ideals),norm_group_checks=norm_group_checks,coefficient_checks=coefficient_checks,annuli=annuli,raw_nonprincipal_witness=dict(prime_ideal_norm=7,value=-1),norm_square_controls=dict(inert25=dict(mu=-1,divisor_norms=[1,25]),split49=dict(mu=1,divisor_norms=[1,7,7,49])),limits='Finite bookkeeping diagnostics support the independent universal proof; do not prove its asymptotic ideal count, uniform estimates or GRH.')
(OUT/'independent-checks.json').write_text(json.dumps(report,indent=2)+'\n')
# Focused repository novelty inventory; omit this review itself and nontext resources.
paths=set((ROOT/'research').glob('*.md'))|set((ROOT/'papers').glob('*.tex'))|set((ROOT/'planning').rglob('*.md'))|set((ROOT/'planning').rglob('*.tex'))
paths={p for p in paths if 'signed-profile-20261105' not in p.parts}
patterns=[r'norm.radial',r'epsilon_N',r'W_D',r'chi_?4.{0,15}N',r'sign.align',r'adversarial.{0,40}profile',r'profile.{0,40}sign',r'profile.{0,40}obstruction']
hits=[]
for p in sorted(paths):
 for i,line in enumerate(p.read_text(errors='replace').splitlines(),1):
  if any(re.search(rx,line,re.I) for rx in patterns):hits.append(dict(file=str(p.relative_to(ROOT)),line=i,text=line[:600]))
(OUT/'novelty-search.json').write_text(json.dumps(dict(scope='Current research/paper text and planning markdown/TeX, no private directories, no claim of comprehensive literature priority',files_scanned=len(paths),patterns=patterns,hits=hits),indent=2)+'\n')
print(json.dumps(dict(passed=True,ideals=len(ideals),coefficient_checks=coefficient_checks,annuli=annuli,novelty_hits=len(hits))))
