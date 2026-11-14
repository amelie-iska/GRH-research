# Farhat model-reduction course: complete text review and mathematical corrections

Review date: 13 November 2026. Page references below are **PDF page numbers**,
including presentation overlays, rather than the smaller slide numbers printed
in the footers.

## Source and coverage

The nine historical `CA-CME345-ChN.pdf` requests returned HTTP 404. The review
therefore uses the current `CA-AA216-CME345-ChN.pdf` replacements from Stanford's
course directory. These are not asserted identical to the editions available
when the fluid-simulation video was published. Their hashes, retrieval outcomes,
and exact read ranges are recorded in `farhat-review.json`.

All **627 PDF pages** were read as complete extracted text, including every
overlay. All 28 pages flagged for very little extractable text were rendered
and inspected, as were 20 additional technical pages: 48 visual page checks in
total. This is not a claim that every illustration on every page received a
separate visual audit. Embedded videos were not played, and the papers listed
in the lecture bibliographies were not all read in full during this pass.

| Deck | Topic | Pages | Primary source |
|---|---|---:|---|
| 1 | Introduction and computational motivation | 58 | [Stanford Ch1](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch1.pdf) |
| 2 | Parameterized PDEs | 39 | [Stanford Ch2](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch2.pdf) |
| 3 | Projection, Galerkin and Petrov–Galerkin reduction | 96 | [Stanford Ch3](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch3.pdf) |
| 4 | Proper orthogonal decomposition | 79 | [Stanford Ch4](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch4.pdf) |
| 5 | Linear dynamical systems | 43 | [Stanford Ch5](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch5.pdf) |
| 6 | Balanced truncation | 95 | [Stanford Ch6](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch6.pdf) |
| 7 | Moment matching and Krylov methods | 58 | [Stanford Ch7](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch7.pdf) |
| 8 | Local parametric models and manifold interpolation | 92 | [Stanford Ch8](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch8.pdf) |
| 9 | Hyperreduction | 67 | [Stanford Ch9](https://web.stanford.edu/group/frg/course_work/CME345/CA-AA216-CME345-Ch9.pdf) |

The counts are physical PDF pages, **not 627 distinct mathematical slides**.
For example, Chapter 3's 96 pages contain overlays of 38 numbered slides.

## Mathematical content that should enter the manuscript

### 1. Projection defines a new dynamical system

For a fixed full-column-rank trial matrix (V\in\mathbb R^{N\times r}), test
matrix (W\in\mathbb R^{N\times r}), and nonsingular (W^TV), Petrov–Galerkin
reduction of (dot x=f(x,t)) is

\[
\dot a=(W^TV)^{-1}W^Tf(Va,t),\qquad
P=V(W^TV)^{-1}W^T.
\]

Then (P^2=P), (\operatorname{im}P=\operatorname{im}V), and

\[
\ker P=\ker W^T=(\operatorname{im}W)^\perp.
\]

The reconstructed trajectory solves (dot{\widetilde x}=Pf(\widetilde x,t)),
not generally the original ODE. Both the initial projection error and the
subsequent dynamical error matter. Chapter 3, pp. 57–96, makes this distinction
and gives a stable nonsymmetric matrix whose orthogonal Galerkin reduction is
unstable. Dissipativity (A+A^T\preceq-2\alpha I), with (\alpha>0), is a
sufficient condition preserved by an orthonormal Galerkin basis; mere stability
of the eigenvalues of a nonsymmetric (A) is insufficient.

For a mass matrix, affine lifting, or moving basis, derive the corresponding
equation before reducing: (W^TMV), the derivative of the lift, and
(\dot V a) cannot be omitted. Boundary conditions and incompressibility are
additional constraints on the trial representation, rather than consequences
of low rank. See Chapters 1–3.

### 2. POD optimality has a particular norm and data measure

Let (M\succ0) specify the spatial inner product and let (alpha_j\geq0)
be snapshot weights. For snapshots (x_j), form

\[
S=[\sqrt{\alpha_1}x_1\ \cdots\ \sqrt{\alpha_m}x_m],
\qquad Y=M^{1/2}S.
\]

If (U_r) contains (r) leading left singular vectors of (Y), then
(V=M^{-1/2}U_r) satisfies (V^TMV=I), and

\[
\min_{Z^TMZ=I}\sum_j\alpha_j
 \|x_j-ZZ^TMx_j\|_M^2
 =\sum_{i>r}\sigma_i(Y)^2.
\]

**Proof.** Change variables to (M^{1/2}x). For an orthonormal (U), the
objective is (\|Y\|_F^2-\operatorname{tr}(U^TYY^TU)). Maximizing this trace
selects the largest (r) eigenvalues of (YY^T), leaving the stated tail.
The minimizing subspace need not be unique at a repeated singular value.

This statement concerns the selected snapshots and their weights. It supplies
no generalization theorem for unsampled parameters, no uniform-in-time bound,
and no guarantee for derivatives or a quantity of interest measured in another
norm. Chapter 4, pp. 35–42, explicitly limits the energy criterion to sampled
snapshots and distinguishes it from the total ROM error. Its covariance integral
and quadrature approximation are also distinct objects. Direct SVD avoids the
squaring of the condition number associated with (S^TS).

Centering changes the approximation from a linear subspace to an affine one;
uncentered snapshot energy and centered variance should not be conflated.
The snapshot singular values are also not the eigenvalues of the PDE generator
or a quantum Hamiltonian.

### 3. A residual becomes an error bound only with stability information

For an approximate trajectory (widetilde x), put
(\rho=\dot{\widetilde x}-f(\widetilde x,t)). Suppose the exact and approximate
trajectories remain in a region where (f) is Lipschitz with constant (L(t)).
Then

\[
\|x(t)-\widetilde x(t)\|
\leq e^{\int_0^tL}\|x(0)-\widetilde x(0)\|
 +\int_0^t e^{\int_s^tL}\|\rho(s)\|\,ds.
\]

Subtract the ODEs, take the norm using a positive regularization at zero, and
apply an integrating factor. This proves the bound and identifies all its
inputs. A one-sided Lipschitz bound can replace a full Lipschitz estimate in the
corresponding inner-product argument.

Chapter 3, p. 92, gives a finite-time linear convolution-operator bound in terms
of projection error. Chapters 4 and 7 distinguish certified error bounds from
residual indicators used in greedy sampling. A small sampled residual is only
an indicator until interpolation/enclosure and a stability factor have been
supplied. Near a singular limit, the stability factor may grow, even if an
empirical low-rank representation remains compact.

### 4. Gramians measure input reachability and output observability

For (dot x=Ax+Bu), (y=Cx),

\[
P_T=\int_0^T e^{At}BB^Te^{A^Tt}\,dt,\qquad
Q_T=\int_0^T e^{A^Tt}C^TCe^{At}\,dt.
\]

The range of (P_T), for (T>0), is the reachable subspace. To see both
inclusions, (z^TP_Tz=0) holds exactly when (B^Te^{A^Tt}z=0) on the
interval, equivalently when (B^T(A^T)^jz=0) for every (j\geq0).
Cayley–Hamilton reduces this to finitely many powers. Taking orthogonal
complements gives the range assertion. This completes the inclusion-only
power-series argument presented on Chapter 6, p. 30.

On the reachable subspace, the minimum control cost to reach (x_T) from zero
is (x_T^TP_T^{\dagger}x_T). When (P_T\) is invertible, the minimizing input is

\[
u_*(t)=B^Te^{A^T(T-t)}P_T^{-1}x_T.
\]

Substitution gives the prescribed endpoint and
(\int_0^T\|u_*\|^2=x_T^TP_T^{-1}x_T). Any other admissible input differs by
an element of the endpoint map's kernel, orthogonal to (u_*), proving
minimality. The minimized quantity is **(\int\|u\|^2)**, not
(\int\|Bu\|^2). Similarly, (x_0^TQ_Tx_0) equals the output energy of the
unforced trajectory; it is not an optimization over outputs.

Infinite-horizon Gramians require appropriate convergence; a Hurwitz matrix
(A) suffices. Positive definiteness requires reachability and observability.
When zero Gramian directions exist, first restrict to a minimal realization
or formulate the construction on the appropriate subspaces. Chapter 6,
pp. 32–68, is the relevant source.

### 5. Balanced truncation bounds have restrictive but useful hypotheses

For a finite-dimensional, asymptotically stable minimal LTI realization, exact
balancing makes the two infinite Gramians equal to
(\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_N)). Truncating complete
separated Hankel-value blocks preserves strict stability. A standard valid
bound, with multiplicities counted, is

