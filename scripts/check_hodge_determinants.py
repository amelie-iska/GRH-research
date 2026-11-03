#!/usr/bin/env python3
"""Exact finite checks of Hodge cancellation and the escaping-boundary defect.

The infinite Hilbert-space and Fredholm statements are proved in the note;
these deterministic rational checks do not formalize them or establish GRH.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_projective_resolutions import (
    zero, identity, add, scale, multiply, determinant, inverse, rank)


def transpose(a):
    return [list(row) for row in zip(*a)]


def block(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def complex_checks():
    examples = [
        ('interval', [2, 1], [[[-1, 1]]]),
        ('circle', [3, 3], [[[-1, 1, 0], [0, -1, 1], [1, 0, -1]]]),
        ('filled_triangle', [3, 3, 1],
         [[[-1, 1, 0], [0, -1, 1], [1, 0, -1]], [[1, 1, 1]]]),
        ('augmented_triangle', [1, 3, 3, 1],
         [[[1], [1], [1]], [[-1, 1, 0], [0, -1, 1], [1, 0, -1]], [[1, 1, 1]]]),
        ('nontrivial_cohomology', [2, 3, 2],
         [[[1, 0], [0, 0], [0, 0]], [[0, 1, 0], [0, 0, 0]]])]
    result = []
    counts = {'complex_metric_systems': 0, 'normalized_determinants': 0,
              'cleared_shifted_determinants': 0, 'positive_mass_ratios': 0}
    for name, dims, differentials in examples:
        for i in range(len(differentials)-1):
            assert multiply(differentials[i+1], differentials[i]) == zero(dims[i+2], dims[i])
        ranks = [rank(d) for d in differentials]
        betti = [d - (ranks[i] if i < len(ranks) else 0) -
                 (ranks[i-1] if i > 0 else 0) for i, d in enumerate(dims)]
        chi = sum((-1)**i*d for i, d in enumerate(dims))
        assert chi == sum((-1)**i*d for i, d in enumerate(betti))
        offsets, total = [], 0
        for d in dims:
            offsets.append(total)
            total += d
        parities = [[offsets[i]+j for i, d in enumerate(dims)
                     if i % 2 == parity for j in range(d)] for parity in [0, 1]]
        for metric in range(3):
            # Exact orthonormal coordinates for H=diag(r_j^2), r_j>0.
            scales = [Q(1) if metric == 0 else Q(1+(j+metric) % 5) for j in range(total)]
            d = zero(total, total)
            for i, diff in enumerate(differentials):
                for row in range(dims[i+1]):
                    for col in range(dims[i]):
                        r, c = offsets[i+1]+row, offsets[i]+col
                        d[r][c] = scales[r]*Q(diff[row][col])/scales[c]
            assert multiply(d, d) == zero(total, total)
            dirac = add(d, transpose(d))
            laplace = multiply(dirac, dirac)
            even, odd = parities
            b = [[dirac[i][j] for j in even] for i in odd]
            g0, g1 = multiply(transpose(b), b), multiply(b, transpose(b))
            assert block(laplace, even) == g0 and block(laplace, odd) == g1
            assert all(laplace[i][j] == 0 for i in even for j in odd)
            for z in [Q(0), Q(1, 3), Q(-1), Q(2)]:
                assert determinant(add(identity(len(even)), scale(z, g0))) == determinant(
                    add(identity(len(odd)), scale(z, g1)))
                counts['normalized_determinants'] += 1
            for mass in [Q(0), Q(1, 2), Q(-1), Q(3)]:
                a0 = determinant(add(scale(mass, identity(len(even))), g0))
                a1 = determinant(add(scale(mass, identity(len(odd))), g1))
                assert a0*mass**len(odd) == a1*mass**len(even)
                counts['cleared_shifted_determinants'] += 1
                if mass > 0:
                    assert a0 > 0 and a1 > 0 and a0/a1 == mass**chi
                    counts['positive_mass_ratios'] += 1
            counts['complex_metric_systems'] += 1
        result.append({'name': name, 'term_dimensions': dims, 'betti_numbers': betti,
                       'euler_characteristic': chi})
    return result, counts


def boundary_checks():
    samples = []
    for weight in [Q(1, 2), Q(1, 3), Q(-1, 2), Q(2)]:
        for n in range(2, 8):
            shift = zero(n, n)
            for i in range(n-1):
                shift[i+1][i] = 1
            a = add(identity(n), scale(-weight, multiply(transpose(shift), shift)))
            c = add(identity(n), scale(-weight, multiply(shift, transpose(shift))))
            relative = multiply(a, inverse(c))
            limit_compression = identity(n)
            limit_compression[0][0] = 1-weight
            assert relative[0][0] == 1-weight
            assert relative[-1][-1] == 1/(1-weight)
            assert determinant(relative) == 1
            assert determinant(limit_compression) == 1-weight
            difference = add(relative, scale(-1, limit_compression))
            assert all(difference[i][j] == 0 for i in range(n) for j in range(n)
                       if (i, j) != (n-1, n-1))
            trace_norm = sum(abs(difference[i][i]) for i in range(n))
            assert trace_norm == abs(1/(1-weight)-1) > 0
            assert [row[:-1] for row in relative[:-1]] == [row[:-1] for row in limit_compression[:-1]]
            samples.append({'N': n, 'weight': str(weight), 'finite_relative_det': '1',
                            'boundary_relative_det': str(1-weight),
                            'trace_norm_distance': str(trace_norm)})
    return samples


def run():
    examples, counts = complex_checks()
    boundary = boundary_checks()
    # Same exact identity complex d=1; only the positive target metric changes.
    metrics = [{'target_metric': str(r), 'laplacians': [str(r), str(r)],
                'ordinary_factor_at_z_1': str(r-1)} for r in [Q(1), Q(4)]]
    assert metrics[0]['ordinary_factor_at_z_1'] == '0'
    assert metrics[1]['ordinary_factor_at_z_1'] == '3'
    report = {'arithmetic': 'exact Fraction arithmetic; deterministic; no random seed required',
              'finite_complexes': examples, 'counts': counts, 'metric_example': metrics,
              'finite_boundary_samples': boundary,
              'boundary_count': len(boundary),
              'infinite_result_scope': 'Hilbert shift, relative Fredholm determinant, strong-limit and non-trace-norm-convergence claims are proved in prose, not inferred from finite samples.',
              'GRH_scope': 'No arithmetic L-function identity or positive arithmetic realization; no GRH proof.'}
    out = Path(__file__).resolve().parents[1]/'outputs/checks/2026-11-03-hodge/exact-checks.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'counts': counts, 'boundary_samples': len(boundary),
                      'output': str(out), 'scope': report['GRH_scope']}, indent=2))


if __name__ == '__main__':
    run()
