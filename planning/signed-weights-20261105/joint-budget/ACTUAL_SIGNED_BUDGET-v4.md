# Actual fixed-profile h=1 budget: exact reduction and surviving estimate

Status: **new exact signed decomposition and a proved h=1 absolute budget; no new saving.** The Jacobi/Hecke identification is used with the exact normalization in the separately reviewed phase work, not claimed as a new Jacobi identity. The governing Jacobi application is `quadratic-phase/TWO_PIVOT_APPLICATION-v3.md`, SHA256 `f1113869c23041e1f12b3d7869559e670234cec9a4b5188c33e0f030f7ff30d4`, independently accepted in review-phase/REVIEW-v1.md. The quantitative advance here is an actual-weight, raw-mask-preserving gcd-Möbius budget that does not infer a bound for a signed gcd slice from positivity of the full energy. It identifies the precise cancellation still needed at both remaining neighborhoods.

Fix the original K=Q(omega), S, finite-order nu, one common possibly complex smooth W supported in[1,2], D>1 and U²<=D. W is fixed as D varies; constants in a proposed stronger signed bound may depend on its fixed seminorms. Fix one literal unit/S/ray class u0 and an actual row block

    u=u0 v1 v2²,  A1<=Nv1<2A1, A2<=Nv2<2A2,
    v1,v2 good, squarefree, (v1,v2)=1, Nu<=H.

All other good factors are one, including A6=1. Let F be this exact common finite indicator, including the sharp capacity and ray restrictions. Its Fourier transform is not replaced by a smooth rectangular or uniform weight. The dyadic neighborhoods under consideration are

    H=D^(3/4), mixed (A1,A2)=(D^(5/12),D^(1/6)),
    pure (A1,A2)=(D^(3/4),1).

Both are nonprincipal outside S once the moving first factor is nonunit, so P_u=0 there. This note addresses their h=1 slice, not the other gcd slices or the entire P7 target.

## 1. Exact original signed slice and its mean

For X=C,mu,A let X_U(m) denote respectively the original C_U(m), mu(m), A_U(m)=C_U(m)-mu(m). Define on squarefree columns

    g_X(m)=mu(m)X_U(m).

This definition is valid for every allowed U. In the high window 2D/7<=U²<=D,

    g_C=r_U,  g_mu=1,  g_A=r_U-1.

One must not replace g_A by r_U-1 outside that window. In all cases the actual coefficients satisfy |X_U(m)| <<_eta (Nm)^eta uniformly in U, by the original divisor-assignment bound and C=A+mu.

For q=mn squarefree, (m,n)=1, both column norms in[D,2D], put theta=chi_m overline(chi_n), and let J_q contain every legal original orientation, including those at which one coefficient happens to vanish. Write

    Gamma_q(r)=sum_(v1,v2) F(v1,v2) theta_(r,q/r)(v1 v2²),
    a_q^XY(r)=g_X(r)g_Y(t)nu(r)overline(nu(t))
               W(Nr/D)overline(W(Nt/D)) theta_(r,t)(u0), t=q/r.

All values are raw symbols. In particular Gamma deletes every common prime with v1 or v2. The exact slice is

    S_h1^XY = D^(-1) sum_q mu(q) sum_(r in J_q) a_q^XY(r)Gamma_q(r).       (1)

The literal phase stays in a, mu(q) stays inside the q sum, and F is orientation-independent. C-C and C-mu are obtained by the stated g factors, not arbitrary replacement weights. The actual A-A combination is CC-Cmu-muC+mumu; it need not require an individual target estimate for each stronger component.

For q with n_q=|J_q|>0, let barGamma_q=n_q^(-1)sum Gamma_q and bara_q=n_q^(-1)sum a_q. Conductors with J_q empty contribute zero and are omitted from the centered definitions. Then exactly, with no absolute values and with a bilinear rather than sesquilinear covariance,

    D S_h1^XY = sum_q mu(q){ (sum_r a_q(r))barGamma_q
                   + sum_r(a_q(r)-bara_q)(Gamma_q(r)-barGamma_q) }.       (2)

The two terms must both remain. Centering the correlation and discarding the first term is not a principal-residue subtraction. For A-A and real F, reversal r<->q/r makes the complete slice real; it does not make either mean or covariance nonnegative.

## 2. Two-pivot completion and what the CM gauge does

