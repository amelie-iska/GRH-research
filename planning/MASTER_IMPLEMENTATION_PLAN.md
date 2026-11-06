# GRH research book and computational laboratory: master implementation plan

Updated 2026-11-03. This is the governing plan for all instructions in this conversation. Earlier plans, sources, proofs, experiments and histories remain preserved. Later user instructions amend this plan and its queue; they do not silently cancel the original research objective.

## Objective and completion contract

Develop a coherent, didactic research book from both complete Amelie Schreiber source manuscripts, with concise and extended TeX/PDF papers, a public repository, an on-page interactive book, exact mathematical constructions, useful physics and quantum/hybrid implementations, meaningful training experiments, and progressively complete Lean4 verification. Continue independent research toward a complete rigorous proof of the intended GRH scopes.

There are two distinct acceptance gates:

1. **Implementation completion:** the requested content, reviewed mathematics, computations, trained examples, architecture inspectors, unique contextual visualizations, documentation and verification coverage are delivered, reproducible and tested. Complete source preservation is not the same as complete corrected exposition or full formalization.
2. **Research completion:** the independent arithmetic determinant/zero-location bridge and all scope-specific obligations are proved, with explicit derivations, appropriate kernel checks and independent adversarial review. A trained model, finite check, conditional theorem, reformulation, known-spectrum benchmark or unfinished Lean interface does not pass this gate.

Neither gate is inferred from time spent or a scheduled run ending. Refuted assertions cannot be formalized as valid theorems; retain the original claim as historical source data and formalize its correction/counterexample where possible. Do not promise a date or guaranteed proof of an open problem.

## Non-negotiable working constraints

- Root: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH`. Public remote: `amelie-iska/GRH-research`.
- Preserve the three pinned source clones, both original source paths, all data/history/outputs/caches/checkpoints/environments and unrelated changes. No deletion, cleanup, migration, broad upgrade or history rewriting.
- Preserve the two complete source TeX files, with hashes, in historical source volumes. Maintain `book/SOURCE_COVERAGE.md` mapping every source topic to corrected development, examples, formal status and any refutation.
- Use actual infinite locally gentle algebras and completed surface orders of cellular dessins as primary algebra examples. Explicit finite quotients/support strata must retain their category labels.
- Keep polynomial, formal, Laurent and operator-norm completions distinct; module, lattice, stable, perfect and bounded-derived categories are not interchangeable.
- Maintain Dirichlet, Hecke, Dedekind, elliptic-curve and general Artin scopes, critical centers, holomorphy and normalization separately. Do not assume the desired positivity or GRH to claim an unconditional result.
- Existing Lean4.24/mathlib pins and environments stay unchanged. The new approved CPU environment is `.tools/book-quantum-cpu`, with its lockfile. Ask before further production dependencies/infrastructure, paid or cloud/GPU jobs, OAuth/account linking, broad access or irreversible actions.
- Use existing GitHub CLI authentication. Never reuse chat credentials in files, commands, URLs, logs or commits. Research is public by explicit owner instruction of 4 November 2026; credentials and unrelated model data remain protected.
- Keep the local preview available at `http://127.0.0.1:8765`. Restart only its known process when needed; do not expose the server publicly or enable public Pages without explicit authorization.
- Keep MCP servers disabled unless an exact server materially helps; enable only that server and disable/verify after use. Do not change Claude configuration.
- Preserve requested periodic links on substantive progress; avoid no-op/repetitive status commits and repetitive visualizations.

## Current verified baseline

Private milestone `948fc4c2fe18ce2e5a71b57b97ca3bc93a3284ad` is pushed. It contains the 26-chapter working book, both full historical source editions, 23/50-page article editions, six actual CPU-trained finite models, larger/hyperbolic surface views, pinned ToricGT/NVIDIA sources, 240 successful printed Lean dependency reports, and independent reviews. See `outputs/checks/2026-11-03-book/milestone.json` for evidence and limits.

The latest user-requested extension is in progress: deduplicate the on-page/PDF diagrams, add architecture-level tensor/state inspectors, connect persistence and commutative algebra explicitly to the cited papers, and correct/expand the Manim scenes. Source preservation and selected checked components do **not** mean every source assertion or entire book chapter is already formalized.

## Workstreams and dependency order

### User interface amendment: living dark mode

The user requested a fixed top-left dark-mode toggle with a biomechanical/future-starship aesthetic, staggered transformations and distributed living lights, motion and color-changing accents. Implement this across the project page, native book, source volumes and embedded laboratories, with persistent local preferences, a separate ambient-motion pause, reduced-motion support, accessible controls and unchanged scientific data. [Design and acceptance scope](living-theme-design.md); focused browser evidence is in `outputs/checks/2026-11-03-living-theme/`. This visual amendment does not close either completion gate or replace the next arithmetic research task.

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

Before each milestone: inspect relevant staged changes; run focused scientific/browser/Lean checks, source-pin and credential scans, PDF/HTML integrity and intended public visibility. Push substantive verified work only. Preserve unrelated/concurrent edits and raw failed probes. Keep a concise handoff with evidence, remaining risks and the next concrete task.

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

P4 DG-foundations slice (2026-11-03): source1308–1478 now has an explicit
corrected chapter, actual infinite nodal DG/completed model, clock and theta
endpoint proofs, higher-operation/trace/filtration boundaries,20 checked Lean
components and one canonical3D monomial tool. Whole P4 remains in progress.
After this implementation slice rotate a run to ready P7-low-gcd to keep the
independent arithmetic lane active; do not wait for every broad source topic
to be completed first. Then resume P4 with the next precise source topic.

P7 arithmetic rotation (2026-11-03): a proposed absolute coprime pair-square
input is refuted for the unchanged sextic row family by the classical frame
bound on actual prime columns. Four weighted/unimodular finite Gram statements
are kernel checked and independently reviewed; the original signed estimate
is still open. Its next attempt must retain the exact truncated Möbius
convolution, total squarefreeness, all row zeros and conductors before Cauchy.
The prior high-gcd prose's cubic label is corrected to sextic (the cubic is
its square), without changing that derivation. Resume P4 linear relations
next, alternating with this explicit coefficient-sensitive P7 research lane.

## Latest explicit correction: actual RG and quantum TokenGT

Renormalization presentation must lead with a full effective action, constants,
partition/observable comparisons and scale maps. Compression and covariance
benchmarks retain their own evidence category. The actual clean K2,m dessin
physical graph, infinite gentle quiver and completed-order carrier are distinct.
Every architecture needs a bbycroft-style original step-through tensor view
synchronized with actual dessin/quiver/order geometry and precise index maps.

The user additionally requires a quantum TokenGT version with tropical
attention, GraphCG-style learned concept steering, latent forest search,
measured analogical transfer/persistent homology and continuous embedding
GFlowNet training. Implemented finite quantum-classical versions retain exact
physical RG teachers, heldout/OOD and matched classical comparisons, explicit
MI random variables and GFN state measures, and separately executed idealQEC
feature-memory layers. No semantic/mirror/quantum-advantage theorem or complete
GFN law is inferred from training. QEC must refer to an actual recovery/noise
model; the one-face genus-two CSS [[10,4,1]] counterexample is retained.

The new book explains concrete Fukaya/HMS/tropical and materials/generative
interfaces with their actual missing hypotheses. See ACTUAL_RG_DESIGN.md,
research/actual-rg.md and independent review. New scalarFiniteRG components
are kernel checked; whole learned/physical/categorical formalization and both
completion gates remain open. Preserve original22record hashes, all source
manuscripts, checkpoints/environments and existing shared theme. Continue P4
and the coefficient-sensitive P7 arithmetic lane after this user correction.


P4 linear-relations slice (2026-11-03): original2053 lines1097–1307 now have
an explicit corrected branch-module/Fitting chapter, exact genus2/4 examples,
nonrigid-string counterexample, formal/polynomial band distinction, cyclic
transport determinant and one canonical relation lab. Eleven actual general
Lean statements supplement the prose categories. Whole-source expansion and
both completion gates stay open. Rotate next to the recorded signed Möbius
arithmetic attempt, preserving all masks and conductor uniformities.


P7 signed-split attempt (2026-11-03): the unchanged ideal Möbius family now
has an exact full-mask Vaughan/type-I/type-II construction. A proposed
all-cutoff separate-piece bound fails at U1 by a genuine principal/unit-row
lower bound; this is not a refutation of original signed MS or moving U.
Eight actual Nat Dirichlet components are checked; the remaining ideal,
Hecke and analytic interfaces remain explicit. Next P4 finite categorical
formalization can construct the actual genus-two nonsplit branch extension;
next P7 analytic lane is the type-I squarefree Euler ratio with all masks,
primitive/imprimitive conductors and uniform Mellin/residue contracts retained.


## Latest reference-fidelity and ConvexTok amendments (2026-11-03)

The user's follow-up requires substantially closer study of bbycroft.net/llm,
not merely generic block diagrams. Pin the primary llm-viz source revision,
inspect the live overview and self-attention walkthrough, and implement
original tensor-dimensional solids, parallel semantic lanes, overview/focus,
cell picking, supported numerical dependency expansions and guided navigation.
Keep actual model semantics and preserved checkpoint/reference categories.
A source-confirmed interaction is not claimed as a live observation when the
reference renderer crashes. The local implementation need not copy upstream
WebGL machinery or assets; describe projection and rendering differences.

The further requested paper is arXiv:2605.22821v1, Tokenisation via Convex
Relaxations. Review and pin the complete primary source; explain its coloured
segmentation graph, occurrence capacities, vocabulary budget, IP/LP distinction
and rounding. Provide executable small examples with exact rational primal/dual
certificates and exhaustive integer comparisons, including a fractional-gap
case and a permitted-word corpus from the actual higher-genus dessin algebra.
Add one canonical contextual interactive tool to the architecture chapter.
Keep string tokenisation separate from TokenGT graph token identities; a
compressed finite path corpus neither changes the infinite algebra nor proves
an arithmetic determinant or GRH. Do not infer downstream training improvements
from these small examples or fabricate quantum speedups.

## Learned functions, covers, generative physics and GPU extension (2026-11-04)

The user requests a substantial extension, preserved alongside every prior
requirement. Implement and distinguish: finite-width trained quantum and
hybrid models; explicitly normalized infinite-width/random-feature/NTK
limits with their hypotheses; real/complex embeddings versus finite-field
algebraic coefficients and non-Archimedean valuations; tropical attention
and its actual tropical/HMS boundaries. Keep arithmetic candidate discovery
separate from exact spectral/determinant verification and the independent
GRH comparison theorem.

Add explicit universal-cover examples: distinguish the free group F2 from
the field F_2, the four-regular Cayley tree from a theta graph's three-regular
universal cover, and their punctured/compact-surface category hypotheses.
Include finite-support string/path/geodesic examples with computed Hom,
Ext/Tor and deck-sum covering functors; do not assume every covering is
Hom-controlled, dense or an equivalence of derived categories.

Add concrete quantum matter/materials and molecular benchmark applications,
pants/Frobenius gluing and TQFT examples, carefully scoped CFT/string and
holographic proposals, anabelian reconstruction hypotheses, and quantum
nonlocal-game calculations with the current MIP*=RE/Connes-embedding status.
No elementary CHSH or finite circuit is a constructive solution to the
commuting-versus-tensor correlation separation or an arithmetic proof.

Research current primary repositories for AI/manual classical and quantum
chip design, including AlphaChip, placement/synthesis flows, superconducting
layout and bare-metal control. Pin source revisions and audit scope. Provide
several tropical/hybrid accelerator reference architectures and executable
bit/operation-level models; distinguish those from synthesized/routed/taped
out chips, physical resource estimates and hardware benchmarks.

Include quantum-channel diffusion and trained hybrid quantum-feature score
and flow-matching models, with actual physical target distributions,
normalization/positivity/equilibrium and sampling checks, matched baselines,
seeds/splits/checkpoints/costs, interactive paths and circuits. Separate CPTP
quantum evolution from classical stochastic samplers containing quantum
features. Relate learned renormalization to true marginal actions and
explicit coarse observables rather than using unrelated compression targets.

GPU deployment: the user explicitly requested RustDesk access to
iska-linux-vscode and transfer of the project. Preserve the Mac copy and
all existing Linux files. The saved host is reachable and has an RTX4090;
copy into a new GRH-from-Mac-20261104 directory with resumable transfer and
verification. Preserve copied macOS environments as archives, use separate
Linux environments, never overwrite existing tokengt/other environments.
Use existing CUDA-capable torch for initial simulations; an isolated
cuQuantum environment requires the specified dependency approval. Do not
claim cuQuantum execution before its actual backend checks pass.

Deliver this extension through evidence-based slices in the same existing
implementation/research loop; full implementation and GRH gates remain open.

## Additional complementary synthetic corpora (2026-11-04)

The user explicitly requests two ADDITIONAL complementary datasets, one for
HolonForge/Aster and one for Mora-3. Read the two remote projects only; do not
change, enroll sources, train models, interrupt jobs or modify their data/splits.
Work entirely in the GRH project. Implement simulated nontrivial diverse
physical/chemical response data, curation, exact/numerical tests and contextual
interactive examples. Design and limitations: planning/synthetic-training/DESIGN.md.

The user further requires private Hugging Face storage with proper dataset
cards and Parquet shards, and verified dataset links on the project page/book.
Authorized credential source is a protected copy of exactly HolonForge/keys.txt;
never display, commit or upload any credentials. Ignore secret paths and upload
only explicitly reviewed dataset files. No new production dependencies.

Leakage policy: similarity-connected whole groups before task projection,
parent/conformer/gauge/intervention linkage, structural/scaffold/fingerprint
and appropriate topological/geometric audits, thresholds and cross-split
nearest-neighbor reports. Do not call finite threshold checks a guarantee
against every leakage or overfitting mechanism. Preserve giant components;
do not force independence by breaking a known similarity group. Protein
RMSD/TM-score analogies do not turn small-molecule geometry into protein data.
Computed/synthetic labels retain their provenance; never relabel them as
observed to bypass a current model's admission rule. Source construction and
actual training admission remain separate gates.

### Large-source dataset acceptance amendment

The user requested at least10K rows per additional dataset and explicit labels
for planned-training-source examples versus newly computed/synthetic examples.
The defaults contain16,384 Aster and22,951 Mora static rows; dynamic frames
are not counted as independent systems. Origin columns apply to every config.
576 Aster anchors derive from48 existing MP20 train structures;74 Mora rows
derive from32 existing PubChem train identities, and192 from8 public PDB
source anchors. Existing-source presence is not a statement of prior optimizer
exposure; new simulation is not a claim of chemical novelty against all corpora.

Validate source stereochemistry/forces, preserve charged/isotopic/stereo graph
metadata and source atom order, keep validation diagnostics out of scientific
conditions, and audit all molecular anchors against frozen default heldouts.
Quarantine whole conflicting source parents without moving heldouts. Record
historical PDB1HRW actual HEADER and1LE0 replacement. Native synthetic-label
admission and global exposure evaluation remain future owning-model decisions.
Keep the private HF cards, Parquet configurations, exact remote hashes and
commit-pinned official-loader receipts linked from book and explorer.

### Latest visualization and chemistry amendment

The user requested visible peptide bonds, traditional alpha/3-10/beta cartoon
views, more informative orbital/current/coherence dynamics, further nontrivial
topological examples and deeper, better animated physical/chemical diffusion
and flow matching. Implementation/design: planning/synthetic-training/
VISUALIZATION_PLAN.md. Use source secondary annotations and actual connectivity;
never invent secondary structure or confuse a contact graph with chemical bonds.
Keep phase winding, Chern/winding, chemical torsion torus and dessin genus
distinct. Retain actual quantum-feature and classical chemistry checkpoints,
correct positive-noise references, matched controls, visible errors and smooth
source-preserving display animation. No new dependencies/active-model changes.

## 2026-11-04 accepted additions: coherent clouds, certificates and gluing

