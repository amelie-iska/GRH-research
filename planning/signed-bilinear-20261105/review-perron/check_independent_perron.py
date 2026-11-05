#!/usr/bin/env python3
"""Independent exact finite controls; does not import the author or project code."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]

class E:
    def __init__(self, a=0, b=0):
        if isinstance(a, E):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)
    def __add__(self, other):
        other = E(other)
        return E(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return E(-self.a, -self.b)
    def __sub__(self, other):
        return self + -E(other)
    def __rsub__(self, other):
        return E(other) + -self
    def __mul__(self, other):
        other = E(other)
        return E(self.a*other.a-self.b*other.b,
                 self.a*other.b+self.b*other.a-self.b*other.b)
    __rmul__ = __mul__
    def norm(self):
        return self.a*self.a-self.a*self.b+self.b*self.b
    def inverse(self):
        n = self.norm()
        assert n
        return E((self.a-self.b)/n, -self.b/n)
    def __truediv__(self, other):
        return self * E(other).inverse()
    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return self.inverse() ** -n
        result, base = E(1), self
        while n:
            if n & 1:
                result = result * base
            n //= 2
            if n:
                base = base * base
        return result
    def __eq__(self, other):
        other = E(other)
        return self.a == other.a and self.b == other.b

def ep(values):
    ans = E(1)
    for value in values:
        ans = ans * value
    return ans

def divides(p, u):
    q = u / p
    return q.a.denominator == q.b.denominator == 1

ROOT6 = E(1, 1)
PHASES = [ROOT6 ** k for k in range(6)]
assert len({(v.a, v.b) for v in PHASES}) == 6 and ROOT6 ** 6 == E(1)

def raw(p, u):
    if divides(p, u):
        return E(0)
    n = int(p.norm())
    v = u ** ((n-1)//6)
    hits = [z for z in PHASES if divides(p, v-z)]
    assert len(hits) == 1
    return hits[0]

def run():
    # Actual conjugate split pairs and the prime above inert 5, independently chosen.
    primes = [E(3, 1), E(2, -1), E(4, 1), E(3, -1), E(5, 0)]
    ns = [int(p.norm()) for p in primes]
    assert ns == [7, 7, 13, 13, 25]
    assert all(not divides(p, q) for i, p in enumerate(primes)
               for j, q in enumerate(primes) if i != j)
    rows = [E(1), E(0, 1), E(2), primes[0], primes[0]**3,
            primes[0]**6, (primes[0]**6)*primes[4],
            primes[0]*(primes[2]**2)]
    masks = range(1 << len(primes))
    norms = [1]*len(masks)
    for m in masks:
        norms[m] = 1
        for j, n in enumerate(ns):
            if m >> j & 1:
                norms[m] *= n
    def subprod(values, m):
        return ep(v for j, v in enumerate(values) if m >> j & 1)
    mu = [(-1)**m.bit_count() for m in masks]
    pairs = [(a,b) for a,b in product(masks, repeat=2) if not a & b]
    counts = dict(local_factorizations=0, finite_G_and_triple_series=0,
        sharp_asymmetric_endpoints=0, raw_mask_terms=0,
        coordinate_slices=0, omitted_R_witnesses=0, overlap_witnesses=0,
        uncorrected_endpoint_witnesses=0, halfinteger_endpoint_comparisons=0,
        all_sixth_power_phases=0, third_power_phase_orders=0)
    # All coefficients are exact elements of Q(omega), all scales rational.
    for u, twist, sig in product(rows, [E(1), E(2)], [2,3]):
        raw_values = [raw(p,u) for p in primes]
        q = [r*raw(p,twist)*Q(1,n**sig)
             for p,n,r in zip(primes,ns,raw_values)]
        t = [v/(1+v) for v in q]
        qm = [subprod(q,m) for m in masks]
        tm = [subprod(t,m) for m in masks]
        F0 = ep(1+v for v in q)
        for m in masks:
            if any(r == E(0) and m >> j & 1 for j,r in enumerate(raw_values)):
                assert qm[m] == E(0) and tm[m] == E(0)
                counts["raw_mask_terms"] += 1
        for z,w in [(-1,-1),(-1,1),(0,0),(0,2),(2,0),(1,2)]:
            alpha, beta = [Q(n)**(-z) for n in ns], [Q(n)**(-w) for n in ns]
            localE = [1+v-v*a-v*b for v,a,b in zip(q,alpha,beta)]
            localR = [1-v*v*(1-a)*(1-b)/((1-v*a)*(1-v*b))
                      for v,a,b in zip(q,alpha,beta)]
            main = [(1-v*a)*(1-v*b)/(1-v)
                    for v,a,b in zip(q,alpha,beta)]
            for j in range(len(primes)):
                assert localE[j] == main[j]*localR[j]
                assert localE[j] == (1+q[j])*(1-t[j]*alpha[j]-t[j]*beta[j])
                counts["local_factorizations"] += 1
            direct = E(0)
            for a,b in pairs:
                csum = ep(1+q[j] for j in range(len(primes)) if not (a|b) >> j & 1)
                direct += mu[a]*mu[b]*qm[a|b]*csum*Q(norms[a])**(-z)*Q(norms[b])**(-w)
            gsum = sum((mu[a]*mu[b]*tm[a|b]*Q(norms[a])**(-z)*Q(norms[b])**(-w)
                        for a,b in pairs), E(0))
            assert direct == ep(localE) == ep(main)*ep(localR) == F0*gsum
            counts["finite_G_and_triple_series"] += 1
            counts["omitted_R_witnesses"] += ep(localE) != ep(main)
            if z == 0 or w == 0:
                shift = w if z == 0 else z
                assert ep(localR) == E(1)
                assert direct == ep(1-v*Q(n)**(-shift) for v,n in zip(q,ns))
                counts["coordinate_slices"] += 1
        for Ua,Ub in product([Q(1),Q(7),Q(15,2),Q(13),Q(25)], repeat=2):
            Va = Q(Ua.numerator//Ua.denominator)+Q(1,2)
            Vb = Q(Ub.numerator//Ub.denominator)+Q(1,2)
            assert all((n <= Ua) == (n < Va) and (n <= Ub) == (n < Vb) for n in norms)
            counts["halfinteger_endpoint_comparisons"] += len(norms)
            incl = sum((mu[a]*mu[b]*tm[a|b] for a,b in pairs
                        if norms[a] <= Ua and norms[b] <= Ub), E(0))
            def h(U,n):
                return Q(1) if n < U else Q(1,2) if n == U else Q(0)
            half = sum((mu[a]*mu[b]*tm[a|b]*h(Ua,norms[a])*h(Ub,norms[b])
                        for a,b in pairs), E(0))
            fixed = sum((mu[a]*mu[b]*tm[a|b]*
                         (h(Ua,norms[a])+Q(1,2)*(norms[a] == Ua))*
                         (h(Ub,norms[b])+Q(1,2)*(norms[b] == Ub))
                         for a,b in pairs), E(0))
            assert incl == fixed
            counts["sharp_asymmetric_endpoints"] += 1
            counts["uncorrected_endpoint_witnesses"] += incl != half
            if Ua == Ub:
                one = sum((mu[a]*tm[a] for a in masks if norms[a] <= Ua), E(0))
                counts["overlap_witnesses"] += incl != one*one
    # Independent raw sixth/cubic powers: deletion survives a primitive conductor drop.
    for p in primes:
        for v in rows:
            if not divides(p,v):
                assert raw(p,v**6) == E(1)
                assert raw(p,v**3)**2 == E(1)
                counts["all_sixth_power_phases"] += 1
                counts["third_power_phase_orders"] += 1
    p = primes[0]
    for e in [3,6]:
        assert raw(p,p**e) == E(0)
    # At p, cubic primitive psi is ramified but psi^2 is unramified principal.
    n = Q(7)
    cubic_primitive_ratio = 1-n**(-2)
    cubic_full_mask_correction = 1/(1-n**(-2))
    sixth_primitive_ratio = (1-n**(-2))/(1-n**(-1))
    sixth_full_mask_correction = (1-n**(-1))/(1-n**(-2))
    assert cubic_primitive_ratio == Q(48,49) != 1
    assert sixth_primitive_ratio == Q(8,7) != 1
    assert cubic_primitive_ratio*cubic_full_mask_correction == 1
    assert sixth_primitive_ratio*sixth_full_mask_correction == 1
    # Equal norms can occur on distinct coprime ideals in both variables.
    assert norms[1] == norms[2] == 7 and not 1 & 2
    assert Q(1,2)**2 == Q(1,4) != 1
    # A local R zero is allowed inside Omega. At Np=7, sigma=2,
    # q=1/49, alpha=48, beta=2: sigma+x,y>0 since 48,2<49,
    # and kappa>1 iff 48*2<7**3. Both denominators are nonzero.
    q, alpha, beta = Q(1,49), Q(48), Q(2)
    assert alpha < 49 and beta < 49 and alpha*beta < 7**3
    assert 1+q-q*alpha-q*beta == 0
    assert 1-q*q*(1-alpha)*(1-beta)/((1-q*alpha)*(1-q*beta)) == 0
    # Exact rational domain points distinguish correction convergence from safe inversion.
    sig,x,y = Q(3,5),-Q(1,25),-Q(1,25)
    assert sig+x>0 and sig+y>0 and 2*sig+x+y>1
    assert not sig+x>1 and not sig+y>1
    for sig in [Q(11,20),Q(3,5),Q(3,4),Q(9,10)]:
        delta = sig-Q(1,2)
        assert 2*(2-2*sig) == 2-4*delta
    for k in ["omitted_R_witnesses","overlap_witnesses","uncorrected_endpoint_witnesses"]:
        assert counts[k] > 0
    files = ["planning/signed-bilinear-20261105/perron/DOUBLE_PERRON.md",
        "planning/signed-bilinear-20261105/perron/check_double_perron_exact.py",
        "planning/signed-bilinear-20261105/perron/HANDOFF.md",
        "planning/signed-bilinear-20261105/perron/manifest-v1.json",
        "outputs/checks/2026-11-05-signed-bilinear/perron/exact-controls-v1.json",
        "papers/masked-moment-core.tex","papers/masked-moment-details.tex",
        "papers/weighted-cutoff-core.tex","papers/weighted-cutoff-details.tex",
        "research/weighted-cutoff-moment.md"]
    files.append(str(Path(__file__).relative_to(ROOT)))
    return dict(passed=True, author_code_imported=False, dependencies="Python standard library only",
        exact_arithmetic="Fractions in Q(omega); independent quotient and residue-symbol evaluation",
        deterministic=True, seed="none; exhaustive finite enumerations",
        prime_ideal_generators=[[str(p.a),str(p.b)] for p in primes], prime_norms=ns,
        rows=len(rows), counts=counts,
        primitive_conductor_drop_controls=dict(cubic_ratio=str(cubic_primitive_ratio),
            cubic_correction=str(cubic_full_mask_correction),
            sixth_ratio=str(sixth_primitive_ratio),sixth_correction=str(sixth_full_mask_correction)),
        scope="Finite algebra/mask/endpoints and exponent bookkeeping only; analytic proof audited in separate prose",
        new_analytic_saving=False, BT_sigma=False, new_Lean=False, GRH=False,
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files})

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    args = ap.parse_args()
    assert not args.output.exists(), "Preserve evidence; choose a fresh report path"
    report=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open("x") as f:
        f.write(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k != "source_sha256"},indent=2))
