#!/usr/bin/env python3
"""Replay exact finite quantum-channel, feedback and tropical-gain examples.

Every executable validation is an explicit condition, never an assert.
All quantum matrix entries, controls, trajectories and error budgets use
rational arithmetic. The producer's existing transport module deliberately
refuses optimized Python imports; run this driver without -O. Its standalone
integer witness checker is invoked independently in subprocesses.

This is classical exact simulation of separately accessible ensemble states,
not a single-copy nonlinear quantum channel, trained model, hardware run,
finite-shot instrument or fluid solver. The stochastic interpretation of
readout errors is deliberately absent: only stated deterministic bounds are
used. The written global envelope and channel proofs have separate scope
from these finite implementation checks.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import platform
import random
import subprocess
import sys
import tempfile

import quantum_gain_control as model
from verify_toric_transport import (
    enumerate_matrix_paths, path_multiplicity_bounds, weighted_gain_witness,
)


SEED = 20261114
STEPS = 32
SOURCE_DIR = Path(__file__).resolve().parent
REPO = SOURCE_DIR.parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def cadd(left, right):
    return left[0] + right[0], left[1] + right[1]


def csub(left, right):
    return left[0] - right[0], left[1] - right[1]


def cmul(left, right):
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def cscale(value, scale):
    return value[0] * scale, value[1] * scale


def density(state):
    """Independent Pauli-matrix encoding, including imaginary coherence."""
    x, y, z = state
    return [[((1 + z) / 2, Q(0)), (x / 2, -y / 2)],
            [(x / 2, y / 2), ((1 - z) / 2, Q(0))]]


def determinant2(matrix):
    return csub(cmul(matrix[0][0], matrix[1][1]), cmul(matrix[0][1], matrix[1][0]))


def check_density(matrix):
    require(cadd(matrix[0][0], matrix[1][1]) == (1, 0), "Density trace is not one")
    for i in range(2):
        require(matrix[i][i][1] == 0 and matrix[i][i][0] >= 0, "Invalid density diagonal")
        for j in range(2):
            require(matrix[i][j] == (matrix[j][i][0], -matrix[j][i][1]), "Density is not Hermitian")
    det = determinant2(matrix)
    require(det[1] == 0 and det[0] >= 0, "Density matrix is not positive semidefinite")


def matrix_channel(matrix, control, retention):
    """Independent linear matrix action on arbitrary 2x2 complex inputs."""
    trace = cadd(matrix[0][0], matrix[1][1])
    probabilities = ((1 + control) / 2, (1 - control) / 2)
    result = [[cscale(value, retention) for value in row] for row in matrix]
    for i, probability in enumerate(probabilities):
        result[i][i] = cadd(result[i][i], cscale(trace, (1 - retention) * probability))
    return result


def choi_from_matrix_units(control, retention):
    result = [[Q(0)] * 4 for _ in range(4)]
    for i, j in itertools.product(range(2), repeat=2):
        unit = [[(Q(0), Q(0)) for _ in range(2)] for _ in range(2)]
        unit[i][j] = Q(1), Q(0)
        image = matrix_channel(unit, control, retention)
        for a, b in itertools.product(range(2), repeat=2):
            require(image[a][b][1] == 0, "Real matrix-unit image acquired an imaginary part")
            result[2 * i + a][2 * j + b] = image[a][b][0]
    return tuple(tuple(row) for row in result)


def determinant(matrix):
    """Permutation formula: exact and independent of a numerical eigensolver."""
    result = Q(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix)) for j in range(i + 1, len(matrix)))
        term = Q((-1) ** inversions)
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        result += term
    return result


def matrix_distance_squared(left, right):
    a, b = density(left), density(right)
    difference = [[csub(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]
    require(cadd(difference[0][0], difference[1][1]) == (0, 0), "Difference has nonzero trace")
    det = determinant2(difference)
    require(det[1] == 0 and det[0] <= 0, "Traceless Hermitian determinant has the wrong sign")
    return -det[0]


def exact_json(value):
    return json.dumps(model.encode_exact(value), indent=2, allow_nan=False) + "\n"


def source_hashes():
    names = ("quantum_gain_control.py", "verify_quantum_gain_control.py",
             "verify_toric_transport.py", "check_weighted_gain_witness.py")
    return {str((SOURCE_DIR / name).relative_to(REPO)):
            hashlib.sha256((SOURCE_DIR / name).read_bytes()).hexdigest() for name in names}


def run_checks():
    before = source_hashes()
    counts = {"channel_parameter_cases": 0, "choi_principal_minors": 0,
              "coherent_matrix_bloch_comparisons": 0, "fixed_control_distance_equalities": 0,
              "controller_pair_block_bounds": 0, "trajectory_state_budget_checks": 0,
              "residual_one_step_block_checks": 0, "path_horizons": 0,
              "invalid_domain_rejections": 0, "independent_gain_replays": 0}
    states = [(Q(0), Q(0), Q(0))]
    for axis, sign in itertools.product(range(3), (-1, 1)):
        state = [Q(0)] * 3
        state[axis] = Q(sign)
        states.append(tuple(state))
    states += [(Q(1, 3), Q(2, 3), Q(2, 3)), (Q(-2, 3), Q(1, 3), Q(2, 3)),
               (Q(2, 3), Q(2, 3), Q(-1, 3)), (Q(1, 3), Q(-1, 4), Q(1, 5)),
               (Q(0), Q(1, 2), Q(-1, 2))]
    for state in states:
        model.validate_bloch(state)
        check_density(density(state))
    controls = sorted({Q(n, d) for d in range(1, 9) for n in range(-d, d + 1)})
    retentions = (Q(0), Q(1, 4), Q(1, 2), Q(1))
    for retention, control in itertools.product(retentions, controls):
        choi = model.channel_choi(control, retention)
        require(choi == choi_from_matrix_units(control, retention), "Choi matrix-unit reconstruction failed")
        decomposition = model.choi_psd_decomposition(control, retention)
        require(all(coefficient >= 0 for coefficient, _ in decomposition), "Negative PSD coefficient")
        reconstructed = tuple(tuple(sum(coefficient * vector[i] * vector[j]
                                        for coefficient, vector in decomposition)
                                    for j in range(4)) for i in range(4))
        require(choi == reconstructed, "Choi PSD decomposition failed")
        require(sum(choi[i][i] for i in range(4)) == 2, "Unnormalized Choi trace is not two")
        for i, j in itertools.product(range(2), repeat=2):
            require(sum(choi[2*i+k][2*j+k] for k in range(2)) == int(i == j),
                    "Output partial trace of Choi is not the input identity")
        for size in range(1, 5):
            for indices in itertools.combinations(range(4), size):
                minor = [[choi[i][j] for j in indices] for i in indices]
                require(determinant(minor) >= 0, "A Choi principal minor is negative")
                counts["choi_principal_minors"] += 1
        for i, state in enumerate(states):
            other = states[(i + 1) % len(states)]
            evolved = model.channel_step(state, control, retention)
            independent = matrix_channel(density(state), control, retention)
            require(density(evolved) == independent, "Matrix and Bloch channel actions disagree")
            check_density(independent)
            counts["coherent_matrix_bloch_comparisons"] += 1
            evolved_other = model.channel_step(other, control, retention)
            initial_squared = matrix_distance_squared(state, other)
            final_squared = matrix_distance_squared(evolved, evolved_other)
            require(final_squared == retention**2 * initial_squared, "Fixed-control distance did not scale exactly")
            require(final_squared == model.squared_trace_distance(evolved, evolved_other),
                    "Bloch and determinant trace-distance identities disagree")
            counts["fixed_control_distance_equalities"] += 1
        counts["channel_parameter_cases"] += 1

    gain = model.feedback_gain()
    expected_gain = ((Q(1, 4), Q(3, 2)), (Q(3, 32), Q(1, 4)))
    require(gain == expected_gain, "Feedback envelope coefficients changed")
    require(max(sum(row) for row in gain) == Q(7, 4), "Unweighted row bound changed")
    require(model.feedback_step(model.FIXED_POINT)["states"] == model.FIXED_POINT,
            "Explicit fixed point is not fixed")
    initial_weighted_squared = max(
        model.squared_trace_distance(state, fixed) / weight**2
        for state, fixed, weight in zip(model.INITIAL_STATE, model.FIXED_POINT, model.WEIGHTS))
    require(initial_weighted_squared == model.INITIAL_ERROR_BUDGET**2,
            "Initial budget is not the exact weighted trace distance")
    first_step = model.feedback_step(model.INITIAL_STATE)
    require(first_step["states"] == ((Q(0), Q(1, 4), Q(-3, 4)), (Q(0), Q(0), Q(-1, 4))),
            "Initial coherent/saturated step disagrees with independent fractions")
    require(first_step["raw_controls"][0] == Q(-7, 4) and first_step["controls"][0] == -1,
            "Initial saturation is absent")

    # The exact local envelope is attained in an unsaturated diagonal direction.
    displaced = ((Q(0), Q(0), Q(2, 3)), (Q(0), Q(0), Q(1, 8)))
    local_budget = Q(1, 24)
    displaced_step = model.feedback_step(displaced)
    require(not any(displaced_step["saturated"]), "Sharpness witness unexpectedly clips")
    for i, weight in enumerate(model.WEIGHTS):
        require(model.squared_trace_distance(displaced[i], model.FIXED_POINT[i])
                == (local_budget * weight)**2, "Sharpness input distance changed")
        require(model.squared_trace_distance(displaced_step["states"][i], model.FIXED_POINT[i])
                == (model.RATE * local_budget * weight)**2, "Local gain rate is not attained")

    rng = random.Random(SEED)
    for graph in (model.GRAPH, tuple(tuple(-value for value in row) for row in model.GRAPH)):
        require(model.feedback_gain(graph=graph) == gain, "Signed graph gains must use absolute values")
        for _ in range(64):
            left, right = tuple(rng.choice(states) for _ in range(2)), tuple(rng.choice(states) for _ in range(2))
            left_out = model.feedback_step(left, graph=graph)["states"]
            right_out = model.feedback_step(right, graph=graph)["states"]
            squared_input = [matrix_distance_squared(x, y) for x, y in zip(left, right)]
            for i, row in enumerate(gain):
                squared_output = matrix_distance_squared(left_out[i], right_out[i])
                require(squared_output == model.squared_trace_distance(left_out[i], right_out[i]),
                        "Controller output distance disagrees with its matrix determinant")
                # For nonnegative gains and squared distances s0,s1, the
                # actual inequality sqrt(sout) <= g0*sqrt(s0)+g1*sqrt(s1)
                # is equivalent to t<=0 or t^2<=4*g0^2*g1^2*s0*s1, where
                # t=sout-g0^2*s0-g1^2*s1. No root approximation or larger
                # L1 bound is substituted for either input trace distance.
                t = squared_output - sum(coefficient**2 * squared
                                         for coefficient, squared in zip(row, squared_input))
                cross_squared = 4 * row[0]**2 * row[1]**2 * squared_input[0] * squared_input[1]
                require(t <= 0 or t**2 <= cross_squared,
                        "Global gain bound failed on an exact controller pair")
                counts["controller_pair_block_bounds"] += 1

    low = ((Q(0), Q(0), Q(0)), (Q(0), Q(0), Q(0)))
    high = ((Q(0), Q(0), Q(0)), (Q(0), Q(0), Q(1)))
    middle = tuple(tuple((x+y)/2 for x, y in zip(a, b)) for a, b in zip(low, high))
    gap = (model.feedback_step(middle)["states"][0][2]
           - (model.feedback_step(low)["states"][0][2] + model.feedback_step(high)["states"][0][2]) / 2)
    require(gap == Q(9, 32), "Nonlinear feedback midpoint witness changed")

    epsilon = Q(1, 100)
    delta = model.readout_error_budget((epsilon, epsilon))
    require(delta == Q(3, 1600), "Uniform readout residual budget changed")
    require(delta / (1 - model.RATE) == Q(1, 200), "Residual limsup upper bound changed")
    # Check unequal uncertainties independently, including one noiseless sensor.
    for e1, e2 in ((Q(0), epsilon), (epsilon, Q(0)), (Q(1, 50), Q(1, 200))):
        require(model.readout_error_budget((e1, e2)) == max(Q(3, 16)*e2, Q(3, 64)*e1),
                "Asymmetric residual formula changed")
    trajectories, saturation_events, residual_bound_attained = {}, {}, False
    for mode, one_step in (("ideal", Q(0)), ("bounded_readout_error", delta)):
        state = model.INITIAL_STATE
        budgets = model.iterate_error_budget(model.RATE, model.INITIAL_ERROR_BUDGET, [one_step]*STEPS)
        rows, saturated_count = [], 0
        for n in range(STEPS + 1):
            closed_form = model.RATE**n * model.INITIAL_ERROR_BUDGET + sum(
                model.RATE**k * one_step for k in range(n))
            require(budgets[n] == closed_form, "Residual recurrence and finite sum disagree")
            distances, limits = [], []
            for i, block in enumerate(state):
                check_density(density(block))
                distance = model.squared_trace_distance(block, model.FIXED_POINT[i])
                require(distance == matrix_distance_squared(block, model.FIXED_POINT[i]),
                        "Trajectory distance disagrees with matrix determinant")
                limit = (budgets[n] * model.WEIGHTS[i])**2
                require(distance <= limit, "Trajectory exceeded its exact weighted error budget")
                distances.append(distance)
                limits.append(limit)
                counts["trajectory_state_budget_checks"] += 1
            row = {"step": n, "bloch_states": state, "distance_squared_to_fixed_point": distances,
                   "weighted_distance_budget": budgets[n], "per_block_budget_squared": limits}
            if n < STEPS:
                proposed = (epsilon * (-1)**n, epsilon * (-1)**(n+1))
                errors = (tuple(model.clip_control(block[2] + error) - block[2]
                                for block, error in zip(state, proposed))
                          if mode == "bounded_readout_error" else (Q(0), Q(0)))
                require(all(abs(error) <= epsilon for error in errors), "Readout error bound violated")
                ideal = model.feedback_step(state)
                actual = model.feedback_step(state, measurement_errors=errors)
                require(all(-1 <= value <= 1 for value in actual["readouts"]),
                        "Example readout left the observable range")
                residual_squared = []
                for i, weight in enumerate(model.WEIGHTS):
                    squared = model.squared_trace_distance(actual["states"][i], ideal["states"][i])
                    require(squared <= (one_step * weight)**2, "One-step residual budget violated")
                    if mode == "bounded_readout_error" and squared == (one_step * weight)**2:
                        residual_bound_attained = True
                    residual_squared.append(squared)
                    counts["residual_one_step_block_checks"] += 1
                saturated_count += sum(actual["saturated"])
                row.update({"readout_errors": errors, "readouts": actual["readouts"],
                            "raw_controls": actual["raw_controls"], "controls": actual["controls"],
                            "saturated": actual["saturated"], "one_step_weighted_residual_bound": one_step,
                            "residual_distance_squared": residual_squared})
                state = actual["states"]
            rows.append(row)
        trajectories[mode] = rows
        saturation_events[mode] = saturated_count
    require(all(value > 0 for value in saturation_events.values()), "A trajectory never exercised clipping")
    require(residual_bound_attained, "The error sequence did not exercise the stated residual bound")

    normalized = tuple(tuple(value * model.WEIGHTS[j] / model.WEIGHTS[i]
                             for j, value in enumerate(row)) for i, row in enumerate(gain))
    require(normalized == ((Q(1, 4), Q(3, 8)), (Q(3, 8), Q(1, 4))), "Weighted graph normalization changed")
    path_rows = []
    for horizon in range(1, 9):
        result = path_multiplicity_bounds([normalized]*horizon, 2)
        direct = enumerate_matrix_paths([normalized]*horizon, 2)
        require((result["actual"], result["maximum"], result["counts"]) == direct,
                "Dynamic and exhaustive path calculations disagree")
        maximum = max(value for row in result["maximum"] for value in row)
        require(maximum == Q(3, 8)**horizon, "Max-times path rate changed")
        require(result["norm"] == Q(5, 8)**horizon, "Ordinary path-sum norm changed")
        require(result["norm"] > maximum, "Path sums were conflated with a largest path")
        require(result["norm"] <= result["row_bound"] <= result["coarse_bound"],
                "Multiplicity bound failed")
        path_rows.append({"horizon": horizon, "ordinary_product": result["actual"],
                          "maximum_path_products": result["maximum"], "path_counts": result["counts"],
                          "ordinary_row_norm": result["norm"], "maximum_single_path_weight": maximum,
                          "multiplicity_row_bound": result["row_bound"], "coarse_bound": result["coarse_bound"]})
        counts["path_horizons"] += 1

    invalid = [lambda: model.channel_step((2, 0, 0), 0),
               lambda: model.channel_step((0.0, 0, 0), 0),
               lambda: model.channel_step((True, 0, 0), 0),
               lambda: model.channel_step((0, 0), 0),
               lambda: model.channel_step((0, 0, 0), Q(5, 4)),
               lambda: model.channel_step((0, 0, 0), Q(-5, 4)),
               lambda: model.channel_step((0, 0, 0), 0, Q(-1, 4)),
               lambda: model.channel_choi(0, Q(5, 4)),
               lambda: model.channel_choi(float("nan")),
               lambda: model.feedback_step(()),
               lambda: model.feedback_step(model.INITIAL_STATE, graph=((1,),)),
               lambda: model.feedback_step(model.INITIAL_STATE, bias=(0,)),
               lambda: model.feedback_step(model.INITIAL_STATE, measurement_errors=(0,)),
               lambda: model.feedback_step(model.INITIAL_STATE, measurement_errors=(0.0, 0)),
               lambda: model.readout_error_budget((Q(-1, 100), 0)),
               lambda: model.readout_error_budget((0, 0), weights=(0, 1)),
               lambda: model.iterate_error_budget(-1, 1, []),
               lambda: model.iterate_error_budget(1, -1, []),
               lambda: model.iterate_error_budget(1, 1, [-1]),
               lambda: model.iterate_error_budget(.5, 1, [])]
    for case, operation in enumerate(invalid):
        try:
            operation()
        except (TypeError, ValueError):
            counts["invalid_domain_rejections"] += 1
        else:
            raise RuntimeError(f"Invalid-domain case {case} was accepted")

    artifacts = {"trajectories.json": exact_json({"steps_per_trajectory": STEPS, "trajectories": trajectories}),
                 "path-comparison.json": exact_json({"weighted_gain": normalized, "horizons": path_rows})}
    replays = []
    with tempfile.TemporaryDirectory(prefix="grh-quantum-gain-") as directory:
        for name, rate, exit_code, status in (("accepted", model.RATE, 0, "certified"),
                                            ("rejected", Q(3, 5), 2, "rejected")):
            witness = weighted_gain_witness(gain, model.WEIGHTS, rate)
            payload = json.dumps(witness, indent=2) + "\n"
            path = Path(directory) / (name + ".json")
            path.write_text(payload)
            run = subprocess.run([sys.executable, "-B", str(SOURCE_DIR / "check_weighted_gain_witness.py"), str(path)],
                                 text=True, capture_output=True, timeout=20)
            require(run.returncode == exit_code, "Independent gain replay returned the wrong exit code: " + run.stdout + run.stderr)
            replayed = json.loads(run.stdout)
            require(replayed["status"] == status and replayed["bound_holds"] == (exit_code == 0),
                    "Independent gain replay reported the wrong status")
            artifacts[f"gain-{name}.json"] = payload
            artifacts[f"gain-{name}-replay.json"] = run.stdout
            replays.append({"name": name, "proposed_rate": rate, "exit_code": run.returncode,
                            "status": status, "certifies_contraction": replayed["certifies_contraction"]})
            counts["independent_gain_replays"] += 1

    require(before == source_hashes(), "A checked source changed during verification")
    report = {
        "schema_version": 1, "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "seed": SEED, "arithmetic": "fractions.Fraction; exact rational complex matrix pairs",
        "execution": "classical standard-library CPU simulation; no training or quantum hardware",
        "state_domain": "tuple of separately accessible qubit ensemble density matrices with known Z expectations",
        "counts": counts,
        "channel_checks": {"retentions": retentions, "controls": controls, "state_fixtures": len(states),
                           "choi_convention": "unnormalized input tensor output; trace two; output partial trace identity",
                           "positivity_method": "nonnegative weighted rank-one decomposition and all exact principal minors"},
        "feedback": {"retention": model.RETENTION, "controller_graph": model.GRAPH, "bias": model.BIAS,
                     "gain_matrix": gain, "weights": model.WEIGHTS, "rate": model.RATE,
                     "unweighted_row_bound": Q(7, 4), "normalized_gain_matrix": normalized,
                     "fixed_point_bloch": model.FIXED_POINT, "initial_bloch": model.INITIAL_STATE,
                     "initial_weighted_trace_distance": model.INITIAL_ERROR_BUDGET,
                     "local_rate_attained": True, "sharpness_displaced_bloch": displaced,
                     "sharpness_input_weighted_distance": local_budget,
                     "pair_comparison": "actual trace distances via exact two-block squared-radical inequalities; no L1 relaxation",
                     "nonlinear_midpoint_z_gap": gap,
                     "semantics": "Fixed-control blocks are CPTP; state-dependent expectation feedback is not a single linear CPTP map."},
        "trajectories": {"steps_per_trajectory": STEPS, "states_per_trajectory": STEPS + 1,
                         "coherent_initial_block": "+Y", "saturation_events": saturation_events,
                         "distance_checks": "exact squared trace distances against squared nonnegative budgets"},
        "readout_error": {"epsilon_each_sensor": epsilon, "weighted_one_step_budget": delta,
                          "limsup_upper_bound": delta / (1 - model.RATE),
                          "one_step_bound_attained_in_example": residual_bound_attained,
                          "sequence": "alternating +/-epsilon proposed errors, readout clipped to [-1,1], actual error recorded",
                          "scope": "conditional deterministic error control; the limsup bound is not an attained-limit or finite-shot probability claim"},
        "tropical_comparison": {"maximum_single_path_rate": Q(3, 8), "ordinary_row_norm_rate": Q(5, 8),
                                "representation": "exact max-times products; logarithms not numerically evaluated"},
        "independent_gain_replays": replays,
        "source_sha256": before, "sources_unchanged_during_checks": True,
        "artifact_sha256": {name: hashlib.sha256(payload.encode()).hexdigest() for name, payload in artifacts.items()},
        "scope": "Finite exact implementation checks and replayed supplied-gain witnesses. The analytic channel/trace-distance envelope argument is separate; no complete Lean quantum formalization, finite-shot instrument, learned controller, fluid solver, speedup or hardware claim.",
    }
    return report, artifacts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        report, artifacts = run_checks()
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for name, payload in artifacts.items():
            (args.output_dir / name).write_text(payload)
        (args.output_dir / "verification.json").write_text(exact_json(report))
    except (OSError, TypeError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "failed", "error": str(error)}))
        return 1
    print(json.dumps({"status": report["status"], "counts": report["counts"],
                      "source_sha256": report["source_sha256"], "output_directory": str(args.output_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
