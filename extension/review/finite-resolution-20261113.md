# Finite resolution, nonlinear residuals and laboratory scope

**Release date:** 13 November 2026, America/Los_Angeles. Machine records use explicitly labeled UTC timestamps, which may fall on 14 November.

**Status:** Three analytic-family diagnostics, an independent high-precision reference generator, a numerical verifier and an isolated UI helper are implemented. Focused numerical and DOM-behavior checks passed. Those DOM checks do not claim a rendered browser or assistive-technology audit.

The complete written arguments are in **extension/manuscript/chapters/finite-resolution.tex**; the new bibliography is **extension/manuscript/finite-resolution-sources.bib**. These are project-specific derivations for the declared models. The primary sources supply context and arithmetic semantics, not an external proof of the combined software.

## 1. Error categories

| Category | Evidence supplied here | What remains outside it |
|---|---|---|
| Analytic truncation | Real-arithmetic bounds with field, smoothness, grid and step hypotheses | An interval enclosure of every JavaScript operation |
| Observed convergence | Named refinements, including unfavorable rates | A proof inferred from a fitted slope |
| Rounding | Explicit heuristic scales; retained cancellation and underflow | A uniform verified math-library bound |
| Finite volume | Periodic diffusion generator gap as a function of box and grid size | An infinite-volume mass-gap theorem |
| Model discrepancy | Declared initial data, period and local curvature family | Error of an arbitrary measured fluid or quantum field |
| Exact structure | Existing rational/integer contracts and the scalar square-error lemma | A continuum interpretation of a finite-field toy or display mesh |

The live panels have independent labeled parameters. They do not silently inherit animation state, point/peak initial data, or the old gauge flux slider.

## 2. API and domains

The file **extension/site/finite-resolution-core.js** exports **ResolutionMath** in a browser and the same API through CommonJS.

| Function | Default options | Returned comparison |
|---|---|---|
| taylorGreenDiagnostics | n=16, time=1.5, nu=.08 | Actual centered derivatives, curl/Laplacian/nonlinear residual bounds and exact-family energy quadrature discrepancy |
| heatModeDiagnostics | n=16, nu=.08, time=1, modeX=1, modeY=0; optional steps | Discrete/semidiscrete/continuum amplitudes, separate spatial/time errors, actual one-step kernel check and generator gaps |
| u1PlaquetteDiagnostics | n=1, curvature=1, quadratic=0 | Exact local flux, raw existing Wilson action, stable action, averaging/small-angle bounds and phase aliasing |
| convergenceStudy | Family name, options object, optional increasing levels | Error rows and observed rates, withheld at rounding scale or underflow |

Taylor–Green requires integer \(5\le n\le128\), resolving velocity harmonic 1 and pressure harmonic 2 strictly below Nyquist. Heat accepts integer \(4\le n\le128\), integer mode components with \(|k_x|,|k_y|<n/2\), and CFL ratio in \([0,1/4]\). Zero time requires zero steps; positive time requires a positive count. U(1) accepts integer \(1\le n\le65536\). Nonfinite values, malformed options and invalid domains fail closed. Resource limits are explicit; an automatic step count exceeding the permitted limit is rejected before grid computation.

Each row records **boundStatus = analytic-real-arithmetic-not-an-interval-certificate**, **roundingStatus = heuristic-not-a-certified-roundoff-bound**, an **errorStatus**, and an **observedOrder** that is null when unresolved. The first row also has no two-level rate.

The UI file **extension/site/finite-resolution-ui.js** autoloads containers with **data-resolution-lab** set to **taylor-green**, **heat-mode** or **u1-plaquette**. Its **ResolutionUI.mount** and **mountAll** functions return panels with controls, refresh(), and getReport(). An invalid edit clears the previous table and displays the domain error.

## 3. Taylor–Green: derivatives and nonlinear consistency

For \(a=e^{-2\nu t}\), the existing solution is
\[
u=a\sin x\cos y,\quad v=-a\cos x\sin y,\quad
p=\frac{a^2}{4}(\cos2x+\cos2y).
\]
The periodic box has side \(2\pi\), with \(h=2\pi/n\). Centered first differences multiply a Fourier derivative by \(\operatorname{sinc}(kh)\). The velocity Laplacian eigenvalue magnitude is \(\lambda_h=8\sin^2(h/2)/h^2\). The derived maximum component bounds are
\[
E_{\rm curl}\le ah^2/3,\qquad E_{\Delta}\le ah^2/6,\qquad
\|R_h\|_\infty\le\nu ah^2/6+a^2h^2/4.
\]
The time derivative remains analytic. The nonlinear residual includes the different discrete multipliers of advection and pressure. Discrete divergence cancels exactly in real arithmetic for this family.

Energy quadrature equals \(a^2/4\) exactly in real arithmetic because its nonconstant Fourier terms have zero discrete average on the admitted grids. The actual floating discrepancy is still reported. This finite Fourier identity is proved directly; [S2] provides broader aliasing context.

