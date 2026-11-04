#!/usr/bin/env python3
"""Generate/validate the finite ConvexTok teaching examples. Existing bytes stay."""
import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from pathlib import Path

import numpy as np
import scipy

from model import (bpe, candidates, certify, formulate, integer_optimum,
                   segment, solve, surface_case, token_count)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs/checks/2026-11-03-convextok'


def definitions():
    cases = []
    for cid, label, rows, budget in [
        ('paper', 'Paper: greedy vocabulary trap', ['abc', 'abd', 'abe', 'bc', 'bd', 'be'], 3),
        ('gap', 'Original: a strict integrality gap', ['cbcbc', 'cbca', 'cbabac', 'caaab'], 2),
        ('fraction', 'Original: a fractional lower bound', ['aaaab', 'baaccb', 'aac', 'babaab', 'cbbbca'], 2),
    ]:
        words = list(map(tuple, rows))
        cases.append(dict(id=cid, label=label, words=words, tokens=candidates(words),
                          max_budget=budget, context=dict(
                              scope='All substrings allowed within each word; mandatory characters outside K.')))
    return cases + [surface_case(2), surface_case(4)]


def store(path, payload):
    data = (json.dumps(payload, indent=2, sort_keys=True) + '\n').encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        assert path.read_bytes() == data, f'Protected existing output differs: {path}'
    else:
        path.write_bytes(data)


def brute_segments(word, vocabulary):
    if not word:
        return [[]]
    vocab = set(map(tuple, vocabulary)) | {(c,) for c in word}
    return [[t] + tail for t in vocab if tuple(word[:len(t)]) == t
            for tail in brute_segments(word[len(t):], vocabulary)]


def focused_checks():
    checks = {}
    for empty in [[], [()], [tuple('a'), ()]]:
        try:
            formulate(empty, [], 0)
        except ValueError:
            pass
        else:
            raise AssertionError('Empty corpus/word must be rejected before LP construction')
    word = tuple('abcd')
    vocab = [tuple('ab'), tuple('bcd')]
    assert len(segment(word, vocab)) == 2
    assert len(segment(word, vocab, True)) == 3
    checks['greedy_counterexample'] = dict(word=word, vocabulary=vocab,
                                          dp=segment(word, vocab),
                                          greedy=segment(word, vocab, True))
    # Compare independent enumeration of every segmentation on every toy vocab.
    small = tuple('ababa')
    ts = candidates([small])
    n = 0
    for size in range(3):
        for vocabulary in combinations(ts, size):
            assert len(segment(small, vocabulary)) == min(map(len, brute_segments(small, vocabulary)))
            n += 1
    checks['independent_segmentations'] = n
    # A selected token may be used many times: p_e<=c_t is per occurrence.
    words, tokens = [tuple('abab')], [tuple('ab')]
    s = solve(words, tokens, 1)
    assert s['value'] == '2'
    assert sum(Q(e['flow']) for e in s['edges'] if len(e['token']) > 1) == 2
    checks['repeated_capacity_occurrences'] = 2
    p = formulate(words, tokens, 1)
    x, y, z = [list(map(Q, s['certificate'][k])) for k in ('x', 'y', 'z')]
    # Perturbing either witness must fail exact feasibility/objective equality.
    rejections = 0
    for key in ['x', 'y', 'z']:
        copies = {name: list(v) for name, v in [('x', x), ('y', y), ('z', z)]}
        copies[key][0] += Q(1, 7)
        try:
            certify(p, copies['x'], copies['y'], copies['z'])
        except AssertionError:
            rejections += 1
    assert rejections == 3
    checks['corrupt_certificate_rejections'] = rejections
    boundary = formulate([tuple('ab'), tuple('cd')], [tuple('bc')], 1)
    assert not any(e['token'] == tuple('bc') for e in boundary['edges'])
    checks['boundary_crossing_rejected'] = True
    # Same LP optimum need not force a particular token across optimal bases.
    degenerate = solve([tuple('abc')], [tuple('ab'), tuple('bc')], 1)
    assert degenerate['value'] == '2'
    assert integer_optimum([tuple('abc')], [tuple('ab'), tuple('bc')], 1)['value'] == 2
    checks['integral_colour_does_not_mean_universally_forced'] = True
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='write new deterministic evidence; refuse to change differing existing outputs')
    args = parser.parse_args()
    dataset = dict(schema='grh-convextok-v1',
                   source='https://arxiv.org/html/2605.22821v1',
                   seed=22821, cases=[], focused_checks=focused_checks(),
                   environment=dict(numpy=np.__version__, scipy=scipy.__version__),
                   scope='Original CPU finite examples and exact rational certificates, no upstream NLP benchmark reproduction.')
    total_subsets = total_certificates = 0
    for case in definitions():
        case['results'] = []
        previous_lp = previous_ip = float('inf')
        for budget in range(case['max_budget'] + 1):
            lp = solve(case['words'], case['tokens'], budget)
            ip = integer_optimum(case['words'], case['tokens'], budget)
            assert lp['numeric_value'] <= ip['value'] <= previous_ip
            assert lp['numeric_value'] <= previous_lp
            for round_result in lp['rounded'].values():
                assert len(round_result['vocabulary']) <= budget
                assert ip['value'] <= round_result['dp_count'] <= round_result['greedy_count']
                for word, pieces in zip(case['words'], round_result['segments']):
                    assert tuple(c for piece in pieces for c in piece) == tuple(word)
            # BPE can create >3-arrow tokens, so it is omitted for restricted surface candidates.
            baseline = bpe(case['words'], budget) if 'genus' not in case['context'] else None
            case['results'].append(dict(budget=budget, lp=lp, integer=ip, bpe=baseline))
            total_subsets += ip['subsets_checked']
            total_certificates += 1
            previous_lp, previous_ip = lp['numeric_value'], ip['value']
        dataset['cases'].append(case)
    byid = {case['id']: case for case in dataset['cases']}
    assert byid['paper']['results'][3]['lp']['value'] == '9'
    assert byid['paper']['results'][3]['bpe']['merge_count'] == 10
    assert byid['gap']['results'][2]['lp']['value'] == '10'
    assert byid['gap']['results'][2]['integer']['value'] == 11
    assert byid['fraction']['results'][2]['lp']['value'] == '31/2'
    assert byid['fraction']['results'][2]['integer']['value'] == 16
    assert byid['surface-g2']['results'][2]['integer']['value'] == 19
    assert byid['surface-g4']['results'][2]['integer']['value'] == 31
    summary = dict(cases=len(dataset['cases']), exact_primal_dual_certificates=total_certificates,
                   exhaustive_vocabulary_subsets=total_subsets,
                   focused=dataset['focused_checks'],
                   sources={str(Path(__file__).relative_to(ROOT)): hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                            'examples/tokenization/model.py': hashlib.sha256(Path(__file__).with_name('model.py').read_bytes()).hexdigest()})
    if args.write:
        store(OUT / 'results.json', dataset)
        store(OUT / 'checks.json', summary)
        store(ROOT / 'web/data/convextok.json', dataset)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
