# Static companion verification

Date: 13 November 2026. This report records the site author’s checks before final integration. Subsequent deployment checks, if performed, should be recorded separately.

## Completed

The six mathematical labs passed the executable tests in `extension/site/verify-math.cjs`. The elliptic-curve model contains 19 points and all 6,859 associativity triples were checked. The cone residual was at most 1.67 × 10⁻¹⁶ on the sample grid; the Fourier off-support probability was at most 2.18 × 10⁻³⁴; gauge holonomy changed by at most 4.48 × 10⁻¹⁶ under the sampled local gauge transformations; torus seams matched to 6.62 × 10⁻¹⁶. These are checks of finite models and floating-point implementations, separate from the Lean proof inventory.

JavaScript syntax and CSS parsing passed. Static DOM checks found 102 unique IDs, 22 labelled native controls, 19 range controls paired with output elements, 8 labelled visual elements, 2 keyboard-focusable interactive canvases, and 14 valid internal fragments. The site has no automatic animation or external runtime dependencies. Keyboard accessibility was checked structurally; actual keyboard interaction was not exercised in a browser by this reviewer.

## Rendered checks blocked

The browser plugin could not initialize because the originating browser context was unavailable. The parent-authorized local headless fallback failed before loading a page: Chromium could not create its process-singleton socket (`Operation not permitted`). No screenshots, console inspection, responsive overflow measurements, computed reduced-motion checks, URL-history interaction tests, or live control tests were completed by this reviewer. No repeated permission or browser-runtime workaround was attempted after the parent’s instruction to stop.

The root workstream is responsible for inspecting the published companion and recording those results separately. Missing download and inherited-material links at the time of this snapshot were integration work, not mathematical lab failures. The machine-readable report `site-static-qa.json` contains exact values and source hashes for this snapshot.
