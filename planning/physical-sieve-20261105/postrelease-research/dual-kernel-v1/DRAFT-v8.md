# Exact squarefree-row Poisson kernel before the source's absolute Cauchy step

DRAFT v8 (v1--v7 preserved; independently requested good-dual-factor notation guard). New research after the frozen physical-sieve application; EXCLUDED from the current release. This is an actual-weight identity and a failed bound attempt, not an improved estimate. A final attempt receipt and independent review will follow the root's public-release confirmation. No prior arithmetic/control table is rerun.

## 1. What is new in this attempt

The already reviewed input was de Faveri, arXiv:2610.04045v1, Theorem 1.1. Here the relevant additional proof is Lemma 3.1 (Poisson), Lemma 3.3 (root-number splitting), the exact expressions before (4.3)--(4.4), and the passage from the first display of Section 5 to the inequalities (5.1)--(5.3). I read the proof, not just the introduction. The local PDF/text have the previously pinned hashes; full third-party sources stay in the private local cache.

There are TWO different absolute steps. In Lemma 4.4, after opening a positive energy, the proof takes absolute values separately in the gcd d and finite classes. In Section 5 it inserts an absolute value in each dual a' fibre, Mellin-separates the product conductor, and then uses |S1| |S2| and Cauchy. Our original h=1 form already has coprime columns, so its first gcd-sort variable is 1. The new question is whether the exact preceding dual expression can exploit the actual A_U coefficients before either dual-fibre absolute values or square-divisor absolute values. It cannot be answered by the already accepted arbitrary-coefficient norm theorem alone.

The source's b-sharp cross-root couplings vanish when its two COLUMN indices are squarefree. This simplifies that one part of the proof; it does not remove the actual row squarefree/coprime/capacity filters or prove cancellation of the original coefficients.

Precisely, source (3.3) defines b*=rad(b) and b-sharp=b/b*, with b-sharp supported on b*. For b=product p^e (0<=e<=5), b-sharp=product p^(max(e-1,0)). Lemma 3.3 is

    eps(chi-tilde_{b1,b2})
      = eta beta_b1 conjugate(beta_b2)
          chi_{b1-sharp}(b2*) conjugate(chi_{b2-sharp}(b1*)),  (1.1)

for coprime sixth-power-free b1,b2 in the SAME source class, using the primitive character of Lemma 2.4. Here m,n are SF, so their sharp parts are 1. In the opposite dual orientation the actual physical a=v1 v2^2 is sixth-power-free but NOT generally squarefree: a*=v1v2 and a-sharp=v2. Transposing this physical index into the source's column position restores the two cross terms in (1.1). Neither a* nor a can replace the other's norm: physical Na=Nv1 Nv2^2, while the good conductor is Nv1 Nv2. The simplification in one orientation is not an assertion that the physical mixed family is squarefree.


## 2. Actual form, coefficients and all masks

Work over O=Z[omega], with the original fixed S above 2 and 3, fixed finite-order nu, and ONE common possibly complex smooth W supported in [1,2]. D>1. All m below are original good squarefree IDEALS with D<=Nm<=2D, weighted by W(Nm/D); this includes distinct conjugate ideals and norm-duplicate ideals separately. There is no restriction to selected conductors or selected norm fibres.

The actual coefficient is

    c_m = A_U(m) nu(m) (u0/m)_6 W(Nm/D),
    A_U(m) = sum_{ab|m,(a,b)=1,Na,Nb<=U} mu(a)mu(b).

No factorization of A_U(dm) is introduced. In the original high window it is legitimate to rewrite A_U(m)=mu(m)(r_U(m)-1) on the active annulus; consequently c_m conjugate(c_n) ALREADY includes the complete mu(mn) sign for coprime columns. No additional mu(q) is inserted and none is deleted. The ternary formula, not a proxy coefficient or a rough-prime +/-1 formula, is the definition throughout.

Fix the A6=1 two-pivot block

    u=u0 alpha(v1) alpha(v2)^2,
    A1<=Nv1<2A1, A2<=Nv2<2A2,
    v1,v2 good squarefree, (v1,v2)=1,
    Nu0 Nv1 Nv2^2 <= H.

Literal unit/S/ray class data are fixed, as in the original family. Write any additional actual fixed ray projectors explicitly. The following formulas describe the unweighted actual rows; arbitrary inserted row weights are NOT covered by a classical norm assertion. For the pure block v2 is the literal unit. If v2 is nonunit, every one of its original raw column collision zeros remains.

