# GRH research book and computational laboratory: master implementation plan

Updated 2026-11-03. This is the governing plan for all instructions in this conversation. Earlier plans, sources, proofs, experiments and histories remain preserved. Later user instructions amend this plan and its queue; they do not silently cancel the original research objective.

## Objective and completion contract

Develop a coherent, didactic research book from both complete Amelie Schreiber source manuscripts, with concise and extended TeX/PDF papers, a private repository, an on-page interactive book, exact mathematical constructions, useful physics and quantum/hybrid implementations, meaningful training experiments, and progressively complete Lean4 verification. Continue independent research toward a complete rigorous proof of the intended GRH scopes.

There are two distinct acceptance gates:

1. **Implementation completion:** the requested content, reviewed mathematics, computations, trained examples, architecture inspectors, unique contextual visualizations, documentation and verification coverage are delivered, reproducible and tested. Complete source preservation is not the same as complete corrected exposition or full formalization.
2. **Research completion:** the independent arithmetic determinant/zero-location bridge and all scope-specific obligations are proved, with explicit derivations, appropriate kernel checks and independent adversarial review. A trained model, finite check, conditional theorem, reformulation, known-spectrum benchmark or unfinished Lean interface does not pass this gate.

Neither gate is inferred from time spent or a scheduled run ending. Refuted assertions cannot be formalized as valid theorems; retain the original claim as historical source data and formalize its correction/counterexample where possible. Do not promise a date or guaranteed proof of an open problem.

## Non-negotiable working constraints

- Root: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH`. Private remote: `amelie-iska/GRH-research`.
- Preserve the three pinned source clones, both original source paths, all data/history/outputs/caches/checkpoints/environments and unrelated changes. No deletion, cleanup, migration, broad upgrade or history rewriting.
- Preserve the two complete source TeX files, with hashes, in historical source volumes. Maintain `book/SOURCE_COVERAGE.md` mapping every source topic to corrected development, examples, formal status and any refutation.
- Use actual infinite locally gentle algebras and completed surface orders of cellular dessins as primary algebra examples. Explicit finite quotients/support strata must retain their category labels.
- Keep polynomial, formal, Laurent and operator-norm completions distinct; module, lattice, stable, perfect and bounded-derived categories are not interchangeable.
- Maintain Dirichlet, Hecke, Dedekind, elliptic-curve and general Artin scopes, critical centers, holomorphy and normalization separately. Do not assume the desired positivity or GRH to claim an unconditional result.
- Existing Lean4.24/mathlib pins and environments stay unchanged. The new approved CPU environment is `.tools/book-quantum-cpu`, with its lockfile. Ask before further production dependencies/infrastructure, paid or cloud/GPU jobs, OAuth/account linking, broad access or irreversible actions.
- Use existing GitHub CLI authentication. Never reuse chat credentials in files, commands, URLs, logs or commits. Research stays private; upstream-only public forks contain no private research.
- Keep the local preview available at `http://127.0.0.1:8765`. Restart only its known process when needed; do not expose the server publicly or enable public Pages without explicit authorization.
- Keep MCP servers disabled unless an exact server materially helps; enable only that server and disable/verify after use. Do not change Claude configuration.
- Preserve requested periodic links on substantive progress; avoid no-op/repetitive status commits and repetitive visualizations.

## Current verified baseline

Private milestone `948fc4c2fe18ce2e5a71b57b97ca3bc93a3284ad` is pushed. It contains the 26-chapter working book, both full historical source editions, 23/50-page article editions, six actual CPU-trained finite models, larger/hyperbolic surface views, pinned ToricGT/NVIDIA sources, 240 successful printed Lean dependency reports, and independent reviews. See `outputs/checks/2026-11-03-book/milestone.json` for evidence and limits.

The latest user-requested extension is in progress: deduplicate the on-page/PDF diagrams, add architecture-level tensor/state inspectors, connect persistence and commutative algebra explicitly to the cited papers, and correct/expand the Manim scenes. Source preservation and selected checked components do **not** mean every source assertion or entire book chapter is already formalized.

## Workstreams and dependency order

### P0 — Preserve a working edition and remove duplicated visuals

Files: `scripts/assemble_book.py`, `scripts/prepare_book_html.py`, `scripts/render_html_diagrams.py`, `scripts/verify_project.py`, book/HTML outputs.

