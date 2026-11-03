# GRH research

A private research workspace for auditing and developing surface-order and Hilbert–Pólya approaches to the generalized Riemann hypothesis, with synchronized concise and extended manuscripts and exact Lean4 checks.

**Current result:** a corrected conditional spectral criterion, convergent arithmetic approximants with explicit errors, an explicit arithmetic Abel trace-class family, and rigorous obstructions to several supplied proof steps. **A complete proof of GRH has not been established.** In particular, the claimed prime/geodesic identification is false, and the absolute prime-tail bound used in the separate GRH PDF diverges in the asserted range. These require mathematical replacements. See [audit](planning/AUDIT.md) and [open obligations](planning/OPEN_OBLIGATIONS.md).

## Infinite dessin orders and determinant development (2026-11-03)

The current focused editions use **infinite-dimensional locally gentle algebras and completed surface orders from explicit cellular dessins** throughout: the nodal interval, spherical loop, two theta dessins, elliptic square, and a Chebyshev family. [Shared core](papers/dessin-core.tex), [expanded proofs](papers/dessin-details.tex), and [pinned primary references](papers/dessin-references.tex) form the new account. Earlier general bodies and source clones remain intact; [previous focused PDFs](outputs/papers/archive/c465a95/) are preserved.

| Current focused edition | TeX | PDF |
|---|---|---|
| Concise, 19 pages | [resolutions-concise.tex](papers/resolutions-concise.tex) | [resolutions-concise.pdf](outputs/papers/resolutions-concise.pdf) |
| Extended, 38 pages with calculations and diagrams | [resolutions-extended.tex](papers/resolutions-extended.tex) | [resolutions-extended.pdf](outputs/papers/resolutions-extended.pdf) |

The paper gives complete explicit resolution/order/Cartan calculations; presentation semi-invariant weights and their precise Hom/Ext scope; positive-degree Schur module functors, Young tableaux and natural Littlewood–Richardson maps; the cyclic monodromy invariant ring and a convergent local positive Cauchy kernel. Schur functors fail termwise exactness and fixed order-base action in displayed examples. On continuous finite-length completed modules cycle traces are nilpotent, so nonconstant parameters require semi-invariants, flags or pp data.

The actual node lattice category has two proved almost-split sequences and a genuine exact 3×3 specialization diagram. The supplied affine-C diamond paper is realized as an explicit quotient-annihilator subcategory of the infinite Chebyshev dessin order, with nine actual string modules, twelve signed maps and four exact meshes. Its intrinsic AR property is not silently promoted to the entire order category. Ringel/Puninski–Prest/Laking–Prest–Puninski results enter through a precisely specified domestic quotient and relative Ziegler spectrum. [Independent reviews](planning/reviews/dessins/README.md) record coverage and qualifications.

Ordinary Leavitt/graph CK1 relations collapse when combined with all closed-dessin gentle zero relations. The replacement constrained-path Fock C* algebra retains them and has a proved compact extension; its boundary map is minus unsigned graph incidence. The degree spectral triple is ungraded and its spectrum depends only on edge count. The compact ideal supports the earlier [arithmetic Abel family](research/abel-boundary-determinant.md), preserving exact L determinants and trace-norm convergence, but not yet module/Frobenius compatibility. Two complex-isomorphic elliptic Belyi pairs have different rational Frobenius factors: arithmetic descent cannot be recovered from complex dessin data alone.

Thirty new Lean declarations verify **actual formal-power-series node order and resolution components**, CK1 collapse, determinant base change and actual symmetric-square identities; the full analytic suite has **203 checked declarations**. The [exact checker](scripts/check_dessin_extension.py) and [diamond checker](scripts/check_dessin_diamonds.py) supplement universal proofs with reproducible finite diagnostics. They do not formalize all the papers or GRH. Recent Connes/Consani/Moscovici, van Suijlekom and Deninger sources are used with exact domain, ground-state, arithmetic and convergence hypotheses.

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

Lean4.24.0 is isolated under ignored `.tools/`; [lean/README.md](lean/README.md) records the official archive, checked digest, exact theorem scope and instructions for another machine. Mathlib4.24.0 and its pinned verification dependencies are isolated under `.tools/`; public build caches were downloaded without cleaning existing caches. No production library or global Lean configuration was changed. The standalone Lean build verifies seven arithmetic/finite-matrix statements. A [separate pinned mathlib layer](lean-analytic/README.md) verifies 203 statements about complex Euler factors, boundary convergence, Hermitian rigidity, positive spectral pencils, certificate geometry, Jensen metric components, Euler-correction components, principal-residue normalization, frozen row-count components, the perturbed low-energy exponent, central contour/integral components, actual finite-field characters/Gauss sums, normalized finite Fourier/dyadic Gram components, actual Eisenstein quotient-ring reciprocity phases, local reflected characters/phase and common-density components, projective-resolution and arrow-state determinant components, Hodge/boundary matrices, continuous Abel boundary operators, actual completed nodal order/resolution components and symmetric-square/invariant components. Both layers print axiom dependencies. They do not formalize the whole papers or prove GRH.

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
