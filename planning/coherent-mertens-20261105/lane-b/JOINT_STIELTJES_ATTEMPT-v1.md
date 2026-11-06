# Joint signed incidence, Abel variation and the radial squarefunction

NEW research-only lane B, 5 November 2026. Outcome: an exact joint operator lift and mean-retaining radial squarefunction identity; the inherited positive operator input still has the old critical 5/6 PIT cost. No target estimate, actual-error lower bound, improved global exponent, determinant/zero-location/GRH result, or new Lean theorem is proved. No old table, accepted control, browser/publication audit or author evaluator is rerun. All source inputs and eleven protected HEAD/index states are pinned separately.

## 1. Actual objects and the point of departure

Use the accepted rma objects, with integral IDEALS throughout. Fix S containing the primes above 2,3, a unitary multiplicative nu on good ideals, ONE common possibly complex W supported in [1,2], smooth and zero at its endpoints. Retain the complete original squarefree good annular family, every actual row unit/ray/capacity condition, raw zero, common-prime/full-union restriction, and any specified sixth-factor masks. Put

    U>=7, U^2<=D, 2D<=7U^2,
    A(g)=sum_{xy|g,(x,y)=1,Nx,Ny<=U} mu(x)mu(y),
    T_f(t;u)=sum_{a SF good,(a,f)=1} A(fa)nu(a)chi_a(u)W(Nf*t*Na/D),
    G_f(t)=sum_{actual u,(f,u)=1} w_u |T_f(t;u)|^2,
    Q(t)=sum_{f SF good,U-smooth} mu(f)G_f(t).

Here w_u>=0, R_w=sum w_u, and chi_a(u)=0 on a common prime. The f variable is an intermediate smooth common divisor, not the original h=1 sector. The exact algebra below is valid for the fixed actual row family and weights. The classical lambda specialization later is ONLY the accepted unweighted A6=1 two-pivot family (or its already justified bounded natural multiplicities), not arbitrary weights or sixth-factor families.

With fixed-S prime-ideal discrepancy E(t)=pi_K^S(t)-Li(t), counting conjugate primes separately, the accepted identity is

    KS=sum_{p good,Np>U} Q(Np),
    J=integral_U^infinity Q(t)dt/log t,
    EPIT=KS-J=-E(U)Q(U)-integral_U^infinity E(t)Q'(t)dt.       (1)

There is no absolute f sum in (1). The endpoint excludes Np=U exactly and CANNOT be discarded. Q vanishes at and beyond 2D. The original raw slice remains

    S1AA=(K0-J)/D + Delta_mask + Ctwo/D - EPIT/D.             (2)

The accepted mask/unit corrections and every original principal residue remain separate. KS is auxiliary: p may divide a or u, and pfa may be nonsquarefree. The coefficient in T_f is A(fa), never A(pfa). Nothing below restores a deleted original zero or treats those auxiliary columns as original annular columns. Even EPIT=0 would leave the mean-retaining K0-J unestimated.

Novelty relative to COHERENT_PIT_BUDGET-v2: that note embeds the exact signed Q but bounds its variation by individual f-length norms and then sums absolute f costs. Here all f terms are lifted to ONE common short-column space first; Abel and Mellin squarefunctions are tested directly on its signed self-adjoint form. This is an alternative derivation/diagnosis, not an automatic stronger bound.

## 2. Exact common-column lift, including the masks

Take the finite space indexed by squarefree good g with Ng<=2D/U, without identifying equal-norm ideals. Let

    b_g(t)=A(g)nu(g)W(Ng*t/D),
    (R c)(u)=sqrt(w_u) sum_g c_g chi_g(u),
    (P_f c)_g=1_{f|g}c_g.

R has exactly the ACTUAL row indices and raw symbols. All P_f are diagonal orthogonal projections. For (f,u)=1, multiplicativity on the squarefree product g=fa gives

    (R P_f b)(u)=sqrt(w_u)nu(f)chi_f(u)T_f(t;u).

