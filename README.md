# GRH research

A private research workspace for auditing and developing surface-order and Hilbert–Pólya approaches to the generalized Riemann hypothesis, with synchronized concise and extended manuscripts and exact Lean4 checks.

**Current result:** a corrected conditional spectral criterion, convergent arithmetic approximants with explicit errors, an explicit arithmetic Abel trace-class family, and rigorous obstructions to several supplied proof steps. **A complete proof of GRH has not been established.** In particular, the claimed prime/geodesic identification is false, and the absolute prime-tail bound used in the separate GRH PDF diverges in the asserted range. These require mathematical replacements. See [audit](planning/AUDIT.md) and [open obligations](planning/OPEN_OBLIGATIONS.md).

## Research book and interactive companion (2026-11-03)

The new [book TeX](book/main.tex), [PDF](outputs/book/surface-orders-book.pdf), and [native-MathML on-page edition](web/book/main.html) develop the supplied manuscripts with corrected physics, full category-labelled AR diagrams, Hom-control, determinant relations, ToricGT/hybrid interfaces and higher-genus examples. Both **complete original TeX sources** are preserved byte-identically in [source-editions](book/source-editions/) with [provenance](book/source-provenance.json). Preservation is distinct from endorsement: the original unconditional GRH claims do not survive the recorded audits. [Full inclusion and verification ledger](book/VERIFICATION.md).