\[
\|G-G_r\|_{H_\infty}\leq 2\sum_{i=r+1}^N\sigma_i,
\qquad
\|y-y_r\|_{L^2}\leq\|G-G_r\|_{H_\infty}\|u\|_{L^2}.
\]

The input-output assertion assumes zero initial conditions and matching direct
feedthrough. The continuous-time Hardy domain is **(\Re s>0)**, and the
matrix norm at a frequency is the spectral operator norm. For stable rational
transfer functions it is equivalent to the supremum over (s=i\omega).
Chapter 6, pp. 69–74, gives the distinct-block version and its stability
qualification. The stronger block formulation should not be quoted without
its block assumptions, or its operator-norm statement confused with equality
for every individual input.

Balanced POD approximates the Gramians from primal and adjoint snapshots.
It does not automatically inherit every exact balanced-truncation guarantee:
Chapter 6, p. 92, expressly says stability is not guaranteed in general.
Quadrature, truncation, complex conjugation, and finite precision add separate
errors. Classical finite-dimensional guarantees do not directly prove a
continuum Navier–Stokes regularity result.

### 6. Moment matching means interpolation at specified regular points

Let (R_0=(s_0I-A)^{-1}), and assume (s_0I-A) and
(s_0I-A_r) are invertible. If

\[
\operatorname{span}\{R_0b,R_0^2b,\ldots,R_0^rb\}
\subseteq\operatorname{im}V,\quad W^TV=I,
\]