This is sampling and differentiation of a known solution. A stability theorem and compatible norms would be needed to convert the residual into a trajectory error. No time-marching Navier–Stokes solver or regularity theorem is introduced.

## 4. Heat: fixed time, separated errors and finite box

For nonzero mode \(k\), the smooth probability stripe is
\[
p^0_{j\ell}=\frac{1+\frac12\cos(k_xjh+k_y\ell h)}{n^2}.
\]
The zero mode is uniform. The existing heatStep is used directly. Define
\[
\lambda=|k|^2,\quad
\lambda_h=\frac4{h^2}\sum_{\alpha=x,y}\sin^2(k_\alpha h/2),\quad
x=\nu\Delta t\lambda_h .
\]
At fixed \(T=m\Delta t\), the amplitudes are \((1-x)^m\), \(e^{-\nu T\lambda_h}\), and \(e^{-\nu T\lambda}\). The separate bounds are
\[
B_s=\min\{1,\nu T h^2(k_x^4+k_y^4)/12\},\qquad
B_t=\min\{2,mx^2/2\}.
\]
Their sum, capped at 2, bounds total amplitude error. A telescoping power difference proves the time estimate even for an admissible negative multiplier \(1-x\). Positivity of the full translation channel and positivity of one Fourier multiplier are different conditions.

The default count is \(\max(1,\lceil5\nu T/h^2\rceil)\) at positive time, keeping the same final time and CFL at most \(1/5\). The original point and peak fixtures have grid-index widths and are not claimed to define this fixed smooth continuum family.

Retained default errors at \(n=8,16,32,64\) are approximately \(9.12\cdot10^{-4}\), \(3.26\cdot10^{-5}\), \(3.12\cdot10^{-5}\), and \(1.10\cdot10^{-5}\), with rates \(4.805,0.067,1.501\). Spatial under-diffusion and Euler time error partly cancel. The separate budgets remain visible; the sequence is not selected to produce a preferred rate.

For physical side length \(L\), the smallest positive heat-generator eigenvalue is \(g_L=\nu(2\pi/L)^2\). The grid value is
\[
g_{L,n}=\frac{4\nu\sin^2(\pi/n)}{(L/n)^2},\qquad
0\le1-g_{L,n}/g_L\le\pi^2/(3n^2)
\]
for \(\nu>0\). The UI reports both at \(L=2\pi\), with deficit bound \(\nu h^2/12\). At \(\nu=0\) both are zero. These are generator gaps, not guaranteed absolute mixing gaps for every discrete-time channel. Refining \(n\) at fixed \(L\) tends to a positive box gap; increasing \(L\) sends that continuum gap to zero. This supplies no infinite-volume Yang–Mills mass gap.

## 5. U(1): local curvature and small-angle error

The family declares a centered cell of side \(h=1/n\) inside a unit-square patch:
\[
B(x,y)=B_0+\kappa(x^2+y^2),\quad
\overline B_h=B_0+\kappa h^2/6,\quad
\Phi_h=h^2\overline B_h .
\]
Its flux is exact, without edge quadrature. The original gaugePlaquette provides the four-link product and raw action. The normalized density \(Q_h=2(1-\cos\Phi_h)/h^4\) is also evaluated as \(4\sin^2(\Phi_h/2)/h^4\), and compared with the central value \(B_0^2\).

If \(|\overline B_h-B_0|\le d\), the written bound is
\[
|Q_h-B_0^2|\le d(2|B_0|+d)+h^4(|B_0|+d)^4/12.
\]
For the implemented field, \(d=|\kappa|h^2/6\). A smooth local field with bounded pure second derivatives admits \(d=h^2(M_{xx}+M_{yy})/24\), from two midpoint estimates. Those derivatives are not inferred for arbitrary data. Constant curvature gives an \(O(h^4)\) bound; variation generally introduces \(O(h^2)\).

The scalar implication
\[
|e|\le d\ \Longrightarrow\
|(B_0+e)^2-B_0^2|\le d(2|B_0|+d)
\]
is freshly kernel-checked as **LaboratoryContracts.square_perturbation_bound**, with Lean 4.24, zero warnings and the disclosed standard foundational axioms. It supports only the square-error component of **prop:fr-local-wilson-bound**, not smoothness, integration, trigonometry or floating arithmetic. Its source and printed type are in the canonical formal manifest.

The loop still records flux only modulo \(2\pi\). The retained coarse fluxes \(8\) and \(8+2\pi\) have the same Wilson quantity and different unwrapped targets. This is an Abelian classical local calculation, motivated by [S1], not a non-Abelian quantum continuum construction.

The raw subtraction loses significance at small flux. At \(B_0=1,\kappa=0,n=65536\), its binary64 density is 0 and the stable density rounds to 1. The high-precision reference retains the positive deficit, about \(4.52\cdot10^{-21}\). Stable zero numerical error is marked unresolved. The raw heuristic rounding scale grows like machine precision divided by \(h^4\); it is not a certified bound. The transcendental semantics in [S3] also require keeping real-arithmetic bounds distinct from evaluated values.

## 6. Formal and control connections

