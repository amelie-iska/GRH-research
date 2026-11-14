"""Finite tokenization DAGs, exact integer teachers, and independent certificates.

The fixed-vocabulary weighted decoding problem is tractable by dynamic
programming. The separate vocabulary-selection example uses a relaxation;
neither task is a reproduction of a language-model campaign.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

MAX_LENGTH = 12
FEATURE_DIM = 8
COST_SCALE = 32.0
ALPHABET = "abcd"
VOCABULARY = tuple("".join(t) for k in (2, 3) for t in itertools.product(ALPHABET, repeat=k))


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def solve_dag(record):
    """Exact shortest distances and a deterministic minimizing path; integer costs."""
    length = len(record["text"])
    outgoing = [[] for _ in range(length + 1)]
    for j, edge in enumerate(record["edges"]):
        u, v = edge["source"], edge["target"]
        if not 0 <= u < v <= length or not isinstance(edge["cost"], int):
            raise ValueError("The teacher requires a forward DAG and integer costs")
        outgoing[u].append((j, v, edge["cost"]))
    distance = [None] * length + [0]
    chosen = [None] * length
    for u in range(length - 1, -1, -1):
        if not outgoing[u]:
            raise ValueError("Every nonterminal vertex must reach the terminal")
        cost, j = min((c + distance[v], j) for j, v, c in outgoing[u])
        distance[u], chosen[u] = cost, j
    path, u = [], 0
    while u != length:
        j = chosen[u]
        path.append(j)
        u = record["edges"][j]["target"]
    return distance, path


def enumerate_paths(record):
    """Independent recursive path enumeration, used only for bounded checks."""
    terminal = len(record["text"])
    def visit(vertex, path, total):
        if vertex == terminal:
            yield total, path
        else:
            for j, edge in enumerate(record["edges"]):
                if edge["source"] == vertex:
                    yield from visit(edge["target"], path + [j], total + edge["cost"])
    return list(visit(0, [], 0))


def path_certificate(record, path, potential):
    """Check a primal path and an exact integral dual potential independently."""
    terminal = len(record["text"])
    if len(potential) != terminal + 1 or any(type(v) is not int for v in potential):
        raise ValueError("Certificate potentials must be literal integers")
    u, total, text = 0, 0, ""
    valid = True
    for j in path:
        if not isinstance(j, int) or not 0 <= j < len(record["edges"]):
            valid = False
            break
        edge = record["edges"][j]
        if edge["source"] != u or edge["token"] != record["text"][u:edge["target"]]:
            valid = False
            break
        text += edge["token"]
        total += edge["cost"]
        u = edge["target"]
    valid = valid and u == terminal and text == record["text"]
    dual = potential[-1] == 0 and all(
        potential[e["source"]] - potential[e["target"]] <= e["cost"]
        for e in record["edges"])
    return {"path_valid": bool(valid), "dual_feasible": bool(dual),
            "path_cost_units": int(total), "lower_bound_units": int(potential[0]),
            "gap_units": int(total - potential[0]),
            "optimality_certified": bool(valid and dual and total == potential[0])}


def learned_proposal(record, predicted_distances):
    """Greedy learned path; exact potential feasibility and optional DP repair."""
    terminal = len(record["text"])
    pred = np.asarray(predicted_distances, dtype=float) * COST_SCALE
    if pred.shape != (terminal + 1,) or not np.isfinite(pred).all():
        raise ValueError("Expected finite per-vertex predictions")
    pred[-1] = 0
    path, u = [], 0
    while u != terminal:
        _, j = min((e["cost"] + pred[e["target"]], j)
                   for j, e in enumerate(record["edges"]) if e["source"] == u)
        path.append(int(j))
        u = record["edges"][j]["target"]
    potential = [int(v) for v in np.rint(pred)]
    potential[-1] = 0
    for u in range(terminal - 1, -1, -1):
        potential[u] = min(potential[u], min(e["cost"] + potential[e["target"]]
            for e in record["edges"] if e["source"] == u))
    initial = path_certificate(record, path, potential)
    exact_distances, exact_path = solve_dag(record)
    repaired = path_certificate(record, exact_path, exact_distances)
    if not repaired["optimality_certified"]:
        raise AssertionError("Independent exact certificate failed")
    return {"proposed_path": path, "proposal_certificate": initial,
            "proposal_regret_units": initial["path_cost_units"] - exact_distances[0],
            "repair_required": not initial["optimality_certified"],
            "certified_path": path if initial["optimality_certified"] else exact_path,
            "final_certificate": initial if initial["optimality_certified"] else repaired}


def make_record(text, rng, split):
    control = int(rng.integers(-2, 3))
    colors = sorted({text[i:j] for i in range(len(text))
                     for j in range(i + 2, min(len(text), i + 3) + 1)})
    costs = {word: (int(rng.integers(7, 30)), int(rng.integers(-2, 3)))
             for word in colors if rng.random() < .72}
    edges = []
    for i in range(len(text)):
        for j in range(i + 1, min(len(text), i + 3) + 1):
            word = text[i:j]
            if j == i + 1:
                base, slope = 16, 0
            elif word in costs:
                base, slope = costs[word]
            else:
                continue
            edges.append({"source": i, "target": j, "token": word,
                          "base_cost": base, "slope": slope, "cost": base + control * slope})
    record = {"text": text, "control": control, "edges": edges, "split": split}
    record["id"] = canonical_hash(record)
    distance, path = solve_dag(record)
    record["distance_units"], record["optimal_path"] = distance, path
    record["optimal_cost_units"] = distance[0]
    return record


def build_dataset(seed=20261113, sizes=(512, 128, 128, 128)):
    rng = np.random.default_rng(seed)
    seen, splits = set(), {}
    for split, count in zip(("train", "validation", "test", "ood"), sizes):
        rows = []
        while len(rows) < count:
            length = int(rng.integers(9, 13) if split == "ood" else rng.integers(4, 9))
            text = "".join(rng.choice(list(ALPHABET), size=length))
            if text in seen:
                continue
            seen.add(text)
            rows.append(make_record(text, rng, split))
        splits[split] = rows
    result = {"schema": "quantum-toricgt-dag-dataset-v1", "seed": seed,
              "cost_scale": COST_SCALE, "max_length": MAX_LENGTH,
              "split_rule": "Byte strings are disjoint across all splits; OOD lengths9–12, others4–8.",
              "task": "weighted fixed-vocabulary tokenization-DAG distances; exact integer teacher",
              "splits": splits}
    result["content_sha256"] = canonical_hash(result)
    return result


def tensor_record(record):
    """Tokens have intrinsic byte positions; incidence depends only on endpoints.

    Endpoint identifiers are used through their orthonormal Gram comparisons,
    rather than a learned table tied to arbitrary vertex storage labels.
    """
    n = len(record["text"])
    features, endpoints, info = [], [], []
    for i in range(n + 1):
        features.append([1, 0, i / MAX_LENGTH, i / MAX_LENGTH, 0, 0,
                         record["control"] / 2, 0])
        endpoints.append((i, i))
        info.append({"kind": "vertex", "position": i})
    for j, e in enumerate(record["edges"]):
        u, v = e["source"], e["target"]
        features.append([0, 1, u / MAX_LENGTH, v / MAX_LENGTH,
                         (v-u) / MAX_LENGTH, e["cost"] / COST_SCALE,
                         record["control"] / 2, e["slope"] / 2])
        endpoints.append((u, v))
        info.append({"kind": "edge", "edge_index": j, "source": u, "target": v})
    p = np.asarray(endpoints)
    incidence = sum((p[:, a, None] == p[None, :, b]).astype(float)
                    for a in (0, 1) for b in (0, 1)) / 4
    node_mask = np.arange(len(features)) <= n
    targets = np.zeros(len(features))
    targets[:n+1] = np.asarray(record["distance_units"]) / COST_SCALE
    return np.asarray(features), incidence, node_mask, targets, info


def batch_arrays(records):
    encoded = [tensor_record(r) for r in records]
    longest = max(len(x[0]) for x in encoded)
    count = len(records)
    x = np.zeros((count, longest, FEATURE_DIM), np.float32)
    incidence = np.zeros((count, longest, longest), np.float32)
    valid = np.zeros((count, longest), bool)
    nodes = np.zeros_like(valid)
    target = np.zeros((count, longest), np.float32)
    for b, (f, inc, nm, y, _) in enumerate(encoded):
        t = len(f)
        x[b,:t], incidence[b,:t,:t], valid[b,:t] = f, inc, True
        nodes[b,:t], target[b,:t] = nm, y
    return {"features": x, "incidence": incidence, "valid": valid,
            "nodes": nodes, "targets": target}


def vocabulary_lp_example():
    """Small colored-flow LP plus an exact rational weak-duality certificate."""
    from scipy.optimize import linprog
    corpus, budget = ["abca", "bcab", "cabc"], 2
    colors = sorted({w[i:j] for w in corpus for i in range(len(w))
                     for j in range(i+2, min(len(w), i+3)+1)})
    all_edges, row_offset = [], 0
    supplies = []
    for doc, word in enumerate(corpus):
        supplies.extend([1] + [0]*(len(word)-1) + [-1])
        for i in range(len(word)):
            for j in range(i+1, min(len(word), i+3)+1):
                all_edges.append((doc, i, j, word[i:j], row_offset))
        row_offset += len(word)+1
    ne, nc = len(all_edges), len(colors)
    eq = np.zeros((row_offset, ne+nc))
    ub, rhs = [], []
    for e, (_, i, j, word, offset) in enumerate(all_edges):
        eq[offset+i,e], eq[offset+j,e] = 1, -1
        if len(word)>1:
            row = np.zeros(ne+nc); row[e]=1; row[ne+colors.index(word)]=-1
            ub.append(row); rhs.append(0)
    row = np.zeros(ne+nc); row[ne:]=1; ub.append(row); rhs.append(budget)
    ub = np.asarray(ub); rhs = np.asarray(rhs)
    objective = np.r_[np.ones(ne), np.zeros(nc)]
    solved = linprog(objective, A_ub=ub, b_ub=rhs, A_eq=eq,
                     b_eq=supplies, bounds=(0,1), method="highs")
    if not solved.success:
        raise RuntimeError(solved.message)
    y = [Fraction(float(v)).limit_denominator(10000) for v in solved.eqlin.marginals]
    z = [min(Fraction(0), Fraction(float(v)).limit_denominator(10000))
         for v in solved.ineqlin.marginals]
    upper = []
    for j in range(ne+nc):
        a = sum(Fraction(int(eq[i,j]))*y[i] for i in range(len(y)))
        a += sum(Fraction(int(ub[i,j]))*z[i] for i in range(len(z)))
        upper.append(min(Fraction(0), Fraction(int(objective[j]))-a))
    lower = sum(Fraction(v)*y[i] for i,v in enumerate(supplies))
    lower += sum(Fraction(int(v))*z[i] for i,v in enumerate(rhs)) + sum(upper)
    best = None
    for chosen in itertools.combinations(colors, budget):
        total = 0
        for word in corpus:
            r = {"text": word, "edges": [{"source": i,"target":j,"token":word[i:j],"cost":1}
                 for i in range(len(word)) for j in range(i+1,min(len(word),i+3)+1)
                 if j==i+1 or word[i:j] in chosen]}
            total += solve_dag(r)[0][0]
        if best is None or (total,chosen)<best:
            best=(total,chosen)
    assert lower <= best[0]
    return {"corpus":corpus,"vocabulary_budget":budget,"candidate_colors":colors,
            "numerical_lp_objective":float(solved.fun),"exact_dual_lower_bound":str(lower),
            "exact_enumerated_integer_optimum":best[0],"optimal_vocabulary":list(best[1]),
            "gap_to_rational_bound":str(Fraction(best[0])-lower),
            "certificate":{"equality_multipliers":[str(v) for v in y],
                           "inequality_multipliers":[str(v) for v in z],
                           "upper_bound_multipliers":[str(v) for v in upper],
                           "Aeq":eq.astype(int).tolist(),"beq":supplies,
                           "Aub":ub.astype(int).tolist(),"bub":rhs.astype(int).tolist(),
                           "objective":objective.astype(int).tolist(),
                           "variable_bounds":[0,1]},
            "scope":"Small original colored-flow example; no full ConvexTok training campaign."}


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(build_dataset(),indent=2)+"\n")
    print(args.output)