Keep the two complementary private HF releases frozen. Extend their companion
with deposited peptide bonds/ribbons, exact finite SSH/QWZ phase/current
benchmarks, coherent spatial density clouds, and trained periodic chemistry
flow/DSM models with correctly distinct endpoint laws. Preserve failed pilots
and the stalled game seed. The new learned-GRH lane must separate analytic
approximation, certified contour counts and zero-location obligations;
infinite-feature readout rates must retain initialization/source assumptions.
Add trained CHSH/tilted/magic-square examples, exact strategy/moment/SOS
checks and the external Connes/NPA boundary. Add pinned HoTT hubs-and-spokes
references, actual clean-dessin rotations, disk/punctured-disk and
spine/filled-surface-cover calculations. Homotopy gluing must not be equated
with a module-category/Hom-controlled/HMS or arithmetic determinant theorem.
No new Lean4 HIT or univalence axiom is permitted. Full analytic/topological
formalization and a validated oracle remain separate implementation work.

Publication amendment (4 November 2026): the latest explicit user request supersedes earlier private-research wording. The research repository, project page and both reviewed HF datasets are public. Preserve original private-release receipts as historical evidence; protect credentials and unrelated model repositories. Continue the existing implementation/research queue and local8765 preview.


### Remote validated-oracle/moment checkpoint (4 November 2026)

The specific q3/4/5 interval sample and readout subtask now has an independently
accepted finite certificate (final-v5), with no new Lean declarations. Preserve
the historical floating runs. Arbitrary-tolerance selection and actual analytic
Lean interfaces remain separate. A reviewed fixed-twist original-family AFM
proof improves the full-mask remainder; retain its D^(2delta)U^(2-4delta)
loss, principal/short/covariance obligations and independent arithmetic bridge.
The next arithmetic task is the full d-weighted moment before absolute sums.
The new concise/extended technical-note PDFs do not imply the preserved main
book and live HTML already include this content. Finish their integration with
the pinned remote build prerequisites; do not install/upgrade or overwrite
historical outputs to disguise missing formalization. Both completion gates
remain false and the existing research/implementation heartbeat remains active.

### Accepted remote integration and publishing exception (5 November 2026)

The user explicitly permits the existing Mac GitHub login for publishing only;
all project edits, clones, builds and numerical/browser/Lean checks remain on
iska-linux-vscode. No credentials may be read/copied/transferred or new login
performed. The reviewed weighted-cutoff results and233-page40-chapter book,
49/129-page focused articles and8/20-page notes are integrated. Maintain the
cutoff-uniform envelope's residual D^(1/2) loss and the conditional boundary
implication as separate from GRH. New analytic/categorical Lean, signed
covariance and the positive determinant bridge remain open. The unified hub
and four missing project pages are public; preserve pre-existing sites and
private active-model data. Resume from latest receipts, never rebuild a
completed audit as if it were a new proof. Both completion gates remain false.


## Signed covariance and two-cutoff frontier (5 November 2026)

New shared proofs are papers/signed-bilinear-{core,details}.tex in chapter40,
with executable examples/arithmetic_cutoff/signed_covariance.py and
research/signed-cutoff-covariance.md. In the window2D/7<=U²<=D, every actual
active coefficient is mu(m)(r_U(m)-1), where r_U is an even ordered-factor
count. Thus it is odd/nonzero. Elementary lattice/squarefree counting gives
an explicit positive lower constant for its normalized coefficient norm,
for each fixed nonzero smooth profile. This is not a row-energy lower bound.

A finite example in the ORIGINAL sextic family, with D=400,U=17,nu=1,
all72literal B7 rows and the complete four columns of norms439/475, has
Q(C,mu)=-27/25 despite nonnegative pointwise coefficient overlap and a
positive-definite real Gram. A genuine common nonnegative smooth profile
has exact integer-norm values10/1. A second guaranteed nonprincipal246-row
subset atH89 preserves raw zeros and gives-69/50; it is not the full
nonprincipal family. Independent direct F439/F19/F25 exponentiation
reproduced1272raw characters, full complex Gram matrices and all12amplitude
cases. These are exact finite sign counterexamples, not asymptotic BT_sigma
or GRH counterexamples. No lower bound for arithmetic row energy is inferred.

The high-window bilinear attempt retainsDX after legal factor Cauchy/BGL;
the older regrouped estimate is stronger. The exact two-variable Perron
factorization, normal correction domain, half-integer sharp cutoff and
finite-height error are proved. Safe reciprocal-L contours reproduce the
oldU^(2-4delta)energy cost, with M4(W)^2 and fixed margins retained. Moving
the contours requires actual reciprocal/zero-residue control; numerator
moments do not justify dropping those terms. The coordinate slice is a
meromorphic identity, including the stated numerator-zero caveat.

Independent proof and final-byte TeX acceptance is under
planning/signed-bilinear-20261105/{review-covariance,review-perron}; exact
reports are outputs/checks/2026-11-05-signed-bilinear/. The new book is
237pages/40chapters/6412nativeMathML, with13unique laboratories. Focused
articles51/133pages and paired notes9/24pages are synchronized. Three-pass
builds, source audits, XML/numbered-reference checks and320/390/768/1440px
browser checks pass. Paragraph headings now match the unnumbered PDF style.
Old source volumes, diagrams, data and environments are preserved. Earlier
overfull/undefined-proposition staging failures are retained; valid outputs
alone are promoted. Inherited amsmath/underfull and3old munder warnings stay
explicit. No new dependency, training/GPU job, Lean declaration or GRH proof.

Next: prove a QUANTITATIVE lower covariance budget or coupled arithmetic
fourth moment that permits the observed negative covariance, uniformly in
the original masks, conductors, cutoffs and common profile; cover neighboring
near-saturating blocks. Alternatively control the actual two-variable
reciprocal integrals and all crossed residues. Do not retry automatic
covariance positivity, coefficient shrinkage, marginal independence or a
pole-free contour shift as if these missing inputs had been established.
The best global envelope here still losesD^(1/2) atH=D^(3/4); short/principal
assembly, analytic/category Lean and the positive determinant bridge remain
open. Both completion gates remainfalse; the existing heartbeat stays active.

## Accepted extension: requested-error training and covariance budget (5 November2026)

P11 now includes a bounded requested-rational-tolerance readout API over the
preserved q3/q4/q5 samples, exact executed midpoint-objective GD and a
certified perturbation from ideal-root least squares. Strict-floor refusal
is required; do not describe this as arbitrary-precision theta sampling.
Final-v3 certificates and independent acceptance are under the dated
adaptive-readout experiment/check/review paths. A new source-backed replay
is readout.html, linked from the canonical analytic laboratory and book.

The arithmetic lane proves an actual-vector negative covariance budget,
cutoff-uniform high-window balanced-factor moments sum r<<D, sum r²<<DlogD,
exact normmod36/equal-level deletions and full saturation-face identities.
It leaves the old DX middle term and D^(1/2) relative loss. Next estimate
the unequal-product coupled fourth moment and mixed Mobius term with all
union masks and the full A3 saturation direction. A negative-part budget
alone does not supply BT_sigma. Both gates remainfalse; no new Lean/GRH.

## Adaptive sampler/family acceptance — 5 November 2026

A separate variable-precision theta sampler and adaptive family driver now
implement requested positive rational errors for fixed q = 3, 4, 5/domain and
compact. Do not apply the preserved fixed-label floor to this new API, nor
claim all-conductor/height or practical extreme-tolerance complexity.
Actual1e-24 degree 48 / 88-node examples and192eta1e-32 samples are source-bound
and independently accepted. Exact executed midpoint-objective states have
lossless shared-vector/scale compression; their true-root perturbation and
all sampling/alias/Taylor/rounding terms remain explicit. No new Lean.

Arbitrary four-column moments may have exponents ±2; original internally
coprime C-C factors have only 0, ±1. Primitive conductor collapse never
restores full-union zeros. The small-conductor attempted estimate is a
known high-gcd recovery, not new analytic progress; governing novelty
addendum/review supersede the preserved draft's optimistic language.
Next arithmetic target remains the signed large-conductor/common divisor 1
sum over conductors and dual frequencies with all masks and A3 neighborhood.
Both completion gates remain false; keep heartbeat active.

## Cube-factor and joint-dual refinement — 5 November 2026

The original r3³ pivot admits the already-classical GL quadratic family bound R0+D R0/A3 after exact raw-zero-preserving freezing and fixed finite S/ray partition. This is a refinement of the application, not a new large sieve. With the old powered bound it improves the A3-dominant sector; at H=D^(3/4), the full face has leading power min(5/4,1+2a), 0<=a<=1/4. All a>=1/8 remain at5/4; even a=0 costs D above the H target. Near-saturated middle monomials necessarily have A3<=M D^eta plus the old capacity/imbalance/high-power slack. This is not an actual row-energy lower bound.

The exact joint six-coordinate completion keeps mu(q), CRT generator phases, all common-prime Ramanujan factors and actual cutoff/factor-count coefficients. Its orientation Parseval and finite tail budget do not estimate the actual signed h,q,K weight; coherent fibers and fixed length-one factors prevent automatic cancellation. Preserve arbitrary overlapping r6, all literal units/S factors, common profile, ray/squarefree/capacity masks. Do not reuse a generic four-column conductor or claim a new global exponent/GRH/Lean result. The new standalone quadratic-pivot.html is linked to the proof without duplicating canonical embedded tools. Both gates remain false.

## Ordinary conductor refinement and finite arithmetic learning — 5 November 2026

This accepted frontier supersedes earlier descriptions of5/4 as the best
available global unsigned exponent. A classical ordinary all-primitive-character
comparison gives Lambda_A << (HD)^epsilon A6[D+(A1 A2 A3 A4 A5)^2],
with the arbitrary overlapping r6 retained as its actual coefficient mask.
Combining with the powered-family bound and exact capacity yields
H + D H^(1/6) + (DH)^(2/3) for the original residue-subtracted energy,
with fixed nu/S and one common possibly complex W. At H=D^(3/4), power7/6
improves5/4 by1/12 but still exceeds the target3/4 by5/12.
The whole old A1=A2=A,A3=B,AB=H^(1/3) face now costsD; it is no longer
the worst upper-bound face. New upper-envelope witnesses are
(log_D A1,log_D A2)=(5/12,1/6) and pure log_D A1=3/4.
They are not actual-energy lower bounds. The proof includes all-modulus
primitive Gauss completion, nonunit vanishing, reduced Eisenstein fractions,
a lattice large sieve, raw conductor/zero transfer and principal assembly.
It is a refined application of classical sieves, not a new classical sieve.
Independent exact-production proof receipt: outputs/checks/2026-11-05-arithmetic-learning/review-mixed/acceptance-v1.json.

A separate finite Fourier-feature learner targets all210 actual original
coupled correlation coordinates,95(h,q) blocks including65 h1 blocks.
D6000/U60/H625 and one stated common smooth four-bump profile activate all15
squarefree ideal columns; principal nu,2262 literal rows and a separately
labelled2148 guaranteed nonprincipal subset retain4530 raw column zeros.
Four tau1e-12 runs execute216 metric-gradient updates and200 budget-limited
ordinary updates, saving every exact rational state. Both signed observables
and the full-vector tolerance are certified; weighted spectral loss and
metric/ordinary gradient conventions are distinct. Exact labels are supplied
before training, so no speedup, unseen-conductor generalization or uniform
analytic saving is asserted. Immutable v2 manifest binds source/input/output.
Independent acceptance-v2 in outputs/checks/2026-11-05-arithmetic-learning/review-learning/
reconstructs31668 symbols/450 Gram targets/186552 histogram cells and every
saved update/certificate. The failed logging-only v1 remains preserved.

Next substantive arithmetic research must estimate the actual signed joint
conductor/dual-frequency weights before per-conductor absolute Cauchy,
including h1 and the new remaining upper-envelope neighborhoods, with all
coherent fibers, raw common-prime zeros, ray/squarefree/capacity restrictions,
fixed profiles and conductor uniformities. A finite learned Gamma certificate
is not this varying-family saving. Short/principal target assembly, independent
positive arithmetic determinant/zero-location comparisons and scope-specific
Dirichlet/Hecke/Dedekind/elliptic/Artin obligations remain open.
No new analytic/category Lean declaration, PSD or GRH proof is supplied.
Pinned Linux4.24 compiler approval remains pending; do not install/substitute
or repeat the completed inventory without an explicit reply/changed state.
Keep both completion gates false and the existing heartbeat ACTIVE.

Evidence and reproduction: research/mixed-conductor-and-learning.md;
shared papers/mixed-conductor-{core,details}.tex and
arithmetic-learning-{core,details}.tex; examples/arithmetic_learning/README.md.
Do not rerun accepted author/reviewer grids or frozen216/200 traces as new
research. Preserve all earlier sources/runs/releases and original HEAD/index.


## Moving-profile and coherent-mean boundary — 5 November 2026

For principal nu=1, fixed S above2,3 (or a fixed larger S), and U²=D,
the actual norm-radial A_U and literal epsilon=1+omega phase admit ONE
common complex smooth profile W_D with supnorm1. It varies with D, has
derivatives O_k(D^k), and vanishes at the annulus endpoints. On actual
nonprincipal rows epsilon*beta_v^6 the primitive conductor is432, with
power conductors432/27/16/27/432; every original S/v collision remains
deleted. The ideal v is arbitrary, including repeated/overlapping primes.
An elementary positive-density coprime-triple proof gives full original
E-energy >=(c_S+o(1))D H^(1/6), H=D^theta,0<theta<1. This uses outer
row-energy positivity and a SELECTED literal class's h1 A-A contribution;
it does not lower-bound the signed h1 sum over unselected rows.
At theta3/4 lower power9/8 is below the current upper7/6. No new unsigned
upper saving, fixed-W counterexample, positive determinant or GRH follows.
The DH^(1/6) term is necessary in the varying-profile supnorm class for
theta<2/3. A target uniform through M_k(W)^alpha for every epsilon would
need k*alpha>=1−5theta/6; this does not refute existing derivative costs.

The actual orientation projection exactly returns the coupled Gamma norm;
rank supplies no conductor saving. Coherent restriction has compression
3^(-omega(q))*11* and leakage lambda(1−lambda), so it cannot commute with
projection for free. An exact original D4000/U63/q-five-prime fixture has
four active orientations, Gamma=3 and variance0, but selected h1AA=3/1000.
Omitting the literal unit phase incorrectly gives−3/4000. This rules out a
variance-only centering rule without its mean term on nonprincipal rows.
The A6=1 mixed/pure upper-envelope sectors remain open.

Sources: papers/profile-uniformity-{core,details}.tex;
research/profile-uniformity-and-coherent-means.md; examples/profile_uniformity/.
Design review and exact joint note: planning/signed-profile-20261105/.
Independent implementation acceptance-v1 reconstructs all30482 norm groups,
1219280 raw-mask entries,40 distinct arbitrary ideals through norm64, and
14720 direct literal symbols across the six frozen scales. The governing
v2 manifest is a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460.
The fixed-X64 good-S family has19 rows; the separate capacity-matched small
caps2..4 contain only the good-S unit. Finite ratios do not prove the
asymptotic theorem. The new standalone profile-uniformity.html inspector
is a hash-bound exact-data view, not browser training. Preserve failed v1
manifests/builds, all earlier sources/outputs/releases and the fixed-profile
frontier. No new Lean declaration or compiler/dependency change occurred.

Next: bound actual signed h,q,K weights BEFORE per-conductor absolute Cauchy,
retaining coherent means, fixed common profiles, full union/common-prime
masks and conductor/ray/squarefree/capacity uniformities, especially h=1
and the A6=1 remaining neighborhoods. Short/principal target assembly,
independent positive determinant/zero-location and scope-specific GRH
obligations remain open. Pinned Linux4.24 approval remains pending; do not
install/substitute/reinventory without explicit reply or changed state.
Both completion gates remain false; keep this existing heartbeat ACTIVE.


## Signed coprime slice and exact character twist — 5 November 2026

