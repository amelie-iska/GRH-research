# Independent short-row hybrid-energy review

Date: 2026-11-03. Read-only mathematical review. No shared manuscript, planning, Lean or source-clone files were changed. No MCP, authentication, installation or push was used.

## Result and actionable finding

The stated completed quadratic reduction and quadratic–cubic hybrid bound survive this review, relative to the cited classical quadratic and cubic large-sieve theorems. Both complete Möbius masks, the squarefree bad-prime parts, divisor-Cauchy losses and coefficient independence are handled in the displayed proof. I found no counterexample to those stated inequalities.

There is, however, a concrete unconditional obstruction to the next tempting strengthening: the completed bound's `(K+NB)` factor cannot uniformly be replaced by `K`, or have its `NB` contribution reduced by a fixed power, while retaining arbitrary bounded coefficients. This obstruction uses a fixed nonunit arithmetic row, not the zero row or a missing collision mask. A short-row advance must exploit additional structure of the actual reflected theta coefficients; further manipulation of an arbitrary bounded β cannot supply it. The precise construction is in Section 5 below.

A smaller literal correction is recorded in Section 4: the final assertion that subunit quotient ranges are empty needs qualification under annular comparison constants. The existing bounded-range convention repairs it with no exponent loss.

## 1. Immutable source and actual coverage

