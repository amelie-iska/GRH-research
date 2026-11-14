#!/usr/bin/env python3
"""Regression tests for exact gain witnesses and independent integer replay.

Run normally; the assertion-dependent parent transport verifier deliberately
refuses optimized imports. This suite separately runs the standalone replay
checker under ordinary Python, -O, -OO and both PYTHONOPTIMIZE settings.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction as Q
import hashlib
import json
from math import lcm
import os
from pathlib import Path
import platform
import random
import shutil
import subprocess
import sys
import tempfile
import unittest

import check_weighted_gain_witness as replay
import verify_toric_transport as producer


SEED = 20261114
RANDOM_CASES = 256


def encoded(value):
    value = Q(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def common_denominator_oracle(gain, weights, rate):
    """Decide each inequality by a single integer common denominator.

    This uses no Fraction sum/product/comparison and does not call either
    implementation's evaluation or rational-arithmetic helpers.
    """
    q, ws = Q(rate), [Q(value) for value in weights]
    for i, row in enumerate(gain):
        terms = [(Q(g).numerator * w.numerator, Q(g).denominator * w.denominator)
                 for g, w in zip(row, ws)]
        rhs = (q.numerator * ws[i].numerator, q.denominator * ws[i].denominator)
        denominator = lcm(rhs[1], *(term[1] for term in terms))
        left_integer = sum(numerator * (denominator // divisor)
                           for numerator, divisor in terms)
        right_integer = rhs[0] * (denominator // rhs[1])
        if left_integer > right_integer:
            return False
    return True


def poisoned_arithmetic(*args, **kwargs):
    raise RuntimeError("Custom scalar arithmetic must not be reached")


class PoisonInt(int):
    __mul__ = __rmul__ = __add__ = __radd__ = poisoned_arithmetic
    __lt__ = __le__ = __gt__ = __ge__ = poisoned_arithmetic


class PoisonFraction(Q):
    __mul__ = __rmul__ = __add__ = __radd__ = poisoned_arithmetic
    __lt__ = __le__ = __gt__ = __ge__ = poisoned_arithmetic


class WeightedGainTests(unittest.TestCase):
    randomized_cases_checked = 0
    scalar_rejection_cases = 0
    witness_mutation_cases = 0
    cli_cases_checked = 0

    def setUp(self):
        self.gain = [[0, 2], [Q(1, 8), 0]]
        self.weights = [4, 1]

    def witness(self, rate=Q(1, 2)):
        return producer.weighted_gain_witness(self.gain, self.weights, rate)

    def test_existing_exact_example_and_rejected_rate(self):
        self.assertTrue(producer.weighted_gain_certificate(self.gain, self.weights, Q(1, 2)))
        self.assertFalse(producer.weighted_gain_certificate(self.gain, self.weights, Q(2, 5)))
        accepted = self.witness()
        rejected = self.witness(Q(2, 5))
        self.assertEqual(accepted["row_lhs"], [encoded(2), encoded(Q(1, 2))])
        self.assertEqual(accepted["row_slack"], [encoded(0), encoded(0)])
        self.assertEqual(accepted["weighted_bound"], encoded(Q(1, 2)))
        self.assertEqual(rejected["row_slack"], [encoded(Q(-2, 5)), encoded(Q(-1, 10))])
        self.assertEqual(replay.replay_weighted_gain_witness(accepted)["status"], "certified")
        self.assertEqual(replay.replay_weighted_gain_witness(rejected)["status"], "rejected")

    def test_float_underflow_false_positive_is_rejected(self):
        gain, weight, rate = 1.01, 5e-324, .99
        # This equality is the actual binary64 collision behind the old bug.
        self.assertEqual(gain * weight, rate * weight)
        for function in (producer.weighted_gain_certificate, producer.weighted_gain_witness):
            with self.assertRaises(TypeError):
                function([[gain]], [weight], rate)
        exact = tuple(Q.from_float(value) for value in (gain, weight, rate))
        self.assertFalse(producer.weighted_gain_certificate([[exact[0]]], [exact[1]], exact[2]))
        self.assertEqual(replay.replay_weighted_gain_witness(
            producer.weighted_gain_witness([[exact[0]]], [exact[1]], exact[2]))["status"], "rejected")
        self.assertFalse(producer.weighted_gain_certificate(
            [[Q(101, 100)]], [Q(1, 10**324)], Q(99, 100)))

    def test_infinite_weight_false_positive_is_rejected(self):
        for function in (producer.weighted_gain_certificate, producer.weighted_gain_witness):
            with self.assertRaises(TypeError):
                function([[2]], [float("inf")], Q(1, 2))

    def test_inexact_and_custom_scalars_rejected_in_every_role(self):
        invalid = [.5, 0.0, 5e-324, float("nan"), float("inf"), -float("inf"),
                   True, False, Decimal("0.5"), complex(1), "1/2", None,
                   PoisonInt(1), PoisonFraction(1, 2)]
        for value in invalid:
            for role in ("gain", "weights", "rate"):
                for function in (producer.weighted_gain_certificate, producer.weighted_gain_witness):
                    gain, weights, rate = [[Q(1, 2)]], [1], 1
                    if role == "gain":
                        gain = [[value]]
                    elif role == "weights":
                        weights = [value]
                    else:
                        rate = value
                    with self.subTest(role=role, value_type=type(value).__name__, function=function.__name__):
                        with self.assertRaises(TypeError):
                            function(gain, weights, rate)
                        type(self).scalar_rejection_cases += 1

    def test_shape_and_sign_constraints(self):
        invalid = [([], [], 0), ([[]], [1], 1), ([[0, 0], [0]], [1, 1], 1),
                   ([[0, 0]], [1], 1), ([[0]], [], 1),
                   ([[-1]], [1], 1), ([[0]], [0], 1), ([[0]], [-1], 1),
                   ([[0]], [1], -1)]
        for inputs in invalid:
            for function in (producer.weighted_gain_certificate, producer.weighted_gain_witness):
                with self.subTest(inputs=inputs, function=function.__name__):
                    with self.assertRaises(ValueError):
                        function(*inputs)

    def test_integer_fraction_tuples_and_no_input_mutation(self):
        gain, weights = ((0, 2), (Q(1, 8), 0)), (4, Q(1))
        self.assertTrue(producer.weighted_gain_certificate(gain, weights, Q(1, 2)))
        original = deepcopy((self.gain, self.weights))
        self.witness()
        self.assertEqual((self.gain, self.weights), original)
        integer_witness = producer.weighted_gain_witness([[1, 0], [0, 1]], [2, 3], 1)
        self.assertTrue(replay.replay_weighted_gain_witness(integer_witness)["bound_holds"])

    def test_zero_and_noncontracting_rates(self):
        cases = [([[0]], 0, True, True), ([[1]], 1, True, False),
                 ([[1]], 2, True, False), ([[Q(1, 2)]], 2, True, False),
                 ([[1]], Q(1, 2), False, False)]
        for gain, rate, holds, contraction in cases:
            with self.subTest(gain=gain, rate=rate):
                record = producer.weighted_gain_witness(gain, [1], rate)
                checked = replay.replay_weighted_gain_witness(record)
                self.assertEqual(checked["bound_holds"], holds)
                self.assertEqual(checked["certifies_contraction"], contraction)

    def test_large_rationals_and_exact_boundary_separation(self):
        numerator = 10**1000 + 7
        denominator = 10**999 + 9
        weight = Q(numerator, denominator)
        boundary = Q(2**521 + 1, 2**523 + 3)
        epsilon = Q(1, 10**1000 + 31)
        for gain, expected in ((boundary, True), (boundary + epsilon, False)):
            record = producer.weighted_gain_witness([[gain]], [weight], boundary)
            checked = replay.replay_weighted_gain_witness(
                replay.load_weighted_gain_witness(json.dumps(record)))
            self.assertEqual(checked["bound_holds"], expected)
            self.assertEqual(common_denominator_oracle([[gain]], [weight], boundary), expected)

    def test_positive_weight_scaling_and_rate_monotonicity(self):
        factor = Q(2**257 + 1, 2**127 + 3)
        scaled = [factor * value for value in self.weights]
        for rate in (Q(1, 2), Q(3, 4), 1, 2):
            record = producer.weighted_gain_witness(self.gain, scaled, rate)
            self.assertEqual(record["row_bounds"], [encoded(Q(1, 2))] * 2)
            self.assertTrue(replay.replay_weighted_gain_witness(record)["bound_holds"])

    def test_seeded_cases_against_integer_common_denominator_oracle(self):
        rng = random.Random(SEED)
        for case in range(RANDOM_CASES):
            size = rng.randrange(1, 7)
            gain = [[Q(rng.randrange(17), rng.randrange(1, 23)) for _ in range(size)]
                    for _ in range(size)]
            weights = [Q(rng.randrange(1, 17), rng.randrange(1, 23)) for _ in range(size)]
            bound = max(sum(g * w for g, w in zip(row, weights)) / weights[i]
                        for i, row in enumerate(gain))
            rate = (bound, bound + Q(1, 17), bound / 2, Q(0))[case % 4]
            # Exercise both permitted exact scalar representations.
            gain = [[int(g) if g.denominator == 1 else g for g in row] for row in gain]
            with self.subTest(case=case, size=size):
                expected = common_denominator_oracle(gain, weights, rate)
                self.assertEqual(producer.weighted_gain_certificate(gain, weights, rate), expected)
                witness = producer.weighted_gain_witness(gain, weights, rate)
                checked = replay.replay_weighted_gain_witness(
                    replay.load_weighted_gain_witness(json.dumps(witness)))
                self.assertEqual(checked["bound_holds"], expected)
                self.assertEqual(checked["certifies_contraction"], expected and rate < 1)
                type(self).randomized_cases_checked += 1

    def test_every_input_and_derived_field_is_recomputed(self):
        mutations = [(["gain", 0, 1], encoded(3)), (["gain", 1, 0], encoded(Q(1, 4))),
                     (["weights", 0], encoded(5)), (["weights", 1], encoded(2)),
                     (["rate"], encoded(Q(3, 5))), (["row_lhs", 0], encoded(3)),
                     (["row_lhs", 1], encoded(0)),
                     (["row_rhs", 0], encoded(3)), (["row_slack", 0], encoded(1)),
                     (["row_rhs", 1], encoded(0)), (["row_slack", 1], encoded(1)),
                     (["row_bounds", 0], encoded(Q(3, 5))),
                     (["row_bounds", 1], encoded(0)),
                     (["weighted_bound"], encoded(Q(3, 5))),
                     (["bound_holds"], False), (["certifies_contraction"], False)]
        for path, value in mutations:
            witness = self.witness()
            target = witness
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = value
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    replay.replay_weighted_gain_witness(witness)
                type(self).witness_mutation_cases += 1

    def test_schema_shape_and_summary_types_are_strict(self):
        invalid = []
        for field in self.witness():
            witness = self.witness()
            del witness[field]
            invalid.append(witness)
        replacements = {"schema_version": [True, 1.0, 2], "kind": ["other", 1],
                        "gain": [[], [[encoded(0)]]], "weights": [[], [encoded(0), encoded(1)]],
                        "rate": [encoded(-1)], "bound_holds": [1], "certifies_contraction": [0]}
        for field, values in replacements.items():
            for value in values:
                witness = self.witness()
                witness[field] = value
                invalid.append(witness)
        witness = self.witness()
        witness["unrecognized"] = None
        invalid.append(witness)
        for i, witness in enumerate(invalid):
            with self.subTest(case=i):
                with self.assertRaises(ValueError):
                    replay.replay_weighted_gain_witness(witness)

    def test_noncanonical_rationals_are_rejected(self):
        invalid = [{"numerator": value, "denominator": "1"}
                   for value in ["00", "-0", "+1", " 1", "1 ", "1\n", "1e3", "1/2", "０", "", "-01", 1, True]]
        invalid += [{"numerator": "1", "denominator": value}
                    for value in ["0", "-1", "+1", "01", "1.0", "", 1, True]]
        invalid += [{"numerator": "2", "denominator": "4"},
                    {"numerator": "0", "denominator": "2"}, {"numerator": "1"},
                    {"numerator": "1", "denominator": "1", "extra": "0"},
                    {"numerator": "1" * (replay.MAX_INTEGER_DIGITS + 1), "denominator": "1"}]
        for i, value in enumerate(invalid):
            witness = self.witness()
            witness["row_lhs"][0] = value
            with self.subTest(case=i):
                with self.assertRaises(ValueError):
                    replay.replay_weighted_gain_witness(witness)

    def test_json_duplicate_float_and_resource_rejection(self):
        payload = json.dumps(self.witness())
        invalid = ['{"schema_version": 1, ' + payload[1:],
                   payload.replace('"numerator": "0"', '"numerator": "0", "numerator": "0"', 1),
                   '{"schema_version": 1.0}', '{"schema_version": 1e0}',
                   '{"rate": NaN}', '{"rate": Infinity}', '{"rate": -Infinity}',
                   b"\xff", " " * (replay.MAX_WITNESS_BYTES + 1)]
        for i, value in enumerate(invalid):
            with self.subTest(case=i):
                with self.assertRaises(ValueError):
                    replay.load_weighted_gain_witness(value)

    def test_standalone_cli_exit_codes_under_optimization(self):
        cases = [("holding", self.witness(), 0, "certified", True),
                 ("noncontracting", self.witness(1), 0, "certified", False),
                 ("rejected", self.witness(Q(2, 5)), 2, "rejected", False)]
        tampered = self.witness()
        tampered["row_slack"][0] = encoded(1)
        cases.append(("tampered", tampered, 1, "invalid", None))
        modes = [("ordinary", [], None), ("O", ["-O"], None), ("OO", ["-OO"], None),
                 ("env1", [], "1"), ("env2", [], "2")]
        with tempfile.TemporaryDirectory(prefix="grh-weighted-replay-") as directory:
            root = Path(directory)
            script = root / "check_weighted_gain_witness.py"
            # Only the replay checker is copied, so a producer import cannot
            # accidentally satisfy an alleged independent replay.
            shutil.copyfile(replay.__file__, script)
            for name, witness, exit_code, status, contraction in cases:
                path = root / (name + ".json")
                path.write_text(json.dumps(witness))
                for mode, flags, optimization in modes:
                    environment = os.environ.copy()
                    environment.pop("PYTHONOPTIMIZE", None)
                    environment.pop("PYTHONPATH", None)
                    environment["PYTHONDONTWRITEBYTECODE"] = "1"
                    if optimization is not None:
                        environment["PYTHONOPTIMIZE"] = optimization
                    with self.subTest(case=name, mode=mode):
                        run = subprocess.run([sys.executable, *flags, str(script), str(path)],
                                             cwd=root, env=environment, text=True, capture_output=True,
                                             timeout=20)
                        self.assertEqual(run.returncode, exit_code, run.stdout + run.stderr)
                        result = json.loads(run.stdout)
                        self.assertEqual(result["status"], status)
                        if contraction is not None:
                            self.assertEqual(result["certifies_contraction"], contraction)
                        type(self).cli_cases_checked += 1
            missing = subprocess.run([sys.executable, str(script), str(root / "absent.json")],
                                     cwd=root, text=True, capture_output=True, timeout=20)
            self.assertEqual(missing.returncode, 1)
            self.assertEqual(json.loads(missing.stdout)["status"], "invalid")
            type(self).cli_cases_checked += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    sources = [Path(__file__).resolve(), Path(producer.__file__).resolve(), Path(replay.__file__).resolve()]

    def source_hashes():
        return {str(path.relative_to(repo)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sources}

    before = source_hashes()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(WeightedGainTests)
    expected_methods = suite.countTestCases()
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    unchanged = before == source_hashes()
    success = (result.wasSuccessful() and not result.skipped and unchanged
               and result.testsRun == expected_methods
               and WeightedGainTests.randomized_cases_checked == RANDOM_CASES)
    report = {
        "schema_version": 1,
        "status": "passed" if success else "failed",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "test_methods_run": result.testsRun,
        "failures": len(result.failures), "errors": len(result.errors), "skipped": len(result.skipped),
        "seed": SEED,
        "randomized_exact_cases_checked": WeightedGainTests.randomized_cases_checked,
        "scalar_rejection_cases": WeightedGainTests.scalar_rejection_cases,
        "derived_field_mutation_cases": WeightedGainTests.witness_mutation_cases,
        "standalone_cli_cases_checked": WeightedGainTests.cli_cases_checked,
        "source_sha256": before,
        "sources_unchanged_during_tests": unchanged,
        "scope": "Exact finite weighted-gain input/replay regressions, including an independent "
                 "integer common-denominator oracle. No optimizer, model gain-envelope, "
                 "continuum or cryptographic certification.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