Use the exact jdq additive character e_beta(z)=exp(2pi i Tr(z/(delta beta))) for q=(beta), Q=Nq. For q-unit frequencies,

    tau_beta(theta)tau_beta(theta²)
       = J_q(theta,theta²)tau_beta(xi_q),  xi_q=theta³=x_q³,
    J_q(theta,theta²)=j(r)overline(j(t)).

Here j(p)=J_p(chi6,chi6²) is the repository's raw Jacobi sum, not the separately signed theta normalization. The scalar is QUADRATIC tau(xi_q). For this two-factor identity there is no extra xi_q(-1); the six-factor jdq identity does contain that factor.

Write kappa=Psi/sqrt(N), where Psi is the algebraic type-one character with conductor f=(2delta), Nf=12, in the phase team's exact normalization. The local identities j(p) generates p and j(p)=-1 modulo f give

    mu(m)j(m)=Psi(m),  j(m)/sqrt(Nm)=mu(m)kappa(m)              (m sf).   (3)

For clarity, the underlying finite-conductor argument is elementary: the six units map bijectively onto(O/f)^times; Psi((alpha))=alpha/u_f(alpha), with u_f(alpha) the unique unit having the residue of alpha. The local congruences identify -j(p) with that unique generator. Minimality follows from units -1 at modulus2 and omega at modulusdelta. This is a fixed column twist, never an independent phase for each q or orientation.

Set

    b_X(m)=kappa(m)g_X(m)nu(m)W(Nm/D),
    T_q,F(theta)=sum_(k1,k2 mod q)^times Fhat_q(k1,k2)
                                      overline(theta(k1 k2²)),
    gamma_beta=tau_beta(xi_q)/sqrt(Q).

Exact two-factor inversion now gives

    D S_h1^XY = sum_q gamma_beta/Q
          sum_(rt=q) b_X(r)overline(b_Y(t))theta_(r,t)(u0)T_q,F(theta).  (4)

The two Gauss magnitudes, equivalently the central Gauss and Jacobi magnitudes, give exactly1/Q. Equation(3) absorbs the complete original mu(q), rather than dropping it. The finite central phase is the already known quadratic phase; fixing its finite ray class cannot supply cancellation by itself. All original annulus, squarefree, ray, union-prime and capacity restrictions are still present.

The temptation to replace the original row polynomial by

    sum_m kappa(m)g_A(m)nu(m)chi_m(u)W(Nm/D)

is false. Put rho(m)=j(m)/sqrt(Nm)=mu(m)kappa(m). The new frequency kernel is the old correlation kernel conjugated by this unitary diagonal gauge. In row language its compensating factor is overline(rho(m))=mu(m)overline(kappa(m)); the Möbius weight has moved into the transformed kernel. Keeping the old row kernel and only the attractive new coefficient would change the arithmetic problem. Consequently ordinary coefficient/operator l2 norms are unchanged. A fixed-frequency Hecke estimate would additionally need a genuine bound for the actual q-dependent Fhat/product-frequency coupling; there is no proved lower-height tail or uniform smooth q weight here.

There is an exact obstruction at the pure endpoint. If v2=c is fixed and q-coprime (in the actual pure block c=1), then

    T_q,F(theta)=theta(c)² tau_beta(overline(theta²))
                   sum_(k1 mod q)^times Fhat_1(k1)overline(theta(k1)).

Because theta²(-1)=1 and tau(theta²)tau(overline(theta²))=Q,

    Q^(-2) J_q tau(xi_q) tau(overline(theta²))=tau(theta)/Q.             (5)

Thus inversion of the literal fixed second factor undoes the apparent two-pivot phase simplification and returns the original orientation-dependent sextic Gauss sum. Nonunit c gives the original zero instead. No central-phase or gauge-only argument can claim a saving uniformly through this pure endpoint. In the mixed neighborhood the second factor grows, but its exact squarefree/coprime/capacity Fourier weight is not a smooth short independent transform; controlling it is precisely the missing estimate.

## 3. A proved gcd-Möbius budget for the actual h=1 slice

There is a separate exact identity that retains the signs before any conductor absolute Cauchy. For squarefree d, set

    T_d^X(u)=sum_(a sf,(a,dS)=1) X_U(da)nu(a)chi_a(u)W(Nd Na/D),
    G_d^XY=sum_(u in F,(d,u)=1) T_d^X(u)overline(T_d^Y(u)).

Then

    D S_h1^XY = sum_(d sf,(d,S)=1) mu(d) G_d^XY.                        (6)

