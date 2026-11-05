# A quantitative actual-coefficient covariance budget and its unsaved term

5 November 2026. Remote-only arithmetic attempt; exclusive planning/check namespaces. **A new lower covariance budget and an elementary balanced-divisor second-moment bound are proved below. They do not improve the existing analytic exponent or establish BT_sigma.** The load-bearing missing step is identified in sections 6–8. No asymptotic arithmetic energy lower bound, reciprocal-L estimate, Lean declaration, positive determinant bridge or GRH conclusion is claimed.

## 1. Exact retained family

The current sources and reviews were read before this attempt: papers/signed-bilinear-{core,details}.tex, research/signed-cutoff-covariance.md, all four current covariance/Perron mathematical/TeX reviews, the accepted CENTERING_AND_SIGNED_TARGET.md and its clarification acceptance, the weighted-cutoff and original masked-moment sources, and the actual residue-field/raw-zero scripts. No repository AGENTS.md or relevant Python package manifest/lockfile exists in the traversed project hierarchy. The root README and existing arithmetic-cutoff script instructions were read. Existing unrelated work and all production/build/queue/publication state are preserved.

Use K=Q(omega), fixed finite-order nu, fixed S containing primes over 6 and conductor(nu), squarefree columns m prime to S, and one common possibly complex W in C_c^infinity supported in [1,2]. For the new quantitative estimate restrict to the already accepted high window

    2D/7 <= U^2 <= D,  D>1.

This restriction is explicit: the estimates below do not prove the target uniformly over every smaller cutoff. On the active annulus, retain the accepted identities

    C_U(m)=mu(m) r_U(m),   A_U(m)=mu(m)(r_U(m)-1),
    r_U(m)=#{ordered a*b=m: Na>U, Nb>U}.

All factorizations are squarefree/disjoint, and every original zero x_m(u)=(u/m)_6=0 for ((u),m)>1 remains. No row-indexed primitive character is substituted on a noncoprime pair. The independently primitive psi_u and psi_(u,2), their possibly different conductors, and the original full deleted sets remain exactly those of the accepted transfer. The present argument works directly with the finite raw Gram; it needs neither a new contour shift nor a change to those conventions.

For any finite literal row block B let

    G_mn = sum_(u in B) x_m(u) conjugate(x_n(u)),
    lambda_m=mu(m)nu(m)W(Nm/D),   v_m=conjugate(lambda_m),
    R=diag(r_U(m)),  S_R=sqrt(R).

Thus G is Hermitian positive semidefinite, and

    Re Q_B(C_U,mu) = D^(-1) Re(v^* R G v).

All conclusions hold for complex W and unitary column phases. On the accepted nonprincipal blocks P_u=0. On other rows they concern the uncentered C_U-versus-mu covariance only; they do not redefine or separately subtract the original principal residue P.

## 2. A sharp vector-specific lower budget

Assume a proved operator bound 0 <= G <= Lambda_B I on this exact block. Define the three actual coefficient moments

    M_j = v^* R^j v = sum_m r_U(m)^j |W(Nm/D)|^2,  j=0,1,2.

The value of nu drops from these moments because it is unitary off S. If Lambda_B=0 the covariance is zero. Otherwise B_0=2G/Lambda_B-I is a self-adjoint contraction. Therefore

    Re(v^* R G v)
      = Lambda_B/2 [M_1 + Re(v^* R B_0 v)]
      >= Lambda_B/2 [M_1 - sqrt(M_0 M_2)].

This proves the actual lower bound

    Re Q_B(C_U,mu)
      >= - Lambda_B/(2D) [sqrt(M_0 M_2)-M_1].            (VB)

The bracket is nonnegative by Cauchy. This estimate uses the actual factor-count distribution rather than only max r or |Cov| <= sqrt(Q(C,C)Q(mu,mu)). It is sharp among all Hermitian 0<=G<=Lambda_B I for the fixed pair (v,Rv): the Hermitian rank-two matrix [(Rv)v^*+v(Rv)^*]/2 has possible nonzero eigenvalues (M_1 +/- sqrt(M_0 M_2))/2. Choosing G to be Lambda_B times its negative spectral projection gives equality. This sharpness statement is linear algebra, not a claim that an arithmetic Gram attains the extremum.

For a <= r_U(m) <= b on the weighted support, with a+b>0, the pointwise inequality r^2 <= (a+b)r-ab gives

    sqrt(M_0 M_2)-M_1 <= M_0 (b-a)^2/[4(a+b)].

Indeed put t=M_1/M_0 and maximize sqrt((a+b)t-ab)-t over a<=t<=b; the maximum is (b-a)^2/[4(a+b)]. Consequently

    Re Q_B(C_U,mu) >= -Lambda_B M_0 (b-a)^2/[8D(a+b)].  (RB)

