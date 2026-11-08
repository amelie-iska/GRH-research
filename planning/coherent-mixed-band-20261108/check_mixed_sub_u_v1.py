from collections import Counter
from functools import lru_cache
from fractions import Fraction as Q
from itertools import product
from math import isqrt, prod
from pathlib import Path
import json

# Finite exact control. The rational nodal profiles below model the selector
# endpoints and coefficients; they are not an experiment on asymptotic powers.
def isprime(n):
    return n>1 and all(n%j for j in range(2,isqrt(n)+1))
def prime_ideals(B):
    out=[]
    for p in range(5,B+1):
        if not isprime(p):
            continue
        if p%3==2:
            if p*p<=B:
                out.append((p*p,p,None))
        else:
            roots=[w for w in range(p) if (w*w+w+1)%p==0]
            assert len(roots)==2
            out.extend((p,p,w) for w in roots)
    return sorted(out)
P=prime_ideals(20000)
norms=tuple(rec[0] for rec in P)

@lru_cache(None)
def norm(I):
    return prod(norms[j] for j in I)
def mu(I):
    return (-1)**len(I)
def sf(B):
    def go(j,I,n):
        yield I
        while j<len(P) and n*norms[j]<=B:
            yield from go(j+1,I|{j},n*norms[j])
            j+=1
    return tuple(go(0,frozenset(),1))
@lru_cache(None)
def splits(I):
    L=sorted(I)
    return [frozenset(p for j,p in enumerate(L) if mask>>j&1)
            for mask in range(1<<len(L))]
@lru_cache(None)
def ternary(I,U):
    return sum(mu(a)*mu(b) for a in splits(I) for b in splits(I-a)
               if norm(a)<=U and norm(b)<=U)
def gap_coeff(I,U):
    return mu(I)*(sum(norm(a)>U and norm(I-a)>U for a in splits(I))-1)
def squarefree_divides(d,I):
    return not d-I

zero=(0,0)
def add(x,y):
    return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    a,b=x
    c,d=y
    return a*c-b*d,a*d+b*c-b*d
def scale(x,s):
    return x[0]*s,x[1]*s
def conj(x):
    return x[0]-x[1],-x[1]
def sq(x):
    a,b=x
    return a*a-a*b+b*b
def power(x,n):
    y=(1,0)
    while n:
        if n&1:
            y=mul(y,x)
        x=mul(x,x)
        n//=2
    return y

@lru_cache(None)
def primary(pidx):
    n,p,w=P[pidx]
    if w is None:
        z=((-p if p%3==2 else p),0)
        assert z[0]%3==1 and sq(z)==n
        return z
    bnd=2*isqrt(n)+2
    candidates=[(a,b) for a in range(-bnd,bnd+1) for b in range(-bnd,bnd+1)
                if a%3==1 and b%3==0 and (a+b*w)%p==0 and sq((a,b))==n]
    assert len(candidates)==1,(p,w,candidates)
    return candidates[0]
def generator(I):
    z=(1,0)
    for j in I:
        z=mul(z,primary(j))
    return z

