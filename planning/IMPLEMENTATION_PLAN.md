# GRH audit and research implementation plan

> For agentic workers: use superpowers:executing-plans for approved implementation, preserving all source clones.

**Goal:** Produce an auditable research project, two compiled manuscripts, and genuinely checked Lean results while pursuing the unresolved GRH bridge.

**Architecture:** Immutable pinned upstream sources feed a claim ledger; shared mathematical statements feed both papers. Exact algebraic obstructions and conditional analytic results are kept separate from open arithmetic identifications.

**Tech stack:** Git/GitHub CLI, existing TeX Live/latexmk, Python standard library for exact arithmetic, pinned Lean 4; mathlib only if the approved formalization needs it.

**Spec:** `planning/DESIGN.md`.

## Execution status

Audit, exact obstruction checks, the standalone Lean layer, and both paper editions are implemented; see PROGRESS.md. The analytic/mathlib proof milestones and the research frontier remain open. Checklist entries below retain their acceptance conditions; this document does not assert they are all achieved.

## Global constraints
Preserve source repositories and unrelated data; never delete or move protected progress. No credentials in files or logs. No new production dependencies, CI infrastructure, or broad upgrades. No `sorry`, `admit`, project-specific axioms, or GRH assumptions hidden in an unconditional theorem. Use named output directories and deterministic exact checks. Preserve upstream licenses.

## Review focus
- Principal characters and poles at zero/one: use pole-removed entire targets.
- Odd characters: do not descend a weight-zero twist through PSL2 when χ(-1)=-1.
- Infinite prime tails at σ≤1: never replace conditional cancellation by absolute convergence.
- Determinant normalizations: distinguish det(I−T), its reciprocal, and det(sI−(1/2+iH)).
- Convergence and formalization scope: no transfer from a weak topology or toy predicate to analytic GRH without a proved bridge.

## Task 1: evidence inventory and full audit
Files: `planning/SOURCES.json`, `planning/COVERAGE.md`, `planning/AUDIT.md`, `planning/CLAIMS.csv`, `planning/BIBLIOGRAPHY.md`.
- [ ] Record each upstream commit, tracked paths, file hashes, relevant paper section, and source license.
- [ ] Read repository instructions, README, lockfiles and scripts; inventory all RH/GRH matches in math.
- [ ] Review relevant papers in bounded sections and record exact coverage, including PDF/source differences.
- [ ] Record each invalid step, explicit counterexample, affected claims and necessary repair.
- [ ] Verify selected background against primary sources; distinguish abstract-level lookup from full-paper review.
- [ ] Commit and push audit milestone after approval; never claim full review from keyword search.

## Task 2: exact obstruction results
Files: `research/obstructions.md`, `scripts/check_obstructions.py`, `outputs/checks/obstructions.json`.
Interfaces: deterministic `python3 scripts/check_obstructions.py` exits zero iff all exact assertions pass.
- [ ] Prove no integral-trace hyperbolic matrix has norm p^k, by quadratic conjugation or rational algebraic units.
- [ ] Prove C2×C2 refutes integral cyclic-subgroup induction by degree parity.
- [ ] Check the 2×2 Iwahori shift orientation, determinant reciprocal sign and a Hermitian-part counterexample.
- [ ] Record exact rational witnesses; no random seeds are needed for deterministic arithmetic.
- [ ] Run checks, inspect report, commit and push.

## Task 3: Lean verification
Files: `lean/lean-toolchain`, `lean/lakefile.toml`, `lean/GRHResearch/*.lean`, `lean/README.md`, `outputs/checks/lean.log`.
Interfaces: `lake build` checks exported named theorems; an explicit axioms report identifies all dependencies.
- [ ] Locate existing Lean; if absent, obtain approval for a project-local pinned toolchain before installing.
- [ ] First formalize parity obstruction to integer cyclic induction and finite exact counterexamples.
- [ ] With mathlib, formalize real-eigenvalue/critical-line implication and prime/geodesic algebraic obstruction using actual integer/real/complex objects.
- [ ] Then formalize the analytic zero-free local-uniform-limit theorem using the library's actual analytic functions and topology. Do not encode it as an assumed proposition and call that verification.
- [ ] Build with warnings-as-errors where supported; inspect `#print axioms`; scan for admissions; explain what remains informal.
- [ ] Commit and push only checked results, labeling unimplemented obligations in prose.

## Task 4: papers and documentation
Files: `papers/concise.tex`, `papers/extended.tex`, `papers/common.tex`, bibliography, `README.md`, `scripts/build_papers.sh`, `outputs/papers/*.pdf`.
- [ ] Write a concise article with definitions, proved obstruction theorems, corrected conditional closure, and the explicit open bridge.
- [ ] Write an extended version with complete calculations, worked character examples, determinant conventions, source audit and alternate approaches.
- [ ] Ensure both use the same theorem assumptions; do not present an unresolved program as the full proof requested.
- [ ] Build twice with latexmk, check warnings and references, visually inspect representative pages.
- [ ] Link builds, source pins and checks in README; commit and push publication-preparation milestone.

## Task 5: research frontier (not achieved by scaffolding)
- [ ] Construct arithmetic operators independently of unknown L-function zeros.
- [ ] Prove actual trace identities with ramified and archimedean terms and correct determinant orientation.
- [ ] Prove trace-norm convergence or a normal-family bound uniform in approximation level on a connected domain with genuine overlap with Re(s)>1.
- [ ] Test whether symmetrization preserves the arithmetic determinant; abandon it if a finite counterexample disproves the proposed identity.
- [ ] Compare Weil/Li positivity, canonical products/Jensen polynomials, and adelic trace methods against the exact missing condition, not just analogous shapes.
- [ ] Only after all analytic and arithmetic obligations are proved, derive Dirichlet GRH; extend separately to Hecke/Artin families with all hypotheses checked.
- [ ] Seek independent expert review before asserting a complete proof. There is no guaranteed date or guaranteed outcome for this task.