If a=0 this is -Lambda_B b M_0/(8D). If a=b=0 the covariance is zero. This is a negative-part budget only; it does not supply the positive lower covariance of size Q(C,C)+Q(mu,mu) demanded by BT_sigma.

## 3. Arithmetic control of the moments, uniform within the high window

The following bounds use the actual ideal factorizations and require only the elementary ideal count N_K(Y) <<_K Y for Y>=1, already established by the accepted Eisenstein lattice count:

    sum_(D<=Nm<=2D) r_U(m)       <<_K D,
    sum_(D<=Nm<=2D) r_U(m)^2     <<_K D log(2D).        (ME)

Restricting to squarefree ideals prime to S only decreases these positive sums. The constants can be chosen independent of U within this window.

Set T=sqrt(D), c=sqrt(2/7), C=sqrt(14). Every counted factor obeys

    cT < Na,Nb < CT.

The first bound follows by counting the O_K(T) possible a and O_K(T) possible b. This is an upper count; no coprimality or raw zero is removed from an identity.

For the second bound, r_U(m)^2 counts two ordered factorizations a*b=c_1*d_1=m. Put g=gcd(a,c_1), a=g h, c_1=g k. Since m is squarefree, h and k are coprime and necessarily

    b=k ell,   d_1=h ell;

indeed g,h,k,ell are pairwise coprime and squarefree. For the positive upper count they may be enlarged to arbitrary ideals. Put M=max(Nh,Nk). The factor upper bounds give

    Ng <= CT/M,   Nell <= CT/M,   1<=M<=CT.

On the dyadic range 2^j <= M < 2^(j+1), there are O_K(2^(2j)) choices of (h,k), and O_K((T/2^j)^2) choices of (g,ell), whenever that range is nonempty. The constants C absorb the terminal ranges where T/2^j is bounded. Hence each range contributes O_K(D); there are O(log(2D)) ranges. This proves (ME). It is a coefficient multiplicative-energy count, not the row-coupled fourth moment.

For the actual common W, the ideal count and (ME) give

    M_0 << ||W||_infinity^2 D,
    M_1 << ||W||_infinity^2 D,
    M_2 << ||W||_infinity^2 D log(2D).

Substituting in (VB) yields the new explicit, cutoff-uniform-in-this-window lower budget

    Re Q_B(C_U,mu)
      >= -C_K ||W||_infinity^2 Lambda_B sqrt(log(2D)).   (AB)

The retained subtraction M_1 in (VB) can make the finite budget materially smaller than (AB). The elementary moment proof has no derivative seminorm, no moving profile, no height dependence and no hidden primitive-conductor replacement. Constants remain for the fixed field; any inherited sieve constants below retain fixed nu,S and epsilon. Nothing here is uniform in changing nu or S.

## 4. The double commutator and a real coefficient-adapted budget

The exact identity proposed in the task is valid:

    (RG+GR)/2 = S_R G S_R + (1/2)[S_R,[S_R,G]].

Its double commutator entries are

    [S_R,[S_R,G]]_mn = (sqrt(r_m)-sqrt(r_n))^2 G_mn.

Thus all diagonal and equal-factor-count-level entries vanish. Define the actual real arithmetic contributions

    t_mn = Re(lambda_m conjugate(lambda_n) G_mn)/D,
    delta_mn=(sqrt(r_m)-sqrt(r_n))^2 >=0.

Then the exact positive term and the coefficient-adapted loss are

    Q_B(sqrt(r)mu,sqrt(r)mu)=sum_mn sqrt(r_m r_n)t_mn >=0,
    B_fix=(1/2)sum_mn delta_mn |t_mn|.

Here the notation sqrt(r)mu denotes only the displayed finite coefficient sequence with the same nu,W and raw symbols. It is not a new arithmetic residue. The useful lower estimate is

    Re Q_B(C_U,mu) >= Q_B(sqrt(r)mu,sqrt(r)mu)-B_fix.    (CB)

It takes absolute values only after the actual phases and common profile have formed the real contribution. A looser phase-blind version has

    B_abs=(1/(2D))sum_mn delta_mn |lambda_m| |lambda_n| |G_mn|,
    B_fix <= B_abs.

Neither budget is asserted small by arithmetic. Equations (VB), (ME), and the unit-class filter below are the proved quantitative information, rather than an assumption that a commutator has a favorable sign.

For calibration, the accepted four-column smooth B7 fixture has r=(0,0,2,2). At profile amplitude x>=0 the new decomposition is exactly

    Q_B(sqrt(r)mu,sqrt(r)mu)=18/25,
    B_fix=9x/50,
    Re Q_B(C_U,mu)=18/25-9x/50.

