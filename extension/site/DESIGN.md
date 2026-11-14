# Interactive research companion: technical and scientific contract

## Analytical job and reading path

This is an explanatory research page with small exploratory mathematical laboratories. The reading path is: scope of the synthesis; current evidence status; six explicit constructions; source and proof boundaries; downloadable monograph and code. The visuals compare changes of structure and distinguish algebraic identities from analytic conclusions.

The primary rendering route is native Canvas2D for projected three- and four-dimensional wire geometry, plus SVG/HTML for finite plots, labels, tables, matrices, and controls. Three geometric canvases are visible in the document, including a static hero preview; only controls or resize trigger redraws. No external runtime, CDN, generated image, autoplay, or network data is needed. A static local HTTP server is sufficient. The fallback is the adjacent equations, state summaries, and complete finite tables.

## Six laboratory contracts

1. **Complex torus.** A point with real coordinates `(u,v)` represents `u+vτ mod (Z+Zτ)`. The three-dimensional torus is a topological visualization of identified sides. Its embedding is deliberately independent of τ; the parallelogram and displayed Gram matrix carry τ's flat metric. It is not a conformal or isometric embedding of that flat metric.
2. **Four-dimensional complex variety.** The equation is `x·y=0` in `R²×R²`. The unit link is parameterized through equal-length u and v vectors. Ambient rotations and projection are viewing operations; residuals and ranks are calculated in original coordinates before viewing transforms. The radius control includes the cone vertex. A projected crossing is not an intersection certificate.
3. **Finite elliptic curve.** Exact integer arithmetic modulo 17 enumerates `y²=x³+2x+2`. The point `(5,1)` generates nineteen points including infinity. A slider selects its multiple. Plot positions represent residues, not a real cubic; the finite-field chord formulas are stated separately. All nineteen values are available as text.
4. **Fourier annihilator.** The exact model is a uniform kernel-coset state for `f(a,b)=a+d b mod 7`. The probability at `(u,v)` is computed from the finite complex sum, with support `v=d u mod 7`. This is a classical numerical model of the Fourier step, not execution on quantum hardware or a resource estimate.
5. **Hodge operator.** The complex has `d₀=(ε,0)ᵀ`, `d₁=(0,1)`, so `Δ₁=diag(ε²,1)`. Euler index stays zero while the least eigenvalue tends to zero. At ε=0 the kernel dimension changes, and the smallest strictly positive eigenvalue returns to one; the distinction is explicit. This finite example supplies no Yang–Mills mass-gap estimate.
6. **Gauge plaquette.** Four U(1) edge phases transform by vertex-phase differences. The product around the cycle is invariant. A displayed complex residual checks the floating-point calculation. The exact cancellation proof is stated in text. A single compact-group plaquette does not establish a continuum quantum field theory.

## Interaction, state, and accessibility

Native range and select controls provide the authoritative state. Geometric canvases have optional mouse drag and keyboard arrow rotation; sliders provide the same actions without dragging. Touch scrolling remains native. No essential value requires hovering or color. Teal indicates the first family or invariant, ochre marks the second family or selected point, and neutral grey supplies context. Dashed lines and labels distinguish families in monochrome.

The `Share current view` control encodes all laboratory parameters in the query string; URL values are bounded and validated. Reset clears the query. Browser history navigation restores the same controls and text summaries. No persistent storage is required. Canvas dimensions follow their CSS rectangles at DPR capped at two; text and controls use the DOM. The mobile layout stacks display before controls, preserves all scientific caveats, and uses controls at least 44 CSS pixels high. Canvas may be rendered at a reduced backing scale without changing mathematical samples.

## Performance and maintenance

The two interactive geometry displays use roughly 1,500–3,000 segments each, with depth ordering and direct perspective projection. No GPU context is necessary at this scale. A geometric canvas at 700×380 CSS pixels and DPR 2 costs about 4.3 MB of backing memory. The hero preview is smaller. Resize is scheduled through requestAnimationFrame. No idle animation loop runs.

`math.js` owns mathematical definitions and exact modular calculations. `app.js` owns state, SVG/Canvas rendering, and interaction. `index.html` owns scientific prose and accessible structure. `styles.css` owns responsive presentation. Parent integration supplies final download artifacts, repository URL, and the actual Lean build evidence; the interface never fabricates a declaration count.

## Verification

Meaningful mathematical checks cover enumeration and all group-operation cases for the nineteen-point curve; annihilator support and total probability for all seven hidden slopes; original-coordinate cone residuals and rank-degenerate cases; the Hodge eigenvalue distinction at zero; and gauge holonomy invariance. Browser QA should inspect desktop and mobile screenshots, keyboard controls, current-view sharing/back navigation, no horizontal overflow, download links, reduced-motion behavior, and console errors. The research page labels numerical checks separately from prose proofs and selected Lean proofs.
