#!/usr/bin/env python3
"""Exact finite diagnostics for separately specified infinite/topological models.

Run with the existing .tools/book-quantum-cpu/bin/python. No random input,
installation, external services or writes outside this example directory.
General proofs and category conventions are in planning/learned-frontier/geometry.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import argparse
import json
import sympy as s


def reduce_word(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def group_mul(g, h):
    return reduce_word(g + h)


def inverse(g):
    return tuple(-x for x in reversed(g))


# Theta graph A--B has three undirected edges, positively directed A to B.
# Vertex coordinates (g,side) use g in free group on x=1,y=2, side A=0,B=1.
VOLTAGE = {1: (), 2: (1,), 3: (2,)}


def lift_step(vertex, edge):
    g, side = vertex
    assert (edge > 0) == (side == 0)
    voltage = VOLTAGE[abs(edge)]
    return (group_mul(g, voltage if edge > 0 else inverse(voltage)), 1-side)


def lift(path, start=((), 0)):
    vertex = start
    for edge in path:
        vertex = lift_step(vertex, edge)
    return vertex


def theta_check(radius=8):
    levels = [[()]]
    seen = {lift(()): ()}
    for n in range(1, radius+1):
        level = []
        sign = 1 if n % 2 else -1
        for path in levels[-1]:
            for label in (1, 2, 3):
                edge = sign*label
                if path and edge == -path[-1]:
                    continue
                q = path+(edge,)
                vertex = lift(q)
                assert vertex not in seen
                seen[vertex] = q
                level.append(q)
                for deck in ((), (1,), (-1,), (2, 1), (-2, 1, 2)):
                    assert lift(q, (deck, 0)) == (group_mul(deck, vertex[0]), vertex[1])
        assert len(level) == 3*2**(n-1)
        levels.append(level)
    # Backtracking cancels; all three edge labels have unique lifts at a vertex.
    for vertex in seen:
        sign = 1 if vertex[1] == 0 else -1
        neighbours = [lift_step(vertex, sign*edge) for edge in (1, 2, 3)]
        assert len(set(neighbours)) == 3
        for edge, target in zip((1, 2, 3), neighbours):
            assert lift_step(target, -sign*edge) == vertex
    # A finite-supported representation: two isolated a-edge interval modules.
    # Pushdown has A=B=Q^2, a=I, b=c=0. Thus any 2x2 matrix is an endomorphism.
    grades = [(), (1,)]
    f = s.Matrix(2, 2, s.symbols('f:4'))
    for arrow in (s.eye(2), s.zeros(2), s.zeros(2)):
        assert f*arrow == arrow*f
    homogeneous = Counter(group_mul(h, inverse(g)) for h in grades for g in grades)
    assert homogeneous == {(): 2, (1,): 1, (-1,): 1}
    parts = []
    for degree in homogeneous:
        part = s.Matrix(2, 2, lambda i, j: f[i, j]
                        if group_mul(grades[i], inverse(grades[j])) == degree else 0)
        parts.append(part)
    assert sum(parts, s.zeros(2)) == f
    return dict(radius=radius, vertices=len(seen), sphere_sizes=list(map(len, levels)),
                degree=3, cayley_F2_degree=4, pushdown_end_dimension=4,
                cover_end_dimension=2,
                deck_components={str(k): v for k, v in homogeneous.items()},
                scope='Tree cover of theta graph; graph-quiver representations, not dessin algebra cover')


def pants_check():
    # Q[t]/t^2, ordered basis (1,t), epsilon(1)=0, epsilon(t)=1.
    mu = s.Matrix([[1, 0, 0, 0], [0, 1, 1, 0]])
    delta = s.Matrix([[0, 0], [1, 0], [1, 0], [0, 1]])
    unit, counit, ident = s.Matrix([1, 0]), s.Matrix([[0, 1]]), s.eye(2)
    kron = s.kronecker_product
    swap = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    assert mu*kron(mu, ident) == mu*kron(ident, mu)
    assert kron(delta, ident)*delta == kron(ident, delta)*delta
    assert delta*mu == kron(mu, ident)*kron(ident, delta)
    assert delta*mu == kron(ident, mu)*kron(delta, ident)
    assert mu*swap == mu and swap*delta == delta
    assert mu*kron(unit, ident) == mu*kron(ident, unit) == ident
    assert kron(counit, ident)*delta == kron(ident, counit)*delta == ident
    pairing = counit*mu
    assert s.Matrix(2, 2, list(pairing)).det() == -1
    handle = mu*delta
    amplitudes = [(counit*(handle**g)*unit)[0] for g in range(5)]
    assert amplitudes == [0, 2, 0, 0, 0]
    assert mu.T*mu != s.eye(4) and delta.T*delta != ident and delta != mu.T
    # Exact positive-metric completion to a heralded isometry for K=mu/sqrt(2).
    K = mu/s.sqrt(2)
    failure = s.Matrix([[1/s.sqrt(2), 0, 0, 0],
                        [0, s.Rational(1, 2), -s.Rational(1, 2), 0],
                        [0, -s.Rational(1, 2), s.Rational(1, 2), 0],
                        [0, 0, 0, 1]])
    V = K.col_join(failure)
    assert s.simplify(V.T*V) == s.eye(4)
    probabilities = [(v.T*K.T*K*v)[0] for v in [s.eye(4)[:, j] for j in range(4)]]
    assert probabilities == [s.Rational(1, 2)]*3+[0]
    return dict(algebra='Q[t]/(t^2)', mu=mu.tolist(), delta=delta.tolist(),
                unit=list(unit), counit=list(counit),
                associativity=True, coassociativity=True, frobenius=True,
                genus_0_to_4_closed_amplitudes=amplitudes,
                physical_completion_shape=list(V.shape),
                basis_postselection_probabilities=list(map(str, probabilities)),
                scope='Oriented finite-state 2D TQFT, neither unitary CFT nor string/holographic model')


def chsh_check():
    X, Z = s.Matrix([[0, 1], [1, 0]]), s.diag(1, -1)
    A0, A1, B0, B1 = Z, X, (Z+X)/s.sqrt(2), (Z-X)/s.sqrt(2)
    kron = s.kronecker_product
    T = kron(A0, B0+B1)+kron(A1, B0-B1)
    psi = s.Matrix([1, 0, 0, 1])/s.sqrt(2)
    for O in (A0, A1, B0, B1):
        assert O == O.T and s.simplify(O*O) == s.eye(2)
    comm = lambda a, b: a*b-b*a
    assert s.simplify(T*T-(4*s.eye(4)-kron(comm(A0, A1), comm(B0, B1)))) == s.zeros(4)
    assert s.simplify((psi.T*T*psi)[0]) == 2*s.sqrt(2)
    classical = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        score = a0*(b0+b1)+a1*(b0-b1)
        wins = sum((a0 if x == 0 else a1)*(b0 if y == 0 else b1) == (-1)**(x*y)
                   for x, y in product((0, 1), repeat=2))
        assert s.Rational(wins, 4) == s.Rational(1, 2)+s.Rational(score, 8)
        classical.append(wins)
    assert max(classical) == 3
    eig = T.eigenvals()
    assert eig == {-2*s.sqrt(2): 1, 0: 2, 2*s.sqrt(2): 1}
    return dict(classical_strategies=len(classical), classical_value='3/4',
                quantum_value='(2+sqrt(2))/4', bell_score='2*sqrt(2)',
                operator_eigenvalues={str(k): v for k, v in eig.items()},
                scope='Finite exact CHSH illustration; does not witness Cqa versus Cqc separation')


M = 5


def module(support, arrows=None):
    dims = [int(i in support) for i in range(M)]
    matrices = {(b, i): s.zeros(dims[(i-1) % M], dims[i])
                for b in (0, 1) for i in range(M)}
    for b, i in arrows or []:
        matrices[b, i][0, 0] = 1
    for b in (0, 1):
        for i in range(M):
            assert matrices[1-b, (i-1) % M]*matrices[b, i] == s.zeros(dims[(i-2) % M], dims[i])
    return dims, matrices


def hom_dim(source, target):
    sd, sa = source
    td, ta = target
    variables = s.symbols('h:'+str(sum(a*b for a, b in zip(sd, td))))
    pos, hs = 0, []
    for a, b in zip(sd, td):
        hs.append(s.Matrix(b, a, variables[pos:pos+a*b]))
        pos += a*b
    equations = []
    for branch in (0, 1):
        for i in range(M):
            equations.extend(hs[(i-1) % M]*sa[branch, i]-ta[branch, i]*hs[i])
    if not variables:
        return 0
    coefficient, _ = s.linear_eq_to_matrix(equations, variables)
    return len(variables)-coefficient.rank()


def resolution_words(kind, n):
    """Labels for projective summands, with differential read from the last tail.

    P0=e0A. S0: two alternating forbidden indexing chains.
    B=(a0 interval): first kernel generator b0, second a0*a4;
    tails continue by the unique forbidden successor. Full labels of length
    greater than the initial generator are zero in A; never multiply them as
    differential entries. Only the final arrow is the next differential.
    """
    if n == 0:
        return [()]
    if kind == 'simple':
        return [tuple((first ^ (r % 2), -r % M) for r in range(n)) for first in (0, 1)]
    assert kind == 'branch'
    return [tuple([(1, 0)]+[(1-r % 2, -r % M) for r in range(1, n)]),
            tuple([(0, 0), (0, 4)]+[(r % 2, -(r+1) % M) for r in range(1, n)])]


def endpoint(word):
    return (word[-1][1]-1) % M if word else 0


def action(N, word):
    dims, arrows = N
    start = word[0][1] if word else 0
    out = s.eye(dims[start])
    for letter in word:
        out = arrows[letter]*out
    return out


def cochain(kind, N, n):
    """Hom(P_n,N) -> Hom(P_{n+1},N), right modules in travel convention."""
    dims, _ = N
    here, nxt = resolution_words(kind, n), resolution_words(kind, n+1)
    if n == 0:
        return s.Matrix.vstack(*(action(N, w) for w in nxt))
    blocks = [action(N, (w[-1],)) for w in nxt]
    out = s.zeros(sum(dims[endpoint(w)] for w in nxt), sum(dims[endpoint(w)] for w in here))
    row = col = 0
    for block in blocks:
        out[row:row+block.rows, col:col+block.cols] = block
        row += block.rows
        col += block.cols
    return out


def ext_tor(kind, N, through=12):
    dims, _ = N
    maps = [cochain(kind, N, n) for n in range(through+1)]
    for n in range(through):
        assert maps[n+1]*maps[n] == s.zeros(maps[n+1].rows, maps[n].cols)
    ext, tor = [], []
    for n in range(through+1):
        size = sum(dims[endpoint(w)] for w in resolution_words(kind, n))
        incoming = 0 if n == 0 else maps[n-1].rank()
        value = size-maps[n].rank()-incoming
        # P_n tensor D(N): boundary is transpose of the displayed Hom map.
        tensor_boundary = s.zeros(0, size) if n == 0 else maps[n-1].T
        tensor_next = maps[n].T
        tor_value = size-tensor_boundary.rank()-tensor_next.rank()
        assert value == tor_value and value >= 0
        ext.append(value)
        tor.append(tor_value)
    return dict(ext=ext, tor_against_dual_target=tor)


def dessin_check():
    # y^2=x^5-1, beta=x^5: sigma=(01234)(56789), alpha pairs i,i+5.
    sigma = tuple(list(range(1, 5))+[0]+list(range(6, 10))+[5])
    alpha = tuple((i+5) % 10 for i in range(10))
    phi = tuple(alpha[sigma.index(i)] for i in range(10))
    cycle, seen = [], set()
    i = 0
    while i not in seen:
        seen.add(i)
        cycle.append(i)
        i = phi[i]
    assert len(cycle) == 10 and 2-5+1 == 2-2*2
    simple0, simple4 = module({0}), module({4})
    branch = module({0, 4}, [(0, 0)])
    assert hom_dim(branch, branch) == 1
    assert hom_dim(simple0, branch) == 0
    assert hom_dim(branch, simple0) == 1
    assert hom_dim(simple4, branch) == 1
    # Actual normal-path multiplication; length zero is an idempotent.
    def normal(start, branch_label, length):
        return (start, branch_label if length else None, length)

    def multiply(p, q):
        i, b, length = p
        j, c, tail_length = q
        if (i-length) % M != j:
            return None
        if length and tail_length and b != c:
            return None
        return normal(i, b if length else c, length+tail_length)

    # Check normal-form kernels in finite windows; the prose proof is unbounded.
    kernel_checks = 0
    for start in range(M):
        for first_branch in (0, 1):
            arrow = normal(start, first_branch, 1)
            basis = [normal((start-1) % M, None, 0)]+[
                normal((start-1) % M, b, length) for b in (0, 1) for length in range(1, 13)]
            kernel = {p for p in basis if multiply(arrow, p) is None}
            expected = {p for p in basis if p[1] == 1-first_branch and p[2] >= 1}
            assert kernel == expected
            surviving = [multiply(arrow, p) for p in basis if p not in kernel]
            assert len(surviving) == len(set(surviving))
            kernel_checks += len(basis)
    for kind in ('simple', 'branch'):
        for n in range(2, 14):
            for previous, word in zip(resolution_words(kind, n-1), resolution_words(kind, n)):
                assert word[:-1] == previous
                assert word[-2][0] != word[-1][0]
                assert endpoint(previous) == word[-1][1]
    # Test the actual B presentation kernel: only e0 and a0 survive P0 -> B.
    for b in (0, 1):
        for length in range(1, 13):
            word = tuple((b, -r % M) for r in range(length))
            killed = action(branch, word) == s.zeros(branch[0][-length % M], 1)
            assert killed == (b == 1 or length >= 2)
    # A genuine nonsplit extension 0 -> B -> E -> B -> 0, not a dimension claim.
    edims = [2, 0, 0, 0, 2]
    earrows = {(b, i): s.zeros(edims[(i-1) % M], edims[i])
               for b in (0, 1) for i in range(M)}
    earrows[0, 0] = s.eye(2)
    earrows[1, 0] = s.Matrix([[0, 1], [0, 0]])
    for b in (0, 1):
        for i in range(M):
            assert earrows[1-b, (i-1) % M]*earrows[b, i] == s.zeros(edims[(i-2) % M], edims[i])
    inc, proj = s.Matrix([1, 0]), s.Matrix([[0, 1]])
    for arrow, scalar in ((earrows[0, 0], 1), (earrows[1, 0], 0)):
        assert arrow*inc == inc*scalar and proj*arrow == scalar*proj
    assert proj*inc == s.zeros(1)
    unknowns = s.symbols('section:4')
    section0, section4 = s.Matrix(unknowns[:2]), s.Matrix(unknowns[2:])
    equations = list(section4-section0)+list(earrows[1, 0]*section0)
    equations += list(proj*section0-s.ones(1))+list(proj*section4-s.ones(1))
    coefficients, rhs = s.linear_eq_to_matrix(equations, unknowns)
    assert coefficients.rank() < coefficients.row_join(rhs).rank()
    cases = {}
    for name, N in [('S0', simple0), ('S4', simple4), ('B', branch)]:
        for kind in ('simple', 'branch'):
            cases[kind+'->'+name] = ext_tor(kind, N)
    for j in range(M):
        result = ext_tor('simple', module({j}))['ext']
        assert result[0] == int(j == 0)
        for n in range(1, len(result)):
            assert result[n] == 2*int(j == -n % M)
    assert cases['branch->B']['ext'][:2] == [1, 1]
    return dict(genus=2, quiver_vertices=5, face_cycle=cycle,
                algebra='Infinite polynomial locally gentle two-branch dessin algebra; right modules',
                Hom=dict(B_B=1, S0_B=0, B_S0=1, S4_B=1),
                projective_resolution_degrees_checked=12,
                normal_kernel_samples=kernel_checks, nonsplit_branch_self_extension=True,
                cases=cases,
                scope='Ordinary polynomial module Ext/Tor; no completion, AR equivalence or HMS claim')


def check():
    return dict(passed=True, arithmetic='SymPy exact Q and Q(sqrt(2)); deterministic',
                seed=None, theta=theta_check(), pants=pants_check(),
                chsh=chsh_check(), dessin=dessin_check())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent/'outputs'/'exact.json')
    args = parser.parse_args()
    result = check()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, default=str)+'\n')
    print(json.dumps(dict(passed=result['passed'], theta_vertices=result['theta']['vertices'],
                         pants_axioms=True, CHSH=result['chsh']['quantum_value'],
                         resolution_degrees=result['dessin']['projective_resolution_degrees_checked'],
                         output=str(args.output)), indent=2))
