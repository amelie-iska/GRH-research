"""Small canonical Eisenstein ideal towers and exact raw-zero masks."""
from math import isqrt
from fractions import Fraction as Q
from collections import Counter
PH_ZETA=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
PH_OMEGA=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def norm(z):a,b=z;return a*a-a*b+b*b
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def power(x,n):
    out=(1,0)
    while n:
        if n%2:out=mul(out,x)
        x=mul(x,x);n//=2
    return out

def quotient(x,y):
    N=norm(y);a,b=mul(x,(y[0]-y[1],-y[1]))
    return (a//N,b//N) if a%N==0 and b%N==0 else None

def elements(cap):
    B=isqrt(2*cap)+2
    return [(a,b) for a in range(-B,B+1) for b in range(-B,B+1) if 0<norm((a,b))<=cap]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def prime_ideals(cap):
    out=[(2,0),(1,-1)]
    for g in elements(cap):
        a,b=g;N=norm(g)
        if a%3!=1 or b%3 or N%2==0 or N%3==0:continue
        if prime(N) or b==0 and prime(abs(a)) and abs(a)%3==2:out.append(g)
    return sorted(set(p for p in out if norm(p)<=cap),key=lambda p:(norm(p),p))

def factor_ideal(g,ps):
    rem=g;out=[]
    for p in ps:
        e=0
        while (v:=quotient(rem,p)) is not None:rem=v;e+=1
        if e:out.append(dict(generator=p,norm=norm(p),exponent=e))
    assert norm(rem)==1,(g,rem)
    return out

def canonical_ideals(cap):
    representatives={min(mul(g,u) for u in PH_OMEGA) for g in elements(cap)}
    ps=prime_ideals(cap);rows=[]
    for g in sorted(representatives,key=lambda z:(norm(z),z)):
        fs=factor_ideal(g,ps);split=Counter();inert=[]
        for f in fs:
            N=f['norm']
            if N in (3,4):continue
            if prime(N):assert N%3==1;split[N]+=1
            else:
                p=isqrt(N);assert p*p==N and p%3==2;inert.append(p)
        assert all(s<=2 for s in split.values())
        u=mul((1,1),power(g,6));Nv=norm(g);assert norm(u)==Nv**6
        rows.append(dict(generator_omega=g,norm=Nv,factors=fs,squarefree=all(f['exponent']==1 for f in fs),good_S=Nv%2!=0 and Nv%3!=0,split_prime_coverage=dict(split),inert_prime_coverage=sorted(inert),literal_row_omega=u,literal_row_norm=Nv**6))
    assert sum(r['norm']==1 for r in rows)==1
    return rows

def allowed_multiplicity(group,v):
    value=1
    for p,e in group['rational_prime_factors']:
        if p%3==1:
            sigma=v['split_prime_coverage'].get(p,0)
            if e==1:value*=2-sigma
            elif sigma:return 0
        elif p in v['inert_prime_coverage']:return 0
    return value

def integer_root(n,k):
    lo,hi=0,1
    while hi**k<=n:hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return lo

def family(groups,D,cap=64):
    rows=canonical_ideals(cap)
    for v in rows:
        allowed=[allowed_multiplicity(g,v) for g in groups]
        T=sum(a*abs(g['A_U']) for a,g in zip(allowed,groups))
        v.update(allowed_norm_group_multiplicities=allowed,allowed_ideal_columns=sum(allowed),T_v=T,row_energy=Q(T*T,D),primitive_order6_character_nonprincipal=True,all_nontrivial_powers_nonprincipal=True)
    def moment(selected):
        return dict(rows=len(selected),energy=sum((v['row_energy'] for v in selected),Q(0)),sum_T_v=sum(v['T_v'] for v in selected))
    caps=[]
    for X in (2,4,8,16,64):
        good=[v for v in rows if v['good_S'] and v['norm']<=X]
        dyadic=[v for v in rows if v['good_S'] and 2*v['norm']>=X and v['norm']<X]
        assert good
        caps.append(dict(X=X,H=X**6,primary_goodS_cumulative=moment(good),secondary_goodS_dyadic_interval='[X/2,X)',secondary_goodS_dyadic=moment(dyadic),finite_only=True))
    H=integer_root(D**3,4);X=integer_root(H,6);assert X**8<=D<(X+1)**8
    selected=[v for v in rows if v['good_S'] and v['norm']<=X]
    matched=dict(H_floor_D_3over4=H,X_floor_H_1over6=X,selected_cap_complete=X<=cap,selected_goodS_cumulative=moment(selected),scope='Small finite capacity-matched probe, separate from fixed X64 / H64^6 experiment')
    at49=[v for v in rows if v['norm']==49]
    assert len(at49)==3 and sorted(v['split_prime_coverage'][7] for v in at49)==[1,1,2]
    return dict(primitive_unit_omega=[1,1],primitive_character_order=6,all_nontrivial_powers_nonprincipal=True,exact_conductor_claim=False,probe_all_ideal_v_cap=cap,canonical_associates='lexicographic minimum among six unit associates; beta^6 is associate-independent',primary_family='good-S integral ideals v with Nv<=X, including arbitrary powers and v=1',secondary_family='good-S ideals in [X/2,X); may be empty',rows=rows,caps=caps,capacity_matched=matched,scope='One common D-dependent complex profile aligns every surviving column for every selected v. Raw (m,v)=1 deletion retained. No fixed-W claim; no finite proof of an asymptotic cDX lower bound.')

def direct_symbol(factors,u):
    """Independent residue-field exponentiation, including inert fields."""
    out=0
    for (a,b),e in factors:
        q=a*a-a*b+b*b
        if b:
            p=q;omega=(-a*pow(b,-1,p))%p;zeta=(1+omega)%p
            residue=(u[0]+u[1]*omega)%p
            if residue==0:return None
            value=pow(residue,(p-1)//6,p);phase=[pow(zeta,j,p) for j in range(6)].index(value)
        else:
            p=abs(a);x=(u[0]%p,u[1]%p)
            if x==(0,0):return None
            def pmul(x,y):return tuple(v%p for v in mul(x,y))
            def ppow(x,n):
                y=(1,0)
                while n:
                    if n%2:y=pmul(y,x)
                    x=pmul(x,x);n//=2
                return y
            value=ppow(x,(p*p-1)//6);phase=[ppow((1,1),j) for j in range(6)].index(value)
        out=(out+e*phase)%6
    return out
