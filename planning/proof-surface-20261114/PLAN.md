# Source-proof and surface-quantum continuation

Base: f118d0fff06bdf50ae9597459645b636f3c2dc56. This is a work plan and
source-access receipt, not a claim that every upstream theorem is verified.

The user's request requires a source-led port of the research proofs, not an
argument based only on architecture names or on the previous supplement.
The five accessible requested repositories were reopened at exact commits:

- TropicalGT: f8ffc7150afdd83bace8078c86fde7c8eeb0e08e
- ToricGT: a5199bc989a6fb170e21220e5e87bf95bc2fc0b4
- ToricGT-Program: f91ba1811b5a4f70d53c7120acf8ca2a0049f85b
- Mora-3: 75ac2d696f42da0a673fc43a20d84686a2ceed40
- Tropical_Quivers_of_Archs: 2b6ab79a685e2c6233fb8892e59589951feeddad

`amelie-iska/TropicalGT-Program` returned 404 both from the public API and the
selected GitHub connector. No equivalence with a different repository is assumed.
TropicalGT itself contains Parts I–IV and a separate `references/main.tex` on
graph expressivity; these are included rather than omitted from the audit.

## Checkpoints

1. Preserve exact theorem/proof text, locations and source hashes in a replayable
   source archive; distinguish source porting from mathematical review and Lean
   checking. Audit uniform graph approximation, tensor order, decoding metrics,
   tropical geometry and finite-temperature assumptions against primary papers.
2. Give constructive corrected graph-to-graph proofs where needed, with explicit
   encoding, permutation and decoder interfaces; implement counterexample and
   positive-control tests and formalize useful transfer/robustness statements.
3. Implement a connected dessin/rotation-system → surface → qubit circuit →
   classical tropical controller example. Check independent CPU/browser kernels,
   and cuQuantum if already installed and safely available. No simulated circuit
   is represented as quantum hardware or as evidence of quantum advantage.
4. Add measured physical/communication controls with source-native representation,
   held-out grouping, graph-side-information and compression accounting. Preserve
   old results and disclose unsuccessful/null results and selection limitations.
5. Build interactive, accessible SVG views of the actual combinatorial surface,
   circuit, per-coordinate tropical winners and observables. Provide a flat chart,
   readable numeric alternatives, shareable state, export and mobile tests.
6. Publish tested source checkpoints without force; retain evidence and update the
   associated dataset and Pages. Synchronize clean clones without disturbing the
   original Mora training campaign or unrelated processes.

## Proof status policy

Written upstream proof, repaired written proof, finite computation, Lean theorem,
CPU/GPU numerical agreement, training result and physical observation are distinct.
The source inventory must never mark all extracted claims as validated by default.
A positive uniform approximation theorem is compatible with the fact that Yun's
specific theorem is Lp; use an appropriate uniform theorem or an explicit proof.
No generated explanation is substituted for the user's actual source statements.
