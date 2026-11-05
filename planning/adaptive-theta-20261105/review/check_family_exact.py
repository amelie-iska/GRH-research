"""Independent saved-family audit: no producer or author arithmetic imported."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,hashlib,math,time
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review'
PINS={'dyadic.py':'82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170','theta_oracle.py':'c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1','adaptive_readout.py':'dc64e37cdadac8ffadaa666cdd0e6a0941580f89f3674817c803e8c89ee7e274'}
M={3:4,4:10,5:6};U,V=F(7,12),F(7,24);checks=0;summary=[]
def check(ok,label):
 global checks
 checks+=1
 if not ok:raise AssertionError(label)
def integer(s):
 sign=-1 if s.startswith('-') else 1;v=0
 for c in s.lstrip('+-'):v=v*10+int(c)
 return sign*v
def dec(x):
 if isinstance(x,dict) and 'numerator' in x and 'denominator' in x:return F(integer(x['numerator']),integer(x['denominator']))
 if isinstance(x,dict):return {k:dec(v) for k,v in x.items()}
 if isinstance(x,list):return [dec(v) for v in x]
 return x
def decimal(x):
 try:return str(x)
 except ValueError:
  sign='-' if x<0 else '';x=abs(x);parts=[]
  while x:x,last=divmod(x,10**8);parts.append(last)
  return sign+str(parts[-1])+''.join(format(t,'08d') for t in reversed(parts[:-1]))
def hash_state(state):
 raw=';'.join(','.join(decimal(x.numerator)+'/'+decimal(x.denominator) for x in z) for z in state)
 return hashlib.sha256(raw.encode('ascii')).hexdigest()
def ceildiv(n,d):return -((-n)//d)
def up(x,B):return F(ceildiv(x.numerator*(1<<B),x.denominator),1<<B)
def E(x):return F(1,1<<(x.numerator//x.denominator))
def Q(x):return F(1)/x+F(2)/x**2+F(2)/x**3
@lru_cache(None)
def analytic(q,N,J,K,eta):
 parity=0 if q==5 else 1;chi={3:(0,1,-1),4:(0,1,0,-1),5:(0,1,-1,-1,1)}[q];d=F(3,q);n0=N+1;T=2**J;C=F(1) if not parity else (1+1/d)/2
 nt=2*C*Q(d*n0*n0)*E(d*n0*n0/2)/(1-E(d*n0));tt=sum((2*n**parity*T**3*E(d*n*n*T)*Q(d*n*n*T) for n in range(1,N+1)),F());qt=F();discard=F();active=skipped=0;threshold=eta/F(8*4*J*N)
 for j in range(J):
  for ell in range(4):
   m=F(2**j)*(1+F(2*ell+1,8));h=F(2**j,8);r=m/2;v=h/r;B=max((m+r)**2,(m-r)**(-2),F(1))
   for n in range(1,N+1):
    qt+=4*h*n**parity*3*B*E(d*n*n*m/2)*v**(2*K+2)/(F(2*K+3)*(1-v*v))
    if not chi[n%q]:continue
    pair=4*h*n**parity*(m+h)**2*E(d*n*n*(m-h))
    if pair<=threshold:discard+=pair;skipped+=1
    else:active+=1
 return {'n_tail':nt,'time_tail':tt,'quadrature':qt,'discard':discard},active,skipped,threshold

def growth(q):
 parity=0 if q==5 else 1;k=1 if not parity else 2;d=F(3,q);n0=8
 def qk(x):return sum((F(math.factorial(k),math.factorial(k-j))/x**(j+1) for j in range(k+1)),F())
 def upper(x):return (1+x/16)**(-16)
 C=F(1) if not parity else (1+1/d)/2
 prefix=sum((n**parity*upper(d*n*n)*qk(d*n*n) for n in range(1,n0)),F())
 tail=C*qk(d*n0*n0)*upper(d*n0*n0/2)/(1-upper(d*n0))
 return 2*(prefix+tail)

class Arithmetic:
 def __init__(self,bits):self.bits=bits;self.S=1<<bits
 def real(self,x):return x.numerator*self.S//x.denominator,ceildiv(x.numerator*self.S,x.denominator)
 def complex(self,x=F(),y=F()):return self.real(x),self.real(y)
 def addR(self,a,b):return a[0]+b[0],a[1]+b[1]
 def negR(self,a):return -a[1],-a[0]
 def subR(self,a,b):return self.addR(a,self.negR(b))
 def mulR(self,a,b):
  corners=[x*y for x in a for y in b];return min(corners)//self.S,ceildiv(max(corners),self.S)
 def divR(self,a,n):return a[0]//n,ceildiv(a[1],n)
 def add(self,a,b):return self.addR(a[0],b[0]),self.addR(a[1],b[1])
 def mul(self,a,b):return self.subR(self.mulR(a[0],b[0]),self.mulR(a[1],b[1])),self.addR(self.mulR(a[0],b[1]),self.mulR(a[1],b[0]))
 def divide(self,a,n):return self.divR(a[0],n),self.divR(a[1],n)
 def decode(self,r):
  result=[]
  for name in ['real','imag']:
   p=r[name];check(type(p['dyadic_bits']) is int and p['dyadic_bits']>=32 and integer(p['lo'])<=integer(p['hi']),'valid integer dyadic endpoints');lo=F(integer(p['lo']),1<<p['dyadic_bits']);hi=F(integer(p['hi']),1<<p['dyadic_bits']);result.append((self.real(lo)[0],self.real(hi)[1]))
  return tuple(result)
 def midpoint(self,r):return tuple(F(x+y,2*self.S) for x,y in r)
 def radius(self,r):return sum((F(hi-lo,2*self.S) for lo,hi in r),F())

def audit_sample(s,q,j,count,eta):
 check(s['q']==q and s['target_kind']=='true_circle_node' and s['node_index']==j and s['node_count']==count,'ordered true sample metadata')
 check(s['requested_sample_error']==eta and s['circle_center']==F(1,2) and s['circle_radius']==F(6,5),'sample target contract')
 raw,active,skipped,threshold=analytic(q,s['N'],s['J'],s['K'],eta)
 check(all(0<=v<=eta/8 for v in raw.values()),'sample analytic allocations')
 check(s['active_pairs']==active and s['discarded_pairs']==skipped and s['per_pair_discard_threshold']==threshold,'whole-pair discard accounting')
 ctx=Arithmetic(s['bits']);box=ctx.decode(s['quadrature_sum_box']);center=ctx.midpoint(box);rawradius=ctx.radius(box)
 check((s['center_real'],s['center_imag'])==center,'sample exact midpoint')
 check(0<=s['raw_interval_radius']==rawradius<=eta/4,'sample raw arithmetic radius')
 raw['interval_arithmetic']=rawradius;B=s['budget_rounding_bits'];check(F(5,1<<B)<=eta/8,'sample serialization allocation')
 check(s['budget']=={n:up(v,B) for n,v in raw.items()},'sample all five exact rounded components')
 check(s['radius']==sum(s['budget'].values(),F())<=7*eta/8,'sample literal total')
 check(s['precision_attempts'][-1]['bits']==s['bits'] and s['precision_attempts'][-1]['interval_radius']==rawradius,'sample accepted retry')
 for at in s['precision_attempts'][:-1]:check(at['interval_radius']>eta/4,'sample preceding retry fails')

def audit_family(r):
 q=r['q'];eps=r['requested_tolerance'];degree=r['degree'];count=r['sample_count'];eta=r['requested_sample_error']
 check(type(q) is int and q in M and eps>0,'supported family/tolerance')
 d=0
 while 10*V**(d+1)/(1-V)>eps/8:d+=1
 c=d+1
 while 10*F(1,2**c)/(1-F(1,2**c))/(1-V)>eps/8:c+=1
 c=8*((c+7)//8)
 check((degree,count,eta)==(d,c,eps*(1-U)/8),'independent parameter selection')
 check(degree<count and count%8==0,'Fourier orthogonality dimensions')
 check(r['coefficient_basis']=='((s-1/2)/(6/5))^n' and r['compact_radius']==F(7,10) and r['circle_radius']==F(6,5) and r['growth_radius']==F(12,5),'literal normalized polynomial/geometry')
 check(r['growth_integer_bound']==M[q] and r['growth_exact_majorant']==growth(q)<M[q],'independent accepted U16 growth majorant')
 rows=r['samples'];check(len(rows)==count,'complete actual sample family')
 for j,s in enumerate(rows):audit_sample(s,q,j,count,eta)
 attempts=r['sample_precision_attempts'];last=attempts[-1];actual=max(s['bits'] for s in rows)
 check(last['max_sample_bits']==actual and last['Fourier_bits']==actual+32,'last Fourier precision')
 for earlier in attempts[:-1]:check(earlier['Fourier_radius_sum']>eps/8,'preceding Fourier retry fails')
 for before,after in zip(attempts,attempts[1:]):check(after['initial_bits']==2*before['max_sample_bits'],'Fourier retry refreshes initial sample precision')
 A=Arithmetic(last['Fourier_bits']);labels=[A.complex(s['center_real'],s['center_imag']) for s in rows];roots=[A.decode(s['root_box']) for s in rows];roots=[(z[0],A.negR(z[1])) for z in roots];powers=[A.complex(F(1)) for _ in rows];bounds=[]
 for n in range(degree+1):
  result=A.complex()
  for j in range(count):result=A.add(result,A.mul(labels[j],powers[j]))
  result=A.divide(result,count);bounds.append(result);check(result==A.decode(r['target_rectangles'][n]),'independent integer Fourier rectangle')
  powers=[A.mul(z,root) for z,root in zip(powers,roots)]
 targets=[A.midpoint(b) for b in bounds];check(targets==[tuple(t) for t in r['targets']],'exact Fourier midpoint targets')
 arithmetic=sum((A.radius(b)*U**n for n,b in enumerate(bounds)),F());check(arithmetic==last['Fourier_radius_sum']<=eps/8,'independent weighted Fourier arithmetic budget')
 # Execute every rational update independently; no closed form is used here.
 state=[(F(),F()) for _ in targets];trace=r['trace'];check(r['steps']==len(trace)-1 and r['gradient_step']==F(1,4),'trace dimensions/gradient step')
 for k,row in enumerate(trace):
  check(row['iteration']==k,'trace iteration order')
  check(all(x==row['coefficient_scale']*tx and y==row['coefficient_scale']*ty for (x,y),(tx,ty) in zip(state,targets)),'lossless compressed complete vector state')
  check(row['coefficient_state_sha256']==hash_state(state),'full-state exact hash')
  differences=[(x-tx,y-ty) for (x,y),(tx,ty) in zip(state,targets)]
  objective=sum((x*x+y*y for x,y in differences),F())/2;residual=sum(((abs(x)+abs(y))*U**n for n,(x,y) in enumerate(differences)),F())
  check((row['objective'],row['residual'])==(objective,residual),'exact objective/weighted residual')
  check((residual<=eps/4)==(k==len(trace)-1),'first stopping iterate')
  if k<len(trace)-1:state=[((3*x+tx)/4,(3*y+ty)/4) for (x,y),(tx,ty) in zip(state,targets)]
 check(state==[tuple(z) for z in r['coefficients']],'literal final coefficient vector')
 w=F(1,2**count);eta_actual=max(s['radius'] for s in rows)
 raw={'oracle':eta_actual*sum((U**n for n in range(degree+1)),F()),'alias':M[q]*w/(1-w)*sum((V**n for n in range(degree+1)),F()),'Taylor':M[q]*V**(degree+1)/(1-V),'coefficient_arithmetic':arithmetic,'optimization':trace[-1]['residual']}
 check(all(raw[n]<=eps/8 for n in ['oracle','alias','Taylor','coefficient_arithmetic']) and raw['optimization']<=eps/4,'all five raw readout allocations')
 B=r['budget_rounding_bits'];check(F(5,1<<B)<=eps/8,'readout serialization allocation')
 check(r['budget']=={n:up(x,B) for n,x in raw.items()},'five exact outward serialized readout components')
 check(r['compact_uniform_bound']==sum(r['budget'].values(),F())<=7*eps/8,'literal certified global bound')
 summary.append({'q':q,'requested_tolerance':str(eps),'degree':degree,'sample_count':count,'steps':r['steps'],'coefficient_states_checked':len(trace)*(degree+1),'uniform_bound':str(r['compact_uniform_bound'])})

if __name__=='__main__':
 experiment=Path(sys.argv[1]);raw=(experiment/'family-certificates.json').read_bytes();data=dec(json.loads(raw))
 check(data['sample_oracle_validated'] is True and data['coefficient_certificate'] is True and data['new_Lean_declarations']==0 and data['GRH_proved'] is False,'certificate scope flags')
 for name,pin in data['source_sha256'].items():check(hashlib.sha256((experiment/name).read_bytes()).hexdigest()==pin,'source snapshot checksum')
 for name,pin in PINS.items():check(data['source_sha256'][name]==pin,'historical accepted source pin')
 for r in data['readouts']:audit_family(r)
 report={'passed':True,'checks':checks,'experiment':str(experiment),'family_certificate_sha256':hashlib.sha256(raw).hexdigest(),'source_sha256':data['source_sha256'],'families':summary,'producer_imported':False,'author_arithmetic_imported':False,'exact_integer_fourier_reconstruction':True,'all_executed_gd_states_reconstructed':True,'five_component_budget_reconstructed':True}
 path=OUT/('family-exact-'+experiment.name+'-'+str(time.time_ns())+'.json');path.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(path),**report}))
