# Independent review: actual two-pivot Jacobi gauge — PASS

5 November 2026. Reviewed exact `quadratic-phase/TWO_PIVOT_APPLICATION-v3.md` (SHA256 f1113869c23041e1f12b3d7869559e670234cec9a4b5188c33e0f030f7ff30d4), including sections1–5, with an independent reconstruction of the local residue convention and two-pivot normalization. Version3 removes only the literal EOF artifact from preserved version2; no mathematical change occurred. No canonical source or old experiment was edited or rerun.

## What is new in this project connection

The four-term quadratic phase is ALREADY in `research/reciprocity-period.md` §2, with the same inverse-different delta=1+2omega pairing, Gaussian proof, mod4 table and finite Lean components. The classical Gauss/Jacobi product and norm are ALREADY proved in `papers/theta-jacobi-core.tex` and reviewed under `planning/reviews/jacobi/`. This review caught that overlap before any new old-phase table was run. Neither fact is a new phase/norm theorem or historical CM priority claim.

The surviving application is the exact two-pivot completion of the actual h1 signed kernel, identifying its squarefree Mobius/Jacobi column weight with an explicitly constructed fixed-conductor angular Hecke character, while preserving the actual Fourier weight. This is a reformulation and a precise failed shortcut; it proves no signed upper saving.

## Independent local derivation and orientation

For z=x+yomega, Tr(z/(delta beta))=(-b*x+a*y)/Nbeta, beta=a+bomega. For the positive RAW sextic symbol at a good prime ideal p of norm n, reduction of chi(z) in O/p is z^((n-1)/6). Therefore j(p)=J(chi,chi²) belongs to O and reduces to the finite-field sum of x^s(1-x)^(2s), s=(n-1)/6. Its expanded exponents lie strictly between0 and n-1, so the sum vanishes. Thus j(p) lies in the SAME prime ideal p. All three characters chi,chi²,chi³ are nontrivial; the elementary Gauss product and norm give N(j(p))=n. Consequently (j(p))=p. This also applies to an inert prime of norm p²; it does not require the rational norm to be squarefree. Inverting the character conjugates j and changes a split ideal to its conjugate.

The old theta section uses rho=chi², eta=chi³ and signed j_theta=-eta(-1)J(rho,eta). Dividing Gauss products gives J(chi,chi²)=J(chi²,chi³), since Gchi*Gchi5/Gchi3²=chi(-1)/chi³(-1)=1. The raw j is therefore exactly the old RAW J, not silently its signed Frobenius normalization.

Primary-source cross-check: Weil, *Numbers of solutions of equations in finite fields*, printed pp.499–502, gives the classical finite-field character/Gauss/Jacobi method. Its homogeneous notation is not substituted for the project's signed normalization; the derivation above fixes that explicitly. [Primary paper](https://math.ucr.edu/~res/math205B-2021/app2number-theory/weil-conjectures1949.pdf). The project's pinned [mathlib Jacobi implementation](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/NumberTheory/JacobiSum/Basic.lean) supplies an additional primary definition/norm reference; this review did not compile Lean or claim a new kernel theorem.

## Explicit finite ray and exact conductor

Let f=(2delta), norm12. In the character VALUE ring modulo delta, sixth roots satisfy v=v³ and v²=1. Removing both raw zero branches first gives j(p)=-1 modulo delta. Modulo2, v=v⁴, and J(chi⁴,chi²)=-chi⁴(-1)=-1 because the two characters are inverse and nontrivial. Therefore -j(p)=1 modulo f. These reductions are distinct from reduction in O/p used for the ideal orientation.

The six units map bijectively to (O/f)^*: the mod2 map has kernel{1,-1}, the moddelta map kernel mu3, their intersection is1, and the target has6 elements. Since O is a PID, every ideal prime to f has a unique generator Psi(a)=1 modulo f. Products of such generators are again normalized, proving multiplicativity. For a principal ideal(alpha), Psi((alpha))=alpha/u_f(alpha), where u_f(alpha) is the unique unit in its residue class. This constructs the algebraic Hecke character of infinity type(1,0); its unitary normalization is Psi(a)/sqrt(Na). At each good prime, uniqueness gives Psi(p)=-j(p).

