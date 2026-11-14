"""Candidate B: two functional units with a bounded, ordered completion buffer.

Abstract cycles/latencies are chosen model parameters, not measured hardware.
MAC: exact wide dot -> arithmetic right shift frac -> signed W saturation.
MAXPLUS: widened sums -> masked max -> saturation. Empty valid set is invalid.
"""
from dataclasses import dataclass
from fixed import Format
from maxplus_tile import reduce_pairs


@dataclass(frozen=True)
class Job:
    op: str
    a: tuple
    b: tuple
    mask: tuple


def execute(job, fmt=Format()):
    if job.op not in ("MAC", "MAXPLUS"):
        raise ValueError("unknown opcode")
    if not len(job.a) == len(job.b) == len(job.mask):
        raise ValueError("job lane lengths differ")
    for x, y, valid in zip(job.a, job.b, job.mask):
        fmt.check(x)
        fmt.check(y)
        if type(valid) is not bool:
            raise ValueError("mask must contain bools")
    n = sum(job.mask)
    if job.op == "MAXPLUS":
        c = reduce_pairs(job.a, job.b, job.mask, fmt)
        return {"raw": c.raw, "valid": c.valid, "overflow": c.overflow,
                "winner": c.winner, "adds": n, "multiplies": 0,
                "compares": max(0, n - 1)}
    wide = sum(x * y for x, y, v in zip(job.a, job.b, job.mask) if v)
    # Python >> is floor division for negative integers, matching signed ASR.
    raw, overflow = fmt.sat(wide >> fmt.frac)
    return {"raw": raw, "valid": n > 0, "overflow": overflow,
            "winner": None, "adds": max(0, n - 1), "multiplies": n,
            "compares": 0}


def schedule(jobs, ready=(True,), capacity=4, latencies=None, fmt=Format(),
             max_cycles=100000):
    if capacity < 1 or not ready or any(type(x) is not bool for x in ready):
        raise ValueError("invalid buffer capacity or ready pattern")
    latencies = {"MAC": 3, "MAXPLUS": 2} if latencies is None else latencies
    if set(latencies) != {"MAC", "MAXPLUS"} or any(
            type(x) is not int or x < 1 for x in latencies.values()):
        raise ValueError("latencies must be positive integer cycles")
    # Validate even jobs that would otherwise be stuck behind backpressure.
    answers = [execute(job, fmt) for job in jobs]
    inflight, complete, launched, retired, trace, outputs = {}, {}, 0, 0, [], []
    for cycle in range(max_cycles):
        events = {"cycle": cycle, "finish": [], "retire": None, "launch": None}
        for op, (due, seq) in list(inflight.items()):
            if due == cycle:
                complete[seq] = answers[seq]
                events["finish"].append(seq)
                del inflight[op]
        if ready[cycle % len(ready)] and retired in complete:
            outputs.append((retired, complete.pop(retired)))
            events["retire"] = retired
            retired += 1
        if launched < len(jobs) and launched - retired < capacity:
            op = jobs[launched].op
            if op not in inflight:
                inflight[op] = (cycle + latencies[op], launched)
                events["launch"] = launched
                launched += 1
        events["occupancy"] = launched - retired
        trace.append(events)
        if retired == len(jobs):
            return {"outputs": outputs, "trace": trace,
                    "abstract_cycles": cycle + 1, "latencies": latencies,
                    "capacity": capacity}
    raise TimeoutError("bounded reference simulation did not drain")


if __name__ == "__main__":
    jobs = [Job("MAC", (16, -16), (16, 8), (True, True)),
            Job("MAXPLUS", (-10, -5), (-6, -7), (True, True))]
    print(schedule(jobs, ready=(True, False))["outputs"])