then the reduced transfer function matches the first (r) Taylor coefficients
at (s_0). This follows inductively by applying (W^T(s_0I-A)V) to the
coordinates of (R_0^jb), then applying the output functional. Expansion at
infinity is instead expressed in (z=1/s), with Markov coefficients
(D,CB,CAB,\ldots). Ordinary derivatives evaluated at an unspecified
“infinity” coordinate are not the correct notation.

Krylov rank loss, biorthogonality breakdown, conjugate pairs for real models,
and reduced poles at an intended interpolation node must be handled. Matching
moments provides local interpolation, not an unconditional global error or
stability certificate. In IRKA, interpolation nodes are iteratively updated
to reflected reduced poles to satisfy first-order (H_2) optimality
conditions; general moment matching does not inherently interpolate at its
own poles. See Chapter 7, pp. 19–38.

### 7. Interpolate subspaces and aligned operators

Chapter 8 gives a decisive counterexample to entrywise interpolation of bases:
two matrices differing only by a column sign represent the same subspace, but
their average may lose rank. The correct fixed-rank object is
(\mathrm{Gr}(r,N)=\mathrm{St}(r,N)/O(r)), with tangent-space interpolation
performed in a valid local chart. The displayed Grassmann logarithm requires
(V_0^TV_i) invertible, equivalently no principal angle equal to (\pi/2).
A global single-valued logarithm is not available on an arbitrary manifold.

Reduced operators also need consistent coordinates. Orthogonal Procrustes
alignment solves
(\min_{Q^TQ=I}\|V_iQ-V_0\|_F) by an SVD of (V_i^TV_0), followed by
((A_i,B_i,C_i)\mapsto(Q^TA_iQ,Q^TB_i,C_iQ)).
The cross-Gram matrix costs (O(Nr^2)) to form; the small SVD is (O(r^3)).
An online cost depending only on (r) therefore requires the cross-Gram data
to be precomputed or otherwise accessible. Fixed-rank geometry, positive
definiteness, and coordinate consistency are useful structural properties;
none by itself certifies interpolation accuracy or nonlinear stability.

### 8. Hyperreduction is a second approximation with its own conditioning

