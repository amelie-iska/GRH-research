# Cubic transposition of actual signed common-divisor bands

NEW research-only v2 (v1 preserved; concurrent explicit Schur input pinned), 6 November 2026. This proves a scoped quantitative norm comparison for an actual-weight auxiliary divisor-band component. It does NOT obtain cancellation from the sign mu(d), improve the whole signed13/12/global9/8 bounds, or solve the remaining intermediate/high dual problem. No old controls or numerical tables are rerun.

## 1. Scope, notation and the new result

Use the current intermediate-kernel HANDOFF-v1 (bb9463e0...), accepted aggregate5470159d..., the exact primitive Poisson representation DRAFT-v8 plus its required two-pivot scope addendum, the proved global root law25ad1b4a..., and the accepted arbitrary-coefficient Phi norm. All are inputs, not new audits. The external input below is the ALREADY PINNED de Faveri arXiv2610.04045v1 Theorem1.1, now with n=3 and its primary-generator Example2.2; this is an application, not a new sieve.

Work over O=Z[omega], with the original fixed S/ray/source data, fixed unitary nu, original cutoff1<=U<=sqrt(D), D>1, and ONE common possibly complex W in C_c^infinity((0,infinity)), supported in[1,2]. Original columns are the COMPLETE good squarefree IDEAL annulus, with distinct equal-norm/conjugate ideals separate. The actual coefficient remains

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_{rs|m,(r,s)=1,Nr,Ns<=U}mu(r)mu(s).

Rows are ONLY the original UNWEIGHTED two-pivot sector v3=v4=v5=v6=O, fixed literal u0 unit/S-supported with NO good-prime support, actual SF/coprime v1,v2 and literal/ray/exact capacity restrictions. Additional good frozen factors or varying-u0 assembly are not covered.

Fix ONE source class C on both original columns and the rho=1 component of the original finite row-ray expansion. Thus the primitive product has no S conductor factor and the inherited root extension is kappa_C beta_m conjugate(beta_n). Keep the exact original finite pre-S cutoff K_ell=sqrt(b(v2)/Nell), all finite e/ell terms, sharp-capacity profile G_v2, and every dual ideal y=h z, h S-supported and z good. No zero or orientation mean is centered or removed.

After the accepted AUXILIARY individual-column extension, insert the EXACT coprime-column identity sum_{d|m,n}mu(d). For1<=E<=D/2 define P_E,C^id(Y,2Y] by keeping E<Nd<=2E AND [d]=1 in the FIXED source class group. It is the corresponding signed summand of that fixed gcd-inversion representation, including ALL modes with Y<Ny<=2Y. It contains auxiliary off-coprime column pairs; it is not their primitive character/root number and is not a positive physical energy. Summing every divisor and every class is required to recover the original coprime form. We do not bound such a sum by one component.

Set L=D/E (so L>=2), and

    Theta3(E,L)=E+L+(EL)^(2/3),
    Phi(Z,L)=Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6),
    M(W)=(1/(2pi))integral_R |What(it)|dt,
    What(s)=integral_0^infinity W(x)x^s dx/x.

M(W) is finite and controls ||W||infinity. It is a fixed Mellin seminorm of the ORIGINAL column W, not a derivative-uniformity claim for the nodal row G. It can be bounded by a constant times the L1(dx/x) norms of W and (x d/dx)^2 W.

For every FIXED0<sigma<1/2 and epsilon>0 the new comparison is

    |P_E,C^id(Y,2Y]|/D
      << M(W)^2 (DYA2)^epsilon
         A2 A1^(1-sigma) D^(2sigma-1) Y^(-sigma)
         min{Phi(Y,L), (Y/E)Theta3(E,L)},  Y>=1.          (1)

Constants depend only on the stated fixed data, sigma and epsilon. They are not uniform at sigma=0 or1/2. A last partial band satisfies the same comparison. The first branch is the existing positive-d Phi method restricted to this d band. The SECOND branch is the new cubic d-by-residual-column transposition proved below; it applies to the actual A_U and sharp-capacity representation after a finite, endpoint-controlled Schur separation.

