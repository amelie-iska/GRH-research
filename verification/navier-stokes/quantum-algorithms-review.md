# Quantum fluid algorithms: independent primary-source review

Review date: 13 November 2026. Scope: the exact cached versions identified below. All 129 PDF pages were read, including appendices, figure captions, tables, and references. Selected pages were additionally rendered to resolve mathematical notation and inspect the numerical figures. This is a mathematical and resource-accounting review; it does not claim reproduction of the papers' numerical experiments, execution on quantum hardware, verification of every numerical matrix entry, or review of every work in their bibliographies.

## Overall finding

These sources support useful, precisely delimited methods: finite Carleman lifting, structured tensor representations, collision/streaming algebra, block encodings, and explicit accounting for conditioning and measurement. They do not supply a proof of three-dimensional Navier–Stokes regularity or singularity, a general convergent quantum fluid solver, or a demonstrated hardware advantage for the project's examples. Several printed formulas require correction before they can be used as executable interfaces. The counterexamples and finite repairs below are independent algebraic checks, not claims that the underlying research programmes are impossible.

The project should retain its independently proved finite interfaces and its explicit contractivity assumptions. It should describe the computational laboratory as a classical simulation of the stated finite circuits and channels. Neither its two-qubit circuit nor its toric-code examples inherit a fluid-solving advantage from these papers.

## Provenance and exact coverage

