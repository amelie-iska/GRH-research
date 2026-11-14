# Yang–Mills source review — 13 November 2026

## Result for the manuscript

The late-October 2026 OpenAI result is a **nonperturbative existence construction**, not just the earlier single-minus gluon amplitude calculation. The independent group's initial assessment dated 10 November judges the October submission to construct a Wightman quantum field theory from a four-dimensional Wilson-lattice scaling limit for the specified simple compact gauge groups. It explicitly does **not** claim a mass gap or uniqueness of the infinite-volume limit.

The manuscript's four chapters are in `manuscript/chapters/gauge-theory.tex` in the shared staging workspace. They contain 9,564 words as measured by whitespace tokenization, 13 complete supporting proofs, 14 named theorem/proposition statements, and 27 cited bibliography keys. One named theorem is explicitly the external Atiyah–Hitchin–Singer index theorem. The external 2026 construction and deep reconstruction results are explained and cited, not relabeled as proofs created or rebuilt by this project.

## Immutable upstream identities

| Material | Frozen identity |
|---|---|
| Original October submission | `yang-mills-group/OpenAI-YM-20261028@3456e5e75cf8d4cd558955a5c7638fba2d68f464` |
| Independent review repository | `yang-mills-group/YM@55ba9fc36293b3f4d52c6b1f813169a0be76ee98` |
| Assessment | `docs/assessment-1.pdf`, 35 pages, 657,626 bytes |
| Assessment SHA-256 | `8e658c00900bf723cbe90436eb1f78fca4f287e008a85c21fdceaf59e61db219` |
| Submission Lean | `leanprover/lean4:v4.32.0` |
| Pinned Mathlib | `81a5d257c8e410db227a6665ed08f64fea08e997` |
| Independent Comparator kernel | Lean 4.34.0 |

The assessment first fetched from the default branch was byte-compared with the immutable URL and matched. `source-manifest.json` records downloaded evidence hashes. `external-proof-dependencies.json` records toolchains and intended endpoints without treating historical evidence as a local build result.

Primary links:

