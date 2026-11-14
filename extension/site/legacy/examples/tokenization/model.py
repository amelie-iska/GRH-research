"""Original small ConvexTok formulation, exact certificates and segmenters.

CPU only; no training, installs, network, or import-time writes. A symbol is
one string element (an arrow label in the surface examples), not its UTF-8 bytes.
"""
from fractions import Fraction as Q
from itertools import combinations

import numpy as np
from scipy.optimize import linprog


def candidates(words):
    return sorted({tuple(w[i:j]) for w in words for i in range(len(w))
                   for j in range(i + 2, len(w) + 1)})


def segment(word, vocabulary, greedy=False):
    """Exact shortest segmentation; ties lexicographic. Greedy = longest first."""
    word = tuple(word)
    vocab = {tuple(t) for t in vocabulary} | {(s,) for s in word}
    if greedy:
        out, i = [], 0
        while i < len(word):
            token = min((t for t in vocab if word[i:i + len(t)] == t),
                        key=lambda t: (-len(t), t))
            out.append(token)
            i += len(token)
        return out
    best = [None] * (len(word) + 1)
    best[-1] = []
    for i in range(len(word) - 1, -1, -1):
        options = [[t] + best[i + len(t)] for t in vocab
                   if word[i:i + len(t)] == t]
        best[i] = min(options, key=lambda ts: (len(ts), ts))
    return best[0]


def token_count(words, vocabulary, greedy=False):
    return sum(len(segment(w, vocabulary, greedy)) for w in words)


def integer_optimum(words, tokens, budget):
    """Exhaust every subset of exactly min(K,|C|): monotonicity covers <=K."""
    checked, best = 0, None
    for vocab in combinations(tokens, min(budget, len(tokens))):
        checked += 1
        item = (token_count(words, vocab), vocab)
        if best is None or item < best:
            best = item
    return dict(value=best[0], vocabulary=list(best[1]), subsets_checked=checked)


def bpe(words, budget):
    """Frequency-driven pair merging with lexicographic tie and L->R overlap."""
    rows = [[(s,) for s in w] for w in words]
    vocab = []
    for _ in range(budget):
        counts = {}
        for row in rows:
            for pair in zip(row, row[1:]):
                counts[pair] = counts.get(pair, 0) + 1
        if not counts:
            break
        pair = min(counts, key=lambda p: (-counts[p], p))
        merged = pair[0] + pair[1]
        vocab.append(merged)
        for n, row in enumerate(rows):
            i, out = 0, []
            while i < len(row):
                if i + 1 < len(row) and (row[i], row[i + 1]) == pair:
                    out.append(merged)
                    i += 2
                else:
                    out.append(row[i])
                    i += 1
            rows[n] = out
    return dict(vocabulary=vocab, merge_count=sum(map(len, rows)),
                dp_count=token_count(words, vocab))


def formulate(words, tokens, budget):
    """min q*x, A*x=b, G*x<=h, x>=0. G includes x<=1 explicitly.

    Separate unit flows per word equal the paper's joined-terminal DAG: no
    candidate edge crosses a word boundary. Each occurrence has x_e<=c_t.
    Repeated words are retained, not de-duplicated without weights.
    """
    if not words or any(not word for word in words):
        raise ValueError('The finite teaching LP requires a nonempty corpus of nonempty words')
    tokens = [tuple(t) for t in tokens]
    edges, offsets, vertex_count = [], [], 0
    for n, word in enumerate(words):
        offsets.append(vertex_count)
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                t = tuple(word[i:j])
                if j == i + 1 or t in tokens:
                    edges.append(dict(word=n, start=i, end=j, token=t,
                                      colour=None if len(t) == 1 else tokens.index(t)))
        vertex_count += len(word) + 1
    ne, nc = len(edges), len(tokens)
    A = np.zeros((vertex_count, ne + nc), dtype=int)
    b = np.zeros(vertex_count, dtype=int)
    capacities = []
    for n, word in enumerate(words):
        b[offsets[n]], b[offsets[n] + len(word)] = -1, 1
    for e, edge in enumerate(edges):
        offset = offsets[edge['word']]
        A[offset + edge['start'], e] = -1
        A[offset + edge['end'], e] = 1
        if edge['colour'] is not None:
            row = np.zeros(ne + nc, dtype=int)
            row[e], row[ne + edge['colour']] = 1, -1
            capacities.append(row)
    budget_row = np.r_[np.zeros(ne, dtype=int), np.ones(nc, dtype=int)]
    G = np.vstack([*capacities, budget_row, np.eye(ne + nc, dtype=int)])
    h = np.r_[np.zeros(len(capacities), dtype=int), budget,
              np.ones(ne + nc, dtype=int)]
    q = np.r_[np.ones(ne, dtype=int), np.zeros(nc, dtype=int)]
    return dict(A=A, b=b, G=G, h=h, q=q, edges=edges, tokens=tokens,
                budget_row=len(capacities))