The new branch is a genuine partial norm improvement. For example, E comparable to D^(2/3), L comparable to D^(1/3), gives Theta3(E,L)/E=O(1). Hence the inner comparator becomes O(Y), whereas Phi(Y,L) is larger by a positive power when Y=D^gamma with any fixed0<gamma<2/3. At E comparable to sqrt(D), it gives Y D^(1/6), improving the old comparator for0<gamma<2/5. These are bounds on a possibly empty representation component, not density/lower constructions. They do not control all d or the mixed range beyond normD. The proof uses |mu(d)|<=1 at its final cubic Cauchy step: no signed-Mobius saving is claimed.

## 2. Exact arithmetic root splitting in the identity d class

Write the fixed source decomposition as tilde_chi_a=xi_a psi_C for[a]=C, with cond(xi_a)=a and beta_a=epsilon(xi_a)psi_C(a). Individual xi_a may have nonzero fixed unitary infinity type and are NOT asserted to have order6.

If[d]=1, then the primitive tilde_chi_d has conductor d and trivial total infinity type. Indeed compare d with the unit in the source conductor lemma (or use the principal-ray construction): the S component cancels. For SF d,a with(d,a)=1 and[a]=C, exact index multiplicativity gives

    xi_da=tilde_chi_d xi_a.                              (2)

This is an equality of primitive Hecke characters, not merely a statement after deleting S values. On good ideals it follows by dividing tilde_chi_da=tilde_chi_d tilde_chi_a by the SAME psi_C. Equality of primitive extensions follows; the conductors d and a are coprime. The angular/radial types in(2) are0 plus those of xi_a. Thus the proved global coprime root multiplication has archimedean correction i^(|0|+|k_C|-|k_C|)=1 and yields

    beta_da=epsilon(tilde_chi_d)beta_a
                      tilde_chi_d(a)tilde_chi_a(d)
           =epsilon(tilde_chi_d)beta_a alpha(1,C)
                                      tilde_chi_a(d)^2. (3)

The last equality is the EXACT source reciprocity convention
    tilde_chi_d(a)conjugate(tilde_chi_a(d))=alpha(1,C).
No multiplicativity of beta or A_U is assumed. Formula(3) holds also for a=O when that residual is allowed, with its actual primitive unit-conductor normalization.

For residuals a,b individually SF and coprime to d, but possibly overlapping EACH OTHER, their common source class C gives

    beta_da conjugate(beta_db)
       =beta_a conjugate(beta_b) lambda_ab(d),
    lambda_ab=(tilde_chi_a conjugate(tilde_chi_b))^2.       (4)

Let g=(a,b), a0=a/g,b0=b/g. The primitive character underlying lambda_ab is cubic, with GOOD conductor a0 b0; it is nonprincipal if a!=b. The local exponents at the good primes of a0,b0 are+2,-2 modulo6, hence exact order3 and tame conductor exponent1. Common good primes drop from that primitive conductor. The S component cancels since[a]=[b]. If a=b the primitive character is principal. In EVERY case the full union a*b remains deleted from d by original squarefreeness; conductor drop is not zero restoration. No statement here interprets the auxiliary a=b component as an original primitive diagonal or as a global obstruction.

All other common d phases cancel literally in the paired expression: nu(d), R_d(u0), the raw factors at k^2 ell v2^2, and primitive tilde_chi_d(e/h). Their zeros remain as the full row mask

    (d, S a b k v2 z)=1.                                (5)

Here ell|v2 and e,h are S-supported. Primitive e/h values are legitimate and unitary at a good d. The original z raw factor supplies(d,z)=1. We keep(5), not the smaller primitive conductor of lambda_ab. No frozen good factor has been omitted, since the scope excludes them.

Thus swapping d and z exposes a cubic-character sum in d with conductor at most4L^2, coupled to the sextic z modulation and actual A_U(da)A_U(db). It is not a fixed-field scalar Mertens sum.

