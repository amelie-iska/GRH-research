# Current conductor refinement — frozen inspector handoff

All work ran on `iska-linux-vscode`, designated GRH project. Writes are confined to the three owned web files and the fresh `planning/arithmetic-learning-20261105/qa-pivot/` and `outputs/checks/2026-11-05-arithmetic-learning/ui-pivot/` directories. No existing output, proof, page, environment, dependency, authentication, GPU job, publication or MCP setting was changed.

Before editing, all three prior web files were copied byte-for-byte into `outputs/checks/2026-11-05-arithmetic-learning/ui-pivot/previous/`. Their receipt matches the earlier frozen hashes, and final verification rechecks every copy. Existing historical receipts and exports remain intact.

The full old face now shows old BGL power 5/4, the earlier cube-only minimum, current ordinary power 1 everywhere and target 3/4. The text explicitly retires the former remaining-half-face claim as historical. Actual terms D and R², ordinary and current finite sums, six scales and weighted capacity remain evaluated with unknown constants and epsilon losses explicitly omitted. Finite sums are not measured or guaranteed numerical energies.

A distinct original SVG heatmap shows x1,x2≥0, x1+2x2≤3/4, other exponents zero. It evaluates min(max(r,1+r−m,2/3+r−m/3),max(1,2r)). It supports click selection, native arrow navigation and exact buttons for (5/12,1/6) and (3/4,0), both power 7/6. The global envelope H+DH^(1/6)+(DH)^(2/3) and remaining gap 5/12 are explained. These are upper-envelope witnesses, never arithmetic energy lower bounds. The signed covariance, gcd-one coupled sum and determinant/zero-location bridge remain open; no new analytic large-sieve theorem, Lean result, training result or GRH proof is claimed.

`pivotState` retains every prior field with exactly its prior cube-only meaning. Added fields include ordinaryPowers/Terms/Power/Sum, currentPower/Sum/Saving/TargetGap and globalPower/TargetGap. New `obstructionState` exports the triangle evaluator. Historical consumers remain compatible.

## Focused verification

- `python3 planning/arithmetic-learning-20261105/qa-pivot/independent_numeric.py`: PASS, 1,037 face cases plus 4,186 triangle points, independently derived Fraction exponents and 70-digit Decimal terms. Historical fields equal the preserved prior evaluator at every face case. Both exact 7/6 witnesses and invalid-point refusal pass. These finite checks do not prove the infinite analytic theorem.
- `python3 planning/arithmetic-learning-20261105/qa-pivot/run_browser.py`: PASS, real Firefox9335. Both palettes at 320/390/768/1440px, all controls, full face, historical/current separation, capacity, native slider/select and map arrows, both witness buttons, 1,024 triangle cells, iframe theme sync, no horizontal overflow, no page/fetch errors. Legend contrast is at least 5.06:1 light and 9.16:1 night. Evidence: `run-20261105T150507550530/browser.json` and screenshots in the owned output directory. Desktop light full-face and night obstruction screenshots were visually inspected.
- `node --check web/quadratic-pivot.mjs`: PASS. Post-browser edit only inserted readable spaces into prose; evaluator, geometry, controls and CSS are unchanged. The initial independent-check fixture had one parenthesis typo, corrected before any numeric run; no application failure occurred.

Firefox9335 was released and the ephemeral HTTP fixture shut down in finally. The existing browser process is preserved and available to root.

Root integration owns `/book/main.html#mcs:core`, the current `research/mixed-conductor-and-learning.md` link, navigation and final integrated byte/link checks. The historical `/book/main.html#qp:core` and pinned GL source remain linked. Frozen hashes: `outputs/checks/2026-11-05-arithmetic-learning/ui-pivot/frozen-receipt.json`.