The multiplier has modulus one. If (f,u)>1, every g divisible by f has chi_g(u)=0, so the left side is exactly zero. Consequently

    G_f(t)=||R P_f b(t)||^2,
    Q(t)=b(t)^* M_U b(t),
    M_U=sum_{f SF good,U-smooth} mu(f) P_f R^*R P_f.         (3)

This is an equality, with the actual nonfactored A(g). M_U is fixed, finite and self-adjoint; positivity is NOT asserted. The scalar f-row mask has not been enlarged: it has become an exact raw-zero identity. No primitive-conductor replacement, independent marginal family, extra column ray, free Gauss phase, or conductor-uniform prime theorem enters (3).

The full row Gram is retained:

    (R^*R)_{g,h}=sum_u w_u conj(chi_g(u))chi_h(u).

Thus (3) keeps coherent orientations and their means. A change of inner-product convention just conjugates the displayed Gram; Q is unchanged.

Expanding the divisor sum yields the exact Schur kernel

    C_U(g,h)=sum_{f|gcd(g,h), f U-smooth}mu(f)
            =1_{gcd(g,h) has no prime ideal of norm<=U}.     (4)

At t>=U every active g has Ng<7U; the endpoint W(2)=0 handles equality. A good nonunit has norm>=7. Therefore a g containing a prime p of norm>U must be g=p: another nonunit factor would make Ng>7U. On the active support,

    C_U(g,h)=1_{(g,h)=1}
                  +1_{g=h=p, p good prime, Np>U}.           (5)

Repeated/conjugate rational norms do not change ideal coprimality. Equations (3)--(5) describe SHORT auxiliary g=fa, not a replacement of the original length-D column family.

## 3. What the existing operator norm actually proves jointly

Let lambda_*(X) be a TRUE squared row-operator bound on good squarefree columns in [X,2X]. It must dominate the actual row weights. On 1/2<=X<1 count the unit column directly, with lambda_*=R_w. There are no active columns at X<1/2. For X>=1 the accepted two-pivot input, in its precise narrow scope, is

    lambda(X) << (HD)^eta min{
        R + X R/M + X^(2/3) R/M^(1/3), X+R^2},
    R=A1*A2, M=max(A1,A2), A1*A2^2<=H.                     (6)

The implicit constants carry the original fixed nu,S,literal hypotheses. One cannot use (6) for arbitrary w; a universally valid alternative is the Frobenius bound lambda(X)<<R_w X.

On a common active dyad, R^*R<=lambda(X)I in positive quadratic-form order. For any c on that dyad,

    |c^*M_U c| <= sum_f ||R P_f c||^2
               <= lambda(X) sum_f ||P_f c||^2
               = lambda(X) sum_g d_U(g)|c_g|^2,
    d_U(g)=#{U-smooth ideal divisors of g}.                 (7)

This is a joint incidence-frame estimate, without a per-f norm at length X/Nf. It is still a positive majorant: the only use of signs was the first inequality. For squarefree g, d_U(g)<=2^omega(g)<<_eta (Ng)^eta. By polarization/self-adjointness, the restricted operator norm is at most lambda(X)max_g d_U(g).

Put X=D/t and M1=max(||W||infinity,||xW'(x)||infinity). The exact short coefficient lemma applies to all active g:

    A(g)=mu(g)(2*1_{Ng<=U}-1), |A(g)|=1.                  (8)

No factorization is asserted outside this coupled range. Ideal counting gives ||b||^2<<B^2 X and ||t b'||^2<<M1^2 X, including the direct unit endpoint. Differentiate the fixed finite form (3), not a moving matrix:

    Q'(t)=2 Re (b'(t)^*M_U b(t)).

Using (7) on the shared support of b,b' proves

    |Q(t)|+|tQ'(t)| <<_eta (HD)^eta M1^2 lambda_*(X)X.     (9)

All norm factors include the retained mean. There is no mean-zero hypothesis hidden in (9).

