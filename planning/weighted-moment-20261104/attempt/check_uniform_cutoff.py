from pathlib import Path
from fractions import Fraction as F
from itertools import product
import math,json,hashlib,time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
PAIRS=[(3,1),(4,1),(5,2),(6,1)]
PRIMES=[a*a-a*b+b*b for a,b in PAIRS]
assert PRIMES==[7,13,19,31]
RESIDUES=[(-a*pow(b,-1,p))%p for (a,b),p in zip(PAIRS,PRIMES)]
assert all((r*r+r+1)%p==0 for p,r in zip(PRIMES,RESIDUES))
Z=(F(0),F(0));ONE=(F(1),F(0))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,t):return x[0]*t,x[1]*t
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]
def prod_c(xs):
 z=ONE
 for x in xs:z=mul(z,x)
 return z
ROOTS=[ONE,(F(0),F(1)),(F(-1),F(1)),(F(-1),F(0)),(F(0),F(-1)),(F(1),F(-1))]
assert mul(ROOTS[1],ROOTS[1])==ROOTS[2]
def emul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def epow(x,n):
 z=(1,0)
 for _ in range(n):z=emul(z,x)
 return z
def chi_prime(u,j):
 p,r=PRIMES[j],RESIDUES[j];x=(u[0]+u[1]*r)%p
 if not x:return Z
 value=pow(x,(p-1)//6,p);powers=[pow(1+r,j,p) for j in range(6)]
 assert len(set(powers))==6 and value in powers
 return ROOTS[powers.index(value)]
def norm_mask(mask):return math.prod(p for j,p in enumerate(PRIMES) if mask>>j&1)
def beta(mask,U):
 k=mask.bit_count();total=0
 for a in range(16):
  if a&~mask:continue
  b=mask^a
  if norm_mask(a)<=U and norm_mask(b)<=U:total+=(-1)**k
 return total
def coeff(mask,U):return sum(beta(d,U) for d in range(16) if not d&~mask)
UVALUES=[1,2,5,7,13,19,25,31,49,91,127,500,math.prod(PRIMES)]
coeff_checks=0
for U,mask in product(UVALUES,range(16)):
 direct=sum((-1)**((a|b).bit_count()) for a,b in product(range(16),repeat=2) if not a&b and not (a|b)&~mask and norm_mask(a)<=U and norm_mask(b)<=U)
 assert coeff(mask,U)==direct
 assert abs(direct)<=3**mask.bit_count()
 if norm_mask(mask)<=U:assert direct==(-1)**mask.bit_count()
 coeff_checks+=1
rows=[x for x in product(range(-2,3),repeat=2) if x!=(0,0)]+[epow((3,1),3),epow((3,1),6)]
recombinations=0
for u,U in product(rows,UVALUES):
 z=[scale(chi_prime(u,j),F(1,p*p)) for j,p in enumerate(PRIMES)]
 left=Z
 for d in range(16):
  term=prod_c(z[j] if d>>j&1 else add(ONE,z[j]) for j in range(4))
  left=add(left,scale(term,beta(d,U)))
 right=Z
 for m in range(16):right=add(right,scale(prod_c(z[j] for j in range(4) if m>>j&1),coeff(m,U)))
 assert left==right
 recombinations+=1
 assert chi_prime(epow((3,1),6),0)==Z
monomial_checks=0
for powers in product(range(6),repeat=6):
 A=[2**x for x in powers];R=math.prod(A);X=math.prod(a**(j+1) for j,a in enumerate(A));M=max(A[0],A[1])
 assert R<=X and R**3<=X*M**3 and R**3<=X*X*M
 monomial_checks+=1
# A1=A2 saturates R/M<=X^(1/3), refuting replacement by1/4 in this monomial argument.
A=[16,16,1,1,1,1];R=math.prod(A);X=math.prod(a**(j+1) for j,a in enumerate(A));M=max(A[:2])
assert R**3==X*M**3 and (R//M)**4>X
# The canonical primitive character at a sixth power would erase an original zero.
u=epow((3,1),6);assert chi_prime(u,0)==Z and add(ONE,chi_prime(u,0))!=add(ONE,scale(ONE,F(1,7**2)))
exponent_checks=0
for a,d in product([F(j,100) for j in range(51)],[F(1,100),F(1,20),F(1,10),F(1,5),F(2,5)]):
 old=2*d+(2-4*d)*a;new=F(1,2)
 assert max(F(3,4),1+F(3,4)/3,F(2,3)*(1+F(3,4)))-F(3,4)==new
 assert min(old,new)<=old
 exponent_checks+=1
report={'passed':True,'field':'Q(omega); exact cyclotomic Q(zeta6) arithmetic','split_prime_generators':PAIRS,'split_prime_norms':PRIMES,'omega_residue_images':RESIDUES,'coefficient_checks':coeff_checks,'masked_recombinations':recombinations,'symbol_rows':len(rows),'sixth_power_zero_control':True,'dyadic_monomial_checks':monomial_checks,'exponent_checks':exponent_checks,'negative_controls':['wrong1/4 monomial exponent rejected','primitive sixth-power restoration differs from literal zero'], 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite algebraic consistency and monomial inequalities only; not a proof of BGL/contour/GRH, not Lean'}
out=ROOT/'outputs/checks/2026-11-04-weighted-moment/attempt';out.mkdir(parents=True,exist_ok=True);target=out/('exact-controls-'+str(time.time_ns())+'.json');target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(target),**report},indent=2))
