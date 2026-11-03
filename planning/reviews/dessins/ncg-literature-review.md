# Dessin-derived infinite algebras: recent arithmetic NCG and spectral RH interfaces

Date: 3 November 2026. Scope: infinite-dimensional dessin-derived locally gentle algebras, completed orders, and possible graph C*/Leavitt realizations. This does not repeat the four supplied-paper audits or return to finite-dimensional gentle-algebra classification. The review reads selected exact theorem statements, relevant proofs and stated open steps in the primary PDFs listed below; it is not an all-page certification of those papers.

## Main finding

Three recent developments complement this program particularly well:

1. Connes–Consani's **2025 arithmetic covers** supply an actual Frobenius-monodromy target, including periods log(p), ramification and archimedean data.
2. Connes–Consani–Moscovici's **2023–2025 semilocal/Jacobi and spectral constructions** supply precise local-factor Hilbert spaces and a proved regularized-determinant formula under explicit ground-state hypotheses.
3. Connes–van Suijlekom's **2025 real-zero theorem** supplies a usable positivity-to-zero-location mechanism with substantial domain, symmetry and simplicity hypotheses.

None identifies a dessin-derived completed order with the adelic construction, proves its determinant is a completed L-function, or supplies global Weil positivity/purity. The 2025 spectral paper and Connes's 2026 survey explicitly retain missing steps. Graph spectra, a positive C* trace, Galois action on dessins, Auslander–Reiten structure, and a formal determinant line are useful structures; their coexistence alone is not that arithmetic bridge.

## Evidence and version pins

New immutable PDFs and layout extractions are under:

`/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/dessin-extension-20261103/`

The downloaded PDF filenames include exact arXiv versions. Page references below refer to those PDFs. Versions were verified from primary arXiv records, not inferred from a search snippet. No MCP, authentication, installation, source-clone mutation or shared manuscript/Lean/planning edits occurred.