With R_m(v)=(alpha(v)/m)_6, extended by the literal zero when (v,m)>1, the exact original signed numerator is

    D S1^AA = sum_{v2 actual} sum_{v1 actual(v2)}
                 sum_{(m,n)=1} c_m conjugate(c_n)
                    R_m(v1 v2^2) conjugate(R_n(v1 v2^2)).       (2.1)

The common smooth W is inside c_m and conjugate(c_n), including its complex phases. No orientation average, orientation mean, equal-norm fibre, primitive-conductor mask or capacity boundary has been removed. On the stated nonprincipal pure/mixed blocks no principal row is being subtracted to create this form. This is only the h=1 slice; other gcd slices are not bounded by its sign or by positivity.

## 3. An exact square-divisor row expansion, before Poisson

For a fixed good squarefree v2, let I(v2) be the exact interval of allowed INTEGER norm nodes for v1:

    a(v2)=ceil(A1),
    b(v2)=min(ceil(2A1)-1, floor(H/(Nu0 Nv2^2))).

If b<a the row fibre is empty. Let s be any one fixed C-infinity step, s(t)=0 for t<=0 and s(t)=1 for t>=1. The auxiliary function

    G_v2(x)=s(4(A1*x-a+1/2)) s(4(b+1/2-A1*x))                 (3.1)

is EXACTLY 1 or 0 at every ideal norm node x=Nv1/A1 according to the original inequalities, including the capacity endpoint. It is smooth and compactly supported, but its normalized derivatives cost O_j(A1^j). It is a device for expressing the SHARP row restriction; it is not the original column profile W, and it must not be called a scale-uniform fixed smooth weight.

For any function B(v1) of finite norm support, elementary ideal-divisor inversion gives

    sum_{v1 good} mu(v1)^2 1_{(v1,v2)=1} B(v1)
     = sum_{k good squarefree,(k,v2)=1} mu(k)
         sum_{ell|v2} mu(ell) sum_{z good} B(k^2 ell z).        (3.2)

All sums in (3.2) are finite when B has the original support. Proof: first use mu(v)^2=sum_{k^2|v}mu(k). The condition (v,v2)=1 forces (k,v2)=1. Then write v=k^2 y and use 1_{(y,v2)=1}=sum_{ell|(y,v2)}mu(ell), giving y=ell z. Notice that k and ell are coprime, while z need NOT be squarefree and may overlap either. This exact expansion must not be replaced by an original-SF-column enumeration that discards auxiliary non-SF z or k^2 ell z. It is a row expansion, not a new column family.

Taking B(v1)=G_v2(Nv1/A1) times the complete character/ray factor gives (2.1) exactly. When a ray character rho is inserted, its prefactor rho(k^2 ell) is also kept after v1=k^2 ell z; it can be included in the finite coefficient h_rho, and is not deleted. For a term with t=k^2 ell and L=A1/Nt, the inner sum has shape

    sum_{z good} G_v2(Nz/L) theta_{m,n}(z)

times theta_{m,n}(t) and the v2^2 factor, plus the explicitly retained finite ray projector. Here theta is the primitive-product family character only after its finite reciprocity factor is accounted for. If m or n meets k ell v2, the original raw prefactor is zero. These zero terms are retained as zeros; they are not restored to units. Nonempty t obey Nt<=2A1, so L>=1/2, with the L<1 cases being unit residual fibres, not a below-range sieve invocation.

## 4. Exact finite ray/S organization

The accepted source family is used here only as notation for its functional equation, not re-audited as a new application. Reciprocity gives R_m(v)=alpha([v],[m]) chi_m(v) on coprime good arguments; at a collision both raw sides are zero. For each column-class pair C1,C2, the finite factor

    alpha([v],C1) conjugate(alpha([v],C2))

is a function of the finite ray-class group. Expand this function, AND every original fixed ray restriction on v, in its full finite character basis. Do not select one convenient class and call it the whole form. Denote a resulting finite ray character by rho and its exact finite coefficient by h_rho(C1,C2; other fixed data).

For (m,n)=1, both good squarefree, let eta_{m,n,rho} be the primitive ray character inducing rho chi_m conjugate(chi_n), let f_{m,n,rho} be its conductor and let eps_{m,n,rho} be its root number. Every good prime of mn occurs with nontrivial local exponent +/-1, so

    f_{m,n,rho} = f_S(C1,C2,rho) mn,

