#!/usr/bin/env python3
"""Exact diagnostics for the arithmetic Abel boundary construction.
Infinite Hilbert/Fredholm and holomorphy claims are prose, not finite certificates.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def chi3(n):
    return (0, 1, -1)[n % 3]


def chi4(n):
    return (0, 1, 0, -1)[n % 4]


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    out = Q(1)
    for j in range(len(a)):
        p = next((i for i in range(j, len(a)) if a[i][j]), None)
        if p is None:
            return Q(0)
        if p != j:
            a[p], a[j] = a[j], a[p]
            out = -out
        c = a[j][j]
        out *= c
        for i in range(j+1, len(a)):
            ratio = a[i][j]/c
            for k in range(j+1, len(a)):
                a[i][k] -= ratio*a[j][k]
    return out


def ell(n):
    assert n >= 1
    return n.bit_length()


def geometric_tail(r, j):
    assert 0 <= r < 1
    return r**j*(Q((j+1)**2, 1)/(1-r) + 2*(j+1)*r/(1-r)**2 +
                 r*(1+r)/(1-r)**3)


def run():
    counts = {'arithmetic_matrix_determinants': 0, 'finite_abel_identities': 0,
              'dyadic_kernel_tail_bounds': 0, 'dyadic_u_tail_bounds': 0,
              'geometric_tail_decompositions': 0}
    samples = []
    for modulus, chi in [(3, chi3), (4, chi4)]:
        cumul = [0]
        for n in range(1, 1025):
            cumul.append(cumul[-1]+chi(n))
        assert max(map(abs, cumul)) == 1
        assert all(cumul[n] == 0 for n in range(modulus, 1025, modulus))
        for exponent in [1, 2, 3]:
            for n in range(1, 19):
                delta = [Q(1, k**exponent)-Q(1, (k+1)**exponent) for k in range(1, n+1)]
                endpoint = cumul[n]*Q(1, (n+1)**exponent)
                raw = sum((chi(k)*Q(1, k**exponent) for k in range(1, n+1)), Q(0))
                abel = sum((cumul[k]*delta[k-1] for k in range(1, n+1)), Q(0))
                assert abel == raw-endpoint
                counts['finite_abel_identities'] += 1
                for include_endpoint in [False, True]:
                    v = [d-Q(k == 0)+(endpoint if include_endpoint and k == 0 else 0)
                         for k, d in enumerate(delta)]
                    mat = [[Q(i == j)+cumul[i+1]*v[j] for j in range(n)] for i in range(n)]
                    det = determinant(mat)
                    assert det == (raw if include_endpoint else abel)
                    counts['arithmetic_matrix_determinants'] += 1
                if n in [3, 4, 6, 12, 18]:
                    samples.append({'modulus': modulus, 's': exponent, 'N': n,
                                    'S_N': str(raw), 'T_N': str(abel), 'endpoint': str(endpoint)})
            r = Q(1, 2**(2*exponent))
            for j in range(7):
                start = 2**j
                # Exactly ||v tail||² in the displayed finite ambient block; w_n²=n ell_n².
                square = sum((Q(n*ell(n)**2)*(Q(1,n**exponent)-Q(1,(n+1)**exponent))**2
                              for n in range(start, 1024)), Q(0))
                assert square <= exponent**2*geometric_tail(r, j)
                counts['dyadic_kernel_tail_bounds'] += 1
            for j in range(1, 7):
                u_tail_sq = sum((Q(cumul[n]**2, n*ell(n)**2)
                                 for n in range(2**j, 1024)), Q(0))
                assert u_tail_sq <= Q(1, j)
                counts['dyadic_u_tail_bounds'] += 1
        assert sum((Q(cumul[n]**2, n*ell(n)**2) for n in range(1,1024)),Q(0)) <= 2
    for r in [Q(1,4), Q(1,2), Q(3,4), Q(1,16)]:
        for j in range(9):
            head = sum((Q((k+1)**2)*r**k for k in range(j)),Q(0))
            assert head+geometric_tail(r,j) == (1+r)/(1-r)**3
            assert geometric_tail(r,j)-geometric_tail(r,j+1) == (j+1)**2*r**j
            counts['geometric_tail_decompositions'] += 1
    minor = Q(1,6)*Q(7,144)-Q(5,36)*Q(1,12)
    assert minor == -Q(1,288)
    # Existing certified chi3 fifth partial sum is unchanged at full-period cutoff6.
    coeffs = {n:chi3(n) for n in range(1,7) if chi3(n)}
    assert coeffs == {1:1,2:-1,4:1,5:-1} and sum(chi3(n) for n in range(1,7))==0
    result = {'arithmetic':'exact Fraction and integer arithmetic; deterministic; no random seed',
              'counts':counts, 'samples':samples, 'normalized_kernel_minor_s1_s2':str(minor),
              'existing_zero_certificate_inherited_at_N6':{'chi_modulus':3,'coefficients':coeffs,
                 'reference':'papers/core.tex theorem finite-offline; not recomputed or a new zero certificate'},
              'scope':'Finite determinants, Abel identities and bounded rational dyadic diagnostics only. Infinite trace norm, holomorphy, Fredholm identity and critical-height metric obstruction are proved in prose; no GRH proof.'}
    path=Path(__file__).resolve().parents[1]/'outputs/checks/2026-11-03-abel-boundary/exact-checks.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'counts':counts,'normalized_minor':str(minor),'output':str(path),'scope':result['scope']},indent=2))


if __name__=='__main__':
    run()