def rational(vector):
    return [Q(float(v)).limit_denominator(1_000_000) for v in vector]


def dot(row, vector):
    return sum((int(a) * v for a, v in zip(row, vector) if a), Q(0))


def certify(problem, x, y, z):
    """Independent exact rational primal/dual validation; no float tolerances."""
    A, b, G, h, q = (problem[k] for k in ('A', 'b', 'G', 'h', 'q'))
    assert len(x) == len(q) and len(y) == len(b) and len(z) == len(h)
    assert all(v >= 0 for v in x) and all(v <= 0 for v in z)
    assert all(dot(row, x) == int(rhs) for row, rhs in zip(A, b))
    assert all(dot(row, x) <= int(rhs) for row, rhs in zip(G, h))
    assert all(dot(A[:, j], y) + dot(G[:, j], z) <= int(q[j])
               for j in range(len(q)))
    primal, dual = dot(q, x), dot(b, y) + dot(h, z)
    assert primal == dual
    return primal


def solve(words, tokens, budget):
    p = formulate(words, tokens, budget)
    result = linprog(p['q'], A_ub=p['G'], b_ub=p['h'], A_eq=p['A'],
                     b_eq=p['b'], bounds=(0, None), method='highs')
    assert result.success, result.message
    x, y, z = map(rational, (result.x, result.eqlin.marginals,
                             result.ineqlin.marginals))
    value = certify(p, x, y, z)
    ne = len(p['edges'])
    c = x[ne:]
    det = sorted(range(len(tokens)), key=lambda i: (-c[i], tokens[i]))[:budget]
    bias = sorted(range(len(tokens)), key=lambda i: (-c[i] / len(tokens[i]), tokens[i]))[:budget]
    # Exact certificate means no approximate-one threshold is needed here.
    integral = [i for i, v in enumerate(c) if v == 1]
    rounded = {}
    for label, ids in [('Det', det), ('Bias', bias), ('Int', integral)]:
        vocab = [tokens[i] for i in ids]
        rounded[label] = dict(vocabulary=vocab, dp_count=token_count(words, vocab),
                              greedy_count=token_count(words, vocab, True),
                              segments=[segment(w, vocab) for w in words])
    return dict(value=str(value), numeric_value=float(value),
                colours=[str(v) for v in c],
                edges=[dict(e, flow=str(x[i])) for i, e in enumerate(p['edges'])],
                certificate=dict(x=list(map(str, x)), y=list(map(str, y)),
                                 z=list(map(str, z)), value=str(value),
                                 convention='min qx; Ax=b; Gx<=h; x>=0; z<=0'),
                variables=len(x), equality_rows=len(y), inequality_rows=len(z),
                rounded=rounded)


def surface_case(genus):
    """Finite nonzero path corpus in A_g, not a truncation or a new algebra."""
    m = 2 * genus + 1
    sigma = [(i // m) * m + (i + 1) % m for i in range(2 * m)]
    tau = [(i // m) * m + (i - 1) % m for i in range(2 * m)]
    alpha = [(i + m) % (2 * m) for i in range(2 * m)]
    phi = [alpha[tau[i]] for i in range(2 * m)]
    def path(start, length):
        out, h = [], start
        for _ in range(length):
            out.append(f'a{h}')
            h = tau[h]
        return tuple(out)
    # Repeated motifs on both actual permitted m-cycles; <=3-arrow candidates.
    words = [path(0, m + 2), path(0, m + 2), path(m - 1, 4),
             path(m, m + 2), path(2 * m - 1, 4)]
    tokens = [t for t in candidates(words) if len(t) <= 3]
    seen, h = set(), 0
    while h not in seen:
        seen.add(h)
        h = phi[h]
    assert len(seen) == 2 * m and h == 0
    assert 2 - m + 1 == 2 - 2 * genus
    for word in words:
        darts = [int(s[1:]) for s in word]
        assert all(y == tau[x] and y != phi[x] for x, y in zip(darts, darts[1:]))
    return dict(id=f'surface-g{genus}', label=f'Genus {genus} path corpus',
                words=words, tokens=tokens, max_budget=2,
                context=dict(genus=genus, m=m, sigma=sigma, alpha=alpha,
                             tau=tau, phi=phi, order_rank=2 * m * m,
                             candidate_limit=3,
                             scope='Finite arrow-word corpus of infinite polynomial locally gentle A_g; not a finite quotient.'))
