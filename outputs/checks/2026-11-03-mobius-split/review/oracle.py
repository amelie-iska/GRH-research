"""Independent divisor-closed ideal-monoid and sextic-mask oracle.
Only reviewer-owned artifacts are written. Not a full ideal-counting proof.
"""
from pathlib import Path
from itertools import product
import json,math
OUT=Path(__file__).resolve().parent
PRIMES=[(7,2),(7,4),(13,3),(13,9),(19,7),(19,11)]
Z=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO=(0,)*len(PRIMES)

def norm(e):return math.prod(p**v for (p,_),v in zip(PRIMES,e))
def mu(e):return 0 if any(v>1 for v in e) else (-1)**sum(e)
def divs(e):return product(*(range(v+1) for v in e))
def minus(e,d):return tuple(v-w for v,w in zip(e,d))
def convolve3(e,f,g):
    return sum(f(a)*g(b) for a in divs(e) for b in divs(minus(e,a)))
def ideal_list(maxnorm):
    exponents=[range(int(math.log(maxnorm,p))+2) for p,_ in PRIMES]
    return [e for e in product(*exponents) if norm(e)<=maxnorm]
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def powel(x,n):
    out=(1,0)
    for _ in range(n):out=mul(out,x)
    return out
def phase(e,u):
    out=0
    for (p,w),v in zip(PRIMES,e):
        if not v:continue
        value=(u[0]+u[1]*w)%p
        if not value:return None
        target=pow(value,(p-1)//6,p)
        roots={pow(1+w,j,p):j for j in range(6)}
        assert len(roots)==6
        out+=v*roots[target]
    return out%6
def add_scaled(out,weight,ph):
    if ph is not None:out[0]+=weight*Z[ph][0];out[1]+=weight*Z[ph][1]
def vals(D,U,u,nu):
    direct=[0,0];short=[0,0];typei=[0,0];typeii=[0,0]
    for e in IDEALS:
        N=norm(e)
        if mu(e)==0 or not D<=N<=2*D:continue
        ph=phase(e,u)
        if ph is None:continue
        if nu=='kummer-lambda':ph=(ph+phase(e,(1,2)))%6
        weight=(N-D)*(2*D-N) # exact finite annular diagnostic, not claimed C-infty
        a=lambda d:mu(d) if norm(d)<=U else 0
        b=lambda d:mu(d)-a(d)
        I=convolve3(e,a,a);II=convolve3(e,b,b)
        assert mu(e)==2*a(e)-I+II
        add_scaled(direct,mu(e)*weight,ph)
        add_scaled(short,a(e)*weight,ph)
        add_scaled(typei,I*weight,ph)
        add_scaled(typeii,II*weight,ph)
    assert direct==[2*short[i]-typei[i]+typeii[i] for i in range(2)]
    return dict(D=D,U=U,row=u,nu=nu,direct=direct,short=short,typeI=typei,typeII=typeii)

IDEALS=ideal_list(3000)
identity_checks=group_checks=0
for U in [1,7,10,50]:
    a=lambda d:mu(d) if norm(d)<=U else 0
    b=lambda d:mu(d)-a(d)
    for e in IDEALS:
        I=convolve3(e,a,a);II=convolve3(e,b,b)
        assert mu(e)==2*a(e)-I+II;identity_checks+=1
        if mu(e)==0:continue
        Ig=0;IIg=0
        for d in divs(e):
            beta=sum(mu(x)*mu(minus(d,x)) for x in divs(d)
                     if norm(x)<=U and norm(minus(d,x))<=U)
            Ig+=beta
        for aa in divs(e):
            ss=minus(e,aa)
            if norm(aa)<=U or norm(ss)<=U:continue
            gu=sum(mu(bb) for bb in divs(ss) if norm(bb)>U)
            assert gu==-sum(mu(bb) for bb in divs(ss) if norm(bb)<=U)
            IIg+=mu(aa)*gu
        assert I==Ig and II==IIg;group_checks+=1
        if U==1 and norm(e)>1:assert I==1 and II==mu(e)+1>=0
rows=[(a,b) for a in range(-5,6) for b in range(-5,6) if 0<a*a-a*b+b*b<=12]
rows+=[(1,3),powel((1,3),6)]
cases=[vals(D,U,u,nu) for D in [20,50,200] for U in [1,7,10]
       for u in rows for nu in ['principal','kummer-lambda']]
# A full denominator's local masks survive exponent6, and conductor reduction
# alone cannot justify changing them. This is a component of new split checks.
assert phase((1,0,0,0,0,0),powel((1,3),6)) is None
for e in IDEALS:
    if mu(e)!=0:
        for a in divs(e):
            bb=minus(e,a)
            for u in rows[:7]+[(1,3)]:
                x,y,t=phase(a,u),phase(bb,u),phase(e,u)
                assert (t is None)==(x is None or y is None)
                if t is not None:assert t==(x+y)%6
report=dict(passed=True,identity_cases=identity_checks,squarefree_group_cases=group_checks,
            exact_row_checks=len(cases),actual_primes=PRIMES,columns=len(IDEALS),
            sixth_power_collision_preserved=True,principal_and_fixed_kummer_twists=True,
            limitations='Finite divisor-closed prime-support subset; exact annular integer profile is not claimed smooth; no prime-ideal theorem or MS bound certified numerically.',
            examples=cases[:8])
(OUT/'oracle.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='examples'},indent=2))
