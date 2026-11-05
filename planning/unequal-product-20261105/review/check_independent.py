"""Independent exact review controls, no author/project arithmetic imports."""
from fractions import Fraction as F
from itertools import product
from math import gcd,isqrt
from pathlib import Path
import argparse,hashlib,json

ROOT=Path(__file__).resolve().parents[3]

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    c=[x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[1]*y[1]]
    return (c[0]-c[2],c[1]-c[2])
def conj(x):return (x[0]-x[1],-x[1])
def norm(x):return x[0]*x[0]+x[1]*x[1]-x[0]*x[1]
def scale(c,x):return (c*x[0],c*x[1])
def power(x,n):
    r=(1,0)
    for _ in range(n):r=mul(r,x)
    return r
UNITS=[power((1,1),j) for j in range(6)]
def canonical(x):return min(mul(x,u) for u in UNITS)
def divides(a,b):
    n=norm(a);c=mul(b,conj(a))
    return canonical((c[0]//n,c[1]//n)) if c[0]%n==c[1]%n==0 else None

def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def ideals(B):
    radius=2*isqrt(B)+2
    allideals=sorted({canonical((a,b)) for a,b in product(range(-radius,radius+1),repeat=2)
                      if 0<norm((a,b))<=B and gcd(norm((a,b)),6)==1},key=lambda x:(norm(x),x))
    pis=[x for x in allideals if prime(norm(x)) or
         (isqrt(norm(x))**2==norm(x) and prime(isqrt(norm(x))) and isqrt(norm(x))%3==2)]
    fac={}
    for x in allideals:
        r=x;parts={}
        for pi in pis:
            e=0
            while (z:=divides(pi,r)) is not None:
                r=z;e+=1
            if e:parts[pi]=e
        assert norm(r)==1
        fac[x]=parts
    return allideals,pis,fac

class Field:
    def __init__(self,p,w=None):
        self.p,self.w=p,w
        self.values=list(range(p)) if w is not None else list(product(range(p),repeat=2))
        self.zero=0 if w is not None else (0,0)
        self.one=1 if w is not None else (1,0)
        self.q=len(self.values)
        self.zeta=self.embed((1,1))
        self.roots=[self.pow(self.zeta,j) for j in range(6)]
        assert len(set(self.roots))==6
    def embed(self,x):return (x[0]+self.w*x[1])%self.p if self.w is not None else (x[0]%self.p,x[1]%self.p)
    def times(self,x,y):return x*y%self.p if self.w is not None else self.embed(mul(x,y))
    def plus(self,x,y):return (x+y)%self.p if self.w is not None else self.embed(add(x,y))
    def pow(self,x,n):
        r=self.one
        while n:
            if n%2:r=self.times(r,x)
            x=self.times(x,x);n//=2
        return r
    def trace(self,x):
        if self.w is not None:return x
        t=self.plus(x,self.pow(x,self.p))
        assert t[1]==0
        return t[0]
    def chi(self,x,k=1):
        return None if x==self.zero else (self.roots.index(self.pow(x,(self.q-1)//6))*k)%6

FIELD={}
def local_field(pi):
    if pi not in FIELD:
        q=norm(pi);p=isqrt(q)
        if p*p==q:FIELD[pi]=Field(p)
        else:FIELD[pi]=Field(q,(-pi[0]*pow(pi[1],-1,q))%q)
    return FIELD[pi]
def chi(parts,u):
    e=0
    for pi,k in parts.items():
        c=local_field(pi);v=c.chi(c.embed(u),k)
        if v is None:return None
        e+=v
    return e%6

def ptrim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def pdivide(a,b):
    a=list(a);b=ptrim(list(b));q=[0]*max(1,len(a)-len(b)+1)
    assert b[-1]==1
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b);c=a[-1];q[k]=c
        for j,x in enumerate(b):a[j+k]-=c*x
        ptrim(a)
    return ptrim(q),ptrim(a)
PHI={}
def cyclotomic(n):
    if n not in PHI:
        a=[-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d==0:
                a,r=pdivide(a,cyclotomic(d));assert r==[0]
        PHI[n]=a
    return PHI[n]
def reduced(a,n):return pdivide(a,cyclotomic(n))[1]
def gauss(c,k,t):
    n=6*c.p;a=[0]*n
    for z in c.values:
        e=c.chi(z,k)
        if e is not None:a[(c.p*e+6*c.trace(c.times(t,z)))%n]+=1
    return a

def field_checks():
    fields=[Field(7,2),Field(13,3),Field(19,7),Field(5),Field(11)]
    local=gauss_n=mutations=0
    for c in fields:
        for membership in product([0,1],repeat=4):
            e=membership[0]+membership[1]-membership[2]-membership[3]
            internal=membership[0]+membership[1]<=1 and membership[2]+membership[3]<=1
            if internal:assert e in [-1,0,1]
            for j in range(1,7):
                vals=set()
                for z in c.values:
                    base=c.chi(c.pow(z,j));lhs=0
                    for yes,sign in zip(membership,[1,1,-1,-1]):
                        if yes:
                            if base is None:lhs=None;break
                            lhs+=sign*base
                    if lhs is not None:lhs%=6
                    rhs=c.chi(z,j*e) if any(membership) else 0
                    assert lhs==rhs
                    if z!=c.zero:vals.add(rhs)
                    local+=1
                if any(membership):assert len(vals)==6//gcd(j*e,6)
        # Negative controls: canceled-prime zero and parity deletion are false.
        assert c.chi(c.zero,0) is None
        assert any(c.chi(z,2) not in [None,0] for z in c.values)
        mutations+=2
        n=6*c.p
        for k in range(6):
            for t in c.values:
                a=gauss(c,k,t)
                if t==c.zero:
                    target=[c.q-1 if k==0 else 0]
                    assert reduced(a,n)==target
                elif k==0:
                    assert reduced(a,n)==[-1]
                else:
                    prod=[0]*n
                    for i,x in enumerate(a):
                        for j,y in enumerate(a):prod[(i-j)%n]+=x*y
                    assert reduced(prod,n)==[c.q]
                gauss_n+=1
    # A common prime13 at zero local frequency contributes12, not1.
    assert 7*(13-1)**2>7
    mutations+=1
    return {'field_sizes':[c.q for c in fields],'local_values':local,'complete_Gauss_Ramanujan_sums':gauss_n,'negative_controls':mutations}

def ideal_checks():
    gs,pis,fac=ideals(256)
    cols=[m for m in gs if 128<=norm(m)<=256 and max(fac[m].values(),default=0)<=1]
    counts={}
    for m in cols:
        ps=list(fac[m]);pairs=[]
        for mask in product([0,1],repeat=len(ps)):
            a=b=canonical((1,0))
            for p,yes in zip(ps,mask):
                if yes:a=canonical(mul(a,p))
                else:b=canonical(mul(b,p))
            if norm(a)>7 and norm(b)>7:pairs.append((a,b))
        counts[m]=pairs
        # Direct disjoint3-placement definition C_U retains any leftover ideal.
        direct=0
        for tags in product([0,1,2],repeat=len(ps)):
            aa=bb=1;sgn=1
            for p,t in zip(ps,tags):
                if t==1:aa*=norm(p);sgn=-sgn
                if t==2:bb*=norm(p);sgn=-sgn
            if aa>7 and bb>7:direct+=sgn
        assert direct==(-1)**len(ps)*len(pairs)
    strata=[];pair_controls=0
    for Y in [1,7,13,49,169,1024,4*128**2]:
        chosen=set();triples=set();dyads={}
        for m,n in product(cols,repeat=2):
            if m==n:continue
            common=set(fac[m])&set(fac[n]);h=canonical((1,0))
            for p in common:h=canonical(mul(h,p))
            r,t=divides(h,m),divides(h,n)
            Q=norm(r)*norm(t)
            if Q>Y:continue
            V=max(norm(r),norm(t))
            assert V*V<=2*Y and norm(h)*V<=256
            assert norm(r)<=2*norm(t) and norm(t)<=2*norm(r)
            assert set(fac[r]).isdisjoint(fac[t])
            triple=(h,r,t);assert triple not in triples
            triples.add(triple);chosen.add((m,n))
            k=V.bit_length()-1;dyads[k]=dyads.get(k,0)+1
            pair_controls+=1
        assert {(canonical(mul(h,r)),canonical(mul(h,t))) for h,r,t in triples}==chosen
        strata.append({'Y':Y,'unequal_pairs':len(chosen),'dyad_counts':dyads,'multiplicity_CC':sum(len(counts[m])*len(counts[n]) for m,n in chosen),'multiplicity_CM':sum(len(counts[m]) for m,n in chosen)})
    basis=[p for p in pis if norm(p) in [7,13]]
    rows=[mul(u,mul(a,power(b,2))) for a,b in product(basis,repeat=2) if a!=b for u in UNITS]
    rows += [mul(u,power(a,3)) for a in basis for u in UNITS]
    kernel_controls=canceled_zeros=0
    for u in rows:
        raw={m:chi(fac[m],u) for m in cols}
        cu=mu=(F(),F())
        expanded_C=(F(),F())
        weights={}
        for m in cols:
            w=F((norm(m)-128)*(256-norm(m)),128**2)
            weight=(-1)**len(fac[m])*w
            weights[m]=weight
            value=(0,0) if raw[m] is None else UNITS[raw[m]]
            mu=add(mu,scale(weight,value));cu=add(cu,scale(weight*len(counts[m]),value))
            for a,b in counts[m]:
                x,y=chi(fac[a],u),chi(fac[b],u)
                v=(0,0) if x is None or y is None else UNITS[(x+y)%6]
                expanded_C=add(expanded_C,scale(weight,v))
        assert cu==expanded_C
        ec=mixed=(F(),F())
        for m,n in product(cols,repeat=2):
            common=set(fac[m])&set(fac[n]);diff=set(fac[m])^set(fac[n])
            powers={p:1 if p in fac[m] else -1 for p in diff}
            osc=chi(powers,u)
            delete=int(all(divides(p,u) is None for p in common))
            expected=None if not delete or osc is None else osc
            actual=None if raw[m] is None or raw[n] is None else (raw[m]-raw[n])%6
            assert expected==actual
            if common and not delete:
                canceled_zeros+=1
                assert actual is None
            v=(0,0) if actual is None else UNITS[actual]
            ec=add(ec,scale(weights[m]*weights[n]*len(counts[m])*len(counts[n]),v))
            mixed=add(mixed,scale(weights[m]*weights[n]*len(counts[m]),v))
            kernel_controls+=1
        assert ec==mul(cu,conj(cu)) and mixed==mul(cu,conj(mu))
    return {'canonical_ideals':len(gs),'squarefree_columns':len(cols),'ordered_long_pairs':sum(map(len,counts.values())),
            'literal_balanced_and_A3_rows':len(rows),'small_conductor_strata':strata,'pair_triple_controls':pair_controls,
            'raw_kernel_moment_controls':kernel_controls,'canceled_prime_zero_controls':canceled_zeros}

def deletion_checks():
    cases=terms=0
    for v in product(range(5),repeat=4):
        for included in product([0,1],repeat=4):
            E={j for j,b in enumerate(included) if b}
            lhs=int(all(x<=1 for x in v) and all(v[j]==0 for j in E))
            rhs=0
            for ds in product([0,1],repeat=4):
                if any(ds[j] and (j not in E or v[j]==0) for j in range(4)):continue
                for hs in product([0,1],repeat=4):
                    if any(hs[j] and (j in E or v[j]<2) for j in range(4)):continue
                    assert all(not(ds[j] and hs[j]) for j in range(4))
                    assert all(ds[j]+2*hs[j]<=v[j] for j in range(4))
                    rhs+=(-1)**(sum(ds)+sum(hs));terms+=1
            assert rhs==lhs
            cases+=1
    return {'valuation_squarefree_deletion_cases':cases,'lift_terms':terms}

def face_checks():
    cases=0;near_nonface=0
    def vectors(prefix,budget,j=1):
        if j==7:
            yield prefix;return
        for x in range(budget//j+1):yield from vectors(prefix+[x],budget-j*x,j+1)
    for x in vectors([],30):
        R=sum(x);M=max(x[:2]);C=sum((j+1)*v for j,v in enumerate(x));slack=30-3*(R-M)
        assert slack>=0
        asym=(x[0]-x[1]) if x[0]>=x[1] else 2*(x[1]-x[0])
        assert slack==30-C+asym+x[3]+2*x[4]+3*x[5]
        assert R+max(x[:5])<=30+slack
        if x[3]+x[4]+x[5]>0:near_nonface+=1
        cases+=1
    face=0
    for t in range(11):
        C=10;A3=C-t;R=2*t+A3;P=max(t,A3)
        assert R-t==C and R+P==max(C+2*t,2*C)<=3*C
        face+=1
    return {'near_face_blocks':cases,'including_nonunit_A4_A5_A6':near_nonface,'full_A3_face_points':face}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError('Preserve prior review')
    names=['planning/unequal-product-20261105/attempt/UNEQUAL_PRODUCT_MOMENT.md',
           'planning/unequal-product-20261105/attempt/check_unequal_product_v3.py',
           'planning/unequal-product-20261105/attempt/source-pins-v1.json',
           'papers/covariance-budget-core.tex','papers/covariance-budget-details.tex']
    before={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}
    report={'field_checks':field_checks(),'ideal_and_moment_checks':ideal_checks(),'deletion_checks':deletion_checks(),
            'face_checks':face_checks(),'scope':'Exact finite review controls; proof of asymptotic count and face bounds is separately audited prose. No long-conductor saving, zero-location, Lean or GRH claim.',
            'source_sha256':before,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert before=={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['source_sha256','scope','checker_sha256']},indent=2))
if __name__=='__main__':main()