The private local page is **[http://127.0.0.1:8765](http://127.0.0.1:8765)**; the [on-page book](http://127.0.0.1:8765/book/main.html) has interactive chapter panels, complete code views and local mathematics. The atlas includes genus1/2/3/5/9/16 dessins, 4D rotations of complex sheet coordinates, and finite windows of the infinite {7,3} tiling in disk/hyperboloid views. A generated Manim clip is included. Source windows are labelled as projections or finite patches, with no claimed arithmetic identification.

Six actual local CPU experiments are displayed: three PennyLane architectures (QCNN compression, quantum graph convolution and quantum-feature attention), Strawberry Fields Gaussian pooling, a ToricGT/PennyLane Harper surrogate followed by exact rational PSD certificates, and a larger genus-four nine-qubit QCNN. [Reproduction and dependencies](examples/quantum/README.md), [saved results](outputs/experiments/), and [independent reviews](planning/reviews/book/). Cirq, Qiskit, PennyLane and Strawberry Fields cross-backend carrier tests pass. NVIDIA cuQuantum/CUDA-Q sources are forked and cloned, but GPU adapters are not executed on this Apple machine. Sage source is supplied; the installed launcher lacks its target app, so its execution is not passed.

The user approved the new isolated CPU environment; existing environments/toolchains were preserved. **243 printed Lean reports pass** at the pinned environment, with no admissions or custom axioms. This does not formalize the whole book: [coverage and outstanding work](book/VERIFICATION.md) are explicit. GRH and the independent positive arithmetic determinant bridge remain open.

Rebuild with `sh scripts/build_book.sh`, `sh scripts/build_book_html.sh`, and `python3 scripts/prepare_companion.py`. Start/restart the loopback-only server with `python3 scripts/serve_book.py`; no public deployment or external scripts are needed. The preview is running as a separate local process, so a chat interruption need not stop it.

## Governing implementation plan and active loop

[Master implementation plan](planning/MASTER_IMPLEMENTATION_PLAN.md), [dependency queue](planning/IMPLEMENTATION_QUEUE.json) and [versioned loop prompt](planning/IMPLEMENTATION_LOOP_PROMPT.md) consolidate every instruction and accepted correction. The existing `grh-research-loop` heartbeat is active hourly. It resumes one ready concrete task, checks evidence, updates the book/page/coverage and privately pushes substantive milestones. Implementation completion and a complete rigorous GRH proof are separate gates.

The [live plan and queue](http://127.0.0.1:8765/implementation-plan.html) tracks ongoing work. The latest extension deduplicates the book's generic panels, introduces corrected Manim theta/HLS/bifiltration/pooling scenes, and adds a fully worked persistence/Schur/surface-coefficient chapter. Both complete original sources and the old clock schematic remain preserved.

The [step-through architecture inspector](http://127.0.0.1:8765/architecture.html)
now displays the [22 numerical cases and 836 DAG nodes](examples/architecture/README.md)
from six trained CPU model families and six fixed-weight references, plus an
adjustable computed clock/shift carrier. Orbit/zoom the 3D dependency scene,
step or play the pass, inspect tensor heads/coordinates and literal values,
select circuit gates, view Gaussian marginals and examine tropical witnesses,
expert routing and exact Harper certificate records. Browser tests cover every
saved case, numerical coordinates, checksum rejection, loading/playback races,
mobile layout and the unique in-book embedding. All 22 original record hashes
and trained checkpoints are unchanged. This is a computational inspector;
complete categorical/physics/arithmetic formalization remains pending.

## Infinite dessin orders and determinant development (2026-11-03)

The [covering/geometry extension](research/covering-geometry-interfaces.md)
integrates the newly requested covering lecture, tame GLS/AR paper and
Schroll geometric-model survey with pinned primary sources. It proves a
finite-support deck-Hom formula for actual theta quotients, a nine-dimensional
indecomposable outside the covering image, and a specified higher-genus
family with the same obstruction (dimensions 27 and 57 in genera 4 and 9).
The bounded-derived push-down is consequently not dense. A separate actual
theta example has unequal Hom-control defects 4 and 1 at the same K0 class.
Exact code checks 36 Hom pairs and the radical multiplication; three new
Lean statements verify the actual matrix relations and Euler obstruction.
The [new book chapter](http://127.0.0.1:8765/book/main.html#x1-8400022)
distinguishes coverings, GLS equivariance, graded/Fukaya categories and
completions. These results do not establish the arithmetic determinant bridge.

The current focused editions use **infinite-dimensional locally gentle algebras and completed surface orders from explicit cellular dessins** throughout: the nodal interval, spherical loop, two theta dessins, elliptic square, and a Chebyshev family. [Shared core](papers/dessin-core.tex), [expanded proofs](papers/dessin-details.tex), and [pinned primary references](papers/dessin-references.tex) form the new account. Earlier general bodies and source clones remain intact; [previous focused PDFs](outputs/papers/archive/c465a95/) are preserved.

| Current focused edition | TeX | PDF |
|---|---|---|
| Concise, 23 pages | [resolutions-concise.tex](papers/resolutions-concise.tex) | [resolutions-concise.pdf](outputs/papers/resolutions-concise.pdf) |
| Extended, 50 pages with calculations and diagrams | [resolutions-extended.tex](papers/resolutions-extended.tex) | [resolutions-extended.pdf](outputs/papers/resolutions-extended.pdf) |

The paper gives complete explicit resolution/order/Cartan calculations; presentation semi-invariant weights and their precise Hom/Ext scope; positive-degree Schur module functors, Young tableaux and natural Littlewood–Richardson maps; the cyclic monodromy invariant ring and a convergent local positive Cauchy kernel. Schur functors fail termwise exactness and fixed order-base action in displayed examples. On continuous finite-length completed modules cycle traces are nilpotent, so nonconstant parameters require semi-invariants, flags or pp data.

The actual node lattice category has two proved almost-split sequences and a genuine exact 3×3 specialization diagram. The supplied affine-C diamond paper is realized as an explicit quotient-annihilator subcategory of the infinite Chebyshev dessin order, with nine actual string modules, twelve signed maps and four exact meshes. Its intrinsic AR property is not silently promoted to the entire order category. Ringel/Puninski–Prest/Laking–Prest–Puninski results enter through a precisely specified domestic quotient and relative Ziegler spectrum. [Independent reviews](planning/reviews/dessins/README.md) record coverage and qualifications.

Ordinary Leavitt/graph CK1 relations collapse when combined with all closed-dessin gentle zero relations. The replacement constrained-path Fock C* algebra retains them and has a proved compact extension; its boundary map is minus unsigned graph incidence. The degree spectral triple is ungraded and its spectrum depends only on edge count. The compact ideal supports the earlier [arithmetic Abel family](research/abel-boundary-determinant.md), preserving exact L determinants and trace-norm convergence, but not yet module/Frobenius compatibility. Two complex-isomorphic elliptic Belyi pairs have different rational Frobenius factors: arithmetic descent cannot be recovered from complex dessin data alone.

Thirty new Lean declarations verify **actual formal-power-series node order and resolution components**, CK1 collapse, determinant base change and actual symmetric-square identities; the full analytic suite has **220 checked declarations**. The [exact checker](scripts/check_dessin_extension.py) and [diamond checker](scripts/check_dessin_diamonds.py) supplement universal proofs with reproducible finite diagnostics. They do not formalize all the papers or GRH. Recent Connes/Consani/Moscovici, van Suijlekom and Deninger sources are used with exact domain, ground-state, arithmetic and convergence hypotheses.

The [dessin extension plan](planning/DESSIN_EXTENSION_PLAN.md), [current frontier](planning/CONTINUATION.md), [claim ledger](planning/CLAIMS.csv) and [open obligations](planning/OPEN_OBLIGATIONS.md) specify what remains. The load-bearing missing result is still a descent/Frobenius-compatible arithmetic determinant with an independently proved positive realization for the same completed L-function. The new local Schur positivity and simple Fock vacuum do not establish it.

## Graph pullbacks and precise category bridges

The [new graph-pullback review](planning/reviews/pullbacks/README.md) records a full reading of arXiv:1907.10260v3. The focused papers now prove that the existing constrained Fock algebra is the graph C* algebra of an explicit state-and-vacuum graph. For the nodal interval, the paper's actual hypotheses yield a constants-symbol AF pullback. A separate paired diagonal-fiber C* model has a faithful polynomial dessin representation and a complete generation proof, while a formal-unit obstruction proves this embedding cannot extend to the entire completed order. The polynomial image generates that C* algebra **with adjoints**; its ordinary norm closure need not contain them.

The string classification applies directly to finitely generated/artinian polynomial dessin modules. Completed lattices escape those hypotheses; the indecomposable branch k[[x]] is a concrete non-string/non-band example in the ordinary polynomial sense. The smooth infinite quotient k[x] has a precise one-stop annulus Perf/Fukaya model, but its module inflation is not derived fully faithful. LP's smoothness, grading and stop hypotheses and OPS's category conventions are retained. Our specified Leavitt examples have invariant basis number, witnessed by finite-dimensional quotients.

[Full derivations](papers/dessin-gluing-details.tex), [category scope](papers/dessin-string-scope.tex), [research handoff](research/dessin-pullbacks-and-categories.md) and [exact diagnostics](scripts/check_dessin_gluing.py) accompany ten further Lean matrix/pullback components. That extension brought the analytic suite to187declarations; topological C* results and arithmetic comparison are not fully formalized. Earlier14/25page focused PDFs are preserved in outputs/papers/archive/fa564b6/.

## Arithmetic theta benchmark

A [uniform Jacobi-sum construction](research/theta-jacobi-benchmark.md) now recovers the local Frobenius polynomials of the rational theta twists for every admissible finite field. For split fields its arithmetic multiplication matrix acts on the **actual dessin cellular H1**, with a fixed positive Gram form inherited from its edges. An explicit rational chain map has odd-over-even determinant equal to the classical finite-field curve zeta function; the Kummer twist is compatible up to a displayed chain homotopy. This is a constructive local benchmark, not a global GRH proof or a new finite-field RH theorem.

Extending that same real two-dimensional deck-compatible carrier to inert primes is impossible: the required deck-conjugating map has nonpositive determinant, while Frobenius needs determinant q>0. A complex local replacement is given with its limits. This is a restriction of that carrier, not of all spectral approaches.

The next order-interface issue is precise: regular/projective identity-tensor insertion produces the sixth/eighteenth power of the local polynomial; a residue-simple insertion has the correct scalar polynomial but is not order-perfect and breaks full deck symmetry. A canonical multiplicity-one order/Frobenius comparison remains open. Finite-field center1/2, global elliptic center1 and Dirichlet center1/2 are distinguished.

[Independent proof reviews](planning/reviews/jacobi/README.md), [shared concise addition](papers/theta-jacobi-core.tex), [extended derivations](papers/theta-jacobi-details.tex) and [exact checker](scripts/check_theta_jacobi.py) accompany16newLeancharacter/cellular components. The analytic suite totals203declarations. The preceding17/32page PDFs are archived under outputs/papers/archive/235066a/.

## Projective multiplicity and a derived branch repair

The [next order-interface result](research/theta-projective-multiplicity.md) now treats **arbitrary** order-linear endomorphisms of finite projectives. Their ordinary determinants specialize to sixth powers; bounded perfect-complex ratios retain the obstruction even after cancellation, excluding both a single local quadratic and the full curve zeta. Generically the ordinary ratios are cubes. This strengthens the earlier identity-tensor test, without excluding alternative determinant categories or semilinear actions.

A constructive repair is available: the actual hereditary-branch column lattice defines a derived functor Perf(Λ)→Perf(Q[[u]]) taking a basic projective to rank one. Its determinant on the earlier external arithmetic matrix is the local factor once, without taking a root. This repairs multiplicity, **not the independent arithmetic action**. The selected branch determinant fails full branch-swap compatibility; strict central-fixed rotation on a rank-one branch lattice is also impossible. Ramification plus a changed lattice gives a precisely qualified rotation model. Full arithmetic descent and the global positive spectral comparison remain open.

[Concise theorem](papers/theta-projective-core.tex), [full constructions](papers/theta-projective-details.tex), [independent reviews](planning/reviews/multiplicity/README.md) and [exact diagnostics](scripts/check_theta_projective_multiplicity.py) accompany five new Lean components, bringing the analytic suite to208. The preceding19/38page PDFs are preserved under outputs/papers/archive/13a6896/.

## Tame descent and the full-deck kernel test

The [tame descent calculation](research/theta-tame-descent.md) now explicitly tests the ramified repair. Its invariants recover the cut column; the actual endomorphism invariant algebra recovers the hereditary branch order. A determinant line descends, with a proved nonunit boundary comparison. The obvious Jacobi rotation polynomial fails descent, while its weighted replacement has the wrong characteristic factor.

More strongly, **every finite free, fixed-center coefficient kernel with invertible rotation and branch-swap intertwiners has vertex rank divisible by six**. For arbitrary induced projective endomorphisms, its determinant specializes to a sixth-multiple power. The full character-orbit repair is the hereditary normalization and returns the original ordinary determinant exactly. This closes that specified kernel route; twisted determinant categories and infinite/other arithmetic correspondences remain open. No global GRH conclusion follows.

[Concise theorem](papers/theta-tame-core.tex), [full proofs](papers/theta-tame-details.tex), [independent reviews](planning/reviews/tame-descent/README.md) and [exact checker](scripts/check_theta_tame_descent.py) accompany12printed Lean components, bringing the full suite to220. The preceding20/43page PDFs are preserved under outputs/papers/archive/46df63d/. The handoff rotates next to the actual short-row hybrid mean-square input, retaining all original masks and avoiding GRH-conditional prime estimates.

## Earlier audit papers

| Edition | Source | Compiled PDF | Scope |
|---|---|---|---|
| Concise, 18 pages | [concise.tex](papers/concise.tex) | [concise.pdf](outputs/papers/concise.pdf) | Definitions, conditional closure, proved obstructions and consequences |
| Extended, 44 pages | [extended.tex](papers/extended.tex) | [extended.pdf](outputs/papers/extended.pdf) | Same core plus calculations, examples, algebra/topology checks, convergence issues and alternate research tracks |

Both editions share [core.tex](papers/core.tex). They are research drafts with full proofs of their stated obstruction results; they do not claim a full proof of GRH or certification of all upstream results. Authorship, novelty assessment and submission venue require confirmation before journal submission.

## Source repositories

The original clones are preserved as pinned Git submodules in this directory:

- `math/` — `4eaee87548250b2682affda7d05d947c05554bae`, selected family003 zero-free-region and Landau–Siegel research, with upstream formalizations.
- `GRH/` — `0c77122d3cff5b737fc56730f54045ef185e3df1`,223 page manuscript PDF.
- `Surface-Orders-Hilbert-Polya/` — `212ff730cdfe5d9ab2dee17c11c7f83061fa0bf2`,15556 line TeX manuscript and separate PDF.

See [manifest](planning/SOURCE_MANIFEST.md), [hashes](planning/SOURCES.json), [coverage](planning/COVERAGE.md), and [detailed reviews](planning/reviews/). All three principal `math` analytic sources and the surface TeX have received full textual reading; that is not a certification of every estimate or of their formal dependency graph. The `math` claims target7/8,11/12 or real-zero exclusion, not full GRH. No decisive refutation was found in the corresponding reading pass. Its two selected actual formalization entry points have3125 transitive local OAI modules; that upstream Lean4.34.1 graph has not been built here.

For a fresh checkout:

```sh
git clone --recurse-submodules https://github.com/amelie-iska/GRH-research.git
```

Each source keeps its original license and history. No source clone has been edited or had its Git directory moved. Avoid `lake update`, cleanup commands, or upstream modifications unless explicitly authorized.

## Reproduce the local results

Use the existing TeX Live/latexmk and Python3 standard library:

```sh
python3 scripts/check_obstructions.py
sh scripts/check_lean.sh
sh scripts/check_analytic.sh
python3 -B scripts/check_dessin_extension.py
python3 -B scripts/check_dessin_diamonds.py
python3 -B scripts/check_dessin_gluing.py
python3 -B scripts/check_theta_jacobi.py
python3 -B scripts/check_theta_projective_multiplicity.py
python3 -B scripts/check_theta_tame_descent.py
python3 scripts/check_arithmetic_approximants.py
python3 scripts/check_exponent_frontier.py
python3 scripts/check_arithmetic_zero.py
python3 scripts/check_jensen_metric.py
python3 scripts/check_euler_correction.py
python3 scripts/check_principal_residue.py
python3 scripts/check_frozen_row_count.py
python3 scripts/check_low_energy.py
python3 scripts/check_central_contour.py
python3 scripts/check_finite_correlation.py
python3 scripts/check_gram_poisson.py
python3 scripts/check_reciprocity_period.py
python3 scripts/check_reflected_identity.py
python3 scripts/check_projective_resolutions.py
python3 scripts/check_hodge_determinants.py
python3 scripts/check_abel_boundary.py
sh scripts/build_papers.sh
```

Lean4.24.0 is isolated under ignored `.tools/`; [lean/README.md](lean/README.md) records the official archive, checked digest, exact theorem scope and instructions for another machine. Mathlib4.24.0 and its pinned verification dependencies are isolated under `.tools/`; public build caches were downloaded without cleaning existing caches. No production library or global Lean configuration was changed. The standalone Lean build verifies seven arithmetic/finite-matrix statements. A [separate pinned mathlib layer](lean-analytic/README.md) verifies 220 statements about complex Euler factors, boundary convergence, Hermitian rigidity, positive spectral pencils, certificate geometry, Jensen metric components, Euler-correction components, principal-residue normalization, frozen row-count components, the perturbed low-energy exponent, central contour/integral components, actual finite-field characters/Gauss sums, normalized finite Fourier/dyadic Gram components, actual Eisenstein quotient-ring reciprocity phases, local reflected characters/phase and common-density components, projective-resolution and arrow-state determinant components, Hodge/boundary matrices, continuous Abel boundary operators, actual completed nodal order/resolution components and symmetric-square/invariant components. Both layers print axiom dependencies. They do not formalize the whole papers or prove GRH.

Evidence is saved in [outputs/checks](outputs/checks/). Exact rational checks are deterministic and need no seed. All four PDFs compile with resolved references and representative rendered pages were inspected. Source data and upstream environments remain untouched. No MCP server was enabled.

## Research next steps

The [implementation plan](planning/IMPLEMENTATION_PLAN.md), [claim ledger](planning/CLAIMS.csv), [background sources](planning/BIBLIOGRAPHY.md), and [progress record](planning/PROGRESS.md) define the continuation. The principal target is an arithmetic determinant identity preserved by a self-adjoint realization, followed by independently proved compact-uniform convergence. Alternative tracks include precise Weil/Li positivity and adelic trace formulations. None is assumed solved.

Milestone commits are pushed to the private GitHub repository. Credentials are never placed in tracked files or remote URLs. This repository contains no token from the chat.

## Continued research

The [Euler convergence report](research/euler-convergence.md) proves a structural no-go for finite Euler products near zeros and supplies constructive partial-sum replacements. The [exponent frontier report](research/exponent-frontier.md) extracts the actual7/8and11/12constraints, an explicitly conditional tiny refinement, and the stronger short-row mean-square input needed for further progress. The refinement is not claimed proved: its analytic hypotheses remain unverified.

The next unresolved target is zero location/self-adjoint realization for the convergent arithmetic approximants. Ordinary convergence alone does not provide that property.

## Scheduled research loop

An active hourly research loop is attached to this chat. It resumes the latest recorded proof obligation, performs research and verification, and pushes substantive private milestones. See [loop workflow](planning/RESEARCH_LOOP.md). It reports meaningful findings or required actions rather than routine unchanged status. Keep the desktop app running and the machine on for local scheduled work.

The [Hermitian-rigidity research note](research/hermitian-rigidity.md) proves that an entrywise holomorphic matrix family Hermitian at every complex parameter must be constant. The associated Lean theorem rules out that particular pointwise extraction shortcut; fixed self-adjoint operators and real-axis Hermitian pencils remain possible, with their arithmetic and zero-location obligations still open.

The [positive-pencil research note](research/positive-pencils.md) provides a valid constructive finite spectral criterion: fixed Hermitian A and positive-definite B give real zeros of det(A−zB), with an explicit resolvent bound in prose. The seven new Lean declarations verify the matrix zero-location mechanism, centered substitution, strict imaginary-form criterion and an indefinite off-line witness. Constructing arithmetic pencils with the required determinant matching remains open.

A [certified finite arithmetic test](research/arithmetic-zero-certificate.md) finds a simple off-line zero of the fifth Dirichlet partial sum for the primitive character modulo3. Exact rational enclosures and an explicit Rouche argument reject its direct positive-pencil identification on that disk. This is a zero of a finite approximant, not the full L-function; GRH and the limiting spectral construction remain unresolved.

The [Jensen-metric report](research/jensen-metric.md) changes the arithmetic approximation class and proves an explicit compact error bound. Its coefficient-defined Newton-sum metric gives a conditional exact self-adjoint determinant, with positivity still unresolved. A smooth positive Gaussian-mixture counterexample rejects deriving that metric's positivity from ordinary kernel moment positivity. This part concerns zeta RH only; no general GRH conclusion follows. The model checker does not enclose actual xi coefficients.

The [Euler-correction report](research/euler-correction.md) proves a larger convergence region for the explicit September local factors, inheriting their scalar arithmetic identity. The principal correction contains a shifted infinite-order angular Hecke factor. With the stated classical completion inputs, its zeros prevent the unchanged correction from satisfying the common-signal nonvanishing condition below7/12. This does not refute GRH or the source's claimed7/8 result. Remaining nonprincipal contours and mean squares remain open.

The [principal-residue report](research/principal-residue.md) verifies the compensated normalizer, a uniform relative-error saving, and the principal contour comparison at the perturbed geometry under the listed inherited scalar/high/Mellin/reciprocal contracts. An exact inert-prime example shows that the pointwise approximation by -1 fails at s=3/5; it does not rule out cancellation after prime averaging. The conditional low and row-count extensions are described below; the general energy estimates and nonprincipal contours remain unverified. No new zero-free theorem or GRH proof is claimed.

The [frozen row-count report](research/frozen-row-count.md) reconstructs the perturbed counting interface with kappa=3/4, removing the Delta/4 capacity loss. This remains conditional on the explicitly unverified arithmetic moments, witnesses and earlier7/8 bound. Mesh selection precedes the fixed slot system, and floor-bin rows remain separate. The conditional low extension is described below; no new zero-free theorem is claimed.

The [low-energy report](research/low-energy.md) verifies the perturbed low application under explicit general reflection, Gram and arithmetic-identity inputs. Its possible row loss is absorbed by the rescaled tuple saving. A universal real-exponent bound with support offsets and the actual real-power absorption are checked in Lean. The conditional central extension is described below; its deep source inputs remain unverified and GRH is unresolved.

The [central-contour report](research/central-contour.md) reconstructs the nonprincipal deformation using the first Euler region below7/8. It keeps the full holomorphic correction for movement, spends conductor deficits simultaneously, and integrates only the original row sum after pointwise envelope bounds. Buffered arithmetic bounds and exact high identity remain inputs; outer rows and final closure are not certified. The finite arithmetic audit is described below; the quantitative Gram estimate still needs independent certification.

The [finite-correlation report](research/finite-correlation.md) proves the universal local field kernel and finite Gauss identities with actual Lean MulChar/AddChar objects. Prime-power lifting and CRT bookkeeping received a separate prose audit. An exact F7 sum36>7 demonstrates why the genuine kernel cannot replace its artificial extension off the coprime-residual locus; the source already distinguishes them. Exact Eisenstein diagnostics include the inert field of size25. The reciprocity-period identification is now supplied in classical prose below; pairing/representation and the remaining global analytic bounds are not thereby certified. No new zero-free theorem or GRH proof is claimed.

The [Gram periodic-Poisson report](research/gram-poisson.md) proves a general annular cancellation lemma in prose and reconstructs the quantitative Gram summation with explicit arithmetic representation and fixed reciprocity-period inputs. Nine additional Lean statements check actual finite Fourier normalization, independent-coordinate character cancellation, infinite dyadic sums and the exact scale cancellation. No extra square of the period is lost. Dropping the small-scale support condition is invalid; the source has the required annuli. The period/phase identification is now supplied in prose using classical reciprocity and class field theory, as detailed below; the other analytic source inputs and GRH remain unresolved.

The [reciprocity-period report](research/reciprocity-period.md) supplies the actual common modulus l_fixed=lcm((12),m_presentations,(6)^6 product_(p in S)p^25), independent of growing rows and divisors. The conductor bound uses named classical class field/discriminant theorems; thirteen additional Lean declarations verify the actual O/(4) algebra and phase table, not those entire number-field arguments. An exact norms31/43 witness shows why modulus12 alone cannot cover fixed numerator characters. All original masks and full defining moduli are retained. The reflected arithmetic extraction is now checked conditionally on the canonical theta formula as described below; the arithmetic self-adjoint determinant bridge and every complete GRH scope remain open.

The [reflected-identity report](research/reflected-identity.md) verifies the exact coefficient normalization, shared-cube extraction, row-mark phase cancellation and original zero masks, retaining the canonical theta/cusp formula as an input. A genuine norms7/13 example shows why moving j=4 primes cannot be handled by dropping their cross phase; the source already freezes them. The defined Mellin kernel supplies a common homogeneous profile bound in prose using classical gamma estimates. Nine additional Lean statements check actual arbitrary-field characters, complex phase units and an integrable Banach-valued common-density bound. The hybrid quadratic-cubic mean square and global theta identification remain open, along with the spectral bridge and GRH.
