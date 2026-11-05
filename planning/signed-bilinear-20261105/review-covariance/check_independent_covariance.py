#!/usr/bin/env python3
"""Independent exact signed-covariance review: stdlib only, no author imports."""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
ONE=(1,0)
ZERO=(0,0)

def mul(x,y):
    # Polynomial multiplication, followed by omega^2=-1-omega.
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c-b*d

def conj(x):
    a,b=x
    return a-b,-b

def norm(x):
    z=mul(x,conj(x))
    assert z[1]==0
    return z[0]

def add(x,y):
    return x[0]+y[0],x[1]+y[1]

def scale(n,x):
    return n*x[0],n*x[1]

def power(x,n):
    r=ONE
    for _ in range(n):
        r=mul(r,x)
    return r

UNITS=tuple(power((1,1),j) for j in range(6))
assert len(set(UNITS))==6 and power((1,1),6)==ONE

def divexact(x,y):
    den=norm(y)
    a,b=mul(x,conj(y))
    return (a//den,b//den) if a%den==b%den==0 else None

def real(x):
    return F(2*x[0]-x[1],2)

def total(xs):
    r=ZERO
    for x in xs:
        r=add(r,x)
    return r

def ip(x,y):
    return mul(x,conj(y))

def isprime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def elements(bound):
    B=2*isqrt(bound)+2
    return sorted(((a,b) for a in range(-B,B+1) for b in range(-B,B+1)
                   if 0<norm((a,b))<=bound),key=lambda g:(norm(g),g))

def ideals(bound):
    # Unique generator congruent to 1 mod 3 for ideals prime to 3.
    return [g for g in elements(bound)
            if g[0]%3==1 and g[1]%3==0 and norm(g)%2 and norm(g)%3]

def primes(bound):
    return [g for g in ideals(bound) if isprime(norm(g))
            or (g[1]==0 and isprime(abs(g[0])) and abs(g[0])%3==2)]

def factor(g,ps):
    r=g; fs=[]
    for p in ps:
        e=0
        while (q:=divexact(r,p)) is not None:
            r=q;e+=1
        if e:
            fs.append((p,e))
    assert norm(r)==1,(g,r)
    return fs

def mu(fs):
    return 0 if any(e>1 for p,e in fs) else (-1)**len(fs)

def coef(fs,U):
    # Enumerate each prime's three disjoint placements a,b,c directly.
    assert all(e==1 for p,e in fs)
    A=C=ordered=0
    for places in product(range(3),repeat=len(fs)):
        qa=qb=1;sgn=1
        for (p,e),place in zip(fs,places):
            if place==0:qa*=norm(p);sgn=-sgn
            elif place==1:qb*=norm(p);sgn=-sgn
        if qa<=U and qb<=U:A+=sgn
        if qa>U and qb>U:C+=sgn
        if qa>U and qb>U and 2 not in places:ordered+=1
    return dict(A=A,C=C,mu=mu(fs),ordered_long_factors=ordered)

def field_phase(pi,u):
    """Direct residue-field exponent (q-1)/6, matched to actual unit roots."""
    q=norm(pi)
    if pi[1]:
        assert isprime(q)
        w=(-pi[0]*pow(pi[1],-1,q))%q
        assert (w*w+w+1)%q==0
        z=(u[0]+u[1]*w)%q
        if z==0:return None
        root=pow(z,(q-1)//6,q)
        roots=[pow((1+w)%q,j,q) for j in range(6)]
    else:
        p=abs(pi[0])
        assert isprime(p) and p%3==2 and q==p*p
        fm=lambda x,y:tuple(t%p for t in mul(x,y))
        def fp(x,n):
            v=ONE
            while n:
                if n&1:v=fm(v,x)
                x=fm(x,x);n//=2
            return v
        z=(u[0]%p,u[1]%p)
        if z==ZERO:return None
        root=fp(z,(q-1)//6)
        roots=[fp((1,1),j) for j in range(6)]
    assert len(set(roots))==6
    return roots.index(root)

def symbol(fs,u):
    es=[field_phase(p,u) for p,e in fs]
    if None in es:return ZERO
    return UNITS[sum(e*t for (p,e),t in zip(fs,es))%6]

def strip_S(u):
    for p in [(2,0),(1,-1)]:
        while (v:=divexact(u,p)) is not None:
            u=v
    return u

def polynomial(R,v,w):
    return sum(F(v[j])*F(w[k])*R[j][k] for j,k in product(range(4),repeat=2))

def main(out):
    if out.exists():raise FileExistsError("Preserve existing output")
    D=400;U=17;H=89
    assert U*U<=D and 7*U*U>=2*D and H**4<=D**3<(H+1)**4
    # Exact rational support closures; interiors give the nonzero values.
    supports=[(F(4*n-1,4*D),F(4*n+1,4*D)) for n in (439,475)]
    assert 1<supports[0][0]<supports[0][1]<supports[1][0]<supports[1][1]<2
    active_norms=[q for q in range(D,2*D+1)
                  if any(a<F(q,D)<b for a,b in supports)]
    assert active_norms==[439,475]
    gs=ideals(2*D);ps=primes(2*D)
    fs={g:factor(g,ps) for g in gs}
    columns=[g for g in gs if norm(g) in active_norms and mu(fs[g])]
    assert len(columns)==4 and [norm(g) for g in columns]==[439,439,475,475]
    cs=[coef(fs[g],U) for g in columns]
    assert [c["A"] for c in cs]==[1,1,1,1]
    assert [c["C"] for c in cs]==[0,0,2,2]
    assert [c["mu"] for c in cs]==[-1,-1,1,1]
    assert all(c["A"]==c["C"]-c["mu"] and c["C"]==c["mu"]*c["ordered_long_factors"]
               and c["ordered_long_factors"]%2==0 for c in cs)
    assert [conj(g) for g in columns]==[columns[1],columns[0],columns[3],columns[2]]
    # Audit primary ideal uniqueness in this finite universe by unit orbits.
    assert len({frozenset(mul(e,g) for e in UNITS) for g in gs})==len(gs)
    small=[g for g in gs if 7<=norm(g)<14 and mu(fs[g])]
    assert len(small)==4 and all(len(fs[g])==1 and fs[g][0][1]==1 for g in small)
    balanced=[mul(e,mul(a,power(b,2)))
              for a,b in product(small,repeat=2) if a!=b for e in UNITS]
    assert len(balanced)==len(set(balanced))==72 and max(map(norm,balanced))==2197
    short=[u for u in elements(H) if norm(strip_S(u))>1]
    assert len(short)==246
    # Explicit valuation checks establishing the guaranteed NP sets.
    val_counts={}
    for name,rows in [("balanced_B7",balanced),("outside_S_nontrivial_H89",short)]:
        exponents=[]
        for u in rows:
            v=strip_S(u)
            vf=factor(v,ps)
            assert vf and all(e in [1,2] for p,e in vf)
            assert all(norm(p)>=7 for p,e in vf)
            exponents.extend(e for p,e in vf)
        val_counts[name]={str(e):exponents.count(e) for e in [1,2]}
    rpath=ROOT/"outputs/checks/2026-11-05-signed-bilinear/root-covariance-v1/counterexample.json"
    original=json.loads(rpath.read_text())
    assert original["D"]==D and original["U"]==U
    assert [tuple(c["generator"]) for c in original["columns"]]==columns
    assert [{k:c[k] for k in ["A","C","mu","ordered_long_factors"]}
            for c in original["columns"]]==cs
    assert F(original["normalized_coefficient_l2"])==F(202,D)
    reports={}
    for name,rows in [("balanced_B7",balanced),("outside_S_nontrivial_H89",short)]:
        raw=[[symbol(fs[g],u) for g in columns] for u in rows]
        old=original["row_cases"][name]
        oldraw={tuple(r["u"]):[tuple(v) for v in r["characters"]] for r in old["row_data"]}
        assert {u:v for u,v in zip(rows,raw)}==oldraw
        G=[[total(ip(v[j],v[k]) for v in raw) for k in range(4)] for j in range(4)]
        assert G==[[tuple(z) for z in row] for row in old["Gram_Eisenstein"]]
        assert all(G[j][k]==conj(G[k][j]) for j,k in product(range(4),repeat=2))
        R=[[real(z) for z in row] for row in G]
        assert [[str(z) for z in row] for row in R]==old["Gram_real"]
        conjugate_controls=0
        for u in rows:
            for j,g in enumerate(columns):
                assert symbol(fs[conj(g)],conj(u))==conj(symbol(fs[g],u))
                conjugate_controls+=1
        zero_entries=sum(z==ZERO for v in raw for z in v)
        assert zero_entries==old["raw_zero_entries"]
        observations=[]
        for x in [0,1,4,5,7,10]:
            w=[x,x,1,1]
            weights=[[c[key]*wi for c,wi in zip(cs,w)] for key in ["A","C","mu"]]
            energies=[F(0),F(0),F(0)];cov=ZERO
            for v in raw:
                aa,ll,mm=[total(scale(t,z) for t,z in zip(tw,v)) for tw in weights]
                assert aa==add(ll,scale(-1,mm))
                for j,t in enumerate([aa,ll,mm]):energies[j]+=F(norm(t),D)
                cov=add(cov,ip(ll,mm))
            diagonal=sum(F(weights[1][j]*weights[2][j])*R[j][j] for j in range(4))/D
            assert diagonal>=0
            re_cov=real(cov)/D
            assert energies[0]==energies[1]+energies[2]-2*re_cov
            assert [polynomial(R,a,a)/D for a in weights]==energies
            assert polynomial(R,weights[1],weights[2])/D==re_cov
            observation=dict(profile_amplitude=x,energy_A=str(energies[0]),
                             energy_C=str(energies[1]),energy_M=str(energies[2]),
                             real_covariance=str(re_cov),diagonal_covariance=str(diagonal),
                             off_diagonal_covariance=str(re_cov-diagonal))
            observations.append(observation)
        assert observations==old["observations"]
        if name=="balanced_B7":
            assert R==[[72,0,0,18],[0,72,18,0],[0,18,72,0],[18,0,0,72]]
            # Q(C,mu)=(72*4-72*x)/400.
            for o in observations:assert F(o["real_covariance"])==F(18,25)-F(9,50)*o["profile_amplitude"]
            assert observations[-1]["real_covariance"]=="-27/25"
        else:
            assert observations[-1]["real_covariance"]=="-69/50"
        reports[name]=dict(rows=len(rows),max_row_norm=max(map(norm,rows)),
                           zero_entries=zero_entries,phase_values_checked=4*len(rows),
                           conjugation_controls=conjugate_controls,Gram_Eisenstein=G,
                           Gram_real=[[str(z) for z in row] for row in R],
                           observations=observations,local_exponents=val_counts[name])
    source_paths=[Path(__file__),ROOT/"examples/arithmetic_cutoff/signed_covariance.py",rpath]
    report=dict(passed=True,implementation="Independent stdlib ring/factor enumeration and direct F439/F19/F25 exponentiation; imports no author helper.",
                active_norms=active_norms,profile_support_closures=[[str(a),str(b)] for a,b in supports],
                supnorm_at_x10=10,normalized_coefficient_l2=str(F(202,D)),columns=columns,
                rows=reports,source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                                           for p in source_paths},
                scope="Automatic nonnegative signed covariance fails for the actual smooth original-family finite case. No BT_sigma refutation, asymptotic energy conclusion, new analytic saving, Lean result or GRH claim.")
    out.mkdir(parents=True)
    (out/"independent-covariance.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True)
    main(p.parse_args().output)