The actual signed h=1 slice on the A6=1 two-pivot row blocks now has a
separate unconditional baseline. Gcd–Mobius inversion retains the actual
X(da), common complex W, nu, full common-prime raw zeros and every original
row/capacity/ray mask. Positive subsequence norms may be enlarged only
inside the exact divisor decomposition. With R=A1*A2, M=max(A1,A2),
|S1(X,Y)| << (HD)^epsilon ||W||infinity^2 min{
R+DR/M+D^(2/3)R/M^(1/3), D+R^2}, X,Y in {A_U,C_U,mu}.
The L=D/Nd in [1/2,1) endpoint is counted directly, not passed to a sieve
outside its domain. At H=D^(3/4), the remaining mixed and pure upper-bound
neighborhoods still cost D^(7/6). No new power saving follows: the sufficient
A-A signed divisor budget sum mu(d)Gd << D H still lacks 5/12 powers.
It is sufficient for this slice, not asserted necessary for all later signed
assembly. Principal/residue assembly and all other row sectors remain separate.

The actual Jacobi column gauge is mu(m)j(m)=Psi(m) on squarefree columns.
Psi is the normalized Eisenstein generator character of exact conductor
(2(1+2omega)), norm12, infinity type(1,0). Its unitary normalization is
infinite order, so the earlier finite-order moment input does not automatically
apply. The exact TWO-factor completion has central quadratic Gauss phase
and one orientation-dependent Jacobi phase; column gauging and changing the
additive generator preserve the matrix norm and do not estimate the kernel.
The central quadratic phase law is inherited, not a new theorem of this run.
A gauged Euler product has reciprocal L(s,Xi); no pole-free contour shift or
unproved reciprocal moment is used. Actual q-dependent Fourier/capacity
weights remain outside that auxiliary fixed-twist series.

A NEW fixed common smooth plateau W, independent of D, at D60000/U244,
H3833/A1=37/A2=7 gives exactly20 original nonprincipal rows after masks.
For TWO selected columns and their complete two-orientation q fiber,
Gamma=-3 +/- i*sqrt(3), selected h1AA=-1/10000. Centering gives zero pairing
but nonzero centered squared norm6 (average variance3); the omitted mean
has squared contribution36 against naive variance budget12. The complete
selected two-column Gram is positive with eigenvalues17 +/- sqrt(21);
its coprime off-diagonal slice is indefinite. This finite remaining-sector
control is not an asymptotic lower bound, whole-family covariance or GRH
counterexample. The inspector exposes all20 rows, actual zeros, phase gauge,
and all18 signed pairings. No browser training or new data inference occurs.

Sources: papers/signed-weights-{core,details}.tex and
research/signed-coprime-weights.md; independent phase/budget/Mellin/diagnostic/
canonical reviews under outputs/checks/2026-11-05-signed-weights/.
The new core/details are shared verbatim with chapter40 and all four focused
wrappers. All prior moving-profile, learning, fixed-family adaptive theta,
source distinctions and scope limitations remain valid. No new Lean theorem,
conductor-uniform theta construction, determinant bridge or zero-location
result is asserted. Pinned Linux4.24 approval remains unanswered; do not
install/substitute/reinventory or ask again absent an explicit reply/change.

Next: estimate the actual mean-retaining signed joint h,q,K weights or the
signed gcd divisor sum before absolute Cauchy, especially h1 and the mixed/
pure A6=1 neighborhoods. Preserve full union/common-prime zeros, coherent
fibers, conductor, literal-ray, squarefree/capacity and common-profile
uniformity. Do not rebrand this D^(7/6) baseline, the exact character gauge,
finite centering control or reciprocal Euler identity as the missing signed
saving. Short/principal assembly, independent positive determinant/zero
comparison and separate Dirichlet/Hecke/Dedekind/elliptic/Artin obligations
remain open. Both completion gates remain false; keep the existing heartbeat.


## Mean-retaining signed divisor lift and complete-column reference — 5 November 2026

The exact original coprime slice now has an arbitrary-coefficient divisor
incidence formulation: D Q1(x,y)=sum_d mu(d) Z_d(x,y), with
F_d(x;u)=sum_(d|m) x_m chi_m(u) and
Z_d=sum_u w_u F_d(x;u) conjugate(F_d(y;u)). The original coefficients
include nu and the ONE common complex profile. Keep full divisors d=m,
actual row zeros, common-prime deletions, literal/ray and capacity masks.
Residual a,b may overlap. There is no extra mu(q) in this identity.
The positive norm majorant B(m)=sum_(d|m) lambda_d gives an exact finite
coefficient-error certificate. Computed Frobenius lambda_d values are
weighted nonzero matrix-entry counts, not an analytic signed saving;
classical uniform lambda_d inputs are asserted only for original unweighted
rows. The absolute divisor triangle still discards the needed cancellation.

For fixed residuals a,b and row u, the ACTUAL signed d series has local
factor 1-q^(-s)(1-q^(-v1)-q^(-v2))(1-q^(-w1)-q^(-w2)). Its exact factorization
has NINE Dedekind zeta factors (four numerator, five denominator) times a
normally convergent correction, with explicit half-integer cutoff,
finite-height errors and successive Perron limits. An independent finite
cutoff expansion keeps all EIGHT nonzero short-divisor states and gives
Z_U(s)=N_U(s)/zeta_K^T(s), with N_U holomorphic for Re(s)>0. Its elementary
bound retains U^(4 max(1-sigma,0)+epsilon), hence the old U^(2-4eta) cost
on sigma=1/2+eta, 0<eta<1/2. Shared-profile Mellin inversion embeds the
actual finite coherent outer sum over a,b,u. Neither this identity nor the
normal correction bounds its reciprocal zeta factors or justifies discarding
crossed residues. An explicit overlapping-residual control detects the
nonzero short-state correction. No uncancelled pole of the complete coherent
sum, new power saving, determinant comparison or zero-location result follows.

A NEW exact full-column evaluator uses all annular squarefree IDEALS, not
rational-squarefree norms. The fixed study profile is chosen ONCE with
width delta=1/240000, support [1,2], value one at all strict integer nodes
for D<=60000 and zero at endpoints. It is distinct from the older broad
plateau; its large derivative cost O_k(delta^(-k)) is explicit and the CLI
refuses D>60000. Different declared row blocks at D=144,576,60000 have
41/164/16953 columns, 53/212/21750 divisor buckets and 5/11/20 actual
nonprincipal rows. These three finite cases are not an asymptotic growth fit.

The largest immutable run retains 339060 raw column-row values (47908 zeros),
73420 incidences and 1305000 complex channel states. All nine signed cross
components are retained. In (A_U,C_U,mu) order the exact matrix is
[[-30714,-11287,19427],[-11287,2644,13931],[19427,13931,-5496]]/30000.
The A-A even/odd divisor masses 543416 and 604844 give -5119/5000 after
normalization by D. Among its columns,1361 are squarefree ideals with a
nonsquarefree rational norm. Independent ideal/finite-field arithmetic
reconstructs every large raw value, F/Z state and gcd-poset class; the naive
5748084180 pair-row visits are an operation-count comparison, NOT an executed
runtime benchmark. Small cases also have independent direct pair checks.
All original v1 scientific sources/tables stay frozen. A separately reviewed
v2 helper corrects ONLY the N=U=1 edge; every accepted column has N>U and
its data/provenance remains v1. No accepted tables were rerun for that fix.

The distinct signed-divisor.html inspector hash-verifies lossless compressed
payloads for every case and exposes actual columns, ideal incidences,
row/channel shapes and values, signed divisor contributions and all nine
pairings. It replays exact data; no browser training occurs. The unique
source-bound workflow PDF/TeX/SVG shows the actual dimensions and masses.
PDF and native MathML share the canonical papers/signed-divisor core/details
with all four focused wrappers. The new narrow table scroll container fixes
measured320px overflow while preserving full table/math bytes and font sizes.

Governing records: planning/signed-divisor-20261105/root/DIVISOR_INCIDENCE_LIFT-v2.md,
analytic-attempt/SIGNED_D_SERIES-v3.md, papers/signed-divisor-{core,details}.tex;
outputs/checks/2026-11-05-signed-divisor/review-design/ and independent large
review under analytic/large-full-column-review-v1/. The exact full-column
run manifests, fixed sources, all failed candidates and old evidence remain
preserved. The new finite profile is not a bounded-seminorm asymptotic theorem,
a whole-family counterexample, learned generalization, quantum/upstream
training, full Lean formalization or GRH proof.

Next research: use the actual short-state expansion or a proof-preserving
U-smooth/rough split to estimate the MEAN-RETAINING signed d sum/coherent
h,q,K weights before absolute Cauchy. Any rough-prime simplification must
first prove its support, endpoint and common-prime constraints; it has NOT
been established here. The current unsigned envelope remains
H+D H^(1/6)+(DH)^(2/3), with power7/6 at H=D^(3/4), still5/12 above target.
Keep coherent orientation means, all full-union/raw-zero masks and
conductor/profile/ray/squarefree/capacity uniformities. Short/principal
assembly, independent positive arithmetic determinant/zero-location
comparisons and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin
obligations remain open. Pinned Linux4.24 compiler approval is unanswered;
no installation, substitution, repeated inventory or repeated question.
Actual analytic/category Lean and both completion gates remain unfinished.
Keep the ONE existing heartbeat ACTIVE; no guaranteed proof schedule.


Final signed-divisor promotion: outputs/checks/2026-11-05-signed-divisor/promotion-v1/promotion-v1.json binds the accepted bookPDFv1/nativev3 and four article/notev1 builds. Current delivered edition279pages/40chapters/8176MathML, preserving ALL7891 prior literal math subtrees in order,385oldtables/13canonical iframes/28oldSVG refs. One new source-matched workflow SVG/PDF/TeX gives29totalSVGrefs. Focused64/175pages; notes23/66pages. Independent source/proof/data/UI/build preservation reviews and finalnative-qa-v3 pass. The failed narrow-table320px candidate and measured local-scroll probe are preserved; finaltable/math bytes and fonts remain unchanged. Root visually inspected workflow and new PDF proof pages. Three inherited malformed munder nodes and old amsmath/hyperref/underfull diagnostics remain disclosed; no new malformednode,overfullbox,unresolvedreference or Lean declaration. This is not a new signed exponent, determinant or zero-location bridge. Publication is separately gated. Protected sourceHEAD/index and all previous worktrees/evidence remain unchanged.


## Explicit rough-prime mask budget — 5 November 2026

A NEW quantitative A-A result replaces the rough-prime deletion by a defined
auxiliary kernel with an explicit correction. Work over the Eisenstein
ideals, with finite fixed S containing primes above2,3, original unitary nu,
ONE common complex W supported in[1,2], full original good squarefree annular
columns, and actual finite NONZERO literal rows1<=Nu<=H with weights w>=0.
Keep all internal row squarefree/coprime/unit/ray/capacity/sixth-factor masks.
The required window is U>=1,U²<=D,2D<=7U². It is not an all-cutoff theorem
or a theorem for arbitrary selected-column subsets/extra column filters.

Write d=f*e for the common IDEAL divisor, with f U-smooth/e U-rough; f is
NOT the original column-pair gcd h. Actual A_U(ez)=A_U(z), with NO mu(e)
inside A_U. Nonunit residual pair max(Na,Nb)>=7 permits at most one rough
prime; the unit pair a=b1 permits two DISTINCT rough prime IDEALS and
forces f1. The exact nonnegative C2 correction includes conjugate primes
of equal rational norm. It is not a lower bound for the whole signed slice.

Let K0 be the smooth-f signed completed norm, KT the original rough-prime
completed norm with full(p,abuS)=1, and KS its explicitly AUXILIARY S-only
rough-prime extension. All outer mu(f) signs, smooth masks and original
raw chi_a(u) zeros remain. With Rw=sum w, B=||W||infinity and kappa_U(u)
the number of distinct good rough prime ideals dividing u,

  D*S1AA = K0-KT+C2,
  Delta=(KS-KT)/D,
  |Delta| <= B²[229376 sum_u w_u kappa_U(u)+2048 Rw],
  0<=C2/D<=1792 B²Rw,
  S1AA=(K0-KS)/D+E,
  |E|<=B²[229376 sum_u w_u kappa_U(u)+3840 Rw].

If H<=D^(3/4), kappa_U(u)<=1 at EVERY scale, so
|E|<=233216 B²Rw<=2^18 B²Rw. For actual unweighted two-pivot rows with
bounded literal multiplicities, Rw<<A1*A2<=H; the correction is O(B²H),
without a divisor-power or profile-derivative factor. This bounds ONLY
the accounted correction, not the remaining signed main (K0-KS)/D.
The existing7/6 global envelope and missing5/12 saving are unchanged.
Principal/residue assembly and other coefficient channels remain separate.

The proof retains the exact disjoint row/residual prime union. Residual
prime deletion forces f1,a=p (and/or b=p) on support and gives exactly
2Re(T_1(P;u) conjugate(z_p(u)))-|z_p(u)|²; the last intersection term is
indispensable. The row term retains all raw zeros before any error triangle.
A support identity gives A_U(g)=mu(g)(2*1_(Ng<=U)-1) when good SF Ng<=7U,
including the unit. Active rough T terms have N(fa)<7U and therefore
|A_U(fa)|=1 exactly. This is not unrestricted multiplicativity, a proxy or
a shrinkage claim for the whole original annulus. Elementary ideal counting
and sum_f(Nf)^(-2)<=64 give the explicit constants; no prime theorem is
needed for the mask result. Both scaled comparisons are WEAK at B=0/Rw=0;
prior strict-product source/acceptance remains historical with a correction
addendum, never silently rewritten.

A separately reviewed coherent Stieltjes substitution retains Gf(t) as the
actual weighted row norm and mu(f) OUTSIDE, with exact lower boundary
-Gf(U)(pi_K^S(U)-Li(U)). Only the fixed-S prime measure is approximated;
growing deleted masks are already accounted by the correction. The analytic
Li/PIT subsection requires U>=7. Its operator variation budget retains
M1(W)^2 and a TRUE weighted norm input; the classical specialization is
ONLY the accepted unweighted/bounded-natural-multiplicity A6=1 two-pivot
family. At H=D^(3/4), U~sqrt(D), its inherited positive-operator majorant
has worst power5/6 times delta_S(U), not a new saving. The pinned fixed-field
Thorner--Zaman2019 Theorem1.1 supplies a subpower prime error after a fixed
threshold, retaining/absorbing any fixed exceptional zero. That upper budget
does not certify the3/4 target; actual signed errors may cancel and K0-J is
still unestimated. No actual-error lower bound, growing-conductor PIT,
pole-free contour shift, Artin holomorphy, positive determinant or GRH follows.
The DOI/publisher URL/cache hashes are in PUBLIC-CITATION-v1.json; full
publisher PDF/text/HTML caches remain local and excluded from publication.

Fresh deterministic controls use D200/U10/H53 with52columns5rows,
D512/U16/H107 with139columns7rows and D900/U30/H384 with250columns2rows.
The last is a declared noncritical capacity, NOT floor(D^(3/4)); its row
rough correction is exactly zero. A new fixed smooth W_delta,delta1/4096,
has exact flat strict norm nodes only on the stated integerD<=1024 scope
and explicit large derivative constants. It is not the previous profile.
All raw original/auxiliary masks, inert and conjugate primes, unit residual
states and non-squarefree auxiliary p² terms are retained. Raw
(K0,KS,KT,Erow,Eres,C2,D*S1AA) are respectively
(339,235,209,20,6,21,151),(366,781,711,48,22,89,-256),
(436,410,366,0,44,28,98). Normalized Delta values13/100,35/256,11/225
and actual-clean errors47/200,159/512,2/25 each divide by D ONCE.
These finite signs do not make Erow/Eres universally nonnegative.