with the finite S component retained exactly. There is no conductor drop at a good prime, and no replacement of mn by a rational norm or merged norm fibre. The finite S component is permitted to depend on the displayed classes; its value is not silently declared 1.

The good-z mask is still present. Put P_S=product_{p in S}p. Remove it, when desired for Poisson, by the exact finite sum

    sum_{z good} G(Nz/L) eta(z)
     = sum_{e|P_S} mu(e) eta(e)
          sum_{y integral} G(Ny/(L/Ne)) eta(y).               (4.1)

If an S-prime is in the primitive conductor, eta(e)=0 on the corresponding terms, as required. No value of the ORIGINAL raw symbol at a forbidden S-prime is invented: eta in (4.1) is the displayed primitive extension, while the finite sum restores the original mask.

## 5. The surviving exact pre-Cauchy Poisson lemma

For each nonzero term above, eta is nontrivial: the original annular columns exceed the unit, and coprime columns have disjoint nonempty good supports. Hence de Faveri Lemma 3.1 applies. With L_e=L/Ne and dotG the transform (3.1) of THAT auxiliary row function (with the field Gamma factors),

    sum_y G(Ny/L_e) eta(y)
      = eps(eta) L_e/sqrt(Nf)
            sum_y dotG(L_e Ny/Nf) conjugate(eta(y)).          (5.1)

The formula is exact for every finite D and auxiliary G from (3.1). Although the source chooses a nonnegative majorant for its inequalities, the Mellin-functional-equation identity is linear for any smooth compactly supported G. Equivalently write G as the difference of two admissible nonnegative majorants; no positivity is invoked to infer an order relation for our coprime form. The dual sum converges rapidly for fixed D; its decay constants include the actual growing derivatives of G. Equation (5.1), inserted in (3.2), is an exact representation of (2.1), with coefficients

    mu(k) mu(ell) mu(e) h_rho,
    c_m conjugate(c_n),
    original raw prefactors at t v2^2,
    eta(e), eps(eta), L_e/sqrt(Nf),
    and the full dual factor dotG(L_e Ny/Nf) conjugate(eta(y)).

No absolute value or Cauchy has yet been used. All (k,ell,e,v2,rho,C1,C2,m,n,y) sums and their equal-norm fibres remain coupled. This is a mean-retaining exact lemma, not a new saving. A useful final theorem would need a bound for this WHOLE signed expression, including the transform's real derivative cost or a justified sharp-endpoint method.

Every root number in (5.1) has absolute value 1 ONLY because eta there is the primitive character at f, with its own primitive additive normalization. It is not a Gauss sum at the original physical row modulus or at any higher induced modulus. At a good prime p=(pi) of norm P, choose compatible local primitive additive characters psi_j and psi_1 with psi_1(x)=psi_j(pi^(j-1)x). If xi is nontrivial primitive modulo p and is lifted to p^j, j>=2, grouping a residue by its lift shows the raw sum with primitive additive character modulo p^j is zero. More generally, with additive frequency k, the raw sum is zero unless v_p(k)=j-1; in that case it is

    P^(j-1) conjugate(xi(k/pi^(j-1))) tau_{p,psi_1}(xi),

and it is again zero for k divisible by p^j. Proof: sum first over the P^(j-1) lifts of each nonzero residue modulo p. This includes cubic/lower-order xi; its order does not repair imprimitive-modulus zeros. No division by a zero Gauss sum or automatic square-root-of-the-physical-modulus formula occurs in (5.1). If more general higher local conductor exponents at S occur, f and the corresponding primitive local factors are kept instead of this simplified good-prime example.

A particularly transparent component is C1=C2=C and rho trivial, before the finite S e-sum. Source Lemma 3.3 applies exactly. Because m,n are squarefree, m-sharp=n-sharp=1, so

    eps(eta_{m,n})=eta_C beta_m conjugate(beta_n),
    Nf=Nm Nn.                                               (5.2)

The relevant expression is therefore a coprime quadratic form with actual Gauss-root-twisted coefficients, a product-norm transform, and conjugated raw dual characters. The root phases beta_m are not discarded and are not asserted to be a fixed angular Hecke character. There is no proposed gauge-only saving. For the other class/rho components (5.1) keeps the actual primitive root number, rather than extending (5.2) without proof.