- Give each interactive tool one canonical location, with topic-specific references from related chapters. Do not insert the same atlas/learning/AR iframe under unrelated chapters.
- Keep one canonical rendering of each node/HLS diagram; retain distinct component windows, stable-category pictures, proofs, matrices and calculations.
- Preserve every historical source and previous build. Compile into staging outputs and promote a build only after it passes, so a failed build does not break the live PDF.
- Verify unique iframe sources, correct links, actual SVG geometry, valid native MathML, no broken assets, no overfull boxes/unresolved references, and live preview responses.

Acceptance: the user can navigate the book without repeated generic panels or broken PDF/HTML diagrams. Deduplication does not delete substantive mathematics.

### P1 — A bbycroft-style architecture inspector using original implementation

Files: `examples/architecture/`, `web/architecture.html`, associated local JS/CSS/data, `book/chapters/architecture.tex`.

- Quantum: inspect actual trained QCNN4/QCNN9, quantum graph convolution, quantum-feature attention, clock/shift carriers and photonic pooling. Show preparation, gates, states/probabilities/phases, readouts, density matrices, pooling channels and tensor dimensions.
- Classical graph/token: implement auditable miniature TokenGT projection/Q/K/V/score/softmax/FFN passes; transport graph identifiers correctly rather than claiming unchecked permutation equivariance.
- Tropical: ordinary scaled QK scores followed by the actual max-plus value reduction, witness indices, ties, margins and block scheduling. Do not label a separate max-plus helper as the upstream attention layer.
- ToricGT: NC-torus phase features, toric certificates, graph attention, Soft-MoE token-dispatch versus expert-slot-combine axes, and useful optional GFlowNet/memory/oracle/derived/persistence probes from the pinned source inventory.
- Hybrid: explicit quantum-feature/classical-head boundaries and the actual trained Harper proposal → exact rational PSD certificate pipeline. Display its known analytic spectrum alongside learned values.
- Provide orbit/zoom/step/play, selectable tensors/heads/tokens, numerical values and code links. Label real checkpoint replay, small executable reference model, proposed extension and unavailable backend distinctly.

Acceptance: every architecture category has a numerically verified forward example and useful intermediate inspection. No fabricated upstream weights, training reproduction or quantum advantage is implied. Original UI/code/assets are used; the referenced website is interaction inspiration.

### P2 — Persistence, generic resolutions and algebraic geometry

Primary papers: arXiv:1810.06750v5,1812.00621v1,2210.11433v1, with exact reviewed sections and hashes.
Files: `book/chapters/persistence.tex`, `research/persistence-interfaces.md`, `examples/persistence/`, a unique on-page persistence tool and Lean modules.

- Construct actual one-/multi-parameter modules, structure maps and rank invariants; do not replace multiparameter persistence by unsupported barcode claims.
- Work out `k[x,y]/(x,y)^2` completely: bifiltration/CW realization, minimal multigraded free resolution, all differentials, exactness, Hilbert numerator, Betti shifts, syzygies and the associated Young/Schur representation structures with characteristic and grading hypotheses.
- Extend to parameterized staircase ideals with explicit generators/syzygies. Distinguish the commutative parameter ring from the primary infinite surface algebra.
- Connect generic complexes, Fitting/determinantal loci, rank constraints and incidence resolutions with the necessary grade/rank/birational hypotheses. Include corrected examples and counterexamples to overbroad claims.
- Build fixed-snapshot quantum/graph bifiltrations with genuine monotonic maps. A training history is not a filtration by default; use proved envelopes, unions, zigzags or fixed-channel contraction only under stated assumptions.
- Connect to actual surface-order modules and projective/derived data through explicitly defined compatible functors, without assuming short resolutions or Langlands/GRH from analogy.

Acceptance: exact polynomial/GF2/linear-algebra diagnostics, actual module maps, proved exactness, independently reviewed source scope, in-book code and matched visual data.

### P3 — Correct and expand Manim and surface geometry

Files: `examples/quantum/manim_research.py`, generated clips, captions and scope records.

- Replace the legacy three-disjoint-loop torus clip as the theta example with three actual theta arcs sharing the correct black endpoints and white midpoints. Preserve the old clip labelled as a clock schematic.
- Animate the signed HLS nine-module component window in its intrinsic quotient category, with mesh composition and exactness clearly distinguished.
- Animate persistence births, module maps, staircase/syzygy diagrams and free resolution geometry using the same tested data as the interactive tool.
- Animate quantum gates and genuine CPTP pooling; include larger higher-genus and hyperbolic finite-window examples where informative.
- Extend 3D/4D views with controls and correct labels for projections, metrics, cuts, side pairings, finite patches and compact quotients. More ambitious surfaces require actual combinatorial/Belyi/quotient certificates.

