# Independent review: Hodge Laplacians as an arithmetic determinant bridge

Date: 2026-11-03. Read-only mathematical review by `surface_completion_audit`. This report is a new generated artifact; no shared manuscript, script, Lean file, source clone, environment or existing output was changed. The statements below are independent deductions, not a GRH claim.

## Conclusion

The proposed finite-dimensional obstruction is correct. A parity superdeterminant built only from the positive Hodge Laplacian cancels all its nonzero spectral information. Its normalized version is identically one as a rational function; its shifted version retains only an Euler-characteristic power. This is a structural identity for every finite odd self-adjoint matrix, stronger than the special case of complexes.

There are three essential qualifications. First, a quotient is pointwise defined only where its denominator is nonzero; common zeros are removed by rational continuation. Second, ordinary determinants and degree-weighted torsion do retain spectral information and are not refuted by this cancellation theorem, but they require separate arithmetic comparison and normalization. Third, infinite-dimensional regularization cannot be inferred from finite Sylvester cancellation without analytic/domain hypotheses. An explicit unilateral-shift example below shows why even a trace-class difference alone does not justify a universal extension.

Positivity of the Hodge Laplacian supplies no theorem that its determinant equals an arithmetic L-function, or that the independent arithmetic chain endomorphism is pure. A parameter-dependent Hodge replacement can additionally destroy holomorphy.

## 1. Exact finite-dimensional statement and proof

Let `(C^bullet,d)` be a bounded complex of finite-dimensional complex vector spaces, with a positive Hermitian inner product on each degree and orthogonal total grading. Thus `d^2=0`, `d*` is the actual adjoint, and

`D=d+d*`, `Delta=D^2=dd*+d*d`.

Write `C_even = sum_(q even) C^q`, `C_odd = sum_(q odd) C^q`, with dimensions `e,o`. Since D reverses parity and is self-adjoint, there is an actual linear map `B:C_even -> C_odd` such that

`D = [0 B*; B 0]`, `Delta_even=B*B`, `Delta_odd=BB*`.

This block identity uses the sum of both differentials/adjoints adjacent to each degree; B need not be one differential of the original complex. It also holds for every arbitrary rectangular matrix B, without assuming a complex exists.

Sylvester's identity over C gives the polynomial identity

`det(I_e+z B*B) = det(I_o+z BB*)` for every complex z.

Consequently the normalized parity superdeterminant is the rational function one. At a common zero of these two polynomials the displayed raw quotient is `0/0`; “identically one” means its unique cancellation/meromorphic continuation, or its value wherever the denominator is nonzero. The inverse parity convention has the same conclusion.

For the shifted determinant the clean global polynomial identity is

`mu^o det(mu I_e+B*B) = mu^e det(mu I_o+BB*)`.

For `mu != 0`, obtain it by substituting `z=1/mu` in Sylvester and multiplying by the indicated powers of mu; polynomial continuation establishes it also at mu=0. Therefore

`det(mu I_e+Delta_even) / det(mu I_o+Delta_odd) = mu^(e-o)`

where the denominator is nonzero, and as a rational identity elsewhere. For real `mu>0` both determinants are strictly positive and the quotient is literally defined. It is not literally defined at every complex nonzero mu: if `mu=-lambda` for a positive eigenvalue shared by both parity blocks, both determinants vanish. This is a necessary precision correction to “for mu != 0” if that phrase is interpreted pointwise rather than as a rational identity.

A spectral proof makes the lost information explicit. If `B*B v=lambda v` with `lambda>0`, then B maps this eigenspace isomorphically to the lambda-eigenspace of BB*, with inverse `lambda^(-1) B*`. Thus all positive eigenvalues agree with multiplicity. Only kernel dimensions can differ, and

`e-o = dim ker B - dim ker B*`.

For a complex, finite Hodge decomposition identifies `ker Delta_q` with `H^q(C)`. Indeed `<Delta_q v,v>=||dv||^2+||d*v||^2`; a closed vector orthogonally decomposes into a boundary plus a vector annihilated by d*. Therefore `e-o = sum_q (-1)^q dim H^q(C) = chi(C)`. The shifted superdeterminant keeps the Euler characteristic, not a characteristic polynomial of an arithmetic Frobenius. The ratio of **primed** parity determinants, which omit zero eigenvalues, is exactly one.