For a fixed smooth row weight with a genuinely uniform transform, Mellin separation would split dotG(L Ny/(Nm Nn)) into product-norm powers and a dual character quadratic form. BEFORE taking absolute values it is a bilinear integral, not a positive norm. Its product-conductor dependence and complex Mellin weights are part of the exact expression. The source passes to fibrewise absolute values in (5.1)--(5.2), then to |S1| |S2| in (5.3), and finally Cauchy. Those operations control arbitrary coefficients, but cannot establish extra cancellation of this specified c_m without an additional signed estimate.

### 5.1 The explicit bilinear Mellin kernel that Cauchy would discard

In the same-column-class/trivial-rho component (5.2), fix k,ell,v2 and an original S-removal term e. Put t=k^2 ell, L=A1/Nt, L_e=L/Ne. Let h_0 be the EXACT scalar coefficient of rho=1 in the finite row-ray expansion of Section 4. Its dependence on the fixed data/v2/classes is retained. The signed outer coefficient is

    mu(k) mu(ell) mu(e) h_0.                                 (5.2a)

It occurs ONCE outside the integral. In particular none of these signs is inserted in both column vectors, where it would incorrectly square away. Without any extra row-ray restriction the constant coefficient is 1 on this same-class component.

The DUAL ideal in (5.1) must ALSO be split exactly as y=h z with h supported on S and z good, as in the source's Section 5 (printed page 15). The h sum is retained, not silently removed. Here eta=chi^(m) conjugate(chi^(n)) by source (3.5). Consequently eta(e) and conjugate(eta(h)) factor, and we define LITERALLY

    a_m(e,h)=c_m beta_m R_m(t v2^2)
                  chi^(m)(e) conjugate(chi^(m)(h)),
    b_m(s;e,h)=a_m(e,h) (Nm)^(s-1/2).                         (5.2b)

These chi^(m) values are the primitive local factors in source (3.4); they are not invented values of the original raw symbol at S. For same-class columns, the finite reciprocity factors cancel in R_m(t) conjugate(R_n(t)), so using the raw R_m(t v2^2) in (5.2b) has the exact product required by (5.1). All collision zeros at k ell v2 remain in this coefficient. Its c_m is the ORIGINAL A_U/nu/u0/common-complex-W coefficient. The fixed-h factors are column phases, not a finite-order assertion about chi^(m).

Let psi be one fixed smooth nonincreasing cutoff, equal to 1 on [0,1] and to 0 on [2,infinity). Put V(x)=psi(x)-psi(2x), take K=2^j for j=0,1,2,..., and use sum_j V(x/2^j)=1 for EVERY x>=1. Thus V is supported in [1/2,2] and the norm-one UNIT is included (V(1)=1). Define

    B_K(s;e,h)=sum_{z good} V(Nz/K) (Nz)^(-s)
             sum_{m,n in C,(m,n)=1}
                 b_m(s;e,h) conjugate(b_n(conjugate(s);e,h))
                       conjugate(chi_m(z)) chi_n(z).         (5.3)

The z sum is finite at every K and uses the original raw zero convention on good z. The EXACT contribution of the FIXED k,ell,v2,e to the numerator is

    mu(k) mu(ell) mu(e) h_0 eta_C
      * sum_{h S-supported} sum_{K=2^j,j>=0} 1/(2 pi i)
          integral_(Re s=sigma) Ghat_v2(1-s) gamma_field(s)
                 L_e^(1-s) (Nh)^(-s) B_K(s;e,h) ds.           (5.4)

Here gamma_field(s) is the FIELD Gamma/discriminant factor from source (3.1), independent of the dyadic scale K. Equations (5.2a)--(5.4) show every outer sign and the scale L_e explicitly; they are not schematic reinsertion instructions. Sum (5.4) over all the displayed actual k,ell,v2,e and all same column classes to obtain precisely this factorized component of (2.1). The GENERAL rho or unequal-column-class components remain the primitive-root formula (5.1), with their exact h_rho, rho(t), f_S and root number; (5.4) is not asserted for them by analogy.

The b_n argument in (5.3) is conjugate(s), not s: the product norm power is (Nm Nn)^(s-1/2). Consequently (5.3) is a bilinear pairing between b(s;e,h) and b(conjugate(s);e,h), and is not a Hermitian positive quadratic form away from the real Mellin axis. All equal-norm ideal fibres remain distinct in both vectors.

