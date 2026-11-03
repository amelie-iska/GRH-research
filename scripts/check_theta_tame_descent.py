#!/usr/bin/env python3
"""Exact bounded diagnostics for tame descent of the actual theta column.

Immutable prior checkers supply integer/Eisenstein arithmetic and the literal
special fiber Λ/uΛ. No source cache, network, dependencies or randomness needed.
Uniform formal-series, valuation and categorical claims rest on separate proofs.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
from check_theta_jacobi import ONE, ZERO, OMEGA, emul, epow, eadd, escale
from check_theta_projective_multiplicity import (
    BASIS, endpoint, multiply, zeros, mmul, local_polynomial, ppow, projective_data)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'outputs/checks/2026-11-03-tame-descent/exact-checks.json'
MAX_SERIES_DEGREE = 32


def phase(exponent):
    return epow(OMEGA, exponent % 3)


def column_action(path, side, cut):
    v, length, branch = path
    if length and branch != side:
        return 0
    return int(not any((v-r) % 3 == cut for r in range(length)))


def normalization_representation():
    """Actual left Λ/uΛ action on the hereditary normalization modulo u.

    Each branch's three columns are the three cut modules. This finite module
    is used as the special fiber of a specified infinite-order coefficient kernel.
    """
    states = [(side, cut, vertex) for side in (1, -1) for cut in range(3)
              for vertex in range(3)]
    index = {s: i for i, s in enumerate(states)}
    reps = {}
    for path in BASIS:
        matrix = zeros(18)
        for col, (side, cut, vertex) in enumerate(states):
            if vertex == endpoint(path):
                matrix[index[(side, cut, path[0])]][col] = column_action(path, side, cut)
        reps[path] = matrix
    rotation, swap = zeros(18), zeros(18)
    for col, (side, cut, vertex) in enumerate(states):
        rotation[index[(side, (cut+1) % 3, (vertex+1) % 3)]][col] = 1
        swap[index[(-side, cut, vertex)]][col] = 1
    count = 0
    for a, b in product(BASIS, repeat=2):
        coef, c = multiply(a, b)
        target = [[coef*x for x in row] for row in reps[c]] if coef else zeros(18)
        assert mmul(reps[a], reps[b]) == target
        count += 1
    deck_checks = 0
    for path in BASIS:
        v, length, branch = path
        shifted = ((v+1) % 3, length, branch)
        assert mmul(rotation, reps[path]) == mmul(reps[shifted], rotation)
        # alpha reverses the branch; the minus full cycle is -plus in Λ/uΛ.
        if length == 3:
            image = [[-x for x in row] for row in reps[path]]
        elif length:
            image = reps[(v, length, -branch)]
        else:
            image = reps[path]
        assert mmul(swap, reps[path]) == mmul(image, swap)
        deck_checks += 2
    assert mmul(mmul(rotation, rotation), rotation) == [
        [int(i == j) for j in range(18)] for i in range(18)]
    assert mmul(swap, swap) == [[int(i == j) for j in range(18)] for i in range(18)]
    assert mmul(swap, rotation) == mmul(rotation, swap)
    assert Counter(v for _, _, v in states) == {0: 6, 1: 6, 2: 6}
    # Arbitrary induced homomorphisms on P tensor_Λ B, with nilpotent Hom entries.
    cases = []
    for multiplicities in ((1, 0, 0), (1, 1, 0), (2, 1, 0)):
        copies, _, _, homs = projective_data(multiplicities)
        tensor_basis = [(v, c, s) for v, c in copies for s in states if s[2] == v]
        ti = {x: i for i, x in enumerate(tensor_basis)}
        ci = {x: i for i, x in enumerate(copies)}
        for case in range(3):
            f = zeros(len(tensor_basis))
            top = zeros(len(copies))
            for j, (v, c, w, d, path) in enumerate(homs):
                coefficient = (7*j+3*j*j+5*case) % 13-6
                for source in states:
                    if source[2] != v:
                        continue
                    for target in states:
                        if target[2] == w:
                            f[ti[(w, d, target)]][ti[(v, c, source)]] += (
                                coefficient*reps[path][index[target]][index[source]])
                if path[1] == 0:
                    top[ci[(w, d)]][ci[(v, c)]] += coefficient
            factor = local_polynomial(f)
            assert factor == ppow(local_polynomial(top), 6)
            cases.append({'multiplicities': multiplicities, 'case': case,
                          'top_factor': local_polynomial(top), 'coefficient_kernel_factor': factor})
    return {'multiplication_pairs': count, 'deck_intertwining_checks': deck_checks,
            'vertex_ranks': [6, 6, 6], 'determinant_cases': cases}


def checks():
    assert emul(OMEGA, emul(OMEGA, OMEGA)) == ONE
    counts = Counter()
    supports, end_entries = [], []
    for degree in range(MAX_SERIES_DEGREE+1):
        for i in range(3):
            weight = phase(degree-i)
            assert epow(weight, 3) == ONE
            counts['tame_cubes'] += 1
            assert phase(degree-(i+1)) == emul(phase(-1), weight)
            counts['clock_shift_commutators'] += 1
            assert phase(degree+1-(i+1)) == weight
            counts['weighted_rotation_commutes'] += 1
            for arrow in range(3):
                # v E_(arrow,arrow-1) on a nonzero basis input.
                if i == (arrow-1) % 3 and degree < MAX_SERIES_DEGREE:
                    assert phase(degree+1-arrow) == weight
                    counts['nonzero_balanced_arrow_intertwiners'] += 1
                counts['balanced_arrow_candidate_cases'] += 1
            if weight == ONE:
                supports.append([i, degree])
            for r in range(3):
                # The orbit intertwiner is C (not v*C), so degree stays fixed.
                assert phase(degree-i+r) == phase(degree-(i+1)+(r+1))
                counts['orbit_intertwiners'] += 1
    for r in range(3):
        exponents = [(i-r) % 3 for i in range(3)]
        cut = [(1+exponents[(i-1) % 3]-exponents[i])//3 for i in range(3)]
        assert cut == [int(i == r) for i in range(3)]
        assert sum(exponents) == 3
        assert sum(x == 0 for x in exponents) == 1
    for i, j in product(range(3), repeat=2):
        exponent = (i-j) % 3
        u_order = (exponent+j-i)//3
        assert u_order == int(i < j)
        end_entries.append({'row': i, 'column': j, 'v_order': exponent, 'u_order_in_invariant_basis': u_order})
        for degree in range(MAX_SERIES_DEGREE+1):
            assert (phase(degree-i+j) == ONE) == (degree % 3 == exponent)
            counts['endomorphism_coefficient_weights'] += 1
    # Sym^m global carrier group weights: central commutation does not imply coarse descent.
    symmetric_weights = []
    for m in range(10):
        monomials = [(a, b, m-a-b) for a in range(m+1) for b in range(m-a+1)]
        weights = Counter((-b-2*c) % 3 for _, b, c in monomials)
        assert sum(weights.values()) == (m+1)*(m+2)//2
        central_trivial = phase(-m) == ONE
        assert central_trivial == (m % 3 == 0)
        symmetric_weights.append({'degree': m, 'dimension': len(monomials),
                                 'inertia_weights': [weights[r] for r in range(3)],
                                 'commutator_trivial': central_trivial,
                                 'effective_coarse_descent': all(r == 0 or n == 0 for r, n in weights.items())})
    assert symmetric_weights[3]['inertia_weights'] == [4, 3, 3]
    assert symmetric_weights[3]['commutator_trivial'] and not symmetric_weights[3]['effective_coarse_descent']
    # Actual prime7 Jacobi edge-polynomial candidates fail at the clock, b != 0.
    failures = []
    for a, b in ((3, 2), (-1, -3)):
        defect = escale(b, eadd(phase(2), (-1, 0)))
        assert defect != ZERO
        failures.append({'a': a, 'b': b, 'commutator_coefficient': defect})
    normalization = normalization_representation()
    return {'scope': 'Bounded exact corroboration; infinite theta order remains primary; no GRH claim',
            'parameters': {'coefficient_field': 'Q(omega)', 'omega_square': '-1-omega',
                           'ramification': 'u=v^3', 'max_series_degree': MAX_SERIES_DEGREE,
                           'randomness': None}, 'counts': dict(counts),
            'invariant_basis_degrees': [0, 1, 2], 'comparison_determinant_v_degree': 3,
            'comparison_closed_fiber_rank': 1, 'determinant_comparison_u_order': 1,
            'invariant_support_sample': supports, 'endomorphism_order_entries': end_entries,
            'symmetric_power_weights': symmetric_weights, 'arithmetic_nondescent_controls': failures,
            'normalization': normalization}


def run(write_output=True):
    report = checks()
    if write_output:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'counts': report['counts'], 'normalization_vertex_ranks': report['normalization']['vertex_ranks'],
                      'normalization_multiplications': report['normalization']['multiplication_pairs'],
                      'normalization_deck_checks': report['normalization']['deck_intertwining_checks'],
                      'coefficient_kernel_determinant_cases': len(report['normalization']['determinant_cases'])}, indent=2))
    return report


if __name__ == '__main__':
    run()