Proof: insert1_(m,n)=1=sum_(d|m,d|n)mu(d) into the original expanded pair sum. Put m=da,n=db. Squarefreeness enforces(a,d)=(b,d)=1. The common nu(d) cancels, while chi_d(u)overline(chi_d(u)) is exactly1_(d,u)=1. Thus every shared-prime deletion remains. No positivity of the gcd-truncated Gram matrix, new row-character substitution, or principal mean removal is used. For A-A, G_d>=0, but the mu(d)-weighted sum is signed.

This yields a rigorous absolute baseline. Put R=A1 A2 and M=max(A1,A2), L=D/Nd (L>=1/2 whenever a column survives). The actual subsequence norm obeys

    sum_a |X_U(da)nu(a)W(Nd Na/D)|²
       <<_(eta) D^eta ||W||infinity² L.                                (7)

This is a counting/divisor bound on the actual sequence, uniform in d,U. Apply the accepted powered-BGL block estimate at column length L and, separately, the accepted ordinary-conductor comparison for A6=1. Positive row enlargement is used only inside each G_d bound. They give

    |G_d^XY| << (HD)^eta ||W||infinity² L
       min{R+L R/M+L^(2/3) R/M^(1/3), L+R²}.                           (8)

The cited sieve statements apply directly when L>=1. If1/2<=L<1, only the unit residual column can survive, since1<=Na<=2L<2. Its actual energy is <<D^eta ||W||infinity² R. Since R>=1, the right side of(8) is at least a constant times R: L min{R+LR/M+L^(2/3)R/M^(1/3),L+R²}>=R/2. This proves the same bound for these final d without invoking a sieve below its declared length range. For a cross term this follows by Cauchy between the two actual subsequences; no original mu(q) is dropped to obtain the exact identities. Taking an absolute triangle in d is explicitly the loss in this baseline, not an asserted signed improvement. The ideal sums

    sum_(Nd<=2D)1/Nd << log(2D),
    sum_d(Nd)^(-2) <<1,  sum_d(Nd)^(-5/3) <<1

show, after division by D and absorption of logarithms, that

    |S_h1^XY| <<_(nu,S,epsilon) ||W||infinity²(HD)^epsilon
       min{ R+D R/M+D^(2/3)R/M^(1/3), D+R² }.                          (9)

This proves the unsigned7/6 budget for this *signed h=1 slice itself*. It is not inferred from a full-energy upper bound, which would not justify it. It applies to the original C-C, C-mu, mu-mu and A-A coefficients; its proof exploits no cancellation beyond their actual divisor-size bound.

At the mixed point the powered exponents are7/12,7/6,10/9, while the ordinary exponents are1,7/6. At the pure point they are3/4,1,7/6 versus1,3/2. Thus both give7/6, with no fabricated saving.

## 4. The precise quantitative estimate still required

For the actual A-A combination and fixed W, a sufficient h=1 target in either neighborhood is

    |sum_d mu(d)G_d^AA| <<_(nu,S,W,epsilon) D H(HD)^epsilon.             (SW)

Equivalently use the full signed sum in(4), with its actual b_A and exact F. At H=D^(3/4) the right side is D^(7/4+epsilon), whereas(9) gives D^(13/6+epsilon) before division by D. A relative D^(5/12) signed saving is therefore required. Bounding the terms in(2) separately by this target is sufficient but stronger; the exact signed sum may have additional mean/covariance cancellation. Deleting the mean is not allowed.

Known block sieves accept arbitrary l2 coefficients and hence give(9), not(SW); the fixed unitary gauge cannot strengthen their norm. An ordinary Möbius partial-sum bound cannot be applied to(6): G_d depends on the prime-ideal support of d through raw row deletions, the actual A_U(da) divisor cutoffs and squarefree/coprime exclusions. It is not a fixed smooth function of Nd, nor an independent bounded coefficient for which cancellation is automatic. No statement uniform over arbitrary q weights, arbitrary characters of conductor D², or arbitrary profiles has been introduced.

The exact analytic obstacle can also be displayed before any q absolute value. For fixed original row u, let psi=prim(nu kappa_u), T=S union supp(u). Introduce four positive Perron variables z1,z2,w1,w2 for the two original small divisors in each column. The coprime two-column six-placement Euler factor is

    P_p=1+x_p(1-(Np)^(-z1)-(Np)^(-z2))
           +y_p(1-(Np)^(-w1)-(Np)^(-w2)),
    x_p=psi(p)(Np)^(-s), y_p=overline(psi(p))(Np)^(-t).                  (10)