| Source | Reviewed version | PDF pages read | Additional rendered pages |
|---|---|---:|---|
| Liu et al., *Efficient quantum algorithm for dissipative nonlinear differential equations* | [arXiv:2011.03185v4](https://arxiv.org/abs/2011.03185v4), 7 July 2026; original PNAS article 2021 | 1–36, all | 4, 7, 14, 33 |
| Gourianov et al., *A Quantum Inspired Approach to Exploit Turbulence Structures* | [arXiv:2106.05782v3](https://arxiv.org/abs/2106.05782v3), 4 July 2022 | 1–36, all; main text 1–11, supplement 12–36 | 3, 6, 29, 32, 33 |
| Jennings et al., *An end-to-end quantum algorithm for nonlinear fluid dynamics with bounded quantum advantage* | [arXiv:2512.03758v2](https://arxiv.org/abs/2512.03758v2), 25 September 2026; PRX Quantum 7, 033060 | 1–57, all | 11, 21, 24, 27, 29, 42, 52 |

Cached source directory: `research/navier-stokes/structures/` in the session workspace. Exact PDF SHA-256 values:

```text
liu2021.pdf
bc3c70f16eab86ea3cef8d15f56fd2f74027299659343b1820e8aaf2b4d2dc17
gourianov2022.pdf
6d04e74070f7603fafde85e241e9229fb87613d30548aa0d0c0d6f5ec71c90ce
jennings2026.pdf
902baecfdf3fbe18ee459f785ff57e49432eba8b99ffb13a3b8fd9dbc5408434
```

The companion JSON records PDF sizes, extracted-text hashes, page lists, findings, and source URLs. The full-read claim refers to these versions and these files. It does not extend to the separate Jennings boundary/driving companion, arXiv:2512.05781, or the articles cited for individual quantum subroutines.

### Coverage ledger

| Source pages | Material examined |
|---|---|
| Liu 1–4 | Motivation, norm convention, oracle problem, diagonalizability and dissipation assumptions, rescaling |
| Liu 5–12 | Carleman blocks, main complexity theorem, norm comparison, truncation estimates, homogeneous special case |
| Liu 13–18 | Euler error, contractivity argument, condition number, lifted input preparation |
| Liu 19–25 | Forcing preparation, postselection, main theorem proof, worst-case hardness setup |
| Liu 26–32 | Hardness proof, SEIR and Burgers examples, applications and limitations |
| Liu 33–36 | Correction acknowledgment and complete references |
| Gourianov 1–11 | Interscale Schmidt diagnostics, TDJ/TGV experiments, finite-difference/MPS algorithms, costs, data/code statements, references |
| Gourianov 12–21 | Supplement front matter, Schmidt spectra/entropy, MPS parametrization and gauges, classical versus quantum interpretation |
| Gourianov 22–26 | Hopf–Cole solution, special Burgers hump, exact Heaviside and triangular-wave tensor representations |
| Gourianov 27–31 | Variational problem, local SPD solves, sweeps, operation counts, CPU timing, arithmetic intensity |
| Gourianov 32–36 | Proposed variational quantum port, circuit diagram, tensor notation, supplementary references |
| Jennings 1–10 | Claimed contributions, LBE/DBE distinction, earlier complexity bottlenecks, norm/readout problem |
| Jennings 11–20 | Shifted ILBE, parameter scaling, discrete lifting, history/final-state systems, block-encoding summary, preparation and extraction |
| Jennings 21–30 | Finite convergence experiments, condition-number estimates, fitted exponents, gate estimates and limitations |
| Jennings 31–40 | Notation; cubic DBE; exact collision-only closure; block-encoding definitions, LCU proofs and circuits |
| Jennings 41–50 | Collision encodings, QLS normalization, parameter tables, invariant eigenvectors, norm bounds, gate-cost derivation |
| Jennings 51–57 | Explicit small collision matrices, dilation and state-preparation costs, synthesis proof and complete references |

## 1. Liu: revised assumptions and the Euclidean energy issue

### 1.1 The correction predates the July arXiv revision

The publisher's correction was released electronically on **20 May 2026**, with issue date **26 May 2026**. The arXiv revision incorporating it is dated **7 July 2026**. The primary correction is [PNAS DOI 10.1073/pnas.2615307123, full text at PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13213974/).

It adds the condition `||F0|| <= ||F2||` to the affected convergence statements, separates a previously conflated error quantity, changes the diagonal-dominance argument to the Hermitian part `G + G†`, and changes the SEIR parameter example to satisfy the added condition. ArXiv v4 acknowledges the change on p. 33; its numbering calls the affected truncation result Lemma 2, whereas the publisher's supporting-information correction calls it Lemma 1. These are different numbering systems, not two independent corrections.

The manuscript should say “May 2026 publisher correction, incorporated in the July 2026 arXiv revision.” An unqualified citation to the 2021 theorem misses an assumption in the reviewed revision.

### 1.2 What the stated algorithm is designed to return

The problem is a finite quadratic ODE

\[
\dot u=F_2(u\otimes u)+F_1u+F_0(t),
\qquad
R=\frac{\|u_0\|\|F_2\|+\|F_0\|/\|u_0\|}{|\operatorname{Re}\lambda_1|}.
\]

Pages 3–6 specify spectral/Euclidean norms, sparse access to coefficients, initial-state preparation, known bounds including forcing derivatives, and a diagonalizable linear part with negative-real-part spectrum. Theorem 1 states its favorable result for `R < 1` and the added forcing condition. It produces a normalized state approximating `u(T)/||u(T)||`, with a success flag, rather than all classical coordinates of `u(T)`.

The stated cost retains substantial dependencies beyond logarithmic dimension: sparsity; evolution time; error; coefficient and forcing-derivative norms; the rescaled initial norm's distance from one; the final norm `g = ||u(T)||`; and `q = ||u0||/g`. In particular, the detailed theorem has a `1/g` dependence in addition to its displayed `q` factor. The abstract's compact expression must not be interpreted as uniform in these parameters. Homogeneous dissipative examples can incur exponentially bad final-norm overhead; the authors explicitly explain this on pp. 27 and 31–32.

Preparing the lifted initial data uses multiple initial-state preparations; generic time-dependent forcing preparation is not free (pp. 18–19). With final-time padding, the postselection analysis gives success of order `1/(N q²)` for truncation degree `N`, leading to amplitude-amplification overhead of order `sqrt(N) q` (pp. 19–23). Page 32 explicitly leaves end-to-end readout to subsequent algorithms. The Burgers experiment at `R ≈ 43.59` is a classical computation with small truncation orders; it does not prove convergence outside the sufficient theorem regime (pp. 29–32).

### 1.3 A separate printed estimate fails for nonnormal matrices

**Finding L1 — exact counterexample; high confidence.** Equation (4.2), p. 7, bounds the linear energy contribution using the largest real part of an eigenvalue:

\[
u^T(F_1+F_1^T)u\le2\operatorname{Re}(\lambda_1)\|u\|^2.
\]

Mere diagonalizability does not imply this Euclidean estimate. The complete paper contains no convention first conjugating into an eigenbasis and then taking all norms in that basis. Its rescaling on pp. 21–23 is scalar and leaves `F1` unchanged. The SEIR application on p. 28 even uses a triangular, generally nonnormal matrix directly.

For a counterexample satisfying the printed problem assumptions and the added forcing inequality, take

\[
F_1=\begin{pmatrix}-1&4\\0&-2\end{pmatrix},\quad
u_0=\begin{pmatrix}1/2\\1/2\end{pmatrix},\quad
F_2=\begin{pmatrix}1/100&0&0&0\\0&0&0&0\end{pmatrix},\quad
F_0=\begin{pmatrix}1/1000\\0\end{pmatrix}.
\]

The eigenvalues are distinct, `-1,-2`; the matrices are sparse; `||u0|| = 1/sqrt(2) < 1`; `||F0|| <= ||F2||`; `||F2|| + ||F0|| = 11/1000 < 1`; and

\[
R=\frac{3\sqrt2}{500}<1.
\]

Direct differentiation gives

\[
\left.\frac{d}{dt}\|u(t)\|^2\right|_{t=0}
=2u_0^T\bigl(F_1u_0+F_2u_0^{\otimes2}+F_0\bigr)
=\frac{1007}{2000}>0.
\]

The proposed right-hand side of (4.2) is instead

\[
2\|F_2\|\|u_0\|^3+2\operatorname{Re}(\lambda_1)\|u_0\|^2
+2\|F_0\|\|u_0\|=-1+\frac{3\sqrt2}{500}<0.
\]

The claimed monotonic norm conclusion in Lemma 1 therefore fails for this stated instance. This is an objection to the printed assumptions/estimate, not a refutation of normal-matrix special cases or of a suitably repaired algorithm.

A valid Euclidean bound uses the numerical abscissa

\[
\mu_2(F_1)=\lambda_{\max}\!\left(\frac{F_1+F_1^*}{2}\right),
\]

or an explicitly proved semigroup estimate. A weighted Lyapunov norm is another possible route, but it changes the norms of the nonlinear and forcing terms and introduces transformation/conditioning costs. Those costs cannot be silently dropped. For the displayed matrix, `mu2(F1) = (sqrt(17)-3)/2 > 0` despite the negative spectrum.

**Finding L2 — a second, independent local proof issue.** The degree-independent estimate in (4.62), p. 14, replaces the degree `j` by the truncation degree `N` in a decreasing factor. It already fails for the scalar normal matrix `F1 = -1`, `N = 2`, `j = 1`, `h = 1/10`: the left side is `81/100`, while the printed upper bound is `64/100`. Thus imposing normality alone does not validate every intermediate Euler estimate as written. A repaired proof needs a correct blockwise contractivity argument. The project should use its own proved finite/contractive estimates instead of citing this displayed calculation as sufficient.

## 2. Gourianov: classical structured simulation and a proposed quantum port

The paper gives a useful separation between grid resolution and correlations across scales. Binary position digits are grouped by scale; Schmidt ranks quantify a coarse/fine partition; MPS or tensor-train representations restrict these ranks. Such a representation is a classical data structure when its tensors are stored and contracted on a classical computer. Entanglement vocabulary applied to a normalized array does not mean the fluid has been prepared as a physical many-qubit state.

The numerical evidence concerns a two-dimensional temporally developing jet and a three-dimensional Taylor–Green vortex, with detailed comparisons to direct and underresolved simulations (main pp. 2–9). The highlighted configurations use Reynolds numbers 1000 and 800, respectively. Reduced parameter counts and better accuracy than selected equally compressed underresolved grids are meaningful evidence for these examples. They do not establish a universal bond-rank bound for turbulent solutions or a uniform continuum convergence theorem.

The supplement has genuine exact finite representation results: a sampled Heaviside vector has an explicit MPS of bond dimension two; the specified triangular-wave vector has a bond-three representation, with an induction eliminating a redundant fourth component (PDF pp. 24–26, supplement pp. 13–15). The special Burgers hump discussion uses Hopf–Cole and approximation regularity. Any analyticity argument must retain its domain, viscosity/time dependence, and approximation constants; it is not a three-dimensional Navier–Stokes regularity theorem.

### Costs that remain

The per-step estimate before simplification is

\[
O\bigl(m_1\,n\,[\chi^4+\chi^3(\mathrm{const}+m_2)]\bigr),
\]

where `n` is the number of tensor sites, `m1` the number of sweeps, and `m2` the local conjugate-gradient iterations. Dropping their observed stable prefactors yields the often quoted `O(chi^4 log M)` per step. The paper does not prove those iteration counts remain bounded for every flow, penalty strength, target precision, or grid refinement (PDF pp. 29–30). Total time integration also retains its number of steps and stability/accuracy requirements.

**Finding G1 — distinguish local and global minimization.** The local equation has an SPD coefficient because its penalty contribution is a squared discrete divergence. This correctly supports a unique local quadratic solve. The sweep procedure in supplement §4C is then described as obtaining the global minimum, but no theorem is supplied guaranteeing global convergence over the nonconvex fixed-rank MPS manifold. Local SPD solvability does not prove that global claim. The project's learning discussion must retain this distinction.

**Finding G2 — quantum-port scope.** Supplement §5 (PDF pp. 32–33) proposes a variational quantum version and illustrates a circuit for nonlinear cost terms using more than one copy of the previous state. Its improvement in the dependence on bond dimension is not a complete end-to-end guarantee. State/circuit preparation, noisy expectation estimation, optimizer iterations, attainable ansatz error, normalization, and output observables still need their own analysis. The study's reported numerical experiments and CPU timings are classical. It does not report a fault-tolerant hardware fluid simulation or establish a ToricGT transfer theorem.

## 3. Jennings: a more complete cost model with important remaining assumptions

### 3.1 What is actually modeled and proved

The algorithm starts with a **shifted incompressible lattice-Boltzmann discretization**. Subtracting a reference equilibrium and choosing the lattice velocity to scale as `N^(-1/2)` addresses the growing norm that would suppress the first Carleman block. This choice also makes the required number of time steps grow. With the paper's parameter conventions,

\[
N_x\asymp\mathrm{Re}^{\beta},\quad
T^\star\asymp\mathrm{Re}^{\beta(D/2+1)},\quad
\bar\tau^\star=\frac12+3\mathrm{Re}^{-\beta(D/2-1)-1}.
\]

The value `beta = 3/4` is a chosen Kolmogorov-resolution scaling, used even for the one- and two-dimensional diagnostic models. It is not a mathematical uniform-resolution theorem for every flow or geometry. The selected ILBE equilibrium approximates divergence freedom and is motivated especially by steady or slowly varying flows. The paper itself points to a different formulation for more exact time-dependent incompressibility (p. 11).

Useful exact algebra includes the discrete Carleman block construction, the history-system inverse, standard LCU constructions, and a collision-only finite closure. Appendix C shows why a cubic **collision-only** DBE at one site has zero first-block truncation error once `NC >= 3`. This is precisely why collision-only tests cannot establish the convergence of combined streaming/collision dynamics.

The matrix estimate

\[
\kappa(A)\ge\frac{\|C\|T^\star}{\sqrt3}
\]

is derived using a unit-modulus eigenvector of the collision-streaming map (pp. 25–26). The periodic, no-wall eigenvector construction is explicit. This gives an obstruction for the analyzed linear-system formulation and its QLS cost model; it is not a lower bound on every possible quantum fluid algorithm. A general worst-case black-box QLS lower bound also must not be silently promoted to an instance-specific lower bound for all ways to exploit a structured right-hand side.

### 3.2 Convergence evidence and extrapolation

Carleman error is measured against the **discrete shifted ILBE**, using a spatially averaged physical-velocity error and a maximum over the simulated times (pp. 20–24). It is not a total error against a continuum Navier–Stokes solution. Continuum modeling, Mach/Knudsen, spatial/time discretization, boundary treatment, truncation, QLS, gate synthesis, and measurement errors remain distinct.

The experiments cover finite truncation orders: one-dimensional examples up to five and two-dimensional examples up to three, with accessible Reynolds ranges differing by order. The reported threshold behavior and exponential-in-order fits are numerical evidence over those ranges. Increasing error over a few orders is not by itself a proof of divergence as `NC -> infinity`; decreasing error is not a uniform convergence theorem. One-dimensional incompressible flow is spatially constant, a limitation the paper explicitly acknowledges when using its D1Q3 tests (p. 21).

For conditioning, the authors numerically estimate the **history** matrix and use it as an estimate for the final-state matrix, while explicitly noting that the former is a lower bound for the latter (p. 26). The commonly quoted exponent `1.936` for `D = 2, NC = 2` is a fitted value in this analysis, not a rigorously established asymptotic upper bound. Figures extrapolating these fits far beyond accessible sizes should be described as projections. The paper does not establish a three-dimensional experimental convergence regime or a fully compiled D3 collision circuit; Appendix I4 leaves the latter for future work.

### 3.3 Preparation, success, and readout

Initial preparation is assumed efficient for structured velocity fields. Arbitrary or unstructured input can cost order `N` to load (p. 17). The lifted input requires order `NC` uses of the initial-state preparer. No exponential input-loading saving is established for unrestricted data.

Final-time extraction uses padding. Its exact success probability depends on the ratio of the accumulated history norm to the final-time norm (Eq. 113); bounded overhead requires a corresponding nondecay assumption. First-block extraction uses approximate relations between the norms of the truncated blocks and powers of `||g||` (Eq. 115). Those relations and the norm bound must hold for the actual approximation, not only the underlying nonlinear trajectory. The paper discusses the loss of this property in inaccurate high-error examples (pp. 20–21).

**Finding J1 — drag overlap is an assumption, not a consequence of support alone.** The measurement cost `qM = O(Re^(beta/2))` is motivated by a boundary overlap expected to scale as `N_x^(-1/2)` (pp. 19–20). A boundary's support size supplies no uniform positive lower bound on this overlap. Signed velocity contributions can cancel, and drag can be arbitrarily small. Absolute versus relative precision, overlap magnitude, preparation of the boundary state, and recovery of the physical normalization must therefore be stated. Quantum amplitude estimation retains its precision dependence. Certain bulk observables may avoid the geometric suppression, but that is not a free readout theorem for all bulk observables.

The resource model is `qQ * gate_cost * qM`, with further dependence through successful extraction and input preparation. For the fitted two-dimensional `NC = 2` case, adding the quoted drag exponent yields `1.936 + 0.375 = 2.311`, slightly worse than the paper's classical comparator exponent `2.25`. Its more favorable bulk projections do not establish a demonstrated runtime advantage.

**Finding J2 — modest-order gate approximation.** The compact cubic-in-`NC` gate estimate suppresses terms present in full Eq. (171), including Fibonacci/exponential permutation-control contributions and `h_NC`. Appendix D, p. 40, explicitly recognizes the near-exponential naive permutation encoding and suggests a Fisher–Yates alternative. Thus the simplified cubic expression is not a uniform large-order theorem. A fitted exponential truncation law also cannot, on its own, turn the full gate cost into a proved polylogarithmic-in-error cost. Approximate compilation counts, ignored controlled-permutation costs, and the hypothetical D3 extrapolation are estimates, not actual executed circuits.

### 3.4 Printed formulas requiring finite interface repairs

These findings concern the reviewed arXiv v2. They were checked against rendered pages, not inferred from OCR alone.

**Finding J3 — continuity sign and normalization (Eq. 42, p. 11).** From the paper's dimensional definitions `sum gm = p/cs²` and `sum gm em = rho0 u`, mass conservation yields

\[
\nabla\cdot u=-\frac{1}{\rho_0c_s^2}\partial_t p.
\]

The displayed equation has the opposite sign and omits `rho0`; the latter can disappear after a density normalization, but the sign cannot. The project must use the derived convention rather than copy that formula.

**Finding J4 — equality-map dilation (D56, p. 42).** With

\[
S=\sum_a|a,0\rangle\langle a,a|,
\]

the printed candidate `B = S tensor I + (S-I) tensor X` is not unitary. For a nonzero bit string `a`,

\[
B|a,a,0\rangle=|a,0,0\rangle+|a,0,1\rangle-|a,a,1\rangle,
\]

whose squared norm is three. The defect is repairable. Apply the reversible XOR map `U|a,b> = |a,b xor a>` and flag whether the second output is zero. Postselection on that flag implements `P0 U = S` with probability `||S x||²` on normalized input `x`. Its norm cost cannot be discarded when using the operation as a stand-alone postselected primitive. The manuscript companion section supplies the complete finite proof.

**Finding J5 — contraction scaling in the dilation (I65, p. 52).** The Halmos-type unitary dilation is written with an unnormalized `Sigma2`. Its square roots are the positive contraction defect operators only after scaling by `alpha >= ||Sigma2||`. The D2 formula in D58 gives the prefactor `6 / tau_bar_star`; the bare value six on p. 52 does not account for arbitrary relaxation time. For a general matrix `A`, the corrected block uses `A/alpha`; postselection has probability `||A x||²/alpha²`. This is a finite, exactly provable repair, not a new global resource theorem.

These defects do not imply that no valid block encoding exists. They show that a mathematically correct implementation must use an explicit unitary extension and retain its normalization. In particular, a successful-branch normalization is not a deterministic implementation of nonlinear evolution on an unknown state.

## Integration decisions

1. Cite the exact versions and keep publisher correction date distinct from revision date.
2. Use the project's independent contractivity and finite energy propositions; do not substitute negative eigenvalue real parts for a Euclidean dissipation proof.
3. Use Gourianov for classical tensor compression, special exact representations, and a proposed VQA architecture. Keep rank, optimization, and quantum-measurement costs explicit.
4. Use Jennings for its discrete reformulation and detailed resource questions, labeling fitted exponents and finite truncation experiments as such. Retain input/observable assumptions and repair the two finite unitary interfaces before implementation.
5. Treat all three as algorithmic or numerical sources. No result here supplies the missing continuum estimates required to reprove or improve the separate Navier–Stokes singularity construction.

No broad numerical tests were added during this review. The exact counterexamples are algebraic calculations; complete finite-interface proofs are recorded separately. The pre-existing project tests and Lean checks cover their explicitly named finite statements, not these entire papers.