Acceptance: every clip renders with existing tools, matches checked data, has legible labels and an accurate caption; no animation substitutes for proof or physical evidence.

### P4 — All original mathematical and physics material, cohesively developed

Maintain a topic-by-topic inclusion/correction ledger for both complete originals. Expand the critical book rather than merely link an archive.

Topics include dessins/quivers/orders/normalization, projective resolutions and duality, strings/bands/infinite words, AR quivers/quilts/almost-split sequences, Hom-controlled functors, derived categories and DG/A-infinity structures, Koszul duality and appropriate Fukaya/HMS/geodesic models, Schur/Young/LR/Procesi/Schofield–Van den Bergh invariants, Leavitt/graph C* and NCG, determinant and zeta/L-function interfaces, generic complexes and persistence.

Retain and improve all physics: positive transfers versus unitaries, logarithms and domains, finite/infinite clocks and rotation algebras, holonomy, QFT/Wick/reflection-positivity hypotheses, entanglement/metric/Einstein models, quantum graph learning and renormalization, associative memory with valid measurement models, noise/resources, molecular/peptide proposals and actual evidence, exchange controls, hyperbolic CSS and hardware assembly. Correct refuted claims rather than hide them, and label measured facts, simulations, proposals and mathematical theorems separately.

Acceptance: complete source-topic mapping, cohesive chapter organization, all definitions/constructions/proof details, unique relevant figures/examples and explicit unresolved statements.

### P5 — Larger training experiments and independent evaluation

- Preserve the six executed baselines, seeds, parameters, splits, histories and held-out results.
- Add larger surface/graph/hyperbolic-local architectures with meaningful targets, matched classical and architectural ablations, uncertainty, OOD tests and compute accounting.
- Use PennyLane/Cirq/Qiskit/Strawberry Fields where technically appropriate; distinguish qubit, photonic, Gaussian and non-Gaussian models.
- Keep cuQuantum/CUDA-Q adapters and forks pinned. Actual supported NVIDIA execution is a separately approved environment/hardware task; do not report source cloning as a GPU benchmark.
- Connect learned components to proposal/search/control of rigorously checked constructions, not as proof of GRH.

Acceptance: real reproducible training and honest negative/limited results. No checkpoint leakage or unperformed hardware claims.

### P6 — Comprehensive Lean4 development by mathematical dependency

Build on actual existing objects and pinned mathlib. Prioritize definitions/interfaces reused across book chapters, then theorem dependencies.

- General dessin paths/completions/resolution exactness; actual order modules and center action.
- Exact/derived/AR factorization interfaces and appropriate category comparisons.
- Graded persistence modules, syzygies/exactness, determinantal/Schur interfaces.
- Finite/infinite operator and channel statements with their genuine hypotheses and domains.
- Arithmetic characters, ideals/CRT/Poisson, determinant limits and zero-location arguments once mathematically supplied.

Every claim is labelled fully kernel checked, component checked, prose proved, external theorem, experimental, refuted or open. Print theorem types and all axiom dependencies; no `sorry`, `admit`, project axioms or hidden desired positivity. Review formal theorem types against the prose. Do not formalize an unrelated finite toy and call the intended theorem verified.

Acceptance for a fully formal chapter: actual objects, all dependency interfaces and stated theorems checked, explicit external dependencies identified. Whole-book formalization remains incomplete until this holds throughout.

### P7 — Arithmetic research toward GRH

The current original-family high-gcd bound is recorded in `research/short-row-high-gcd.md`. Attack the remaining low-gcd kernel, especially common divisor1, preserving all masks and moving-profile uniformities. Alternatively construct a genuinely different positive arithmetic determinant family escaping the established finite full-deck coefficient obstructions.

Maintain local Jacobi/cellular results, center/deck/ramification/multiplicity boundaries, conductor/gamma/bad-prime normalizations and scope distinctions. Classical Weil/Grothendieck/Cartan-Weil/NCG/spectral/HMS sources are useful only with their actual hypotheses and an explicit arithmetic comparison.

Acceptance of each research attempt: a complete derivation, precise counterexample, or documented exact failed step and surviving result. Rotate failed routes, do not repeat completed audits as progress. Acceptance of GRH requires the full research completion gate above.

### P8 — Synchronized deliverables and release discipline