For an orthonormal nonlinear basis (U\in\mathbb R^{N\times m}) and a
coordinate-sampling matrix (P\in\mathbb R^{N\times m}), DEIM uses

\[
D=U(P^TU)^{-1}P^T,
\qquad \widetilde f=Df.
\]

Invertibility of (P^TU) is essential. Since (DU=U),

\[
f-Df=(I-D)(I-UU^T)f,
\qquad
\|f-Df\|\leq\bigl(1+\|(P^TU)^{-1}\|\bigr)
                    \|(I-UU^T)f\|.
\]

This elementary bound already identifies the separate approximation and
sampling-conditioning errors. Sharper DEIM bounds are possible; the safe
bound above needs only the stated assumptions. Oversampled gappy POD replaces
the inverse by a pseudoinverse. Full column rank is still needed for a unique
coefficient fit and exact reproduction of every vector in the chosen basis.
Having more sampled rows than columns alone does not establish that rank.

Online cost independent of (N) additionally requires that selected entries
of (f) be evaluable from a small dependency set, and that only those state
entries be reconstructed. Evaluating a dense global (f(Va)) and sampling
afterwards preserves the original bottleneck. The state basis and nonlinear
basis also have different training obligations. These distinctions appear in
Chapter 9, pp. 7–55.

### 9. Positive weighted assembly preserves a specified variational structure

In a finite-element setting, use the actual assembly

\[
f(x)=\sum_eL_e^Tf_e(L_ex),\qquad
V^Tf(Va)=\sum_e(L_eV)^Tf_e(L_eVa).
\]

An element force (f_e) is not generally the restriction (L_ef) of an
already assembled global force: that substitution double-counts shared
degrees of freedom. If (f_e=\nabla U_e), fixed weights (\xi_e\geq0) give

\[
\widehat U(a)=\sum_{e\in E_s}\xi_eU_e(L_eVa),\qquad
\nabla\widehat U(a)=\sum_{e\in E_s}\xi_e(L_eV)^Tf_e(L_eVa).
\]

Thus a second-order Galerkin model with positive definite reduced mass has a
well-defined modified potential and its corresponding energy identity.
With constant (M_r\succ0) and positive semidefinite damping (C_r),

\[
M_r\ddot a+C_r\dot a+\nabla\widehat U(a)=g
\quad\Longrightarrow\quad
\frac d{dt}\left(\tfrac12\dot a^TM_r\dot a+\widehat U(a)\right)
=\dot a^Tg-\dot a^TC_r\dot a.
\]

This is the relevant structure behind ECSW. Positive weights retain positive
element contributions but do not, by themselves, ensure coercivity after an
arbitrary selection of elements, preservation of every invariant, or a uniform
accuracy bound. The training residual in the nonnegative least-squares problem
is finite-data information, and a sparse NNLS solution is not automatically a
proof of global minimum support. Chapter 9, pp. 56–65, distinguishes its
second-order finite-element Galerkin setting from later fluid Petrov–Galerkin
extensions.

For a learned model, **state-dependent weights need additional terms**:

\[
\nabla_a\sum_e\xi_e(a)U_e(L_eVa)
=\sum_e\xi_e(a)(L_eV)^Tf_e(L_eVa)
 +\sum_eU_e(L_eVa)\nabla_a\xi_e(a).
\]

A neural or quantum model that changes weights online but omits the second
sum has not preserved that potential. Learning a potential and differentiating
it, or learning fixed quadrature weights offline, gives a precise alternative.

## Source-level corrections and qualifications

The following are mathematical corrections to carry into the manuscript,
not reasons to discard the course's useful framework.

