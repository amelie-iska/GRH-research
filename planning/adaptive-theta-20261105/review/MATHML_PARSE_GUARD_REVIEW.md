# Native MathML parse guard review

5 November 2026; Linux-only review. Accepted after the narrow fallback correction below. This reviewer changed only render_native.py plus the named review/harness files; no authentication or publication action was performed.

The diagnostics support a progressive-layout issue: math-diagnosis records one msub child-count event, but its completed DOM has no malformed msub. Hiding all math during parsing removes that event; both diagnostic DOMs retain the same three inherited TeX4ht munder nodes with three children. These old nodes remain preserved and are not new content defects.

The head guard adds native-math-pending before mathematical content is parsed. Its CSS hides math only while that class exists. The external helper is deferred, so it removes the class before fitting a completed subtree. With JavaScript disabled the class is never added; native mathematics stays available. No old mathematical subtree is rewritten by this guard. Independent literal-subtree comparison preserved all 5356 formulas in the pinned 37-chapter baseline, while the candidate contains 6890 formulas. Old tables/iframes and all three inherited malformed munder nodes also match.

Review found one regression in the initial guard: if the external helper failed to load after the inline head script ran, every formula could remain hidden. The authorized correction registers a one-shot DOMContentLoaded class removal in the same inline head script. The existing helper's earlier removal remains unchanged. This releases the guard after parsing even when the optional external asset fails, and both releases are idempotent. The renderer diff against its v3 snapshot contains only that fallback and its explanatory comment. Python syntax passes.

check_mathml_parse_guard.mjs passes six lifecycle paths: scripts disabled; external helper blocked; deferred helper removal before measurement; late helper after fallback; a fitting exception; and external execution when the inline script is blocked. Its scope is state/lifecycle regression, not browser layout.

A separate real Firefox 9335 run against v5 intentionally returned HTTP404 for reviewed-math-scroll.js. The server confirmed one blocked request; the helper remained undefined, the document completed with pending=false, all 6890 math elements had display other than none, and no malformed msub existed. Only the inherited munder diagnostic repeated. The BiDi session and loopback server were closed in finally. The reproducible harness is run_mathml_browser_fallback.py with check_mathml_browser_fallback.mjs; no concurrent 9335 work was used. Root's full strict v5 browser QA is separately recorded in outputs/checks/2026-11-05-adaptive-theta/book-browser-final-v5/.

Reviewed final bindings:

- render_native.py:3d6c24c7799acc2c2e10001da88a618b55e38213c45e3940491592e9328293d8
- reviewed-math-scroll.js:6e133f2880f047f0f36a396263cff99f2d3f507a989cbdf54e2bb3a1f0c87582 (unchanged by this reviewer)
- v5/native/book/main.html:94f3cf9a1841e286f01496f3d4e388abeabb2e5087b71735e9de8b49a63df914

The live renderer/runtime match the exact copies in the v5 build record. The guard/lifecycle review passes; this report does not claim that the three preserved old munder nodes became valid.
