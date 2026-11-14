"""Exact checks for three localized qualifications to the reviewed ToricGT V text."""
from fractions import Fraction
import json
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][col]
        a[r] = [x / scale for x in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def checks():
    # Every nonnegative same-parity pair has the explicit displayed decomposition.
    pairs = 0
    for a in range(33):
        for b in range(33):
            if (a + b) % 2 == 0:
                k = a % 2
                i, j = (a-k)//2, (b-k)//2
                assert i >= 0 and j >= 0 and k >= 0
                assert (2*i+k, 2*j+k) == (a, b)
                pairs += 1
    boundary1 = [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]
    boundary2 = [[1], [1], [1]]
    assert all(sum(row[j] * boundary2[j][0] for j in range(3)) == 0
               for row in boundary1)
    circle = 3-rank(boundary1)
    disk = circle-rank(boundary2)
    assert (0, circle, disk) == (0, 1, 0)
    q_old, q_new = Fraction(1, 4), Fraction(1, 2)
    assert q_new/q_old == 2 and q_old/q_new == Fraction(1, 2)
    return {"schema": "quantum-toricgt-algebra-qualifications-v1", "passed": True,
            "normal_semigroup": {"generators": [[2,0],[0,2],[1,1]],
                "group_lattice": "a+b is even", "cone": "nonnegative quadrant",
                "tested_pairs": pairs, "excluded_candidate": [1,0],
                "general_proof": "Use k=0 for even/even, k=1 for odd/odd, then (a,b)=((a-k)/2)(2,0)+((b-k)/2)(0,2)+k(1,1)."},
            "homology_inclusions": {"boundary1": boundary1, "boundary2": boundary2,
                "boundary1_rank_over_Q": rank(boundary1),
                "boundary2_rank_over_Q": rank(boundary2),
                "betti1_point_circle_disk": [0, circle, disk]},
            "transfer_sign": {"q_old": str(q_old), "q_new": str(q_new),
                "log2_new_over_old": 1, "log2_old_over_new": -1,
                "positive_gain_convention": "log2(q_new/q_old)"}}


if __name__ == "__main__":
    result = checks()
    output = Path(__file__).parent / "results" / "algebra-checks.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
