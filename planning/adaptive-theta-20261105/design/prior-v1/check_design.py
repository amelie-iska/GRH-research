"""Exact parameter-design controls; standard library only, no special functions."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
FAMILIES = {3: (1, (0, 1, -1)), 4: (1, (0, 1, 0, -1)), 5: (0, (0, 1, -1, -1, 1))}


def validate(q, eta):
    if type(q) is not int or q not in FAMILIES:
        raise ValueError('Fixed integer q3/q4/q5 required')
    if not isinstance(eta, F):
        raise TypeError('Exact Fraction eta required')
    if eta <= 0:
        raise ValueError('Positive eta required')


def E(x):
    if not isinstance(x, F):
        raise TypeError('Exact Fraction exponent required')
    if x < 0:
        raise ValueError('Nonnegative exponent required')
    return F(1, 1 << (x.numerator // x.denominator))


def Q(x):
    return 1/x + 2/x**2 + 2/x**3


def panels(J):
    for j in range(J):
        h = F(1 << j, 8)
        for ell in range(4):
            yield F(1 << j) * (1 + F(2*ell + 1, 8)), h


def n_tail(q, N):
    a, _ = FAMILIES[q]
    delta, n0 = F(3, q), N + 1
    C = F(1) if a == 0 else (1 + 1/delta)/2
    return 2*C*Q(delta*n0*n0)*E(delta*n0*n0/2)/(1 - E(delta*n0))


def time_tail(q, N, J):
    a, _ = FAMILIES[q]
    delta, T = F(3, q), 1 << J
    return sum((2*n**a*T**3*E(delta*n*n*T)*Q(delta*n*n*T) for n in range(1, N+1)), F())


def quadrature_terms(q, N, J):
    a, _ = FAMILIES[q]
    delta = F(3, q)
    result = []
    for m, h in panels(J):
        rho = m/2
        v = h/rho
        B = max((m+rho)**2, (m-rho)**(-2), F(1))
        for n in range(1, N+1):
            result.append((2*n**a * 2*h * 3*B * E(delta*n*n*m/2), v))
    return result


def quadrature(terms, K):
    return sum((c*v**(2*K+2)/(F(2*K+3)*(1-v*v)) for c, v in terms), F())


def select(q, eta):
    validate(q, eta)
    N = 1
    while n_tail(q, N) > eta/8:
        N += 1
    J = 1
    while time_tail(q, N, J) > eta/8:
        J += 1
    terms = quadrature_terms(q, N, J)
    K = 0
    while quadrature(terms, K) > eta/8:
        K += 1
    P = 4*J*N
    a, chi = FAMILIES[q]
    delta = F(3, q)
    discard = F()
    active = skipped = zero = 0
    for m, h in panels(J):
        for n in range(1, N+1):
            if chi[n % q] == 0:
                zero += 1
                continue
            bound = 4*h*n**a*(m+h)**2*E(delta*n*n*(m-h))
            if bound <= eta/(8*P):
                discard += bound
                skipped += 1
            else:
                active += 1
    budgets = {'n_tail': n_tail(q, N), 'time_tail': time_tail(q, N, J),
               'quadrature': quadrature(terms, K), 'discard': discard}
    assert all(F() <= x <= eta/8 for x in budgets.values())
    assert active + skipped + zero == P
    assert sum(budgets.values(), F()) + eta/2 <= eta
    assert N == 1 or n_tail(q, N-1) > eta/8
    assert J == 1 or time_tail(q, N, J-1) > eta/8
    assert K == 0 or quadrature(terms, K-1) > eta/8
    return {'q': q, 'eta': eta, 'N': N, 'n0': N+1, 'J': J, 'T': 1 << J,
            'K': K, 'potential_pairs': P, 'active_pairs': active,
            'discarded_pairs': skipped, 'zero_character_pairs': zero,
            'discard_threshold': eta/(8*P), 'budgets': budgets,
            'analytic_total': sum(budgets.values(), F()),
            'interval_radius_acceptance': eta/2,
            'max_certified_total_after_interval_acceptance': sum(budgets.values(), F()) + eta/2}


def encode(v):
    if isinstance(v, F):
        return {'numerator': str(v.numerator), 'denominator': str(v.denominator), 'display': float(v)}
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [encode(x) for x in v]
    return v


def run(output):
    if output.exists():
        raise FileExistsError('Preserve previous check output')
    records = [select(q, F(1, 10**e)) for e in (24, 32) for q in FAMILIES]
    expected = [(12,7,19,71), (14,8,20,65), (16,8,20,111),
                (14,7,25,84), (16,8,26,72), (18,8,26,129)]
    assert [(r['N'],r['J'],r['K'],r['active_pairs']) for r in records] == expected
    # Exact exponential-bound structural controls, including jumps and q5 denominator.
    controls = 0
    for x in (F(), F(1,10), F(999,1000), F(1), F(1001,1000), F(123,2), F(10000)):
        floor = x.numerator // x.denominator
        assert E(x) == F(1,2**floor)
        assert F(1,2**(floor+1)) < E(x) <= 2*F(1,2**floor)
        controls += 1
    for q in FAMILIES:
        assert 1 - E(F(3,q)*2) > 0
        assert E(F(3,q)/2) > 0
        controls += 2
    for J in range(1,10):
        ps = list(panels(J))
        assert len(ps) == 4*J
        assert ps[0][0] - ps[0][1] == 1
        assert ps[-1][0] + ps[-1][1] == 1 << J
        assert all(m-h > 0 and h/(m/2) <= F(2,9) for m,h in ps)
        assert all(m+h == n-k for (m,h),(n,k) in zip(ps,ps[1:]))
        controls += 5
    for badq, badeta in [(True,F(1)), (3.0,F(1)), (2,F(1)), (3,0.1), (3,F()), (3,F(-1))]:
        try:
            validate(badq,badeta)
        except (TypeError,ValueError):
            controls += 1
        else:
            raise AssertionError('Invalid input accepted')
    for bad in [0.1, -F(1), True]:
        try:
            E(bad)
        except (TypeError,ValueError):
            controls += 1
        else:
            raise AssertionError('Invalid E input accepted')
    names = ['examples/analytic_oracle/theta_oracle.py','examples/analytic_oracle/dyadic.py',
             'examples/analytic_oracle/adaptive_readout.py',
             'outputs/experiments/2026-11-04-validated-oracle-final-v5/oracle-certificates.json',
             'papers/validated-oracle-core.tex','papers/validated-oracle-details.tex',
             'papers/adaptive-readout-core.tex','papers/adaptive-readout-details.tex',
             'planning/adaptive-readout-20261105/design/DESIGN.md',
             'planning/adaptive-readout-20261105/review/README.md',
             'planning/MASTER_IMPLEMENTATION_PLAN.md','planning/CONTINUATION.md',
             'planning/weighted-moment-20261105/frontier/HANDOFF.md']
    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}
    assert hashes[names[0]] == 'c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1'
    assert hashes[names[1]] == '82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170'
    assert hashes[names[3]] == '85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8'
    hashes[str(Path(__file__).relative_to(ROOT))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    record = {'scope':'Exact finite parameter design; not an executed theta sample or interval implementation acceptance',
              'records':records, 'structural_controls':controls, 'source_sha256':hashes,
              'special_functions_used':False,'random_seed':None,'new_Lean_declarations':0,'GRH_proved':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)  # Exact denominators can exceed Python3.11 default serialization limit.
    output.write_text(json.dumps(encode(record),indent=2)+'\n')
    print(json.dumps({'records':len(records),'structural_controls':controls,
                      'parameters':[(r['q'],str(r['eta']),r['N'],r['J'],r['K'],r['active_pairs']) for r in records]}))

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    a = p.parse_args()
    run(a.output)
