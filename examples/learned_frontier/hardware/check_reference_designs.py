"""Independent integer oracles and deliberate wrong implementations.

Run with Python >= 3.10, standard library only. --output creates a NEW file.
No asserts are used: checks remain enabled under python -O.
"""
import argparse
import dataclasses
import datetime
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys

from fixed import Format
from maxplus_tile import backward_wide, reduce_pairs, tile
from mixed_scheduler import Job, execute, schedule
from readout_controller import Calibration, ReadoutController


def run():
    checks, negatives = {}, {}
    def require(condition, message):
        if not condition:
            raise AssertionError(message)

    def rejects(call, error=ValueError):
        try:
            call()
        except error:
            return True
        return False

    f = Format()
    for bits in range(256):
        require(f.encode(f.decode(bits)) == bits, "two's complement round trip")
    checks["two_complement_all_8bit_patterns"] = 256
    count = 0
    for a, b in itertools.product(range(-128, 128), repeat=2):
        c = reduce_pairs([a], [b], [True], f)
        exact = a + b
        expected = -128 if exact < -128 else 127 if exact > 127 else exact
        require((c.raw, c.wide, c.overflow, c.winner, c.valid) ==
                (expected, exact, exact < -128 or exact > 127, 0, True),
                "exhaustive widened addition")
        count += 1
    checks["all_signed_8bit_additions"] = count
    count = 0
    f4 = Format(4, 2)
    for vals in itertools.product(range(-8, 8), repeat=4):
        a, b, c, d = vals
        for mask in ((False, False), (True, False), (False, True), (True, True)):
            result = reduce_pairs([a, b], [c, d], mask, f4)
            candidates = [(a + c, 0), (b + d, 1)]
            permitted = [entry for entry, valid in zip(candidates, mask) if valid]
            if permitted:
                # Sorting independently defines the largest term, lowest index.
                exact, winner = sorted(permitted, key=lambda t: (-t[0], t[1]))[0]
                require((result.wide, result.winner, result.valid) ==
                        (exact, winner, True), "two-lane winner/mask")
            else:
                require(dataclasses.asdict(result) ==
                        dict(raw=0, valid=False, winner=None, overflow=False, wide=None),
                        "all-mask identity")
            count += 1
    checks["all_4bit_two_lane_masks_and_winners"] = count
    rng = random.Random(20261104)
    for _ in range(300):
        scores = [[rng.randrange(-128, 128) for _ in range(3)] for _ in range(2)]
        values = [[rng.randrange(-128, 128) for _ in range(2)] for _ in range(3)]
        masks = [[rng.choice((False, True)) for _ in range(3)] for _ in range(2)]
        qvalid = [rng.choice((False, True)) for _ in range(2)]
        cells = tile(scores, values, masks, qvalid)
        for i in range(2):
            for k in range(2):
                permitted = [(scores[i][j] + values[j][k], j)
                             for j in range(3) if qvalid[i] and masks[i][j]]
                expected = sorted(permitted, key=lambda t: (-t[0], t[1]))
                require(cells[i][k].valid == bool(expected), "random valid")
                if expected:
                    require((cells[i][k].wide, cells[i][k].winner) == expected[0],
                            "random tile oracle")
    checks["random_masked_tiles_seed_20261104"] = 300
    # Subgradient and independent finite difference at a unique winner, no clip.
    scores, values = [[2, 5]], [[1, 4], [8, -2]]
    cells = tile(scores, values, [[True, True]], [True])
    ds, dv = backward_wide(cells, [[3, 7]], 2)
    require(ds == [[7, 3]] and dv == [[0, 7], [3, 0]], "VJP routing")
    for j in range(2):
        shifted = [scores[0][:]]
        shifted[0][j] += 1
        changed = tile(shifted, values, [[True, True]], [True])
        derivative = sum(g * (changed[0][k].wide - cells[0][k].wide)
                         for k, g in enumerate((3, 7)))
        require(derivative == ds[0][j], "integer finite-difference VJP")
    ties = tile([[1, 1]], [[2], [2]], [[True, True]], [True])
    require(backward_wide(ties, [[5]], 2) == ([[5, 0]], [[5], [0]]), "tie VJP")
    require(rejects(lambda: backward_wide(
        tile([[120]], [[120]], [[True]], [True]), [[1]], 1)), "clip VJP reject")
    checks["backward_unique_tie_and_clip_policy"] = True

    # Negative controls must demonstrably disagree with the correct contract.
    correct = reduce_pairs([-10], [-6], [True]).raw
    negatives["zero_as_minus_infinity"] = correct != max(0, -10 - 6)
    correct = reduce_pairs([120, 30], [120, 30], [True, True])
    wrong = max(f.decode((x + y) & 255) for x, y in zip([120, 30], [120, 30]))
    negatives["wrapped_sum_before_max"] = correct.raw != wrong
    correct = reduce_pairs([100, 120], [40, 30], [True, True])
    negatives["saturation_before_winner"] = correct.winner != 0
    # Average/softmax aggregation is not max-plus aggregation.
    negatives["arithmetic_mean_substitution"] = reduce_pairs(
        [0, 0], [0, 16], [True, True]).raw != 8

    jobs = []
    for _ in range(200):
        n = rng.randrange(0, 9)
        jobs.append(Job(rng.choice(("MAC", "MAXPLUS")),
                        tuple(rng.randrange(-128, 128) for _ in range(n)),
                        tuple(rng.randrange(-128, 128) for _ in range(n)),
                        tuple(rng.choice((False, True)) for _ in range(n))))
    for job in jobs:
        active = [(a, b, j) for j, (a, b, v) in enumerate(
                  zip(job.a, job.b, job.mask)) if v]
        got = execute(job)
        if job.op == "MAC":
            exact = sum(a * b for a, b, _ in active) // 16
            require(got["multiplies"] == len(active), "MAC operation count")
        else:
            exact = max((a + b for a, b, _ in active), default=0)
            require(got["multiplies"] == 0 and got["adds"] == len(active) and
                    got["compares"] == max(0, len(active) - 1), "max-plus counts")
        require(got["raw"] == min(127, max(-128, exact)) and
                got["valid"] == bool(active) and
                got["overflow"] == (exact < -128 or exact > 127), "operation oracle")
    for capacity in (1, 2, 4):
        simulation = schedule(jobs, (True, False, False, True, False), capacity)
        require(simulation["outputs"] == [(i, execute(j)) for i, j in enumerate(jobs)],
                "ordered retirement after backpressure")
        require(all(0 <= t["occupancy"] <= capacity for t in simulation["trace"]),
                "bounded completion buffer")
        launched = [t["launch"] for t in simulation["trace"] if t["launch"] is not None]
        finished = [i for t in simulation["trace"] for i in t["finish"]]
        require(launched == list(range(len(jobs))) and sorted(finished) == launched,
                "no lost or duplicate jobs")
    small = [Job("MAC", (16,), (16,), (True,)),
             Job("MAXPLUS", (1,), (2,), (True,))]
    sim = schedule(small, latencies={"MAC": 5, "MAXPLUS": 1})
    finish_order = [i for t in sim["trace"] for i in t["finish"]]
    require(finish_order == [1, 0] and [i for i, _ in sim["outputs"]] == [0, 1],
            "out-of-order completion requires ordered retirement")
    require(rejects(lambda: schedule(small, (False,), max_cycles=12), TimeoutError),
            "permanent backpressure times out")
    mac = Job("MAC", (1, 1), (8, 8), (True, True))
    negatives["per_product_rounding"] = execute(mac)["raw"] != sum(
        (a * b) >> 4 for a, b in zip(mac.a, mac.b))
    negatives["negative_truncation_toward_zero"] = execute(
        Job("MAC", (-1,), (1,), (True,)))["raw"] != int(-1 / 16)
    checks["mixed_jobs_three_buffer_sizes"] = {"jobs": 200, "capacities": [1, 2, 4],
                                               "ready": [True, False, False, True, False]}
    checks["completion_reordering_and_permanent_backpressure"] = True

    cal = Calibration(7, 8, -4, 0, 0, 2)
    ctrl = ReadoutController(cal, max_samples=4)
    positive = ctrl.decide([(8, 0, True)] * 4, 7, 20, 23)
    negative = ctrl.decide([(-8, 0, True)] * 4, 7, 20, 23)
    require(positive["action"] == "RESET_REQUEST" and positive["score_raw"] == 16,
            "positive digital discrimination")
    require(negative["valid"] and negative["action"] == "HOLD" and
            negative["score_raw"] == -16, "negative digital discrimination")
    for name, samples, epoch, deadline, reason in [
        ("empty", [(0, 0, False)], 7, 23, "empty_frame"),
        ("overrun", [(8, 0, True)] * 5, 7, 23, "sample_overrun"),
        ("stale", [(8, 0, True)] * 4, 6, 23, "stale_calibration"),
        ("deadline", [(8, 0, True)] * 4, 7, 22, "deadline_miss"),
        ("low_margin", [(0, 0, True)], 7, 23, "low_margin"),
        ("clip", [(127, -128, True)] * 4, 7, 23, "score_saturated"),
    ]:
        got = ctrl.decide(samples, epoch, 20, deadline)
        require(not got["valid"] and got["action"] == "HOLD" and
                reason in got["reasons"], name + " fail closed")
        negatives["readout_bypass_" + name] = got["action"] != "RESET_REQUEST"
    boundary_count = 0
    for n in range(1, 34):
        c = ReadoutController(cal, max_samples=n)
        for value in (-128, 127):
            out = c.decide([(value, value, True)] * n, 7, 0, 100)
            require(out["sum_i"] == n * value and
                    -(1 << (c.acc_width - 1)) <= out["sum_i"] < 1 << (c.acc_width - 1),
                    "accumulator guard bits")
            boundary_count += 1
    checks["readout_guard_cases"] = 6
    checks["readout_accumulator_boundaries"] = boundary_count
    malformed = [lambda: Format(1, 0), lambda: f.check(128),
                 lambda: reduce_pairs([0], [], [True]),
                 lambda: reduce_pairs([0], [0], [1]),
                 lambda: tile([[0]], [[0]], [[1]], [False]),
                 lambda: execute(Job("BAD", (), (), ())),
                 lambda: schedule([], ready=()),
                 lambda: ReadoutController(dataclasses.replace(cal, action_above="ANY_PULSE")),
                 lambda: ctrl.decide([(0, 0, 1)], 7, 0, 10)]
    require(all(rejects(call) for call in malformed), "malformed request rejection")
    checks["malformed_inputs_rejected"] = len(malformed)
    require(all(negatives.values()), "a deliberate wrong implementation survived")
    here = Path(__file__).resolve().parent
    return {"schema_version": 1, "status": "pass",
            "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "python": sys.version, "seed": 20261104,
            "format": {"width": 8, "fraction_bits": 4, "signed": True,
                       "rounding_mac": "arithmetic shift/floor; saturate once at output"},
            "checks": checks, "negative_controls_detected": negatives,
            "reference_trace": {"out_of_order_schedule": sim, "readout": positive},
            "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in sorted(here.glob("*.py"))},
            "limitations": ["Integer Python specification; no RTL simulation/synthesis/PPA",
                            "No FPGA, ASIC, quantum-device or pulse execution",
                            "Synthetic readout; no measured fidelity or quantum advantage",
                            "Reference VJP is unsaturated integer subgradient, not QAT",
                            "No universal training/hardware speedup or GRH implication"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    if args.output:
        # Refuse to overwrite prior experiment evidence.
        with args.output.open("x") as stream:
            json.dump(report, stream, indent=2)
            stream.write("\n")
    print(json.dumps(report, indent=2))