An equivalent finite heat identity is

`Str(exp(-t Delta)) = chi(C)` for all t,

because positive eigenvalues cancel and zero eigenvalues contribute their parity difference. More generally a scalar function f defined on the finite spectrum gives `Str(f(Delta))=f(0) chi(C)`. This formulation includes the logarithmic derivative of the shifted determinant wherever defined.

## 2. Projective complexes require a realization before this construction

A finitely generated projective module over an arbitrary algebra is not intrinsically a finite-dimensional complex Hilbert space. There is no canonical positive Hermitian form, adjoint or positive ordinary Laplacian attached merely to such a projective module. A proposed use of the theorem must specify a realization over C (or a Hermitian vector-bundle fiber), its exactness/derived properties, and the metric. For a noncommutative algebra an arbitrary coordinate transpose is not an intrinsic module adjoint.

Once an actual finite-dimensional Hermitian realization is fixed, the cancellation theorem is automatic. It does not depend on how complicated or periodic the original projective resolution was. If the realization is infinite, the analytic discussion below is required instead. Tensoring an arbitrary resolution with a nonflat residue or coefficient module is not licensed by this theorem; derived specialization must retain its Tor terms.

## 3. Ordinary determinants retain spectrum but vary with the metric

Take the fixed exact cochain complex `0 -> C --1--> C -> 0` in degrees 0 and 1. Give degree zero the metric `h_0(v,w)=conj(v)w` and degree one the metric `h_1(v,w)=r conj(v)w`, where `r>0`. The adjoint of d=1 is d*=r. Hence both degree Laplacians are r.

The normalized parity ratio is `(1+zr)/(1+zr)=1` after cancellation, while the ordinary determinant on the total complex is `(1+zr)^2`. Its shifted version is `(mu+r)^2`, and its unshifted positive determinant is `r^2`. All these ordinary spectral quantities vary with r even though the based algebraic complex and its zero cohomology remain fixed.

Thus the ordinary Laplacian determinant is not determined by the quasi-isomorphism class of a bare complex. This does not make ordinary determinants useless: a geometrically specified metric can be meaningful. It proves that a claim of metric independence or arithmetic matching needs an additional theorem, not just exactness and positivity.

For a particularly simple arithmetic-data counterexample, take one vector space in degree zero with d=0. Its Laplacian is zero for every metric. On this same complex choose either chain endomorphism F=2 or F=3. Their characteristic determinants are `1-2u` and `1-3u`, while the normalized Laplacian determinant is one in both cases. The Laplacian cannot recover even this elementary independent endomorphism data.

## 4. Arithmetic chain endomorphisms are a different input

An arithmetic zeta construction uses a specified degree-preserving chain endomorphism F with `Fd=dF`, and the characteristic expression

`A_F(u) = product_q det(I-u F_q)^((-1)^q)`

(or its reciprocal under the customary zeta convention). Finite cohomological cancellation proves

`A_F(u) = product_q det(I-u H^q(F))^((-1)^q)`.

The remaining eigenvalues are those of the induced arithmetic F on cohomology, not the singular values of d. Replacing F by Delta changes this construction rather than making the same object positive. On cohomology the induced endomorphism of Delta is zero, so its normalized expression is one. The shifted expression induces only scalar multiplication by mu and gives `mu^chi`.

Even a heat regularization with F does not manufacture new arithmetic information. In the finite setting, `exp(-t Delta)` is a chain map inducing identity on cohomology. Therefore `F exp(-t Delta)` is a chain map and

`product_q det(I-u F_q exp(-t Delta_q))^((-1)^q) = A_F(u)`.

This follows by the same cohomological determinant theorem and does not require F to commute with d*: although the harmonic representative of a cohomology class may change under F, the induced cohomology map is still H(F). Assuming simultaneous F-invariant orthogonal splittings without justification would be stronger than necessary and generally wrong.

