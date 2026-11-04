# Exact geometry and game examples

From the repository root, run:

```sh
.tools/book-quantum-cpu/bin/python examples/learned_frontier/geometry/check_geometry.py
```

Uses the existing SymPy 1.14.0 environment; installs nothing. All inputs are
deterministic. Generated exact evidence is `outputs/exact.json` under this
directory. Override with `--output PATH` when a separate preserved run is needed.

The checker covers a degree-three theta universal graph cover and finite-support
deck-Hom decomposition; dual-number 2D Frobenius pants gluing plus a heralded
isometry; exact CHSH values and its Bell matrix; and ordinary right modules of
the actual infinite genus-two polynomial dessin algebra, with explicit simple
and branch resolutions through degree12 and their Hom/Ext/Tor calculations.

General proofs, external theorem pins, and category/physics limitations are in
`planning/learned-frontier/geometry/REVIEW.md`. The graph cover, actual infinite
dessin algebra, oriented TQFT and nonlocal game are separate specified models.
The finite program does not establish general HMS, anabelian reconstruction,
MIP*=RE, Connes embedding results, completed-order equivalence, or GRH.
