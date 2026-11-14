"""Adaptive certified theta/Mellin samples for primitive q3/q4/q5 only.

All five error endpoints are exact Fractions. Parameters and transcendental
precision change with the request. The classical primitive theta identity is
an explicit external analytic input, never an assumed zero-location result.
"""
from fractions import Fraction as F
from pathlib import Path
from dataclasses import dataclass
from functools import lru_cache
import argparse,hashlib,json,time
import precision as arithmetic
from precision import Context,Complex,decimal_integer
SOURCE_AT_IMPORT=Path(__file__).read_bytes()

FAMILIES={3:(1,(0,1,-1)),4:(1,(0,1,0,-1)),5:(0,(0,1,-1,-1,1))}

def exact(x):
    if type(x) is int:return F(x)
    if isinstance(x,F):return x
    raise TypeError('Exact int/Fraction required')

def validate(q,eta):
    if type(q) is not int or q not in FAMILIES:raise ValueError('Only integer conductors3/4/5 supported')
    if not isinstance(eta,F):raise TypeError('Positive rational Fraction tolerance required')
    if eta<=0:raise ValueError('Tolerance must be positive')

def E(x):
    x=exact(x)
    if x<0:raise ValueError('Nonnegative exponential-majorant argument required')
    return F(1,1<<(x.numerator//x.denominator))

def Q(x):
    x=exact(x)
    if x<=0:raise ValueError('Positive tail argument required')
    return 1/x+2/x**2+2/x**3

def panels(J):
    if type(J) is not int or J<1:raise ValueError('Positive dyadic panel count required')
    return tuple((F(2**j)*(1+F(2*l+1,8)),F(2**j,8)) for j in range(J) for l in range(4))

def n_tail(q,N):
    a,_=FAMILIES[q];d=F(3,q);n=N+1;C=F(1) if a==0 else (1+1/d)/2
    return 2*C*Q(d*n*n)*E(d*n*n/2)/(1-E(d*n))

def time_tail(q,N,J):
    a,_=FAMILIES[q];d=F(3,q);T=2**J
    return sum((2*n**a*T**3*E(d*n*n*T)*Q(d*n*n*T) for n in range(1,N+1)),F())

def quadrature_tail(q,N,J,K):
    a,_=FAMILIES[q];d=F(3,q);total=F()
    for m,h in panels(J):
        r=m/2;v=h/r;B=max((m+r)**2,(m-r)**(-2),F(1))
        total+=sum((2*n**a*2*h*3*B*E(d*n*n*m/2)*v**(2*K+2)/(F(2*K+3)*(1-v*v)) for n in range(1,N+1)),F())
    return total

@dataclass(frozen=True,slots=True)
class Parameters:
    N:int
    J:int
    K:int
    n_tail:F
    time_tail:F
    quadrature:F
    discard:F
    active:tuple
    discarded_pairs:int
    per_pair_threshold:F

@lru_cache(maxsize=None,typed=True)
def parameters(q,eta):
    validate(q,eta);allocation=eta/8
    N=1
    while n_tail(q,N)>allocation:N+=1
    J=1
    while time_tail(q,N,J)>allocation:J+=1
    K=0
    while quadrature_tail(q,N,J,K)>allocation:K+=1
    threshold=eta/F(8*4*J*N);a,chi=FAMILIES[q];d=F(3,q)
    active=[];discard=F();skipped=0
    for m,h in panels(J):
        for n in range(1,N+1):
            if not chi[n%q]:continue
            bound=4*h*n**a*(m+h)**2*E(d*n*n*(m-h))
            if bound<=threshold:discard+=bound;skipped+=1
            else:active.append((m,h,n,chi[n%q]*n**a))
    assert discard<=allocation
    return Parameters(N,J,K,n_tail(q,N),time_tail(q,N,J),quadrature_tail(q,N,J,K),discard,tuple(active),skipped,threshold)

@lru_cache(maxsize=64,typed=True)
def active_constants(q,eta,bits):
    plan=parameters(q,eta);ctx=Context(bits)
    return tuple((m,h,weight,ctx.pi()*F(n*n,q)*m,ctx.log(m)) for m,h,n,weight in plan.active)

def integrate(q,eta,s):
    """Private finite-expression evaluation; point/node wrappers prove the domain.

    The analytic error bounds apply to the known true input point. A widened
    arithmetic enclosure need not itself lie inside the closed domain.
    """
    validate(q,eta)
    if not isinstance(s,Complex):raise TypeError('Certified complex rectangle required')
    plan=parameters(q,eta);ctx=s.context;a,_=FAMILIES[q]
    powers=((s+a)/2-1,(1-s+a)/2-1);total=ctx.complex(0)
    for m,h,weight,lm,logm in active_constants(q,eta,ctx.bits):
        u=h/m
        for p in powers:
            previous=ctx.complex(0);current=ctx.complex(1);acc=current
            for j in range(2*plan.K):
                nxt=((p-lm-j)*current*u-previous*lm*(u*u))/(j+1)
                previous,current=current,nxt
                if (j+1)%2==0:acc+=current/(j+2)
            total+=ctx.exp(p*logm-lm)*acc*(2*h*weight)
    return total

def _evaluate(q,eta,factory,metadata,initial_bits=None):
    validate(q,eta);plan=parameters(q,eta)
    if initial_bits is not None and (type(initial_bits) is not int or initial_bits<32):raise ValueError('Integer initial precision >=32 required')
    bits=initial_bits if initial_bits is not None else 32*((max(128,eta.denominator.bit_length()-eta.numerator.bit_length()+64)+31)//32)
    serialization_bits=max(32,eta.denominator.bit_length()-eta.numerator.bit_length()+8)
    while F(5,1<<serialization_bits)>eta/8:serialization_bits+=1
    def up(value):return F(-(-value.numerator*(1<<serialization_bits)//value.denominator),1<<serialization_bits)
    attempts=[]
    while True:
        ctx=Context(bits);s,root=factory(ctx);total=integrate(q,eta,s)
        attempts.append({'bits':bits,'interval_radius':total.radius()})
        if total.radius()<=eta/4:break
        bits*=2
    budget={'n_tail':plan.n_tail,'time_tail':plan.time_tail,'quadrature':plan.quadrature,'discard':plan.discard,'interval_arithmetic':total.radius()}
    budget={key:up(value) for key,value in budget.items()}
    radius=sum(budget.values(),F());assert radius<=eta
    return {'q':q,'requested_sample_error':eta,**metadata,'N':plan.N,'J':plan.J,'T':2**plan.J,'K':plan.K,'bits':bits,
        'center_real':total.re.midpoint(),'center_imag':total.im.midpoint(),'radius':radius,'budget':budget,
        'node_box':s.encode(),'root_box':root.encode() if root is not None else None,'quadrature_sum_box':total.encode(),
        'active_pairs':len(plan.active),'discarded_pairs':plan.discarded_pairs,'per_pair_discard_threshold':plan.per_pair_threshold,
        'precision_attempts':attempts,'budget_rounding_bits':serialization_bits,'raw_interval_radius':total.radius(),'scope':'Known rational point or true-circle node in fixed domain; primitive quadratic q3/4/5, classical theta identity. Not all-conductor/zero-location/Lean/GRH.'}

def point(q,x,y,eta,initial_bits=None):
    validate(q,eta);x,y=exact(x),exact(y)
    if not -1<=x<=2 or abs(y)>F(4,3):raise ValueError('True point outside proved domain')
    return _evaluate(q,eta,lambda c:(c.complex(x,y),None),{'target_kind':'exact_rational_point','point_real':x,'point_imag':y},initial_bits)

def circle(q,j,m,eta,initial_bits=None):
    validate(q,eta)
    if type(m) is not int or type(j) is not int or m<1 or not 0<=j<m:raise ValueError('Valid integer circle index/count required')
    def factory(c):
        root=c.exp(c.complex(0,c.pi()*F(2*j,m)))
        return c.complex(F(1,2))+root*F(6,5),root
    return _evaluate(q,eta,factory,{'target_kind':'true_circle_node','node_index':j,'node_count':m,'circle_center':F(1,2),'circle_radius':F(6,5)},initial_bits)

def encode(value):
    if isinstance(value,F):
        try:display=float(value)
        except OverflowError:display=None
        return {'numerator':decimal_integer(value.numerator),'denominator':decimal_integer(value.denominator),'display':display}
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [encode(v) for v in value]
    return value

def run(output,eta,conductors=(3,4,5),m=64,stride=1):
    if not isinstance(output,Path):raise TypeError('Path output required')
    if output.exists():raise FileExistsError('Preserve existing output')
    if type(m) is not int or type(stride) is not int or m<1 or stride<1:raise ValueError('Positive integer node count/stride required')
    if not isinstance(conductors,(tuple,list)) or not conductors or len(set(conductors))!=len(conductors):raise ValueError('Distinct supported conductors required')
    for q in conductors:validate(q,eta)
    names=('precision.py','adaptive_theta.py');sources={n:Path(__file__).with_name(n).read_bytes() for n in names}
    if sources['precision.py']!=arithmetic.SOURCE_AT_IMPORT or sources['adaptive_theta.py']!=SOURCE_AT_IMPORT:raise ValueError('Loaded modules differ from source at run entry')
    output.mkdir(parents=True)
    for n,b in sources.items():(output/n).write_bytes(b)
    rows=[];started=time.monotonic()
    try:
        for q in conductors:
            for j in range(0,m,stride):rows.append(circle(q,j,m,eta))
            print(json.dumps({'q':q,'samples':sum(r['q']==q for r in rows),'seconds':round(time.monotonic()-started,3),'max_radius':max(float(r['radius']) for r in rows if r['q']==q)}),flush=True)
        assert all(Path(__file__).with_name(n).read_bytes()==b for n,b in sources.items()),'Source changed during run'
        record={'samples':rows,'complete_circle':stride==1,'circle_node_count':m,'evaluated_sample_count_per_family':len(range(0,m,stride)),'stride':stride,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in sources.items()},'external_input':'Primitive quadratic theta/Mellin identity q3/4/5 with rootnumber1; exact Gaussian/Cauchy majorants','sample_oracle_validated':True,'readout_certificate':False,'new_Lean_declarations':0,'GRH_proved':False}
        (output/'sample-certificates.json').write_text(json.dumps(encode(record),indent=2)+'\n')
    except Exception as error:
        (output/'failure.json').write_text(json.dumps({'error_type':type(error).__name__,'error':str(error),'completed_samples':len(rows),'sample_oracle_validated':False},indent=2)+'\n');raise

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--sample-error',type=F,required=True);p.add_argument('--q',type=int,action='append');p.add_argument('--m',type=int,default=64);p.add_argument('--stride',type=int,default=1);a=p.parse_args();run(a.output,a.sample_error,tuple(a.q or(3,4,5)),a.m,a.stride)