| Location | Correction or required qualification |
|---|---|
| Ch2 pp. 36–39 | The (2^p) count describes a full tensor-product or unrestricted multi-affine approximation. It is not a universal sample lower bound for every parameterized PDE family; a globally affine family has only (p+1) scalar coefficients. |
| Ch3 p. 24 | An idempotent is diagonalizable because its minimal polynomial divides (t(t-1)), which has simple roots. Merely knowing possible eigenvalues are 0 and 1 would not suffice. |
| Ch3 pp. 69–72 | (Vq(0)\in\mathbb R^N), not (\mathbb R^r); the projection is parallel to (\ker W^T), not to (\operatorname{range}W). |
| Ch4 p. 7 | The preceding covariance matrix is (N\times N), not infinite-dimensional. An infinite-dimensional covariance operator belongs to a different formulation. |
| Ch4 p. 24 | Use named norms: (\|A\|_2=\max_i\sigma_i), (\|A\|_F^2=\sum_i\sigma_i^2). A general Schatten-(p) identity must not be confused with an induced matrix-(p) norm. |
| Ch4 pp. 25–27 | A singular-value gap is unnecessary for the optimal low-rank approximation value; it affects uniqueness of the appropriate singular subspace. Spectral-norm minimizers need not become unique merely because of a gap. |
| Ch4 pp. 41–42 | The snapshot error identity must use the same weights as the snapshot matrix; the displayed unweighted version implicitly specializes those weights. |
| Ch5 pp. 14–17 | Direct feedthrough is the coefficient (D\delta) in an impulse-response distribution, not an ordinary value (h(0)). Its matrix shape is output dimension by input dimension. |
| Ch5 pp. 35–38 | (A\mapsto TAT^{-1}) is similarity. Gramians transform by congruence; these should not be interchanged. |
| Ch6 pp. 49–50 | The controllability Gramian's minimum cost is (\int\|u\|^2), not (\int\|Bu\|^2). |
| Ch6 p. 69 | Replace (\Im s>0) by (\Re s>0), and interpret the frequency matrix norm as the spectral operator norm. |
| Ch6 pp. 89–91 | Complex snapshot formulas require consistent adjoints or conversion to real/imaginary snapshot bases; unqualified real transpose notation is insufficient. |
| Ch7 pp. 19, 22–25 | Use state-vector Krylov spans, not an equality between scalar output-moment spans and subspaces of (\mathbb R^N). A union of subspaces means their linear span/sum here. |
| Ch7 p. 25 | The displayed right and left spaces each have at most (\ell k) dimensions. Their common reduced dimension is at most (\ell k), not (2\ell k); (2\ell) counts interpolation locations. Deflation can reduce rank further. |
| Ch7 p. 34 | With star meaning conjugate transpose, the (H_2) integrand is (\operatorname{tr}(H(i\omega)^*H(i\omega))). The displayed negative argument in the starred factor mixes two conventions. |
| Ch7 p. 36 | General rational interpolation matches at prescribed regular nodes, not automatically at its own reduced poles. IRKA imposes a fixed-point condition on reflected poles. |
| Ch8 pp. 54–56 | The displayed Grassmann log formula needs (V_0^TV_i) invertible. Treat the log as a local chart. |
| Ch8 p. 77 | Include the (O(Nr^2)) cross-Gram cost unless it has been precomputed. |
| Ch8 pp. 86–87 | Cross-Gram entries are signed inner products; their absolute values, rather than the signed entries themselves, are the nonnegative square roots of entrywise MAC values. |
| Ch9 pp. 47–48 | A Moore–Penrose pseudoinverse is a left inverse only with full column rank. The identity (MM^\dagger M=M) alone neither gives a left inverse nor uniqueness of a least-squares minimizer. |
| Ch9 pp. 60–62 | Specify element contributions before assembly; do not interpret an element force as a restriction of the assembled global vector. |

## Recommended integration

The monograph should keep five certificates separate: spatial discretization,
snapshot approximation, reduced dynamics, hyperreduction, and learned closure.
It should report the norms, parameter/time domain, sampling measure, conditioning,
stability factors, and held-out evidence for each. A quantum model can propose
coordinates, operators, sample sets, or constitutive potentials, but these
different outputs preserve different structures and require different checks.

The most direct connection to the Navier–Stokes release is the distinction
between data compression and all-order continuum control. A finite-dimensional
surrogate, even an accurate and structure-preserving one, does not supply the
release's scale-uniform derivative estimates, compact smooth forcing, or
whole-space comparison theorem. The Farhat material strengthens the project's
computational methodology precisely when that distinction is retained.