## 3. Why the naive fixed-vector cubic sieve step was incomplete, and its finite repair

The concurrent root note planning/coherent-band-20261106/root/FINITE_CUTOFF_SCHUR-v1.md (SHA f07d6228b1e192c07553f6af38c5ce8371c975f48a4dd691c419923c9e973d43) gives the explicit finite operator constant G_IJ[e^2 asinh(T/c)^2/pi^2+32 X^(3/2)/T] at an upper-product parameter X. With X=4D on the rectangle below, it confirms the qualitative transfer used here; the following short proof records its endpoint/error justification independently. A form with the coefficient on both sides costs the SQUARE of the multiplier norm, as already reflected in M(W)^2 and a renamed arbitrarily small exponent.

Before this step the actual coefficient in the d-by-a matrix is A_U(da)W(Nd Na/D); it depends on BOTH variables. Applying a cubic large sieve to a fixed coefficient vector in a while retaining that dependence would be invalid. This is a failure of that proposed step as written, NOT an impossibility theorem: the cutoff admits a finite-height Schur separation.

For SF m put

    H_m(v,w)=product_{p|m}(1-(Np)^(-v)-(Np)^(-w)).

When(d,a)=1, H_da=H_d H_a EXACTLY. Let V=floor(U)+1/2, c=1/log(3D), and use two FINITE Perron heights T on Re v=Re w=c. The two short norm cutoffs are exactly recovered in the limit because every divisor norm is an integer and V lies strictly between integers. The existing elementary one-variable truncated Perron estimate gives a uniform error

    |A_U(m)-A_T(m)|
       << 3^omega(m) V^(2c){U/T+(U/T)^2}, Nm<=4D.         (6)

Indeed min_{n>=1}|log(V/n)|>=1/(2V+1), and the error of each Perron indicator is O((V/n)^c U/T); expand the product of two approximate indicators before summing its3^omega(m) placements. No infinite-height absolute Perron integral is used.

For m=da the finite approximant is an integral of products of diagonal row factors H_d(v,w) and diagonal column factors H_a(v,w), with scalar V^(v+w)/(vw). Uniformly in vertical variables,

    |H_d|<=3^omega(d), |H_a|<=3^omega(a),
    V^(2c)=O(1),
    integral_{-T}^T |dt/(c+it)|=O(log(2T/c)).             (7)