Thus (CB) is attained on that specific fixture. The phase-blind B_abs is larger because the full complex Gram also has purely imaginary entries, which disappear from t_mn for this real fixture. This distinction matters: the displayed 4-by-4 matrix in the accepted article is Re G, not the full complex G. The old x=10 covariance -27/25 is used only to calibrate this new quantitative identity; it is not presented as a new sign counterexample or an asymptotic obstruction.

## 5. An exact arithmetic deletion in the commutator

If B includes all six literal units on each underlying ideal row, multiplication by zeta_6=1+omega permutes B. For a good prime p, its residue-field norm q is 1 mod6 and

    x_p(zeta_6)=zeta_6^((q-1)/6).

For squarefree m, multiplication over p|m and Nm=product_(p|m)(1+6e_p) give

    x_m(zeta_6)=zeta_6^((Nm-1)/6 mod6).

Therefore

    G_B(m,n)=0 unless Nm == Nn (mod36).                (UC)

This is the actual raw unit sum, not an independence assumption or an artificial extension off the coprime locus. If a row has a shared prime, its raw product remains zero under unit multiplication. Fixed nu and possibly complex W are column factors and do not alter the vanishing.

Consequently G and the double commutator split into six norm classes, and (VB) can be applied separately with their actual M_j and admissible classwise Lambda_B. On each class the commutator still retains only unequal r levels. This is a real arithmetic restriction, but it removes only a fixed number of classes and supplies no D^sigma gain. Unit-incomplete row subsets need not satisfy (UC); no such extension is made.

## 6. Comparison with the accepted arithmetic norm and exact failed step

On B_X the previously accepted powered-BGL estimate, applied to arbitrary length-D coefficients with every zero retained, gives

    Lambda_(B_X) <<_(nu,S,epsilon) (DX)^epsilon
                    [X^2 + DX + D^(2/3)X^(5/3)].        (LS)

This is an inherited external analytic input, not a theorem newly proved here. Combining (AB) and (LS), with the logarithm absorbed in an arbitrarily small loss, proves

    Re Q_(B_X)(C_U,mu)
      >= -C_(nu,S,epsilon) ||W||_infinity^2(DX)^epsilon
             [X^2 + DX + D^(2/3)X^(5/3)].              (LOW)

At X~D^(1/4) the exponents remain 1/2,5/4,13/12. The middle covariance budget still has exponent 5/4. At H=D^(3/4) this is the same exponent 1/2 above H as the existing U-independent energy envelope. The factor-count moment proof improves the explicit coefficient bookkeeping to a square-root logarithm; it does not improve the power.

The exact failed analytic inference would be to replace Lambda_(B_X) in (VB) by D^(1-sigma)X (or claim B_fix has that scale) merely because equal-r entries and different norm classes vanish. The proved large sieve still has DX on each of the remaining finitely many classes. The moment bound (ME) supplies only the ordinary coefficient diagonal ab=c_1d_1; it has not estimated the unequal-product character quadruples in the row-coupled fourth moment. No generic positivity/contraction argument upgrades that coefficient count to a better arithmetic operator bound.

There is a second separate gap: even a small negative-commutator loss alone would not imply BT_sigma. Let lambda_k be lambda restricted to r=k, and let q_kl be the exact normalized raw Gram pairing of those sequences. Then

    Q_B(A_U,A_U)=sum_kl (k-1)(l-1) q_kl.

If all different-level pairings were zero, the energy would still be

    sum_k (k-1)^2 q_kk.

The high-window levels k are even, so the nonzero coefficient (k-1)^2 is at least one, and each q_kk is nonnegative. Controlling the commutator's negative part is therefore weaker than the required lower covariance

    2Re Q(C_U,mu) >= Q(C_U,C_U)+Q(mu,mu)-R_sigma.

One must also establish the appropriate cancellation of the actual within-level energies against different-level pairings, or directly bound the signed (r-1) sequence. Neither is supplied by (VB), (ME), (CB), or (UC). The accepted finite -27/25 example by itself never ruled out a lower covariance budget; the present quantitative calculation shows exactly which available budget is too expensive.

## 7. Neighboring near-saturating blocks: the full face survives

For the accepted six-factor dyadic row decomposition, put

    R_0=product_(j=1)^6 A_j,  M=max(A_1,A_2),
    product_(j=1)^6 A_j^j <= H.

Retain all pairwise-coprime squarefree masks on a_1,...,a_5, the arbitrary a_6, fixed S-part and all six units. On each such block the inherited operator bound is

    Lambda_A << (HD)^epsilon
       [R_0 + D R_0/M + D^(2/3)R_0/M^(1/3)].           (NB)