With delta(U)=sup_{t>=U}|E(t)|/t and X0=D/U, (1) and t=D/X give

    |EPIT|/D <<_epsilon (HD)^epsilon M1^2 delta(U)
       [lambda_*(X0)+integral_(1/2)^X0 lambda_*(X)dX/X].    (10)

One may retain max d_U explicitly instead of absorbing it. Thus (10) does not promise a uniform logarithmic improvement over the older per-f certificate: a maximum divisor factor may exceed a logarithm. It has the same D-powers. Inserting the first branch of (6) gives, up to the requested epsilon,

    |EPIT|/D << (HD)^epsilon M1^2 delta(U)
       [R log(2X0)+X0 R/M+X0^(2/3)R/M^(1/3)].             (11)

The previously displayed R log^2 term can be bypassed in this incidence formulation only at the cost of the explicit divisor/subpower factor. Taking an arbitrary-coefficient positive norm and relabeling it as signed cancellation would be incorrect.

## 4. A genuine discrepancy-squarefunction criterion, with its endpoint

Partition [U,2D] into dyadic intervals I_T=[T,2T] intersected with that range. Let lambda^#(D/T) dominate (6) on the adjacent length dyads. Define the DIMENSIONLESS discrepancy norm

    d2(T)=T^(-3/2) (integral_(I_T)|E(t)|^2 dt)^(1/2).