| Manuscript label | Coverage |
|---|---|
| prop:fr-taylor-green | Written Fourier/Taylor proof and actual numerical kernel checks; no Lean coverage claimed |
| prop:fr-energy-quadrature | Written finite Fourier proof and compensated numerical sum |
| prop:fr-heat-mode | Written spatial/time proof, actual one-step and repeated heat kernel checks |
| prop:fr-local-wilson-bound | Written local-field/trigonometric proof; only scalar square perturbation is Lean-checked |

Exact topological invariants and rational certificates retain their meaning under display refinement. An exact finite-field example is not a mesh approximation to a continuum field.

The chapter gives a conditional nonlinear stability connection: a Lipschitz reference ODE and integrable residual yield an exponentially weighted trajectory bound on a common controlled region. The manufactured residual alone supplies neither that region nor a PDE stability estimate.

For a \(q<1\) contraction, a **uniform** one-step error \(\eta\) gives \(e_m\le q^m e_0+(1-q^m)\eta/(1-q)\). Spatial, time, arithmetic and physical errors can enter only in compatible norms under explicit hypotheses. A single Fourier-mode error is not a uniform state-space error; a rounding heuristic is not a certified summand. The separate workbench chapter owns the finite probability and runtime certificate return paths.

## 7. Evidence and negative controls

The independent generator **extension/code/build_finite_resolution_reference.py** uses mpmath 1.3.0 at 80 decimal digits. Scalar/spectral formulas include an independently evaluated nonlinear residual symbol. The fixture keeps longer decimal strings and binary64 comparison values. It never calls the JavaScript implementation.

The numerical verifier has 11 groups: 24 high-precision reference cases, 24 sampled-flow grid cases, 36 heat-budget cases, and 23 rejected inputs, plus repeated heat evolution and gauge comparisons. Largest retained reference discrepancies are approximately \(4.98\cdot10^{-15}\), \(1.11\cdot10^{-15}\), and \(2.57\cdot10^{-16}\) for flow, heat and U(1). Numerical allowances are explicit; none is interval certification.

Retained controls include:

- pressure underresolution, Nyquist aliases, unstable CFL, inconsistent time/step counts, nonfinite values and malformed option objects;
- an admissible negative Fourier multiplier, distinct from instability;
- heat cancellation and irregular total-error rates;
- raw U(1) cancellation and withheld stable rates;
- coarse phase aliases, zero fields, zero time and underflow.

The UI verifier has eight groups using a minimal in-memory DOM fixture. It checks labels, captions, status messages, event updates, invalid-result clearing, recovery, and numerical-limit messages. Browser layout, keyboard and screen-reader checks are separate work.

Reproduce from the repository root:

~~~sh
python3 extension/code/build_finite_resolution_reference.py
node extension/site/verify-finite-resolution.cjs
node extension/site/verify-finite-resolution-ui.cjs
~~~

Canonical records are **extension/verification/finite-resolution-node.json**, **extension/verification/finite-resolution-ui.json**, and **extension/lean/final-verification/verification.json**. Numerical receipts hash the inspected source and reference files; the reference fixture also hashes its generator. The page links the numerical receipt and this note without presenting a floating calculation as a Lean instance.

## 8. Primary sources and actual reading scope

This was a bounded review for the new diagnostics, not a renewed whole-project literature review. No full paper or transcript is copied into the repository.

**[S1] Kenneth G. Wilson (1974), “Confinement of quarks,” Physical Review D 10, 2445–2459.** DOI: [10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445). Read the [publisher abstract and metadata](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.10.2445), and selected Section III.A text, pp. 2448–2449, in an [academic-hosted scan](https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/Rabinovici/Wilson.pdf). It distinguishes lattice gauge invariance and classical small-spacing reasoning from the quantum continuum problem. Equation OCR is imperfect; the U(1) formulas above are independently derived. No complete-paper reading claim. BibTeX key: **frWilson1974**.

**[S2] Lloyd N. Trefethen and J. A. C. Weideman (2014), “The Exponentially Convergent Trapezoidal Rule,” SIAM Review 56(3), 385–458.** DOI: [10.1137/130932132](https://doi.org/10.1137/130932132). Read title/abstract and the Fourier-series/aliasing portion of Section 3, pp. 394–396, especially (3.1)–(3.12), in the [author-hosted paper](https://people.maths.ox.ac.uk/trefethen/publication/PDF/2014_149.pdf). Used for quadrature context; the project's finite energy identity is proved directly. No general exponential-convergence claim for arbitrary lab data. BibTeX key: **frTrefethenWeideman2014**.

**[S3] Ecma International / TC39, ECMAScript living language specification.** Read the official [Math.cos](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.cos), [Math.exp](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.exp), and [Math.sin](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.sin) clauses, sections 21.3.2.12, 21.3.2.14 and 21.3.2.31, on 14 November 2026 UTC. The page is labeled ECMAScript 2027; it is a living draft, not evidence that a future edition was finalized. These clauses specify implementation-approximated transcendental values. BibTeX key: **frECMAScriptLiving**.