The new column moment estimate and covariance proof apply unchanged to the exact raw Gram of this block. In particular they do not control only one selected B_X.

There is a useful exact description of the troublesome middle-term geometry. Write x_j=log A_j, h=log H, r_0=sum_j x_j, m=max(x_1,x_2), and c_0=sum_j j x_j <= h. Then

    h-3(r_0-m)
      = h-c_0 + (x_1-x_2)+x_4+2x_5+3x_6,   x_1>=x_2;
    h-3(r_0-m)
      = h-c_0 + 2(x_2-x_1)+x_4+2x_5+3x_6, x_2>=x_1.

Every term on the right is nonnegative. Exact saturation R_0/M=H^(1/3) therefore occurs on the whole face

    A_1=A_2,  A_1*A_3=H^(1/3),  A_4=A_5=A_6=1,
    product_j A_j^j=H.

The familiar balanced a_1*a_2^2 block is the endpoint A_3=1, not the whole saturation set. Cubic-power rows with a_3 nonunit occur along the same face. They are still nonprincipal outside S because valuation 3 mod6 is nontrivial; the original residue does not remove them. Exact fixed dyadic endpoint constants only change this description by bounded factors.

Near saturation R_0/M >= H^(1/3)D^(-eta) permits total logarithmic slack at most 3eta log D in the displayed identities. This includes both neighboring a_1/a_2 wedges, small a_4,a_5,a_6 and the complete A_3 direction. Inserting (NB) into the new covariance budget leaves D R_0/M, hence exponent at least 5/4-eta when H=D^(3/4). A fixed D^sigma improvement must control this full neighborhood uniformly; treating only exact A_1=A_2 and A_3=1 is insufficient. The separate global mixed term still reaches D^(7/6), so even removing the middle term would not produce the desired H-sized global energy.

## 8. Surviving lemma, next target, and check boundary

Surviving new results are the sharp actual-vector lower covariance budget (VB), its range specialization (RB), the uniform-in-the-high-window ideal moments (ME), the exact coefficient-adapted commutator budget (CB), the raw unit congruence filter (UC), and the full saturation-face/slack identities. The commutator identity itself was proposed in the task; no novelty is claimed for the elementary linear algebra.

The next substantive target is a signed estimate for the unequal-product portion of the actual coupled fourth moment, jointly with the C_U-versus-mu mixed term, after preserving the complete hyperbolic a,b support and union mask supp(ab*c*d). The coefficient diagonal ab=c*d has now been counted in (ME). For distinct products the oscillatory conductor is their squarefree symmetric difference, while the zero mask remains their union, including common primes. A proposed power gain must bound these remaining character quadruples before absolute Cauchy and must retain the near-saturating face in section 7. Merely iterating the present norm estimate, assuming independent row factors, restoring a raw zero through primitive conductor drop, or shifting reciprocal-L contours without residues does not perform that step.

The new standard-library checker independently implements Eisenstein multiplication, ideal factorization, split/inert residue-field exponentiation, and exact Q-linear combinations of square roots. It imports no project or author arithmetic helpers. Its finite common profiles are exact rational/complex norm tables, each realizable by disjoint smooth bumps at the finite integer norms. This validates the finite algebra; it is not a test of an infinite smooth-profile estimate. The four-column cases use precisely the accepted genuine smooth bump family. The other finite families are explicitly diagnostics, and their row bounds are not claimed to equal H=D^(3/4).

The v2 checker passes 9 complete-annulus moment cases (D=128,400,1024,5000), all their quadruple reparametrizations, and 8 actual Gram cases: four calibrations of the accepted smooth four-column fixture; three complete 119-column D=400 annuli on B7, including nu=kappa_2 and all raw zeros; and a six-column case with r levels {0,2,6}, complex common profile, fixed nu=kappa_2, and all literal units. It checks 27,000 directly evaluated phase values, retains 5,184 raw zero entries, verifies the exact radical commutator identity, both coefficient-adapted and phase-blind budgets, their ordering, the sharp vector lower budget, and norm-class vanishing. A separate exhaustive 227-point rational exponent grid verifies the exact slack formulas and all five saturating grid points. Counts are finite diagnostics, not proofs of (ME)'s asymptotic estimate or the inherited classical sieve.

Command (the output directory must be fresh):

    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/covariance-budget-20261105/attempt/check_covariance_budget_v2.py --output outputs/checks/2026-11-05-covariance-budget/attempt/exact-v2

The v1 script/report are preserved as prior development evidence. No build, Lean run, GPU/model work, dependency change, MCP activation, authentication, external write, publication, queue edit, source replacement, environment or cache operation was necessary. This attempt proves no BT_sigma or new analytic exponent and leaves every complete GRH scope open.
