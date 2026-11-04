# Mobile reader containment review — 2026-11-03

Read-only independent review of `scripts/prepare_book_html.py` lines 65–113, its generated reader CSS, the generated HTML table/MathML structure, and the saved mobile/preservation reports. Scope is book HTML layout, preservation, accessibility, and performance; mathematical claims are outside this review. No application edits, browser launch, dependency install, configuration change, authentication, staging, or commit was performed.

**Result: no blocking finding in the reviewed change.**

The HTMLParser computes insertion offsets in the original Unicode source, including exact line starts. Applying edits in descending offset order preserves subsequent offsets. Wrapping only depth-zero tables preserves each complete nested table subtree and its MathML, IDs, captions and equation numbers; it does not serialize or rewrite those subtrees. The second XML parse rejects malformed output before writing the book. The global existing-wrapper guard makes the current complete generated output idempotent; it assumes a fresh all-unwrapped TeX4ht build or an already fully wrapped edition, not a mixed partially wrapped input. That assumption matches this build.

The runtime pass first measures candidates, then mutates them, avoiding repeated read/write layout thrashing within the scan. It moves the existing native MathML element into a scroll span and leaves its internal content and semantics intact. It skips already contained tables/expressions, handles fonts becoming ready and hidden details becoming visible, and uses the parent content width after padding. The current corpus contains no nested `<math>` elements, so precollecting candidates does not produce nested expression wrappers. The inline wrapper's max-width and horizontal overflow contain the equation while preserving access to the complete expression. Existing wrappers remain harmless after resizing to a wider viewport.

Generated HTML independently parsed as XML: **323 table elements, 323 scroll wrappers, 4,541 MathML elements**; every outer table is contained, every scroll wrapper has one table child, and no nested math was found. `outputs/checks/2026-11-03-hecke-type-i/math-preservation.json` separately reports all 323 table subtrees unchanged, ignoring exterior tails moved outside the wrapper. This reviewer inspected that result rather than rerunning the book build.

The saved `browser.json` and `mobile-layout-probe.json` report **390px inner width, 390px document client width and 390px document scroll width**, with no browser exceptions. Comparing against client width checks the mobile auto-shrink failure that a scrollWidth-versus-innerWidth assertion could miss. A long MathML child still has a wider bounding box in the probe; it is inside its intentional scroll viewport, so that is expected and does not imply document overflow. Browser execution and screenshot assessment were performed by the parent; this reviewer did not access the reserved CDP port.

Two nonblocking observations remain explicit:

1. All 323 tables receive `tabindex="0"`, even tables that fit. This preserves keyboard access to horizontal scrolling but adds tab stops through a long book. Conditional focusability for overflowing tables could reduce keyboard effort in a separate accessibility pass. Native table/MathML descendants and visible focus outlines remain available.
2. `fitReaderMath` scans the 4,541 MathML elements for each captured details toggle and schedules a scan for every resize event. requestAnimationFrame schedules work but does not coalesce queued resize callbacks. The scan skips contained tables early and batches writes, which limits cost here; measured performance should determine whether future event coalescing or targeted scans are warranted. This is not a demonstrated regression in the passing current mobile check.

The parent's planned heading `scroll-margin-top` addition addresses fixed-navigation anchor visibility and does not change the containment algorithm. Final heading offset/rebuild verification remains with the parent.

Reviewed snapshot SHA-256 values (before any final heading-only CSS addition):

- `scripts/prepare_book_html.py`: `b24e19db379e388515e0daaed7dc7a4475aae165a5ac9ede06f08823d3a71649`
- `web/book/reader.css`: `9eceb875dc3a24bac9f1e110a509b08f869f737e46f30219e439bb15c9bcbb45`
- `web/book/main.html`: `2523c251b4fa0ac937bfb00170987f85db2cf336f64afcfa82172e8ae8f482a5`