To deduce purity from a positive metric, one would need an identity such as `F* H F=q H` for the **same zero-bearing arithmetic F**. Mere positivity of `dd*+d*d` is unrelated to that assertion. Taking the unitary factor in a polar decomposition of F also changes its characteristic determinant in general.

A Hermitian pencil constructed from D can of course have its zeros on a chosen real spectral axis, and after a change of variable on a chosen vertical s-line. This is a legitimate spectral construction. A determinant-preserving identification with the intended completed L-function remains a separate research problem; it is not supplied by defining D from a resolution.

## 5. Degree-weighted torsion is not the parity superdeterminant

The degree weighting in analytic torsion prevents the simple pairwise cancellation above. With one conventional choice, the finite torsion number is

`T(C,h) = product_q (det' Delta_q)^(((-1)^(q+1) q)/2)`.

For comparison, if `zeta_q(w)=sum_(lambda>0) lambda^(-w)`, then `log det' Delta_q=-zeta_q'(0)` and `log T=(1/2) sum_q (-1)^q q zeta_q'(0)`. The original analytic definition and its finite combinatorial model appear in Ray–Singer, Definition 1.6 and Proposition 1.7, printed pp.149–150. [Primary paper](https://www.ms.uky.edu/~hislop/papers/ray-singer1.pdf).

The factor q is essential. A positive singular value of d_q occurs in Delta_q and Delta_(q+1), but their weighted exponents add to `(-1)^q/2`, rather than zero. If `P_q` denotes the product of the positive eigenvalues of `d_q* d_q`, then this convention gives `T=product_q P_q^(((-1)^q)/2)`.

For the exact two-term identity complex with metrics (1,r), this T equals `sqrt(r)`; it is nonconstant. For the standard-metric exact complex `C -> C^2 -> C`, with `d_0=(1,0)^t` and `d_1=(0,3)`, the Laplacians are `1`, `diag(1,9)`, `9`, and the same torsion convention gives `T=1/3`. Their ordinary parity determinant still cancels completely.

These finite metric examples do not refute Ray–Singer metric independence for closed manifolds under its stated geometric hypotheses: that theorem concerns an elliptic differential complex with correlated metric changes, spectral regularization and specified flat orthogonal coefficients, not arbitrary independent inner products on a fixed finite complex. The acyclic closed-manifold theorem is Ray–Singer Theorem 2.1, printed p.151. [Primary paper](https://www.ms.uky.edu/~hislop/papers/ray-singer1.pdf).

Torsion, determinant-line metrics and arithmetic special-value formulas can therefore be meaningful secondary invariants. The finite parity obstruction does not rule them out. But a torsion number or a special-value formula is not an all-variable determinant identity locating every nontrivial zero. A proposed torsion bridge needs its own precise variable, normalization, coefficient system and arithmetic comparison theorem.

## 6. A second obstruction: parameter-dependent adjoints need not be holomorphic

Suppose d(s) is holomorphic in a complex spectral parameter s. With a fixed positive metric, d(s)* depends on the conjugated matrix coefficients and is generally antiholomorphic. Consequently Delta(s)=d(s)d(s)*+d(s)*d(s) need not be holomorphic.

The scalar two-term family d(s)=s already gives `Delta_0(s)=Delta_1(s)=|s|^2`. The ordinary determinant `(1+z |s|^2)^2` is not holomorphic in s for fixed nonzero z. This defect would block a direct use of holomorphic compact-uniform convergence, Rouché or Hurwitz. It occurs independently of the parity cancellation issue.

A holomorphic matrix-valued function which is Hermitian at every point of a connected complex open domain is constant: its real diagonal entries are constant by the Cauchy–Riemann equations, while each off-diagonal entry is simultaneously holomorphic and the conjugate of a holomorphic entry, hence constant. Thus one should not demand both a nontrivially varying holomorphic operator family and pointwise self-adjointness on the whole complex domain.

A parameter-independent self-adjoint operator with holomorphic scalar spectral parameter in `D-zI` avoids this defect. Its arithmetic determinant identity and convergence must still be proved independently. A complex “formal transpose” can preserve holomorphy but supplies no positive Hermitian adjoint and therefore no automatic positivity theorem.

## 7. Infinite-dimensional scope: what does extend, and what does not

For a densely defined closed map B between Hilbert spaces, positive spectral pairing survives through polar decomposition: away from their kernels, `B*B` and `BB*` are unitarily equivalent on their spectral subspaces. However, defining determinants and traces requires more than this pairing.

Two sound extensions are:

1. If B is Hilbert–Schmidt, then `B*B` and `BB*` are trace class and their ordinary Fredholm determinants `det_F(I+z B*B)` and `det_F(I+z BB*)` agree. This is an extension with genuine determinant existence; it is not a theorem for every unbounded Laplacian.
2. For a self-adjoint odd elliptic-type D with finite-dimensional kernels and individually trace-class heat operators in each parity, positive spectra cancel in the heat trace. If the corresponding primed spectral zeta functions admit continuations regular at zero, with the same spectral cut and normalization, their determinants agree. For a positive scalar shift mu, including zero modes gives the quotient `mu^(dim ker B-dim ker B*)`. The exponent is the Fredholm index, not an undefined difference of two infinite ambient dimensions.

In either case, the hypotheses on domains, compactness/trace ideals, continuation and zero modes are part of the theorem. They cannot be imported merely because the original algebraic resolution is periodic.

Here is an explicit warning against a broader statement. Let B=S be the unilateral shift on `ell^2(N_0)`, and let P_0 be projection onto the first coordinate. Then

`B*B=I`, `BB*=I-P_0`, `index(B)=-1`.

Neither individual heat operator is trace class. Nevertheless their difference is rank one, and

`Tr(exp(-t B*B)-exp(-t BB*)) = -(1-exp(-t))`,

which is not the Fredholm index for finite positive t. Thus merely requiring a trace-class **difference** of heat operators is insufficient for the usual individual-trace cancellation argument. Subtracting divergent traces is a genuine additional regularization choice.

Likewise, for `z != -1`, the relative product on these identified Hilbert spaces is

`(I+z B*B)(I+z BB*)^(-1)=I+z P_0`,

whose Fredholm determinant is `1+z`. This is not the finite normalized superdeterminant one. It is a different relative determinant, available because the **product differs from identity** by a trace-class operator; the two individual factors have no ordinary Fredholm determinant. The calculation does not produce arithmetic data. It demonstrates why one must not claim that every conceivable infinite regularization is forced to equal the finite answer.

An infinite secondary invariant can depend on boundary conditions, continuous spectrum, renormalization or relative geometry. Such dependence must be defined and then compared to arithmetic; it cannot be declared either automatically canceled or automatically equal to an L-function. If a proposed regularization introduces an anomaly, the anomaly itself becomes an additional object requiring definition, invariance and arithmetic matching.

## 8. Independent exact checks and research implication

I imported the project's existing standard-library rational-matrix checker with a non-main run name, avoiding its shared output writer. For the rectangular matrix

`B=[[1,2,0],[0,1,3]]`,

I independently computed

`B*B=[[1,2,0],[2,5,3],[0,3,9]]`, `BB*=[[5,2],[2,10]]`.

Both normalized determinants are `1+15z+46z^2`. The shifted even determinant is `mu(mu^2+15mu+46)` and the odd determinant is `mu^2+15mu+46`, giving the predicted exponent one. Exact rational tests passed at five z values and six mu values, including zero for the cleared identity. The two-term metric calculation was also checked at r=1,2,3/2. These tests support the formulas; the universal proofs are the block decomposition, Sylvester identity and spectral pairing above. No new Lean declaration was read or compiled as part of this report; root is developing that separate artifact.

The route that fails is precise: replacing arithmetic/Cartan data by the **unweighted parity characteristic determinant of a finite Hodge Laplacian** cannot retain nonzero spectral data, and taking its ordinary determinant instead loses automatic invariance and arithmetic matching. This does not obstruct using Hodge theory to compute cohomology, to organize a metric on determinant lines, or to study degree-weighted/regularized torsion under established hypotheses. For a zero theorem, the productive remaining target is still a rigorously realized arithmetic endomorphism or flow, with a determinant identity and positivity proved for that same realization.

## Addendum: a constructive relative boundary realization of the Cartan ratio

The following replacement is valid and useful. It realizes each finite determinant as a relative Fredholm determinant supported at the boundary of a unilateral shift. This is a different construction from the canceled finite Hodge parity superdeterminant.

Let `H=ell^2(N_0) tensor C^r`, let S be the unilateral shift on the first factor, and put `P=P_0 tensor I_r`. For a finite complex r-by-r matrix M with `I_r-M` invertible, define bounded operators

`A_M=I-(S*S) tensor M = I tensor (I_r-M)`,

`C_M=I-(SS*) tensor M = P_0 tensor I_r + (I-P_0) tensor (I_r-M)`.

The tensor factors have the indicated order. Decompose H as its first coordinate fiber and its orthogonal complement. On the first fiber A_M acts by `I_r-M` while C_M acts by identity; on the complement both act by `I_r-M`. Thus both A_M and C_M are boundedly invertible exactly when `I_r-M` is invertible, and

`A_M C_M^(-1)=I-P_0 tensor M`.

This differs from identity by a rank-at-most-r operator. Its Fredholm determinant is therefore the actual finite boundary determinant

`R(M):=det_F(A_M C_M^(-1))=det(I_r-M)`.

The individual A_M and C_M generally have no ordinary Fredholm determinant, since their deviations from identity have infinite rank. The construction uses a relative product, not the quotient of two nonexistent individual determinants. In this special model the factors commute, so reversing multiplication order while retaining the same inverse does not matter; reversing the ratio to `C_M A_M^(-1)` gives `det(I_r-M)^(-1)`.

The right-hand side is a polynomial in the entries of M, and `det_F(I-P_0 tensor M)` is defined even if `I_r-M` is singular. This supplies a canonical polynomial continuation of R across that locus. The original quotient `A_M C_M^(-1)` is undefined at a singular `I_r-M`; the continuation must not be confused with a newly existing inverse there. For a holomorphic finite matrix family M(s), the continued relative boundary operator is a holomorphic finite-rank perturbation and its determinant is holomorphic.

Apply this to the permitted and forbidden arrow-state matrices U,V. On the locus where both original relative quotients exist,

`R(-V)/R(U)=det(I+V)/det(I-U)=det C_A`.

Using the polynomial continuation for the numerator extends this identity to points where `I+V` is singular but `I-U` is invertible. The quotient extends meromorphically across zeros of `det(I-U)`, with any numerator/denominator cancellations handled in the usual way. In the formal augmentation ring both determinants are units, so the formal identity is unchanged. The scalar node expression after equal-weight specialization and cancellation is `R(-z)/R(z)=(1+z)/(1-z)`; this z is a path weight, not the node's central parameter `t=x+y`.

This is an exact concrete relative operator realization of the finite Cartan formula. It does not establish self-adjointness or positivity for arbitrary U,V, and it adds no arithmetic Frobenius, gamma factor or completed-L identity. On the positive-length half-plane, the same finite cycle factors remain nonzero, so the previously proved Hurwitz/Rouché obstruction continues to apply. Moving the finite determinant into a shift boundary does not change its zeros or poles.

### Finite-section check and the precise continuity issue

There is no contradiction with finite-dimensional Sylvester cancellation. Let `S_N` be the shift on coordinates `0,...,N`, with the last vector sent to zero, where N>=1. Then

`S_N*S_N=I-P_N`, `S_NS_N*=I-P_0`.

The analogous finite relative product acts by `I-M` at the first boundary, by `(I-M)^(-1)` at the last boundary, and by identity at all intermediate fibers. Its determinant is exactly one. A finite shift has two boundaries; the infinite isometry retains only the first one.

Embed these finite products into the infinite space by adjoining identity on all remaining coordinates. Their difference from the limiting relative boundary operator is

`P_N tensor ((I-M)^(-1)-I)`.

It tends strongly to zero as N tends to infinity, but its trace norm is the constant finite-matrix value `||(I-M)^(-1)-I||_1`, which is nonzero whenever M is nonzero. Consequently the finite determinants, all equal to one, need not converge to the limiting boundary determinant `det(I-M)`. For the scalar M=1/2, the last boundary contributes 2 at every finite stage, whereas the limiting first-boundary determinant is 1/2. The disappearing boundary never becomes small in trace norm.

This gives a concrete instance of the exact missing analytic hypothesis: strong operator convergence does not ensure Fredholm determinant convergence. Any proposed infinite arithmetic implementation must specify the relevant relative model and prove convergence in a determinant-compatible topology, rather than appeal to finite sections alone.

## Final artifact validation: note, two paper additions, Lean and checker

Independently read the entire final research note `research/hodge-boundary-determinants.md` (79 lines), `lean-analytic/HodgeDeterminant.lean` (128 lines), and `scripts/check_hodge_determinants.py` (134 lines). Also read the complete new core subsections at `papers/resolutions-core.tex` lines 144–175 and the complete new Appendix F at `papers/resolutions-details.tex` lines 228–288. These are additions to, rather than replacements for, the earlier full article review.

The new artifacts faithfully express the mathematical results reviewed above. In particular:

- The finite cancellation theorem gives both the normalized identity and the cleared shifted polynomial identity. Its proof includes the extension at zero, while the quotient statement explicitly excludes pointwise division by zero.
- The metric counterexample describes the per-degree ordinary factor r-z; on the full two-term total space it would be squared. Nothing in the example requires confusing these two determinants.
- The nonholomorphy example has the correct directional difference quotients: 2+h along real h and -ih along imaginary increments ih at s=1.
- Harmonic representatives, arithmetic endomorphism data, degree-weighted torsion and their separate hypotheses remain distinguished. The Ray–Singer sign convention and imported scope are disclosed.
- The boundary construction explicitly defines the bounded shift, its initial projection and inverse blocks. Only a finite-support relative Fredholm determinant is used; nonexistent individual bulk Fredholm determinants are not divided.
- Singular I-M is handled by scalar polynomial continuation, not by asserting an operator inverse. General Cartan ratios have the stated numerator polynomial and denominator meromorphic scopes.
- The final-boundary finite-section formula, strong convergence and constant positive trace-norm gap are all correct. The shift heat-trace counterexample correctly warns against subtracting two individually divergent traces.
- The Hilbert–Schmidt positive-Gram Fredholm identity is given as a properly restricted contrast and is not applied to the bulk shift operators.
- Neither the note nor the new paper additions claim an arithmetic completed-L identity, positivity of the same arithmetic realization, or GRH.

One literal wording issue was sent to root and has now been corrected and independently reread: note line 49 says “Reversing the relative order inverts the determinant”, and details line 258 says “Reversing the relative product reverses the determinant”. The intended true operation is **swapping numerator and denominator**, from A_M C_M^(-1) to C_M A_M^(-1). Merely exchanging multiplication order to C_M^(-1) A_M does not invert the determinant; in this example the operators commute and that product is unchanged. This is an ambiguity of phrasing, not an error in the formulas or proof.

### Independent Lean compilation

Ran the project's pinned Lean 4.24.0/mathlib environment on `HodgeDeterminant.lean` with `-DwarningAsError=true`. It exited zero. All eleven declarations printed their exact types and axiom dependencies. `boundary_relative_product` depends only on `propext`; the remaining declarations print only `propext`, `Classical.choice` and `Quot.sound`. No `sorryAx` was present.

The kernel-checked scope matches the written disclosure:

1. Actual odd block-matrix squaring.
2. Both actual Gram matrices positive semidefinite.
3. The normalized Gram determinant identity.
4. The shifted matrix scalar factorization for nonzero mass.
5. The cleared shifted Gram determinant identity **assuming nonzero mass**.
6. The normalized quotient equal to one **assuming its denominator is nonzero**.
7. Positive one-dimensional target metrics for positive real r.
8. The one-dimensional weighted-adjoint matrix identity for d=I and source metric I.
9. The per-degree ordinary factor r-z.
10. The distinct zero behavior for r=1 and r=4.
11. A universal noncommutative ring product identity with explicit commutation and right-inverse hypotheses.

The last lemma does not require P to be a projection for its algebraic identity. In the actual Hilbert-space application, P is a projection and the full inverse block formula is supplied independently in prose. The file does not formalize an arbitrary Hilbert complex, its harmonic/cohomology theorem, the extension at mass zero, the unilateral shift on mathlib Hilbert space, Fredholm determinants, strong convergence or trace norms. Those boundaries are accurately stated in the research note and Appendix F.

### Independent exact checker run without shared writes

Imported the checker with a non-main run name and called only `complex_checks()` and `boundary_checks()`. Its `run()` writer was never invoked, so `outputs/checks/2026-11-03-hodge/exact-checks.json` was not overwritten by this review. Both calls passed.

Returned counts: 15 complex/metric systems, 60 normalized determinant identities, 60 cleared shifted determinant identities, 30 positive-mass quotient identities, and 24 scalar boundary samples. The five examples have the expected Betti data: interval (1,0), circle (1,1), filled triangle (1,0,0), augmented triangle all zero, and the additional example (1,1,1). The metric construction really changes to orthonormal coordinates for the positive diagonal metric H=diag(r_j^2), so the transpose used after that change is the appropriate real adjoint. The test includes mass zero only in the cleared identity and restricts scalar division to positive masses where both determinants are explicitly checked positive.

For scalar boundary weights 1/2,1/3,-1/2,2 and dimensions N=2,...,7, the code constructs the actual finite shift and its two Gram products, computes the relative inverse exactly, checks determinant one, verifies the rank-one terminal defect and its diagonal trace norm. These are deterministic Fraction calculations, not floating-point spectral evidence. The last weight is allowed to be nonpositive in I-M; no positive-operator conclusion is inferred from it.

No new substantive theorem or code-scope error was identified. This focused validation does not independently rerun root's full 137-declaration suite or PDF builds, and does not substitute for them.

Reviewed artifact snapshot hashes (the author may subsequently clarify the two wording locations):

- `research/hodge-boundary-determinants.md`: 11138 bytes, 79 lines, SHA-256 `9b8546995ebf8ef9eeea5b3d0e09b3096817a32248a5357fe514ecbd1366aafd`.
- `lean-analytic/HodgeDeterminant.lean`: 5755 bytes, 128 lines, SHA-256 `c6451b5294ae5c5a90478c0fd8236ade7ee0bb86750c8a5d159942f013aa753f`.
- `scripts/check_hodge_determinants.py`: 6723 bytes, 134 lines, SHA-256 `d657c35063c477c39029965bf57b535ea0aef115827fdd0747983b4f00366ede`.
- `papers/resolutions-core.tex`: 29871 bytes, 241 lines, SHA-256 `be284e8c9dc8cd3f9518368c53c0f0255accc962bdc98912d722939e4e5e1465`.
- `papers/resolutions-details.tex`: 41491 bytes, 288 lines, SHA-256 `ff9d8d2a57a21d607f24da03c996ad12fd5677be1275233cc88bf758059ce4d8`.

Final wording resolution: the note line 49 and Appendix F line 258 now explicitly swap the relative pair to `C_M A_M^(-1)` and state that merely reordering multiplication does not invert the determinant. The correction is mathematically precise. There are no outstanding substantive or literal wording findings from this focused artifact review.

Final corrected snapshot updates:
- `research/hodge-boundary-determinants.md`: 11138 bytes, SHA-256 `9b8546995ebf8ef9eeea5b3d0e09b3096817a32248a5357fe514ecbd1366aafd`.
- `papers/resolutions-details.tex`: 41491 bytes, SHA-256 `ff9d8d2a57a21d607f24da03c996ad12fd5677be1275233cc88bf758059ce4d8`.
