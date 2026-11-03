#!/usr/bin/env python3
"""Exact finite diagnostics for the dessin graph and diagonal-fiber models.

Only run() writes, and only to outputs/checks/2026-11-03-gluing/exact-checks.json.
Fock inputs have bounded length; outputs are never projected or truncated.
Circle tests use Gaussian rationals, not floating point. These tests do not
prove an infinite C*-generation, graph uniqueness, or arithmetic theorem.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/checks/2026-11-03-gluing/exact-checks.json"
MAX_PATH = 8
SOURCE = ROOT / "research/literature/pullback-extension-20261103/1907.10260v3.pdf"
SOURCE_SHA256 = "9f5c3e023e4333bd20cb8305dc53fd7cbcd62555f58647a1ff0ea050e3a97436"


def load_extension():
    path = ROOT / "scripts/check_dessin_extension.py"
    spec = importlib.util.spec_from_file_location("dessin_gluing_helper", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


D = load_extension()


@dataclass(frozen=True)
class Gaussian:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Gaussian) else Gaussian(F(value))

    def __add__(self, other):
        other = self.coerce(other)
        return Gaussian(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.re, -self.im)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        return Gaussian(self.re*other.re - self.im*other.im,
                        self.re*other.im + self.im*other.re)

    __rmul__ = __mul__

    def conjugate(self):
        return Gaussian(self.re, -self.im)

    def __truediv__(self, other):
        other = self.coerce(other)
        norm = other.re**2 + other.im**2
        if not norm:
            raise ZeroDivisionError("zero Gaussian rational")
        value = self * other.conjugate()
        return Gaussian(value.re/norm, value.im/norm)

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer, base = Gaussian(F(1)), self
        while n:
            if n % 2:
                answer = answer * base
            base = base * base
            n //= 2
        return answer

    def __bool__(self):
        return bool(self.re or self.im)

    def json(self):
        return {"real": str(self.re), "imaginary": str(self.im)}


ONE = Gaussian(F(1))
SAMPLES = (Gaussian(F(-1)), Gaussian(F(0), F(1)), Gaussian(F(0), F(-1)))


def matrix_unit(i, j, value=ONE):
    value = Gaussian.coerce(value)
    return {(i, j): value} if value else {}


def matrix_add(a, b):
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, Gaussian()) + value
        if not result[key]:
            del result[key]
    return result


def matrix_scale(value, a):
    value = Gaussian.coerce(value)
    return {key: value*x for key, x in a.items() if value*x}


def matrix_mul(a, b):
    result = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            if j == k:
                key = (i, l)
                result[key] = result.get(key, Gaussian()) + x*y
                if not result[key]:
                    del result[key]
    return result


def diagonal(a):
    return {key: value for key, value in a.items() if key[0] == key[1]}


def sparse_json(a):
    return [[i, j, value.json()] for (i, j), value in sorted(a.items())]


def smith_by_minors(a):
    """Small exact determinantal divisors, including rectangular/zero matrices."""
    rank = D.rank(a)
    previous, entries = 1, []
    for n in range(1, rank + 1):
        divisor = 0
        for rows in combinations(range(len(a)), n):
            for cols in combinations(range(len(a[0])), n):
                minor = D.det([[a[i][j] for j in cols] for i in rows])
                assert minor.denominator == 1
                divisor = math.gcd(divisor, abs(int(minor)))
        assert divisor and divisor % previous == 0
        entries.append(divisor // previous)
        previous = divisor
    return entries


def smith_with_unit_reduction(a):
    """Unimodular integer unit pivots, then minor gcds on the small remainder."""
    b = [list(map(int, row)) for row in a]
    rows, cols, k = len(b), len(b[0]), 0
    while k < min(rows, cols):
        pivot = next(((i, j) for i in range(k, rows) for j in range(k, cols)
                      if abs(b[i][j]) == 1), None)
        if pivot is None:
            break
        i, j = pivot
        b[k], b[i] = b[i], b[k]
        for row in b:
            row[k], row[j] = row[j], row[k]
        if b[k][k] == -1:
            b[k] = [-x for x in b[k]]
        for i in range(k + 1, rows):
            coefficient = b[i][k]
            b[i] = [x - coefficient*y for x, y in zip(b[i], b[k])]
        for j in range(k + 1, cols):
            coefficient = b[k][j]
            for i in range(rows):
                b[i][j] -= coefficient*b[i][k]
        k += 1
    assert all(b[i][j] == int(i == j)
               for i in range(k) for j in range(cols))
    assert all(b[i][j] == 0 for i in range(k, rows) for j in range(k))
    remainder = [row[k:] for row in b[k:]]
    tail = smith_by_minors(remainder)
    assert k + len(tail) == D.rank(a)
    entries = [1]*k + tail
    assert all(y % x == 0 for x, y in zip(entries, entries[1:]))
    return entries, k, remainder


def graph_relation_checks(d):
    tau, edge = d["allowed"], d["edge"]
    m, e = len(tau), len(d["quiver"].vertices)
    cycles = D.cycles(tau)
    # Vertex order: arrow states first, then vacuum sinks. Columns: regular states.
    relation = [[0]*m for _ in range(m + e)]
    graph_edges = []
    for h in range(m):
        relation[h][h] += 1
        relation[tau[h]][h] -= 1
        relation[m + edge[tau[h]]][h] -= 1
        graph_edges.extend(((h, tau[h]), (h, m + edge[tau[h]])))
    incidence = [[sum(edge[h] == v for h in cycle) for cycle in cycles]
                 for v in range(e)]
    for j, cycle in enumerate(cycles):
        total = [sum(row[h] for h in cycle) for row in relation]
        assert total == [0]*m + [-incidence[v][j] for v in range(e)]
    graph_smith, units, remainder = smith_with_unit_reduction(relation)
    incidence_smith = smith_by_minors(incidence)
    rg, ri = D.rank(relation), D.rank(incidence)
    assert rg == m - len(cycles) + ri
    assert [x for x in graph_smith if x > 1] == [x for x in incidence_smith if x > 1]
    assert m - rg == len(cycles) - ri
    assert m + e - rg == e + len(cycles) - ri
    return {"state_vertices": m, "vacuum_sinks": e,
            "graph_edges_source_target": graph_edges,
            "regular_vertex_relation_matrix": relation,
            "unsigned_incidence_matrix": incidence,
            "cycle_column_sum_identities": len(cycles),
            "graph_relation_Smith_nonzero_diagonal": graph_smith,
            "incidence_Smith_nonzero_diagonal": incidence_smith,
            "integer_unit_pivots": units, "residual_matrix_for_minor_gcds": remainder,
            "K0_free_rank": m + e - rg,
            "K0_torsion_orders": [x for x in graph_smith if x > 1],
            "K1_free_rank": m - rg,
            "scope": "Exact relation-matrix diagnostics; graph-algebra K-theory theorem is external."}


def fock_graph_checks(d):
    tau, edge, q = d["allowed"], d["edge"], d["quiver"]
    m, e = len(tau), len(q.vertices)
    endpoints = {h: (s, t) for h, (_name, s, t) in enumerate(q.arrows)}
    basis = [(v, tuple(map(int, word))) for n in range(MAX_PATH + 1)
             for v, word in D.H.paths(q, n)]
    graph_edges = [(h, exit_) for h in range(m) for exit_ in (False, True)]

    def vertex(v, p):
        if p is None:
            return None
        support = (p[1] and p[1][0] == v) if v < m else (not p[1] and p[0] == v-m)
        return p if support else None

    def prefix(h, p):
        if p is None or p[0] != endpoints[h][1]:
            return None
        if p[1] and p[1][0] != tau[h]:
            return None
        return endpoints[h][0], (h,) + p[1]

    def deletion(h, p):
        if p is None or not p[1] or p[1][0] != h:
            return None
        return endpoints[h][1], p[1][1:]

    def target(a):
        h, exit_ = a
        return m + edge[tau[h]] if exit_ else tau[h]

    def action(a, p):
        return prefix(a[0], vertex(target(a), p))

    def adjoint(a, p):
        return vertex(target(a), deletion(a[0], p))

    counts = {"vertex_orthogonality": 0, "vertex_partition_of_unity": 0,
              "graph_CK1": 0, "regular_vertex_CK2": 0,
              "source_range": 0, "creator_and_adjoint_reconstruction": 0}
    largest_output = 0
    for p in basis:
        assert sum(vertex(v, p) is not None for v in range(m + e)) == 1
        counts["vertex_partition_of_unity"] += 1
        for v, w in product(range(m + e), repeat=2):
            assert vertex(v, vertex(w, p)) == (vertex(v, p) if v == w else None)
            counts["vertex_orthogonality"] += 1
        for a, b in product(graph_edges, repeat=2):
            image = action(b, p)
            if image is not None:
                largest_output = max(largest_output, len(image[1]))
            assert adjoint(a, image) == (vertex(target(a), p) if a == b else None)
            counts["graph_CK1"] += 1
        for h in range(m):
            pieces = [action(a, adjoint(a, p)) for a in ((h, False), (h, True))]
            assert all(x is None or x == p for x in pieces)
            assert sum(x is not None for x in pieces) == int(vertex(h, p) is not None)
            counts["regular_vertex_CK2"] += 1
            for a in ((h, False), (h, True)):
                image = action(a, p)
                assert vertex(h, image) == image
                counts["source_range"] += 1
            for act, original in ((action, prefix), (adjoint, deletion)):
                pieces = [act((h, exit_), p) for exit_ in (False, True)]
                surviving = [x for x in pieces if x is not None]
                expected = original(h, p)
                assert surviving == ([] if expected is None else [expected])
                counts["creator_and_adjoint_reconstruction"] += 1
    assert largest_output == MAX_PATH + 1
    return {"maximum_input_path_length": MAX_PATH, "basis_input_vectors": len(basis),
            "maximum_output_path_length_observed": largest_output,
            "outputs_never_truncated": True, "identity_counts": counts,
            "scope": "Exact actions on bounded inputs in the infinite formal path basis; no compression."}


def circle_checks(d):
    tau, edge, m = d["allowed"], d["edge"], len(d["allowed"])
    e = len(d["quiver"].vertices)
    cycles = D.cycles(tau)
    cuts = {cycle[0] for cycle in cycles}
    projections = [{(h, h): ONE for h in range(m) if edge[h] == v} for v in range(e)]
    identity = {(h, h): ONE for h in range(m)}
    for v, w in product(range(e), repeat=2):
        assert matrix_mul(projections[v], projections[w]) == (projections[v] if v == w else {})
    assert sum(len(p) for p in projections) == m
    assert all(len(p) == 2 for p in projections)
    assert {key: value for p in projections for key, value in p.items()} == identity
    samples, curves = [], [[] for _ in cycles]
    totals = {"forbidden_relations": 0, "source_target_identities": 0,
              "based_full_cycles": 0, "fiber_matrix_units": 0}
    for z in SAMPLES + (ONE,):
        assert z*z.conjugate() == ONE
        amplitude = (Gaussian(F(2)) - z - z.conjugate()) / 4
        assert amplitude.im == 0 and 0 <= amplitude.re <= 1
        arrows = [matrix_unit(h, tau[h], amplitude * (z if h in cuts else ONE))
                  for h in range(m)]
        for h in range(m):
            assert matrix_mul(arrows[h], arrows[d["forbidden"][h]]) == {}
            totals["forbidden_relations"] += 1
            assert matrix_mul(projections[edge[h]], arrows[h]) == arrows[h]
            assert matrix_mul(arrows[h], projections[edge[tau[h]]]) == arrows[h]
            totals["source_target_identities"] += 2
        for j, cycle in enumerate(cycles):
            value = amplitude**len(cycle) * z
            curves[j].append(value)
            for h in cycle:
                word, current = [], h
                matrix = matrix_unit(h, h)
                for _ in cycle:
                    word.append(current)
                    matrix = matrix_mul(matrix, arrows[current])
                    current = tau[current]
                assert current == h
                assert matrix == matrix_unit(h, h, value)
                totals["based_full_cycles"] += 1
            if amplitude:
                # Evaluation-fiber generation only. For h=j use a nonempty full turn.
                for h, target in product(cycle, repeat=2):
                    current, matrix, coefficient = h, matrix_unit(h, h), ONE
                    for n in range(1, len(cycle) + 1):
                        coefficient *= amplitude * (z if current in cuts else ONE)
                        matrix = matrix_mul(matrix, arrows[current])
                        current = tau[current]
                        if current == target:
                            break
                    assert coefficient
                    assert matrix_scale(ONE/coefficient, matrix) == matrix_unit(h, target)
                    totals["fiber_matrix_units"] += 1
        if z == ONE:
            assert not amplitude and not any(arrows)
        samples.append({"z": z.json(), "g": amplitude.json(),
                        "full_cycle_values": [(amplitude**len(c) * z).json() for c in cycles]})
    assert all(len(set(values)) == len(SAMPLES) + 1 for values in curves)
    # Paired diagonal constants are actual evaluations of the constant p_e sections.
    lam = [Gaussian(F(v + 1), F(v, 3)) for v in range(e)]
    mu = [Gaussian(F(2*v - 1), F(1, 2)) for v in range(e)]

    def paired(values):
        return {(h, h): values[edge[h]] for h in range(m) if values[edge[h]]}

    assert paired(lam) == {key: lam[v] for v, p in enumerate(projections) for key in p}
    assert matrix_mul(paired(lam), paired(mu)) == paired([x*y for x, y in zip(lam, mu)])
    assert paired([x.conjugate() for x in lam]) == {
        key: value.conjugate() for key, value in paired(lam).items()}
    assert all(lam[edge[h]] == lam[edge[d["alpha"][h]]] for h in range(m))
    return {"cut_arrows": sorted(cuts), "circle_samples": samples,
            "constant_paired_projections": [sparse_json(p) for p in projections],
            "paired_constant_sample": [value.json() for value in lam],
            "paired_constant_embedding_multiplication_and_star": True,
            "finite_identity_counts": totals,
            "sampled_polar_values_pairwise_distinct": True,
            "scope": "Gaussian-rational point evaluations and finite path identities only. "
                     "Not a proof of polar-curve injectivity or infinite C*-generation."}


def diagonal_negative_control():
    a, b = matrix_unit(0, 1), matrix_unit(1, 0)
    lhs, rhs = diagonal(matrix_mul(a, b)), matrix_mul(diagonal(a), diagonal(b))
    assert lhs == matrix_unit(0, 0) and rhs == {} and lhs != rhs
    return {"diag_E01_times_E10": sparse_json(lhs),
            "diag_E01_times_diag_E10": sparse_json(rhs),
            "diagonal_extraction_is_not_multiplicative": True,
            "scope": "Use full matrix evaluation as the *-homomorphism in the fiber diagram."}


def checks():
    source_cached = SOURCE.is_file()
    if source_cached:
        assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
    digest = SOURCE_SHA256
    result = {}
    for d in D.examples():
        result[d["name"]] = {"graph_relation_matrix": graph_relation_checks(d),
                             "Fock_graph": fock_graph_checks(d),
                             "scaled_circle": circle_checks(d)}
    assert len(result) == 8
    return {"source": {"arxiv_version": "1907.10260v3", "pages": 17,
                       "url": "https://arxiv.org/abs/1907.10260v3",
                       "sha256": digest,
                       "local_source_cache": "verified" if source_cached else "absent; pinned citation retained; not needed for exact diagnostics"},
            "helper_sha256": hashlib.sha256((ROOT / "scripts/check_dessin_extension.py").read_bytes()).hexdigest(),
            "arithmetic": "Exact integers/Fraction and Gaussian Fraction; deterministic; no random seed.",
            "conventions": "Travel-order path algebra; matrices E_(h,tau h); graph cycle edges plus vacuum exits.",
            "maximum_Fock_input_length": MAX_PATH,
            "amplitude": "g(z)=|1-z|^2/4=(2-z-conjugate(z))/4",
            "examples": result, "diagonal_negative_control": diagonal_negative_control(),
            "scope": "Finite exact diagnostics of the eight specified infinite dessin models. "
                     "No numerical assertion of infinite C*-generation, a general pullback theorem, "
                     "arithmetic descent, Frobenius compatibility, purity or RH/GRH."}


def run():
    result = checks()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: exact dessin gluing diagnostics for 8 dessins; certificate:", OUT)
    return result


if __name__ == "__main__":
    run()