| Primary item | Version/date | PDF pages | Precisely inspected material |
|---|---|---:|---|
| Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators* | [2310.18423v2](https://arxiv.org/abs/2310.18423v2), 4May2024; first2023 |30| Introduction; semilocal construction and proofs of Props4.1–4.3; Thm4.6; Prop4.8; relevant cyclic-pair/Jacobi setup |
| Same authors, *On q-series and the moment problem associated to local factors* | [2403.01247v1](https://arxiv.org/abs/2403.01247v1), 2March2024 |37| Props2.1 and3.1 with proofs; semilocal measure; q-series/integrality scope in introduction |
| Same authors, *Zeta Spectral Triples* | [2511.22755v1](https://arxiv.org/abs/2511.22755v1),27November2025 |34| Thm3.6/proof; finite-form setup; Prop5.9, Thm5.10/proof; numerical scope; Lemma7.3/proof; §8 missing steps |
| Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* | [2511.23257v1](https://arxiv.org/abs/2511.23257v1),28November2025 |26| Cor1.1; Prop2.1/GNS mechanism; Props4.1–4.2, Remark4.3; Thm5.6; Prop5.10; Thm6.1/proof. Thm6.1 PDF page rendered and checked |
| Connes–Consani, *Knots, primes and class field theory* | [2501.06560v1](https://arxiv.org/abs/2501.06560v1),11January2025 |30| Intro; finite-cover/ramification definitions; Thm3.12 and proof; Thm4.2; semilocal sheaf construction/Thm5.3 |
| Same authors, *On the Jacobian of the compactified Spec Z* | [2602.15941v1](https://arxiv.org/abs/2602.15941v1),17February2026 |48| Thms1.1–1.4 and relevant definitions; §9.1–9.2 explicit formula/isotropy; Thm9.1. No full audit of later tensor/root constructions |
| Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time* | [2602.04022v1](https://arxiv.org/abs/2602.04022v1),3February2026 |42| §4.1 Weil criterion; §6.6 remaining steps; §7.2 archimedean inequality; §7.4 trace formula; §7.5–7.6 and RH assumption in Thm7.3 |
| Deninger, *Dynamical systems for arithmetic schemes* | [1807.06400v4](https://arxiv.org/abs/1807.06400v4),7February2024; substantial v3 was2022 |119| Introduction/limitations; actual Thm6.1 and packet construction. Published Indag.Math.37(2026),25–136, [DOI10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007) |
| Deninger, *Primes, knots and periodic orbits* | [2301.11643v1](https://arxiv.org/abs/2301.11643v1),27January2023 |survey| Introduction and relation to preceding construction; supporting orientation rather than a new spectral theorem |
| Deninger, *There is no “Weil-”cohomology theory with real coefficients for arithmetic curves* | [2204.02714v2](https://arxiv.org/abs/2204.02714v2),27January2023; first2022 |8| Entire theorem/argument in §2, especially properties2.1–2.12, Thm2.13, and scope discussion |
| Ponge–Tian, *Nonclassical Weyl laws and Connes' Integration for weak Lorentz ideals,I* | [2605.25591v2](https://arxiv.org/abs/2605.25591v2),28September2026 |40| Regular-variation/ideal hypotheses; Thm3.26/proof, Thm5.8/proof, Prop6.2 and its explicit RH assumption |

The 2026 survey and Jacobian paper are valuable current summaries/geometric refinements, but their restatements of older trace formulas are not new proofs of RH. In particular, publication year, submission year and revised-version year are kept distinct above.

## 1. Strongest arithmetic bridge: actual Frobenius-monodromy, not graph-cycle analogy

**Connes–Consani2501.06560v1, Theorem3.12, pp.15–17.** For a finite abelian extension L/Q, the canonical continuous quotient of the cyclotomic Galois group defines a contravariant functor

`Ab(Q) → Cov_ab(X_Q)`.

Here X_Q is their specified Riemann sector of the adele class space. In the paper's precise cover/ramification sense, the ramification set consists of the archimedean place together with the finite ramified primes. For an unramified finite prime p, the monodromy of the orbit C_p is the **arithmetic** Frobenius Frob_p. Connected components over C_p are circles indexed by places of L overp. The orbit has length log(p). The proof uses actual global/local class field theory and the explicit adelic cover; it is not a consequence of a circle's unitary spectrum.

**Theorem4.2, p.19**, refines the maximal abelian-cover interpretation using the map on abelianized étale fundamental groups. **Theorem5.3, p.23**, identifies the semilocal crossed products as a sheaf of algebras on SpecZ, with semilocal sections `S(A_S) ⋊ Z_S^×`, generic stalk `S(A_Q) ⋊ Q^×`, and archimedean global sections `S(R) ⋊ {±1}`.

**Transfer to dessins/completed orders.** This gives a concrete benchmark for any proposed Galois/Frobenius action on a dessin-derived category. One needs a functor or correspondence to these arithmetic covers, preserving character sectors, orbit periods, ramification and scaling. Galois equivariance of the abstract dessin or its combinatorial automorphism group does not identify its path-cycle monodromy with arithmetic Frob_p. The theorem is abelian overQ; it is not an arbitrary nonabelian dessin/Galois representation theorem or an Artin-holomorphy result.

The sheaf of **Bruhat–Schwartz crossed products** is also a plausible arithmetic recipient for a dense subalgebra of a completed order. An algebraic/Morita/K-theoretic resemblance is insufficient: compatibility with the smooth algebra, topology, scaling action, additive Fourier transform and trace distributions must be exhibited.

## 2. Semilocal local factors give a rigorous Jacobi/Hilbert-space target

**Connes–Consani–Moscovici2310.18423v2, Proposition4.1, p.17; Proposition4.2, p.18.** Fix a finite set S of rational places containing∞; choose the local additive Fourier transforms self-dually normalized, so `1_Zp` is fixed. They construct an actual map from even archimedean L²-functions to the compact-invariant sector of the semilocal adele quotient. Its multiplicative Fourier transform acquires exactly the factors

`∏_{p∈S\{∞}} (1-p^(-(1/2-is)))^(-1)`.

The map intertwines the local additive Fourier transforms. The resulting cyclic pair has a unitary realization as multiplication bys on

`L²(R, dm_S),  dm_S(s)=|∏_{v∈S} L_v(1/2-is)|² ds`.

The∞-factor includes the gamma factor. Thus the measure encodes actual local arithmetic factors and archimedean normalization, not a guessed collection of graph edge weights.

**Theorem4.6, p.23; Proposition4.8, p.24.** The semilocal Sonin spaces are isomorphic through the specified maps to the archimedean Sonin space and a de Branges space of entire functions. The paper says **hilbertian**: the topological Hilbert-space structure is preserved, while the induced inner products depend onS. This should not be silently strengthened to a common isometry with bounds uniform as S grows.

**2403.01247v1, Proposition3.1, p.7.** For each such finiteS the corresponding moment problem is determinate. The proof uses the bounded finite-prime factor and gamma decay to obtain a Carleman-type bound. **Proposition2.1, p.3**, identifies the orthogonal polynomial with the characteristic polynomial of the finite compression of multiplication byx to lower-degree polynomials.

**Useful new test.** In a rooted representation of the infinite dessin/path algebra, compute the weighted closed-walk moments of a proposed symmetric nearest-neighbor/Jacobi operator. Compare them with the semilocal moments above, including∞. An all-moments identity plus determinacy would identify the cyclic spectral measure. A finite list of matching moments is a diagnostic, not that identity.

**Critical limitation.** This semilocal measure is absolutely continuous and has full real support; its multiplication operator is not a discrete operator whose spectrum is the zeta zeros. Real zeros of its finite orthogonal polynomials do not become zeta zeros merely by increasing the matrix size. The later conditioning, quotient and arithmetic convergence steps remain necessary. Positivity of this moment Hankel matrix also does not prove positivity of a different Newton-sum metric or the global Weil functional.

## 3. A proved determinant formula with explicit assumptions, and explicitly missing convergence

**Connes–Consani–Moscovici2511.22755v1, Theorem3.6, p.9.** The operator associated with the closed lower-bounded restricted Weil quadratic form on a fixed multiplicative interval has discrete lower-bounded spectrum. The compactness argument uses compact support and the archimedean logarithmic Fourier weight; finite-prime terms are bounded perturbations. This proves existence of the lowest eigenvalue. It does not prove it is simple or has the required parity.

**Theorem5.10, pp.23–24.** Fixλ>1 and a finite truncationN. Assume the smallest eigenvalue of the restricted form is simple, its eigenvectorξ is even, and normalize the specified boundary functional by δ_N(ξ)=1. The rank-one perturbation of the scaling operator is self-adjoint on the specified decomposition. On the finite quotient `E_N/Cξ`, the inner product is induced by the positive form `QW_λ^N-ε_N〈·,·〉`; it is not asserted to be self-adjoint for an arbitrary unchanged Euclidean metric. The theorem computes

`det_reg(D_log^(λ,N)-z) = -i λ^(-iz) ξ̂(z)`.

The Fourier transformξ̂ is entire with real zeros, equal to the spectrum in the theorem. The complement retains an explicit arithmetic-progression tail of the unperturbed circle spectrum. The proof computes the finite determinant ratio and the regularized circle determinant; this is a genuine infinite-operator regularized determinant calculation, not merely an algebraic determinant line.

**What remains open in the primary paper.** Section6, pp.25–26, reports high-precision numerical agreement. Section7, pp.27–31, proposes normalized determinant convergence; Lemma7.3, p.31, proves compact/closed-substrip convergence toXi for a specifically constructed prolate-based comparison function k_λ. It does **not** identify that function with the Weil ground-state eigenfunction. Section8, pp.32–33, explicitly leaves two tasks: prove the lowest infinite-dimensional Weil eigenvalue is simple with even eigenvector, and prove the comparison function sufficiently approximates that ground state, with normalization adequate for zero convergence. The latter is the arithmetic matching step.

Connes2602.04022v1, **§6.6, p.30**, repeats these remaining steps. The numerical digits and the paper's chance estimates are not a convergence theorem or a certified exhaustive matching of all zeros.

**Transfer.** A dessin-order spectral realization could aim to produce exactly this form, its quotient and boundary functional, or a unitarily equivalent construction with controlled normalization. Merely finding a self-adjoint cycle operator with plausible spacing does not yield the determinant formula. Even after finding a regularized determinant, convergence toXi needs a proved nonzero holomorphic limit on the relevant complex domain; convergence of selected real eigenvalues alone is insufficient.

## 4. The useful 2025 C*-positivity theorem is more specific than “a positive trace”

**Connes–van Suijlekom2511.23257v1, Corollary1.1, p.2.** A Hermitian positive-semidefinite Toeplitz matrix of size n+1 and rankn has a nonzero kernel vector whose associated polynomial has all roots on the unit circle. **Proposition2.1, pp.3–4**, constructs a positive functional on the specified Laurent-polynomial quotient; its GNS realization makes the class ofX unitary. This is a direct connection to cycle/Laurent algebras. Its rank-one kernel, Toeplitz moment structure and positive functional are essential; an arbitrary positive matrix does not satisfy the conclusion for an arbitrary kernel polynomial.

**Theorem5.6, p.11; Proposition5.10, p.12**, extend this mechanism to particular real symmetric matrices with divided-difference off-diagonal structure, prescribed symmetry, a one-dimensional even kernel and a simple diagonal spectral operator. This structure must be proved for the dessin-derived form, not inferred from gentleness.

**Theorem6.1, p.13**, is the precise infinite-dimensional statement. Start with a real distributionD on[0,L], define the form on trigonometric polynomials by the paper's equation(6), and assume it defines a lower-bounded **essentially self-adjoint** operator with a simple isolated bottom eigenvalue and an even eigenfunction. Then the eigenfunction's entire Fourier transform has only real zeros. The proof uses the trigonometric core, the spectral gap, finite compressions and compact-uniform Fourier convergence, followed by Hurwitz.

Do not quote only the looser introductory version. **Remark4.3, p.9**, explains why the distribution on[0,L] and its form construction matter: symmetrization of a distribution can lose endpoint data (the example is δ'_0). A formal even convolution kernel or a Friedrichs extension alone does not automatically verify the essential-self-adjointness/core hypothesis in Theorem6.1.

This theorem is a strong reusable operator result. Applying it to a function not yet proved to beXi gives real zeros of that function, not RH.

## 5. Weil positivity: exact arithmetic criterion versus available local inequalities

Connes2602.04022v1, **§4.1, pp.20–21**, records the classical criterion with its sign conventions. For the indicated compactly supported smooth multiplicative test functionsg, put `g*(x)=overline(g(x^(-1)))` and impose `ĝ(±i/2)=0`. Then RH is equivalent to

`Σ_v W_v(g*g*) ≤ 0`.

Equivalently, the negative of this functional is positive on that constrained space. The finite-prime terms contain `(log p)p^(-m/2)` at p^m andp^(-m). Every fixed compact-support test involves finitely many primes, but the criterion quantifies over **all** test functions/support sizes. Proving one truncation, many numerical positive matrices, or a bound with constants uncontrolled as support grows does not establish that universal condition.

The survey's **Theorem7.1, p.31**, restates an archimedean compression inequality on the specific small support interval `[2^(-1/2),2^(1/2)]`, with its stated transform vanishing at i/2 and0. Its positive Sonin trace is important, but it does not prove the corresponding all-place/all-support Weil inequality. **§7.4, p.32**, displays the semilocal trace representation, retaining the cutoff projections and normalization term. Replacing that signed/corrected expression by an arbitrary positive graph trace loses the equality being used.

For a completed order, a candidate Weil form must therefore reproduce the actual local distributions, pole-removal conditions, signs and archimedean finite parts before its positivity can be invoked as an RH criterion. This is an arithmetic comparison requirement, not a reason to assume the positivity premise.

## 6. Deninger supplies a compatible infinite-dynamical target, with important limitations

**Deninger1807.06400v4, Theorem6.1, pp.38–39**, constructs continuous-time systems from rational Witt-vector structures attached to the specified normal arithmetic schemes and admissible character classes. Closed points of finite residue field normNx correspond to **packets** of periodic orbits of length log(Nx). Individual orbits are not in one-to-one correspondence with primes. The introduction, pp.4–5, explicitly leaves cohomological and analytic structures unresolved; it is not a proved Lefschetz trace/determinant realization of the completed zeta function. A naive sum over every orbit in a packet can give the wrong multiplicities.

This is relevant to infinite dessin inverse systems or a graph/groupoid model: a functor preserving actual closed-point packets and Frobenius would be more meaningful than relabeling arbitrary graph cycles by primes. The 2023 *Primes, knots and periodic orbits* survey explains the analogy but explicitly says only some expected properties are realized.

**Deninger2204.02714v2, Theorem2.13, p.5**, gives a real-coefficient obstruction with exact scope. There is no functorial real-valued arithmetic cohomology theory for all number rings whose complexification has the stated central Artin-L zero multiplicities (property2.12). The proof uses symplectic Galois representations with root number−1: odd central multiplicity contradicts the parity forced by real representation theory. This is not a theorem that all self-adjoint RH models are impossible. It does rule out silently assigning ordinary real structures to a functorial full arithmetic theory while also demanding those multiplicity properties.

Properties2.1–2.7, pp.2–3, explain the missing positivity/purity mechanism: a derivationθ, trace/cup pairing, and an antilinear quaternionic-type star with positive scalar product would make `θ-1/2` skew-symmetric. That would give the desired real parts once the arithmetic spectral identification is established. These are hoped-for inputs, not consequences of ordinary AR duality or a surface intersection pairing. The paper points to twisted/complex/quaternionic structures as possibilities.

## 7. Recent geometry and trace-ideal technology: useful, but not an arithmetic determinant theorem

**Connes–Consani2602.15941v1, Theorem1.1, p.4**, identifies the Riemann adelic sector with a monoid of torsion-free rank-one groups equipped with the specified seminorm. Theorems1.3–1.4, pp.6–7, describe tensor/adelic-cover structures. This is relevant to arithmetic line objects and compatible towers. It is a singular Picard **monoid**, not an abelian variety with a proved polarization/Hodge index theorem. **§9.1–9.2, pp.39–41**, interpret the explicit formula via adelic isotropy and local-field transverse factors; **Theorem9.1,p.42**, recalls the semilocal crossed-product sheaf. None proves the global positive pairing that would establish RH. The function/distribution spaces and prime/∞ isotropy are additional structures beyond a formal determinant line of a locally gentle resolution.

**Ponge–Tian2605.25591v2, Theorem3.26, p.18**, characterizes measurability of operators in a specified weak Lorentz ideal by convergence of normalized eigenvalue sums. Its setup uses a continuous regularly varying functiong of index−1 with divergent integral and `G(t)=∫_0^t g`. **Theorem5.8, pp.27–28**, makes Weyl operators strongly measurable. These are useful for proving that a regularized/noncommutative integral attached to an infinite-order spectral model is well-defined and stable in the correct ideal. They do not supply an arithmetic spectral identification or a zeta-regularized holomorphic determinant.

**Proposition6.2,p.30**, explicitly **assumes RH** for the operator built from zeta-zero ordinates, obtaining spectral measurability of `|D|^(-1)` for `g(t)=(t+1)^(-1)log(t+2)`, with noncommutative integral1/π. It must not be used as an unconditional construction of the desired operator. Similarly Connes2602.04022v1, **Theorem7.3,p.32**, states its zeta-zero heat expansion under RH. Matching the leading Weyl law or heat coefficients leaves low spectral/arithmetic data undetermined.

## 8. Consequences specifically for locally gentle completions, graph C* and Leavitt methods

The following are deductions about the proposed interface, not claims that the cited authors constructed a dessin model.

### The completion and involution must be specified

An arrow-adic/profinite completion of a locally gentle order is not a C*-completion. Define the involution, representation, dense smooth algebra and topology; show any proposed map to an adelic crossed product is continuous in the relevant senses. An abstract algebraic equivalence, derived equivalence or K-theory identification does not identify the unbounded operator, its domain, the scaling time or the trace distribution.

### A graph C* algebra need not admit the intended finite trace

For a Cuntz-type vertex with n≥2 isometries satisfying `s_i*s_i=1` and `Σ_i s_i s_i*=1`, a normalized tracial state would satisfy `1=Σ_i τ(s_i s_i*)=Σ_i τ(s_i*s_i)=n`, a contradiction. Thus graph/Leavitt universality alone does not supply a finite faithful positive trace. Weights, semifinite traces or KMS states may be appropriate, but they have different trace/cyclicity/modular properties and need an explicit arithmetic comparison. A unitary-cycle component can supply a Laurent algebra/C(T) and an ordinary positive trace; that by itself still does not select the arithmetic Toeplitz kernel or Frobenius weights.

### Determinants are different objects

The Fuglede–Kadison determinant `exp(τ(log|T|))` is nonnegative real and loses the phase. It is not by itself a holomorphic scalar completed L-function. A holomorphic regularized/Fredholm determinant needs its own operator-ideal, domain, spectral-cut and normalization hypotheses. An algebraic determinant line of a perfect complex is line-valued; it needs a compatible trivialization and analytic realization before it becomes such a function. The 2025 zeta-triple result is useful precisely because it proves an actual determinant formula in a specified analytic model.

### Prime cycles need the full local arithmetic, not just unit modulus

For an unramified representationρ the desired factor has the form `det(1-p^(-s)ρ(Frob_p))^(-1)` (with inertia invariants and modified factors at ramified places). A graph cycle with unitary holonomy has unitary eigenvalues for a combinatorial reason. To identify its factor with this one, prove the arithmetic Frobenius correspondence, multiplicities, norm/log-time and ramification. Assigning `sqrt(p)` times a unitary as a “pure Frobenius” presupposes the spectral size rather than proving it for the arithmetic object. The∞-factor and conductor/functional equation must also be recovered; they are absent from a bare cycle-counting trace.

### AR/semi-invariant structure supplies a place to formulate the missing comparison

AR translation, Serre-type duality, semi-invariant weights or periodic projective resolutions can organize the coefficient category and its pairings. They do not automatically produce a positive Hermitian metric compatible with arithmetic scaling. A usable theorem would specify a functor from the chosen completed-order category to an adelic character sector, prove that its duality matches the relevant Fourier/functional-equation operation, and show that its pairing becomes the actual Weil form or the required positive ground-state quotient metric. This is a constructive target, not a blanket obstruction.

## 9. Concrete next research test

Work with one explicit infinite locally gentle dessin order and its chosen analytic representation, retaining the infinite completion rather than replacing it by a finite-dimensional algebra.

1. **Arithmetic character test.** Select one finite abelian extension/character sector (for example the quadratic character modulo5). Construct an actual map to the corresponding Connes–Consani adelic cover. For each unramified prime in a finite test set, prove the monodromy isχ(p), the period is log(p), and the local trace/determinant coefficient is the required one. Handle the ramified prime5 and∞ separately, with the character's parity and gamma factor. Testing finitely many primes is diagnostic; a functorial proof for all is the obligation.
2. **Moment/operator test.** Compare the rooted closed-walk/Jacobi moments with the correct finiteS adelic measure, including gamma. Prove the identity or exhibit the first mismatch. Establish essential self-adjointness on a named core and identify whether the spectrum is continuous or discrete.
3. **Weil-form test.** Transport the actual constrained Weil form, or a proved equivalent form, to the completed-order representation. Verify the divided-difference/Toeplitz structure needed for the2025 real-zero theorem, along with a simple even ground state and nonzero boundary normalization.
4. **Arithmetic determinant/convergence test.** Prove a normalized holomorphic determinant identity and a compact-uniform convergence statement to the completed target. Alternatively prove the universal Weil positivity with the full support/character quantifiers. Neither branch follows from the earlier finite diagnostics.

Items1–2 are realistic discriminating tests: they use the new literature to detect whether the dessin model has the correct arithmetic input before investing in a global positivity claim. Items3–4 remain substantial analytic/arithmetic obligations. The available primary work does not close them for the proposed completed orders and does not establish fullRH/GRH.

## Verification limits and reproducibility

Selected statements and their hypotheses were read from pinned primary PDFs, including relevant proofs and explicit open-step sections; theorem/page references were cross-checked against page boundaries. One key theorem page was rendered for its essential-self-adjointness/core wording. No claim of full independent proof certification of all primary articles is made. No supplied-source audit was repeated. The report contains no new theorem claiming RH.

Key PDF SHA-256 values:

- 2511.22755v1: c98d89f7fc999d038e15e80a9aaaee2af797c17711c4329ca7ce48ad49cb336b
- 2511.23257v1: fbe73c759babb7f34cecb2bc13221a4e28ab2816a7341d09ff1643b7d81369c4
- 2310.18423v2: 8bc197642ee9ca4f2393b6cbfd3db292be6a315ce76ad61bfb845d9fedb47f2e
- 2403.01247v1: 92cf4eb3ef8b1586a0c0ab15fa8f4bf2aa1492bd32c8943216edcb06183124d1
- 2501.06560v1: f200c41d6d772389528bb1de58ad7fe98fd8db807d72360d4311ecb3c44d2fe5
- 2602.15941v1: f40eb90d3d1f020e54c001812973b16e33b011776c24fb95c45dbbd3015a1223
- 2602.04022v1: 9b7a5cdd2d39453360f2899a4681ddb2862e9be51a1a89746a11674acbeb7eea
- 1807.06400v4: edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09
- 2204.02714v2: abef52f91f14b13f53602c5af2add8e657caffbcee984b288d3eaf8adca50e37
- 2605.25591v2: 5d4f5f27a424828ce999203b05e21ffd10dbbf792c9d50ba211801173ff12f9e
