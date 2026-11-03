#!/usr/bin/env python3
"""Exact bounded diagnostics for infinite dessin algebras and their Fock model.

Only run() writes, and only to the two named dessin diagnostic files. No
truncation is imposed on the algebra: basis vectors of bounded input length
are tested using exact creation/adjoint rules with unrestricted output length.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import importlib.util
import json
import math
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/checks/2026-11-03-dessins"
MAX_PATH = 8
MAX_SERIES = 10


def load_helper(filename):
    spec = importlib.util.spec_from_file_location(filename[:-3], ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # dataclasses need the module registry.
    spec.loader.exec_module(module)
    return module


H = load_helper("check_projective_resolutions.py")
zero, eye, mul = H.zero, H.identity, H.multiply
add, scale, rank, inverse = H.add, H.scale, H.rank, H.inverse


def det(a):
    """Exact elimination; separate from the existing Leibniz determinant."""
    b, answer = [list(map(F, row)) for row in a], F(1)
    for j in range(len(b)):
        p = next((i for i in range(j, len(b)) if b[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            b[p], b[j] = b[j], b[p]
            answer = -answer
        pivot = b[j][j]
        answer *= pivot
        for i in range(j+1, len(b)):
            q = b[i][j]/pivot
            b[i] = [x-q*y for x, y in zip(b[i], b[j])]
    return answer


def perm(n, *cycles):
    p = list(range(n))
    for cycle in cycles:
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            p[a] = b
    assert sorted(p) == list(range(n))
    return tuple(p)


def cycles(p):
    seen, out = set(), []
    for h in range(len(p)):
        if h not in seen:
            orbit, x = [], h
            while x not in seen:
                orbit.append(x)
                seen.add(x)
                x = p[x]
            out.append(tuple(orbit))
    return tuple(out)


def dessin(name, sigma, alpha, expected_genus):
    n = len(sigma)
    assert n == len(alpha) and n > 0 and n % 2 == 0
    assert all(alpha[h] != h and alpha[alpha[h]] == h for h in range(n))
    inv = tuple(sigma.index(h) for h in range(n))
    phi = tuple(alpha[inv[h]] for h in range(n))
    edges = cycles(alpha)
    edge = {h: i for i, c in enumerate(edges) for h in c}
    arrows = tuple((str(h), edge[h], edge[inv[h]]) for h in range(n))
    forbidden = frozenset((str(h), str(phi[h])) for h in range(n))
    q = H.Quiver(name, tuple(range(len(edges))), arrows, forbidden)
    reached = {0}
    while True:
        larger = reached | {sigma[h] for h in reached} | {alpha[h] for h in reached}
        if larger == reached:
            break
        reached = larger
    assert len(reached) == n
    euler = len(cycles(sigma))-len(edges)+len(cycles(phi))
    assert euler == 2-2*expected_genus
    for h in range(n):
        successors = [int(b) for b, s, _ in arrows if s == edge[inv[h]]]
        assert sorted(successors) == sorted((inv[h], phi[h]))
        assert inv[h] != phi[h]
    return {"name": name, "sigma": sigma, "alpha": alpha, "allowed": inv,
            "forbidden": phi, "edge": edge, "quiver": q,
            "sigma_cycles": cycles(sigma), "phi_cycles": cycles(phi),
            "genus": expected_genus}


def examples():
    result = [
        dessin("interval", perm(2), perm(2, (0, 1)), 0),
        dessin("loop", perm(2, (0, 1)), perm(2, (0, 1)), 0),
        dessin("elliptic_theta", perm(6, (0, 1, 2), (3, 4, 5)),
               perm(6, (0, 3), (1, 4), (2, 5)), 1),
        dessin("spherical_theta", perm(6, (0, 1, 2), (3, 4, 5)),
               perm(6, (0, 3), (1, 5), (2, 4)), 0),
        dessin("elliptic_square", perm(4, (0, 1, 2, 3)),
               perm(4, (0, 2), (1, 3)), 1)]
    # beta=1/(1-T_n(z)^2), the dual of the n-edge path dessin.
    # Start with path rotation rho, then use sigma=(alpha*rho^-1)^-1.
    # This is essential: using rho itself checks a different order, rank4n-2.
    for n in range(3, 6):
        rho = perm(2*n, *((2*i-1, 2*i) for i in range(1, n)))
        alpha = perm(2*n, *((2*i, 2*i+1) for i in range(n)))
        face = tuple(alpha[rho.index(h)] for h in range(2*n))
        sigma = tuple(face.index(h) for h in range(2*n))
        d = dessin("chebyshev_%d" % n, sigma, alpha, 0)
        assert len(d["sigma_cycles"]) == 1 and len(d["sigma_cycles"][0]) == 2*n
        assert sorted(map(len, d["phi_cycles"])) == [1, 1]+[2]*(n-1)
        ep = {h: (s, t) for h, (_a, s, t) in enumerate(d["quiver"].arrows)}
        assert ep[0] == (0, 0) and ep[2*n-1] == (n-1, n-1)
        for i in range(1, n):
            assert ep[2*i-1] == (i-1, i)  # a_i
            assert ep[2*i] == (i, i-1)  # b_i
            assert d["forbidden"][2*i-1] == 2*i
            assert d["forbidden"][2*i] == 2*i-1
        assert d["forbidden"][0] == 0 and d["forbidden"][2*n-1] == 2*n-1
        result.append(d)
    return result


def cycle_value(cycles_, q, signed=False):
    out = F(1)
    for c in cycles_:
        out *= 1-((-1)**len(c) if signed else 1)*q**len(c)
    return out


def cartan_checks(d):
    qv, m = d["quiver"], len(d["sigma"])
    e = len(qv.vertices)
    samples = []
    for q in (F(1, 2), F(1, 3), F(-1, 2)):
        t, u, s, r = zero(m, m), zero(m, m), zero(e, m), zero(m, e)
        for h, (_a, v, w) in enumerate(qv.arrows):
            t[h][d["allowed"][h]] = q
            u[h][d["forbidden"][h]] = q
            s[v][h], r[h][w] = q, F(1)
        denominator = add(eye(m), scale(-1, t))
        numerator = add(eye(m), u)
        assert add(denominator, mul(r, s)) == numerator
        c = add(eye(e), mul(mul(s, inverse(denominator)), r))
        ratio = cycle_value(d["phi_cycles"], q, True)/cycle_value(d["sigma_cycles"], q)
        assert det(numerator) == cycle_value(d["phi_cycles"], q, True)
        assert det(denominator) == cycle_value(d["sigma_cycles"], q)
        assert det(c) == H.determinant(c) == ratio
        if d["name"] in ("interval", "loop"):
            assert ratio == (1+q)/(1-q)
        elif d["name"] == "elliptic_theta":
            assert ratio == (1+q**3)/(1-q**3)
        elif d["name"] == "spherical_theta":
            assert ratio == (1-q*q)**3/(1-q**3)**2
        elif d["name"] == "elliptic_square":
            assert ratio == 1
        else:
            n = e
            assert ratio == (1+q)**2*(1-q*q)**(n-1)/(1-q**(2*n))
        samples.append({"q": str(q), "cartan": [[str(x) for x in row] for row in c],
                        "determinant": str(ratio)})
    # Enumerate genuine paths; source-row/target-column convention.
    permitted, forbidden = [], []
    counts = []
    for n in range(MAX_SERIES+1):
        matrices = []
        for bad in (False, True):
            matrix = zero(e, e)
            for source, word in H.paths(qv, n, forbidden=bad):
                matrix[source][H.target(qv, source, word)] += 1
            matrices.append(matrix)
        permitted.append(matrices[0])
        forbidden.append(scale((-1)**n, matrices[1]))
        counts.append(int(sum(map(sum, matrices[0]))))
    assert counts == [e]+[m]*MAX_SERIES
    for n in range(MAX_SERIES+1):
        for a, b in ((permitted, forbidden), (forbidden, permitted)):
            value = zero(e, e)
            for j in range(n+1):
                value = add(value, mul(a[j], b[n-j]))
            assert value == (eye(e) if n == 0 else zero(e, e))
    return {"rational_samples": samples, "path_counts": counts,
            "series_degree_through": MAX_SERIES,
            "signed_EC_and_CE_scalar_coefficients": 2*(MAX_SERIES+1)*e*e}


def fock_checks(d):
    q, g, f, edge = d["quiver"], d["allowed"], d["forbidden"], d["edge"]
    ep = {h: (s, t) for h, (_a, s, t) in enumerate(q.arrows)}
    basis = [(v, tuple(map(int, w))) for n in range(MAX_PATH+1)
             for v, w in H.paths(q, n)]

    def start(p):
        return p[0]

    def terminal(p):
        return ep[p[1][-1]][1] if p[1] else p[0]

    def prefix(h, p):
        if p is None or ep[h][1] != start(p):
            return None
        if p[1] and p[1][0] != g[h]:
            return None
        return ep[h][0], (h,)+p[1]

    def adjoint(h, p):
        if p is None or not p[1] or p[1][0] != h:
            return None
        word = p[1][1:]
        return (ep[word[0]][0] if word else ep[h][1]), word

    def has_first(h, p):
        return bool(p[1]) and p[1][0] == h

    initial = forbidden = vacuum = terminal_checks = number = 0
    for p in basis:
        for h in range(len(g)):
            image = prefix(h, p)
            expected = p if (start(p) == ep[h][1] and not has_first(f[h], p)) else None
            assert adjoint(h, image) == expected
            initial += 1
            assert prefix(h, prefix(f[h], p)) is None
            forbidden += 1
            assert (prefix(h, adjoint(h, p)) == p) == has_first(h, p)
            if image is not None:
                assert terminal(image) == terminal(p)
                assert len(image[1])-len(p[1]) == 1
                terminal_checks += 1
                number += 1
        for v in q.vertices:
            residual = int(start(p) == v)-sum(
                int(has_first(h, p)) for h, (_a, s, _t) in enumerate(q.arrows) if s == v)
            assert residual == int(not p[1] and start(p) == v)
            vacuum += 1
    sector_counts = []
    for n in range(MAX_PATH+1):
        cs = [sum(terminal(p) == v and len(p[1]) == n for p in basis) for v in q.vertices]
        assert cs == [1 if n == 0 else 2]*len(q.vertices)
        sector_counts.append(cs)
    # Actual L_p vac_v L_q* matrix units, not just their formal labels.
    short = [p for p in basis if len(p[1]) <= 3]
    matrix_units = 0
    for v in q.vertices:
        sector = [p for p in short if terminal(p) == v]
        for p, qpath in product(sector, repeat=2):
            for z in short:
                image = z
                for h in qpath[1]:
                    image = adjoint(h, image)
                if (image is not None and not qpath[1]
                        and start(image) != start(qpath)):
                    image = None  # A stationary path acts by its vertex projection.
                if image is not None and (image[1] or start(image) != v):
                    image = None
                if image is not None:
                    for h in reversed(p[1]):
                        image = prefix(h, image)
                    if not p[1] and start(image) != start(p):
                        image = None
                assert image == (p if z == qpath else None)
                matrix_units += 1
    incidence, defects, lift_checks = [], [], 0
    for orbit in cycles(g):
        a, length = orbit[0], len(orbit)

        def w(p):
            if not has_first(a, p):
                return p
            out = p
            for h in reversed(orbit):
                out = prefix(h, out)
            assert out is not None
            return out

        def wadjoint(p):
            if not has_first(a, p):
                return p
            if len(p[1]) <= length:
                return None
            out = p
            for h in orbit:
                out = adjoint(h, out)
            assert out is not None and has_first(a, out)
            return out

        for p in basis:
            assert wadjoint(w(p)) == p
            back = wadjoint(p)
            defect = has_first(a, p) and len(p[1]) <= length
            assert (back is None) == defect
            if back is not None:
                assert w(back) == p
            lift_checks += 1
        # Defect counts need the full cycle even if length > MAX_PATH.
        word, vector = (), [0]*len(q.vertices)
        for h in orbit:
            word += (h,)
            defect_vector = (ep[a][0], word)
            assert wadjoint(defect_vector) is None
            assert wadjoint(w(defect_vector)) == defect_vector
            vector[terminal(defect_vector)] += 1
        wanted = [sum(edge[h] == v for h in orbit) for v in q.vertices]
        assert vector == wanted
        incidence.append(wanted)
        defects.append({"allowed_cycle": orbit, "defect_by_terminal_sector": vector,
                        "connecting_map_column": [-x for x in vector],
                        "naive_Lc_plus_complement_vacuum_norm_squared": 2})
        # L_c+(1-Q_a) sends this vacuum to two orthogonal basis vectors.
        vac = (ep[a][0], ())
        c_vac = vac
        for h in reversed(orbit):
            c_vac = prefix(h, c_vac)
        assert c_vac is not None and c_vac != vac and not has_first(a, vac)
    matrix = [[column[v] for column in incidence] for v in q.vertices]
    matrix_rank = rank(matrix)
    # Determinantal divisors give the exact Smith torsion, not just rational rank.
    previous, smith = 1, []
    for size in range(1, matrix_rank+1):
        divisor = 0
        for rows in combinations(range(len(matrix)), size):
            for cols in combinations(range(len(incidence)), size):
                minor = det([[matrix[i][j] for j in cols] for i in rows])
                assert minor.denominator == 1
                divisor = math.gcd(divisor, abs(int(minor)))
        assert divisor and divisor % previous == 0
        smith.append(divisor//previous)
        previous = divisor
    return {"basis_input_length_through": MAX_PATH, "basis_vectors": len(basis),
            "unrestricted_output_lengths": True,
            "initial_projection_identities": initial, "forbidden_products": forbidden,
            "vertex_vacuum_identities": vacuum, "terminal_preservation": terminal_checks,
            "number_commutators_on_nonzero_creation": number,
            "terminal_sector_dimension_by_degree": sector_counts,
            "matrix_unit_input_and_word_length_through": 3,
            "actual_terminal_sector_matrix_unit_actions": matrix_units,
            "cycle_isometry_and_defect_checks": lift_checks, "cycle_defects": defects,
            "unsigned_incidence_matrix": matrix, "Smith_nonzero_diagonal": smith,
            "K0_free_rank": len(q.vertices)-matrix_rank+len(incidence),
            "K0_torsion_orders": [x for x in smith if x > 1],
            "K1_free_rank": len(incidence)-matrix_rank,
            "K_group_scope": "Diagnostic incidence calculation; analytic extension proof is prose."}


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def kron(a, b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def sym(a, n):
    """Monomial basis e1^(n-j)e2^j; columns are images, no divided powers."""
    out = zero(n+1, n+1)
    for j in range(n+1):
        for p in range(n-j+1):
            for q in range(j+1):
                out[p+q][j] += (math.comb(n-j, p)*math.comb(j, q)*
                    a[0][0]**(n-j-p)*a[1][0]**p*a[0][1]**(j-q)*a[1][1]**q)
    return out


def complete(a, max_degree):
    powers, power_sums = eye(len(a)), [F(0)]
    for _ in range(max_degree):
        powers = mul(powers, a)
        power_sums.append(trace(powers))
    h = [F(1)]
    for n in range(1, max_degree+1):
        h.append(sum((power_sums[j]*h[n-j] for j in range(1, n+1)), F(0))/n)
    return h


def schur_checks():
    x1, x2, x3 = [[1, 1], [0, 1]], [[2, 0], [0, 1]], [[1, 0], [1, 1]]
    m = mul(mul(x3, x2), x1)
    assert m == [[2, 2], [2, 3]]
    samples = [m, [[1, 1], [0, 2]], [[0, 1], [-1, 1]]]
    singular = [[[0, 1], [0, 0]], zero(2, 2)]
    theta = next(d for d in examples() if d["name"] == "elliptic_theta")
    arrow = {h: zero(2, 2) for h in range(6)}
    arrow.update({0: x1, 2: x2, 1: x3})
    for h in range(6):
        j = theta["forbidden"][h]
        assert mul(arrow[j], arrow[h]) == zero(2, 2)
        assert mul(sym(arrow[j], 2), sym(arrow[h], 2)) == zero(3, 3)
    assert mul(mul(sym(x3, 2), sym(x2, 2)), sym(x1, 2)) == sym(m, 2)
    for a in samples+singular:
        t, delta = trace(a), det(a)
        assert trace(sym(a, 2)) == t*t-delta
        assert trace(sym(a, 2)) == (t*t+trace(mul(a, a)))/2
        assert trace(sym(a, 3)) == t**3-2*t*delta
    assert sym(zero(2, 2), 0) == [[1]]
    assert mul(sym(zero(2, 2), 0), sym(zero(2, 2), 0)) != [[0]]
    b = [[1, 0, 0, 0, 0, 0], [0, F(2, 3), 0, 0, 1, 0],
         [0, 0, F(1, 3), 0, 0, 1], [0, F(1, 3), 0, 0, -1, 0],
         [0, 0, F(2, 3), 0, 0, -1], [0, 0, 0, 1, 0, 0]]
    assert det(b) == 1
    for a in samples+singular:
        rhs = H.block_diagonal(sym(a, 3), scale(det(a), a))
        assert mul(kron(a, sym(a, 2)), b) == mul(b, rhs)
    # A single actual Young idempotent, not a central isotypic projector.
    words = list(product(range(2), repeat=3))

    def place(p):
        out = zero(8, 8)
        for j, word in enumerate(words):
            out[words.index(tuple(word[i] for i in p))][j] = F(1)
        return out

    y = mul(add(eye(8), place((1, 0, 2))), add(eye(8), scale(-1, place((2, 1, 0)))))
    assert mul(y, y) == scale(3, y) and rank(y) == 2
    for a in samples:
        assert trace(mul(kron(kron(a, a), a), scale(F(1, 3), y))) == det(a)*trace(a)
    coefficients = 0
    for a, c in product(samples, repeat=2):
        lhs, ha, hc = complete(kron(a, c), 8), complete(a, 8), complete(c, 8)
        for n in range(9):
            rhs = sum((det(a)**j*ha[n-2*j]*det(c)**j*hc[n-2*j]
                       for j in range(n//2+1)), F(0))
            assert lhs[n] == rhs
            coefficients += 1
    r = F(1, 100)
    gram = [[1/det(add(eye(4), scale(-r, kron(a, c)))) for c in samples] for a in samples]
    norms = [sum(F(x*x) for row in a for x in row) for a in samples]
    assert r*max(norms) == F(21, 100) < 1
    minors = []
    for n in range(1, 4):
        for ids in combinations(range(3), n):
            value = det([[gram[i][j] for j in ids] for i in ids])
            assert value >= 0
            minors.append({"indices": ids, "determinant": str(value)})
    assert det(gram) > 0
    tableau_shapes = 0
    diagonal = [[2, 0], [0, 3]]
    for size in range(6):
        for j in range(size//2+1):
            shape = (size-j, j)
            boxes = [(i, k) for i, length in enumerate(shape) for k in range(length)]
            count, character = 0, F(0)
            for entries in product((1, 2), repeat=size):
                table = dict(zip(boxes, entries))
                rows_ok = all(table[i, k] <= table[i, k+1] for i, k in boxes if (i, k+1) in table)
                columns_ok = all(table[i, k] < table[i+1, k] for i, k in boxes if (i+1, k) in table)
                if rows_ok and columns_ok:
                    count += 1
                    character += F(2)**entries.count(1)*F(3)**entries.count(2)
            assert count == size-2*j+1
            assert character == det(diagonal)**j*trace(sym(diagonal, size-2*j))
            tableau_shapes += 1
    # Source weights and target dual weights: coordinate action is contragredient.
    source, dual = [[2, 0], [0, 3]], [[F(1, 5), 0], [0, F(1, 7)]]
    assert complete(kron(source, dual), 2)[2] == F(2281, 1225)
    assert F(2281, 1225) == trace(sym(source, 2))*trace(sym(dual, 2))+det(source)*det(dual)
    # The actual split simple-module sequence loses exactness under Sym^2.
    inc, projection = [[1], [0]], [[0, 1]]
    sym_inc, sym_projection = [[1], [0], [0]], [[0, 0, 1]]
    assert mul(projection, inc) == [[0]]
    assert 3-rank(sym_inc)-rank(sym_projection) == 1
    # Actual node lattice: x+y=uI, but Schur arrow maps do not preserve it.
    lattice_samples = []
    for u in (F(2), F(3, 2)):
        x, z = [[u, 0], [0, 0]], [[0, 0], [0, u]]
        assert add(x, z) == scale(u, eye(2))
        sx, sz = sym(x, 2), sym(z, 2)
        assert mul(sx, sz) == zero(3, 3)
        assert add(sx, sz) != scale(u, eye(3))
        assert add(sx, sz) != scale(u*u, eye(3))
        assert add(sx, sz)[1][1] == 0
        lattice_samples.append(str(u))
    return {"monodromy": m, "monodromy_trace": int(trace(m)), "monodromy_det": int(det(m)),
            "Young_shape": [2, 1], "Young_hook_factor": 3, "Young_rank": 2,
            "semistandard_two_row_shapes_size_through_5": tableau_shapes,
            "actual_theta_zero_relations_and_Sym2_images": 6,
            "Young_trace_samples": 3, "LR_actual_matrix_intertwiners": 5,
            "LR_includes_singular_and_zero": True, "cauchy_coefficients": coefficients,
            "cauchy_degree_through": 8, "cauchy_r": str(r),
            "sufficient_convergence_bound": "r*max_Frobenius_norm_squared=21/100<1",
            "Gram_all_principal_minors": minors, "coordinate_degree_two": "2281/1225",
            "split_Sym2_middle_homology_dimension": 1,
            "fixed_R_lattice_failures_u_samples": lattice_samples,
            "empty_partition_scope": "constant scalar feature, not a zero-relation module functor",
            "scope": "Exact finite identities; no global arithmetic PSD or exact Schur functor claim."}


def finite_field_checks():
    counts, data = {}, {}
    for d in (1, 2):
        assert (-432*d*d) % 7 != 0
        fibers = [[y for y in range(7) if (y*y-x*x*x+d) % 7 == 0] for x in range(7)]
        count = 1+sum(map(len, fibers))
        counts[str(d)] = count
        data[str(d)] = {"y_fibers_x_0_through_6": fibers,
                        "fiber_cardinalities": list(map(len, fibers)),
                        "points_including_infinity": count, "a7": 8-count,
                        "H1_local_factor_ascending": [1, -(8-count), 7]}
    assert counts == {"1": 4, "2": 7}
    assert data["1"]["fiber_cardinalities"] == [0, 1, 1, 0, 1, 0, 0]
    assert data["2"]["fiber_cardinalities"] == [0, 0, 0, 2, 0, 2, 2]
    return {"field": "F_7", "equation": "y^2=x^3-d", "point_counts": counts,
            "models": data, "scope": "Two good-reduction models; complex Belyi descent argument is prose."}


def check_all():
    result = {}
    for d in examples():
        name = d["name"]
        result[name] = {"sigma": d["sigma"], "alpha": d["alpha"],
            "phi": d["forbidden"], "genus": d["genus"],
            "sigma_cycles": d["sigma_cycles"], "phi_cycles": d["phi_cycles"],
            "quiver_arrows_source_target": d["quiver"].arrows,
            "rank_over_common_DVR": sum(len(c)**2 for c in d["sigma_cycles"]),
            "cartan": cartan_checks(d), "Fock": fock_checks(d)}
    assert result["elliptic_theta"]["rank_over_common_DVR"] == 18
    assert result["spherical_theta"]["rank_over_common_DVR"] == 18
    for n in range(3, 6):
        data = result["chebyshev_%d" % n]
        assert data["rank_over_common_DVR"] == (2*n)**2
        data["Belyi_map"] = "1/(1-T_%d(z)^2)" % n
        data["arrow_labels"] = {"l": 0, "r": 2*n-1,
            **{"a_%d" % i: 2*i-1 for i in range(1, n)},
            **{"b_%d" % i: 2*i for i in range(1, n)}}
    for name, k0, torsion, k1 in (("interval", 2, [], 1), ("loop", 1, [2], 0),
                                 ("elliptic_theta", 4, [], 1), ("spherical_theta", 4, [], 1)):
        data = result[name]["Fock"]
        assert (data["K0_free_rank"], data["K0_torsion_orders"], data["K1_free_rank"]) == (k0, torsion, k1)
    return {"arithmetic": "Deterministic exact integers/Fraction; no dependencies or random seed",
        "conventions": "Travel-order words; phi=alpha*sigma^-1; Cartan source rows; prefix Fock action",
        "bounds": {"input_Fock_path_length_through": MAX_PATH,
                   "signed_series_degree_through": MAX_SERIES,
                   "rational_Cartan_samples_per_dessin": 3},
        "examples": result, "schur": schur_checks(), "finite_field_twists": finite_field_checks(),
        "scope": "Bounded exact diagnostics of the stated infinite path algebras, Fock basis rules, "
                 "Schur matrices and two F7 curves. Not an analytic extension proof, a universal "
                 "completed-order Schur/resolution theorem, an arithmetic determinant bridge, or RH/GRH."}


def run():
    result = check_all()
    assert result["examples"]["interval"]["genus"] == 0
    assert result["examples"]["elliptic_theta"]["genus"] == 1
    assert result["examples"]["elliptic_square"]["rank_over_common_DVR"] == 16
    assert result["finite_field_twists"]["point_counts"] == {"1": 4, "2": 7}
    assert result["schur"]["cauchy_coefficients"] == 81
    # Independently maintained HLS/diamond checker: import only its pure API.
    diamond = load_helper("check_dessin_diamonds.py")
    result["HLS_diamond_checker"] = diamond.checks()
    totals = {"dessins": len(result["examples"]),
              "rational_Cartan_samples": 3*len(result["examples"]),
              "Fock_initial_projection_identities": sum(
                  x["Fock"]["initial_projection_identities"] for x in result["examples"].values()),
              "Fock_forbidden_products": sum(
                  x["Fock"]["forbidden_products"] for x in result["examples"].values()),
              "cycle_lift_and_defect_checks": sum(
                  x["Fock"]["cycle_isometry_and_defect_checks"] for x in result["examples"].values()),
              "terminal_sector_matrix_unit_basis_actions": sum(
                  x["Fock"]["actual_terminal_sector_matrix_unit_actions"] for x in result["examples"].values()),
              "signed_series_scalar_coefficients": sum(
                  x["cartan"]["signed_EC_and_CE_scalar_coefficients"] for x in result["examples"].values()),
              "Cauchy_coefficients": result["schur"]["cauchy_coefficients"],
              "actual_LR_matrix_intertwiners": result["schur"]["LR_actual_matrix_intertwiners"]}
    result["totals"] = totals
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "exact-checks.json").write_text(json.dumps(result, indent=2, default=str)+"\n")
    log = "PASS: exact dessin extension diagnostics\n"+json.dumps(totals, indent=2)+"\n"+result["scope"]+"\n"
    (OUT / "exact-check.log").write_text(log)
    print(log, end="")
    return result


if __name__ == "__main__":
    run()
