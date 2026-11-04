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