No analytic continuation of an inverse-L series is invoked. For a DIRECT absolute interchange of all h,K sums with the vertical integral, use sigma>1. If 0<sigma<=1 is used instead, first integrate each finite (h,K) dual block, THEN sum the resulting transform values in h,K. Those resulting values give the rapidly convergent Poisson sum for each fixed D. One must not interchange absolute integrands at sigma<=1 without a further bound. This ordered identity asserts NO uniform sharp-interpolant tail or finite Mellin-height truncation.

This locates the requested missing estimate more finely than simply renaming S1: it is the signed (k,ell,v2,e,rho)-coupled bilinear integral (5.4) together with all general components (5.1), with the actual root-number coefficient and exact product-norm Mellin power. The source replaces this by absolute values and then Cauchy between the two coefficient vectors. Our attempted substitution of its available arbitrary-coefficient norms gives Section 7's worse powers. No bound on the coupled actual expression with the necessary cancellation is obtained by that substitution.

The non-discardable mean is visible without a variance calculation. The dual UNIT y=O (h=z=O) belongs to the exact sum and gives

    sum_{m,n in C,(m,n)=1}
          b_m(s;e,O) conjugate(b_n(conjugate(s);e,O)),         (5.5)

with the same outer factor mu(k)mu(ell)mu(e)h_0 eta_C and all original raw prefactor masks. More generally a GOOD dual ideal y=z^6 with h=O gives character value 1 on coprime columns and 0 on colliding columns; this statement does not replace the primitive local factors for h supported on S. These terms are not zero by the fact that eta is nontrivial. Only the ZERO IDEAL (0), which is not in the integral-ideal sum and whose character value would vanish, is absent from the source. There is no justification for deleting the unit/sixth-power dual modes or centering (5.3). They can cancel with other complete components only through an estimate of the actual signed expression.

## 6. Test of the cubic norm-compression idea

The cubic application in the source's Section 1.3.4 and Section 8 gains by combining variables after conjugation. The sextic mixed block has a different physical exponent. In THIS section let z be the GOOD dual factor after y_full=h z. The S-supported h is fixed and RETAINED in the primitive local column phases of (5.2b); the raw symbol R_m is never evaluated at a forbidden S-prime. On coprime arguments, and with the zeros also agreeing at collisions,

    R_m(v2^2) conjugate(R_m(z))
       = conjugate(R_m(z v2^4)).                             (6.1)

Thus the post-Poisson GOOD physical radicand in this component is z v2^4, not z v2, z v2^2 or rad(z v2). One must retain sixth-power extraction and its common-prime mask if overlaps create sixth powers. For the clean k=ell=e=h=1 same-class/trivial-rho fixed-smooth-row model, a typical coprime conductor has norm about D^2, so the nominal dual length is

    Y=D^2/A1.

At the mixed witness (A1,A2)=(D^(5/12),D^(1/6)), the nominal fixed-smooth-model physical norm calculation is Y A2^4=D^(9/4), versus original H=D^(3/4). At the pure witness the nominal scale is Y=D^(5/4), versus D^(3/4). These are exact exponent calculations WITHIN THE STATED nominal fixed-smooth model. They are not literal finite dual supports for the actual sharp interpolant G_v2, whose derivative constants grow as A1^j and whose dual transform has an infinite tail. The calculation explains the failure of this cubic-style norm compression; it does not prove that the actual signed dual sum is large.

The additional exact k,ell factors do not restore a small physical norm: inversion changes the original k^2 ell factor to k^4 ell^5 in the dual raw character (after finite reciprocity factors). They MUST remain together with their mu signs. No radicalization is allowed.

## 7. Quantitative result of trying only the available norm envelope

This paragraph is deliberately a best-case comparison for the smooth, factorable same-class/trivial-rho/e=h=1 component, not an unconditional new bound for the original sharp form or for the other S/ray components. Suppose one gives the transformed weight a uniform dyadic decay bound, Mellin-separates it with no power cost, and then bounds every actual dual coefficient sequence by the already accepted arbitrary-coefficient envelopes. Even with these optimistic concessions, the signed structure does not improve.

For an all-ideal dual row sum of nominal length Y, the positive comparison is the global envelope

    Phi(Y,D)=Y+D Y^(1/6)+Y^(5/6)D^(1/3)+Y^(1/3)D^(5/6),