A direct Cauchy bound, using (9) in L2, yields

    |EPIT|/D << (HD)^epsilon M1^2 {
       (|E(U)|/U)lambda_*(D/U)
                  +sum_T d2(T)lambda^#(D/T)}.             (12)

For instance ||Q'||_(L2(I_T))<< (HD)^eta M1^2
lambda^#(D/T)(D/T)/sqrt(T), and ||E||_2=d2(T)T^(3/2), so division by D gives exactly the summand in (12). The same estimate follows by vector Cauchy on the direct sum of all f-row amplitudes, retaining the signature diag(mu(f)); it does not create an extra power of T. Global Cauchy across widely separated T can be worse, so the dyadic version is the safe conclusion.

A sufficient NEW INPUT for target-budget prime substitution is that the braces in (12) are <<H(HD)^epsilon, with its endpoint included. This is a precise attainable inequality to investigate, not an established theorem. The accepted fixed-field PIT only gives d2(T)<=sup_(I_T)|E(t)|/t times an absolute constant, hence the same subpower exponential scale. No power-saving mean-square discrepancy or independence between E and the actual signed derivative has been supplied here. S is fixed throughout; the growing supp(abu) is not put into the prime-counting measure.

## 5. Mellin/Abel squarefunctions preserve equal-norm coherence

Extend the SAME finite g-vector formula to all t>0 just for a full-scale Parseval identity. This adds no new original columns. Actual KS and (1) still use only t>=U; enlarging a norm integral below U is legitimate only inside a positive estimate, not in a signed equality for KS.

For fixed f,u put c_g=A(g)nu(g)chi_g(u)1_{f|g}. With

    W_hat(i tau)=integral_0^infinity W(x)x^(i tau)dx/x,

ordinary Mellin/Plancherel gives exactly

    integral_0^infinity |sum_g c_g W(Ng*t/D)|^2 dt/t
       =(1/(2pi))integral_R |W_hat(i tau)|^2
                      |sum_g c_g (D/Ng)^(i tau)|^2 d tau.  (13)

For t*d/dt, replace |W_hat|^2 by tau^2|W_hat|^2. Summing the FINITE signed f forms in (13) retains (3) at the unimodular norm-twisted coefficient vector. No orientation is centered or averaged away.

Crucially, for distinct ideals g,h with Ng=Nh, their radial W profiles AND all t-derivatives are identical. The off-diagonal radial correlation is the same nonzero profile norm as the diagonal when W is nonzero. Conjugate split prime ideals supply actual distinct equal-norm columns. Mellin's factor (Ng)^(-i tau) is also identical on that fiber. Thus a radial squarefunction does not orthogonalize ideal orientations, remove their mean, or justify replacing their signed pairing by orientation variance. Applying the existing arbitrary-coefficient lambda to each tau is unchanged by this unimodular twist; integration merely produces a fixed profile/Sobolev factor.

The accepted mean counterexamples are logically decisive here: the profile-uniformity example has nonprincipal rows and nonzero pairing but zero centered orientation norm; the fixed-W two-pivot example has variance sum6 but |sum a Gamma|^2=36>||a||^2*6=12. They are not rerun or asserted to be instances of this KS discrepancy. They rule out dropping a mean term. The safe exact decomposition is

    sum_r a_r Gamma_r = Gamma_av sum_r a_r
                           +sum_r a_r(Gamma_r-Gamma_av).

Both terms remain in (3), (12) and (13).

## 6. The sharp limitation of the f-sign argument and the actual power budget

On the legitimate rough-prime column subspace (g=p, Np>U), P_f is zero for every nonunit U-smooth f. Hence

    M_U restricted to this subspace = R_prime^* R_prime >=0. (14)

There is NO mu(f) cancellation there. The actual coefficient is A(p)=+1, so in the allowed principal-nu scope b_p=W(Np*t/D); these are not freely chosen phases or a moving profile. This does not lower-bound full Q or EPIT: other columns can cancel it, and E changes sign. It proves that f-sign cancellation alone cannot be inferred from a black-box bound on ||R||. In abstract linear algebra the bound is already tight on such a subspace, but that is not a claim that the actual arithmetic operator saturates it.

At the critical line H=D^(3/4), U comparable to D^(1/2), evaluate the three monomials in (11) with capacity slack:

    pure A1~D^(3/4), A2~1:
       R:3/4, (D/U)R/M:1/2,
       (D/U)^(2/3)R/M^(1/3):5/6;
    mixed A1~D^(5/12), A2~D^(1/6):
       R:7/12, linear:2/3, powered:7/9.

These are MAJORANT exponents, not actual-error lower bounds. The corresponding worst-dyad discrepancy factors needed to make those powered terms fit H are D^(-1/12)=U^(-1/6) in the pure block and D^(-1/36)=U^(-1/18) in the mixed block. The endpoint in (12) needs compatible control too. The fixed-field exponential-in-sqrt-log bound does not provide either fixed power for arbitrarily small requested epsilon. The second branch X+R^2 of (6) is larger at both witness scales, so taking the stated minimum does not repair these two deficits. The general formula (12), not just these witnesses, retains neighboring capacity-feasible blocks.

The accepted smooth-tail cutoff does not fix this failure: all rough-prime support has Nf<2D/U, and f=1 survives every nontrivial small-f localization. High-f target-size tails leave (14) and the full mean-retaining small-f main intact.

## 7. Result and precise failed step

Surviving NEW derivation: exact joint lift (3)--(5), incidence-frame norm (7), mean-retaining Abel/squarefunction criteria (10),(12), and radial Mellin coherence identity (13). These expose a single coupled signed operator whose cancellation would suffice, rather than treating f energies as unrelated weights.

Failed inference: neither joint integration by parts nor radial squarefunction/Parseval supplies a factor D^(-1/12) in the pure positive budget (or D^(-1/36) at the displayed mixed scale). Existing arbitrary-coefficient operator norms and the accepted fixed-field PIT still reproduce the inherited powers. A new estimate must control the ACTUAL pairing of E with the signed joint derivative (including the lower endpoint), or prove extra arithmetic cancellation in M_U/b beyond those inputs. It must also estimate K0-J; prime substitution alone does not do that. Replacing Gamma by centered Gamma, using arbitrary independent orientation phases, dropping the rough-prime subspace, varying W with D, or inserting a growing-conductor prime theorem would not establish the stated target.

No new external literature theorem is invoked: the positive input and fixed-field PIT are the already source-bound accepted statements, with their actual restrictions. New accompanying checks use only exact Fraction exponent arithmetic and source/protected-state guards, not old numerical fixtures or a proof by finite sampling. All canonical/book/UI/publication/queue/index files remain untouched.