- [Official announcement, 26 October](https://openai.com/index/building-scientific-understanding-with-academic-communities/).
- [Frozen independent assessment](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/docs/assessment-1.pdf).
- [Frozen original source](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464).
- [Official Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
- [Earlier gluon-amplitude paper](https://arxiv.org/abs/2602.12176v2).

## What was actually read

### Full documents and interfaces

- All 35 pages of the independent assessment, including the statement glossary on pages 23–35.
- All 14 pages of the Clay/Jaffe–Witten problem statement, including references. Its historical status statements are treated as historical, not copied as 2026 status.
- Official OpenAI announcement, including the distinction between pure Yang–Mills, QCD, and the broader announced construction.
- Original source `README.md`, `lean-toolchain`, `Solution.lean`.
- `PublicTheory.lean` (325 lines), `PublicWilson.lean` (92 lines), `ChallengeSpec.lean` (190 lines), `Construction.lean` (42 lines).
- Review `AcceptanceSpec.lean` (178 lines), `CombinedAcceptance.lean` (122 lines), `CompleteOS.lean`, `OPESpec.lean`, `OPECheck.lean`.
- Commented `OctoberChain.lean` (298 lines) and `LeadingTrace-20261028.lean` (357 lines).
- Historical clean-build report, source/audit summary, acceptance Comparator result, and the four control outcomes. These record upstream actions, not actions performed here.

### Bibliographic or theorem-level use

The classical sources on gauge theory, ASD deformation/index, ADHM, Wilson lattice theory, OS reconstruction, transfer matrices, elliptic bundles, and Narasimhan–Seshadri are cited through primary publisher/author or repository records. This review does not claim a complete independent proof audit of all those papers. The manuscript supplies its own derivations for the elementary propositions it uses and labels deep external results.

### Not performed

- No full read of all 9,477 upstream Lean files.
- No fresh build or kernel replay of the million-line submission.
- No assertion of an independently implemented second-kernel verification.
- No analysis of the November 4 submission, which the repository listed as work in progress.
- No certification of the announcement's QCD or unified-theory claims.
- No proof of mass gap, infinite-volume uniqueness, or every theorem in the entire manuscript in Lean.

## Mathematical scope ledger

| Question | What the reviewed package establishes or reports | Boundary |
|---|---|---|
| Gauge group | Closed matrix subgroup of a unitary group with nonabelian simple real Lie algebra | Use the actual formal predicate, not an unspecified notion of simple group |
| Finite theory | Wilson action and normalized product Haar law, local gauge-invariant insertions | Compact finite integration alone is much weaker than continuum existence |
| UV limit | Full convergence on the construction's chosen spacing sequence at each suitable fixed volume | No universality for every spacing schedule or action |
| IR limit | Every increasing volume sequence admits a refinement; one refinement works coherently for the hierarchy | No uniqueness across refinements |
| Phases | Mixture represented by a measure on a ground-state character space; selected and other phase theories | A selected phase is not automatically the original periodic finite-volume limit |
| Wightman reconstruction | Explicit positive-energy, domain, covariance, locality and vacuum properties of selected phase | Positive energy and vacuum uniqueness do not imply a gap |
| Independent OS bridge | Selected centered scalar trace on diagonal-flat Schwartz tests with growth condition | Not every tensor field translated independently; not uniqueness of unrestricted Euclidean contact extensions |
| Trace | Positive leading coefficient `3 dim(g)/pi^4` in fixed normalization | A UV asymptotic does not constrain all low-energy spectral support |
| Non-freeness | Specified finite mass-shell Wick-profile exclusion | Not every continuous-mass generalized free description excluded by that public clause |
| OPE | Uniform finite-degree remainder bounds with shared coefficients across phases/spectators/truncations | Degree cutoff is not loop order; no all-orders perturbative matching inferred |
| Positive two-point calibration | A nonzero limiting observable establishes a scale-sensitive probe | `TwoPointScale.MassLimit` is not a mass-gap theorem |
| Millennium problem | Substantial existence result with independent assessment | No mass gap in reviewed claim; no Clay certification inferred |

## Formal-verification distinctions

The original `YangMills.jointExistence` target did not retain every construction certificate available in `YangMills.constructed`. The independent stronger endpoint `YMReview.Acceptance.combined_acceptance` retains `C.Makes` and `Spec.Final`, tying the finite lattice law, normalization, continuum table, phase, trace and reconstructed theory to one witness. The manuscript explains why quantifier order and this common witness matter.

The reported clean build used no pre-existing project build artifacts and compiled 9,470 project modules in 11,036.28 seconds (about 183.94 minutes). It reused the official Mathlib dependency cache. Historical records report 100,168 project declarations rechecked for 17 principal results, 14,364 external declarations at the boundary, and only `propext`, `Classical.choice`, and `Quot.sound` for those endpoints. A `sorry` in the separate reference challenge is not imported by the solution.

The recorded combined Comparator run rebuilt the review modules but reused the prior submission build. It used the built-in Lean kernel with pinned tools. The macOS development launcher did not supply Linux Landrun process isolation. Controls accepted a valid theorem and rejected a changed theorem statement, an unapproved axiom, and a changed definition. The upstream records explicitly leave semantic agreement with the intended physics to review and do not claim a Palomar submission.

## Original supporting derivations supplied

1. Curvature-square and Bianchi identities with graded-bracket conventions.
2. First and second Yang–Mills variations, including the curvature term.
3. Self-dual/anti-self-dual energy inequality and Yang–Mills implication.
4. ASD deformation complex and exact nonzero-cotangent symbol sequence.
5. ADHM zero-product identity and constant-rank middle dimension.
6. Exact complexes with arbitrarily small positive Laplacian eigenvalues.
7. Finite Wilson partition-function bounds and gauge invariance.
8. Positive-type Wilson link weight via unitary characters and tensor products.
9. OS null quotient and positive-definite induced form.
10. Hamiltonian gap equivalence with uniform Euclidean-time decay.
11. Positive spectral measures with identical UV trace asymptotics and different gaps, with full dominated-convergence proof.
12. Passage of a uniform semigroup gap through strong convergence with convergent ground-state projections.
13. A direct flat elliptic-torus/order/character/line-bundle bridge, including contragredient action and exact twisted spectrum.

The chapter also proves a contractive renormalization-error recurrence and derives the exact one-loop model ODE solution, while separating both from a continuum mass-gap theorem. Some items combine named propositions with direct calculations. These are ordinary mathematical proofs in the manuscript. They should be marked as Lean-verified only for individual declarations that are actually implemented and compiled by the main project.

## Suggested interactive figures

- Curvature obstruction: show `d_A^2=[F_A,-]`, with a flat versus curved control; explain which projected complex is valid at ASD connections.
- ASD symbol: rotate a nonzero covector in four dimensions, project to three dimensions, and display kernel/image dimensions 1 and 3. Explicitly label the rendering as a projection.
- Twisted elliptic-torus spectrum: use the exact equation `4*pi^2*((m+s)^2/L1^2+(n+t)^2/L2^2)` and sliders for holonomies/side lengths. Show kernel jump and absence of a uniform moduli gap.
- UV versus IR: compare the two explicitly defined positive spectral densities; label them spectral countermodels, not simulations of Yang–Mills.
- Limit order: display chosen UV sequence at fixed volume, refined IR sequence, phase decomposition and reconstructed fields; avoid suggesting interchangeable limits.

## Redistribution

Upstream OpenAI/YM code and review material declare Apache-2.0 with notices. If any downloaded upstream code is vendored, preserve its license and notices. The manuscript, bibliography, review and manifests are original project materials; linking to pinned upstream proof repositories avoids distributing their million-line source. Do not automatically publish the attached scanned books or unrelated downloaded papers.
