#!/usr/bin/env python3
"""Exact finite regression checks for the final toric source audit.

Uses only the Python standard library. Rational matrix checks compare
independent direct suffix summation and chronological recurrence with the
telescoping formula. These examples supplement the accompanying general
proofs; they are not a continuum PDE, quantum-hardware, or security result.
"""
from __future__ import annotations

# Protect imported verifier functions as well as the command-line entry point.
if not __debug__:
    raise RuntimeError("Verification requires assertions; run without -O or PYTHONOPTIMIZE")

import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
import math
from pathlib import Path
import random


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def shape(a):
    if not a or not a[0] or any(len(row) != len(a[0]) for row in a):
        raise ValueError("Expected a nonempty rectangular matrix")
    return len(a), len(a[0])


def mul(a, b):
    _, ac = shape(a)
    br, _ = shape(b)
    if ac != br:
        raise ValueError("Matrix composition has incompatible types")
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    if shape(a)[1] != len(x):
        raise ValueError("Matrix and vector have incompatible types")
    return [sum((r[j] * x[j] for j in range(len(x))), Q(0)) for r in a]


def add(x, y):
    if len(x) != len(y):
        raise ValueError("Cannot add vectors in different spaces")
    return [a + b for a, b in zip(x, y)]


def sub(x, y):
    if len(x) != len(y):
        raise ValueError("Cannot subtract vectors in different spaces")
    return [a - b for a, b in zip(x, y)]


