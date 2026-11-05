"""Validated finite primitive-Dirichlet completed samples and readout budget.

External analytic input: standard primitive theta/Mellin identity. No zero
locations assumed. All interval/certificate endpoints are exact rational.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,json,math,hashlib,time
from dyadic import R,C,real,complex_box,pi,log_fraction,exp_box,BITS
FAMILIES={3:(1,[0,1,-1]),4:(1,[0,1,0,-1]),5:(0,[0,1,-1,-1,1])}
BP=180;BS=1<<BP

def up(x):return F(-(-x.numerator*BS//x.denominator),BS)
def U(x):return up((1+x/128)**(-128))
def Q(x):return 1/x+2/x**2+2/x**3
def frac(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display=float(x))
def panels():
 for j in range(7):
  h=F(2**j,8)
  for ell in range(4):yield F(2**j)*(1+F(2*ell+1,8)),h

@lru_cache(maxsize=None,typed=True)
def analytic_error(q,K=12):
 if type(q) is not int or q not in FAMILIES or type(K) is not int or K<0:raise ValueError('Supported conductor and nonnegative integer order required')
 a,_=FAMILIES[q];d=F(3,q);n0=12;T=128
 C0=F(1) if a==0 else (1+1/d)/2
 nt=up(2*C0*Q(d*n0*n0)*U(d*n0*n0/2)/(1-U(d*n0)))
 tt=up(sum((2*n**a*T**3*U(d*n*n*T)*Q(d*n*n*T) for n in range(1,12)),F()))
 qt=F()
 for m,h in panels():
  radius=m/2;v=h/radius;B=max((m+radius)**2,(m-radius)**(-2),F(1))
  for n in range(1,12):qt+=up(2*n**a*2*h*3*B*U(d*n*n*m/2)*v**(2*K+2)/(F(2*K+3)*(1-v*v)))
 return nt,tt,qt

@lru_cache(maxsize=None,typed=True)
def panel_parameters(q):
 a,chi=FAMILIES[q];d=F(3,q);active=[];discard=F();skipped=0
 for m,h in panels():
  left=m-h;right=m+h
  for n in range(1,12):
   if not chi[n%q]:continue
   bound=up(4*h*n**a*right**2*U(d*n*n*left))
   if bound<F(1,1<<90):discard+=bound;skipped+=1;continue
   lm=pi()*F(n*n,q)*m
   active.append((m,h,n,chi[n%q]*n**a,lm,log_fraction(m)))
 return active,discard,skipped

def domain(s):
 if not isinstance(s,C):raise TypeError('Certified complex rectangle required')
 if s.re.lo< -R.frac(1).hi or s.re.hi>R.frac(2).hi or s.im.magnitude()>F(4,3):raise ValueError('Sample box outside proved domain')

def integrate(q,s,K=12):
 if q not in FAMILIES or type(q) is not int:raise ValueError('Only q3/4/5 families are supported')
 if type(K) is not int or K<0:raise ValueError('Nonnegative integer order required')
 domain(s);a,_=FAMILIES[q];powers=[(s+a)/2-1,(1-s+a)/2-1];total=complex_box(0)
 active,discard,skipped=panel_parameters(q)
 for m,h,n,weight,lm,logm in active:
  u=h/m
  for p in powers:
   previous=complex_box(0);current=complex_box(1);acc=current
   for j in range(2*K):
    nxt=((p-lm-j)*current*u-previous*lm*(u*u))/(j+1)
    previous,current=current,nxt
    if (j+1)%2==0:acc=acc+current/(j+2)
   total=total+exp_box(p*logm-lm)*acc*(2*h*weight)
 nt,tt,qt=analytic_error(q,K)
 assert all(x>=0 for x in [total.radius(),nt,tt,qt,discard])
 radius=up(total.radius()+nt+tt+qt+discard)
 assert radius>=0
 return dict(q=q,box=total,center_real=total.re.midpoint(),center_imag=total.im.midpoint(),radius=radius,
     interval_radius=up(total.radius()),n_tail=nt,time_tail=tt,quadrature=qt,discard=discard,active_pairs=len(active),discarded_pairs=skipped)

@lru_cache(maxsize=None,typed=True)
def circle_node(j,m):
 if type(m) is not int or type(j) is not int or m<1 or not 0<=j<m:raise ValueError('Invalid circle node')
 root=exp_box(C(real(0),pi()*F(2*j,m)))
 return complex_box(F(1,2))+root*F(6,5),root

def output_sample(q,j,m,K):
 s,root=circle_node(j,m);row=integrate(q,s,K)
 assert 0<=row['radius']<F(1,10**14),'Requested sample precision not certified'
 box=row.pop('box');record={k:frac(v) if isinstance(v,F) else v for k,v in row.items()}
 record.update(node_index=j,node_count=m,node_box=s.encode(),root_box=root.encode(),quadrature_sum_box=box.encode())
 row['node_index']=j;row['node_count']=m
 return record,root,row

def growth_majorant(q):
 a,_=FAMILIES[q];d=F(3,q);k=max(0,math.ceil((1+F(1,2)+F(12,5)+a)/2-1));n0=8
 def qk(x):return sum((F(math.factorial(k),math.factorial(k-j))/x**(j+1) for j in range(k+1)),F())
 def upper_exp(x):return (1+x/16)**(-16)
 C0=F(1) if a==0 else (1+1/d)/2
 prefix=sum((n**a*upper_exp(d*n*n)*qk(d*n*n) for n in range(1,n0)),F())
 tail=C0*qk(d*n0*n0)*upper_exp(d*n0*n0/2)/(1-upper_exp(d*n0))
 return 2*(prefix+tail)

def readout(records,m,degree=28,steps=180):
 if type(m) is not int or m<1 or len(records)!=m or type(degree) is not int or not 0<=degree<m or type(steps) is not int or steps<0:raise ValueError('Complete m-node family and nonnegative degree/steps required')
 q0=records[0][1]['q']
 if any(row['q']!=q0 or row.get('node_index')!=j or row.get('node_count')!=m or root!=circle_node(j,m)[1] or row['radius']<0 for j,(root,row) in enumerate(records)):raise ValueError('Inconsistent certified circle records')
 labels=[C(real(row['center_real']),real(row['center_imag'])) for _,row in records]
 roots=[C(root.re,-root.im) for root,_ in records];power=[complex_box(1) for _ in roots];coeff=[];star=[]
 u=F(7,12);v=F(7,24);w=F(1,2)**m;eta=max(row['radius'] for _,row in records);q=records[0][1]['q'];M={3:4,4:10,5:6}[q];exact_M=growth_majorant(q)
 assert exact_M<M,'Integer growth bound failed exact recomputation'
 factor=1-F(3,4)**steps
 opt=F();arithmetic=F()
 for n in range(degree+1):
  b=sum((label*power[j] for j,label in enumerate(labels)),complex_box(0))/m
  trained=b*factor;star.append(b);opt+=F(3,4)**steps*b.magnitude()*u**n
  arithmetic+=trained.radius()*u**n
  coeff.append(dict(real=frac(trained.re.midpoint()),imag=frac(trained.im.midpoint()),exact_GD_coefficient_enclosure=trained.encode()))
  power=[power[j]*root for j,root in enumerate(roots)]
 oracle=eta*(1-u**(degree+1))/(1-u);alias=M*w/(1-w)*(1-v**(degree+1))/(1-v);taylor=M*v**(degree+1)/(1-v)
 opt,oracle,alias,taylor,arithmetic=map(up,[opt,oracle,alias,taylor,arithmetic])
 budget=opt+oracle+alias+taylor+arithmetic
 assert budget<F(5,10**15)
 return dict(q=q,degree=degree,steps=steps,sample_count=m,gradient_step=frac(F(1,4)),M_r_integer_bound=M,growth_exact_bound=frac(exact_M),optimizer_evaluation='Closed-form exact iterate of specified GD recurrence; not an executed optimizer loop',
     optimization=frac(up(opt)),oracle=frac(up(oracle)),alias=frac(up(alias)),Taylor=frac(up(taylor)),coefficient_arithmetic=frac(up(arithmetic)),compact_uniform_bound=frac(budget),coefficients=coeff,
     scope='Literal exact rational midpoint polynomial; compact |s-1/2|<=7/10. Not a zero-location, all-conductor or full Lean theorem.')

def run(output,m=64,stride=1,K=12):
 if type(m) is not int or m<1 or type(stride) is not int or stride<1:raise ValueError('Positive integer circle size/stride required')
 if stride==1 and m<=28:raise ValueError('This readout requires m>28')
 if output.exists():raise FileExistsError('Preserve old experiment directory')
 output.mkdir(parents=True);rows=[];trained=[];started=time.time()
 source_at_start={f:(Path(__file__).parent/f).read_bytes() for f in ['dyadic.py','theta_oracle.py']}
 for q in FAMILIES:
  group=[]
  for j in range(0,m,stride):
   record,root,row=output_sample(q,j,m,K);rows.append(record);group.append((root,row))
  print(json.dumps(dict(q=q,samples=len(group),max_radius=max(float(row['radius']) for _,row in group),seconds=round(time.time()-started,2))),flush=True)
  if stride==1:trained.append(readout(group,m))
 files=['dyadic.py','theta_oracle.py']
 assert all((Path(__file__).parent/f).read_bytes()==source_at_start[f] for f in files),'Source changed during run; refuse provenance claim'
 source_hashes={f:hashlib.sha256(source_at_start[f]).hexdigest() for f in files}
 for f in files:(output/f).write_bytes((Path(__file__).parent/f).read_bytes())
 result=dict(samples=rows,readouts=trained,source_sha256=source_hashes,dyadic_bits=BITS,external_input='Primitive theta/Mellin identity and explicit real quadratic characters q3/4/5, root number1',sample_oracle_validated=True,coefficient_certificate=bool(trained),GRH_proved=False,new_Lean_declarations=0)
 (output/'oracle-certificates.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--m',type=int,default=64);p.add_argument('--stride',type=int,default=1);a=p.parse_args();run(a.output,a.m,a.stride)