Ideal counting gives O(E) possible d and O(L) possible a; their product is O(D). Taking T=(3D)^(N+10), the entry error in(6), multiplied by the square root of that dimension product, is O_N(D^(-N)) after the usual arbitrarily small divisor loss. For a matrix K whose(d,a) entries vanish when(d,a)>1, a uniform entry error delta has Schur-operator effect at most delta sqrt(#d #a)||K||, since max|K_da|<=||K||. Noncoprime entries therefore cause no misuse of H_da=H_d H_a.

Consequently the actual multiplier obeys

    ||[A_U(da)K_da]||op
        <<_epsilon D^epsilon(log(3D))^2 ||K||op,

with an arbitrary-small polynomial error absorbed, or simply

    ||[A_U(da)K_da]||op <<_eta D^eta ||K||op              (8)

for every eta>0. This is a finite-matrix bound with true endpoints; it does not shift an inverse zeta function, discard tail errors, or assert A_U(da)=A_U(d)A_U(a).

The common W has an exact absolutely convergent Mellin representation on Re s=0. Its matrix multiplier norm is at most M(W), because W(Nd Na/D) is the integral of scalar D^(it) times the two unitary diagonals(Nd)^(-it),(Na)^(-it). Composing with(8) costs M(W)D^eta. Fixed phases, zero-column modulations, original class selectors and unitary Mellin powers cost no additional norm. A moving profile would require its actual M(W); a mere supnorm-uniform assertion is not made.

## 4. The actual cubic matrix and quantitative inner bound

At a fixed source-Mellin point s=sigma+i tau, freeze v2,k,ell,e,h and good z. The original m=da annulus with E<Nd<=2E forces L/2<=Na<=2L. This is the union of a bounded number of ordinary dyadic ranges with lower endpoint>=1 (since E<=D/2); no subunit sieve is needed in this theorem.

Use(3) in each one-sided column sum BEFORE taking the signed d pairing. Common d phases cancel as above. The new d-by-a core is

    K_da^(z)=1{[d]=1,[a]=C,(d,k v2 z)=1}
                  tilde_chi_a(d)^2 conjugate(R_a(z)),    (9)

with all additional residual primitive e/h, k/ell/v2, beta_a, nu(a),u0 and radial unitary phases left as DIAGONAL column modulations. These have modulus<=1. In particular(d,a)=1 is already the raw zero of the cubic character. Equation(9) does not assume z is SF, primitive, or free of a-primes; its collision zeros and every equal-norm ideal remain.

The raw cubic entries tilde_chi_a(d)^2 are the actual primary cubic residue family, up to harmless fixed-class reciprocity phases. Both a and d are SF, hence cube-free. Choose the primary generators alpha_a congruent1 mod3 as in the already pinned family construction. Squaring the sextic symbol gives(alpha_a/d)_3; source Example2.2 realizes exactly this cubic family (or its transposed form by cubic reciprocity). Deleting2 and imposing our fixed source6-class selectors only restricts rows/columns inside the positive comparison. Thus the SAME pinned Theorem1.1 at n=3 gives

    ||K^(z)||op^2 <<_eta (EL)^eta Theta3(E,L).            (10)

This uses PHYSICAL ideal norms E,L. No theorem for arbitrary primitive conductor labels is substituted. The extra row mask(d,z k v2) and column factors conjugate(R_a(z)) are retained as contractions in(9); they are not restored as nonzero entries in the identity.

After composing(8), W and the magnitude factors(Nd Na)^(sigma-1/2), the squared norm of either one-sided d vector is at most

    M(W)^2 D^eta E^(2sigma-1) Theta3(E,L)
                       *sum_{Na in[L/2,2L]}(Na)^(2sigma-1)
       << M(W)^2 D^(2sigma+eta) Theta3(E,L)/E.           (11)

The two vectors paired by the source integral are at s and conjugate(s) BEFORE conjugation; they need not define a PSD form. Cauchy in d with |mu(d)|<=1 is legitimate and gives the same right side of(11) for their bilinear pairing. This is the point where no further mu cancellation has been proved.

For a good-z prefix Nz<=Z, a final triangle over z costs only O_K(Z) ideals. Therefore the coupled signed d/z inner sum satisfies

    |T_E(Z;s)| << M(W)^2 D^(2sigma+eta)
                              (Z/E)Theta3(E,L).         (12)

The original mean, nonunit modes and raw zeros are included. No z-phase cancellation is claimed by this last triangle. The accepted positive-d method, applied to the same restricted divisor band with the original coefficient bound, separately gives

    |T_E(Z;s)| << M(W)^2 D^(2sigma+eta) Phi(Z,L).         (13)

There are O(E) divisors, each original-annulus subsequence norm is O(M(W)^2 D^(2sigma+eta)/E), and the residual raw Phi norm is used before the d triangle; this is precisely the old method, not a newly claimed result. Taking the minimum of(12),(13) is the new surviving inner comparison.

## 5. Completing the finite dual-band bound with all original modes

For a total dual band Y<Nh Nz<=2Y, the complex Mellin row weight has modulus at most Y^(-sigma). At fixed h use Z_h=2Y/Nh>=1. The new branch sums its z count as

    sum_{h S-supported,Nh<=2Y} Z_h
       <=2Y product_{p in S}(1-1/Np)^(-1).              (14)

The other branch uses the four positive Phi exponents as in the accepted proof. Thus both branches sum with fixed S constants. This includes the good dual unit whenever h lies in the band; no unit/sixth-power or S-supported mode is dropped.

All exact finite e/ell signs, ray coefficients and scalar phases remain before taking the bound. At the Mellin point the prefactor has magnitude A1^(1-sigma)(Nell Ne)^(sigma-1), and normalization is ONCE by1/D. The actual FINITE k sum is bounded, AFTER the new joint estimate, by zeta_K^S(2-2sigma), finite for sigma<1/2. The finite e sum is fixed; the original ell restriction is kept and its upper bound costs tau(v2). Actual unweighted v2 counting costs A2(DA2)^eta. Finally the already accepted BV--Gamma product integral has uniformly finite L1 norm at this fixedsigma, with no higher derivative of the sharp G. These operations prove(1). They do not complete the actual finite k sum or extend an infinite dual interchange.

We do not take sigma=0. When making only an exponent comparison in polynomially bounded D,Y,A1,A2 ranges, a sufficiently small FIXED positive sigma can be absorbed into a requested epsilon exactly as in the accepted prefix proof. Constants may depend on that epsilon. This observation is not a new whole-prefix theorem and does not sum the unresolved all-d/high-dual range.

## 6. Actual signed mechanism tested, and its precise failure so far

The attempted mechanism was to exploit the sign mu(d) before an absolute d triangle. The root computation genuinely reveals a coupled cubic quotient character. It also shows why a scalar fixed-field Mertens bound is not directly the needed input: for fixed residuals a,b the conductor is q_ab=(a/g)(b/g), with Nq_ab as large as4L^2, and the complete deleted set includes every prime of a*b*k*v2*z even if it dropped from q_ab. The two actual A_U factors and the radial product profile stay in that sum.

As a transparent specialization, restrict d to rough prime ideals p with Np>U and[p]=1. Then the short-divisor definition gives A_U(pa)=A_U(a) exactly, because no short divisor can include p. The remaining fixed-(a,b,z) arithmetic sum is therefore a weighted PRIME-character sum

    -A_U(a)A_U(b)
       sum_{p in(E,2E],Np>U,[p]=1,p notin T}
            lambda_ab(p)(Np)^(2s-1)
              W(Np Na/D)conjugate(W(Np Nb/D)),            (15)
    T=S union supp(a b k v2 z).

Under the original high window2D/7<=U^2, active residual a,b satisfy Na,Nb<7U, so the accepted short-coefficient lemma also says these A_U(a),A_U(b) have modulus1. This is a restricted auxiliary rough support, not global coefficient shrinkage. The identity(15) itself requires only Np>U, not that high-window lemma.

On this prime component mu(p)=-1 is CONSTANT. It is therefore incorrect to assign it scalar Mobius cancellation. For a!=b, cancellation would be an estimate for cubic prime twists of varying conductor with this exact ray/deletion/profile dependence; for a=b it is principal but that auxiliary sector can cancel against OTHER d sectors and is not a full-slice obstruction. We do not import a fixed-field PIT estimate uniformly over Nq_ab growing like L^2. Nor do we claim that these arithmetic sums cannot be estimated by a repaired Type-I/II method.

The finite-Perron repair permits the honest cubic LS in Sections3--5, but its final Cauchy step still bounds mu(d) rather than exploiting its sign, and the final z triangle loses cross-prime dual coherence. Its floor Z in(12) already prevents a general power improvement once the existing Phi comparator is itself of orderZ. At E near D^(2/3) this transposition controls that divisor band efficiently, but the small-d bands and the pure/mixed open dual range do not disappear.

One exact next criterion is a signed, coupled refinement of the actual quantity in(11)--(12), summed over all d source classes and with the total-dual z weight RETAINED before triangle. It must improve the pairing of the two real-cutoff Schur-modulated cubic matrices, not replace A_U(da) by A_U(a), drop raw(d,z), assume independent columns, or use a generic conductor-parametric sieve. A proof for that stronger coupled Type-I/II form is NOT supplied here. The new result is(1), and the surviving failed step is precisely the absence of an extra joint mu(d)/z cancellation estimate beyond it.

No principal/residue target assembly, positive physical energy lower bound, desired positivity, determinant/zero-location bridge, analytic/category Lean completion or GRH claim follows. All current canonical/released sources, outputs, indexes, environments and histories are preserved.
