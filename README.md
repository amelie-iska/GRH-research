# GRH research

A private research workspace for auditing and developing surface-order and Hilbert–Pólya approaches to the generalized Riemann hypothesis, with synchronized concise and extended manuscripts and exact Lean4 checks.

**Current result:** a corrected conditional spectral criterion and rigorous obstructions to several supplied proof steps. **A complete proof of GRH has not been established.** In particular, the claimed prime/geodesic identification is false, and the absolute prime-tail bound used in the separate GRH PDF diverges in the asserted range. These require mathematical replacements. See [audit](planning/AUDIT.md) and [open obligations](planning/OPEN_OBLIGATIONS.md).

## Papers

| Edition | Source | Compiled PDF | Scope |
|---|---|---|---|
| Concise,4 pages | [concise.tex](papers/concise.tex) | [concise.pdf](outputs/papers/concise.pdf) | Definitions, conditional closure, proved obstructions and consequences |
| Extended,8 pages | [extended.tex](papers/extended.tex) | [extended.pdf](outputs/papers/extended.pdf) | Same core plus calculations, examples, algebra/topology checks, convergence issues and alternate research tracks |

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
sh scripts/build_papers.sh
```

Lean4.24.0 is isolated under ignored `.tools/`; [lean/README.md](lean/README.md) records the official archive, checked digest, exact theorem scope and instructions for another machine. No new production libraries or global environment changes were needed. The Lean build verifies six exact arithmetic/finite-matrix statements, with printed axiom dependencies. It does not formalize analytic continuation, the whole papers, or GRH.

Evidence is saved in [outputs/checks](outputs/checks/). Exact rational checks are deterministic and need no seed. Both PDFs compile with resolved references and representative rendered pages were inspected. Source data and upstream environments remain untouched. No MCP server was enabled.

## Research next steps

The [implementation plan](planning/IMPLEMENTATION_PLAN.md), [claim ledger](planning/CLAIMS.csv), [background sources](planning/BIBLIOGRAPHY.md), and [progress record](planning/PROGRESS.md) define the continuation. The principal target is an arithmetic determinant identity preserved by a self-adjoint realization, followed by independently proved compact-uniform convergence. Alternative tracks include precise Weil/Li positivity and adelic trace formulations. None is assumed solved.

Milestone commits are pushed to the private GitHub repository. Credentials are never placed in tracked files or remote URLs. This repository contains no token from the chat.
