#!/usr/bin/env python3
"""Exact bounded quiver diagnostics; not a certificate for GRH or all resolutions."""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json
from itertools import permutations


@dataclass(frozen=True)
class Quiver:
    name: str
    vertices: tuple
    arrows: tuple
    forbidden: frozenset


NODE = Quiver("node", (0,), (("x", 0, 0), ("y", 0, 0)),
              frozenset({("x", "y"), ("y", "x")}))
DUAL = Quiver("dual_numbers", (0,), (("x", 0, 0),),
              frozenset({("x", "x")}))
LINE = Quiver("radical_square_zero_length_two_line", (0, 1, 2),
              (("a", 0, 1), ("b", 1, 2)), frozenset({("a", "b")}))
# Critical example is the manuscript quiver with labels b and c exchanged.
CRITICAL = Quiver(
    "critical_two_vertex_four_arrow", (0, 1),
    (("a", 0, 1), ("b", 1, 0), ("c", 0, 1), ("d", 1, 0)),
    frozenset({("a", "d"), ("d", "c"), ("c", "b"), ("b", "a")}))
EXAMPLES = (NODE, DUAL, LINE, CRITICAL)
MAX_INTERNAL_DEGREE = 10
MAX_SERIES_DEGREE = 12
OUT = (Path(__file__).resolve().parents[1] / "outputs/checks/"
       "2026-11-03-projective/exact-quiver-checks.json")


def endpoints(quiver):
    return {a: (s, t) for a, s, t in quiver.arrows}


def target(quiver, start, word):
    return endpoints(quiver)[word[-1]][1] if word else start


def admissible(quiver, word, forbidden=False):
    ep = endpoints(quiver)
    return all(ep[a][1] == ep[b][0] and
               ((a, b) in quiver.forbidden) == forbidden
               for a, b in zip(word, word[1:]))


def paths(quiver, length, forbidden=False, source=None):
    """Travel-order words; stationary paths retain their vertex."""
    if length < 0:
        return []
    current = [(v, ()) for v in quiver.vertices if source is None or v == source]
    for _ in range(length):
        extended = []
        for v, word in current:
            end = target(quiver, v, word)
            for a, s, _t in quiver.arrows:
                if s == end and (not word or
                        ((word[-1], a) in quiver.forbidden) == forbidden):
                    extended.append((v, word + (a,)))
        current = extended
    return current