There is no x_p y_p term: it would put the same prime into both columns. On initial absolutely convergent lines, successive Perron LIMITS from positive auxiliary lines (using floor(U)+1/2 to avoid integer endpoints), together with the two common-profile Mellin inversions, recover the actual A-A coprime sum. A finite-height Perron expression requires explicit truncation errors; no such finite-height error or uniform tail estimate is proved here. The exact statement is the limiting bookkeeping identity, not a finite-height equality or a critical-strip Dirichlet-series evaluation.

At all four auxiliary variables zero, the untruncated local factor is1-x_p-y_p and

    product_(p notin T)(1-x_p-y_p)
       = C_u(s,t)/{L^T(s,psi)L^T(t,overline(psi))},
    C_u=product_(p notin T){1-x_p y_p/[(1-x_p)(1-y_p)]}.                (11)

C_u converges normally for Re(s),Re(t)>0 and Re(s+t)>1, uniformly at fixed margins and over deleted primes/phases. Nonvanishing is not asserted. Letting t tend to+infinity gives exactly1/L^T(s,psi), so the pair-coprimality correction cannot be assumed to cancel all reciprocal-L singularities. This slice is not a replacement of the finite cutoff by its limit. It explains why a proposed contour proof of(SW) needs actual joint reciprocal moments/residue control; the known central phase and a coefficient gauge do not supply that input. No new external zero-free theorem or unverified literature hypothesis is invoked here.

## 5. Fresh exact diagnostic with fixed W and A6=1

The source-bound checker uses no author arithmetic module and no previous fixture. Its new parameters are D=60000,U=244,H=floor(D^(3/4))=3833, nu=1,S above2,3. Use the fixed profile

    W(y)=s(8(y-1))s(8(2-y)),
    s(t)=exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) for0<t<1,

extended by0/1. This one profile, independent of D, is identically1 on[9/8,15/8]. Choose one split prime ideal at each norm37,43,61,307,313 (the residue embeddings are pinned). At their selected q there are exactly two legal annular orientations97051/96091 and its reversal. Direct original ternary divisor assignments give A_U=1 at both columns; r_U is respectively0 and2. Hence mu(q)=-1 and a_AA=-1 in each orientation: the sign is essential.

The checker completely enumerates the actual row blocks(A1,A2)=(13,13) and(37,7), with primary generators1mod3, pairwise coprimality, squarefree ideals, literal unit1 and the exact capacity. They contain6 and20 rows. In the20-row block every row is nonprincipal because its first outside-S Kummer valuation is1. Twelve orientation/row evaluations are raw zeros. Exact finite-field exponentiation gives

    Gamma=(-4-2omega,-2+2omega), barGamma=-3,
    S_h1^AA=(-6)/60000=-1/10000,
    centered-only pairing=0.

The actual coefficient vector is a_AA=(-1,-1), with squared norm2. The centered correlations are(-1,-2) and(1,2) in omega coordinates, each with Euclidean squared norm a²-ab+b²=3. Their squared-norm SUM is6 and normalized average is3; this is not a zero-variance example. Nevertheless |sum a_AA Gamma|²=36, whereas the proposed variance-only Cauchy right side is2*6=12. Thus dropping the mean makes even that bound false by a factor sqrt(3) in amplitude. The exact centered pairing itself is0. Restoring the raw collision zeros changes Gamma and is rejected. The negative value is legitimate for a selected gcd slice; it is not a negative row energy. This demonstrates the mean issue for an actual fixed profile and A6=1 block, without reusing the moving-profile sixth-factor fixture. It concerns one selected q, not the full q sum, and proves no asymptotic lower bound, target obstruction or exponent saving.

Frozen checker/inputs: source-freeze-v1.json. Exact output: outputs/checks/2026-11-05-signed-weights/joint-budget/fixed-profile-h1-v1.json. All work is new and isolated; canonical papers, queue, accepted experiments, source index and publications are untouched. The current result is the exact signed budget and its boundary, not(SW), a new global estimate, a determinant theorem, Lean formalization or GRH.

The separate BUDGET-ADDENDUM-v1.md preserves an independent review of the root's exact single-column gauged note v1 and derives a new finite-cutoff coprime-pair central-denominator identity. It does not replace the original ungauged six-placement factor(10). The root's superseding gauged note v2 has its own independent review pending; no unreviewed v2 analytic claim is used to prove(6)–(9).
