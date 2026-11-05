# Mobile reader candidate and QA handoff

5 November2026. All repository reads, edits, builds and browser tests in this work ran through SSH on iska-linux-vscode. No production promotion, package installation, authentication, MCP activation, deletion or cache mutation was performed. Root owns promotion, main book documentation and publication.

## Reproduction and root cause

The pinned37chapter baseline and native-v2 both reproduce the same real page overflow in isolated Firefox BiDi9335: innerWidth390, clientWidth378, scrollWidth799. The12px difference between inner/client is Firefox's vertical scrollbar and is not overflow. Hiding the three added chapters leaves scrollWidth799. Evidence is retained in native-browser-diagnosis-v1/v2/v3.

Some native display MathML boxes have a350px CSS box but785px intrinsic scroll width. Firefox exposes their math content outside that box even with MathML overflow-x:auto. The old fitReaderMath measures only getBoundingClientRect().width, so misses constrained display formulas. The old table wrappers work correctly. A one-variable diagnostic wrapped only actually overflowing math in HTML scroll containers, reducing the full page scroll799to378 without scaling or clipping formulas.

The additive reviewed-math-scroll.js tests max(scrollWidth,bounding width), respects numbered equations' narrower grid cells, and creates focusable HTML scroll containers only where needed. Its CSS gives those containers min-width0/max-width100%/overflow-x:auto. Math contents, attributes and font sizes stay untouched. The renderer adds the new asset/style/script only within its fully reversible supplement insertion. The complete old HTML/runtime remains unchanged except the two already authorized old prose corrections. No body/root overflow hiding is used.

## Final evidence

Candidate: outputs/book-integration-20261104/native-v3. PDF remains accepted v4/main.pdf. Final browser report and screenshots: outputs/checks/2026-11-04-weighted-moment/native-browser-v9. The browser session ends in finally; its ephemeral loopback HTTP server also shuts down/closes/joins. Port9335is released.

The complete browser suite passes320/390/768/1440and390again, with document scrollWidth equal clientWidth at each size. At390the old page is378/799and candidate378/378. At320the candidate is308/308. Equation40.4 retains18px native math in a302px viewport with672px scrollable content. Every overflowing HTML equation/table container can scroll to its end, has tabindex0 and an accessibility label. Light and scrolled screenshots differ. All5356old MathML,384old tables and13iframe browser DOM subtrees match the baseline hashes exactly. The6216total math count,13unique frames, labels/references, actual reference click, three exact source downloads and PDF download pass.

The original night screenshot in v7was taken during the shared theme's2100ms background transition. No theme CSS was changed. The final harness waits until actual computed body background/ink, section ink and math ink settle. Final night background isrgb(7,13,20), body/math inkrgb(210,225,230), math18px, base-color contrast14.537915:1, page378/378. Root should inspect v9/weighted-envelope-mobile-night.png. This computed contrast uses the base body background; the preserved atmospheric layers remain a visual-review concern.

Three malformed old TeX4ht munder nodes for lim-leftarrow have three children. They are identical in the pinned baseline and candidate. Reflows repeat Firefox's existing invalid-markup diagnostic. There are zero such malformed nodes in the860new expressions and no new distinct browser diagnostics. These inherited diagnostics are recorded separately, not reported as zero total browser errors.

The unchanged independent semantic checker passes against native-v3: native-browser-v7/fidelity.json. It verifies exact source preservation,19diagram relations, old45chapter files, reversible HTML insertion, chapter order1..40,860MathML/AST annotations,33labels and aux numbering. Fresh wrapper reproduction-v2includes the runtime automatically; reproduction-comparison.json verifies byte-identical native HTML/runtime and byte-identical extracted PDF layout text relative to accepted v4. The rebuilt PDF remains233pages/40chapters/19diagrams.

Previous namespaces are preserved: v3QAfailed because the test treated wc:uniform's theorem as equation40.4; v4failed because the reference hash was read before asynchronous navigation settled; v5failed on inherited baseline MathML diagnostics before they were identified separately; v8failed due a QA selector escape. v6/v7passed the earlier suite; v9passes the final suite including settled night contrast.

## Root promotion handoff

Exact source/target paths, bytes, hashes and current-target guard hashes are in native-browser-v9/promotion-plan.json. Only main.html, the new runtime and12new source assets differ from existing native assets; avoid copying the whole candidate directory over unrelated progress. Existing PDF/log/toc targets are listed separately. The optional proposed-build-remote-book-candidate.py may be copied to scripts/build_remote_book_candidate.py; retain its three planning helpers at their recorded paths. The fresh reproduction demonstrates this wrapper includes reviewed-math-scroll.js.

The existing public-site builder uses git ls-files, so the new runtime and12source files must be explicitly staged before root builds a fresh publication bundle. It already maps outputs/book/surface-orders-book.pdf to bundle/book.pdf. No production promotion or publication was performed by this worker.
