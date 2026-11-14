"""Exact oriented surface cellulations, clean dessins, and CSS preparation.

Qubit q is bit q (little endian) in a state-vector basis index.  Incidence
matrices are represented by sparse supports; integer bitsets are used only
for small/medium exact GF(2) calculations.  No quantum hardware is required.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from copy import deepcopy
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Iterable


def support_mask(support: Iterable[int]) -> int:
    mask = 0
    for q in support:
        mask ^= 1 << q
    return mask


def mask_support(mask: int) -> list[int]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return result


def gf2_rref(rows: Iterable[int], n: int) -> tuple[list[int], list[int]]:
    """Reduced row echelon basis, with ascending (little-endian) pivots."""
    work = [int(row) for row in rows if row]
    pivot_row = 0
    pivots = []
    for col in range(n):
        selected = next((i for i in range(pivot_row, len(work))
                         if (work[i] >> col) & 1), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        pivot = work[pivot_row]
        for i in range(len(work)):
            if i != pivot_row and ((work[i] >> col) & 1):
                work[i] ^= pivot
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work[:pivot_row], pivots


def in_rowspace(mask: int, basis: list[int], pivots: list[int]) -> bool:
    for row, pivot in zip(basis, pivots):
        if (mask >> pivot) & 1:
            mask ^= row
    return mask == 0


def gate(name: str, target: int, control: int | None = None,
         angle: float | None = None) -> dict:
    entry = {"gate": name, "target": int(target),
             "qubits": [int(target)] if control is None else [int(control), int(target)]}
    if control is not None:
        entry["control"] = int(control)
    if angle is not None:
        entry["angle"] = float(angle)
    return entry


def css_prepare(x_supports: list[list[int]], n: int) -> dict:
    """Prepare 2^(-rankX/2) sum_{x in row(H_X)} |x> from |0...0>."""
    rows, pivots = gf2_rref((support_mask(s) for s in x_supports), n)
    pivot_set = set(pivots)
    circuit = [gate("H", pivot) for pivot in pivots]
    for row, pivot in zip(rows, pivots):
        for target in mask_support(row):
            if target == pivot:
                continue
            if target in pivot_set:
                raise AssertionError("RREF has a nonzero off-diagonal pivot")
            circuit.append(gate("CX", target, control=pivot))
    return {"circuit": circuit, "pivots": pivots,
            "rref_generators": [mask_support(row) for row in rows],
            "state_definition": "uniform_positive_superposition_over_rowspace_HX",
            "logical_state": "all_Z_logical_eigenvalues_plus_one",
            "locality": "algebraic_encoder; CNOTs need not be geometrically adjacent"}


def torus_checks(lx: int, ly: int) -> tuple[list[list[int]], list[list[int]]]:
    """Sparse stars and faces; O(lx*ly) storage, no dense matrices.

    h(x,y)=y*lx+x; v(x,y)=lx*ly+y*lx+x, with periodic coordinates.
    lx,ly >= 3 ensures four distinct edges and neighbors at each star.
    """
    if lx < 3 or ly < 3:
        raise ValueError("This square-cellulation API requires lx,ly >= 3")
    nv = lx * ly
    h = lambda x, y: (y % ly) * lx + (x % lx)
    v = lambda x, y: nv + (y % ly) * lx + (x % lx)
    stars = [[h(x, y), v(x, y), h(x - 1, y), v(x, y - 1)]
             for y in range(ly) for x in range(lx)]
    faces = [[h(x, y), v(x + 1, y), h(x, y + 1), v(x, y)]
             for y in range(ly) for x in range(lx)]
    return stars, faces


def permutation_cycles(permutation: list[int]) -> list[list[int]]:
    if sorted(permutation) != list(range(len(permutation))):
        raise AssertionError("Not a permutation")
    seen = bytearray(len(permutation))
    cycles = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        cycle, current = [], start
        while not seen[current]:
            seen[current] = 1
            cycle.append(current)
            current = permutation[current]
        if current != start:
            raise AssertionError("Permutation cycle failed to close")
        cycles.append(cycle)
    return cycles


def _torus_point(x: float, y: float, lx: int, ly: int) -> list[float]:
    a, b = 2 * math.pi * x / lx, 2 * math.pi * y / ly
    radius = 2.0 + 0.7 * math.cos(b)
    return [radius * math.cos(a), radius * math.sin(a), 0.7 * math.sin(b)]


def square_torus(lx: int, ly: int, *, include_encoder: bool = True,
                 include_permutations: bool = True, exact_rank: bool = True) -> dict:
    torus_checks(lx, ly)  # Validate dimensions before allocating geometry.
    nv = lx * ly
    vertex = lambda x, y: (y % ly) * lx + (x % lx)
    h = lambda x, y: vertex(x, y)
    v = lambda x, y: nv + vertex(x, y)
    vertices = [{"id": vertex(x, y), "x": x, "y": y,
                 "position3d": _torus_point(x, y, lx, ly), "patch": 0,
                 "label": f"v({x},{y})"} for y in range(ly) for x in range(lx)]
    edges = []
    for orientation in ("h", "v"):
        for y in range(ly):
            for x in range(lx):
                horizontal = orientation == "h"
                q = h(x, y) if horizontal else v(x, y)
                cx, cy = x + (0.5 if horizontal else 0), y + (0 if horizontal else 0.5)
                edges.append({"id": q, "u": vertex(x, y),
                              "v": vertex(x + int(horizontal), y + int(not horizontal)),
                              "orientation": orientation, "x": cx, "y": cy,
                              "center": [cx, cy], "position3d": _torus_point(cx, cy, lx, ly),
                              "patch": 0, "label": f"{orientation}({x},{y})"})
    faces = []
    for y in range(ly):
        for x in range(lx):
            boundary = [[h(x, y), 1], [v(x + 1, y), 1],
                        [h(x, y + 1), -1], [v(x, y), -1]]
            faces.append({"id": vertex(x, y), "oriented_edges": boundary,
                          "x": x + .5, "y": y + .5, "center": [x + .5, y + .5],
                          "patch": 0, "label": f"f({x},{y})"})
    model = {"id": f"torus{lx}x{ly}", "label": f"{lx} × {ly} torus",
             "kind": "square_torus", "dimensions": [lx, ly], "vertices": vertices,
             "edges": edges, "faces": faces,
             "geometry": {"type": "parametric_torus", "embedding": "explicit smooth torus",
                          "uniformization": "not asserted", "periodic": True}}
    return finalize(model, include_encoder=include_encoder,
                    include_permutations=include_permutations, exact_rank=exact_rank)


def _face_vertices(model: dict, face: dict) -> list[int]:
    vertices = []
    previous_head = None
    for edge_id, sign in face["oriented_edges"]:
        edge = model["edges"][edge_id]
        tail, head = (edge["u"], edge["v"]) if sign == 1 else (edge["v"], edge["u"])
        if previous_head is not None and tail != previous_head:
            raise AssertionError("Oriented face boundary is not a path")
        vertices.append(tail)
        previous_head = head
    if previous_head != vertices[0]:
        raise AssertionError("Oriented face boundary is not closed")
    return vertices


def connected_sum(left: dict, right: dict, face_left: int = 0,
                  face_right: int = 0, *, case_id: str | None = None,
                  include_encoder: bool = True) -> dict:
    """Delete embedded disk faces and identify boundaries orientation-reversingly.

    Edges are identified explicitly, not by their endpoints, so distinct
    parallel edges cannot accidentally disappear.
    """
    a, b = deepcopy(left), deepcopy(right)
    fa, fb = a["faces"][face_left], b["faces"][face_right]
    va, vb = _face_vertices(a, fa), _face_vertices(b, fb)
    m = len(va)
    if len(vb) != m or len(set(va)) != m or len(set(vb)) != m:
        raise ValueError("Connected sum needs simple embedded disk faces of equal length")
    na = len(a["vertices"])
    parent = list(range(na + len(b["vertices"])))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        parent[find(y)] = find(x)
    for i in range(m):
        union(va[i], na + vb[(-i) % m])
    root_ids = {}
    vertex_map = []
    for old in range(len(parent)):
        root = find(old)
        root_ids.setdefault(root, len(root_ids))
        vertex_map.append(root_ids[root])
    vertices = []
    all_vertices = a["vertices"] + b["vertices"]
    for new_id in range(len(root_ids)):
        members = [i for i, mapped in enumerate(vertex_map) if mapped == new_id]
        chart = []
        for old in members:
            source = all_vertices[old]
            chart.append({"source": "left" if old < na else "right",
                          "source_vertex": source["id"], "x": source["x"], "y": source["y"]})
        first = all_vertices[members[0]]
        vertices.append({"id": new_id, "x": first["x"], "y": first["y"],
                         "charts": chart, "label": f"v{new_id}",
                         "position3d": None})
    edges = []
    for old in a["edges"]:
        edge = deepcopy(old)
        edge.update(u=vertex_map[old["u"]], v=vertex_map[old["v"]], position3d=None)
        edges.append(edge)
    right_edge_map = {}
    seam = []
    for i, (edge_a, sign_a) in enumerate(fa["oriented_edges"]):
        j = (-i - 1) % m
        edge_b, sign_b = fb["oriented_edges"][j]
        factor = -sign_a * sign_b
        right_edge_map[edge_b] = (edge_a, factor)
        edges[edge_a]["orientation"] = "seam"
        seam.append({"left_edge": edge_a, "right_edge": edge_b,
                     "new_edge": edge_a, "orientation_factor": factor})
    for old in b["edges"]:
        if old["id"] in right_edge_map:
            continue
        edge = deepcopy(old)
        new_id = len(edges)
        edge.update(id=new_id, u=vertex_map[na + old["u"]],
                    v=vertex_map[na + old["v"]], position3d=None)
        right_edge_map[old["id"]] = (new_id, 1)
        edges.append(edge)
    faces = []
    for side, model, deleted in (("left", a, face_left), ("right", b, face_right)):
        for old in model["faces"]:
            if old["id"] == deleted:
                continue
            face = deepcopy(old)
            if side == "right":
                face["oriented_edges"] = [[right_edge_map[e][0], s * right_edge_map[e][1]]
                                           for e, s in old["oriented_edges"]]
            face.update(id=len(faces), source_side=side, source_face=old["id"])
            faces.append(face)
    model = {"id": case_id or "connected_sum", "label": "Connected sum of square tori",
             "kind": "oriented_connected_sum", "vertices": vertices, "edges": edges,
             "faces": faces, "geometry": {"type": "glued_cellulation_charts",
                 "embedding": "combinatorial charts; no smooth embedding claimed",
                 "uniformization": "not computed", "seam": seam,
                 "deleted_faces": [face_left, face_right],
                 "boundary_gluing": "vertex i on left to vertex -i on right"}}
    return finalize(model, include_encoder=include_encoder)


def finalize(model: dict, *, include_encoder: bool = True,
             include_permutations: bool = True, exact_rank: bool = True) -> dict:
    vertices, edges, faces = model["vertices"], model["edges"], model["faces"]
    nv, ne, nf = len(vertices), len(edges), len(faces)
    if [e["id"] for e in edges] != list(range(ne)):
        raise AssertionError("Edge ids must be contiguous qubit indices")
    stars = [[] for _ in vertices]
    adjacency = [[] for _ in vertices]
    for edge in edges:
        u, v, q = edge["u"], edge["v"], edge["id"]
        stars[u].append(q)
        stars[v].append(q)
        adjacency[u].append(v)
        adjacency[v].append(u)
    stars = [mask_support(support_mask(s)) for s in stars]
    face_supports = []
    edge_occurrences = [[] for _ in edges]
    phi = [-1] * (2 * ne)
    for face in faces:
        face["vertices"] = _face_vertices(model, face)
        boundary = face["oriented_edges"]
        darts = [2 * e + int(sign < 0) for e, sign in boundary]
        for i, dart in enumerate(darts):
            if phi[dart] != -1:
                raise AssertionError("An oriented edge belongs to more than one face")
            phi[dart] = darts[(i + 1) % len(darts)]
        for edge, sign in boundary:
            edge_occurrences[edge].append(sign)
        support = mask_support(support_mask(e for e, _ in boundary))
        face["edges"] = support
        face["qubits"] = support
        face["darts"] = darts
        face_supports.append(support)
    if any(len(signs) != 2 or sum(signs) != 0 for signs in edge_occurrences):
        raise AssertionError("Closed oriented cellulation requires two opposite incidences per edge")
    sigma1 = [dart ^ 1 for dart in range(2 * ne)]
    sigma0 = [phi[sigma1[dart]] for dart in range(2 * ne)]
    black_cycles = permutation_cycles(sigma0)
    face_cycles = permutation_cycles(phi)
    if len(black_cycles) != nv or len(face_cycles) != nf:
        raise AssertionError("Vertex links or face cycles disagree with the cellulation")
    for cycle in black_cycles:
        tails = {edges[d // 2]["v" if d % 2 else "u"] for d in cycle}
        if len(tails) != 1:
            raise AssertionError("Rotation cycle mixes distinct vertices")
    visited, queue = {0}, deque([0])
    while queue:
        for nxt in adjacency[queue.popleft()]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    if len(visited) != nv:
        raise AssertionError("The cellulation is disconnected")
    # Every face boundary has zero incidence; this checks HX HZ^T sparsely.
    for support in face_supports:
        incidence = Counter()
        for q in support:
            incidence[edges[q]["u"]] += 1
            incidence[edges[q]["v"]] += 1
        if any(count % 2 for count in incidence.values()):
            raise AssertionError("HX HZ^T is nonzero")
    chi = nv - ne + nf
    if (2 - chi) % 2 or chi > 2:
        raise AssertionError("Invalid Euler characteristic for a connected oriented surface")
    genus = (2 - chi) // 2
    if exact_rank:
        x_basis, _ = gf2_rref((support_mask(s) for s in stars), ne)
        z_basis, _ = gf2_rref((support_mask(s) for s in face_supports), ne)
        rank_x, rank_z = len(x_basis), len(z_basis)
        if (rank_x, rank_z) != (nv - 1, nf - 1):
            raise AssertionError("Computed ranks disagree with connected closed-surface homology")
        rank_method = "exact_GF2_integer_bitset_RREF"
    else:
        rank_x, rank_z = nv - 1, nf - 1
        rank_method = "proved_connected_closed_oriented_surface_rank_formula"
    model.update(n=ne, genus=genus,
                 x_checks=[{"id": f"A{v}", "vertex": v, "qubits": s}
                           for v, s in enumerate(stars)],
                 z_checks=[{"id": f"B{f}", "face": f, "qubits": s}
                           for f, s in enumerate(face_supports)])
    model["metadata"] = {"V": nv, "E": ne, "F": nf, "n": ne, "chi": chi,
                         "rankX": rank_x, "rankZ": rank_z, "k": ne - rank_x - rank_z,
                         "rank_method": rank_method, "commutes": True,
                         "closed": True, "oriented": True, "connected": True,
                         "vertex_links_are_single_cycles": True,
                         "bit_order": "little_endian_qubit_q_is_bit_q",
                         "dessin_degree": 2 * ne,
                         "dessin_black_vertices": nv, "dessin_white_vertices": ne,
                         "dessin_faces": nf,
                         "max_star_weight": max(map(len, stars)),
                         "max_face_weight": max(map(len, face_supports))}
    if model["metadata"]["k"] != 2 * genus:
        raise AssertionError("CSS logical dimension does not equal 2g")
    if include_permutations:
        sigma_inf = [0] * len(phi)
        for i, j in enumerate(phi):
            sigma_inf[j] = i
        model["permutations"] = {"sigma0": sigma0, "sigma1": sigma1,
                                  "sigma_infinity": sigma_inf, "face_permutation": phi,
                                  "black_cycles": black_cycles,
                                  "white_cycles": [[2 * q, 2 * q + 1] for q in range(ne)],
                                  "face_cycles": face_cycles,
                                  "composition": "right_to_left; sigma0*sigma1=face_permutation",
                                  "meaning": "connected clean dessin; Belyi map coefficients not computed"}
    if include_encoder:
        preparation = css_prepare(stars, ne)
        model["prepare_circuit"] = preparation.pop("circuit")
        model["preparation"] = preparation
        model["metadata"]["preparation_gate_count"] = len(model["prepare_circuit"])
    else:
        model["prepare_circuit"] = []
        model["preparation"] = {"omitted": True, "reason": "sparse topology-only request"}
    return model


def distance_small(model: dict, max_weight: int = 4) -> dict:
    """Exact exhaustive distance if both logical types found by max_weight.

    This function is intentionally for small codes.  It never reports a
    missing witness as an established distance.
    """
    n = model["n"]
    hx = [support_mask(c["qubits"]) for c in model["x_checks"]]
    hz = [support_mask(c["qubits"]) for c in model["z_checks"]]
    bx, px = gf2_rref(hx, n)
    bz, pz = gf2_rref(hz, n)
    found = {}
    tested = 0
    for weight in range(1, max_weight + 1):
        for subset in combinations(range(n), weight):
            mask = support_mask(subset)
            tested += 1
            if "Z" not in found and all((mask & row).bit_count() % 2 == 0 for row in hx):
                if not in_rowspace(mask, bz, pz):
                    found["Z"] = {"weight": weight, "qubits": list(subset)}
            if "X" not in found and all((mask & row).bit_count() % 2 == 0 for row in hz):
                if not in_rowspace(mask, bx, px):
                    found["X"] = {"weight": weight, "qubits": list(subset)}
        if len(found) == 2:
            return {"exact": True, "distance": min(w["weight"] for w in found.values()),
                    "logical_witnesses": found, "subsets_tested": tested,
                    "method": "exhaustive_increasing_weight_CSS_centralizer_mod_stabilizer"}
    return {"exact": False, "searched_through_weight": max_weight,
            "logical_witnesses": found, "subsets_tested": tested}


def simulate_numpy(model: dict, extra_gates: list[dict] | None = None):
    """Actual dense CPU state vector; restricted to at most 20 qubits."""
    import numpy as np
    n = model["n"]
    if n > 20:
        raise ValueError("CPU validation is restricted to <=20 qubits")
    state = np.zeros(1 << n, dtype=np.complex128)
    state[0] = 1
    indices = np.arange(1 << n, dtype=np.uint64)
    for instruction in model["prepare_circuit"] + (extra_gates or []):
        name, q = instruction["gate"], instruction["target"]
        bit = 1 << q
        if name == "CX":
            control = instruction["control"]
            permutation = indices ^ ((((indices >> control) & 1) * bit))
            state = state[permutation]
        elif name == "X":
            state = state[indices ^ bit]
        elif name == "Z":
            state = state * (1 - 2 * ((indices >> q) & 1).astype(np.int8))
        elif name in ("H", "RY", "RZ"):
            zero = indices[(indices & bit) == 0]
            one = zero | bit
            a, b = state[zero].copy(), state[one].copy()
            if name == "H":
                state[zero], state[one] = (a + b) / math.sqrt(2), (a - b) / math.sqrt(2)
            elif name == "RY":
                theta = instruction["angle"] / 2
                c, s = math.cos(theta), math.sin(theta)
                state[zero], state[one] = c * a - s * b, s * a + c * b
            else:
                theta = instruction["angle"] / 2
                state[zero], state[one] = a * np.exp(-1j * theta), b * np.exp(1j * theta)
        else:
            raise ValueError(f"Unsupported gate {name}")
    return state


def numpy_validation(model: dict) -> dict:
    import numpy as np
    state = simulate_numpy(model)
    n = model["n"]
    rows = [support_mask(s) for s in model["preparation"]["rref_generators"]]
    support = [0]
    for row in rows:
        support += [x ^ row for x in support]
    expected = np.zeros_like(state)
    expected[support] = 2 ** (-len(rows) / 2)
    amplitude_error = float(np.max(np.abs(state - expected)))
    indices = np.arange(1 << n, dtype=np.uint64)
    values = {}
    for kind, checks in (("X", model["x_checks"]), ("Z", model["z_checks"])):
        for check in checks:
            mask = support_mask(check["qubits"])
            if kind == "X":
                value = np.vdot(state, state[indices ^ mask]).real
            else:
                parity = np.zeros(len(state), dtype=np.int8)
                for q in check["qubits"]:
                    parity ^= ((indices >> q) & 1).astype(np.int8)
                value = np.sum(abs(state) ** 2 * (1 - 2 * parity))
            values[check["id"]] = float(value)
    theta = [.65, -.4, .5, -.6]
    patch = model["x_checks"][0]["qubits"]
    if len(patch) != 4:
        raise AssertionError("QNN demonstration requires a four-edge star")
    qnn_errors = []
    qnn_rows = []
    for bits in range(16):
        signs = [1 if ((bits >> i) & 1) == 0 else -1 for i in range(4)]
        circuit = [gate("RY", q, angle=s * math.pi / 2 + t)
                   for q, s, t in zip(patch, signs, theta)]
        circuit += [gate("CX", patch[0], control=q) for q in patch[1:]]
        qnn_state = simulate_numpy(model, circuit)
        z = 1 - 2 * ((indices >> patch[0]) & 1).astype(np.int8)
        measured = float(np.sum(abs(qnn_state) ** 2 * z))
        analytic = math.prod(signs) * math.prod(map(math.cos, theta))
        qnn_errors.append(abs(measured - analytic))
        qnn_rows.append({"signs": signs, "actual_expectation": measured,
                         "analytic_expectation": analytic})
    if amplitude_error > 1e-12 or max(abs(v - 1) for v in values.values()) > 1e-12:
        raise AssertionError("CSS state-vector validation failed")
    if max(qnn_errors) > 1e-12:
        raise AssertionError("QNN state-vector identity failed")
    return {"backend": "NumPy CPU complex128 full state vector",
            "n": n, "dimension": len(state), "norm_squared": float(np.vdot(state, state).real),
            "nonzero_amplitudes": len(support), "max_amplitude_error": amplitude_error,
            "stabilizer_expectations": values,
            "qnn": {"patch": patch, "theta": theta, "cases": qnn_rows,
                     "max_identity_error": max(qnn_errors)},
            "hardware_execution": False}


def write_cases(output_dir: Path, site_dir: Path | None = None, *, validate_cpu: bool = True) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    if site_dir:
        site_dir.mkdir(parents=True, exist_ok=True)
    t18 = square_torus(3, 3)
    t30 = square_torus(3, 5)
    g2 = connected_sum(t18, t18, case_id="genus2_3x3")
    g2["label"] = "Genus 2 · connected sum · 32 qubits"
    # After the first gluing, face 3 is the retained original left face 4.
    # Its four boundary vertices remain distinct; finalize checks every link.
    g3 = connected_sum(g2, t18, face_left=3, case_id="genus3_3x3")
    g3["label"] = "Genus 3 · connected sum · 46 qubits"
    large = square_torus(32, 32, include_encoder=False, exact_rank=True)
    for model in (t18, t30, g2, g3):
        model["distance_certificate"] = distance_small(model, max_weight=3)
    cases = [t18, t30, g2, g3, large]
    listing = {"schema_version": 1, "cases": []}
    for model in cases:
        path = output_dir / (model["id"] + ".json")
        path.write_text(json.dumps(model, separators=(",", ":")) + "\n")
        live = model["id"] == "torus3x3"
        listing["cases"].append({"id": model["id"], "label": model["label"],
                                  "path": "data/" + path.name, "browserLive": live,
                                  "n": model["n"], "genus": model["genus"],
                                  "k": model["metadata"]["k"]})
        if site_dir:
            (site_dir / path.name).write_bytes(path.read_bytes())
    (output_dir / "surface-cases.json").write_text(json.dumps(listing, indent=2) + "\n")
    if site_dir:
        (site_dir / "surface-cases.json").write_text(json.dumps(listing, indent=2) + "\n")
    if validate_cpu:
        report = numpy_validation(t18)
        (output_dir / "cpu-validation.json").write_text(json.dumps(report, indent=2) + "\n")
        if site_dir:
            (site_dir / "cpu-validation.json").write_text(json.dumps(report, indent=2) + "\n")
    return listing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "cases")
    parser.add_argument("--site-data", type=Path)
    parser.add_argument("--skip-cpu", action="store_true")
    args = parser.parse_args()
    listing = write_cases(args.output, args.site_data, validate_cpu=not args.skip_cpu)
    print(json.dumps(listing, indent=2))


if __name__ == "__main__":
    main()
