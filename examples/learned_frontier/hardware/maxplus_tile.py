"""Candidate A: streaming, masked max-plus attention aggregation.

Inputs already contain scores: QK projection/scoring is outside this tile.
Scores and values are signed W-bit raw Q-format integers. Addition and
comparison use W+1 bits; saturation occurs only AFTER the winner is selected.
No numerical sentinel represents minus infinity: every entry has a valid bit.
"""
from dataclasses import dataclass
from fixed import Format


@dataclass(frozen=True)
class Cell:
    raw: int
    valid: bool
    winner: int | None
    overflow: bool
    wide: int | None


def reduce_pairs(a, b, mask, fmt=Format()):
    if not len(a) == len(b) == len(mask):
        raise ValueError("parallel lane lengths differ")
    best, winner = None, None
    for j, (x, y, valid) in enumerate(zip(a, b, mask)):
        fmt.check(x)
        fmt.check(y)
        if type(valid) is not bool:
            raise ValueError("mask must contain bools")
        if valid:
            term = x + y
            if best is None or term > best:  # earliest index wins a tie
                best, winner = term, j
    if best is None:
        return Cell(0, False, None, False, None)
    raw, overflow = fmt.sat(best)
    return Cell(raw, True, winner, overflow, best)


def tile(scores, values, legal, query_valid, fmt=Format()):
    n = len(values)
    d = len(values[0]) if n else 0
    if any(len(row) != d for row in values):
        raise ValueError("ragged values")
    if not len(scores) == len(legal) == len(query_valid):
        raise ValueError("query axes differ")
    result = []
    for row, mask, qvalid in zip(scores, legal, query_valid):
        if len(row) != n or len(mask) != n or type(qvalid) is not bool:
            raise ValueError("invalid query shape/validity")
        if any(type(v) is not bool for v in mask):
            raise ValueError("mask must contain bools")
        effective = [qvalid and v for v in mask]
        result.append([reduce_pairs(row, [values[j][k] for j in range(n)],
                                    effective, fmt) for k in range(d)])
    return result


def backward_wide(cells, upstream, nkeys):
    """Exact integer VJP of unsaturated maximum; reject clipped-output gradients.

    Select earliest-index subgradient at a true tie. Gradient accumulators here
    are unbounded mathematical integers; a training ASIC must size or saturate
    them separately. This is not differentiation through quantization.
    """
    if nkeys < 0 or len(cells) != len(upstream):
        raise ValueError("invalid gradient shape")
    d = len(cells[0]) if cells else 0
    ds, dv = [[0] * nkeys for _ in cells], [[0] * d for _ in range(nkeys)]
    for i, (row, grad) in enumerate(zip(cells, upstream)):
        if len(row) != d or len(grad) != d:
            raise ValueError("invalid gradient feature axis")
        for k, (cell, g) in enumerate(zip(row, grad)):
            if type(g) is not int:
                raise ValueError("integer upstream gradient required")
            if cell.overflow:
                raise ValueError("clipped result: choose an explicit quantization VJP")
            if cell.valid:
                if cell.winner is None or not 0 <= cell.winner < nkeys:
                    raise ValueError("invalid witness")
                ds[i][cell.winner] += g
                dv[cell.winner][k] += g
    return ds, dv


if __name__ == "__main__":
    print(tile([[-6, -3, 100]], [[-4, 2], [-2, -3], [100, 100]],
               [[True, True, False]], [True]))