Keep the concise and extended articles, critical book, native-MathML on-page edition, full historical sources, source code, Sage/Macaulay-style examples, Lean coverage, README and project page synchronized. Compile and inspect changed content; do not multiply the same visualization across chapters. Keep canonical example/tool anchors and cross-references.

Before each milestone: inspect relevant staged changes; run focused scientific/browser/Lean checks, source-pin and credential scans, PDF/HTML integrity and private visibility. Push substantive verified work only. Preserve unrelated/concurrent edits and raw failed probes. Keep a concise handoff with evidence, remaining risks and the next concrete task.

## Automated iteration protocol

The existing hourly `grh-research-loop` heartbeat is the implementation/research loop; update it rather than create a second scheduler or custom cron daemon. It reads this plan plus `planning/IMPLEMENTATION_QUEUE.json` and the latest durable handoff.

Each run:

1. Read Git state/instructions/README/locks/scripts, this plan, queue, progress, claims, obligations, continuation, latest reviews/logs and current local-preview state.
2. Reconcile unfinished concurrent work. Select one ready, concrete queue item; use the queue helper's atomic claim/checkpoint and preserve unrelated edits. If a prior task is incomplete, finish or hand it off explicitly.
3. State the exact acceptance criterion and implement/research it. Use independent agents only when explicitly authorized/applicable; independently review major advances.
4. Run focused checks. Fix failures, record exact boundaries, and avoid broad redundant reruns unless new changes warrant them. Build to staging and promote only valid artifacts.
5. Update the chapter/source/formalization ledger, queue and concise handoff. Update the page/book/papers when relevant; keep the preview running.
6. At a real milestone, inspect staged changes, scan credentials/source pins/integrity/privacy, commit and push privately. Surface meaningful new links/findings or a concrete blocker; do not make no-op status commits.
7. Select the next concrete implementation or research task. Keep the heartbeat active until both acceptance gates pass or the user explicitly pauses/cancels. Never mark GRH proved because implementation tasks are exhausted.

## Immediate queue

P0 deduplication/build promotion → P3 corrected Manim completion → P2 persistence chapter/checked data → P1 architecture tensor/state export and inspector → P6 formal interfaces → P5 larger matched experiments and P7 low-gcd/arithmetic bridge attempts. Work may proceed independently where inputs are already fixed; do not overlap edits or mislabel partially completed features as shipped.


## Requested covering and geometric literature extension (2026-11-03)

The three new references are pinned and reviewed under
planning/reviews/covering-literature/. Retain the new exact theta-quotient
cover, non-lifting and Hom-control calculations when expanding the AR and
derived chapters. Respect precovering versus covering/density, right/left
module conventions, finite string quotient versus quadratic gentle algebra,
finite module versus DVR lattice, and graded Fukaya category versus compact
Riemann surface/completed order. The specified higher-genus family and derived
non-density are proved; three matrix components are Lean checked. General
module/functor formalization and any actual GLS/skew-group identification
remain P6/P4 obligations. Do not infer positivity or block determinants from
a Hom decomposition. This reference task does not replace the next canonical
architecture inspector or the open low-gcd/positive arithmetic research lane.


P1 completion note (2026-11-03): the core numerical architecture inspector is
implemented for all22 saved cases plus the computed clock, with one canonical
book embedding. Its detailed checks and limits are recorded in the queue,
examples/architecture/README.md and independent inspector review. Optional
upstream probes, broader trained campaigns and physical/GPU runs remain
separate P4/P5 obligations. P2 persistence tools are the next ready dependency.

P2 tools completion note (2026-11-03): one canonical persistence laboratory
now exposes strict staircase resolutions, rank/Betti/syzygy/CW/fiber data,
actual nodal coefficients and fixed-channel quantum flag inclusions. General
proofs are integrated into the shared articles and book. Numerical quantum
labels are frozen and separately scoped; exact finite ranks are checked by
independent algorithms and review. P6 persistence/module formalization is the
next dependency-ready task; the arithmetic lane remains independently open.

P6 persistence-interface note (2026-11-03): the worked square-ideal module now
has an actual MvPolynomial ungraded free resolution, ideal quotient and residue
Hom differential calculation checked in Lean. Nineteen printed dependencies
use standard foundations; the complete pinned suite passes262 reports. The
ordinary regular action is explicitly distinguished from the residue field
action. This closes the concrete interface task, not general staircase,
graded/CW/Schur/cone/category formalization or either completion gate. Continue
P4 source expansion with a precise corrected construction and source-topic map;
retain the independent P7 arithmetic lane and the broader P6 formal backlog.
