#!/usr/bin/env python3
"""Independent standard-library review: no production imports or LP solver.

Rebuilds sparse constraints from words; checks rational witnesses, then
separately exhausts vocabulary subsets with a forward shortest-path routine.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / 'outputs/checks/2026-11-03-convextok/results.json'


def cost(word, vocab):
    best = [0] + [len(word) + 1] * len(word)
    for end in range(1, len(word) + 1):
        best[end] = best[end - 1] + 1
        for token in vocab:
            start = end - len(token)
            if start >= 0 and tuple(word[start:end]) == token:
                best[end] = min(best[end], best[start] + 1)
    return best[-1]


def g_cost(word, vocab):
    count = index = 0
    while index < len(word):
        lens = [len(t) for t in vocab if tuple(word[index:index+len(t)]) == t]
        index += max([1] + lens)
        count += 1
    return count


def sparse_dot(row, vector):
    return sum((v * vector[i] for i, v in row.items()), F(0))


def system(words, tokens, budget):
    edges = []
    offsets = []
    offset = 0
    for wi, word in enumerate(words):
        offsets.append(offset)
        offset += len(word) + 1
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                part = tuple(word[start:end])
                if len(part) == 1 or part in tokens:
                    edges.append((wi, start, end, part))
    n = len(edges) + len(tokens)
    eq = [{} for _ in range(offset)]
    rhs = [0] * offset
    le = []
    for wi, word in enumerate(words):
        rhs[offsets[wi]] = -1
        rhs[offsets[wi]+len(word)] = 1
    for ei, (wi, start, end, part) in enumerate(edges):
        eq[offsets[wi]+start][ei] = -1
        eq[offsets[wi]+end][ei] = 1
        if len(part) > 1:
            le.append({ei: 1, len(edges)+tokens.index(part): -1})
    h = [0] * len(le) + [budget] + [1] * n
    le.append({len(edges)+ti: 1 for ti in range(len(tokens))})
    le.extend({i: 1} for i in range(n))
    return edges, eq, rhs, le, h


def exact_certificate(words, tokens, budget, lp):
    edges, eq, b, le, h = system(words, tokens, budget)
    cert = lp['certificate']
    x, y, z = ([F(v) for v in cert[k]] for k in ('x', 'y', 'z'))
    n = len(edges)+len(tokens)
    assert (len(x), len(y), len(z)) == (n, len(b), len(h))
    assert all(0 <= v <= 1 for v in x)
    assert all(v <= 0 for v in z)
    assert all(sparse_dot(row, x) == v for row, v in zip(eq, b))
    assert all(sparse_dot(row, x) <= v for row, v in zip(le, h))
    lhs = [F(0)] * n
    for duals, rows in ((y, eq), (z, le)):
        for dual, row in zip(duals, rows):
            for i, value in row.items():
                lhs[i] += dual * value
    q = [1]*len(edges) + [0]*len(tokens)
    assert all(v <= c for v, c in zip(lhs, q))
    primal = sum(x[:len(edges)], F(0))
    lower = sum((v*d for v, d in zip(b, y)), F(0)) + sum((v*d for v, d in zip(h, z)), F(0))
    assert primal == lower == F(lp['value']) == F(cert['value'])
    assert lp['colours'] == list(map(str, x[len(edges):]))
    assert len(lp['edges']) == len(edges)
    for e, saved, flow in zip(edges, lp['edges'], x):
        wi, start, end, part = e
        assert (saved['word'], saved['start'], saved['end'], tuple(saved['token'])) == e
        assert F(saved['flow']) == flow
    return primal, x[len(edges):], len(h), len(edges)


def cycles(perm):
    remaining = set(range(len(perm)))
    result = []
    while remaining:
        start = min(remaining)
        walk, v = [], start
        while v not in walk:
            walk.append(v)
            remaining.remove(v)
            v = perm[v]
        assert v == start
        result.append(walk)
    return result


def main():
    data = json.loads(DATA.read_text())
    summary = []
    certificates = subsets_exact_size = subsets_at_most = 0
    for case in data['cases']:
        words = [tuple(w) for w in case['words']]
        tokens = [tuple(t) for t in case['tokens']]
        assert len(tokens) == len(set(tokens))
        allparts = {w[i:j] for w in words for i in range(len(w)) for j in range(i+2, len(w)+1)}
        if 'genus' in case['context']:
            c = case['context']
            m, genus = c['m'], c['genus']
            assert m == 2*genus+1
            sigma = [m*(i//m)+(i+1)%m for i in range(2*m)]
            tau = [m*(i//m)+(i-1)%m for i in range(2*m)]
            alpha = [(i+m)%(2*m) for i in range(2*m)]
            phi = [alpha[tau[i]] for i in range(2*m)]
            assert (sigma, tau, alpha, phi) == (c['sigma'], c['tau'], c['alpha'], c['phi'])
            assert len(cycles(sigma)) == 2 and len(cycles(alpha)) == m and len(cycles(phi)) == 1
            assert len(cycles(sigma))-m+len(cycles(phi)) == 2-2*genus
            assert c['order_rank'] == 2*m*m
            assert set(tokens) == {t for t in allparts if len(t) <= 3}
            assert words[0] == words[1]
            for word in words:
                darts = [int(s.removeprefix('a')) for s in word]
                assert all(s == 'a'+str(h) for s, h in zip(word, darts))
                assert all(j == tau[i] and j != phi[i] for i, j in zip(darts, darts[1:]))
        else:
            assert set(tokens) == allparts
        results = []
        for result in case['results']:
            k = result['budget']
            value, colours, nr, ne = exact_certificate(words, tokens, k, result['lp'])
            certificates += 1
            minima = []
            # Exhaust *all* sizes rather than use production's monotonicity shortcut.
            for size in range(min(k, len(tokens))+1):
                vals = [sum(cost(w, subset) for w in words) for subset in combinations(tokens, size)]
                subsets_at_most += len(vals)
                if size == min(k, len(tokens)):
                    subsets_exact_size += len(vals)
                    assert len(vals) == result['integer']['subsets_checked']
                minima.extend(vals)
            optimum = min(minima)
            assert optimum == result['integer']['value'] and value <= optimum
            assert sum(cost(w, set(map(tuple, result['integer']['vocabulary']))) for w in words) == optimum
            expected = {
                'Det': sorted(range(len(tokens)), key=lambda i: (-colours[i], tokens[i]))[:k],
                'Bias': sorted(range(len(tokens)), key=lambda i: (-colours[i]/len(tokens[i]), tokens[i]))[:k],
                'Int': [i for i, v in enumerate(colours) if v == 1],
            }
            for method, rounded in result['lp']['rounded'].items():
                vocab = [tokens[i] for i in expected[method]]
                assert vocab == list(map(tuple, rounded['vocabulary'])) and len(vocab) <= k
                assert sum(cost(w, vocab) for w in words) == rounded['dp_count']
                assert sum(g_cost(w, vocab) for w in words) == rounded['greedy_count']
                for word, parts in zip(words, rounded['segments']):
                    assert tuple(s for part in parts for s in part) == word
                    assert all(len(p) == 1 or tuple(p) in vocab for p in parts)
            results.append(dict(K=k, lp=str(value), integer=optimum, occurrence_variables=ne, inequality_rows=nr))
        summary.append(dict(id=case['id'], results=results))
    byid = {row['id']: row for row in summary}
    assert byid['gap']['results'][-1]['lp'] == '10' and byid['gap']['results'][-1]['integer'] == 11
    assert byid['fraction']['results'][-1]['lp'] == '31/2' and byid['fraction']['results'][-1]['integer'] == 16
    paper = next(c for c in data['cases'] if c['id'] == 'paper')
    words = [tuple(w) for w in paper['words']]
    assert sum(map(len, words)) == 15
    # The first unique most frequent adjacent pair is ab; after merging it,
    # every remaining pair has frequency one, so the next two saves are 1 each.
    freq = {}
    for word in words:
        for a, b in zip(word, word[1:]):
            freq[(a,b)] = freq.get((a,b), 0)+1
    assert freq[('a','b')] == 3 and all(v <= 2 for key, v in freq.items() if key != ('a','b'))
    assert paper['results'][-1]['bpe']['merge_count'] == 15-3-1-1 == 10
    assert sum(cost(w, [tuple('bc'), tuple('bd'), tuple('be')]) for w in words) == 9
    assert byid['paper']['results'][-1]['lp'] == '9'
    output = dict(status='PASS', independent_of_production_imports=True,
                  solver_used=False, exact_primal_dual_certificates=certificates,
                  same_size_subsets=subsets_exact_size, all_at_most_subsets=subsets_at_most,
                  source_sha256=hashlib.sha256(DATA.read_bytes()).hexdigest(), cases=summary)
    destination = Path(__file__).with_name('oracle.json')
    destination.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
