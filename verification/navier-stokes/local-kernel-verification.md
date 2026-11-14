# Fresh local Lean verification

Fresh Lean kernel elaboration of the four local companion modules only, with their exact existing sources and cached pinned Lean 4.24/mathlib. The printed dependencies are compared declaration by declaration to the original verification manifests. This does not verify every manuscript theorem or any upstream continuum Navier--Stokes release theorem.

Status: **verified**. 4 modules; 82 declarations. Checked 2026-11-13T21:30:23.635201+00:00.

Compiler: `Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)`. Mathlib: `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

| Module | Declarations | Exit | Warnings | Axiom manifest match |
|---|---:|---:|---:|---|
| BridgeTheorems.lean | 25 | 0 | 0 | True |
| QuantumInterfaces.lean | 7 | 0 | 0 | True |
| DiagramGrammar.lean | 16 | 0 | 0 | True |
| FluidInterfaces.lean | 34 | 0 | 0 | True |

The original sources, manifests, and original logs were unchanged: **True**. Every declaration reports dependencies only among `propext`, `Classical.choice`, and `Quot.sound`. These foundational axioms are disclosed, not claimed absent.

The new fluid module certifies selected finite matrix, recurrence, block, and derivative identities. In particular, the energy derivative is not the global finite ODE continuation theorem; discrete memory is not the continuous matrix-exponential formula; determinant arithmetic is not covering-space topology; and a zero block composite is not the analytic Volterra convergence theorem.

The separate upstream Lean 4.34 release attempt did not complete kernel verification after a rate-limited cache download and missing compiled imports. This successful local check does not change that status. See `release-build-verification.json` for the exact earlier failure boundary.

Reproduce with `python extension/review/navier-stokes/local-kernel-verify.py` after installing the exact pinned tools at the recorded paths, or supply `--toolchain` and `--mathlib`. The script performs no downloads.
