"""Exact Eisenstein reciprocity diagnostics; no floating-point or GRH input."""
from itertools import product
from functools import lru_cache
from math import isqrt
from pathlib import Path
import json
from check_finite_correlation import ResidueField, emul

OUT = Path(__file__).resolve().parents[1] / 'outputs/checks/2026-11-03-reciprocity-period'
I = ((1,0),(0,1),(-1,0),(0,-1))

def mulmod(x,y,n):
    return tuple(t % n for t in emul(x,y))

def power(x,n):
    out=(1,0)
    while n:
        if n%2:out=emul(out,x)
        x=emul(x,x);n//=2
    return out

def gamma(x):
    a,b=x
    terms=(I[0],I[-b%4],I[a%4],I[(b-a)%4])
    out=tuple(sum(t[j] for t in terms) for j in (0,1))
    assert all(v%2==0 for v in out)
    return tuple(v//2 for v in out)

def cmul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c

def rphase(x,y):
    a,b=gamma(x),gamma(y)
    den=cmul(a,b)
    quotient=cmul(gamma(emul(x,y)),(den[0],-den[1]))
    assert quotient in ((1,0),(-1,0))
    return quotient[0]

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def norm(x):
    a,b=x;return a*a-a*b+b*b

@lru_cache(maxsize=None)
def prime_field(pi):
    q=norm(pi)
    if pi[1]==0:
        return ResidueField(abs(pi[0]))
    assert prime(q)
    return ResidueField(q, -pi[0]*pow(pi[1],-1,q)%q)

def prime_symbol(pi,x):
    f=prime_field(pi);a,b=x
    residue=(a+b*f.omega)%f.p if f.omega is not None else a%f.p+f.p*(b%f.p)
    return f.phase[residue]

def symbol(factors,x):
    out=0
    for pi,e in factors:
        value=prime_symbol(pi,x)
        if value is None:return None
        out=(out+e*value)%6
    return out

def pairprod(factors):
    out=(1,0)
    for pi,e in factors:out=emul(out,power(pi,e))
    return out

def run():
    units=[x for x in product(range(4),repeat=2) if x[0]%2 or x[1]%2]
    assert len(units)==12
    squares={mulmod(x,x,4) for x in units}
    assert squares=={(1,0),(0,1),(3,3)}
    tables=0
    for x,y,z in product(units,repeat=3):
        assert rphase(emul(x,y),z)==rphase(x,z)*rphase(y,z)
        assert rphase(x,emul(y,z))==rphase(x,y)*rphase(x,z)
        assert rphase(x,y)==rphase(y,x)
        assert rphase(emul(x,y),emul(x,y))==rphase(x,x)*rphase(y,y)
        tables+=1
    assert [gamma(x) for x in ((1,0),(-1,0),(1,2),(-1,-2))]==[(1,0),(1,0),(0,1),(0,-1)]
    # Actual primary primes, split and inert, with the source embedding convention.
    primes=[(1,3),(-2,-3),(4,3),(1,-3),(-2,3),(1,6),(1,-6),(-5,0),(-11,0)]
    assert all(a%3==1 and b%3==0 for a,b in primes)
    denominators=[[(pi,e)] for pi in primes for e in (1,2,6,7)]
    denominators += [[(p,1),(q,2)] for p,q in zip(primes,primes[1:])]
    recip=0;zeros=0
    for fa,fb in product(denominators,repeat=2):
        a,b=pairprod(fa),pairprod(fb)
        ab,ba=symbol(fb,a),symbol(fa,b)
        if ab is None or ba is None:
            assert ab is None and ba is None
            zeros+=1
        else:
            assert (ab-ba)%6==(0 if rphase(a,b)==1 else 3)
        recip+=1
    # Same modulo12, but actual sextic symbols differ: modulus12 does NOT suffice.
    p31,p43=(1,6),(1,-6);lam=(1,2)
    assert tuple(t%12 for t in p31)==tuple(t%12 for t in p43)
    assert prime_symbol(p31,lam)==1 and prime_symbol(p43,lam)==5
    # Full row conversion with units, fixed S-primes2,3 and good powers.
    eu=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
    conversions=0
    for u,e2,e3,eg in product(eu,(0,1,5,6,7),(0,1,5,6,7),(1,2,6,7)):
        sg=emul(u,emul(power((-2,0),e2),power(lam,e3)))
        sg_reduced=emul(u,emul(power((-2,0),e2%6),power(lam,e3%6)))
        moving=(1,3);kg=power(moving,eg);k=emul(sg,kg)
        for fm in denominators:
            m=pairprod(fm);lhs=symbol(fm,k);kap=symbol(fm,sg_reduced)
            assert kap==symbol(fm,sg)  # S-powers reduce mod6 only on S-units.
            local=prime_symbol(moving,m)
            if local is None:
                assert lhs is None
            else:
                rhs=(kap+(0 if rphase(kg,m)==1 else 3)+eg*local)%6
                assert lhs==rhs
            conversions+=1
    report={'unit_ring_table_cases':tables,'actual_sextic_reciprocity_cases':recip,
            'shared_zero_cases':zeros,'actual_row_conversion_cases':conversions,
            'modulus12_counterexample':{'denominators':[[1,6],[1,-6]],'norms':[31,43],
                'numerator':[1,2],'sextic_exponents':[1,5]},
            'scope':'exact finite diagnostics, not a formal CFT/conductor theorem or a global GRH proof',
            'parameters':'O/(4) all12units; nine primary split/inert primes; exponents1,2,6,7; six units; deterministic, no randomness'}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':run()