def zero(rows, columns):
    return [[F(0) for _ in range(columns)] for _ in range(rows)]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def multiply(a, b):
    """Used for nonempty square/transfer matrices, never zero-dimensional ones."""
    assert a and b and len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    """Exact rectangular rank, also for a zero-row or zero-column matrix."""
    if not a or not a[0]:
        return 0
    rows = [list(map(F, row)) for row in a]
    pivot = 0
    for column in range(len(rows[0])):
        found = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        c = rows[pivot][column]
        rows[pivot] = [v/c for v in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                c = rows[i][column]
                rows[i] = [u-c*v for u, v in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def determinant(a):
    """Leibniz formula is independent of the Gaussian inverse implementation."""
    n = len(a)
    assert all(len(row) == n for row in a)
    out = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = F((-1)**inversions)
        for i, j in enumerate(perm):
            term *= a[i][j]
        out += term
    return out


def inverse(a):
    n = len(a)
    rows = [list(map(F, row)) + identity(n)[i] for i, row in enumerate(a)]
    for column in range(n):
        pivot = next(i for i in range(column, n) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        c = rows[column][column]
        rows[column] = [v/c for v in rows[column]]
        for i in range(n):
            if i != column:
                c = rows[i][column]
                rows[i] = [u-c*v for u, v in zip(rows[i], rows[column])]
    result = [row[n:] for row in rows]
    assert multiply(a, result) == identity(n)
    return result


def resolution_basis(quiver, vertex, homological, internal):
    """A generator is a forbidden chain, followed by a permitted projective path.

    Right modules and travel-order paths are used here.  The chain generator
    has internal degree equal to its length.  There is no special-fiber step.
    """
    return [(chain, word) for _v, chain in
            paths(quiver, homological, forbidden=True, source=vertex)
            for _w, word in paths(quiver, internal-homological,
                                  source=target(quiver, vertex, chain))]


def differential(quiver, vertex, homological, internal):
    domain = resolution_basis(quiver, vertex, homological, internal)
    if homological == 0:
        codomain = [("simple", ())] if internal == 0 else []
        images = [0 if internal == 0 else None for _ in domain]
    else:
        codomain = resolution_basis(quiver, vertex, homological-1, internal)
        lookup = {basis: i for i, basis in enumerate(codomain)}
        images = []
        for chain, word in domain:
            new_word = (chain[-1],) + word
            if admissible(quiver, new_word):
                assert new_word  # All nonzero images lie in the arrow radical.
                images.append(lookup[(chain[:-1], new_word)])
            else:
                images.append(None)
    matrix = zero(len(codomain), len(domain))
    for j, image in enumerate(images):
        if image is not None:
            matrix[image][j] = F(1)
    return domain, codomain, images, matrix


def check_resolution(quiver):
    exactness = compositions = 0
    largest_basis = 0
    for vertex in quiver.vertices:
        for internal in range(MAX_INTERNAL_DEGREE+1):
            data = [differential(quiver, vertex, m, internal)
                    for m in range(internal+2)]
            for m in range(internal+1):
                domain, _codomain, images, matrix = data[m]
                next_domain, next_codomain, next_images, next_matrix = data[m+1]
                assert next_codomain == domain
                assert all(image is None or images[image] is None
                           for image in next_images), (quiver.name, vertex, internal, m)
                compositions += 1
                assert len(domain)-rank(matrix) == rank(next_matrix), (
                    quiver.name, vertex, internal, m, "nonzero homology")
                exactness += 1
                largest_basis = max(largest_basis, len(domain), len(next_domain))
            assert rank(data[0][3]) == int(internal == 0)
    return {"internal_degrees": [0, MAX_INTERNAL_DEGREE],
            "homological_degrees": "0..internal degree, including augmentation",
            "square_zero_checks": compositions, "exactness_checks": exactness,
            "largest_homogeneous_projective_basis": largest_basis}


def series(quiver, forbidden=False):
    n = len(quiver.vertices)
    vi = {v: i for i, v in enumerate(quiver.vertices)}
    result = []
    for degree in range(MAX_SERIES_DEGREE+1):
        matrix = zero(n, n)
        for source, word in paths(quiver, degree, forbidden):
            matrix[vi[source]][vi[target(quiver, source, word)]] += 1
        result.append(matrix)
    return result


def series_product(a, b):
    return [sum_matrices([multiply(a[j], b[d-j]) for j in range(d+1)])
            for d in range(MAX_SERIES_DEGREE+1)]


def sum_matrices(matrices):
    result = zero(len(matrices[0]), len(matrices[0][0]))
    for matrix in matrices:
        result = add(result, matrix)
    return result


def check_series(quiver):
    c = series(quiver)
    unsigned_ext = series(quiver, forbidden=True)
    signed_ext = [scale((-1)**d, m) for d, m in enumerate(unsigned_ext)]
    wanted = [identity(len(quiver.vertices))] + [
        zero(len(quiver.vertices), len(quiver.vertices))
        for _ in range(MAX_SERIES_DEGREE)]
    # Rows are sources and columns targets for BOTH series, so no transpose.
    assert series_product(signed_ext, c) == wanted
    assert series_product(c, signed_ext) == wanted
    if quiver == LINE:
        assert c[2] == zero(3, 3) and unsigned_ext[2][0][2] == 1
        assert unsigned_ext[3] == zero(3, 3)
    if quiver == NODE:
        assert c[0] == [[1]] and all(m == [[2]] for m in c[1:])
        assert all(m == [[2]] for m in unsigned_ext[1:])
        wrong = series_product(c, unsigned_ext)  # E(-q) when E already signed.
        assert wrong[1] == [[4]] and wrong != wanted
    return {"degree_through": MAX_SERIES_DEGREE,
            "signed_E_times_C_and_C_times_E_coefficients_checked":
                2*(MAX_SERIES_DEGREE+1)*len(quiver.vertices)**2,
            "permitted_path_counts": [int(sum(map(sum, m))) for m in c],
            "forbidden_chain_counts": [int(sum(map(sum, m))) for m in unsigned_ext]}


def successor_cycles(quiver, forbidden):
    """Primitive arrow cycles, each once; open successor chains contribute no factor."""
    ep = endpoints(quiver)
    successors = {}
    for a, _s, t in quiver.arrows:
        choices = [b for b, s, _t in quiver.arrows if s == t and
                   ((a, b) in quiver.forbidden) == forbidden]
        assert len(choices) <= 1
        if choices:
            successors[a] = choices[0]
    assert len(set(successors.values())) == len(successors)
    result = []
    visited = set()
    for start in ep:
        if start in visited:
            continue
        word = []
        current = start
        while current not in visited and current in successors:
            visited.add(current)
            word.append(current)
            current = successors[current]
        if current in word:
            result.append(tuple(word[word.index(current):]))
    return result


def cycle_product(cycles, weights, forbidden):
    result = F(1)
    for cycle in cycles:
        weight = F(1)
        for a in cycle:
            weight *= weights[a]
        result *= 1-((-1)**len(cycle) if forbidden else 1)*weight
    return result


def check_transfer(quiver):
    n, m = len(quiver.vertices), len(quiver.arrows)
    vi = {v: i for i, v in enumerate(quiver.vertices)}
    permitted_cycles = successor_cycles(quiver, False)
    forbidden_cycles = successor_cycles(quiver, True)
    samples = []
    for sample in range(3):
        weights = {a: (F(1, i+2) if sample == 0 else
                       F((-1)**i, i+3) if sample == 1 else
                       F(0) if i == 0 else F(1, i+2))
                   for i, (a, _s, _t) in enumerate(quiver.arrows)}
        t, u = zero(m, m), zero(m, m)
        start, end = zero(n, m), zero(m, n)
        for i, (a, source, target_) in enumerate(quiver.arrows):
            start[vi[source]][i] = weights[a]
            end[i][vi[target_]] = 1
            for j, (b, source_b, _target_b) in enumerate(quiver.arrows):
                if target_ == source_b:
                    (u if (a, b) in quiver.forbidden else t)[i][j] = weights[b]
        denominator = add(identity(m), scale(-1, t))
        numerator = add(identity(m), u)
        assert add(denominator, multiply(end, start)) == numerator
        cartan = add(identity(n), multiply(multiply(start, inverse(denominator)), end))
        transfer_value = determinant(numerator)/determinant(denominator)
        bh_value = (cycle_product(forbidden_cycles, weights, True) /
                    cycle_product(permitted_cycles, weights, False))
        assert determinant(denominator) == cycle_product(permitted_cycles, weights, False)
        assert determinant(numerator) == cycle_product(forbidden_cycles, weights, True)
        assert determinant(cartan) == transfer_value == bh_value
        if quiver == CRITICAL:
            assert len(permitted_cycles) == len(forbidden_cycles) == 1
            assert len(permitted_cycles[0]) == len(forbidden_cycles[0]) == 4
            assert determinant(numerator) == determinant(denominator)
            assert transfer_value == 1
        samples.append({"arrow_weights": {a: str(w) for a, w in weights.items()},
                        "det_C": str(determinant(cartan)),
                        "det_I_minus_permitted_transfer": str(determinant(denominator)),
                        "det_I_plus_forbidden_transfer": str(determinant(numerator)),
                        "BH_cycle_ratio": str(bh_value)})
    return {"permitted_primitive_arrow_cycles": permitted_cycles,
            "forbidden_primitive_arrow_cycles": forbidden_cycles,
            "rational_weight_samples": samples}


def block_diagonal(a, b):
    result = zero(len(a)+len(b), len(a[0])+len(b[0]))
    for i, row in enumerate(a):
        for j, v in enumerate(row):
            result[i][j] = v
    for i, row in enumerate(b):
        for j, v in enumerate(row):
            result[len(a)+i][len(a[0])+j] = v
    return result


def check_specialization_and_period():
    # Lambda = R[x]/(x^2-tx), y=t-x; at t=0, y=-x in dual numbers.
    x = [[F(0), F(0)], [F(1), F(0)]]
    minus_x = scale(-1, x)
    d1 = [rx+ry for rx, ry in zip(x, minus_x)]
    d2 = block_diagonal(minus_x, x)
    d3 = block_diagonal(x, minus_x)
    assert multiply(d1, d2) == zero(2, 4)
    assert multiply(d2, d3) == zero(4, 4)
    h = [2-rank(d1), 4-rank(d1)-rank(d2), 4-rank(d2)-rank(d3)]
    assert h == [1, 1, 0]  # Extra H1 = Tor^R_1(k,k), not an exact resolution.
    assert 2-rank(x) == 1 and 2-rank(x)-rank(x) == 0
    # The true special-fiber resolution has rank one, not two, in every degree.
    assert [len(paths(NODE, d, True)) for d in range(6)] == [1, 2, 2, 2, 2, 2]
    assert [len(paths(DUAL, d, True)) for d in range(6)] == [1, 1, 1, 1, 1, 1]
    forbidden_successor = {"x": "y", "y": "x"}
    pair = ("x", "y")
    next_pair = tuple(forbidden_successor[a] for a in pair)
    assert pair != next_pair and sorted(pair) == sorted(next_pair)
    assert tuple(forbidden_successor[a] for a in next_pair) == pair
    # Formal diagonal-word conjugation by the summand swap exchanges the maps.
    diag_words = (("x", "0"), ("0", "y"))
    swapped = tuple(tuple(diag_words[1-i][1-j] for j in range(2)) for i in range(2))
    assert swapped == (("y", "0"), ("0", "x"))
    return {"nonflat_node_specialization":
                {"central_parameter": "t=x+y", "order": "R[x]/(x^2-tx)",
                 "fiber": "k[x]/(x^2)", "reduced_complex_H0_H1_H2": h,
                 "true_fiber_resolution_positive_homology": 0,
                 "order_Betti_0_through_5": [1, 2, 2, 2, 2, 2],
                 "fiber_Betti_0_through_5": [1, 1, 1, 1, 1, 1]},
            "nodal_period": {"ordered_arm_period": 2, "unordered_syzygy_tail_period": 1,
                            "first_ordered_pair": pair, "next_ordered_pair": next_pair,
                            "meaning": "ungraded positive syzygy tail; NOT Omega^p(k)=k"},
            "double_sign_counterexample":
                {"correct_q_coefficient": 0, "double_signed_q_coefficient": 4,
                 "C": "(1+q)/(1-q)", "signed_E": "(1-q)/(1+q)"}}


def run():
    # First test: the empty path is an actual degree-zero basis vector.
    assert paths(NODE, 0) == [(0, ())]
    assert paths(NODE, 2) == [(0, ("x", "x")), (0, ("y", "y"))]
    assert paths(NODE, 2, forbidden=True) == [
        (0, ("x", "y")), (0, ("y", "x"))]
    assert rank([[1, 2], [2, 4]]) == 1 and rank([[], []]) == 0
    assert determinant([[F(1, 2), F(1, 3)], [F(2, 5), F(3, 7)]]) == F(17, 210)
    assert paths(DUAL, 2) == [] and paths(DUAL, 3, True) == [(0, ("x",)*3)]
    assert paths(LINE, 2) == [] and paths(LINE, 2, True) == [(0, ("a", "b"))]
    examples = {}
    for quiver in EXAMPLES:
        assert all(admissible(quiver, w) for _v, w in paths(quiver, 5))
        assert all(admissible(quiver, w, True) for _v, w in paths(quiver, 5, True))
        examples[quiver.name] = {
            "vertices": quiver.vertices, "arrows_source_target": quiver.arrows,
            "forbidden_adjacent_travel_pairs": sorted(quiver.forbidden),
            "resolution": check_resolution(quiver),
            "series": check_series(quiver),
            "transfer_and_BH": check_transfer(quiver)}
    result = {
        "arithmetic": "exact integers and fractions.Fraction; deterministic; no randomness",
        "conventions":
            "right modules; arrows/words in travel order; matrices source-row/target-column; "
            "generator degree m in resolution degree m; E already includes (-1)^m",
        "bounds": {"maximum_internal_degree": MAX_INTERNAL_DEGREE,
                   "maximum_series_degree": MAX_SERIES_DEGREE,
                   "rational_weight_samples_per_quiver": 3},
        "manuscript_critical_arrow_to_checker": {"a": "a", "b": "c", "c": "b", "d": "d"},
        "examples": examples, "counterexamples": check_specialization_and_period(),
        "totals": {
            "homogeneous_exactness_checks": sum(x["resolution"]["exactness_checks"]
                                               for x in examples.values()),
            "homogeneous_d_squared_zero_checks": sum(x["resolution"]["square_zero_checks"]
                                                    for x in examples.values()),
            "signed_series_scalar_coefficients": sum(
                x["series"]["signed_E_times_C_and_C_times_E_coefficients_checked"]
                for x in examples.values()),
            "rational_transfer_BH_samples": 3*len(EXAMPLES)},
        "scope":
            "Finite exact diagnostics for the four stated monomial quivers and rational "
            "weights; each tested internal degree includes all its homological terms. "
            "Not a universal resolution theorem, a theorem about arbitrary completed or "
            "mixed-characteristic orders, analytic determinant identification, or RH/GRH."}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"output": str(OUT), "totals": result["totals"],
                      "scope": result["scope"]}, indent=2))


if __name__ == "__main__":
    run()
