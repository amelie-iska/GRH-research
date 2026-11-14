# Exact graph-computation research workbench

This extension is part of [GRH-research](https://github.com/amelie-iska/GRH-research).
It preserves the historical atlas/book release and adds a separate research
supplement, live finite-certificate adapters, measured-data component experiments,
and a source-pinned BGG/category-O synthesis.

## Run the checked components

```sh
# Python standard library plus Node for cross-runtime parity tests.
# The real-data protocol tests additionally require NumPy.
python3 -m unittest discover -s workbench/tests -v
python3 -O -m unittest discover -s workbench/tests -v
python3 workbench/numerics.py
python3 workbench/bgg.py

# Live laboratory adapter and optional pinned Lean compiler; loopback only.
python3 workbench/bridge_host.py --lean /absolute/lean-4.24.0-linux/bin/lean
# Open http://127.0.0.1:8767/workbench/
# Or /workbench/laboratory.html?lab=fluids (or lab=cosmology).
```

The browser computes bounded exact rational contracts. The local service emits
only fixed Lean templates and rejects uploaded code. A receipt is invalidated
when inputs change and is accepted only for its matching payload digest. Static
GitHub Pages cannot run Lean; it supports arithmetic/export and identifies that
limitation. The existing fluid and cosmology pages are not rewritten on disk.

Five contract types are implemented: positive heat-stencil coefficients, weighted
gain contraction, finite Monte Carlo rank, an allocated family-wise risk budget,
and skew-symmetric quiver/positive rational seed mutation. The exact Python/JS
implementations are separately replayed. Four measure-theoretic Lean statements
retain event calibration and model discrepancy as premises. Six BGG coefficient
identities are formalized; full category O and physical theories are not.

## Research and data

`research/main.tex` builds the separate supplement with `pdflatex` from that
directory. It includes corrected graph-approximation hypotheses, constructive
Turing and circuit mechanisms, ConvexTok, GFlowNets, quantum/hybrid scope, analogy,
cluster/gentle/order connections, actual measured-data results and the BGG layer.
The historical monograph PDF has not been silently replaced.

`experiments/run_realdata.py` executes a bounded CPU study using the actual pinned
Mora-3 TokenGT/tropical modules. It is not the full model or the original training
campaign. The recorded release contains 16 freshly trained component runs on
four measured/observation-derived processes, plus a known human-English control.
All seeds, negative results, costs and failed preflights remain visible.

`datasets/package.py` builds a rights-aware publication packet: NOAA graph records,
separate test-only exact fixtures, primary-source catalog, reproducibility source
and execution evidence. The associated dataset is
[GRH-Physical-Graph-Workbench](https://huggingface.co/datasets/AmelieSchreiber/GRH-Physical-Graph-Workbench).
Its manifest and publication receipt, rather than this link alone, establish the
published revision. SILSO and ECG raw records are source-linked rather than
relicensed or copied. No third-party full-text papers or credentials are included.

## Evidence boundaries

A finite scalar proof does not establish continuum convergence, a correctly
calibrated noise model, categorical equivalence or an observed physical signal.
Predictive compression is not evidence of an intentional message. The measured
pilot reports both conditional likelihood and model/memory-inclusive coding costs;
it does not compute Kolmogorov complexity or establish an architecture-wide win.
BGG exact examples and synthetic contract fixtures remain mathematical references,
not mislabeled physical data or trained semantic capabilities.
