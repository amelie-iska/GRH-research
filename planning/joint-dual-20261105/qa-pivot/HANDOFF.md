# Quadratic pivot exponent inspector — frozen handoff

Implemented only `web/quadratic-pivot.{html,css,mjs}` plus this QA directory and the matching owned output directory. All edits, execution, browser checks and screenshot generation took place on `iska-linux-vscode` in the designated GRH project. No dependency, environment, server configuration, publication, GPU job, authentication or existing laboratory was changed.

The original SVG visual shows the entire a∈[0,1/4] face with the old power5/4, quadratic1+2a, their minimum and target3/4. Controls select a, five D scales, and dominant/all-monomial detail. Actual monomial values, both finite sums, all six scale coordinates, R, H, M, AB=H^(1/3), and the weighted capacity (AB)^3=H are evaluated. Finite algebraic sums explicitly omit unknown constants and epsilon losses; they are not numerical Lambda bounds or observations.

Scope is explicit throughout: Goldmakher–Louvel Corollary1.2 for n=6, power3 is the external input. A strict power gain occurs exactly below a=1/8. The complete remaining half-face survives with power5/4; the target3/4 is never met. Original collision zeros, finite local partitions, the arbitrary global sixth-power factor and original gcd-one signed coupled-sum obligations remain visible. No new analytic large sieve, global exponent improvement, Lean theorem, training result or GRH proof is claimed.

Shared assets were attached to the owned HTML via `scripts/theme_assets.py:install_theme`; the broad HTML preparation script was not run. The responsive custom SVG avoids shared-theme inversion while matching both site palettes. The iframe parent-theme protocol is inherited and verified.

## Evidence

- `python3 planning/joint-dual-20261105/qa-pivot/independent_numeric.py`:1,037 independent cases; Fraction exponents on all1,001 slider positions, Decimal70-digit monomials at all five scales and crossover neighbors; weighted capacity, strict sector, never-met target and invalid inputs pass. The checker does not reprove the external analytic theorem.
- `python3 planning/joint-dual-20261105/qa-pivot/run_browser.py`: final run `outputs/checks/2026-11-05-joint-dual/qa-pivot/run-20261105T135209099174/`. Real Firefox9335 passes320/390/768/1440px in light/night, all controls and native keyboard slider/select navigation, all endpoints and crossover neighbors, term detail, no horizontal overflow, no page/fetch errors, embedded theme with no duplicate toggle. Legend text contrast is at least5.06:1 light and9.16:1 night. Desktop light/night and320px night screenshots were visually inspected.
- `node --check web/quadratic-pivot.mjs`, unique HTML IDs, local asset existence and required outgoing link targets pass. The final SHA256 receipt is `outputs/checks/2026-11-05-joint-dual/qa-pivot/frozen-receipt.json`.

Earlier harness failures are preserved: the first contrast parser contained a JavaScript escape typo; two extra synthetic-Space probes of the pre-existing shared theme button did not activate it in this Firefox session. The final focused keyboard checks cover all three new native controls. Shared theme code was unchanged; no claim is made that those extra probes passed. Session ownership and the ephemeral HTTP fixture are released in finally; the existing browser process remains intact.

## Root integration

The page links to `/book/main.html#qp:core`, the planned GitHub `research/quadratic-pivot-sector.md`, and pinned `https://arxiv.org/pdf/1112.1642v2`. Root owns book/research content, navigation, build/copy integration and final checks that those new link targets exist in the integrated edition. No existing page or manuscript was modified by this subtask. Browser smoke checks can import the exported `pivotState(a,dLog)` without a DOM.
