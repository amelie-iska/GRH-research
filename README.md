# GRH research

A private research workspace for auditing and developing surface-order and Hilbert–Pólya approaches to the generalized Riemann hypothesis, with synchronized concise and extended manuscripts and exact Lean4 checks.

**Current result:** a corrected conditional spectral criterion, convergent arithmetic approximants with explicit errors, and rigorous obstructions to several supplied proof steps. **A complete proof of GRH has not been established.** In particular, the claimed prime/geodesic identification is false, and the absolute prime-tail bound used in the separate GRH PDF diverges in the asserted range. These require mathematical replacements. See [audit](planning/AUDIT.md) and [open obligations](planning/OPEN_OBLIGATIONS.md).

## Papers

| Edition | Source | Compiled PDF | Scope |
|---|---|---|---|
| Concise, 6 pages | [concise.tex](papers/concise.tex) | [concise.pdf](outputs/papers/concise.pdf) | Definitions, conditional closure, proved obstructions and consequences |
| Extended, 13 pages | [extended.tex](papers/extended.tex) | [extended.pdf](outputs/papers/extended.pdf) | Same core plus calculations, examples, algebra/topology checks, convergence issues and alternate research tracks |

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
python3 scripts/check_arithmetic_approximants.py
python3 scripts/check_exponent_frontier.py
sh scripts/build_papers.sh
```

Lean4.24.0 is isolated under ignored `.tools/`; [lean/README.md](lean/README.md) records the official archive, checked digest, exact theorem scope and instructions for another machine. Mathlib4.24.0 and its pinned verification dependencies are isolated under `.tools/`; public build caches were downloaded without cleaning existing caches. No production library or global Lean configuration was changed. The standalone Lean build verifies seven arithmetic/finite-matrix statements. A [separate pinned mathlib layer](lean-analytic/README.md) verifies sixteen statements about complex Euler factors, boundary convergence, Hermitian rigidity, and positive generalized spectral pencils. Both layers print axiom dependencies. They do not formalize the whole papers or prove GRH.

Evidence is saved in [outputs/checks](outputs/checks/). Exact rational checks are deterministic and need no seed. Both PDFs compile with resolved references and representative rendered pages were inspected. Source data and upstream environments remain untouched. No MCP server was enabled.

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
