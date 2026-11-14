"""Bounded directed analogy witnesses and finite ground-rule deduction.

A graph witness checks declared vertices, directed paths, endpoint types and
licensed relation words, not equality of unknown physical laws. Optional integer
orders certify increasing paths, not physical causation. Retrieval is a proposal:
only explicit rules with available premises justify the reported deduction.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

MAX_NODES = 4096
MAX_EDGES = 16384
MAX_PATH = 4096
MAX_TOTAL_PATH = 65536
MAX_BANK = 65536
MAX_DIM = 1024
MAX_STEPS = 10000


def _label(value, name='label'):
    if type(value) is not str or not 0 < len(value) <= 4096:
        raise ValueError(f'{name} must be a nonempty bounded string')
    return value


def _groups(value):
    if type(value) is not frozenset or not 0 < len(value) <= MAX_NODES:
        raise ValueError('Explicit nonempty immutable leakage groups required')
    for x in value:
        _label(x, 'group')


def _key(value):
    if type(value) is not tuple or not 0 < len(value) <= MAX_DIM:
        raise ValueError('A nonempty bounded embedding tuple is required')
    for v in value:
        if type(v) not in (int, float):
            raise ValueError('Embedding values must be built-in finite numbers')
        try:
            finite = math.isfinite(v)
        except OverflowError as error:
            raise ValueError('Embedding scalar exceeds arithmetic range') from error
        if not finite:
            raise ValueError('Embedding values must be finite')


@dataclass(frozen=True)
class Memory:
    identity: str
    groups: frozenset[str]
    split: str
    encoder: str
    key: tuple[float, ...]


def retrieve(query: tuple[float, ...], groups: frozenset[str], encoder: str,
             bank: list[Memory], k: int = 4):
    """Exact L2 shortlist with strict provenance, identity and numeric checks.

    An empty eligible bank returns no proposals. It never fabricates a negative
    analogy or a proof. Encoder identifiers are caller-bound labels, not verified
    hashes of an actual learned model; physical semantics are not inferred.
    """
    if type(k) is not int or not 1 <= k <= 256:
        raise ValueError('Retrieval count must be an integer from 1 to 256')
    _key(query); _groups(groups); _label(encoder, 'encoder identity')
    if type(bank) is not list or len(bank) > MAX_BANK:
        raise ValueError('A bounded explicit memory list is required')
    out, identities = [], set()
    for item in bank:
        if type(item) is not Memory:
            raise ValueError('An explicit Memory record is required')
        _label(item.identity, 'memory identity'); _groups(item.groups)
        _label(item.encoder, 'encoder identity'); _key(item.key)
        if item.identity in identities:
            raise ValueError('Duplicate memory identity makes provenance ambiguous')
        identities.add(item.identity)
        if item.split != 'train':
            raise ValueError('Memory bank must contain training objects only')
        if item.encoder != encoder:
            raise ValueError('Stale encoder/codebook identity')
        if len(item.key) != len(query):
            raise ValueError('Embedding dimension mismatch')
        if groups & item.groups:
            continue
        distance = math.dist(query, item.key)
        score = distance * distance
        if not math.isfinite(score):
            raise ValueError('Squared distance exceeds arithmetic range')
        out.append((score, item.identity))
    return sorted(out)[:k]


def _graph(nodes, edges):
    if type(nodes) is not dict or len(nodes) > MAX_NODES:
        raise ValueError('A bounded declared vertex dictionary is required')
    if type(edges) is not dict or len(edges) > MAX_EDGES:
        raise ValueError('A bounded declared edge dictionary is required')
    for node, kind in nodes.items():
        _label(node, 'vertex'); _label(kind, 'vertex type')
    for edge, triple in edges.items():
        _label(edge, 'edge')
        if type(triple) not in (tuple, list) or len(triple) != 3:
            raise ValueError('Each edge must declare source, target and relation')
        u, v, relation = triple
        _label(u, 'edge source'); _label(v, 'edge target'); _label(relation, 'relation')
        if u not in nodes or v not in nodes:
            raise ValueError('Every edge endpoint must be a declared vertex')


def _order(nodes, edges, order):
    if type(order) is not dict or set(order) != set(nodes):
        raise ValueError('Order labels must cover exactly the declared vertices')
    if any(type(x) is not int or abs(x) > 10**9 for x in order.values()):
        raise ValueError('Order labels must be bounded exact integers')
    if any(order[u] >= order[v] for u, v, _ in edges.values()):
        raise ValueError('An ordered edge must strictly increase its declared rank')


def verify_mapping(source_nodes: dict, target_nodes: dict, source_edges: dict,
                   target_edges: dict, node_map: dict, paths: dict,
                   relation_words: dict, *, source_order: dict | None = None,
                   target_order: dict | None = None) -> bool:
    """Verify an injective boundary mapping and all declared path obligations.

    Interior vertices must exist in the target graph. Boundary types agree and
    the caller's licensed relation words are respected. A relation-specific type
    signature or a semantic commutation theorem is an additional obligation.
    Empty graphs are allowed; a vacuous syntax witness is not a physical result.
    """
    _graph(source_nodes, source_edges); _graph(target_nodes, target_edges)
    if type(node_map) is not dict or type(paths) is not dict:
        raise ValueError('Explicit mapping and path dictionaries required')
    if set(node_map) != set(source_nodes) or set(paths) != set(source_edges):
        raise ValueError('Incomplete node or branch coverage')
    for value in node_map.values():
        _label(value, 'mapped vertex')
    if len(set(node_map.values())) != len(node_map):
        raise ValueError('This contract requires injective boundary vertices')
    if any(v not in target_nodes or source_nodes[u] != target_nodes[v]
           for u, v in node_map.items()):
        raise ValueError('Node type mismatch')
    if type(relation_words) is not dict or len(relation_words) > MAX_EDGES:
        raise ValueError('A bounded relation dictionary is required')
    word_budget = 0
    for relation, alternatives in relation_words.items():
        _label(relation, 'source relation')
        if type(alternatives) not in (set, frozenset) or len(alternatives) > MAX_PATH:
            raise ValueError('Relation alternatives must be a bounded set of tuples')
        for word in alternatives:
            if type(word) is not tuple or not 0 < len(word) <= MAX_PATH:
                raise ValueError('A licensed relation word must be a nonempty tuple')
            word_budget += len(word)
            if word_budget > MAX_TOTAL_PATH:
                raise ValueError('Relation-word budget exceeded')
            for symbol in word:
                _label(symbol, 'target relation')
    if (source_order is None) != (target_order is None):
        raise ValueError('Both source and target order witnesses are required')
    if source_order is not None:
        _order(source_nodes, source_edges, source_order)
        _order(target_nodes, target_edges, target_order)
    total = 0
    for key, (u, v, relation) in source_edges.items():
        path = paths[key]
        if type(path) is not list or not 0 < len(path) <= MAX_PATH:
            raise ValueError('Explicit bounded nonempty target path required')
        total += len(path)
        if total > MAX_TOTAL_PATH:
            raise ValueError('Total mapped-path budget exceeded')
        for edge in path:
            _label(edge, 'path edge')
            if edge not in target_edges:
                raise ValueError('Unknown path edge')
        edges = [target_edges[edge] for edge in path]
        if (edges[0][0] != node_map[u] or edges[-1][1] != node_map[v]
                or any(a[1] != b[0] for a, b in zip(edges, edges[1:]))):
            raise ValueError('Direction or path boundary mismatch')
        if tuple(e[2] for e in edges) not in relation_words.get(relation, set()):
            raise ValueError('Unlicensed relation composition')
    return True


def verify_deduction(initial: frozenset[str], rules: dict,
                     steps: list[tuple[str, str]]) -> frozenset[str]:
    """Replay finite ground rules. The supplied rules and premises are assumptions."""
    if type(initial) is not frozenset or len(initial) > MAX_TOTAL_PATH:
        raise ValueError('Bounded immutable initial premises required')
    if type(rules) is not dict or len(rules) > MAX_STEPS:
        raise ValueError('Bounded named ground rules required')
    if type(steps) is not list or len(steps) > MAX_STEPS:
        raise ValueError('Derivation budget exceeded or invalid step list')
    for fact in initial:
        _label(fact, 'initial premise')
    total_premises = 0
    for name, rule in rules.items():
        _label(name, 'rule name')
        if type(rule) not in (tuple, list) or len(rule) != 2:
            raise ValueError('A ground rule is a premise set and one conclusion')
        premises, conclusion = rule
        if type(premises) not in (set, frozenset):
            raise ValueError('Rule premises must be an explicit set, not a string')
        total_premises += len(premises)
        if total_premises > MAX_TOTAL_PATH:
            raise ValueError('Ground-rule premise budget exceeded')
        for fact in premises:
            _label(fact, 'rule premise')
        _label(conclusion, 'rule conclusion')
    known = set(initial)
    for step in steps:
        if type(step) not in (tuple, list) or len(step) != 2:
            raise ValueError('Each step must name a rule and its conclusion')
        rule, claim = step
        _label(rule, 'step rule'); _label(claim, 'step claim')
        if rule not in rules:
            raise ValueError('Unknown rule')
        premises, conclusion = rules[rule]
        if claim != conclusion or not premises <= known:
            raise ValueError('Unproved premise or wrong conclusion')
        known.add(claim)
    return frozenset(known)