Independent arithmetic reconstructs complete ideal universes/SF subsets,
3561 literal phase values (including auxiliary residual universes),3353
COMPLEX Fd transfers,199smooth/3154rough grid states INCLUDING exact-zero
placeholders,5119terms/39auxiliary nonSF terms and273767 ordered original
column-pair-row checks. All2510 active-profile reduced coefficients satisfy
the exact coupled short identity. A captured norm247=13*19 example rejects
its unrestricted use outside Ng<=7U. No old table/trajectory/evaluator was
rerun; fresh arithmetic/phase controls do not prove the analytic constants.
The compact exact summary web/data/rough-mask-controls.json SHA7596718f is
a projection of these immutable new inputs, with no browser training.

Governing canonical proposals f6de9534/a7d91548 match shared
papers/rough-mask-{core,details}.tex and book fragments. Independent gate
outputs/checks/2026-11-05-rough-mask/review/canonical-acceptance-v1.json
SHA89fa5333 binds analyticv5, zero/domain addendum, independent data/projection,
root PIT review and primary citation. Source/builds and all earlier failed
reviewer schema assumptions are preserved. Both originals, source clones,
all prior environments/outputs/cache/history and unrelated progress remain
untouched. No new Lean declaration, dependency, authentication or GPU work.
Pinned Linux4.24 compiler approval remains unanswered; do not install,
substitute, reinventory or repeat the question.

Next: estimate the ACTUAL clean mean-retaining signed main (K0-KS)/D, or the
coherent K0-J and signed prime-error cancellation, using the exact coupled
cutoff/Mobius coefficients and original row masks/conductors. Do not recast
this explicit correction bound, elementary unit-sector count or inherited
5/6 operator budget as the missing5/12 saving. Short/principal assembly,
independent positive arithmetic determinant/zero-location bridges and the
separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remain
open. Actual analytic/category Lean and both completion gates remain false.
Keep the ONE existing heartbeat ACTIVE; no guaranteed proof schedule.


Final rough-mask promotion: outputs/checks/2026-11-05-rough-mask/promotion-v1/promotion-v1.json binds bookPDF/nativev1 and four focused/notev1 builds. Current edition288pages/40chapters/8552MathML; ALL8176previous literal math subtrees remain ordered/byte-identical, all386previous tables retained in388,13canonical iframes and29SVGrefs/assets unchanged. Focused67/183pages; notes25/74pages. Source-bound detailed proof, independent new ideal/phase/data checks, nativeQA at all widths and rootPDFvisual review pass; no new malformednode/overfull/unresolvedref/Lean declaration. Three inherited munder nodes and old amsmath/hyperref/underfull diagnostics remain disclosed. Exact zero/domain/full-column qualifiers supersede historical weaker/strict-scaled drafts without rewriting them. The explicit mask error has target size; the signed clean main, global5/12 saving, principal/determinant/zero-location bridges and full Lean remain open. Original sourceHEAD/index, all earlier releases/environments/cache/history and Macpreview remain preserved. Publication is a separate concrete gate.


## Physical-radicand sieve and coherent main — 5 November 2026

This substantive frontier supersedes older current7/6/global5/12 and
pure5/6-positive-certificate descriptions; their mathematical history stays.
NEW external input: Alexandre de Faveri, Optimal large sieve for fixed order
characters, arXiv2610.04045v1,2October2026, Theorem1.1. This is a pinned
submitted preprint theorem being invoked, NOT a new proof of that sieve,
a priority claim or complete Lean verification. PrimaryPDF SHA256:
97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726.
Full primary reading caches remain LOCAL; public metadata pins the version.

The exact application uses K=Q(omega), containing mu6; mu12 is not needed
for Theorem1.1. Unique ideal generators alpha=1mod3 remove unit ambiguity
in the source's allowed fixed Section2.3 construction. BOTH indices are
sixth-power-free ideals. Physical radicand norm, valuations1..5, lower
character orders and all raw common-prime/union/ray/SF/capacity masks remain.
There is NO radical relabeling or arbitrary-family reciprocity premise.
Freeze arbitrary possibly nonsquarefree/overlapping r6 with its ACTUAL
coefficient collision mask. For original raw and residue-subtracted sums,

 Phi(H,D)=H+D H^(1/6)+H^(5/6)D^(1/3)+H^(1/3)D^(5/6),

 times B²(HD)^epsilon for fixed nu/S and ONE common complex W, B=supnorm.
The r6 sums use powers-6,-5,-2; the Dterm counts H^(1/6) ideals. All global
S-factor exponents are positive; principal residues/cutofflogs are retained.
For1<=H<=D every term is <=D H^(1/6). Critical9/8 improves previous7/6 by
1/24, still3/8 above target3/4. For fixed0<theta<1 and H=D^theta, the accepted moving-W_D obstruction matches
this unsigned SUPNORM-CLASS power ONLY when W may vary with D. It does not
prove fixed-W sharpness or refute suitable explicit-seminorm bounds/GRH.

For original UNWEIGHTED A6=1 two-pivot h1 rows, the exact gcd-Mobius
subsequence norms retain A_U(dn), every raw zero and direct subunit counts:

 |S1AA| << B²(HD)^epsilon [H+D+H^(5/6)D^(1/3)+H^(1/3)D^(5/6)].

Critical13/12 improves former7/6 by1/12, still1/3 above target. The Dterm's
S-factor exponentzero uses a finite polylog count, NOT a convergent sum.
Under inherited high-window/capacity hypotheses,
 |(K0-Kall)/D|<=|S1AA|+236800 B² actualrowmass.
This retains the combined mean; neither separate main is estimated at
target scale. Arbitrary positive weights require a TRUE weighted norm.

Previously reviewed research-only reductions are now integrated with full
proofs. KS=Kall+P2 has ORDERED(p,q),p=qallowed and onlyq's rowmask;
P2/D<=3584 B²rowmass differs from unordered DISTINCT C2/both masks.
Old233216 remains for the old main;236800 belongs to the new main.
Endpoint-exact two-jump Mertens summation keeps both closed-prefix terms,
fullT including common primes, and196608 M1²rowmass D/(UZ)m_(14DH)(Z).
Zcuts residual lengthX, NOT smoothf. Hypothetical scalar powers are not
proved; boundedX has unitf and marginal cancellation cannot bound the full
coherent outer sum. Euler deletion includes ALL supported prime powers;
only fixed-field subpower transfer follows, with fixed exceptional-zero
qualifications. The old sufficient smooth-f tail bound remains valid as a
coarse inherited localization, not current optimality or signed saving.

The joint Stieltjes operator keeps -E_S(U)Q(U), orientation means/equalnorm
fibres/rawzeros/fullsignedmatrix. Rough-prime positive compression is NOT
invariant and supplies no full energy lower bound. Radial Mellin Parseval
keeps equalnorm correlations. The current short positive input is the MINIMUM
with older valid bounds on1<=L<=D, directunitcount on1/2<=L<1. Pure budget
improves5/6 to19/24; mixed7/9 remains smaller. These are sufficient positive
MAJORANTS, not actual-error lower bounds. Keep the minimum INSIDE the
variation integral and the pointwise lowerendpoint.

CONDITIONAL diagnostic only: an all-scale/all-epsilon squarefunction
d2(T)<<T^(-alpha+epsilon) would imply zeta_K zero-free STRICTLY right of
max(1-alpha,1/2) by Mellin discrepancy continuation and primepowers.
Scalar inputs sufficient for pure/mixed majorants would be U^(-1/12),
U^(-1/18), yielding conditional strips11/12,17/18. NONE of these inputs or
strips is proved or asserted necessary for the actual signed target.

Canonical shared sources: papers/coherent-main-{core,details}.tex and
papers/physical-sieve-{core,details}.tex, exact book counterparts. Two
independent application reviews and one joint source-bound canonical review
keep the deep theorem external. The EXISTING quadratic-pivot inspector
shows currentglobal9/8/A6=1slice13/12, historical curves, suppressed unknown
constants/epsilon losses. The entire former cube face remains better
controlled at power1 by the old ordinary comparison. Displayed numbers are
bound expressions, not measured norms/energies/training/GRH.

Next: improve ACTUAL mean-retaining combinedK0-Kall or coherentK0-J PLUS
signedprimeerror/endpoint BEFORE per-f/per-conductor independent absolute
Cauchy, retaining exact generalA_U (NOTroughshortlemma onK0), fixedcommonW/
explicitseminorms, fullunion/commonprime/ray/SF/capacity masks, means/equalnorm
fibres and neighboring mixed/pure blocks. No target cancellation follows
from this new positive norm application. Short/principal target assembly,
independent positive determinant/zero-location bridges and separate
Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remainOPEN. No
Artinholomorphy/GRH/desiredpositivity/zeros premise or new analytic/category
Lean. Linux4.24 permission stillUNANSWERED: no install/download/substitute/
reinventory/repeatedquestion. BothgatesFALSE; ONE heartbeatACTIVE. Preserve
sourceHEAD/index, all releaseworktrees/indices/originals/data/outputs/caches/
environments/history/Macworkspace/old8765preview/privateactive-modeldata.


Final physical-sieve promotion: outputs/checks/2026-11-05-physical-sieve/promotion-v1/promotion-v1.json binds valid bookPDF/nativev3, focused concisev1/extendedv2 and notes concisev1/extendedv2, plus inspected inspectorv3. Edition303pages/40chapters/9172MathML, focused71/200pages, notes29/89. ALL8552previous literal math subtrees remain ordered/byte-identical, all388oldtables remain in389,13canonical iframes/29SVGrefs/assets unchanged. Current external-preprint-based unsigned envelope has critical9/8 and original unweighted A6=1two-pivot signed comparison13/12; target3/4 is still open. Globalgap3/8/scopedsignedgap1/3 supersede former5/12. Newshortpositivecertificate19/24pure and min7/9mixed have only CONDITIONAL scalarinput/strictstrip diagnostics; no input or newzero-free strip is proved. Fixed0<theta<1 moving-profile supnorm sharpness is not fixed-W sharpness. Every original mask/commonprofile/mean/endpoint and arbitraryweightednorm qualification remains.

All6source-bound PDF/native builds, independent mathematical/application/integration reviews, focused exponent/model controls and UI/native desktop/mobile/night/keyboard/source/PDF/visual checks pass. No new malformedMathML/overfull/unresolvedreference/Lean declaration. Three inherited munder nodes and old amsmath/hyperref/underfull diagnostics remain; source-matched cachedPDF searchability/publicSVG limits unchanged. Failed hash-line/native-spacing/earlycapture candidates and all old outputs remain preserved. Both completiongatesFALSE; target signedassembly, independent determinant/zero-location and scope-specific GRH/analytic-categoryLean remainOPEN. Linux4.24approval stillunanswered; no newinstall/substitution/question. OriginalsourceHEAD/index, all releaseworktrees/indices/environments/caches/history/Macpreview/privateactive-data protected. Publication is separately gated; keepONEheartbeatACTIVE.


## Verified physical-sieve public release and accepted postpublication component research — 5 November 2026

Authoritative Main5d49a3e99267d35c3613b196a10ee5f6d11ca090 / Pages504df4af84e587e7a0763d3fcc0faba0c61131a9 are LIVE. Read planning/physical-sieve-20261105/POST_RELEASE_HANDOFF.md and the physical-sieve PUBLIC_RELEASE_VERIFIED.json SHA6e695033a110e201bd311d748638cc313bd7465436b552b59d0313049689b5d6 before historical pending flags. All17hostedhashes/765treeentries and191strict LIVEgroups pass, no errors/timeouts/pending/filter relaxation;303pages/9172MathML, all8552oldmathsubtrees preserved. Physical-norm application of pinned deFaveri arXiv2610.04045v1 Theorem1.1 gives current global9/8, original UNWEIGHTED A6=1 TWO-pivot signed13/12; gaps3/8 and1/3 to target3/4 remain. External submitted-preprint dependency is explicit; no new sieve or Lean reproof. Fixed0<theta<1 moving-profile supnorm sharpness is not fixed-W/bounded-seminorm sharpness. All prior actual-mask/profile/mean/endpoint/weighted-norm safeguards remain.

Research CONTINUED AFTER publication, outside frozen153-file release/current book: exact pre-Cauchy primitive-Poisson DRAFT-v8 cba96d34 and required two-pivot scope addendum5f576c22 are accepted as an exact representation with FAILED nominal norm route (no saving). NEW DUAL_UNIT_K_LEMMA-v3 abeee901 proves actual finite good-dual-unit k-sum = its orientation/deletion-dependent Euler mean at exponent2 plus explicit cutoff/Bessel-moment errors; independent acceptance7318ee69, author8f0d410d. Natural finite cutoff, empty fibres, primitive root/full conductor, eta(k)^2, fullT and literal AU/nu/commonW/rawzeros are retained. Actual scope v3=v4=v5=v6=O/u0S-supported; adding good frozen factors requires their primal finite deletions/rescalings. All nonunit/S-supported dual modes and outer means remain. This component already has a row-count triangle bound: no whole-kernel nonvanishing/lowerbound/target-power gain is asserted.

Next genuine task is actual mean-retaining root/Euler-weighted outer kernel together with nonunit modes BEFORE absolute Cauchy. Finite good-dual-window recombination/Bessel-Stieltjes complement is a PROPOSED next route, not executed accepted work; bounded variation alone is not a summable absolute tail. Do not rerun completed exponents/tables/traces/failed norm route/build/publication/auth as new research. Integrate these postpublication notes only with a future substantive reviewed book/source milestone; no status-only republish. P7 claim f8a62714-2626-45cc-8ae3-3377b059d8da / final checkpoint 9ef5313e-4173-484f-bbbb-e132d80371a7 remains in_progress; earlier P9 remains in_progress. Checkpoint outputs/checks/2026-11-05-physical-sieve/root/checkpoint-postrelease-v1.json SHA256 595a47effafca53f38e664c108b3741029d403f0133eeae8098a46b703723f55. Both project_complete/research_complete remain FALSE; ONE existing heartbeat ACTIVE.

All12 HEAD/index states/11 release worktrees/sourceHEADdba/index0ef remain protected; source origin/main fetched5d49a3e without reset/auth/FETCH_HEAD. ExistingMacgh publishingONLY/allscienceLinux/old8765Macpreview untouched/no externalMCP or newdependency. Linux4.24 permission remains UNANSWERED: no install/download/substitution/reinventory/repeatedquestion. Short/principal targetassembly, independent determinant/zero-location and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations/actual analytic-categoryLean remain OPEN, no Artinholomorphy/GRH/desiredpositivity/zeros premise. No cleanup/reset/no-op/statuscommit or proof-schedule guarantee.


## Research-only dual-window checkpoint — 6 November 2026

NO NEW PUBLIC RELEASE: Main5d49a3e/Pages504df4af and303pages/9172MathML remain current. Read planning/dual-window-20261106/HANDOFF-v1.md SHA4a8415c2b6c8be9cacda1cb57b0cb8c6934034dc8b393234e73b554b365fdf60 and aggregate outputs/checks/2026-11-06-dual-window/RESEARCH_ACCEPTED-v1.json SHA9aea44feff625b4af056b703f4060f308093f7f6a4a4ee1b76e3154ad354761e. New independently reviewed actual good/S-complete window/model/error, Euler-Schur inverse/finite-mode hierarchy, and sharp-row all-dual summable tail retain all masks/means/primitive phases and actualAU/fixedcomplexW. NEW same-C/rho1 LOW MODEL joint bound is B²(DYA2)^eps A1A2Phi(Y,D): atcriticalY=D3/8 normalizedmodel13/16pure31/48mixed; with certifiederror, mixed REPRESENTATION-FIXED FINITE WINDOW reaches target3/4. This is not whole-kernel/energy/globalgain; currentwhole13/12 andglobal9/8 unchanged. C generalrootlawH_ROOT remains UNPROVED/conditional, inheritedsameclass gauge notnew. Root250fresh syntheticanalyticcontrols/9numericalconsistencyquads are not arithmeticdata/intervalproof; copiedvenv launch127 preserved, existingpurempmath usedreadonly withoutinstall/envchange.