Main source: `math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, git blob `268c4e3206d460c617d3d2129742a72b831b3def`, SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

Read the current `research/reflected-identity.md` completely, and Section 5 (plus surrounding scope) of `research/exponent-frontier.md`, before inspecting the target. Source coverage in this pass: 2672–2840 and 7484–7657 in full; additionally 2530–2676 for the imported quadratic sieve and profile context, 584–610 for the fixed excluded set, and the immediate reflected-energy application around 7657–7760 and 7950–8050. This is a review of the specific hybrid arithmetic step, not another certification of the upstream theta reflection or the already checked local phase/cube extraction.

Primary sieve sources checked:

- Goldmakher–Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642v2, 31 May 2012, Definition 1 and Theorem 1.1 on PDF pages 1–2. [Pinned PDF](https://arxiv.org/pdf/1112.1642v2). Downloaded only to `/tmp/grh-shortrow-goldmakher-louvel-v2.pdf`; SHA256 `5cc5f03388d3996b4333f07be51f989f60779fe172f8bd24c7aa6ddad64dd304`.
- Heath-Brown, *Kummer's conjecture for cubic Gauss sums*, Theorem 2 on PDF pages 3–4, using the author's Oxford archive copy (26 pages). [Oxford PDF](https://ora.ox.ac.uk/objects/uuid:16c3966e-61cb-499d-839c-559b3794fcff/files/m502494cff282fae8a90f44a466f2b941). `/tmp/grh-shortrow-heath-brown-kummer.pdf`, SHA256 `54a1148394a5de1a22dee153f60411aeb0c8775a7fea090da6b1720ebbe915ad`. This file's metadata records a 2005 TeX production date; it should not be mislabeled a newly verified publisher version.

GL requires a primitive quadratic Hecke family, trivial infinite type, a finite reciprocity class map, and primitive product conductor ab for coprime indices in the same class. Its two summation indices are squarefree ideals prime to a fixed modulus. The source's family verification at 2650–2672 addresses these hypotheses, including the primary-unit adjustment, common ramified factor and finite class partition; transpose duality supplies the displayed orientation. No assumption of squarefree rational norm is present.

HB's theorem has arbitrary complex coefficients and both indices squarefree as Eisenstein elements congruent to one modulo three. It includes the `U+V+(UV)^(2/3)` term, with no exclusion of rational prime factors. Its statement therefore permits the source's squarefree cubic row j to retain primes of the fixed S other than λ. Conjugation and cubic reciprocity give the orientation used here. Neither imported upper bound assumes GRH. This pass checks their statements/hypothesis match; it does not reprove their full papers.

## 2. Completed quadratic reduction: proof audit

Write b=gt², with g squarefree, and c=(n,g), n=cm, g=ch. Then c,m,h are pairwise coprime and squarefree. The proof correctly allows g and t to share primes; squarefree extraction does not imply they are coprime. The exact zero-preserving identity at 2732–2739 is

    χ_k(nb)^3 = χ_k(mh)^3 · 1_(k,ct)=1.

Here the expression on the right means multiplication by the coprimality indicator. In particular it retains the zero at a prime dividing c or t even when its exponent in nb has become even.

Cauchy over t costs O(T) in the squared row norm. At fixed t, `(k,t)=1` is a fixed row restriction. The entire remaining indicator `(k,c)=1` is expanded as the sum of μ(r) over r|(k,c). Rowwise divisor Cauchy gives only a small norm power. After k=rk′ and c=rc′, `(k′,r)=1` and `(k′,t)=1` are fixed row restrictions and `(c′,r)=1` is a column restriction. There is no extra `(k′,c′)=1` indicator in an individual summand. Reinstating one would not be justified; the source explicitly avoids that mistake.

The factor χ_r(mh)^3 is bounded and independent of k′. Splitting the squarefree S-parts of m and h leaves finitely many possibilities because S is fixed independently of Z and all current rows/averaged labels (584–605). Their symbols can be removed as fixed bounded row scalars. The good product j=m_g h_g is squarefree, so GL applies with lengths K/q_r and O(NG/C²). It would be incorrect to discard those S-parts from the original support or to leave them inside the GL good column. The proof does neither.

Grouping columns by j costs a divisor factor for its factorization into m_g,h_g and O(C/q_r) for c′. This yields the stated coefficient-square sum for arbitrary complex β, not just bounded β. The latter generality is important in the hybrid application, where β is multiplied by an inner P′-sum before this reduction.

For bounded β, the count of triples is O((C/q_r)(N/C)(G/C)). Combining both C/q_r factors, the O(r_0) possible r in a dyad, and the two t factors gives the displayed `NB/r_0 · (K/r_0+NG/C²)`. Consequently the completed norm bound `(K+NB)NB` follows after logarithmically many blocks and a rescaling of ε. These counts remain valid at the unit dyad with fixed comparison constants.

## 3. Hybrid norm: both complete masks and final powers

The first complete mask is `(P,k)=1` at 7544–7575. Its full Möbius expansion, rowwise Cauchy and substitutions P=DP′, k=Dk′ are valid. The induced coefficient β_D retains χ_D(nb)^3, χ_D(n)^(-2) and `(D,b)=1`, and is independent of k′ and P′. The extracted inverse root contributes exactly q_D^(-1) after squaring. No mask `(P′,k′)=1` may be inserted after Cauchy; its original cancellation belongs to the completed divisor sum. The source expressly does not insert it.

The second complete mask is the c-collision already treated by the completed quadratic reduction. The P′-sum is an arbitrary coefficient independent of k′, so the reduction applies. After c=rc′, its factorization at 7610–7616 is valid at collisions: χ_P′(r)^(-2) supplies the zero at r, χ_P′(c′m)^(-2) supplies the zeros at c′ and m, and the remaining indicator `(P′,ht)=1` handles h and t. No zero has been replaced by a unit character.

Only after this is a positive coefficient-square sum may |β_D|² be discarded. For fixed h,t,D,r, the P′ coefficients are independent of the cubic row j=c′m=n/r. They have bounded weighted square mass because q_P′ is in its annulus and the number of such ideals is O(L/q_D), with bounded scales handled separately. The grouping multiplicity of c′,m is divisor-bounded. The cubic sieve now applies to squarefree j and P′, retaining the permitted bad primes of j. The mask at ht is fixed in this application and is a coefficient restriction, not an arbitrary row–column mask.

The bookkeeping is consistent. T·#t, the factor C/r_0, and the h-count G/C combine to B/r_0. The O(r_0) choices of r cancel that denominator. On a D-dyad, Σ_D 1/q_D=O(1). The two sieve factors are

    K/(D_0 r_0)+NG/C²,
    N/r_0+L/D_0+(NL/(r_0D_0))^(2/3).

Bounding D_0,r_0 below by the fixed unit convention and using NG/C²≪NB gives exactly

    (KNBL)^ε (K+NB) B [N+L+(NL)^(2/3)].

Thus this arithmetic hybrid implication is supported by the cited unconditional sieve theorems and the stated fixed-data/coefficient hypotheses. It does not certify the prior arithmetic theta identification, the later global moment closure, or the short-row input MS_h.

## 4. Minor literal range correction

Source line 7652 says that subunit quotient ranges are empty. A quotient *scale* below one need not have an empty actual annulus. For example take L=4, a good prime D of norm 7, and P=D in the annulus 4≤q_P<8. Then P′=1 is retained although L/q_D=4/7<1. Such D-summands legitimately occur after the complete mask expansion even when original overlap terms later cancel.

The accurate statement is: a range whose actual upper endpoint is below one is empty; all remaining bounded quotient scales must retain the unit ideal and may use max(1,scale) as the sieve length. This is already the convention at 2718–2719 and 2774–2777. Thus the strict literal sentence needs qualification, but the proof can use its existing convention and loses no power. No protected source edit was made.

## 5. Concrete sharpness obstruction for arbitrary β

Fix one squarefree good nonunit row k_0. If allowed by the fixed S, take its primary generator π=1+3ω of norm 7. Set K=q_(k_0), restrict the row support to {k_0}, and set N=L=1 with n=P=1, a(1)=1. Choose the fixed coefficient sequence

    β(1,b)=χ_(k_0)(b)^3

on a B-annulus. This sequence is independent of the variable row and P: k_0 is selected once as part of the example. All hypotheses of the stated arbitrary-coefficient lemma permit this choice and this fixed row restriction. Since χ_(k_0)^3 is the zero-extended real quadratic character, the selected row sum is exactly

    Σ_(q_b~B) χ_(k_0)(b)^6
      = #{primary b in the annulus : (b,k_0)=1}.

All masks involving P=1 are one. The count is ≍B by elementary lattice counting in finitely many residue classes; no PNT or GRH is needed. Hence the energy is ≍B², whereas a hypothetical K-only replacement of the completed factor would give O_ε(KB^(1+ε)), false for any fixed ε<1. More generally replacing B in K+B by B^(1−δ) fails for ε<δ. This is a nonunit-row counterexample, so deleting the unit row cannot repair such a proposed uniform improvement.

For the norm-7 example, write b=a+cω with a≡1 mod 3 and c≡0 mod 3, so N(b)=a²−ac+c² and b mod π is a+2c mod 7. In the annulus B≤N(b)<2B the coprime count is

    (4π/(21√3)) B + O(√B+1).

The constant follows from the area of the norm ellipse, the index-nine primary congruence lattice, and exclusion of one of seven residue classes. An exact integer enumeration in memory gave amplitudes 7,24,91,359,1411,5664 at B=16,64,256,1024,4096,16384, respectively. Their squares are the exact row energies. The asymptotic proves the obstruction; these finite counts only check its concrete realization. No script or shared output artifact was written.

This does not assert that the actual normalized theta coefficient β from reflection equals this adversarial sequence. It identifies the missing ingredient accurately: a further advance must preserve and exploit that actual arithmetic coefficient, prove cancellation against the relevant quadratic rows, or change the decomposition/estimate. A uniform theorem for arbitrary bounded β with the same masks cannot provide the missing power. It is therefore appropriate to close the present hybrid large-sieve sub-obligation in classical prose while leaving the genuine short-row moment target, theta input and arithmetic spectral bridge open.

## 6. Independent review of a new genuine large-gcd partial MS estimate

The proposed partial result is valid after explicitly separating the diagonal and specifying the smooth majorant. The necessary correction is that the uniform primitive-character estimate applies only off the diagonal; a diagonal pair has principal residual character and a contribution of order H. The final advertised H=D^(3/4) conclusion survives this correction.

### Precise hypotheses

Let H,D≥1, let Φ be a fixed globally nonnegative radial Schwartz function on C with Φ≥1 on the unit disk (a compactly supported smooth choice suffices), and let |c_n|≤1 be supported on squarefree S-good primary ideals in a fixed annulus q_n~D, independent of the element row u. For either common orientation ε=±1, consider

    E_Φ(H,D)=D⁻¹ Σ_(u∈O) Φ(u/√H) |Σ_n c_n χ_n(u)^ε|².

The zero row can be removed separately; for D bounded away from the unit support its contribution is already zero. This is the smoothed majorant of the all-element-row raw moment at source 12356–12362. It is not a theorem for arbitrary row-dependent coefficients or the scale-supremum variant needed later in amplification.

“Smooth and ≥1 on the unit ball” alone is insufficient: global nonnegativity is needed for majorization, and Schwartz decay or compact support is needed for the sums and Fourier bounds. These are routine hypotheses to impose, but should be stated.

### Exact common-factor mask and conductor

For an off-diagonal pair, write n=ha and m=hb with h=(n,m). Because n,m are squarefree, h,a,b are pairwise coprime and squarefree. The original character product is

    χ_n(u)^ε overline(χ_m(u)^ε)
      = ψ_(a,b)(u) · 1_(u,h)=1,
    ψ_(a,b)(u)=χ_a(u)^ε overline(χ_b(u)^ε).

The indicator notation again means the coprimality indicator. Since a,b are coprime and not both one, this raw residue character is primitive nonprincipal with conductor ideal ab. At each prime dividing a or b its local exponent is ±1, so no local character becomes principal. Its conductor norm is Q=q_aq_b~D²/G² when q_h~G.

No equality of the ray classes of a and b is necessary here: we sum raw characters on the full element lattice, not a unit-trivial ideal character on an arbitrary ray sector. If a later argument restricts rows to a sector or introduces row weights, that is a different claim requiring its own treatment. Radial unit symmetry can make some raw sums vanish, but this extra cancellation is not needed for the bound.

Complete Möbius inversion of the mask gives, with d the fixed primary generator of each divisor ideal,

    K_(n,m)=Σ_(d|h) μ(d) ψ_(a,b)(d)
               Σ_(v∈O) ψ_(a,b)(v) Φ(dv/√H).

This is exact including collisions. Since (d,ab)=1, ψ_(a,b)(d) has modulus one; no conductor factor or nonunit correction is lost. Radiality changes the inner scale to X=H/q_d without introducing an angular weight.

### Uniform Poisson bound at every scale

For any primitive nonprincipal raw character ψ of conductor norm Q and any X>0,

    |Σ_(v∈O) ψ(v) Φ(v/√X)| ≪_Φ √Q.

Here is the scale calculation. Expand into residue classes modulo the conductor and apply ordinary two-dimensional lattice Poisson. The Fourier coefficient of a primitive character has magnitude √Q at unit frequencies and zero at nonunits; in particular its zero-frequency coefficient vanishes. Up to fixed lattice-covolume and different factors, the absolute value is bounded by

    (X/√Q) Σ_(0≠k∈O) |Φ̂(√(X/Q) · Rk)|,

where R is a rotation. A fixed Euclidean dual-lattice rescaling is harmless. Uniformly for t>0 and all rotations,

    Σ_(k≠0) |Φ̂(tRk)| ≪_Φ t⁻².

For t≤1 this is elementary lattice counting and Schwartz decay. For t≥1, omit the absent zero vector and use a decay exponent greater than two; the resulting bound is O(t^(-A))≤O(t⁻²). Thus no additive “1” remains to create a false X/√Q term at large X. This proves the bound uniformly in X=H/q_d, even far below one or far above Q, with no GRH assumption.

Consequently every off-diagonal pair satisfies

    |K_(n,m)| ≪_Φ τ(h) √Q ≪_Φ τ(h) D/G.

This uses the original complete common-factor mask, not a character with its zeros suppressed.

### Diagonal correction and normalized count

The preceding statement fails for n=m: then a=b=1, ψ is principal, Q=1, and the smoothed sum is generally of order H rather than O(τ(h)). It must be treated separately. Its contribution to E_Φ is at most

    D⁻¹ Σ_n |c_n|² Σ_u Φ(u/√H) ≪_Φ H,

because there are O(D) columns and H≥1. Coprimality only decreases this diagonal positive sum.

For q_h~G, the number of off-diagonal ordered pairs is O(D²/G): there are O(G) choices of h and O(D/G) choices for each residual column. Fixed annular comparisons and the unit dyad are retained. Together with the factor D⁻¹ in the original normalized Gram and τ(h)≪_εD^ε, this gives

    D⁻¹ Σ_(n≠m, q_(n,m)~G) |c_n c_m K_(n,m)|
       ≪_(Φ,ε) D^(2+ε)/G².

Geometric summation of the dyads q_(n,m)≥G_0 yields O(D^(2+ε)/G_0²). Therefore the correct complete high-gcd contribution, including its diagonal when present, is

    O_(Φ,ε)(H + D^(2+ε)/G_0²).

With H=D^(3/4) and G_0=D^(5/8), this is O_(Φ,ε)(H D^ε), as proposed. More generally the same balance is G_0=D/√H within the nonempty gcd range.

The off-diagonal high-gcd piece need not itself be a positive Gram form. The displayed absolute estimate controls it and is enough to reduce the desired moment to the remaining small-gcd pairs; one must not claim it can be deleted by positivity. The unresolved h=1 pairs still number O(D²), with Q~D²; taking absolute values through this same argument gives O(D²) after normalization, far above D^(3/4). The new result is therefore a genuine, unconditional partial reduction, not the full MS_(3/4) estimate or its scale-supremum form.

This review introduces no new external analytic hypothesis beyond ordinary lattice Poisson, Schwartz bounds and the primitive Gauss identity already checked in the project. No source edit, numerical experiment or Lean verification was performed for this appended result.
