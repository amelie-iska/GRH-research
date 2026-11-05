# Strict rough-mask staged/live QA handoff

Prepared only: no staged or live browser was run. The new v2 harness retains all 141 predecessor groups and the byte-identical global WebSocket/idle/error protocol, then adds rough-mask proof/data/metadata checks. The explicitly bound root expectations are 288 PDF pages, 8552 MathML nodes, 388 tables, 13 embedded labs and the original 29 SVG references. Focused articles have 67/183 pages; notes have 25/74.

Use `run_browser_v2.py` with `--mode stage`, the frozen tenth-release `site-bundle-v1`, its canonical inventory SHA, the site freeze receipt, `expectations-v1.json` and its SHA. Use the same exact harness for live mode only after root publishes the new refs and all changed HTTP hashes pass, supplying the new Pages publication receipt. Every execution creates a fresh output directory and preserves failure evidence; no filter or expectation is relaxed.

Prepared v1 remains preserved. V2 adds the explicit smooth-step zero branch and nodal endpoint check. It separately records the one initial navigation and actual parent departures. Every departure waits for genuine network idle and a 750 ms quiet period, with a 30 second bound. Every fetch error remains fatal. No raw arithmetic, training, authentication, dependency change, publication or ref write is part of this runner.

The compact JSON download is byte-bound to SHA256 7596718fc8c3c55a61197f0a17c7c8bca77816f6a7bae4b9ef005d2413cbb9f9. Publisher caches, private citation pins and PDF administrative markers are outside publication closure.