Next estimate actual coherent intermediate Bessel-character partial sum plus otherclass/rho/S-supported modes BEFORE per-conductor/column absoluteCauchy. The finite-window/norm-only/operator/tail routes are DONE as scoped reductions: do not rerun as newresearch. Short/principal/fullsigned/determinant/zero-location/allGRHscopes/actualanalytic-categoryLean remainopen. P7 claim4604f0d9-5da1-42f3-be1d-dccf585c7e76 / checkpointbe368cd9-59f5-481b-bb97-3df9170d3d1d remainsin_progress; earlierP9 remainsin_progress. Checkpoint outputs/checks/2026-11-06-dual-window/root/checkpoint-v1.json SHA9412852f87682bd50722d7df3bf0d0110754b5cf9fc436c82905719613dbd2df. Governing aggregate outputs/checks/2026-11-06-dual-window/RESEARCH_ACCEPTED-v1.json SHA9aea44feff625b4af056b703f4060f308093f7f6a4a4ee1b76e3154ad354761e binds exact notes, authors, independent reviews, fresh controls and12 protectedstates. Bothproject_complete/research_completeFALSE; ONEexistingheartbeatACTIVE. All12 HEAD/indexstates/11releaseworktrees/sourceHEADdba/index0ef/origin5d49 andeveryoldsource/output/cache/environment/history/Macpreview/privateactive-data preserved. No new canonicalbook/UI/build/browser/auth/publication/externalMCP/dependency/globalconfig/Claudechange. Linux4.24approval STILL UNANSWERED: noinstall/download/substitute/reinventory/repeatedquestion. Integrate these notes onlywith FUTURE substantive reviewed milestone; no status-onlyrepublish/no-opcommit/cleanup/reset/proof-schedule guarantee.


Dual-window handoff precision: current planning/dual-window-20261106/HANDOFF-v2.md SHAdaa59cabbc6fb81ba3a120546a26699700b3123fa0b7a17de09a93acc64630cc supersedes preservedv1 only for the C conditional-root wording. Only FIXED normalization/infinity-type correction is in conditionalkappa; xi_m(f_ABrho), conjugatexi_n(f_ABrho),rho(m)rho(n) stay explicit COLUMN gauges, not absorbedconstants. H_ROOT remainsUNPROVED, all scientific bounds/checkpoint/gates unchanged; no controls rerun.

## Research-only intermediate-kernel checkpoint — 6 November 2026

NO NEW PUBLIC RELEASE: Main5d49a3e/Pages504df4af and303pages/9172MathML remain current. Read planning/intermediate-kernel-20261106/HANDOFF-v1.md SHAbb9463e074d822f68cc652ad20d255052536fd7c651febe6fb9a6d9bd2133e74 and aggregate outputs/checks/2026-11-06-intermediate-kernel/RESEARCH_ACCEPTED-v1.json SHA5470159d31d46bf5ce42fc52fcae4dc4013dc662b054f115f27fcc937ff62d63. This supersedes older current-H_ROOT/next-task wording only; every prior instruction, correction and historical version is preserved.

NEW independent Gaussian/CRT derivation closes the project H_ROOT normalization gate for the stated actual primitive conductors and unitary angular/radial types (two independent analytic reviews); it is a convention-complete standard Hecke-law derivation, not a new sieve/GRH theorem. Distinct root column gauges, primitive sigma(e/h) zeros and good-z row phases remain explicit. After separately reviewed unequal-class bilinear transport, the FULL fixed-u0 original unweighted TWO-PIVOT exact finite-K prefix satisfies |P_<=X|/D << B²(DXA2)^eps (A1A2/D)Phi(X,D) for EVERY FINITE X>=1. No Taylor-I/oldX<=sqrtH restriction, no infinite-prefix limit. ALL class/rho/nonunit/S-supported modes INSIDE the prefix are retained, with actualAU/commoncomplexW/nu/fullunion/commonprime/ray/SF/capacity masks and uncentered/equalnorm ideal fibres. u0 remains fixed unit/S-supported with no good support; extra factors/varyingu0 are separate obligations. AtcriticalH=D3/4 the mixedX~D prefix reaches target3/4, pureX=D has upper11/12. Root's separate critical-half dyadic/log² bound remains SAME-class/rho1. Whole signed13/12 and global9/8 are unchanged.

Exactly152 NEW saved consistency assertion entries (58+13+81, labels need not be unique) at65digits include14 Gaussian FE and15 Mellin cases. These are synthetic analytic fixtures, NOT interval enclosures/original arithmetic-family data or proof by numerics; analytic reviews provide the proof gates. Existing purempmath used read-only on Linuxsystempython; no install/env change or old controls/tables/traces rerun.

NEXT estimate the ACTUAL signed coherent annular Bessel-character sum in pure positive-power or mixed BEYOND normD, retaining joint root/deletion/Mobius/mean phases BEFORE positive-d/per-conductor triangles. Completed finite-prefix/root/Mellin/all-j/norm-only routes are done as scoped reductions. Infinite complement, varying-u0/extrafactor/short/principal target assembly, independent arithmetic determinant/zero-location bridges and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes remainOPEN; no Artinholomorphy/GRH/desiredpositivity/zeros premise. No analytic/categoryLean completion. Linux4.24 approval STILL UNANSWERED: noinstall/download/substitute/reinventory/repeatedquestion.

P7claim4e8abce7-b063-4631-b265-3224a9195b6a/checkpoint77968dd4-97bd-4108-b279-c81931e1e1b5 remainsin_progress; priorP9 remainsin_progress; bothcompletiongatesFALSE, ONEexistingheartbeatACTIVE. All12 HEAD/indexstates/11releaseworktrees/sourceHEADdba/index0ef/origin5d49/everyoriginal/output/cache/environment/history/Macworkspace/old8765preview/privateactive-data preserved. No canonical paper/book/UI/build/browser/auth/publication/newdependency/externalMCP/globalconfig/Claudechange. These notes enter the book only with a FUTURE substantive reviewed milestone; no status-only commit/republish/cleanup/reset/proof-schedule guarantee.

## Research-only coherent-band checkpoint — 6 November 2026

NO NEW PUBLIC RELEASE: Main5d49a3e/Pages504df4af and303pages/9172MathML remain current. Governing planning/coherent-band-20261106/HANDOFF-v1.md SHA90a6be03a2518def4243e63c00e587da6837bad04c86dd6fe9f71597cfaa5a82; aggregate outputs/checks/2026-11-06-coherent-band/RESEARCH_ACCEPTED-v1.json SHA34b4f9a51315cafd237a63b13ef4ac5d72b9ceef500d83be573d39dace991ae7. Prior H_ROOT/prefix work remains accepted input. All earlier instructions/corrections/versions stay preserved; only current claim/next-task descriptions advance.

NEW independently reviewed finite-cutoff AU(da) Schur transfer keeps exact half-integer endpoints and finite-height operator error; original common complex W costs its explicit Mellin seminorm. It repairs the invalid fixed-vector shortcut for a row-dependent coefficient, not AU multiplicativity/shrinkage. A's actual cubic d-by-residual-column transposition gives a NORMALIZED SAME-C/rho1 IDENTITY-d-source-class auxiliary divisor-band bound with inner min{Phi6(Y,D/E),(Y/E)Theta3(E,D/E)}, Theta3(E,L)=E+L+(EL)^(2/3), fixed0<sigma<1/2 and exact finiteK/S/ray/capacity masks. External pinned n3 primary-family application, no genericconductor replacement. Transfer constants are squared. This is a scoped norm improvement for auxiliary d bands, not original pair-gcdh, a new high-gcd solution, mu(d) cancellation or full signed saving.

NEW original equal-NORM COPRIME OFF-DIAGONAL columns are conjugate split-only rational-squarefree orientations. Their FULL PRIMAL sector is already O(B²RwD^eps), Rw<<R<=H, with all means retained. For each FIXED W the scoped full h1 target therefore reduces to UNEQUAL norms up to this elementary target-size term. Exact Dirichlet norm-pullback/orientation product is not automatically zero/positive. Paired original good masks handle S not conjugation-stable without enlarging it. EQ primitive-ideal prefix O(B²eps RY/D) and exact whole-minus-prefix signed complement give pureY~D/mixedY~D^(7/6) target-size EQ only; arbitrary high windows and UNEQUAL-norm bands remain open.

NEW pure literal-ray CRT/Poisson reorganization retains the complete coupled band before d/conductor triangles. Its S-local mean beta=gamma_c zeta survives unitprojection when Nm=Nn mod36, basicc6 coefficient1/2. OTHER literal residue channels remain; no global normmod36 deletion or zero-root-mean inference. Literal additive bands are not identified with older primitive-ideal finite bands. All original AU/nu/commonW/rawzeros/fullunion/commonprime/ray/SF/capacity/conductor phases, means and equal-norm ideal distinctions remain. Whole signed13/12/global9/8 unchanged.

Root1511 NEW saved consistency assertion entries55digits on three14x29 actual-good-ideal AUXILIARY cubic matrices (1218states/786maskzeros/42inert-factorstates), D121/289/529,U11/17/23, pass; NOT interval enclosures, complete original physical-family data, training or proof by numerics. B separately proves36 exact local Fourier inversions/Parseval108/unit projections in O/(6), not q-character or asymptotic data. All old tables/controls remain untouched. Existing purempmath used read-only/Linuxsystempython; no install/env change. Independent analytic gates and exact corrections are source-bound.

NEXT estimate ACTUAL SIGNED UNEQUAL-norm coherent intermediate moments with all small-d/source classes, surviving Smean AND other residues retained BEFORE positive d/conductor/z triangles. Do not rerun finished sparse-sector/Schur/cubicnorm/finite-ray routes as the missing signed estimate. Short/principal/varyingu0/extra-factor assembly, independent positive determinant/zero-location and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes remainOPEN; no Artinholomorphy/GRH/desiredpositivity/zeros premise. No analytic/categoryLean. Linux4.24 approval STILL UNANSWERED: noinstall/download/substitute/reinventory/repeatedquestion.

P7claim9da9b383-04f2-491d-910a-6b85d3ae98a1/checkpointc56436af-59e4-4ee8-b55f-24836d39834c remainsin_progress; priorP9 too; bothgatesFALSE, ONEexistingheartbeatACTIVE. All12HEAD/indexstates/11releaseworktrees/sourceHEADdba/index0ef/origin5d49/alloriginals/outputs/caches/environments/history/Macworkspace/old8765/privateactive-data preserved. No canonical paper/book implementation, UI/artifact/build/browser/auth/publication/newdependency/externalMCP/globalconfig/Claude change. Notes enter the book only with a FUTURE substantive reviewed milestone; no cleanup/reset/status-onlycommit/republish/proof-schedule guarantee.


## 6 November 2026 — coherent-band local milestone

Accepted implementation correction: append the reviewed cbk core/details within chapter40; retain all9172old literalMathML/389tables/13oldiframes/29SVGrefs. New working edition319pages/9810MathML has14canonical iframes/30SVGrefs and one original readable2+1 workflow. Use operative source-map-v3, mathematical gate9d1d9567 and source/artifact gates under outputs/checks/2026-11-06-coherent-book; v1/v2 source drafts and every failed guard/layout are historical, preserved. Five source-bound PDFs passed; only the book was rebuilt forfigurev4, four unchanged articlePDFs reused. Inspector55-digit values are saved numericalconsistency, not intervals/physicalfamily/training. Keep the full signed target open: originalunweightedA6=1two-pivot h1 upper13/12/globalunsigned9/8 are unchanged; unequalnorm/positive determinant/Lean/GRH obligations stay open; oneACTIVEheartbeat and all12protectedstates/11releaseworktrees remain. Public Main5d49/Pages504d/303page edition is unchanged; use the fresh releaseplan for a future substantive verified release, not a status-only commit.


## Reviewed coherent-book release edition — 6 November 2026

The reviewed release edition contains a 319-page book with 40 chapters and 9,810 native MathML formulas, focused articles of 76/215 pages and analytic notes of 34/105 pages. All 9,172 previous literal math subtrees, 389 tables, 13 earlier canonical inspectors and 29 SVG references are preserved; totals are 14 inspectors and 30 SVG references. The readable original workflow and complete matrix inspector retain all 1,218 saved auxiliary positions, actual ideal generators/factors, complex numerical values and raw zeros. Saved55-digit values are numerical consistency, not interval certificates, trained models or complete original-family data.

The shared coherent-band sources give primitive root normalization, exact finite Poisson/BV-prefix comparisons, actual-cutoff/profile Schur transfer, the restricted identity-divisor cubic comparison, full primal equal-norm localization and the literal-ray mean. Separate UB01 research is Main-only evidence outside the book and browser data. The original unweighted A6=1 two-pivot signed h1 bound13/12 and global unsigned9/8 remain unchanged. Full signed unequal-norm cancellation, short/principal assembly, independent positive arithmetic determinant/zero-location bridges, analytic/category Lean and GRH remain open.

This section describes verified CONTENT prepared for substantive publication; it does not certify that deployment has completed. A new release requires its exact frozen selection, source/credential/visibility/integrity gates, strict project-prefix browser checks and postpublication hosted hashes/trees. The final PUBLIC_RELEASE_VERIFIED receipt and post-release handoff will govern actual deployed commits. Earlier303-page/local-only statements above are dated historical preparation snapshots. Both completion gates remain false and the one existing heartbeat remains active. Original sources, all old HEAD/index states/worktrees, outputs/caches/environments, Mac workspace/old8765 and private active data remain protected. No Linux4.24 install/substitution/repeated question is authorized.


## VERIFIED LIVE coherent-book release and research-only continuation — 6 November 2026

Main87f89878f470ab98b84055fe72f28766d89202c6 and Pagesf6773684b6ea4d5ee067409c62c88c80d1529080 are VERIFIED LIVE. The authoritative receipt is /home/iska/Documents/LaTeX-projects/GRH-publication-20261106-coherent-book/outputs/publication/20261106-coherent-book/release-preparation-v1/PUBLIC_RELEASE_VERIFIED.json (SHA d85801388a02748e4a1607f288aa3bb974bcd8cb674b4e010ca52cf8e5e959ed). The delivered edition has319pages/40chapters/9810MathML,389tables/14canonical labs/30SVGrefs; all9172old literal math subtrees,389old tables,13old labs and29old refs remain. Five PDFs are319/76/215/34/105pages. All25changed hosted hashes,854selected Git-tree entries/modes/sizes/parents/refs,1247links and854payload roundtrips pass. Strict stage and LIVE220groups each retain ALL191predecessors; the inspector passes58checks/54layouts/1218strings/3654cells. LIVE591timing entries=579protocol entries+12navigation markers,1initial+11departures,13idle checkpoints, zero fetch/new-page errors/timeouts/pending, unchanged750ms-quiet/30s-idle guards. Five live PNGs are byte-identical to their staged renders. Three inherited munder nodes remain; no new malformed node or Lean declaration.

The original preflight directory-index resolution failure and hosted-verifier API trailing-slash404 are preserved. Their narrow reviewed producer fixes changed NO product bytes or browser filter; no republishing occurred. Source HEADdba37ff/index0ef1af remain, origin/main anonymously fetched87f89878, all13HEAD/index states and12release worktrees preserved, including the new225-file indexaca074d8. All edits/builds/checks/durable artifacts ran on Linux; existing Macgh was used only for in-memory publication. Macworkspace/old8765, originals/caches/environments/histories/private active data and all other project sites remain protected.

Research continued after publication OUTSIDE this frozen release, current book, Pages and Main selection. The accepted actual finite primitive sixth-part mean retains every AU/commonW/phase/root/r/k/ell/e/h/rawzero/capacity factor and full q deletion. A self-contained classical fixed-ray disk count t^(1/3), applied cosetwise before complex weighting, sharpens ONLY the same mean's normalized error to B^2(DXA2)^epsilon RXV^(-17/3)(1+sqrt(A1X/D^2)); top-band error is RX^(1/18). Pure critical37/48 still exceeds target3/4; mixed29/48 is only an error certificate. The retained principal coherent mean is unestimated. Governing research-only aggregate outputs/checks/2026-11-06-coupled-sixth/RESEARCH_ACCEPTED-v2.json SHA3be411e2f432bf47a9dd1a8cb8e6eed92d6d1e3f9f666abe8210e9e5ed50ff71 binds independent reviews. No lattice-discrepancy priority, whole signed saving, learning, interval, quantum, Lean or GRH result is claimed.