def inverse(a):
    n = len(a)
    aug = [a[i][:] + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        q = aug[j][j]
        aug[j] = [x / q for x in aug[j]]
        for i in range(n):
            if i != j:
                q = aug[i][j]
                aug[i] = [x - q * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def product(arrows, dim):
    out = eye(dim)
    for a in arrows:
        out = mul(a, out)
    return out


def suffix_sum(arrows, states):
    if len(states) != len(arrows) + 1:
        raise ValueError("A path needs one more state than arrows")
    n = len(arrows)
    out = [Q(0)] * len(states[-1])
    for j in range(n):
        # Later arrows act on the left; order is not commuted.
        suffix = product(arrows[j + 1:], len(states[j + 1]))
        out = add(out, mv(suffix, sub(states[j + 1], mv(arrows[j], states[j]))))
    return out


def recurrence(arrows, states):
    if len(states) != len(arrows) + 1:
        raise ValueError("A path needs one more state than arrows")
    out = [Q(0)] * len(states[0])
    for j, a in enumerate(arrows):
        out = add(mv(a, out), sub(states[j + 1], mv(a, states[j])))
    return out


def old_prefix_sum(arrows, states):
    out, prefix = [Q(0)] * len(states[0]), eye(len(states[0]))
    for j, a in enumerate(arrows):
        # The audited source's A_1 ... A_j convention, exactly as written.
        prefix = mul(prefix, a)
        out = add(out, mv(prefix, sub(states[j + 1], mv(a, states[j]))))
    return out


def tropical_max(values):
    """None represents exact minus infinity, never a finite penalty."""
    finite = [value for value in values if value is not None]
    return max(finite) if finite else None


def tropical_mv(matrix, vector):
    if shape(matrix)[1] != len(vector):
        raise ValueError("Tropical matrix and vector have incompatible types")
    return [tropical_max(weight + value for weight, value in zip(row, vector)
                         if weight is not None and value is not None)
            for row in matrix]


def tropical_merge(left, right):
    if len(left) != len(right):
        raise ValueError("Tropical states have incompatible types")
    return [tropical_max([a, b]) for a, b in zip(left, right)]


def enumerate_paths(matrix, initial, steps):
    """Independent enumeration, using D[target][source] and exact rationals."""
    n = len(initial)
    result = [None] * n
    for source, initial_score in enumerate(initial):
        if initial_score is None:
            continue
        for tail in itertools.product(range(n), repeat=steps):
            score, vertex = initial_score, source
            for target in tail:
                edge = matrix[target][vertex]
                if edge is None:
                    score = None
                    break
                score += edge
                vertex = target
            if score is not None:
                result[vertex] = tropical_max([result[vertex], score])
    return result


def max_times_mul(a, b):
    """Maximum-product composition of nonnegative finite matrices."""
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise ValueError("Maximum-product composition has incompatible types")
    if any(x < 0 for matrix in (a, b) for row in matrix for x in row):
        raise ValueError("Maximum-product weights must be nonnegative")
    return [[max(a[i][k] * b[k][j] for k in range(ac))
             for j in range(bc)] for i in range(ar)]


def path_multiplicity_bounds(arrows, input_dim):
    """Retain path counts that an ordinary max-plus diagnostic discards.

    Products use chronological arrows, including genuinely rectangular maps.
    Every matrix entry is a rational or integer. This finite checker does not
    estimate an infinite-horizon exponent or claim a continuum stability bound.
    """
    if not isinstance(input_dim, int) or input_dim < 1:
        raise ValueError("The input dimension must be a positive integer")
    actual = eye(input_dim)
    absolute_sum = eye(input_dim)
    maximum = eye(input_dim)
    counts = eye(input_dim)
    for arrow in arrows:
        magnitude = [[abs(value) for value in row] for row in arrow]
        support = [[int(value != 0) for value in row] for row in arrow]
        actual = mul(arrow, actual)
        absolute_sum = mul(magnitude, absolute_sum)
        maximum = max_times_mul(magnitude, maximum)
        counts = mul(support, counts)
    bound = [[count * weight for count, weight in zip(cr, wr)]
             for cr, wr in zip(counts, maximum)]
    norm = max(sum(abs(value) for value in row) for row in actual)
    row_bound = max(sum(row) for row in bound)
    max_path_count = max(sum(row) for row in counts)
    max_path_weight = max(value for row in maximum for value in row)
    return {"actual": actual, "absolute_sum": absolute_sum, "maximum": maximum,
            "counts": counts, "entry_bound": bound, "norm": norm,
            "row_bound": row_bound, "coarse_bound": max_path_count * max_path_weight}


def enumerate_matrix_paths(arrows, input_dim):
    """Independent exhaustive calculation for the bounded regression cases."""
    dims = [input_dim]
    for arrow in arrows:
        rows, cols = shape(arrow)
        if cols != dims[-1]:
            raise ValueError("Enumerated path has incompatible spaces")
        dims.append(rows)
    actual = [[Q(0)] * input_dim for _ in range(dims[-1])]
    maximum = [[Q(0)] * input_dim for _ in range(dims[-1])]
    counts = [[0] * input_dim for _ in range(dims[-1])]
    for indices in itertools.product(*(range(dim) for dim in dims)):
        weight = Q(1)
        for t, arrow in enumerate(arrows):
            weight *= arrow[indices[t + 1]][indices[t]]
        if weight:
            i, j = indices[-1], indices[0]
            actual[i][j] += weight
            maximum[i][j] = max(maximum[i][j], abs(weight))
            counts[i][j] += 1
    return actual, maximum, counts


def _weighted_gain_scalar(value, name):
    """Accept only the exact scalar types this certificate can justify."""
    # In particular, bool is an int subclass and custom numeric subclasses
    # can replace arithmetic/comparisons. Check exact types before arithmetic.
    if type(value) is not int and type(value) is not Q:
        raise TypeError(f"{name} must be a built-in int or fractions.Fraction")
    return Q(value)


def _weighted_gain_evaluation(gain, weights, rate):
    rows, cols = shape(gain)
    if rows != cols or len(weights) != rows:
        raise ValueError("Gain certificate needs a square matrix and matching weights")
    gain = [[_weighted_gain_scalar(value, f"gain[{i}][{j}]")
             for j, value in enumerate(row)] for i, row in enumerate(gain)]
    weights = [_weighted_gain_scalar(value, f"weights[{i}]")
               for i, value in enumerate(weights)]
    rate = _weighted_gain_scalar(rate, "rate")
    if any(value < 0 for row in gain for value in row) or rate < 0:
        raise ValueError("Gain bounds and rate must be nonnegative")
    if any(weight <= 0 for weight in weights):
        raise ValueError("Block-norm weights must be strictly positive")
    lhs = mv(gain, weights)
    rhs = [rate * weight for weight in weights]
    slack = [limit - value for limit, value in zip(rhs, lhs)]
    row_bounds = [value / weight for value, weight in zip(lhs, weights)]
    holds = all(value >= 0 for value in slack)
    return {"gain": gain, "weights": weights, "rate": rate,
            "row_lhs": lhs, "row_rhs": rhs, "row_slack": slack,
            "row_bounds": row_bounds, "weighted_bound": max(row_bounds),
            "bound_holds": holds, "certifies_contraction": holds and rate < 1}


def weighted_gain_certificate(gain, weights, rate):
    """Check G w <= q w for exact built-in int/Fraction scalar inputs.

    G must be a nonnegative square matrix, w strictly positive and q >= 0.
    Floats (including finite ones), bools and custom scalar subclasses are
    rejected before arithmetic. Explicit Fraction conversion is the caller's
    responsibility; silently rounding an approximate witness can certify a
    false bound. Existing valid exact inputs still return a bool.

    At fixed q these are linear feasibility inequalities. True with q >= 1
    is a gain bound, not a strict contraction. Applying a q < 1 bound to an
    actual update requires a separately justified domain-valid gain envelope.
    This function verifies supplied weights; it does not optimize q and w.
    """
    return _weighted_gain_evaluation(gain, weights, rate)["bound_holds"]


def weighted_gain_witness(gain, weights, rate):
    """Return a replayable exact JSON witness, including rejected bounds.

    Decimal numerator/positive-denominator strings preserve arbitrary integer
    precision in JSON. Each Fraction is reduced with a positive denominator.
    check_weighted_gain_witness.py independently recomputes the entire record
    using integer arithmetic, without importing this implementation.

    The contraction flag concerns the supplied finite matrix in its weighted
    maximum norm. No LP optimum, global nonlinear gain envelope, invariant
    domain, continuum PDE result or file-authenticity guarantee is implied.
    """
    result = _weighted_gain_evaluation(gain, weights, rate)

    def encode(value):
        return {"numerator": str(value.numerator),
                "denominator": str(value.denominator)}

    return {
        "schema_version": 1,
        "kind": "weighted-gain",
        "gain": [[encode(value) for value in row] for row in result["gain"]],
        "weights": [encode(value) for value in result["weights"]],
        "rate": encode(result["rate"]),
        **{key: [encode(value) for value in result[key]]
           for key in ("row_lhs", "row_rhs", "row_slack", "row_bounds")},
        "weighted_bound": encode(result["weighted_bound"]),
        "bound_holds": result["bound_holds"],
        "certifies_contraction": result["certifies_contraction"],
    }


def run_checks():
    # The exact checks below deliberately use assert. Never certify a run in
    # which Python optimization has compiled those assertions away.
    if not __debug__:
        raise RuntimeError("Verification requires assertions; run without -O or PYTHONOPTIMIZE")
    rng = random.Random(20261113)
    checked = 0
    for dim in range(1, 5):
        for length in range(9):
            for _ in range(8):
                arrows = [[[Q(rng.randrange(-3, 4), rng.randrange(1, 4))
                            for _ in range(dim)] for _ in range(dim)]
                          for _ in range(length)]
                states = [[Q(rng.randrange(-4, 5)) for _ in range(dim)]
                          for _ in range(length + 1)]
                expected = sub(states[-1], mv(product(arrows, dim), states[0]))
                assert suffix_sum(arrows, states) == expected
                assert recurrence(arrows, states) == expected
                checked += 1

    # Actual varying dimensions, including information-losing rectangular maps.
    rectangular_checks = 0
    for length in range(1, 7):
        for _ in range(20):
            dims = [rng.randrange(1, 6) for _ in range(length + 1)]
            arrows = [[[Q(rng.randrange(-3, 4), rng.randrange(1, 4))
                        for _ in range(dims[j])] for _ in range(dims[j + 1])]
                      for j in range(length)]
            states = [[Q(rng.randrange(-4, 5)) for _ in range(dim)] for dim in dims]
            expected = sub(states[-1], mv(product(arrows, dims[0]), states[0]))
            assert suffix_sum(arrows, states) == expected
            assert recurrence(arrows, states) == expected
            rectangular_checks += 1

    # Two noncommuting shears; the third closes the holonomy exactly.
    a = [[Q(1), Q(2)], [Q(0), Q(1)]]
    b = [[Q(1), Q(0)], [Q(3), Q(1)]]
    assert mul(a, b) != mul(b, a)
    c = inverse(mul(b, a))
    assert product([a, b, c], 2) == eye(2)
    flat_checks = 0
    for _ in range(128):
        states = [[Q(rng.randrange(-4, 5)) for _ in range(2)] for _ in range(4)]
        states[-1] = states[0][:]
        assert suffix_sum([a, b, c], states) == [Q(0), Q(0)]
        assert recurrence([a, b, c], states) == [Q(0), Q(0)]
        flat_checks += 1

    arrows, states = [[[Q(2)]], [[Q(1, 2)]]], [[Q(0)], [Q(1)], [Q(0)]]
    assert product(arrows, 1) == eye(1)
    assert old_prefix_sum(arrows, states) == [Q(3, 2)]
    assert suffix_sum(arrows, states) == [Q(0)]

    damping = []
    for eta in [Q(1), Q(1, 2), Q(1, 10), Q(1, 1000)]:
        factor = (1 - eta) + eta * 2
        assert factor > 1
        damping.append({"eta": str(eta), "exact_factor": str(factor)})

    # JVP-only power iteration need not estimate a nonnormal operator norm.
    # J is nilpotent with norm M; starting at e2 gives M*e1 and then zero.
    # By contrast J^T J = diag(0, M^2), identifying the singular direction.
    shear_size = Q(10)
    jacobian = [[Q(0), shear_size], [Q(0), Q(0)]]
    transpose = [list(row) for row in zip(*jacobian)]
    zero_matrix = [[Q(0), Q(0)], [Q(0), Q(0)]]
    assert mul(jacobian, jacobian) == zero_matrix
    assert mv(jacobian, [Q(0), Q(1)]) == [shear_size, Q(0)]
    assert mv(jacobian, [Q(1), Q(0)]) == [Q(0), Q(0)]
    assert mul(transpose, jacobian) == [[Q(0), Q(0)], [Q(0), shear_size**2]]

    # X is uniform on four values; B=Z=X mod 2, S=floor(X/2).
    # Check conditional independence B ⟂ Z | X by cross-multiplication,
    # avoiding numerical logarithms, including every zero-probability pair.
    law = {(x, x % 2, x % 2): Q(1, 4) for x in range(4)}
    ci_checks = 0
    for x in range(4):
        px = sum(p for (xx, _, _), p in law.items() if xx == x)
        for bb in range(2):
            for z in range(2):
                pbz = law.get((x, bb, z), Q(0))
                pb = sum(p for (xx, bbb, _), p in law.items() if xx == x and bbb == bb)
                pz = sum(p for (xx, _, zz), p in law.items() if xx == x and zz == z)
                assert pbz * px == pb * pz
                ci_checks += 1
    # Conditional on either S value B is a fair bit; given Z it is determined.
    entropy_given_s = -2 * 0.5 * math.log2(0.5)
    assert entropy_given_s == 1.0

    tropical_checks = 0
    for dim in range(1, 5):
        for horizon in range(6):
            for _ in range(4):
                matrix = [[None if rng.randrange(4) == 0 else Q(rng.randrange(-3, 4))
                           for _ in range(dim)] for _ in range(dim)]
                initial = [Q(rng.randrange(-3, 4)) for _ in range(dim)]
                exact, bounded = initial[:], initial[:]
                for _ in range(horizon):
                    exact = tropical_mv(matrix, exact)
                    bounded = tropical_merge(bounded, tropical_mv(matrix, bounded))
                assert exact == enumerate_paths(matrix, initial, horizon)
                exhaustive = initial[:]
                for steps in range(1, horizon + 1):
                    exhaustive = tropical_merge(exhaustive, enumerate_paths(matrix, initial, steps))
                assert bounded == exhaustive
                tropical_checks += 1

    # Appendix C.5's pure-power recurrence does not compute its stated star.
    matrix, initial = [[Q(-1)]], [Q(0)]
    exact_two = tropical_mv(matrix, tropical_mv(matrix, initial))
    bounded_two = tropical_merge(initial, tropical_mv(matrix, initial))
    bounded_two = tropical_merge(bounded_two, tropical_mv(matrix, bounded_two))
    assert exact_two == [Q(-2)] and bounded_two == [Q(0)]

    # Finite masks require a range certificate; no finite M annihilates all values.
    mask_examples = []
    for penalty in [Q(1), Q(3), Q(17)]:
        excluded_raw = penalty + 1
        assert max(Q(0), excluded_raw - penalty) == 1
        mask_examples.append({"penalty": str(penalty), "excluded_raw": str(excluded_raw),
                              "masked_max": "1", "admissible_max": "0"})
    lower, upper = Q(-2), Q(5)
    penalty = upper - lower + 1
    assert upper - penalty < lower

    # Exact witnesses at a=b=1: log(1)=0, and log(2)>0 by monotonicity.
    shift = Q(1)
    actual_product_log = -shift
    incorrect_product_log = (-shift) + (-shift) - shift
    corrected_product_log = (-shift) + (-shift) + shift
    assert actual_product_log == corrected_product_log != incorrect_product_log
    assert Q(1) + Q(1) > Q(1)  # the exact positive-input order witness, not a numeric log test

    # Max-times weights alone omit the multiplicity of summands in an
    # ordinary linear product. Check every path independently on small
    # rectangular spaces, including empty paths and exact cancellation.
    multiplicity_checks = 0
    for length in range(6):
        for _ in range(12):
            dims = [rng.randrange(1, 4) for _ in range(length + 1)]
            arrows = [[[Q(rng.randrange(-2, 3), rng.randrange(1, 4))
                        for _ in range(dims[t])] for _ in range(dims[t + 1])]
                      for t in range(length)]
            report = path_multiplicity_bounds(arrows, dims[0])
            exact, maximum, counts = enumerate_matrix_paths(arrows, dims[0])
            assert report["actual"] == exact
            assert report["maximum"] == maximum
            assert report["counts"] == counts
            for i in range(dims[-1]):
                for j in range(dims[0]):
                    assert (abs(exact[i][j]) <= report["absolute_sum"][i][j]
                            <= report["entry_bound"][i][j])
            assert report["norm"] <= report["row_bound"] <= report["coarse_bound"]
            multiplicity_checks += 1

    # All maximal individual paths decay, yet adding their contributions
    # expands the all-ones vector. The dense bound is attained exactly.
    branching_examples = []
    for dim in range(2, 5):
        weight = Q(dim + 1, 2 * dim)
        assert Q(1, dim) < weight < 1 and dim * weight > 1
        matrix = [[weight] * dim for _ in range(dim)]
        for horizon in range(1, 7):
            report = path_multiplicity_bounds([matrix] * horizon, dim)
            assert max(value for row in report["maximum"] for value in row) == weight**horizon
            assert report["norm"] == (dim * weight)**horizon
            assert report["norm"] == report["row_bound"] == report["coarse_bound"]
        branching_examples.append({"dimension": dim, "edge_weight": str(weight),
                                   "max_times_growth_factor": str(weight),
                                   "ordinary_growth_factor": str(dim * weight)})

    gain = [[Q(0), Q(2)], [Q(1, 8), Q(0)]]
    weights = [Q(4), Q(1)]
    assert max(sum(row) for row in gain) == 2
    assert weighted_gain_certificate(gain, weights, Q(1, 2))
    assert not weighted_gain_certificate(gain, weights, Q(2, 5))
    # For every positive witness, multiplying the two feasibility inequalities
    # requires q^2 >= 1/4. This is the exact algebraic impossibility witness.
    assert Q(2, 5)**2 < Q(1, 4)

    # XOR synergy on two independent disjoint components. All comparisons
    # are rational; the entropy values follow from fair/deterministic laws.
    xor_law = {(x, y, x ^ y): Q(1, 4) for x in range(2) for y in range(2)}
    independence_checks = 0
    for left, right in [(0, 1), (0, 2), (1, 2)]:
        for a, b in itertools.product(range(2), repeat=2):
            joint = sum(p for key, p in xor_law.items() if key[left] == a and key[right] == b)
            marginal_left = sum(p for key, p in xor_law.items() if key[left] == a)
            marginal_right = sum(p for key, p in xor_law.items() if key[right] == b)
            assert joint == marginal_left * marginal_right
            independence_checks += 1
    assert all(b == (x + y) % 2 for x, y, b in xor_law)
    # Given B, X and Y are not independent; no overlap of source components
    # is required for the conditional dependence that yields predictive gain.
    assert xor_law[(0, 0, 0)] / Q(1, 2) == Q(1, 2) != Q(1, 2)**2

    # For deterministic binary labels, every interior forecast can be
    # improved. Exact probabilities witness the monotonic log-loss argument.
    endpoint_checks = 0
    for n in range(1, 33):
        q = Q(1, n + 1)
        improved_zero = q / 2
        improved_one = (1 + q) / 2
        assert 0 < improved_zero < q < improved_one < 1
        assert 1 - improved_zero > 1 - q > 0
        endpoint_checks += 1

    return {
        "schema_version": 3,
        "status": "passed",
        "arithmetic": "fractions.Fraction for all matrix and damping checks",
        "seed": 20261113,
        "generic_path_checks": checked,
        "rectangular_path_checks": rectangular_checks,
        "noncommuting_flat_cycle_checks": flat_checks,
        "conditional_independence_checks": ci_checks,
        "prefix_counterexample": {"holonomy": "1", "old_residual": "3/2", "correct_residual": "0"},
        "positive_damping_counterexamples": damping,
        "jvp_norm_counterexample": {
            "matrix": "[[0,10],[0,0]]",
            "matrix_squared": "zero",
            "spectral_radius": "0",
            "spectral_norm": str(shear_size),
            "J_transpose_J": "diag(0,100)",
            "pure_J_iteration_from_e2_after_two_steps": "zero",
            "scope": "A JVP-only iterate is not a certified singular-norm upper bound.",
        },
        "certificate_information_example": {
            "I_B_Z_given_complete_X_bits": 0,
            "I_B_Z_given_lossy_S_bits": entropy_given_s,
            "definition": "X uniform on {0,1,2,3}; B=Z=X mod 2; S=floor(X/2)",
        },
        "tropical_path_enumeration_checks": tropical_checks,
        "tropical_horizon_counterexample": {
            "D": "[-1]", "v0": "[0]", "steps": 2,
            "pure_power": "[-2]", "bounded_length_closure": "[0]",
        },
        "finite_mask_counterexamples": mask_examples,
        "logarithmic_counterexamples": {
            "a": "1", "b": "1", "lambda": "1",
            "v_lambda_ab": str(actual_product_log),
            "incorrect_minus_offset": str(incorrect_product_log),
            "correct_plus_offset": str(corrected_product_log),
            "additivity_witness": "2 > 1, so log(2) > log(1)=0; no floating-point logarithm used",
        },
        "path_multiplicity": {
            "independent_exhaustive_checks": multiplicity_checks,
            "dense_branching_counterexamples": branching_examples,
            "exact_dense_horizons_per_example": 6,
            "bound": "abs(product)[i,j] <= sum_abs_path_weights[i,j] <= count[i,j] * maximum_path_weight[i,j]",
            "scope": "Finite exact products, not empirical or infinite-horizon Lyapunov estimates",
        },
        "weighted_gain": {
            "G": "[[0,2],[1/8,0]]", "weights": "[4,1]",
            "unweighted_row_bound": "2", "certified_weighted_bound": "1/2",
            "rejected_rate": "2/5", "necessary_rate_squared": ">= 1/4",
            "optimization_scope": "Fixed-rate linear feasibility witness; no joint rate/weight LP claim",
        },
        "xor_information_synergy": {
            "exact_pairwise_independence_checks": independence_checks,
            "law": "X,Y independent fair bits; B=X XOR Y; T=X+Y",
            "I_B_X_bits": 0, "I_B_Y_bits": 0, "I_B_T_bits": 1,
            "I_B_Y_given_X_bits": 1, "source_component_overlap": "empty",
            "scope": "Exact probability equalities; fair/deterministic entropy arguments in the manuscript",
        },
        "cross_entropy_endpoints": {
            "exact_interior_improvement_checks": endpoint_checks,
            "deterministic_zero_label_improvement": "q -> q/2",
            "deterministic_one_label_improvement": "q -> (1+q)/2",
            "scope": "Probability inequalities plus monotonicity of log; no numeric logarithm certificate",
        },
        "scope": "Finite exact regression examples; the manuscript and Lean contain the general transport proof.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "upstream_pins": {
            "Tropical_Quivers_of_Archs": "2b6ab79a685e2c6233fb8892e59589951feeddad",
            "ToricGT-Program": "f91ba1811b5a4f70d53c7120acf8ca2a0049f85b",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = json.dumps(run_checks(), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    print(report, end="")


if __name__ == "__main__":
    main()
