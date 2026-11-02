#!/usr/bin/env python3
"""Exact rational Rouché-certificate inequalities for S_5(s, chi mod 3).
No floating point enters the certificate. The analytic Rouché inference is in prose.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
CENTER = (Q(337261, 10**6), Q(11027504, 10**6))
RADIUS = Q(1, 10000)
TERMS = 120
LOG_TERMS = 60

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def scale(a,x): return (a*x[0],a*x[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def l1(x): return abs(x[0])+abs(x[1])
def exp_taylor(w):
    total, term = ONE, ONE
    for k in range(1, TERMS+1):
        term = scale(Q(1,k),mul(term,w))
        total = add(total,term)
    return total

def certify_log(n,ell,delta):
    y=Q(n-1,n+1)
    lower=2*sum((y**(2*k+1)/Q(2*k+1) for k in range(LOG_TERMS)),Q(0))
    tail=2*y**(2*LOG_TERMS+1)/(Q(2*LOG_TERMS+1)*(1-y*y))
    assert ell-delta <= lower
    assert lower+tail <= ell+delta
    return lower,lower+tail

def run():
    # These rational approximations are verified against an exact logarithm series below.
    data=[(2,-1,Q(6931471805599453,10**16),Q(1,10**15)),
          (4, 1,Q(13862943611198906,10**16),Q(2,10**15)),
          (5,-1,Q(16094379124341004,10**16),Q(1,10**15))]
    C=l1(CENTER)
    taylor_error=Q(3**24 * 24**(TERMS+1),factorial(TERMS+1))
    assert taylor_error < Q(1,10**18)
    fapprox, dapprox=ONE,ZERO
    ferr, derr=Q(0),Q(0)
    for n,a,ell,delta in data:
        lo,hi=certify_log(n,ell,delta)
        assert 0 < ell and 0 < lo and hi < (1 if n==2 else 2)
        assert CENTER[0]>0 and C*delta <= Q(1,2)
        w=scale(-ell,CENTER)
        assert l1(w)<=24
        eapprox=exp_taylor(w)
        # exp(-c log n) differs from exp(-c ell) by at most2Cdelta;
        # the latter differs from its Taylor sum by at mosttaylor_error.
        error=taylor_error+2*C*delta
        fapprox=add(fapprox,scale(Q(a),eapprox))
        dapprox=add(dapprox,scale(-Q(a)*ell,eapprox))
        ferr+=error
        # |exp(-c log n)|<=1 because Re(c)>0 and log n>0.
        derr+=delta+ell*error
    center_upper=l1(fapprox)+ferr
    derivative_lower=abs(dapprox[0])-derr
    assert center_upper < Q(1,10**6)
    assert derivative_lower > 1
    assert CENTER[0]-RADIUS>0
    assert CENTER[0]+RADIUS<Q(1,2)
    # |f''(s)|<=log(2)^2+log(4)^2+log(5)^2<1+4+4=9 on the disk.
    rouche_gap=RADIUS-Q(1,10**6)-Q(9,2)*RADIUS**2
    assert rouche_gap>0
    report={
        "function":"1 - exp(-s log 2) + exp(-s log 4) - exp(-s log 5)",
        "interpretation":"S_5(s, chi), primitive nonprincipal character modulo3",
        "center_real":str(CENTER[0]),"center_imag":str(CENTER[1]),
        "radius":str(RADIUS),"log_series_terms":LOG_TERMS,
        "exponential_taylor_degree":TERMS,
        "exp_taylor_error_less_than":"1/1000000000000000000",
        "function_center_norm_less_than":"1/1000000",
        "derivative_center_norm_greater_than":"1",
        "second_derivative_disk_norm_at_most":"9",
        "rouche_margin_strictly_greater_than":str(rouche_gap),
        "disk_real_part_lower":str(CENTER[0]-RADIUS),
        "disk_real_part_upper":str(CENTER[0]+RADIUS),
        "certificate_arithmetic":"exact fractions only; no floating point or randomness",
        "conclusion_in_prose":"Exactly one zero in the disk, counted with multiplicity; the disk lies strictly left of Re(s)=1/2 inside the critical strip.",
        "scope":"Certifies rational inequalities; analytic exponential/logarithm error estimates and Rouche inference are proved in the paper, not formalized in Lean. This is a finite approximant zero, not a zero of the full L-function or a refutation of GRH."
    }
    out=Path(__file__).resolve().parents[1]/"outputs/checks/2026-11-02-arithmetic-zero/certificate.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":run()