@lru_cache(None)
def local_symbol(j,u):
    n,p,w=P[j]
    if w is not None:
        v=(u[0]+u[1]*w)%p
        if v==0:
            return zero
        target=pow(v,(p-1)//6,p)
        e=next(k for k in range(6) if pow((1+w)%p,k,p)==target)
    else:
        v=tuple(x%p for x in u)
        if v==zero:
            return zero
        def mod_mul(x,y):
            return tuple(k%p for k in mul(x,y))
        def mod_pow(x,n):
            y=(1,0)
            while n:
                if n&1:
                    y=mod_mul(y,x)
                x=mod_mul(x,x)
                n//=2
            return y
        target=mod_pow(v,(n-1)//6)
        e=next(k for k in range(6) if mod_pow((1,1),k)==target)
    return power((1,1),e)

@lru_cache(None)
def symbol(I,u):
    z=(1,0)
    for j in I:
        z=mul(z,local_symbol(j,u))
        if z==zero:
            break
    return z
@lru_cache(None)
def w(x):
    if not 1<x<2:
        return zero
    return scale((1,x),(x-1)**5*(2-x)**5)
def cut(x):
    if x<=0:
        return Q(0)
    if x>=1:
        return Q(1)
    return 126*x**5-420*x**6+540*x**7-315*x**8+70*x**9
def selector(F,Y,U):
    return cut(Q(F,Y)-1)*cut(2-2*Q(F,U))
def addinto(z,a,c):
    return add(z,mul(a,c))

counts=Counter()
records=[]
# Two actual unweighted literal mixed-pivot blocks with the exact capacity.
for D,U,H,A1,A2,Y in [(3136,56,418,7,7,7),(6400,80,715,7,7,11),
                        (10000,100,1000,13,7,13)]:
    assert U*U<=D<=Q(7,2)*U*U and H**4<=D**3
    cols=sf(2*D)
    ann=[I for I in cols if D<norm(I)<2*D]
    residual=[I for I in cols if norm(I)<Q(2*D,Y*U)]
    f_all=[I for I in cols if selector(norm(I),Y,U)]
    f_smooth=[I for I in f_all if all(norms[p]<=U for p in I)]
    assert f_all==f_smooth
    fs=set(f_all)
    assert not selector(Y,Y,U) and not selector(U,Y,U)
    assert not selector(U+1,Y,U)
    assert all(not selector(norm(I),Y,U) for I in cols if any(norms[p]>U for p in I))
    rows=[(v1,v2,mul(generator(v1),power(generator(v2),2))) for v1 in cols
          if A1<=norm(v1)<2*A1 for v2 in cols if A2<=norm(v2)<2*A2
          and not v1&v2 and norm(v1)*norm(v2)**2<=H]
    assert rows and len({u for _,_,u in rows})==len(rows)
    assert all(sq(u)==norm(v1)*norm(v2)**2 for v1,v2,u in rows)
    k0=Q(0)
    live_buckets=0
    rawzeros=0
    for v1,v2,u in rows:
        bucket={}
        split_bucket={}
        for m in ann:
            dlist=[d for d in splits(m) if d in fs]
            if not dlist:
                continue
            ac=ternary(m,U)
            gc=gap_coeff(m,U)
            assert ac==gc
            for d in dlist:
                a=m-d
                assert not a&d and norm(m)==norm(a)*norm(d)
                counts['annular_factor_paths']+=1
                s=symbol(a,u)
                if d & (v1|v2) or s==zero:
                    rawzeros+=1
                    continue
                assert symbol(m,u)==mul(symbol(d,u),s)
                z=mul(w(Q(norm(m),D)),s)
                bucket[d]=add(bucket.get(d,zero),scale(z,ac))
                sp=sum(norm(e)>U and norm(m-e)>U for e in splits(m))
                neg,gg=split_bucket.get(d,(zero,zero))
                split_bucket[d]=(add(neg,scale(z,mu(m))),add(gg,scale(z,mu(m)*sp)))
        for d,z in bucket.items():
            a,b=split_bucket[d]
            assert z==add(b,scale(a,-1))
            k0+=selector(norm(d),Y,U)*mu(d)*sq(z)
            live_buckets+=1
        for r in splits(v1|v2):
            g1,g2=r&v1,r&v2
            h1,h2=v1-r,v2-r
            z0=mul(generator(g1),power(generator(g2),2))
            z1=mul(generator(h1),power(generator(h2),2))
            assert u==mul(z0,z1)
            assert norm(g1)*Q(A1,norm(g1))==A1 and norm(g2)*Q(A2,norm(g2))==A2
            for I in residual:
                s=symbol(I,u)
                assert s==mul(symbol(I,z0),symbol(I,z1))
                counts['actual_frozen_row_raw_transfers']+=1
                counts['frozen_row_raw_zeros']+=s==zero
    assert rawzeros and live_buckets and k0!=0

    # The exact continuous integrand is tested at fixed rational points.
    # The discrete term uses the actual primes, strictly above U.
    def q_t(t):
        Q_t=Q(0)
        for v1,v2,u in rows:
            for d in f_all:
                if d & (v1|v2):
                    continue
                f=norm(d)
                vec=zero
                short=zero
                for a in residual:
                    if a&d:
                        continue
                    x=Q(f*norm(a),D)*t
                    if not 1<x<2:
                        continue
                    m=d|a
                    assert norm(m)<Q(2*D,U)<=7*U
                    a0=ternary(m,U)
                    a1=mu(m)*(1 if norm(m)<=U else -1)
                    assert a0==a1
                    s=symbol(a,u)
                    counts['short_coefficients_pointwise']+=1
                    counts['short_unit_residual_paths']+=not a
                    counts['short_raw_zeros']+=s==zero
                    z=mul(w(x),s)
                    vec=add(vec,scale(z,a0))
                    short=add(short,scale(z,a1))
                assert vec==short
                counts['short_integrand_buckets']+=1
                counts['short_nonzero_integrand_buckets']+=vec!=zero
                if t>U and vec!=zero:
                    assert selector(Q(f)*t,Y,U)==0
                    counts['wrong_product_selector_negative_controls']+=1
                Q_t+=mu(d)*selector(f,Y,U)*sq(vec)
        return Q_t
    tgrid=[Q(U),Q(2*U+1,2),Q(3*U,2),Q(2*U)]
    qvalues=[q_t(t) for t in tgrid]
    ks=sum(q_t(Q(n)) for n,p,w0 in P if U<n<Q(2*D,Y))
    assert ks!=0
    records.append({'D':D,'U':U,'H':H,'pivots':[A1,A2],'Y':Y,
                    'actual_rows':len(rows),'good_squarefree_annular_columns':len(ann),
                    'selected_divisors':len(fs),'actual_K0_nonzero':bool(k0),
                    'annular_raw_zeros':rawzeros,'annular_live_buckets':live_buckets,
                    'short_nonzero_grid_values':sum(bool(v) for v in qvalues),
                    'actual_KS_nonzero':bool(ks)})

# Algebra for the shortened pivot powers, including order flips and subunit
# input scales. Compare third monomials after cubing to remain exact.
for A1,A2,q1,q2 in product((1,2,4,7,8,13,16,23,32),repeat=4):
    a,b=Q(A1,q1),Q(A2,q2)
    if min(a,b)<=Q(1,2):
        continue
    assert a*b==Q(A1*A2,q1*q2)
    assert min(a,b)<=min(A1,A2)
    exact_cubed=min(a*a*b**3,a**3*b*b)
    oriented=a*a*b**3 if A1>=A2 else a**3*b*b
    assert exact_cubed<=oriented
    aa,bb=max(1,a),max(1,b)
    assert aa<=2*a and bb<=2*b
    assert min(aa*aa*bb**3,aa**3*bb*bb)<=32*oriented
    counts['exact_shortened_scale_checks']+=1
    counts['shortened_order_flips']+=(A1>A2 and a<b) or (A2>A1 and b<a)
    counts['nonempty_subunit_row_scales']+=min(a,b)<1

def powers(y,a,b,sigma,k):
    delta=(1-sigma)*y/k
    return (a+b-delta,1-y+min(a,b),a+b-max(a,b)/3+2*(1-y)/3-delta,
            a+b+Q(1,2)-y)
a,b,y=Q(5,12),Q(1,6),Q(199,400)
p=powers(y,a,b,Q(7,8),2)
assert p==(Q(10603,19200),Q(803,1200),Q(8621,11520),Q(703,1200))
assert max(powers(Q(52,105),a,b,Q(7,8),2))==Q(3,4)
assert max(powers(Q(13,24),a,b,Q(1),2))==Q(3,4)
assert max(powers(Q(104,201),a,b,Q(7,8),4))==Q(3,4)
assert powers(Q(1,2),Q(3,4),Q(0),Q(7,8),2)[2]==Q(77,96)
assert Q(23,24)-Q(19,48)*Q(1,2)==Q(73,96)
for da,db in product(range(-5,6),repeat=2):
    assert max(powers(y,a+Q(da,10000),b+Q(db,10000),Q(7,8),2))<Q(3,4)
    counts['exact_mixed_neighborhood_points']+=1
assert all(counts[k]>0 for k in ['annular_factor_paths','actual_frozen_row_raw_transfers',
    'frozen_row_raw_zeros','short_unit_residual_paths','short_raw_zeros',
    'wrong_product_selector_negative_controls','shortened_order_flips',
    'nonempty_subunit_row_scales'])
out=Path('outputs/checks/2026-11-08-coherent-mixed-band/controls-v1.json')
receipt={'schema':'coherent-mixed-band-controls-v1','passed':True,
    'scope':'Exact finite literal ideal/row, common band, rational integrand and scale controls. Nodal rational profiles only; no asymptotic fit or zero-free theorem check.',
    'cases':records,**dict(counts),'conditional_powers_at_199_over_400':[str(x) for x in p],
    'conditional_margin':'19/11520'}
with out.open('x') as f:
    json.dump(receipt,f,indent=2)
    f.write('\n')
print(json.dumps(receipt))