NEXT: estimate the ACTUAL principal coherent mean jointly with nontrivial sixth parts and r/k/root/column orientations plus every other class/rho/S mode, before conductorwise/positive-d triangles. Retain full means/equalnorm fibres/commonprime/fullunion/actualAU/fixedW/explicitseminorms and all conductor/ray/SF/capacity uniformities. The present lattice-count route is DONE, not the next rerun. Whole two-pivot13/12 and global9/8 are unchanged; short/principal assembly, independent positive arithmetic determinant/zero-location bridges and the separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes remain OPEN. No Artin holomorphy/GRH/desired positivity/zeros is assumed. Analytic/category Lean remains unfinished. Linux4.24 permission is still unanswered: no install/download/substitution/reinventory/repeated question. Both completion gates remain FALSE, P4/P7/P9 in_progress, and ONE existing heartbeat remains ACTIVE. Integrate research-only notes with a future substantive reviewed source/book milestone; no status-only republish or proof schedule.


## Principal-mean research-only checkpoint — 6 November 2026

NO NEW PUBLIC RELEASE or canonical book/UI/PDF/data change. Main87f89878f470ab98b84055fe72f28766d89202c6 / Pagesf6773684b6ea4d5ee067409c62c88c80d1529080 remain the verified319page/9810MathML edition. New independently reviewed notes and failed-step corrections are OUTSIDE that frozen release/book/Main selection. Governing aggregate outputs/checks/2026-11-06-principal-mean/RESEARCH_ACCEPTED-v2.json SHAbbe4a216c1d513ba988479920f222305f3d15c4dbff2317c2f0432a20981eaa1.

The actual retained mean has an exact finite weighted-Mobius a-band compensation, with a/b overlaps, original root/k/column/ray/capacity and all S values retained. In the top band X/V^6=64<7^6, only a=1 occurs and a finitew<=64 root/column moment remains. The cumulative density multiplier kappa_T/[(6z-1)zeta_K^T(6z)] has removable value1 atz1/6, not0. A finite s-band factor is entire; an isolated analytically continued zero and unweighted finite-ray orthogonality do not delete the actual root/conductor-weighted mean.

The exact incomplete1/6 Bessel moment gives the actual coherent difference F_V-E_V with ORIGINAL finiteK/fullT/eta² and every endpoint. The signed-k endpoint error from completeHQ5/3 is at most24 C0^(-1/2)M0 A^(1/6)(b-V), with A=A1*Nh*Nr/(Nl*Ne*F), DISTINCT from A1. Under explicit nonzeroG/largeK/low-argument conditions, endpoint correction has a component lower bound; this is NEVER a lower bound for M, a row form or energy. LaneA's power-free deletion T=S union supp(mn) differs from LaneB's k deletion T=S union supp(mn*v2). Conductor drops restore no deleted prime. Omitting endpoints/analytically completing the finite kernel is the failed cancellation step.

The proposed mean norm corollary is valid, but its claimed10/9 actual-sector advance was RETRACTED before acceptance/publication: accepted UB01 fixed-s comparison already implies the SAME actual-band bound (R/D)V F6(X/V6,D), through mixedX~D^(3/2) atV=.5D^(1/6). Thus10/9 is only a weaker separate-mean/error certificate, not a new range. The density g(d)^2 dampening is compensated by residualg(a)g(b); no signed-d saving. Unequal virtuald support Nd<2D/13 is a constant cutoff only. A bounded-residual virtualprime-d block already has absolute budget R V Z/D (Z=X/V6), puretop exponent-3/16; fixed-family PIT there is not the missing low-d estimate. Its separate phase/PIT diagnostic remains author-only/unaccepted. Originalpair gcdh, virtuald, sixth-free a and originalk are distinct.

Two new stdlib Fraction checks guard the formal budget and its inherited dominance; they are not original-family numerical data, intervals, proof of cancellation, or old control reruns. Failedv1 comparisons/notes and every before byte are preserved. No new exponent, whole signed estimate, determinant/zero-location, learning, quantum, Lean or GRH result. Whole originaltwo-pivot13/12/global9/8 remain unchanged.

NEXT GENUINE task: estimate the actual finitew<=64 root/column/k moment, or the actual F_V-E_V jointly, with all source/rho/S modes, originalAU/onefixedcommonW/explicitseminorms/fullunion/rawzeros/equalnorm/orientationmeans/conductor/ray/SF/capacity data BEFORE positive-d/conductor triangles. Low virtuald has growing residual/conductor data; bounded-residual fixed-conductor PIT cannot substitute. Do not rerun the finished lattice, density-damping, freeEuler/fractional completion or inherited norm-recovery routes. Integrate these research-only notes only with a future substantive reviewed source/book milestone; no status-only republish.

The short/principal assembly and independent positive arithmetic determinant/zero-location bridges remain open separately for Dirichlet/Hecke/Dedekind/elliptic/generalArtin; no Artinholomorphy/GRH/desiredpositivity/zeros assumed. Analytic/categoryLean unfinished; Linux4.24 approval remains unanswered, no install/download/substitution/reinventory/repeated question. Both completion gates FALSE; P7 in_progress; P4/P9 unchanged, ONE existing heartbeat ACTIVE. SourceolderHEAD/index, all13states/12releaseworktrees/frozen225index, originalsources/datasets/outputs/caches/environments/histories/Macworkspace/old8765/privateactive data remain protected. All work LinuxSSH; no auth/publication/externalMCP/Claude configuration change.


## Root-moment arithmetic-tail research checkpoint — 6 November2026

Research-only, OUTSIDE the frozen319-page/9810MathML public book. Main87f89878/Pagesf6773684 and all canonical PDFs/nativeMathML/UI/data remain unchanged. Governing new aggregate outputs/checks/2026-11-06-root-moment/RESEARCH_ACCEPTED-v1.json SHAd95f711210cb1f078076861ab23d34158efda5c12f8ee9aac57551f78cfa6fd9; full derivations/gates and current frontier are in planning/root-moment-20261106/HANDOFF-v1.md.

New independently reviewed arithmetic: for the ORIGINAL unweighted PURE two-pivot top principal mean, the actual Gauss-weighted large-short-divisor difference satisfies |G_D[A_U,A_U]-G_D[A_Y,A_Y]| << B M(W)D^epsilon(Y^-1/2+D^-1/6),1<=Y<=U<=sqrtD. The external pinned physical cubic theorem atn3 is an explicit INPUT. Exact mu*A_U ternary grouping retains residualmu(c); cubic Gauss CRT exposes the ACTUAL a-by-z cubic residue matrix and T_U(z)+T_Y(z), independent of a. All class/rho/primitiveS/root/rawzero/originalcoprime/optionalunequal/capacity masks survive, including varying other-column deletions. Fixed complex commonW costs explicit Mellin seminorm M(W); no supnorm-only varying-profile assertion, coefficient norm shrinkage, generic conductor substitution or new deep sieve is claimed.

The same signed bound keeps the ORIGINAL finiteQ2/K/fullT. At A1~H=D3/4,X=D3/8,Y=min(U,D1/8), actual retained M/D reduces to finite L0[A_Y,A_Y] up to target-sized error: Besselpower-1/16 and large-short-divisor powers3/4,31/48. The residual has a,b<=Y and c>=D/Y²>=D3/4. That SMALL-short-divisor Gauss moment remains UNESTIMATED. The separate P_top-M_top upper certificate37/48 remains above3/4; it is not an actual lower bound. Whole signed13/12/global unsigned9/8, short/principal/full assembly and determinant/zero-location remain OPEN.

Matched-endpoint finite models have a real-axis factorial remainder with no exponential I-majorant; the infinite hierarchy is inherited. The failed smooth-inner/absolute-short-divisor and automatic-Schur routes are recorded precisely, not claimed as target savings. Historical drafts/corrections and3 NEW exact Fraction consistency guards are preserved; guards are not interval proofs or original-family data. No old finite table, numerical/browser/build/auth/publication audit was rerun.

NEXT: estimate the ACTUAL finite-k long residual-Mobius cubic-Gauss small-short-divisor bilinear moment, or jointly its discrete-s discrepancy, BEFORE losing the original coefficient/mean/root/k/w/other-column/fullunion/source/rho/S/ray/SF/conductor/profile/capacity coupling. This is not fixed-conductor smooth PIT or completed-frequency orthogonality. Keep all earlier accepted safeguards; do not rerun the nowfinished model/norm/large-tail proof as the missing full target. Integrate these notes only with a future substantive reviewed book/source milestone.

No analytic/categoryLean or GRH conclusion. Dirichlet/Hecke/Dedekind/elliptic/generalArtin bridge obligations remain separate; no Artinholomorphy/desiredpositivity/zero assumption. Linux4.24approval remains unanswered: no install/download/substitute/reinventory/repeated question. Both completion gates FALSE, P7 in_progress, P4/P9 unchanged, ONE existing heartbeat ACTIVE. SourceHEADdba/index0ef,13HEAD/indexstates/12releaseworktrees/frozen225index, every original/data/output/cache/environment/history/Macworkspace/old8765/privateactive datum remain protected; no canonical/publication/dependency/auth/config/externalMCP change.


## 6 November 2026 — reviewed local Gauss-tail book milestone

The Linux working book is333pages/40chapters/10299nativeMathML; all9810previous literal math subtrees are ordered and byte-identical. All389tables/14canonical iframes/30oldSVG references and85non-HTML book assets remain unchanged. One original short-divisor partition/cubic-matrix diagram raises SVG references to31. Focused articles are81/228pages; analytic notes39/118pages. Sources papers/gauss-tail-{core,details}.tex and matching generated book copies retain85shared labels plus the book-only figure label, with full proofs and exact PDF-aux numbering.

The prior accepted actual pure Gauss-weighted large-short-divisor tail is now fully cited/explained in the book: the two disjoint cutoff boxes give TU+TY before the physical cubic matrix norm. The only deep input is the previously pinned external deFaveri2610.04045v1 Theorem1.1/Example2.2 n3; no new sieve or reproof is claimed. The original finiteK, all primitive roots/S values/source/ray/class/rawzero/full-union/common-complexW data and explicit Mellin seminorm remain.

NEW independently accepted direct reduction retains the ACTUAL discrete sixth-part s and EVERY original rho: P_X[AU,AU] reduces to its original-finiteK small-AY j0 model. It does not introduce the separate principal-density/counting-mean split. At A1~H=D3/4,X=D3/8,Y=min(U,D1/8), errors have powers-1/16,3/4,31/48 (the coefficient tail is exactly0 ifY=U). There is NO k/s or w/s coprimality mask; overlapping frequencies and all w<64/nonunit S modes remain. The old separate37/48 counting-error certificate is neither improved nor set tozero; its effects stay in the exact-discrete small model. That model is still unestimated at target size. The full signed13/12 and global unsigned9/8 are unchanged.

Separate RESEARCH-ONLY work OUTSIDE these book fragments uses the exact J5 finite ideal HB identity and the same physical cubic norm on balanced residual blocks. The linear TypeII column costs M(W)D^epsilon D^(1/3)Y^(1/3); the stated pure principal leading component has critical power11/16. This is a scoped signed-component estimate, not an energy lower bound or a full target theorem. Exhaustive one-long-unrestricted-factor classification explicitly assumesD>=2^64. BOTH-TypeI, including long prime residuals, remains open. See planning/gauss-book-20261106/lane-a/BALANCED_RESIDUAL_HEATH_BROWN_CUBIC-v2.md and independently reviewed research aggregate outputs/checks/2026-11-06-gauss-book/RESEARCH_ACCEPTED-v1.json.

Focused checks: all5source-bound final PDFs pass; current book and detailed editions are buildsv3, unchanged concise editions are source-bound v2 reuse. Final nativev3 adds489MathML with zero new malformed nodes/rawTeX/conversion warnings. Independent mathematical/source/artifact reviews and representative five-PDF/native visuals pass. The SAME focused browser harness passes40checks at desktop1440/mobile320, both palettes and keyboard horizontal scrolling; all86labels/63equations/65references and source/PDF/figure hashes pass. It records105global protocol events+1initial marker, zero actual parent departures, fetch/HTTP/newpageerrors/pending/timeouts0, with750msquiet/30sidle guards. This is focused local QA, not a rerun of the220group public release audit. Three inherited munder warnings and oldamsmath/hyperref/underfull diagnostics remain, with no new overfull/unresolved reference or Lean declaration. Source-matched cached PDF searchability and public-SVG reproduction limits remain disclosed.

Fresh synthetic formal algebra checks cover2304 coefficient equalities/847 target coefficients and2184 dyadic scale boxes, with exact integer powers, distinct equal-norm formal ideals and seed2026110609. A deliberately incorrect J4/same-fifth-root truncation fails at norm544825 (true+1,wrong-23,remainder+24). These support the new HB algebra/grouping; they are not actual character/Gauss/family data, interval arithmetic or Lean. No old scientific tables/traces/control suites were rerun. Every failed source guard, overfull/Pandoc candidate and night palette diagnostic is preserved. The night filter was readable but altered the new source palette; only the new diagram now keeps that palette on a white canvas, with old theme/assets unchanged.

This is LOCAL promotion only. No new public release: Main87f89878f470ab98b84055fe72f28766d89202c6/Pagesf6773684b6ea4d5ee067409c62c88c80d1529080 and the hosted319page/9810MathML edition remain current. Existing Macworkspace/old8765 preview and all13HEAD/indexstates/12releaseworktrees are preserved. No dependency/toolchain installation, authentication, token access/transfer, external MCP activation, Claude/global config or Git/index/publication action occurred.

NEXT implementation: prepare a separately reviewed substantive release from this milestone with all5PDF exports and the exact new source-only research closure; do not publish a status-only update. NEXT arithmetic: bound the actual residual long TypeI Gauss moment or the full exact-discrete small-AY kernel before losing r/k/w/s/root/column coupling. Retain fixedW/explicit seminorms, exactAU, allclass/rho/nonunitS/full-union/commonprime/rawzero/ray/SF/conductor/capacity hypotheses, and return to neighboring pure/mixed blocks and signed full assembly separately. Do not rebrand the finished balanced block, cutoff tail, scalar-count, density, free-Euler or norm routes as the full target.

P4/P7/priorP9 and both completion gates remain unfinished; one existing heartbeat stays ACTIVE. Independent positive arithmetic determinant/zero-location comparisons remain separate for Dirichlet/Hecke/Dedekind/elliptic/generalArtin; no Artinholomorphy/GRH/desiredpositivity/zero assumption. Actual analytic/categoryLean is unfinished. Linux4.24approval remains unanswered: no install/download/substitute/reinventory/repeated question.


## Reviewed Gauss-tail release edition — 6 November 2026

