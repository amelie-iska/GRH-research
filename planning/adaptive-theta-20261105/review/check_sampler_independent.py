"""Independent exact adaptive-parameter, recurrence and API guard checks."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,math,itertools,hashlib,time
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_theta as a
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review';sources={n:(ROOT/'examples/analytic_oracle'/n).read_bytes() for n in ['precision.py','adaptive_theta.py']}
checks=0;failures=[];plans=[]
def check(ok,label):
 global checks
 checks+=1
 if not ok:failures.append(label)
def rejects(fn,label):
 try:fn()
 except (ValueError,TypeError,ZeroDivisionError,FileExistsError):check(True,label)
 else:check(False,label)
def E(x):return F(1,2**(x.numerator//x.denominator))
def Q(x):return sum((F(math.factorial(2),math.factorial(2-j))/x**(j+1) for j in range(3)),F())
def panelset(J):
 T=F(1);out=[]
 for j in range(J):
  step=T/4
  for k in range(4):out.append((T+k*step+step/2,step/2))
  T*=2
 return tuple(out)
def independent(q,N,J,K):
 parity=0 if q==5 else 1;d=F(3,q);n0=N+1;C=F(1) if parity==0 else (1+1/d)/2;T=2**J
 nt=2*C*Q(d*n0*n0)*E(d*n0*n0/2)/(1-E(d*n0))
 tt=sum((2*n**parity*T**3*E(d*n*n*T)*Q(d*n*n*T) for n in range(1,N+1)),F())
 qt=F()
 for center,halfwidth in panelset(J):
  R=center/2;ratio=halfwidth/R;B=max((center+R)**2,(center-R)**(-2),F(1))
  tailgeo=ratio**(2*K+2)/(F(2*K+3)*(1-ratio**2))
  for n in range(1,N+1):qt+=4*halfwidth*n**parity*3*B*E(d*n*n*center/2)*tailgeo
 return nt,tt,qt
for q,eta in itertools.product([3,4,5],[F(1,10**6),F(1,10**24),F(1,10**32),F(17,10**31)]):
 p=a.parameters(q,eta);nt,tt,qt=independent(q,p.N,p.J,p.K);allocation=eta/8
 check((nt,tt,qt)==(p.n_tail,p.time_tail,p.quadrature),f'{q} exact independent tails {eta}')
 check(all(0<=v<=allocation for v in [nt,tt,qt,p.discard]),f'{q} allocations {eta}')
 check(E(F(3,q)*(p.N+1))<1,f'{q} positive n-tail denominator {eta}')
 if p.N>1:check(independent(q,p.N-1,p.J,p.K)[0]>allocation,f'{q} minimal N {eta}')
 if p.J>1:check(independent(q,p.N,p.J-1,p.K)[1]>allocation,f'{q} minimal J {eta}')
 if p.K>0:check(independent(q,p.N,p.J,p.K-1)[2]>allocation,f'{q} minimal K {eta}')
 check(a.panels(p.J)==panelset(p.J),f'{q} exact dyadic partition {eta}')
 check(sum((2*h for _,h in panelset(p.J)),F())==2**p.J-1,f'{q} partition total length {eta}')
 parity,chi=a.FAMILIES[q];threshold=eta/(8*4*p.J*p.N);active=[];discard=F();discarded=0
 for m,h in panelset(p.J):
  for n in range(1,p.N+1):
   if chi[n%q]==0:continue
   bound=4*h*n**parity*(m+h)**2*E(F(3,q)*n*n*(m-h))
   if bound<=threshold:discard+=bound;discarded+=1
   else:active.append((m,h,n,chi[n%q]*n**parity))
 check((tuple(active),discard,discarded,threshold)==(p.active,p.discard,p.discarded_pairs,p.per_pair_threshold),f'{q} independent whole-pair discard {eta}')
 check(discarded*threshold<=allocation,f'{q} discard accounting {eta}')
 plans.append({'q':q,'eta':str(eta),'N':p.N,'J':p.J,'K':p.K,'active_pairs':len(active),'discarded_pairs':discarded})
# Direct generalized-binomial x exponential convolution versus recurrence.
def add(z,w):return z[0]+w[0],z[1]+w[1]
def scale(z,x):return z[0]*x,z[1]*x
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
for x,y,lm,u in itertools.product([F(-2),F(-1,3),F(1,2)],[F(),F(2,3)],[F(5,7),F(81,5)],[F(1,9),F(1,15)]):
 p=(x,y);prev=(F(),F());cur=(F(1),F());binom=[cur]
 for j in range(40):binom.append(scale(mul(binom[-1],add(p,(F(-j),F()))),F(1,j+1)))
 for j in range(41):
  direct=(F(),F())
  for ell in range(j+1):direct=add(direct,scale(binom[ell],(-lm)**(j-ell)/math.factorial(j-ell)))
  direct=scale(direct,u**j);check(direct==cur,f'binomial recurrence degree{j}')
  nxt=scale(add(scale(mul(add(p,(-lm-j,F())),cur),u),scale(prev,-lm*u*u)),F(1,j+1));prev,cur=cur,nxt
# Exact-input and primed-cache controls.
eta=F(1,10**24);a.parameters(3,eta)
for bad in [3.0,F(3),True,False,2,6]:
 rejects(lambda:a.parameters(bad,eta),f'parameters conductor {bad!r}')
 rejects(lambda:a.point(bad,F(1,2),F(),eta),f'point conductor {bad!r}')
for bad in [1e-24,True,False,0,-1,F(),F(-1)]:rejects(lambda:a.parameters(3,bad),f'tolerance {bad!r}')
for bad in [0.0,1.0,True,False]:
 rejects(lambda:a.point(3,bad,F(),eta),f'point real {bad!r}')
 rejects(lambda:a.point(3,F(1,2),bad,eta),f'point imaginary {bad!r}')
for x,y in [(F(-1001,1000),F()),(F(2001,1000),F()),(F(),F(1334,1000))]:rejects(lambda:a.point(3,x,y,eta),'outside true domain')
for j,m in [(True,64),(0,64.0),(F(0),64),(-1,64),(64,64),(0,0),(0,False)]:rejects(lambda:a.circle(3,j,m,eta),'circle dimension/index')
for bits in [True,False,31,32.0]:rejects(lambda:a.point(3,F(),F(),eta,bits),f'precision {bits!r}')
for value in [F(-1),.0,True]:rejects(lambda:a.E(value),f'exponential majorant {value!r}')
# Nonmultiplicativity is intentional: use E at the actual exponent argument.
check(E(F(3,5)+F(3,5))!=E(F(3,5))*E(F(3,5)),'E is not multiplicative')
rejects(lambda:a.run(OUT,eta,(3,),1,1),'existing output immutable')
check(all((ROOT/'examples/analytic_oracle'/n).read_bytes()==b for n,b in sources.items()),'source stable')
report={'passed':not failures,'checks':checks,'failures':failures,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in sources.items()},'plans':plans,'exact_tail_and_discard_reconstruction':True,'independent_recurrence_convolution':True}
p=OUT/('sampler-independent-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**{k:v for k,v in report.items() if k!='plans'}}))
if failures:raise SystemExit(1)
