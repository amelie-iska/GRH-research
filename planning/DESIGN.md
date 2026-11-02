# GRH research project design

Date: 2026-11-02 (America/Los_Angeles). Status: approved by user on 2026-11-02; implement necessary/helpful improvements.

## Intent
Audit the three supplied research repositories, retain valid results, and pursue a rigorous proof of a precisely scoped GRH. A proof is an objective, not an assumed deliverable. No manuscript may assert a resolved theorem while a necessary dependency is false, conditional, or unverified.

## Layout and preservation
The project root is `/Users/amelieschreiber/Documents/LaTeX-projects/GRH`. Existing fresh clones `math/`, `GRH/`, and `Surface-Orders-Hilbert-Polya/` remain untouched. Register them as pinned Git submodules without moving their Git metadata. A new private GitHub repository `amelie-iska/GRH-research` tracks planning, original research, Lean code, paper sources, and compiled PDFs. Preserve each upstream license; do not impose a new license without instruction.

`planning/`: inventory, coverage, audit, bibliography, obligations, implementation plan.
`research/`: new propositions and reproducible counterexamples.
`lean/`: pinned Lean 4 project, no admitted proofs or project-specific axioms.
`papers/`: concise and extended TeX versions sharing core statements and references.
`outputs/`: generated PDFs, check reports and build evidence; source repositories immutable.
`scripts/`: focused reproducibility commands. `README.md`: status, build instructions and limitations.

## Approaches considered
1. Immediately consolidate the claimed unconditional proof. Rejected by mathematical evidence: the exact prime/geodesic matching is false and several analytic convergence arguments are unsupported.
2. Audit first, preserve conditional spectral results, prove concrete obstructions, then attack one explicit analytic bridge. Recommended: it produces checkable mathematics without assuming GRH.
3. Switch entirely to Weil/Li positivity or an adelic trace formula. Retain as alternate research branches; each carries its own unsolved positivity/trace obligation and cannot be substituted as an established solution.

## Mathematical scope
Start with primitive Dirichlet characters (including the conductor-one principal case, with pole removal). Treat Hecke, Dedekind and general Artin extensions separately. State meromorphic/entire conventions, nontrivial-zero region, parity, conductor, root number and complex conjugate character explicitly. Conditional Hurwitz closure requires local uniform convergence and a nonzero limit on each connected off-line component. General Artin holomorphy is a separate obligation.

## Verification and publication
Every claimed theorem gets a dependency row and proof status: prose checked, Lean checked, conditional, refuted, experimental, or not reviewed. Exact counterexamples take priority over numerics. Lean must compile with a pinned toolchain and report theorem axioms; small abstract lemmas must never be represented as a formal proof of the analytic GRH bridge. TeX builds must pass twice with resolved references and a visual layout check. Push milestone commits only after checking the staged file list, source pins and repository privacy. No CI infrastructure or production dependency is introduced without approval.

## Open decisions
Use the approved repository name GRH-research. Use a project-local pinned Lean toolchain, keeping existing environments untouched. Publication authorship and target journal remain the user's decisions. A rigorous GRH proof and independent expert validation remain outstanding research, not scheduled guarantees.