NOT F6(Y,D) without sixth-power extraction. With ||c||_2^2 << B_W^2 D^(1+epsilon), the normalization of (5.1) gives a nominal normalized contribution

    (L/D) Phi(D^2/L,D)
       = D + D^(1/3)L^(5/6) + D L^(1/6) + D^(1/2)L^(2/3).    (7.1)

Coprime columns cannot be discarded from a quadratic form by positivity. If a norm comparison is made here, it must again use exact divisor inversion and absolute bounds on the resulting positive forms, with the actual beta_{da} A_U(da) coefficients, raw (d,y) masks, and their norm bounds. Such a comparison has the same displayed powers (up to epsilon losses), not a cancellation gain. This statement is only about how the available norm bounds act on (5.1); it is not an independent derivation of them for arbitrary row weights.

For the k=1 component, treating each v2 separately costs A2. At the pure witness, (7.1) has maximal power 9/8, already worse than the reviewed direct 13/12 bound. At the mixed witness it gives 89/72, again worse than 13/12. Combining v2^4 into the physical variable is worse still; at the mixed witness it reaches support D^(9/4). These numbers concern a failed upper-bound route, never an error lower bound. More generally, write A1=D^a, A2=D^b with a,b>=0 and a+2b<=3/4 (fixed u0 constants stay in (3.1)). The optimistic k=1 power in the separate-v2 route is

    b+max(1, 1/3+5a/6, 1+a/6, 1/2+2a/3).                (7.1a)

Thus the calculation applies to actual neighboring capacity-permitted blocks, rather than only two handpicked points. Exact dyadic endpoints and the factor Nu0 remain in (3.1); power notation does not change the family.

If one now also takes the absolute triangle in k, with L=A1/(Nk)^2, the available ideal count gives

    sum_{Nk <= sqrt(2A1)} (7.1)
       << D sqrt(A1) + D^(1/3) A1^(5/6)
          + D^(1/2) A1^(2/3),                               (7.2)

up to epsilon factors. The D L^(1/6) term also sums to D sqrt(A1). The remaining ell divisors cost only a divisor factor for this comparison. The final L in [1/2,1) terms have only the unit residual and cost at most the D-per-term bound; a sieve is not used below length 1. Summing v2 gives leading D A2 sqrt(A1)=D sqrt(H), power 11/8 at BOTH witness scales. This is another loss, not a result improving 13/12. On the neighboring critical face a+2b=3/4, the first term has power 1+a/2+b=11/8 throughout. Off that face the displayed general powers apply; no extrapolation to impermissible capacity blocks is made.

For the actual exact interpolant (3.1), the transformed-weight constants are worse than the optimistic assumptions just used. It would be incorrect to claim a uniformly bounded dual length D^2/L from fixed-weight rapid decay while hiding the O_j(A1^j) constants. The identity (5.1) survives without that claim.

## 8. The concrete missing joint estimate

Let P_D be the full right side obtained by inserting (5.1) into (3.2) and (2.1), with EVERY finite class/rho/e component, signed k/ell coefficients, product norm, root number, primitive conductor, full raw zeros and exact auxiliary G_v2. It is explicitly defined by the preceding finite-conductor/rapid-dual formulas. The target required in these unweighted blocks is

    |P_D| <<_{S,nu,W,epsilon} D H (HD)^epsilon.              (JK)

This retains the orientation mean and every equal-norm fibre; it is the original actual numerator, not a centered replacement. A usable weaker intermediate would bound the full (k,ell,v2)-coupled root-number quadratic integral at a scale between 13/12 and 3/4. No such estimate is proved here. An arbitrary-coefficient large sieve controls the magnitude after the source's absolute steps, not (JK) with a power gain for c_m. The fact that the columns are squarefree removes one root coupling but leaves the prescribed Gauss-root coefficient, coprime truncation and squarefree-row inversion coupled.

The surviving result is the exact pre-Cauchy representation (3.2),(4.1),(5.1), plus the demonstrated failure of a direct cubic-style physical norm compression and of a norm-only dual bound. It is not evidence that (JK) is false. It supplies no new exponent, no fixed-profile counterexample, no variance-only bound, no scalar prime/Mertens hypothesis, no inverse-L argument, no determinant theorem, no Lean or GRH claim. Root's current canonical theorem and release remain unchanged.