The finite conductor is exactly f: it divides f by the principal formula; a proper divisor divides either(2) or(delta). The first admits the nonidentity unit -1 congruent1 and the second the nonidentity unit omega congruent1. The type-one principal value would assign these unit ideals values -1 or omega instead of1, a contradiction. Thus both prime factors are necessary. On squarefree good s ONLY, mu(s)j(s)=Psi(s). For repeated prime factors mu(s)=0 while Psi(s) is nonzero; no extension of this identity beyond the squarefree columns is allowed.

This fixed conductor belongs to the NEW COLUMN GAUGE. The source row character theta and its nontrivial powers remain primitive at the growing squarefree q; their raw q/S/collision zeros are not changed. Additional S-primes remain deleted even though Psi itself is unramified there.

## Actual completion, generator changes and the missing estimate

With h1 and q=rt not1, two-variable inversion has factor Q^-2 and first two transforms tau(theta)tau(theta²). The product is tau(xi_q)*j(r)*conjugate(j(t)), with NO extra xi_q(-1). CRT Jacobi sums have no additive-generator multiplier. After b(s)=Psi(s)c(s)/sqrt(Ns) on squarefree columns and tau(xi_q)=sqrt(Q)*gamma(beta), the exact scalar is gamma(beta)/Q. Inserting the full-six-variable sign xi_q(-1) here would be wrong.

All nonunit-frequency transforms vanish by primitivity; no inverse character is evaluated at such a frequency. The common F retains sharp capacity, squarefree/pairwise/fixed-factor/ray conditions and arbitrary v6 overlaps. Restrictions depending on the orientation must remain outside common F. The uncompleted factor theta(Z) retains every common-prime zero, even for v6 raised to the sixth power. A6=1 does not justify setting every permitted literal v6 representative to1.

Replacing beta by u*beta multiplies tau(xi) by xi(u). Reindexing the two frequency variables multiplies T by the same sign, so their product is invariant; j and Psi themselves do not depend on the additive generator. The counting-measure Cauchy budget is sqrt(phi(q))/(D*Q) times the orientation coefficient norm and ||B2||2. Neither a uniform product-fiber count nor the finite gamma phase justifies treating the actual B2 as independent of the columns or deleting its coherent mean.

If the second pivot is literally fixed to a unit c, its inverse transform contributes theta(c)²*tau(conjugate(theta²)). Pairing with tau(theta²) gives Q, returning EXACTLY the old one-pivot tau(theta)/Q formula. If c is a nonunit, both the original slice and its primitive transform vanish. The extra completion therefore provides no free cancellation in the pure-A1 length-one limit.

The column gauge is diagonal unitary. It preserves every arbitrary-coefficient operator norm, including matrices with the original masks/capacity entries. Exploiting the actual fixed Hecke-twisted coefficients and coupled T before absolute conductor sums is still an OPEN signed estimate. No improved7/6 envelope, target H bound, determinant, zero-location or GRH result follows. Full remaining h, signed C-C/C-mu/mu-mu and principal/residue assembly remain separate obligations.

## Fresh finite evidence and acceptance limits

`exact-jacobi-controls-v1.json` passes642 new exact assertions on six local fields: split conjugate pairs of norms7/31 and inert norms25/121. It checks the literal positive character, ideal orientation, conjugation, all six additive-generator associates, the new two-pivot mixed/zero-frequency identity, and four direct CRT cases of norms49/961/775/5425. The repeated rational norms49/961 are ideal-squarefree examples. Raw zero branches at both Jacobi endpoints are retained; restoring them changes the value/norm. Arithmetic uses integer pairs in Z[omega] and exact Gauss polynomials in Z[omega][zeta_p], reduced by Phi_p. No floating complex signs are used.

`exact-ray-extension-v1.json` adds58 bounded assertions using those SAVED j-values: all six ray classes/units, each -j normalized modulo2delta, equality to the old raw J(rho,eta), six product/repeated-ideal controls, and the proper-divisor unit obstructions. Total700 fresh assertions; no old991 or reciprocity-period run was imported or executed. These corroborate the exact derivation; they do not establish an analytic distribution estimate.

Acceptance criteria satisfied: exact old/new normalization identified; positive versus inverse orientation explicit; inert and rational-nonsquarefree norms retained; growing-conductor raw masks unchanged; common-F and length-one limits explicit; exact f12 proof supplied; mu*j identity restricted to squarefree support; no analytic gain claimed. Future acceptance of a signed improvement requires a quantitative bound on the actual coupled h,q,K or two-pivot sum with fixed-profile derivative/ray/cutoff uniformity, plus the remaining signed/residue assembly.
