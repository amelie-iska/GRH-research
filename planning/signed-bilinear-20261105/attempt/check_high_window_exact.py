#!/usr/bin/env python3
"""Exact diagnostics for the new high-window reduction; no analytic proof."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse, json

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from check_mobius_split import universe
from check_reciprocity_period import emul, norm, power, prime_symbol, symbol

PH = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO = (F(0), F(0))
ONE = (F(1), F(0))

def add(x,y): return x[0]+y[0], x[1]+y[1]
def sub(x,y): return x[0]-y[0], x[1]-y[1]
def scale(c,x): return c*x[0], c*x[1]
def conj(x): return x[0]-x[1], -x[1]
def phase(e): return ZERO if e is None else tuple(map(F,PH[e%6]))
def total(xs):
    z=ZERO
    for x in xs: z=add(z,x)
    return z
def subsets(m):
    s=m
    while True:
        yield s
        if not s: break
        s=(s-1)&m
def mu(m): return (-1)**m.bit_count()

def main(out):
    if out.exists(): raise FileExistsError("Do not overwrite existing research output")
    _,_,_,ps=universe(128)
    ps=[p for p in ps if norm(p) in (7,13,19,25)]
    assert len(ps)==7
    fs=[[(p,1) for i,p in enumerate(ps) if m>>i&1] for m in range(128)]
    ns=[]
    for ff in fs:
        n=1
        for p,_ in ff:n*=norm(p)
        ns.append(n)
    triples={m:[(a,b,m^a^b) for a in subsets(m) for b in subsets(m^a)]
             for m in range(128)}
    cutoffs=[F(v) for v in (1,3,7,10,13,16,19,20,25,31,32,50,64,100,200,500,1000,5000)]
    cutoffs += [F(13,2),F(31,2),F(127,2)]
    tables={}
    coefficient_cases=high_cases=nonzero_long=parity_cases=endpoint_cases=0
    for U in cutoffs:
        aa=[];cc=[];rr=[]
        for m in range(128):
            a=sum(mu(x)*mu(y) for x,y,z in triples[m] if ns[x]<=U and ns[y]<=U)
            c=sum(mu(x)*mu(y) for x,y,z in triples[m] if ns[x]>U and ns[y]>U)
            r=sum(ns[x]>U and ns[y]>U for x in subsets(m) for y in [m^x])
            assert a==mu(m)-2*mu(m)*(ns[m]>U)+c
            coefficient_cases+=1
            for D in (F(ns[m],2),F(2*ns[m],3),F(ns[m])):
                if D>1 and U*U<=D and 7*U*U>=2*D:
                    assert D<=ns[m]<=2*D
                    assert all(z==0 for x,y,z in triples[m] if ns[x]>U and ns[y]>U)
                    assert c==mu(m)*r and a==mu(m)*(r-1)
                    assert r%2==0 and abs(a)>=1 and a%2
                    high_cases+=1;parity_cases+=1;nonzero_long+=bool(r)
            # Boundary 7 U^2=2D is explicit, rather than a floating-point approximation.
            D=F(7,2)*U*U
            if D>1 and D<=ns[m]<=2*D:
                assert all(z==0 for x,y,z in triples[m] if ns[x]>U and ns[y]>U)
                assert c==mu(m)*r and a==mu(m)*(r-1)
                endpoint_cases+=1
            aa.append(a);cc.append(c);rr.append(r)
        tables[U]=(aa,cc,rr)
    assert high_cases and endpoint_cases and nonzero_long
    # Strict Na,Nb>U controls: norms equal to U are not long.
    strict_cases=0
    for i,p in enumerate(ps):
        U=F(norm(p))
        assert not ns[1<<i]>U
        strict_cases+=1
    # Below the high window, a nonunit residual c really can occur.
    ids=[next(i for i,p in enumerate(ps) if norm(p)==q) for q in (7,13,19)]
    m=sum(1<<i for i in ids);U=F(10);D=F(1000)
    assert ns[m]==1729 and D<=ns[m]<=2*D and 7*U*U<2*D
    aa,cc,rr=tables[U]
    assert any(z and ns[x]>U and ns[y]>U for x,y,z in triples[m])
    assert cc[m]!=mu(m)*rr[m] and aa[m]!=mu(m)*(rr[m]-1)

    # Literal rows have squarefree coprime first/second factors with norms in [7,14).
    base=[p for p in ps if norm(p) in (7,13)]
    rows=[]
    for i,j in product(range(len(base)),repeat=2):
        if i==j:continue
        z=emul(base[i],power(base[j],2))
        for unit in PH:rows.append(emul(unit,z))
    assert len(rows)==len(set(rows))==72
    raw=[[phase(symbol(ff,u)) for ff in fs] for u in rows]
    product_cases=shared_zero_cases=0
    for ri,u in enumerate(rows):
        for a in range(128):
            for b in subsets(127^a):
                assert emul(raw[ri][a],raw[ri][b])==raw[ri][a|b]
                product_cases+=1
                if raw[ri][a|b]==ZERO:shared_zero_cases+=1
    # Common finite complex rational profiles check equality, never analytic size.
    parameters=((64,7),(512,16),(1000,20),(1024,32),(6000,64))
    row_identities=covariance_cases=complex_profile_cases=high_active_pairs=0
    for D,Ui in parameters:
        U=F(Ui)
        assert U*U<=D and 7*U*U>=2*D
        aa,cc,rr=tables[U]
        cols=[m for m in range(1,128) if D<=ns[m]<=2*D]
        assert cols
        weights={}
        for m in cols:
            t=F(ns[m]-D,D);q=t*t*(1-t)*(1-t)
            weights[m]=(q,q*t)
        for fixed_numerator in ((1,0),(2,0)):
            nu={m:phase(symbol(fs[m],fixed_numerator)) for m in range(128)}
            for ri,u in enumerate(rows):
                def term(m,c):return scale(c,emul(emul(weights[m],nu[m]),raw[ri][m]))
                direct=total(term(m,aa[m]) for m in cols)
                mob=total(term(m,mu(m)) for m in cols)
                long=total(term(m,cc[m]) for m in cols)
                bil=ZERO
                for m in cols:
                    for a in subsets(m):
                        b=m^a
                        if not(ns[a]>U and ns[b]>U):continue
                        assert a&b==0 and ns[a]*ns[b]==ns[m]
                        assert D<=ns[a]*ns[b]<=2*D
                        assert U<ns[a]<F(2*D,1)/U
                        assert U<ns[b]<F(2*D,1)/U
                        val=emul(emul(nu[a],nu[b]),emul(raw[ri][a],raw[ri][b]))
                        bil=add(bil,scale(mu(a)*mu(b),emul(weights[m],val)))
                        high_active_pairs+=1
                assert bil==long and direct==sub(long,mob)
                assert norm(direct)==norm(long)+norm(mob)-2*(emul(long,conj(mob))[0]-emul(long,conj(mob))[1]/2)
                row_identities+=1;covariance_cases+=1
                complex_profile_cases+=any(w[1] for w in weights.values())
    assert high_active_pairs and complex_profile_cases

    # Exact cyclic Fourier arrays refute a generic marginal-product inference.
    fourier=[]
    for n in (2,3,6):
        A=n*n
        vv=[]
        for r,s in product(range(n),repeat=2):
            gram=total(phase((6//n)*k*(r-s)) for k,l in product(range(n),repeat=2))
            assert gram==(scale(A,ONE) if r==s else ZERO)
            vv.append(gram)
        actual=sum(norm(emul(z,z)) for z in vv)
        claimed=A**4
        assert actual==n*A**4 and actual>claimed
        fourier.append(dict(rows=n,columns=A,marginal_operator_norm_squared=A,
                            actual_unnormalized=str(actual),unsupported_product_bound=claimed,
                            ratio=n,normalized_energy_exponent="DX"))

    # Exact rational exponent arithmetic; it is not an infinite moment check.
    old=[F(1,2),F(5,4),F(13,12)]
    fact=[F(1),F(5,4),F(5,4)]
    exponent_cases=0
    for j in range(61):
        t=F(j,120)
        v=[t+F(1,2),F(5,4),F(13,12)+t/3]
        assert max(v)==F(5,4)
        exponent_cases+=1
    for sigma in (F(1,120),F(1,24),F(1,12)):
        target=[F(1,2),F(5,4)-sigma,F(13,12)]
        assert max(target)==F(5,4)-sigma<max(old)
        exponent_cases+=1

    result=dict(status="PASS: exact algebra diagnostics; BT_sigma remains OPEN",
        seed=None,arithmetic="stdlib integer/Fraction Eisenstein arithmetic",
        coefficient_cases=coefficient_cases,high_window_cases=high_cases,
        strict_cutoff_controls=strict_cases,equality_window_cases=endpoint_cases,
        nonzero_long_cases=nonzero_long,parity_and_nonvanishing_cases=parity_cases,
        outside_window_negative_controls=1,literal_balanced_rows=len(rows),
        raw_disjoint_multiplicativity_cases=product_cases,shared_zero_cases=shared_zero_cases,
        bilinear_row_identities=row_identities,complex_covariance_cases=covariance_cases,
        common_complex_profile_cases=complex_profile_cases,active_bilinear_pair_evaluations=high_active_pairs,
        fourier_counterexamples=fourier,exponent_cases=exponent_cases,
        old_exponents=list(map(str,old)),factor_cauchy_exponents=list(map(str,fact)),
        profile_scope="finite common rational complex annular array, not an analytic smooth-weight bound",
        coefficient_norm_lower_proof="elementary lattice/Mobius argument in derivation, not a numerical test",
        analytic_saving_proved=False,arithmetic_energy_lower_bound=False,
        new_Lean_result=False,GRH_claim=False)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("x") as f:json.dump(result,f,indent=2);f.write("\n")
    print(json.dumps({k:result[k] for k in ("status","high_window_cases","equality_window_cases","bilinear_row_identities","exponent_cases")}))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();main(args.output)
