#!/usr/bin/env python3
"""Exact HLS quotient meshes and finite jets of the actual nodal AR diagram.

The almost-split factorization properties are proved in the accompanying prose.
This diagnostic checks actual representations, signed maps and exactness; it
does not infer ambient AR transfer, infinite exactness, or arithmetic from ranks.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

from check_projective_resolutions import (
    zero, identity, add, scale, multiply, rank)


OUT = (Path(__file__).resolve().parents[1] /
       'outputs/checks/2026-11-03-dessins/diamond-checks.json')
ENDPOINTS = {'a': (1, 2), 'b': (2, 3), 'l': (1, 1), 'r': (3, 3),
             'back1': (2, 1), 'back2': (3, 2)}
# Travel-order strings.  a,b are the retained forward arrows, not reverse ones.
WORDS = {
    'w': (1, ('a', 'b')),
    'hw': (1, ('a', 'b', 'r-')),
    'wh': (3, ('r-', 'b-', 'a-', 'l', 'a', 'b')),
    'wc': (1, ('l-', 'a', 'b')),
    'cw': (1, ('a', 'b', 'r', 'b-', 'a-', 'l-')),
    'hwc': (1, ('l-', 'a', 'b', 'r-')),
    'cwc': (1, ('l-', 'a', 'b', 'r', 'b-', 'a-', 'l-')),
    'hwh': (3, ('r-', 'b-', 'a-', 'l', 'a', 'b', 'r-')),
    'cwh': (3, ('r-', 'b-', 'a-', 'l', 'a', 'b', 'r', 'b-', 'a-', 'l-')),
}
EXPECTED_DIMENSIONS = {
    'w': [1, 1, 1], 'hw': [1, 1, 2], 'wh': [2, 2, 3],
    'wc': [2, 1, 1], 'cw': [3, 2, 2], 'hwc': [2, 1, 2],
    'cwc': [4, 2, 2], 'hwh': [2, 2, 4], 'cwh': [4, 3, 4],
}
RELATIONS = (('l', 'l'), ('r', 'r'), ('a', 'back1'),
             ('back1', 'a'), ('b', 'back2'), ('back2', 'b'))
# source,target,first retained source index,exclusive last index,target offset,sign
MAPS = (
    ('cwc', 'wc', 0, 4, 0, 1), ('wc', 'hwc', 0, 4, 0, 1),
    ('cw', 'w', 0, 3, 0, 1), ('w', 'hw', 0, 3, 0, 1),
    ('cwh', 'wh', 0, 7, 0, 1), ('wh', 'hwh', 0, 7, 0, 1),
    ('cwc', 'cw', 1, 8, -1, -1), ('wc', 'w', 1, 4, -1, 1),
    ('hwc', 'hw', 1, 5, -1, -1), ('cw', 'cwh', 0, 7, 4, -1),
    ('w', 'wh', 0, 3, 4, 1), ('hw', 'hwh', 0, 4, 4, -1),
)
MESHES = (('cwc', 'wc', 'cw', 'w'), ('wc', 'hwc', 'w', 'hw'),
          ('cw', 'w', 'cwh', 'wh'), ('w', 'hw', 'wh', 'hwh'))


def hstack(a, b):
    assert len(a) == len(b)
    return [x + y for x, y in zip(a, b)]


def diagonal(a, b):
    return ([row + [Q(0)]*len(b[0]) for row in a] +
            [[Q(0)]*len(a[0]) + row for row in b])


def sparse(a):
    return [[i, j, str(v)] for i, row in enumerate(a)
            for j, v in enumerate(row) if v]


def string_module(start, word):
    vertices = [start]
    size = len(word)+1
    matrices = {a: zero(size, size) for a in ENDPOINTS}
    for j, letter in enumerate(word):
        inverse = letter.endswith('-')
        arrow = letter[:-1] if inverse else letter
        source, target = ENDPOINTS[arrow]
        assert vertices[-1] == (target if inverse else source)
        vertices.append(source if inverse else target)
        row, col = (j, j+1) if inverse else (j+1, j)
        matrices[arrow][row][col] += Q(1)
    return {'vertices': vertices, 'matrices': matrices}


def check_exact(first, second, source_dimension, target_dimension):
    middle_dimension = len(first)
    assert len(second[0]) == middle_dimension
    assert multiply(second, first) == zero(target_dimension, source_dimension)
    first_rank, second_rank = rank(first), rank(second)
    assert first_rank == source_dimension
    assert second_rank == target_dimension
    assert first_rank == middle_dimension-second_rank
    return {'source_dimension': source_dimension,
            'middle_dimension': middle_dimension,
            'target_dimension': target_dimension,
            'injection_rank': first_rank, 'surjection_rank': second_rank,
            'middle_kernel_dimension': middle_dimension-second_rank}


def hls_checks():
    modules, maps = {}, {}
    module_reports, map_reports, meshes = [], [], []
    for name, (start, word) in WORDS.items():
        module = string_module(start, word)
        vertices, matrices = module['vertices'], module['matrices']
        dimensions = [vertices.count(i) for i in (1, 2, 3)]
        assert dimensions == EXPECTED_DIMENSIONS[name]
        for a, b in RELATIONS:
            assert multiply(matrices[b], matrices[a]) == zero(len(vertices), len(vertices))
        modules[name] = module
        module_reports.append({'label': name, 'travel_word': list(word),
                               'start_vertex': start, 'basis_vertices': vertices,
                               'dimension_vector': dimensions,
                               'total_dimension': len(vertices),
                               'arrow_nonzero_entries': {a: sparse(m) for a, m in matrices.items()}})
    for source, target, begin, end, offset, sign in MAPS:
        src, dst = modules[source], modules[target]
        matrix = zero(len(dst['vertices']), len(src['vertices']))
        for j in range(begin, end):
            k = j+offset
            assert src['vertices'][j] == dst['vertices'][k]
            matrix[k][j] = Q(sign)
        for arrow in ENDPOINTS:
            assert multiply(dst['matrices'][arrow], matrix) == multiply(matrix, src['matrices'][arrow])
        maps[source, target] = matrix
        map_reports.append({'source': source, 'target': target, 'sign': sign,
                            'shape': [len(matrix), len(matrix[0])],
                            'rank': rank(matrix), 'nonzero_entries': sparse(matrix)})
    for source, upper, lower, target in MESHES:
        src = modules[source]['vertices']
        middle = modules[upper]['vertices'] + modules[lower]['vertices']
        dst = modules[target]['vertices']
        first = maps[source, upper] + maps[source, lower]
        second = hstack(maps[upper, target], maps[lower, target])
        exact = check_exact(first, second, len(src), len(dst))
        vertex_checks = []
        for vertex in (1, 2, 3):
            si = [i for i, v in enumerate(src) if v == vertex]
            mi = [i for i, v in enumerate(middle) if v == vertex]
            ti = [i for i, v in enumerate(dst) if v == vertex]
            f = [[first[i][j] for j in si] for i in mi]
            g = [[second[i][j] for j in mi] for i in ti]
            vertex_checks.append({'vertex': vertex, **check_exact(f, g, len(si), len(ti))})
        meshes.append({'source': source, 'middle': [upper, lower], 'target': target,
                       **exact, 'vertex_boundary_ranks': vertex_checks,
                       'mesh_relation': 'sum of the two signed path composites is zero'})
    # A missing mesh sign must be detected; unsigned commuting squares are not complexes.
    wrong_first = maps['w', 'hw'] + maps['w', 'wh']
    wrong_second = hstack(scale(-1, maps['hw', 'hwh']), maps['wh', 'hwh'])
    assert multiply(wrong_second, wrong_first) != zero(8, 3)
    return module_reports, map_reports, meshes


def node_model(level):
    """Actual Lambda/(t^level) action in free R0 bases (1,x), x and y."""
    one, nil = identity(level), zero(level, level)
    t = zero(level, level)
    for j in range(level-1):
        t[j+1][j] = Q(1)
    lam_x = diagonal(nil, t)
    for i in range(level):
        lam_x[level+i][i] = Q(1)
    lam_y = diagonal(t, nil)
    for i in range(level):
        lam_y[level+i][i] = Q(-1)
    central = diagonal(t, t)
    assert add(lam_x, lam_y) == central
    assert multiply(lam_x, lam_y) == zero(2*level, 2*level)
    assert multiply(lam_y, lam_x) == zero(2*level, 2*level)
    assert multiply(lam_x, lam_x) == multiply(central, lam_x)
    assert multiply(lam_y, lam_y) == multiply(central, lam_y)
    actions = {'Lambda': {'x': lam_x, 'y': lam_y},
               'X': {'x': t, 'y': nil}, 'Y': {'x': nil, 'y': t}}
    rows = {'ending_X': ('Y', t + scale(-1, one), hstack(one, t), 'X'),
            'ending_Y': ('X', nil + one, hstack(one, nil), 'Y')}
    reports = {}
    for name, (source, inclusion, quotient, target) in rows.items():
        for generator in ('x', 'y'):
            assert multiply(actions['Lambda'][generator], inclusion) == multiply(inclusion, actions[source][generator])
            assert multiply(actions[target][generator], quotient) == multiply(quotient, actions['Lambda'][generator])
        reports[name] = check_exact(inclusion, quotient, level, level)
    return {'level': level, 'rows': rows, 'ranks': reports, 'actions': actions}


def node_checks():
    # Finite jets keep the source lattice and central action visible.  t:R_m->R_m
    # is NOT injective; use the correct t:R_m->R_(m+1) for column exactness.
    models = {level: node_model(level) for level in range(1, 6)}
    diagrams = []
    for level in range(1, 5):
        upper, middle, fiber = models[level], models[level+1], models[1]
        embedding = zero(level+1, level)
        for j in range(level):
            embedding[j+1][j] = Q(1)
        constant = [[Q(j == 0) for j in range(level+1)]]
        vertical = {'X': embedding, 'Y': embedding,
                    'Lambda': diagonal(embedding, embedding)}
        reduction = {'X': constant, 'Y': constant,
                     'Lambda': diagonal(constant, constant)}
        columns = {name: check_exact(vertical[name], reduction[name],
                                     level*(2 if name == 'Lambda' else 1),
                                     2 if name == 'Lambda' else 1)
                   for name in ('Y', 'Lambda', 'X')}
        for row_name in ('ending_X', 'ending_Y'):
            source, top_in, top_out, target = upper['rows'][row_name]
            _, mid_in, mid_out, _ = middle['rows'][row_name]
            _, bot_in, bot_out, _ = fiber['rows'][row_name]
            assert multiply(mid_in, vertical[source]) == multiply(vertical['Lambda'], top_in)
            assert multiply(mid_out, vertical['Lambda']) == multiply(vertical[target], top_out)
            assert multiply(bot_in, reduction[source]) == multiply(reduction['Lambda'], mid_in)
            assert multiply(bot_out, reduction['Lambda']) == multiply(reduction[target], mid_out)
        diagrams.append({'upper_jet_level': level, 'middle_jet_level': level+1,
                         'bottom_jet_level': 1, 'vertical_map': 'multiplication by t into next jet',
                         'column_boundary_ranks': columns, 'commuting_squares': 8,
                         'upper_rows': upper['ranks'], 'middle_rows': middle['ranks'],
                         'bottom_rows': fiber['ranks']})
    fiber = models[1]
    assert fiber['rows']['ending_X'][1] == [[Q(0)], [Q(-1)]]
    assert fiber['rows']['ending_X'][2] == [[Q(1), Q(0)]]
    return {'order': 'Lambda=k[[x,y]]/(xy), t=x+y; R0-free ranks Y,Lambda,X=1,2,1',
            'basis_convention': 'Lambda basis (1,x), X generator x, Y generator y',
            'formal_maps': {'Y_to_Lambda': ['t', '-1'], 'Lambda_to_X': ['1', 't'],
                            'X_to_Lambda': ['0', '1'], 'Lambda_to_Y': ['1', '0']},
            'fiber': {'algebra': 'k[epsilon]/epsilon^2; x=epsilon,y=-epsilon',
                      'ending_X_inclusion': sparse(fiber['rows']['ending_X'][1]),
                      'ending_X_quotient': sparse(fiber['rows']['ending_X'][2]),
                      'rows': fiber['ranks']},
            'finite_jet_levels': list(models), 'exact_3_by_3_diagrams': diagrams,
            'scope': 'Actual finite jet actions/exactness/commutation. Infinite lattice classification and almost-split factorization are prose proofs, not inferred from bounded jet checks.'}


def checks():
    modules, morphisms, meshes = hls_checks()
    node = node_checks()
    return {'arithmetic': 'Exact Fraction arithmetic; deterministic; no random seed required.',
            'H3_quotient': 'Closed infinite dessin with permitted cycle l a1 a2 r back2 back1, quotient killing back1,back2.',
            'H3_modules': modules, 'signed_morphisms': morphisms,
            'mesh_sequences': meshes, 'node_AR_fiber': node,
            'counts': {'H3_modules': 9, 'dessin_relation_checks': 54,
                       'signed_morphisms': 12, 'arrow_commutations': 72,
                       'exact_mesh_sequences': 4, 'vertex_exactness_checks': 12,
                       'negative_sign_control': 1, 'node_jet_levels': 5,
                       'node_exact_rows': 10, 'node_3_by_3_jet_diagrams': 4,
                       'node_exact_columns': 12, 'node_commuting_squares': 32},
            'scope': 'Intrinsic H3 quotient AR meshes; actual finite matrix diagnostics. No automatic ambient AR transfer, universal exactness certificate, arithmetic Frobenius, or GRH claim.'}


def run(write_output=True):
    report = checks()
    if write_output:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=2)+'\n')
    return report


if __name__ == '__main__':
    result = run()
    print(json.dumps({'counts': result['counts'], 'output': str(OUT),
                      'scope': result['scope']}, indent=2))
