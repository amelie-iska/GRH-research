#!/usr/bin/env python3
"""Exact index/causal/typed-map diagrams for the second-pass chapters.

Every edge is specified by its mathematical endpoints. No generative imagery,
external asset, or layout service is used. Matplotlib writes vector PDF/SVG and
a raster preview. The small numerical Fierz checks validate the plotted index
convention for N=2,...,5; the manuscript proves the general identity.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "extension/manuscript/figures"
INK = "#192f42"
BLUE = "#15657b"
RUST = "#a84732"
MUTED = "#52616f"
PALE = "#eff4f6"
GREY = "#bbc4ca"
FIXED_DATE = datetime(2026, 11, 13, tzinfo=timezone.utc)
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "font.size": 10,
    "text.color": INK,
    "axes.edgecolor": INK,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "svg.hashsalt": "orders-second-pass-figures-v1",
    "savefig.facecolor": "white",
})


def arrow(ax, a, b, color=INK, lw=1.65, zorder=2, **kwargs):
    patch = FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=10,
                            linewidth=lw, color=color,
                            shrinkA=0, shrinkB=0, zorder=zorder, **kwargs)
    ax.add_patch(patch)
    return patch


def plain(ax, a, b, color=INK, lw=1.65, **kwargs):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, **kwargs)


def save(fig, stem, title):
    files = []
    for ext in ("pdf", "svg", "png"):
        path = OUT / (stem + "." + ext)
        metadata = {"Title": title, "Creator": "make_second_pass_figures.py"}
        if ext == "pdf":
            metadata.update(CreationDate=FIXED_DATE, ModDate=FIXED_DATE)
        elif ext == "svg":
            metadata["Date"] = FIXED_DATE.isoformat()
        fig.savefig(path, dpi=240, bbox_inches="tight", pad_inches=0.08,
                    metadata=metadata)
        files.append({"file": str(path.relative_to(ROOT)),
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "bytes": path.stat().st_size})
    plt.close(fig)
    return files


def boundary(ax, center, half=0.7, bottom=0.75, top=2.65):
    points = {"i": (center - half, top), "j": (center - half, bottom),
              "k": (center + half, top), "l": (center + half, bottom)}
    for name, (x, y) in points.items():
        offset = 0.22 if name in ("i", "k") else -0.22
        ax.text(x, y + offset, "$" + name + "$", ha="center", va="center", fontsize=12)
        ax.plot(x, y, "o", color=INK, ms=2.6)
    return points


def make_fierz():
    fig, ax = plt.subplots(figsize=(7.3, 3.25))
    ax.set(xlim=(0, 11), ylim=(-0.55, 3.8))
    ax.set_axis_off()
    ax.text(5.5, 3.7, "Fundamental color completeness", ha="center", fontsize=13, weight="bold")
    ax.text(5.5, 3.32, r"$N\geq 2,\qquad \mathrm{Tr}(T^aT^b)=\delta^{ab}/2$", ha="center", fontsize=10)
    left = boundary(ax, 1.5)
    mid = boundary(ax, 5.4)
    right = boundary(ax, 9.45)
    y_vertex = 1.7
    for x, low, high in [(0.8, "j", "i"), (2.2, "l", "k")]:
        arrow(ax, left[low], (x, y_vertex - 0.2), color=BLUE)
        arrow(ax, (x, y_vertex + 0.2), left[high], color=BLUE)
        ax.add_patch(Circle((x, y_vertex), 0.22, facecolor=PALE, edgecolor=INK, lw=1.3, zorder=4))
        ax.text(x, y_vertex, r"$T^a$", fontsize=10, ha="center", va="center", zorder=5)
    # The adjoint edge alone contracts its a index. Fundamental i,j,k,l stay free.
    plain(ax, (1.02, y_vertex), (1.98, y_vertex), color=RUST, lw=1.8,
          linestyle=(0, (2.0, 1.5)))
    ax.text(1.5, 2.03, r"$\sum_a$", ha="center", fontsize=11, color=RUST)
    ax.text(3.22, 1.7, "=", fontsize=22, ha="center", va="center")
    ax.text(4.03, 1.7, r"$\frac{1}{2}$", fontsize=17, ha="center", va="center")
    # Exchange contraction delta^i_l delta^k_j: bottom l->top i, j->k.
    arrow(ax, mid["l"], mid["i"], color=RUST)
    # A white under-stroke gives a clear overpass: crossing is not a vertex.
    plain(ax, mid["j"], mid["k"], color="white", lw=5.5, zorder=3)
    arrow(ax, mid["j"], mid["k"], color=BLUE, zorder=4)
    ax.text(7.53, 1.7, r"$-\frac{1}{2N}$", fontsize=17, ha="center", va="center")
    arrow(ax, right["j"], right["i"], color=BLUE)
    arrow(ax, right["l"], right["k"], color=RUST)
    ax.text(1.5, 0.15, r"$\sum_a(T^a)^i{}_j(T^a)^k{}_l$", fontsize=10, ha="center")
    ax.text(5.4, 0.15, r"$\delta^i{}_l\,\delta^k{}_j$", fontsize=11, ha="center")
    ax.text(9.45, 0.15, r"$\delta^i{}_j\,\delta^k{}_l$", fontsize=11, ha="center")
    ax.text(5.5, -0.36, "Arrows run from input to output. Only a is summed; a crossing is not a vertex.",
            fontsize=8.2, ha="center", color=MUTED)
    return save(fig, "second-pass-fierz", "Fierz identity with typed fundamental and adjoint index contractions")


def node(ax, xy, label, intervention=False, exogenous=False):
    radius = 0.29
    face = "#fff3e7" if intervention else PALE if exogenous else "white"
    edge = RUST if intervention else INK
    ax.add_patch(Circle(xy, radius, facecolor=face, edgecolor=edge, lw=1.5, zorder=4))
    ax.text(*xy, label, ha="center", va="center", fontsize=11, zorder=5, color=edge)


def shortened(a, b, radius=0.30):
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    delta = (b - a) / np.linalg.norm(b - a)
    return a + radius * delta, b - radius * delta


def causal_panel(ax, model, intervene):
    ax.set(xlim=(0, 4), ylim=(-0.2, 3.65), aspect="equal")
    ax.set_axis_off()
    U, X, Y = (2, 2.45), (0.9, 1.05), (3.1, 1.05)
    a, b = shortened(U, X)
    if intervene:
        plain(ax, a, b, color=GREY, lw=1.3, linestyle=(0, (3, 2)))
        middle = (a + b) / 2
        plain(ax, middle + (-0.12, -0.12), middle + (0.12, 0.12), color=RUST, lw=2.1, zorder=3)
        plain(ax, middle + (-0.12, 0.12), middle + (0.12, -0.12), color=RUST, lw=2.1, zorder=3)
    else:
        arrow(ax, a, b, color=BLUE)
    tail = X if model == "A" else U
    arrow(ax, *shortened(tail, Y), color=BLUE)
    node(ax, U, "$U$", exogenous=True)
    node(ax, X, "$0$" if intervene else "$X$", intervention=intervene)
    node(ax, Y, "$Y$")
    if intervene:
        ax.text(0.9, 0.55, "$X:=0$", ha="center", fontsize=9, color=RUST)
        law = "0" if model == "A" else r"\frac{1}{2}"
        ax.text(2, -0.03, r"$\Pr(Y=1\mid\mathrm{do}(X=0))=" + law + "$", ha="center", fontsize=10.5)
        ax.text(2, 3.3, "Intervention: remove the input to X", ha="center", fontsize=9.2, color=MUTED)
    else:
        equation = r"$X=U,\quad Y=X$" if model == "A" else r"$X=U,\quad Y=U$"
        ax.text(2, 3.35, "MODEL " + model, ha="center", fontsize=10, weight="bold")
        ax.text(2, 2.99, equation, ha="center", fontsize=10.5)
        ax.text(2, 0.18, r"$\Pr((X,Y)=(0,0))=\Pr((X,Y)=(1,1))=\frac{1}{2}$", ha="center", fontsize=8.6)


def make_causal():
    fig = plt.figure(figsize=(7.3, 5.4))
    fig.text(0.5, 0.97, "Same observations, different interventions", ha="center", fontsize=13, weight="bold")
    fig.text(0.5, 0.925, r"$U\sim\mathrm{Bernoulli}(1/2)$ in both models", ha="center", fontsize=10)
    specs = [(0.03, 0.49, "A", False), (0.51, 0.49, "B", False),
             (0.03, 0.055, "A", True), (0.51, 0.055, "B", True)]
    for x, y, model, intervene in specs:
        causal_panel(fig.add_axes((x, y, 0.46, 0.43)), model, intervene)
    fig.text(0.5, 0.025, "Dashed crossed edge: removed structural dependence. The law of U is unchanged.",
             ha="center", fontsize=8.2, color=MUTED)
    return save(fig, "second-pass-causal-models", "Two observationally identical causal models and their distinct intervention laws")


def context_row(ax, y, label, color):
    # Boundary objects and the one-hole replacement have exactly matching types.
    xs = [0.5, 3.35, 6.25, 9.1]
    for x, obj in zip(xs, "ABCD"):
        ax.text(x, y, "$" + obj + "$", ha="center", va="center", fontsize=13)
    for i, name in enumerate(["p", label, "q"]):
        a = (xs[i] + 0.25, y)
        b = (xs[i+1] - 0.25, y)
        arrow(ax, a, b, color=color if i == 1 else INK)
        ax.text((a[0]+b[0])/2, y+0.2, "$" + name + "$", ha="center", va="bottom", fontsize=12,
                color=color if i == 1 else INK)
    ax.add_patch(FancyBboxPatch((3.0, y-0.42), 3.62, 1.0,
                  boxstyle="round,pad=0.03,rounding_size=0.08", fill=False,
                  edgecolor=color, lw=1.3, linestyle=(0,(3,2)), zorder=1))


def make_context():
    fig, ax = plt.subplots(figsize=(7.3, 2.7))
    ax.set(xlim=(0, 9.7), ylim=(-0.65, 3.1))
    ax.set_axis_off()
    ax.text(4.85, 2.9, "A typed sequential rewrite in a fixed context", ha="center", fontsize=13, weight="bold")
    context_row(ax, 1.98, "L", BLUE)
    context_row(ax, 0.6, "R", RUST)
    ax.text(7.85, 1.30, r"$L=R:\ B\longrightarrow C$", ha="center", fontsize=10.3)
    ax.text(4.85, -0.16, r"$q\circ L\circ p=q\circ R\circ p:\ A\longrightarrow D$", ha="center", fontsize=12)
    ax.text(4.85, -0.53, "Dashed box = the typed hole. This figure covers sequential contexts only.", ha="center", fontsize=8.2, color=MUTED)
    return save(fig, "second-pass-typed-context", "Sound replacement of a typed linear map in a sequential context")


def check_fierz():
    results = []
    for n in range(2, 6):
        generators = []
        for i in range(n):
            for j in range(i + 1, n):
                symmetric = np.zeros((n, n), complex)
                symmetric[i, j] = symmetric[j, i] = 0.5
                antisymmetric = np.zeros((n, n), complex)
                antisymmetric[i, j], antisymmetric[j, i] = -0.5j, 0.5j
                generators.extend([symmetric, antisymmetric])
        for k in range(1, n):
            diagonal = np.zeros(n)
            diagonal[:k], diagonal[k] = 1, -k
            generators.append(np.diag(diagonal / np.sqrt(2 * k * (k + 1))))
        t = np.array(generators)
        assert len(t) == n*n - 1
        normalization = np.einsum("aij,bji->ab", t, t)
        identity = np.eye(n)
        lhs = np.einsum("aij,akl->ijkl", t, t)
        rhs = 0.5*np.einsum("il,kj->ijkl", identity, identity) - (0.5/n)*np.einsum("ij,kl->ijkl", identity, identity)
        e1 = float(np.max(np.abs(normalization - 0.5*np.eye(n*n-1))))
        e2 = float(np.max(np.abs(lhs-rhs)))
        assert max(e1, e2) < 1e-12
        results.append({"N": n, "normalization_max_error": e1, "fierz_max_error": e2})
    return results


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    validation = check_fierz()
    files = make_fierz() + make_causal() + make_context()
    record = {
        "generator": str(Path(__file__).relative_to(ROOT)),
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fierz_boundary": {"inputs": ["j", "l"], "outputs": ["i", "k"],
            "summed_adjoint": "a", "exchange_pairs": [["l", "i"], ["j", "k"]],
            "direct_pairs": [["j", "i"], ["l", "k"]],
            "exchange_coefficient": "1/2", "direct_coefficient": "-1/(2N)",
            "crossing_is_vertex": False},
        "fierz_finite_numerical_checks": validation,
        "causal_models": {
            "exogenous_law": "U fair Boolean",
            "A": {"equations": ["X=U", "Y=X"], "edges": [["U","X"],["X","Y"]],
                  "after_do_X_0_edges": [["X","Y"]], "after_do_X_0_prob_Y_1": "0"},
            "B": {"equations": ["X=U", "Y=U"], "edges": [["U","X"],["U","Y"]],
                  "after_do_X_0_edges": [["U","Y"]], "after_do_X_0_prob_Y_1": "1/2"},
            "shared_observations": {"00": "1/2", "11": "1/2"}},
        "typed_context": {"fixed_maps": ["p:A->B", "q:C->D"],
            "replacement": "L=R:B->C", "conclusion": "q o L o p=q o R o p:A->D",
            "scope": "sequential linear-map contexts; not full tensor/traced/dagger graph syntax"},
        "rendering": "vector PDF/SVG plus 240dpi PNG; final visual inspection recorded separately",
        "files": files,
    }
    (OUT / "second-pass-figures.json").write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"files": len(files), "finite_fierz_checks": validation}, indent=2))


if __name__ == "__main__":
    main()