The reviewed release content is333pages/40chapters/10299nativeMathML, with all9810prior literal formulas,389tables,14canonical labs and30priorSVG references preserved; the new original partition/cubic-matrix diagram gives31SVGrefs. Shared papers/gauss-tail-{core,details}.tex and the five approved PDF exports (333/81/228/39/118pages) are reused exactly from the local milestone, not rebuilt as a new experiment. Read the [Gauss-tail chapter](https://amelie-iska.github.io/GRH-research/book/main.html#gtl:core), [book PDF](https://amelie-iska.github.io/GRH-research/book.pdf), [concise article](https://amelie-iska.github.io/GRH-research/concise.pdf), [extended article](https://amelie-iska.github.io/GRH-research/extended.pdf), [concise analytic notes](https://amelie-iska.github.io/GRH-research/validated-oracle-concise.pdf) and [extended analytic notes](https://amelie-iska.github.io/GRH-research/validated-oracle-extended.pdf).

The actual Gauss-weighted large-short-divisor tail and the new all-rho exact-discrete finite-K top-prefix reduction retain original raw zeros, source/ray/S/conductor/capacity data, fixed common complexW and explicit Mellin seminorm. The remaining small-cutoff model, long TypeI terms and full signed estimate remain open; whole signed13/12/global unsigned9/8, determinant/zero-location, comprehensive Lean and GRH are unchanged. The separately reviewed HB balanced residual11/16 component is SOURCE-ONLY outside this book and is not a full model bound.

This describes reviewed release content; stage/live deployment is certified separately by the new publication receipt. Main87f89878/Pagesf6773684 and the public319page/9810MathML edition remain the last VERIFIED LIVE state until that receipt exists. Historical local/pending/older-edition notes are preserved snapshots. The one existing heartbeat remains active, both completion gates are false, all source/private/environment histories stay protected, and unanswered Linux4.24approval licenses no installation or repeated question.


## 6 November 2026 — verified public Gauss-tail edition and continued arithmetic

The final cumulative release is VERIFIED LIVE: Main1f346d1a825aa6eff1479197aef45d293a878902 / Pagesde2614bf439e1c6ab8af09f3242af5a163f16f79. The authoritative receipt is /home/iska/Documents/LaTeX-projects/GRH-publication-20261106-gauss-favicon/outputs/publication/20261106-gauss-favicon/release-preparation-v1/PUBLIC_RELEASE_VERIFIED.json, SHA2569c912f6e419734fa0fa5f315717204a7e44324bb8dd880a207fbfa13f866a965. This supersedes the preceding pending/last-319-page wording; those passages are retained historical snapshots.

The public book is333pages/40chapters/10299MathML. All9810prior literal mathematical subtrees remain ordered and byte-identical; all389tables/14labs/30oldSVGreferences survive, with one new relevant partition/cubic-matrix figure (31totalrefs). The five source-bound PDF exports are book333, concise81, extended228 and analytic notes39/118pages. Read the [Gauss-tail proof](https://amelie-iska.github.io/GRH-research/book/main.html#gtl:core), [book PDF](https://amelie-iska.github.io/GRH-research/book.pdf), [concise article](https://amelie-iska.github.io/GRH-research/concise.pdf), [extended article](https://amelie-iska.github.io/GRH-research/extended.pdf), [concise notes](https://amelie-iska.github.io/GRH-research/validated-oracle-concise.pdf) and [extended notes](https://amelie-iska.github.io/GRH-research/validated-oracle-extended.pdf). The original Mac loopback preview remains untouched.

The first substantive publication was Mainb6e1571219d92432454ffd1afac2c812a9f28b9e / Pages6b3565d4e76c46a07cad6b32ef4b21274e800493:249selected Main paths/884API payload checks and16changed hosted files. Strict LIVE then exposed13 account-root/favicon404 responses. The failure was preserved, not filtered. A real404-origin control reproduced it; a single651byte self-contained SVG-icon insertion in the shared public runtime removed the implicit request. A separate additive repair selected35Main paths and changed ONLY public-base.js on Pages; ALL634other final public files, including every PDF/source/math/data/figure, are byte-identical to the first333-page bundle. One staged repair attempt correctly stopped at an inherited hardcoded runtime hash; its replacement binds the SAME exact-SHA assertion to the newly frozen bundle. The staged origin now returns404 rather than204 for an undeclared favicon. Neither error filters nor HTTP/WS/idle assertions were relaxed.

Final635-file bundle inventory29d5d5eaafbb30ed2f3220887b44bc5da2bb598dad9c1eea8a154718f6dc451b,670repair payload roundtrips/refusal controls,670-file credential-pattern scan/zero matches, exact source pins, allunselected public leaves/modes/actual one-parent commits/refs and all17cumulative hosted hashes pass. The honest Pages chain is f6773684→6b3565d4→de2614bf, not an invented single17-file commit. The failed240second deployment check and all33pending rounds are preserved; actual runtime deployed12:27UTC, and final hosted17 checks passed at13:33UTC.

Strengthened STAGE and actual LIVE each pass220inherited groups+40Gauss-tail groups+58laboratory checks/54layouts, preserving1218saved string positions/3654rendered cells. Governing LIVE run outputs/checks/2026-11-06-gauss-release/qa/live-browser-20261106T133342216621Z: fullreceiptcf9ca5892b183830d9e3a4524e52be4692834f9b478e2ca0fddd102be0f96a0a, focused7688a0cb8ff132b582d00ec53fc99362ef1ff25158010938581d4a18fe0d030f. Its645global events include632protocol events+13navigation markers=1initial+12actualdepartures;15successful idle waits and minimum758ms quiet exceed unchanged750ms/30second guards. HTTP/page/fetch errors, timeouts, departure/final pending requests and favicon requests are zero. Owned tabs/contexts/sessions and stage listeners closed; pre-existing contexts and9335/8765 services preserved. Final independent deployed audit c4bd788a and scientific-scope addendum f4793cb6 pass.

Arithmetic work CONTINUED after publication, outside this frozen book and both release indexes. Governing outputs/checks/2026-11-06-gauss-release/research-aggregate-v1/RESEARCH_ACCEPTED-v1.json SHA77671eeeeb33fc060db945c7e5062e2a3423e8fdcf7e458422afff60691dae2d binds14current notes/reviews/controls:
- NEW actual pure finite-k cubic-band estimate retains the coupled two columns before a positive common-divisor triangle: A1*V times[J^-2+(DJ)^-1+D^-1/3 J^-4/3], with exact Bessel remainder Lambda/J and original finite cutoff. At critical J0=D^(1/32), the large-k sector is target-sized; this is a scoped external cubic-sieve application, not a new sieve or full signed saving.
- The exact TypeI deletion/frequency transfer shifts frequency to d*t and scale to T/Nd, preserving their product and all raw zeros. Its sharp-interval H(alpha,beta) criterion with alpha+beta<=7/8 is explicitly hypothetical, sufficient only and unavailable; additive common-lift completion failed to provide it.
- Governing localization-v2 c0befeb4 (v1prose corrected, no quantitative rerun) leaves actual Nk<=D^(1/32) BOTH-TypeI. The exact identity is mu(m)A_Y(m)=sum_(abc=m,Na,Nb<=Y)mu(c), SF/coprime with unit cases and NO extra-minusmu. T>=cD^(1/2), Nt<=CD^(17/32), T*Nt=D*Nk<=D^(33/32), full deletion NQ<=CD^(51/32), and opened frequency<2D^(33/32). Frequency gcd=k holds only on original support before auxiliary openings. These are a reduction/windows, not a bound for the remaining kernel.
- The new paired-long attempt99fe6c5a matches SAME pinned deFaveri2610.04045v1 Proposition8.1 exactly (squarefree q=k, unrestricted paired long outputs). Opposite Gauss CRT crosses cancel the proposed free long-long cubic interaction; physical cube-free height is LM*min(L,M), not radical LM. The legitimate paired certificate retains LM/J^(3/2), weaker than accepted J^-2 offunit. The actual unit/very-short-k Gauss-vector mean remains open. g0 mayzero and is never divided out.
Fresh825Fraction capacity/1024abstract support checks and13independent rational expressions are FORMAL only, not actual character/energy data or Lean. No finished scientific tables/training/traces were rerun. Full third-party primary caches and private pin locators remain outside public closure.

NEXT genuine arithmetic: estimate the actual mean-retaining unit/very-short-k BOTH-TypeI Gauss vector jointly with every rho/source/e/w/s/root/commonprime/full-union/rawzero/conductor/ray/SF/capacity constraint and ONE fixed common complexW/explicit seminorm, or its original signed discrete discrepancy BEFORE positive divisor/conductor/column triangles. Generic paired norms, the finished large-k/large-short/TypeII/scalar/density/free-Euler routes and finite controls are finished, not the next experiment. Whole signed13/12/global unsigned9/8, short/principal target assembly, independent positive determinant/zero-location bridges and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes remain OPEN; no assumed Artin holomorphy, desired positivity/zeros or GRH.

All15HEAD/index states/14release worktrees are protected, including sourceHEADdba37ffaa78c82ade1385f7ee56c907ab0c67d3a/index0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c, first333frozen249indexce6a9b71 and repairfrozen35index42e7a893. Existing Macgh was used ONLY for authorized publishing in memory; all source/science/build/browser/checks ran SSH-Linux. No credential read/copy/transfer, login, dependency/toolchain installation, external MCP activation or Claude/global configuration change occurred. Preserve every original/environment/cache/history/private model and old preview. Actual analytic/categoryLean remains unfinished; Linux4.24approval is still unanswered, so no install/download/substitution/reinventory/repeated question. P4/P7/priorP9 and both completion gates remain unfinished; the ONE existing heartbeat stays ACTIVE. These append-only local release/research receipts will enter a future substantive source/book milestone; do not create a status-only republish.

## Research-only unit/short-k Gauss checkpoint — 6 November 2026

No new release or canonical book/PDF/laboratory change. Main1f346d1a825aa6eff1479197aef45d293a878902 / Pagesde2614bf439e1c6ab8af09f3242af5a163f16f79 and the verified333-page/10299MathML edition remain current. Latest release authority is planning/gauss-release-20261106/POST_RELEASE_HANDOFF-v1.md and its bound PUBLIC_RELEASE_VERIFIED receipt. This note is outside that frozen edition; integrate only with a future substantive reviewed milestone.

New independently reviewed research aggregate: outputs/checks/2026-11-06-unit-gauss/RESEARCH_ACCEPTED-v1.json (SHAf878074ae8df66e9032875b93a281e4143699015cfa43a76d8968c759a1c2870); detailed handoff planning/unit-gauss-20261106/HANDOFF-v1.md.
- ACTUAL pure short-k BOTH-TypeI auxiliary common-LONG-divisor tail: M(W)^2 A1 V (D X A1)^epsilon I(cLambda)[D^(-1/2)+R0^(-2)+D^(-1/6)/R0], normalized once. AtR0=D^(1/32), critical powers5/16,3/4,59/96 fit the target. This opens every common divisor d, not just the greatest: residual a,b may overlap; no residual coprimality is added. d is not originalh, finitek or oldsmoothf. Exact finiteK/Bessel/commonW/raw/full-union/source/rho/Gamma/class/ray/SF/conductor/capacity data remain. Required finite-S joint-selector companion51f1c728 expands HxH exactly with fixed mass<=|H|sup|f|; its d phase is chi(d)psi(d), not a generally assumed thetaS square. Separate genuine rho(d)^2 and Gamma factors remain.
- The attempted full estimate FAILED at unit/small d, whose inherited normalized13/16 certificate still exceeds3/4 by1/16. No actual coherent mean is discarded. Optional equal-norm auxiliary subtraction is counted globally, not removed inside separated norms. The independent interval-Schur lemma costs2(1+ceil(log2 n)) for arbitrary row intervals; full equal-norm fibres remain.
- A separate source-BARE fixed nonzero-angular sharp-interval corollary gives11/12 unnormalized,5/12 normalized, from the pinned external September2026 repository preprint. It is NOT the actual finite-twisted family: exact Gactual(c)=chi_(3,c)(delta)Gsource(c), the full finite kappa and Q deletion remain unmatched. Deletion keeps productD*Nk but moves level; generous smooth margin .01-.49*kappa is negative at1/32. Cuspidal and prime-only noncubic results cannot fill these interfaces.

Fresh formal checks:625 common-Gauss/gauge Laurent identities,256 Mobius reconstructions,65 exact prefix/exponent controls; interval controls2144prefix/5524interval/14235row-set/256endpoint;25 source/interface checks including9Fractions, plus root's focused Perron exponent receipt. These are synthetic algebra/source/interface evidence, not actual character/energy data, old-table reruns or Lean. All source versions are pinned; full third-party primary bodies and private fetch/cache pin records stay excluded from public closure. Wording/source-status/divisor/unit/S-selector corrections and failed preliminary probes remain preserved.

NEXT genuine task: estimate the ACTUAL joint d<=D^(1/32), unit/very-short-k BOTH-TypeI Gauss mean/discrete discrepancy, retaining every finite/angular/source/rho/e/w/s/primitiveS phase, raw/commonprime/fullunion mask, fixed commonW/explicit seminorm, norm fibre and capacity/conductor/ray/SF uniformity BEFORE positive divisor/conductor/column triangles. The finished long-d/large-k/large-short/TypeII/generic-norm/scalar/density routes and formal controls are not new experiments. Whole signed13/12/global unsigned9/8, short/principal target assembly, independent positive determinant/zero-location and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remain OPEN; no assumed GRH/Artin holomorphy/desired positivity or zeros.

P7claim32a1ca5c-761b-4f5a-ab03-bf5fcd9928c5 remains in_progress; P4/P9 and both completion gates remain unfinished. All15HEAD/index states/14release worktrees, source0ef/index, frozen249ce6/frozen35patch42e, every original/output/cache/environment/history/private model and old Mac8765 preview are preserved. All scientific edits/checks ran via SSH-Linux; no publication, new dependency/infrastructure/GPU/auth/token/config/Claude/externalMCP/Lean action. Linux4.24approval remains unanswered: no install/download/substitution/reinventory/repeated question. Keep the ONE existing heartbeat ACTIVE; no status-only commit/republish or guaranteed proof schedule.

Administrative P7 checkpoint: daa7bb6d-231a-48c2-a286-c9c0eb14c47c; evidence and derivations above govern scientific acceptance.

## Research-only whole-prefix / fixed-twist checkpoint — 6 November 2026

No new public release or canonical scientific book/PDF/lab build. Main1f346d1a825aa6eff1479197aef45d293a878902 / Pagesde2614bf439e1c6ab8af09f3242af5a163f16f79 and the reviewed333-page/10299MathML edition remain current. Read planning/twisted-gauss-20261106/HANDOFF-v1.md and outputs/checks/2026-11-06-twisted-gauss/RESEARCH_ACCEPTED-v1.json SHA590866c2da718fb92e96b86e7e9dfbd4135b4dee1be5e6fb1161fe5f88c4f322 before older next-task text. These notes are outside the frozen book; integrate only with a future substantive reviewed source/book milestone.

NEW actual unweighted PURE BOTH-TypeI localization: group the ORIGINAL shorta,b together with ALL short HB factors into prefixp BEFORE a physicalp-v cubic norm. The signed own-prefix coefficient is divisor-bounded; no separateY count is paid. The large-whole-prefix contribution is <=B M(W)(DXA1)^epsilon A1 V[D^(-1/6)+Z^(-1/2)], retaining all actual root/source/rho/Gamma/primitiveS/raw/fullunion/commonprime/ray/SF/capacity constraints and one fixed complexW. AtZ=D^(1/8), powers31/48 and3/4 fit target, leaving BOTH Np,Nr<=D^(1/8). This is new relative to old balanced residual-c TypeII and the old a>Y tail, not a rerun or relabeling.

On this newly localized support, Nk,Nd<=D^(1/32), t=p*d*k and exact full deletion h|rad_good(r*s*w), with (h,t)=1 forced by raw cubic zeros. Thus Nh<<D^(3/16), N(th)<<D^(3/8), residual length>>D^(21/32), and (T/Nh)N(th)=D Nk. There is a uniform9/64 power margin below sqrt(D Nk). The old worst-prefix moved-level obstruction is REMOVED in THIS smaller sector. Fix opposite residualb BEFORE p-averaging: (p,b)=1 stays in a LEVEL coefficient, not a false(a,b)=1 mask. Required finiteS product expansion and all legal k/w/s overlaps remain. Conditional source-averaged H_tw would give35/48, but the actual full finite-twist H_tw is still unavailable.

NEW admitted SOURCE theorem: for primitive fixed arbitrary finite-order residuekappa moduloF COPRIME3, fixed nonzero angularell, and movingSF r coprime3F, the exact cube completion is L^(Fr)(3s-1/2,kappa^3Theta3ell), with all raw deleted primes kept. Same-CRT finite matrices give refined dual absolute normR^(1/2+epsilon); generic transform counting gives coarseR^(3/2). Completed-numerator convexity is proved before division byL ONLY where its argument has realpart>1. Sharp Perron/partial summation gives V1(W)(RT)^epsilon min(sqrtT,T^(1/4)R^(1/8)), or the coarse exponent3/8. V1=sup|W|+integral|Wprime|; fixedF/kappa/ell dependence is explicit, not all-conductor uniformity. Their localized ACTUAL powers39/64 or41/64 are CONDITIONAL on full actual source/ramified matching, not new unconditional whole/model bounds.

Exact normalization now reads vartheta(c)=Theta1(c)barChi3,c(2), and the actual inverse-different correction combines into sourcefrequency12t. This is NOT a goodSF level. A general3-ramified finite character has an exact coefficient projector using shifts h*lambda^(2-f), trace denominatorlambda^(f+1), l1mass<=3^(f/2), selecting v_lambda(mu)=-3. Its Weyl/cusp closure and quantitative dual absolute norm remain OPEN; fixed dimensionality or a zero-producing naivepsi(lambda4mu) insertion is not a proof. Originalnu is fixed FINITE ORDER, not assumed orderdividing6, so higher3-primary conductor is allowed. Fixedq0 overlap reductions do not dividekappa(t); conductor-drop h terms retain literal Nh^-1/2 orNh^-s and rescaled profiles, under the required normalization companion.

Fresh checks are bounded evidence:105 meaningful exact finite-matrix states in a144-dimensional cyclotomic integer basis;64new affine geometry vertices;319height/2871horizontal/259fallback Fractioncases;root14scope/budget checks+8vertices. These are synthetic algebra/parameter checks, not actual-family energy data, training, Lean or replays of accepted old fixtures. All major derivations have independent gates. Only pinned unconditional DR2109.07463v3 Section5 statements are used for the FE route; no GRH-conditional prime theorem. Full third-party bodies/private cache and failed Patterson-fetch receipts stay excluded from public closure; source metadata stays pinned.

NEXT genuine research: prove the exact ramified3/cusp Weyl matrix for the new projected theta vector, all actual unit/source/primitivee/w states and raw conductor-drop zeros, with an adequate moving-level dual absolute bound. Even coarseR^(3/2+epsilon) already suffices through conditional41/64; refinedR^1/2 is not necessary for this target. Alternatively estimate the original jointly masked mean before positive triangles. Do not repeat finished prefix/large-d/large-k/TypeII/scalar/norm/control routes as new work. Whole signed13/12/global unsigned9/8, short/principal/full-frequency assembly, independent positive determinant/zero-location and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remain OPEN; no assumed GRH/Artinholomorphy/desiredpositivity or zeros.

P7claim9d375667-ff87-48b0-8f5c-1e25d969e9fc / checkpoint1210e91f-8dc8-4cbf-b087-dd27f230d640 remain in_progress; P4/P9 and both completion gates remain unfinished. Preserve all15HEAD/indexstates/14releaseworktrees/source0ef/frozen249ce6/35patch42e/every original/output/cache/environment/history/private model/Macworkspace/old8765. All scientific/project writes and checks SSH-Linux. No canonical build, publication/commit/push, dependency/infrastructure/GPU/auth/token/config/Claude/externalMCP/Lean action. Linux4.24approval unanswered: no install/download/substitution/reinventory/repeated question. Keep the ONE existing heartbeat ACTIVE; no status-only republish or proof schedule guarantee.


## Accepted ramified-Gauss and original full-A_U prefix research —6 November2026

Research-only; public333page/10299MathML edition unchanged. Authoritative handoff planning/ramified-gauss-20261106/HANDOFF-v1.md SHA14afea77ece78dae8cd5e84fd66db3e077c5dbc15ad24700a781ec31ff99246a.

Aggregate outputs/checks/2026-11-06-ramified-gauss/RESEARCH_ACCEPTED-v1.json SHA f3f199171068235f9161c769eda1209d443d46dc3416e95a6b316f1cfc14c503 governs.

The previously missing arbitrary fixed finite-character ramified3 interface is constructed: exact rational-translate SL2/Kubota reduction into KNOWN27 theta cusps; explicit transformed constants; pure nonzero-angular Mellin FE with NC^(1-2s) including Jacobian; actual lambda^3mu primary selector; raw cube completion with no restored Euler prime; known-cusp coefficient norms and conservative R^(3/2+epsilon) moving dual cost. The inherited completed-convexity/sharp-interval argument now gives actual fixed-family H(3/4,3/8), including original higher3-primary nu, full raw zeros, both angular signs and unit/subunit fallback. No refined sqrtR claim. Ell0 residues at1/6 and5/6 are retained, not declared absent.

The actual family is a fixed residue family from original finite-order nu, source ray quotient, Gamma, primitiveS and fixed Kummer numerators. Jacobi rho=mu*vartheta is NOT finite: its ONE varying vartheta supplies angular+/-1; genuine common/prefix phases remain outside. No densityg or arbitrary growing-conductor coefficient function is inserted.

NEW root theorem: planning/ramified-gauss-20261106/root/FULL_AU_PURE_PREFIX-v3.md SHA668f71eb4036d93e7907c7bba36ab59c44001fefad9463c2910490a7a4b04d98, WITH REQUIRED coefficient/annulus precision1f52dac7, prefix-mask precisiondfb2b1e8 and formal-control-scope precisionbd816dfd. Independently accepted B gatef2258609 and C gate5e01ac18.

For the ORIGINAL unweighted PURE finite primitive-dual top piece P_X[A_U,A_U] of DIRECT-v2(2.1), D>=2^64,1<=U<=sqrtD,A1~D^(3/4),X=D^(3/8),V=.5D^(1/16),
 |P_X| <<_fixed,eps (DXA1)^eps A1V
 {B[M(W)+V1(W)]D^(-1/9)+B^2[A1X/D^2+D^(-1)]}.
The normalized leading power is101/144, below3/4 by7/144. The raw numerator D*P_X has one additionalD. Whole signed13/12/global unsigned9/8 remain unchanged.

Proof: open B_U=mu*A_U (NOT original C_U) only on actual Nm>U annulus, retain exact j1/units and all short-factor endpoints. Classify ALL at-most11 original/HB factors together from fixed scales before any a,b triangle. Balanced boxes cost columnD^(1/3). A nonbalanced long factor is genuinely unrestricted coefficient1 because original a,b<=sqrtD and truncated mu factors cannot exceed the2/3 scale at D>=2^64. Whole prefix p<<D^(1/3). Its >Z part costs D^(1/3)+sqrt(D/Z). At p<=Z freeze ORIGINAL opposite n; keep prefix(p,n)/(p,k)/(p,s,w) zeros in the actual prefix coefficient BEFORE opening the long-variable FULLQ=rad_good(pnksw). No auxiliary common d is opened. Including original p^-1/2, h-deletion costs D^1/4 Nk^3/8 Np^-3/8 Nh^-3/8. Sum gives D^1/4 Nk^3/8 Z^5/8. Z=D^2/9 balances columnD^7/18; original finite-k majorant Nk^-13/8+epsilon converges without changing the identity. DIRECT Bessel error is applied directly to A_U,A_U: no A_U-to-A_Y error. All rho/e/w/source/root/primitive phases, means, equal-norm fibres, raw zeros, common W, capacity and original finiteK survive. Legal k/s/w overlaps remain.

### Checks and limits

New exact root geometry:4680 rational cases,648 matrices/24 rational subgroup/27 cosets;3942 wrong-diagonal negative controls. Root finite-geometryv1 serialization failure is preserved; v2 accepted. C:40SL2/120H3/320phase/88Mellin/544primary formal cases. B:432 affine/204primary/12rational envelopes. NEW root793091 formal scale compositions,761471 typed subset,1842TypeI/759629TypeII/28j1, exact Fraction budgets. These are NOT original-family energy data, training, asymptotics or Lean. Typed exponent grid is not exhaustive physical dyad coverage: exact proof inequalities handle constants. No finished old tables/tails/scalar/norm/controls were rerun. V1/v2 proof wording, coefficient conventions, all failed harnesses and required addenda remain preserved.

Only pinned unconditional DR2109.07463v3 Section5/AppendixA and previously admitted physical cubic/HB/CRT/Bessel inputs are used; not the paper's GRH-conditional prime results. Full primary bodies/private cache pins remain excluded from future public closure; citation metadata/versions/hashes are public. Root source closurebc66018a binds44current pins. Scientific claims are prose/external-input theorems, not kernel-checked Lean.

SSH refused during the preceding run; no Mac project fallback occurred. It recovered18:46:51UTC. All15HEAD/index states/14worktrees,18promoted scientific artifact bytes and CPUlock passed preservation5cb46cca. SourceHEADdba37ff/index0ef1af, frozen249ce6/35patch42e and every original/output/cache/environment/history/private model/Macworkspace/old8765 are preserved. No auth/token/dependency/infrastructure/GPU/config/Claude/externalMCP/Lean/build/publish action occurred. Linux4.24approval is unanswered: no install/download/substitution/reinventory/repeated question.

### Checkpoint and next concrete work

P7 claim373b0e7f-3795-4a6a-bb23-fa74388e9004 / helper checkpoint215d3552-f50f-4a24-84c3-1c9c717b5ebc remain in_progress. P4/P9 and both completion gates remain false. The helper is administrative, not a proof checker.

Next substantive implementation milestone: coherently integrate the accepted ramified/full-A_U results into the critical book and focused/note sources, with an original canonical construction visual, staging and independent PDF/MathML/UI preservation checks before any release. Reconcile the existing P4 claim first. Do not perform a status-only republish.

Next genuine arithmetic: map and estimate the ORIGINAL frequency complement outside this declared representation-fixed pure top prefix, or the actual mixed/neighboring two-pivot extension, before losing the joint phases/means/masks. The new result does not bound all pure sectors, the infinite dual-frequency complement, full h1, short/principal assembly, arbitrary weighted rows, independent positive determinant/zero-location bridges, or separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes. No assumed Artin holomorphy/GRH/desired positivity/zero locations. Analytic/category Lean and GRH remain open. Do not replay the now-finished ramified FE or new formal controls as new research.

Keep ONE existing heartbeat ACTIVE; no cleanup/reset/no-op/status commits or proof schedule guarantee. Native automation metadata may be updated on Mac only; all project/scientific work remains SSH-Linux.


## 6 November 2026 — reviewed ramified-cusp/full-coefficient local edition

The Linux working edition is348pages/40chapters/10858nativeMathML. Every one of10299 earlier literal math subtrees remains ordered and byte-identical;389tables,14canonical iframe tools,31earlierSVG references and all91 earlier non-HTML book assets (92 original book files including HTML) are preserved. The new original rational-cusp/whole-factor construction figure raises references to32. Focused concise/extended PDFs are85/243pages; analytic notes43/131pages. All five are freshly built from pinned current sources; no dependency or Lean substitution was used.

Shared papers/ramified-gauss-{core,details}.tex and matching book sections contain the explicit known27 cusp construction, literal Kubota phase, actual raw finite-character family, angular Mellin factor NC^(1-2s), coefficient convention/normalization and coarse R^(3/2) dual norm. The ramified fixed-finite-kappa sharp H(3/4,3/8) estimate follows from the identified unconditional theta/cubic inputs. Zeroth-angular residues at1/6 and5/6 are retained. Jacobi rho is NOT finite order; exactly one angular vartheta remains. DR2109.07463v3 Section5/AppendixA and the pinned deFaveri2610.04045v1 cubic input are external theorems, not new sieve or Lean reproofs. Full primary bodies/private publisher caches remain excluded from public closure; versioned citation metadata and hashes remain pinned.

The ORIGINAL unweighted PURE finite primitive-dual TOP prefix P_X[AU,AU] now has a complete original-coefficient proof. Under D>=2^64,1<=U<=sqrtD,A1~H=D^(3/4),X=D^(3/8),V=X^(1/6)/2, the whole at-most-eleven-factor partition and Z=D^(2/9) give normalized leading upper power101/144, margin7/144 below3/4. The raw numerator D*P_X has one extraD. This is the exact representation-fixed finite prefix, not the whole signed h1 form. Opened B_U=mu*A_U is not the project's original C_U; the ternary identity is used only on Nm>U, with literal unit factors retained. Original n is frozen before the long-column bound; prefix(p,n)/k/s/w rawzeros remain outside the full Q deletion. Original finiteK, source/ray/root/Gamma/primitive-e values, all means/equalnorm fibres, allowed overlaps, capacity and fixed-common-W seminorms remain. No AU-to-AY replacement or auxiliary common-divisor opening occurs.

Independent mathematical/figure reviews and source-bound five-PDF/native checks pass. The original figure was inspected as actual PDF and actual SVG and at its printed book size; representative pages from all five PDFs are legible without clipping. The MathML renderer has no new malformed nodes, raw TeX or conversion warnings, and all75newlabels use PDF-aux numbering. Focused desktop/mobile/night/keyboard/source/PDF browser QA and independent18-artifact promotion review govern the local promotion record, not a replay of the completed public release audit. Three inherited munder warnings and old amsmath/hyperref/underfull diagnostics remain disclosed. No new overfull, unresolved reference or Lean declaration is accepted. Source-matched PDF searchability and the public-SVG reproduction limit remain disclosed. Two bounded administrative guard failures (optional-short-title chapter count; book-vs-paper source-map key) were corrected without rerunning builds or relaxing scientific checks; failed receipts and all candidates are preserved.

A separate NEW research-only result remains OUTSIDE this frozen book package: planning/ramified-book-20261106/lane-c/research/BOUNDED_GOOD_PART_COMPLEMENT-v2.md WITH its required fixed-family-match addendum50a7feb1, aggregate23285bc4 and independent B691a56/root32cae907 gates. It estimates the actual lower-sixth complementary cone and whole finite cone with good sixth-free Nr<64 and ARBITRARY allowed S-supported part, at the same101/144 upper budget. Literal finite-ray order L=lcm(6,exponent G_ray), primitive power raw masks and a NEW fixed numerator family are proved; order alone is never used to bound varying conductor. Equal-norm ideals and legal r/s overlaps remain distinct. Fresh54432 phase/raw-mask and4079 formal cone controls are synthetic, not actual energy/Lean data; completed controls were not rerun for the v2 precision. Growing good sixth-free Nr>=64, the full dual ball and infinite/high-frequency complement remain OPEN.

This is a LOCAL substantive edition, not a new public release. Public Main1f346d1a825aa6eff1479197aef45d293a878902 / Pagesde2614bf439e1c6ab8af09f3242af5a163f16f79 still serve the verified333page/10299MathML edition. All science, staging, rendering, algebra and browser checks ran on iska-linux-vscode via SSH. SourceHEADdba37ff/index0ef1af and all15HEAD/indexstates/14releaseworktrees, original manuscripts, datasets/checkpoints/environments/cache/history/private active models and Macworkspace/old8765preview are protected. No auth/token access/transfer, dependency/toolchain installation, infrastructure/GPU, external MCP or Claude/global configuration change occurred. Linux4.24approval remains unanswered: no install/download/substitute/reinventory/repeated question.

Next implementation: prepare a separately reviewed substantive public release from this local milestone with the five PDF exports, source-only public research closure and strict inherited live-browser/source-pin/integrity/visibility/credential gates; no status-only commit or republish. Next genuine arithmetic: estimate actual growing-good-r finite frequencies or neighboring mixed blocks BEFORE losing joint phases/means/raw masks, then assemble the remaining full frequency/short/principal terms. Whole signed13/12/global unsigned9/8 are unchanged. Independent positive determinant/zero-location and separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin obligations remain open; no Artin holomorphy, GRH, desired positivity or zero locations are assumed. Actual analytic/category Lean remains unfinished.

The governing local record is outputs/checks/2026-11-06-ramified-book/root/MILESTONE_ACCEPTED-v1.json and planning/ramified-book-20261106/HANDOFF-v1.md. P4 claim9902aec2-80f1-48e5-9e0a-1e79a2028dff remains in_progress together with P7/priorP9. Both implementation/research completion gates remain FALSE. Keep this ONE existing heartbeat ACTIVE, with no cleanup/reset/no-op/status commit or guaranteed proof schedule.
