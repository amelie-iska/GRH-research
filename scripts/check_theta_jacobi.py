#!/usr/bin/env python3
"""Deterministic finite Jacobi/elliptic-theta checks, using only the stdlib.

Eisenstein integers are integer pairs (a,b) for a+b*omega, omega^2=-1-omega.
checks() is pure. run() writes only the explicitly named JSON artifact.
Point enumeration and the character/Jacobi calculation are independent routes.
These finite diagnostics do not prove the all-prime theorem or RH/GRH.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import json
import math


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/checks/2026-11-03-jacobi/exact-checks.json"
SPLIT_PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97)
INERT_PRIMES = (5, 11, 17, 23, 29, 41, 47, 53)
MAX_DECK_PATH_LENGTH = 12
ZERO, ONE, OMEGA = (0, 0), (1, 0), (0, 1)


def eadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def escale(n, x):
    return n*x[0], n*x[1]


def emul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def epow(x, n):
    assert n >= 0
    out = ONE
    for _ in range(n):
        out = emul(out, x)
    return out


def econj(x):
    return x[0]-x[1], -x[1]


def enorm(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


def etrace(x):
    return 2*x[0]-x[1]


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))


def prime_divisors(n):
    return [q for q in range(2, n+1) if n % q == 0 and is_prime(q)]


def least_primitive_generator(p):
    assert is_prime(p)
    factors = prime_divisors(p-1)
    for g in range(2, p):
        if all(pow(g, (p-1)//q, p) != 1 for q in factors):
            assert len({pow(g, n, p) for n in range(p-1)}) == p-1
            return g
    raise AssertionError("No primitive generator found")


def legendre(a, p):
    if a % p == 0:
        return 0
    residue = pow(a % p, (p-1)//2, p)
    assert residue in (1, p-1)
    return 1 if residue == 1 else -1


def characters(p):
    assert is_prime(p) and p % 6 == 1
    g = least_primitive_generator(p)
    logs = {pow(g, n, p): n for n in range(p-1)}
    rho = [ZERO]+[epow(OMEGA, logs[a] % 3) for a in range(1, p)]
    eta = [legendre(a, p) for a in range(p)]
    assert rho[g] == OMEGA and eta[g] == -1
    assert Counter(rho[1:]) == {epow(OMEGA, j): (p-1)//3 for j in range(3)}
    for a, b in product(range(p), repeat=2):
        assert emul(rho[a], rho[b]) == rho[(a*b) % p]
        assert eta[a]*eta[b] == eta[(a*b) % p]
    return g, logs, rho, eta


def affine_point_data(p, d):
    """Exhaust all p^2 affine pairs, then add the unique projective infinity."""
    per_x = [sum((y*y-x*x*x+d) % p == 0 for y in range(p)) for x in range(p)]
    count = 1+sum(per_x)
    return count, per_x


def multiplication_matrix(alpha):
    """Multiplication by alpha on Z[omega], ordered basis (1,omega)."""
    a, b = alpha
    return [[a, -b], [b, a-b]]


def determinant_local_coefficients(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    return [1, -(a+d), a*d-b*c]  # det(I-T*M), ascending powers of T


def matrix_zero(rows, columns):
    return [[Q(0) for _ in range(columns)] for _ in range(rows)]


def matrix_identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def matrix_add(a, b):
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def matrix_scale(c, a):
    return [[Q(c)*x for x in row] for row in a]


def matrix_multiply(a, b):
    assert a and b and len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def matrix_power(a, n):
    out = matrix_identity(len(a))
    for _ in range(n):
        out = matrix_multiply(out, a)
    return out


def matrix_transpose(a):
    return [list(column) for column in zip(*a)]


def poly_multiply(a, b):
    result = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def matrix_det_polynomial(a):
    """Coefficientwise Leibniz determinant of I-T*a, independent of factoring."""
    n = len(a)
    assert all(len(row) == n for row in a)
    result = [Q(0)]*(n+1)
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = [Q(sign)]
        for i, j in enumerate(perm):
            term = poly_multiply(term, [Q(i == j), -Q(a[i][j])])
        result = [x+y for x, y in zip(result, term)]
    return result


CELL_BOUNDARY = [[-1, -1, -1], [1, 1, 1]]
CELL_INCLUSION = [[1, 0], [-1, 1], [0, -1]]
CELL_PERMUTATION = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
CELL_GRAM = [[2, -1], [-1, 2]]


def vertex_action(gamma):
    return [[Q(1+gamma, 2), Q(1-gamma, 2)],
            [Q(1-gamma, 2), Q(1+gamma, 2)]]


def edge_action(a, b):
    return matrix_add(matrix_scale(a, matrix_identity(3)), matrix_scale(b, CELL_PERMUTATION))


def cellular_carrier_checks(split):
    d1, inc, pmat, gram = CELL_BOUNDARY, CELL_INCLUSION, CELL_PERMUTATION, CELL_GRAM
    d2 = [[0], [0], [0]]
    cm = multiplication_matrix(OMEGA)
    assert matrix_multiply(d1, inc) == matrix_zero(2, 2)
    assert matrix_multiply(d1, d2) == matrix_zero(2, 1)
    assert matrix_multiply(matrix_transpose(inc), inc) == gram
    assert matrix_multiply(pmat, inc) == matrix_multiply(inc, cm)
    assert matrix_multiply(d1, pmat) == d1
    assert matrix_power(pmat, 3) == matrix_identity(3)
    assert matrix_add(matrix_add(matrix_power(cm, 2), cm), matrix_identity(2)) == matrix_zero(2, 2)
    assert gram[0][0] > 0 and gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0] == 3
    delta, vertex_sum, edge_sum = [[-1], [1]], [[1], [1]], [[1], [1], [1]]
    swap = [[0, 1], [1, 0]]
    assert matrix_multiply(swap, d1) == matrix_scale(-1, d1)
    smat = matrix_add(matrix_add(matrix_identity(3), pmat), matrix_power(pmat, 2))
    assert smat == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    models, k_counts, exponent_counts = {}, Counter(), Counter()
    count = 0
    for prime in SPLIT_PRIMES:
        pdata = split[str(prime)]
        base_a, base_b = pdata["j"]
        rho_powers = [epow(OMEGA, j) for j in range(3)]
        for d in range(1, prime):
            data = pdata["models"][str(d)]
            a, b = data["alpha"]
            gamma = a+b
            f0, f1, f2 = vertex_action(gamma), edge_action(a, b), [[prime]]
            cm_d = multiplication_matrix((a, b))
            assert matrix_multiply(f1, inc) == matrix_multiply(inc, cm_d)
            assert matrix_multiply(d1, f1) == matrix_multiply(f0, d1)
            assert matrix_multiply(f1, d2) == matrix_multiply(d2, f2)
            assert matrix_multiply(f0, vertex_sum) == vertex_sum
            assert matrix_multiply(f0, delta) == matrix_scale(gamma, delta)
            assert matrix_multiply(f1, edge_sum) == matrix_scale(gamma, edge_sum)
            assert matrix_multiply(matrix_multiply(matrix_transpose(cm_d), gram), cm_d) == matrix_scale(prime, gram)
            assert matrix_multiply(f1, pmat) == matrix_multiply(pmat, f1)
            assert matrix_multiply(f0, swap) == matrix_multiply(swap, f0)
            f0_poly, f1_poly, f2_poly = map(matrix_det_polynomial, (f0, f1, f2))
            local_poly = data["local_factor_ascending_T_coefficients"]
            assert f0_poly == poly_multiply([1, -1], [1, -gamma])
            assert f1_poly == poly_multiply([1, -gamma], local_poly)
            assert f2_poly == [1, -prime]
            assert poly_multiply(f1_poly, poly_multiply([1, -1], [1, -prime])) == poly_multiply(
                poly_multiply(f0_poly, f2_poly), local_poly)
            kappa = legendre(d, prime)
            rho_d = escale(kappa, tuple(data["lambda"]))  # eta(d)^-1=eta(d)
            exponent = rho_powers.index(rho_d)
            unred_f1 = matrix_scale(kappa, matrix_multiply(matrix_power(pmat, exponent), edge_action(base_a, base_b)))
            unred_gamma = kappa*(base_a+base_b)
            unred_f0 = vertex_action(unred_gamma)
            unred_f2 = f2
            k = (0, kappa*base_b, kappa*base_a)[exponent]
            assert unred_gamma-gamma == 3*k
            edge_difference = matrix_add(unred_f1, matrix_scale(-1, f1))
            vertex_difference = matrix_add(unred_f0, matrix_scale(-1, f0))
            assert edge_difference == matrix_scale(k, smat)
            homotopy = [[Q(-k, 2), Q(k, 2)] for _ in range(3)]
            assert matrix_multiply(homotopy, delta) == matrix_scale(k, edge_sum)
            assert matrix_multiply(homotopy, vertex_sum) == matrix_zero(3, 1)
            assert matrix_multiply(homotopy, d1) == edge_difference
            assert matrix_multiply(d1, homotopy) == vertex_difference
            assert matrix_multiply(d1, unred_f1) == matrix_multiply(unred_f0, d1)
            assert matrix_multiply(unred_f1, d2) == matrix_multiply(d2, unred_f2)
            assert matrix_add(unred_f2, matrix_scale(-1, f2)) == matrix_zero(1, 1)
            assert matrix_multiply(unred_f1, inc) == matrix_multiply(inc, cm_d)
            k_counts[k] += 1
            exponent_counts[exponent] += 1
            models["%d:%d" % (prime, d)] = {
                "prime": prime, "d": d, "alpha": [a, b], "gamma": gamma,
                "F0": f0, "F1": f1, "F2": f2, "H1_matrix": cm_d,
                "det_I_minus_TF0": f0_poly, "det_I_minus_TF1": f1_poly,
                "det_I_minus_TF2": f2_poly,
                "descent_kappa": kappa, "descent_rho_exponent": exponent,
                "unreduced_F0": unred_f0, "unreduced_F1": unred_f1, "unreduced_F2": unred_f2,
                "homotopy_scalar_k": k, "H_C0_to_C1": homotopy,
                "chain_Gram_equivariance_and_homotopy_pass": True}
            count += 1
    assert count == 516 and exponent_counts == {0: 172, 1: 172, 2: 172}
    assert k_counts[0] == 172 and count-k_counts[0] == 344
    return {"coefficient_field": "Q; Fraction values serialized as exact strings",
        "chain_dimensions_C2_C1_C0": [1, 3, 2], "d2": d2,
        "d1": d1, "H1_inclusion_columns_b0_b1": inc,
        "P_edge_rotation": pmat, "C_H1_rotation": cm, "G_H1_Gram": gram,
        "Gram_principal_minors": [2, 3], "deck_alpha_on_C0": swap,
        "deck_alpha_on_C1": matrix_scale(-1, matrix_identity(3)), "deck_alpha_on_C2": [[1]],
        "split_twist_chain_checks": count, "determinant_polynomial_identities": 4*count,
        "Gram_scaled_isometries": count, "rational_chain_homotopies": count,
        "nonzero_homotopy_scalars": count-k_counts[0],
        "descent_rho_exponent_counts": dict(sorted(exponent_counts.items())),
        "homotopy_scalar_distribution": dict(sorted(k_counts.items())), "models": models,
        "scope": "Actual theta cellular matrices and exact rational homotopies for all "
            "tested split twists. H0/H2 actions chosen as1,p; no integral Tate comparison, "
            "order-projective Frobenius functor, or global positive determinant is inferred."}


def split_prime_checks(p):
    g, logs, rho, eta = characters(p)
    terms = [escale(eta[(1-u) % p], rho[u]) for u in range(p)]
    jacobi = ZERO
    for term in terms:
        jacobi = eadd(jacobi, term)
    j = escale(-eta[p-1], jacobi)
    assert enorm(j) == p and eadd(j, econj(j)) == (etrace(j), 0)
    # The opposite cubic character conjugates the entire Jacobi construction.
    opposite = ZERO
    for u in range(p):
        opposite = eadd(opposite, escale(eta[(1-u) % p], econj(rho[u])))
    assert escale(-eta[p-1], opposite) == econj(j)
    lambdas = [escale(eta[d], rho[d]) for d in range(1, p)]
    assert len(set(lambdas)) == 6
    assert Counter(lambdas) == {value: (p-1)//6 for value in set(lambdas)}
    assert epow(escale(-1, OMEGA), 6) == ONE
    assert all(epow(escale(-1, OMEGA), k) != ONE for k in range(1, 6))
    models = {}
    for d in range(1, p):
        assert (-432*d*d) % p != 0  # all tested curves have good reduction
        lam = lambdas[d-1]
        assert enorm(lam) == 1
        alpha = emul(lam, j)
        trace = etrace(alpha)
        assert isinstance(trace, int) and enorm(alpha) == p
        count, per_x = affine_point_data(p, d)
        assert count == p+1-trace, (p, d, alpha, trace, count)
        assert per_x == [1+eta[(x*x*x-d) % p] for x in range(p)]
        assert trace*trace <= 4*p
        matrix = multiplication_matrix(alpha)
        coefficients = determinant_local_coefficients(matrix)
        assert coefficients == [1, -trace, p]
        # Class dependence is checked for every nonzero sextic twist, not just d=1.
        assert lam == epow(escale(-1, OMEGA), logs[d])
        models[str(d)] = {"lambda": list(lam), "alpha": list(alpha),
            "trace": trace, "norm": enorm(alpha), "point_count": count,
            "y_solution_counts_x_0_through_p_minus_1": per_x,
            "Eisenstein_multiplication_matrix": matrix,
            "local_factor_ascending_T_coefficients": coefficients}
    for a, b in product(range(1, p), repeat=2):
        assert emul(lambdas[a-1], lambdas[b-1]) == lambdas[(a*b) % p-1]
    return {"least_primitive_generator": g,
        "rho_generator": list(OMEGA), "eta_minus_one": eta[p-1],
        "J": list(jacobi), "j": list(j), "j_norm": enorm(j),
        "Jacobi_terms_u_0_through_p_minus_1": [list(x) for x in terms],
        "models": models,
        "counts": {"curves_all_nonzero_d": p-1,
                   "affine_pairs_enumerated": (p-1)*p*p,
                   "rho_and_eta_multiplicativity_equalities": 2*p*p,
                   "lambda_multiplicativity_equalities": (p-1)**2,
                   "point_count_and_local_factor_checks": p-1}}


def inert_prime_checks(p):
    assert is_prime(p) and p % 3 == 2 and p >= 5
    assert len({pow(x, 3, p) for x in range(p)}) == p
    models = {}
    for d in range(1, p):
        assert (-432*d*d) % p != 0
        count, per_x = affine_point_data(p, d)
        assert count == p+1
        assert count == 1+sum(1+legendre(x*x*x-d, p) for x in range(p))
        models[str(d)] = {"point_count": count, "trace": 0,
            "y_solution_counts_x_0_through_p_minus_1": per_x,
            "local_factor_ascending_T_coefficients": [1, 0, p]}
    return {"cube_map_is_bijective": True, "models": models,
        "counts": {"curves_all_nonzero_d": p-1, "affine_pairs_enumerated": (p-1)*p*p,
                   "trace_zero_checks": p-1}}


def compose(a, b):
    """a after b, matching the fixed permutation convention."""
    return tuple(a[b[h]] for h in range(len(a)))


def permutation_power(a, n):
    out = tuple(range(len(a)))
    for _ in range(n):
        out = compose(a, out)
    return out


def permutation_order(a):
    return next(n for n in range(1, math.factorial(len(a))+1)
                if permutation_power(a, n) == tuple(range(len(a))))


def deck_checks():
    sigma = (1, 2, 0, 4, 5, 3)  # (012)(345)
    alpha = (3, 4, 5, 0, 1, 2)  # (03)(14)(25)
    tau = tuple(sigma.index(h) for h in range(6))
    phi = compose(alpha, tau)
    assert compose(sigma, alpha) == compose(alpha, sigma)
    assert permutation_order(sigma) == 3 and permutation_order(alpha) == 2
    assert phi == (5, 3, 4, 2, 0, 1)
    assert permutation_order(phi) == 6
    centralizer = [p for p in permutations(range(6))
                   if compose(p, sigma) == compose(sigma, p)
                   and compose(p, alpha) == compose(alpha, p)]
    generator = compose(sigma, alpha)
    generated = {permutation_power(generator, k) for k in range(6)}
    assert permutation_order(generator) == 6
    assert set(centralizer) == generated and len(centralizer) == 6
    assert Counter(map(permutation_order, centralizer)) == {1: 1, 2: 1, 3: 2, 6: 2}
    edge = (0, 1, 2, 0, 1, 2)
    maps = []
    support_checks = path_checks = 0
    full_cycle_words = set()
    for h in range(6):
        full_cycle_words.add((h, tau[h], tau[tau[h]]))
    for p in centralizer:
        vertex_map = tuple(edge[p[e]] for e in range(3))
        assert sorted(vertex_map) == [0, 1, 2]
        for h in range(6):
            assert edge[p[h]] == vertex_map[edge[h]]
            assert edge[tau[p[h]]] == vertex_map[edge[tau[h]]]
            assert p[tau[h]] == tau[p[h]]
            assert p[phi[h]] == phi[p[h]]
            assert p[alpha[h]] == alpha[p[h]]
            support_checks += 1
        assert {tuple(p[h] for h in word) for word in full_cycle_words} == full_cycle_words
        for successor in (tau, phi):
            for length in range(1, MAX_DECK_PATH_LENGTH+1):
                for h in range(6):
                    word = [h]
                    for _ in range(length-1):
                        word.append(successor[word[-1]])
                    image = tuple(p[a] for a in word)
                    assert all(successor[a] == b for a, b in zip(image, image[1:]))
                    assert edge[image[0]] == vertex_map[edge[h]]
                    assert edge[tau[image[-1]]] == vertex_map[edge[tau[word[-1]]]]
                    path_checks += 1
        maps.append({"dart_permutation": p, "order": permutation_order(p),
                     "induced_edge_vertex_permutation": vertex_map})
    return {"sigma": sigma, "alpha": alpha, "tau": tau, "phi": phi,
        "simultaneous_centralizer": maps, "centralizer_order": 6,
        "cyclic_generator": generator, "order_distribution": {"1": 1, "2": 1, "3": 2, "6": 2},
        "permutation_candidates_exhausted": math.factorial(6),
        "dart_support_and_successor_checks": support_checks,
        "permitted_and_forbidden_word_checks": path_checks,
        "common_DVR_parameter_based_cycle_sum_fixed": True,
        "word_length_range": [1, MAX_DECK_PATH_LENGTH],
        "formal_order_scope": "Arrow relabeling preserves both relations and J, and fixes "
            "the sum of all based full cycles (the common DVR parameter). This gives "
            "the polynomial/order permutation action; not an arithmetic Frobenius identification.",
        "geometric_deck_formulas": "Over a field containing mu_3: (x,y)->(xi*x,y), "
            "xi^3=1, and (x,y)->(x,-y); both preserve beta=x^3/d."}


def arithmetic_self_checks():
    assert emul(OMEGA, OMEGA) == (-1, -1)
    assert epow(OMEGA, 3) == ONE
    units = {epow(escale(-1, OMEGA), k) for k in range(6)}
    assert len(units) == 6 and all(enorm(u) == 1 for u in units)
    pairs = list(product(range(-3, 4), repeat=2))
    for x, y in product(pairs, repeat=2):
        assert enorm(emul(x, y)) == enorm(x)*enorm(y)
        assert econj(emul(x, y)) == emul(econj(x), econj(y))
    for x in pairs:
        assert emul(x, econj(x)) == (enorm(x), 0)
        assert eadd(x, econj(x)) == (etrace(x), 0)
    return {"Eisenstein_pair_box_each_coordinate": [-3, 3],
            "norm_multiplicativity_pairs": len(pairs)**2,
            "conjugation_multiplicativity_pairs": len(pairs)**2,
            "trace_and_norm_conjugation_values": len(pairs), "six_units": sorted(units)}


def checks():
    self_checks = arithmetic_self_checks()
    split = {str(p): split_prime_checks(p) for p in SPLIT_PRIMES}
    inert = {str(p): inert_prime_checks(p) for p in INERT_PRIMES}
    assert split["7"]["least_primitive_generator"] == 3
    assert split["7"]["j"] == [3, 2]
    assert split["7"]["models"]["1"]["trace"] == 4
    assert split["7"]["models"]["2"]["alpha"] == [-1, -3]
    assert split["7"]["models"]["2"]["trace"] == 1
    totals = {"split_primes": len(split), "inert_primes": len(inert),
        "split_curves_all_nonzero_d": sum(p-1 for p in SPLIT_PRIMES),
        "inert_curves_all_nonzero_d": sum(p-1 for p in INERT_PRIMES),
        "affine_pairs_enumerated": sum((p-1)*p*p for p in SPLIT_PRIMES+INERT_PRIMES),
        "character_multiplicativity_equalities": sum(2*p*p for p in SPLIT_PRIMES),
        "twist_multiplicativity_equalities": sum((p-1)**2 for p in SPLIT_PRIMES)}
    totals["all_curves"] = totals["split_curves_all_nonzero_d"]+totals["inert_curves_all_nonzero_d"]
    cellular = cellular_carrier_checks(split)
    totals["cellular_split_twists"] = cellular["split_twist_chain_checks"]
    totals["cellular_determinant_polynomial_identities"] = cellular["determinant_polynomial_identities"]
    totals["cellular_rational_homotopies"] = cellular["rational_chain_homotopies"]
    return {"baseline_function": "checks(): deterministic pure finite exact diagnostics",
        "arithmetic": "Integer pairs for Z[omega], omega^2=-1-omega; Python stdlib only",
        "character_convention": "Least positive primitive generator g>=2; rho(g)=omega; "
            "eta is Legendre; rho(0)=eta(0)=0; J=sum_u rho(u)eta(1-u); "
            "j=-eta(-1)J; lambda_d=eta(d)rho(d); alpha_d=lambda_d*j",
        "bounds": {"split_prime_list": SPLIT_PRIMES, "inert_prime_list": INERT_PRIMES,
                   "all_nonzero_d_per_prime": True, "all_affine_x_y_per_d": True,
                   "excluded_bad_primes": [2, 3], "deck_word_length_through": MAX_DECK_PATH_LENGTH},
        "Eisenstein_self_checks": self_checks, "split_primes": split, "inert_primes": inert,
        "deck_permutation": deck_checks(), "cellular_carrier": cellular, "totals": totals,
        "matrix_scope": "The displayed integral matrix is multiplication by alpha in the "
            "Eisenstein basis, not by itself a construction of etale cohomology or Frobenius.",
        "scope": "Finite corroboration for every nonzero twist at the explicit tested primes, "
            "and the fixed six-dart deck action. Not the uniform all-prime Jacobi/Frobenius "
            "theorem, a proof of arithmetic descent or purity, a global determinant comparison, "
            "or a proof of RH/GRH. No PDF, network, dependency, authentication or random seed required."}


def run(write_output=True):
    result = checks()
    assert result["split_primes"]["7"]["j"] == [3, 2]
    assert result["split_primes"]["7"]["models"]["2"]["alpha"] == [-1, -3]
    assert result["cellular_carrier"]["split_twist_chain_checks"] == 516
    if write_output:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(result, indent=2, default=str)+"\n")
        print(json.dumps({"output": str(OUT), "totals": result["totals"],
                          "p7_j": result["split_primes"]["7"]["j"],
                          "p7_d2_alpha": result["split_primes"]["7"]["models"]["2"]["alpha"],
                          "deck_centralizer_order": result["deck_permutation"]["centralizer_order"],
                          "scope": result["scope"]}, indent=2))
    return result


if __name__ == "__main__":
    run()
