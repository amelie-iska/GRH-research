# Fixed-field prime substitution in the actual coherent A–A main sum

Status: NEW unpublished postrelease derivation/budget. The outcome is an exact coherent Stieltjes embedding and an explicit inherited operator-cost bound. It does NOT prove a new power saving, target moment, lower bound, GRH, determinant comparison or Lean result. No old experiment/checker is executed. All formulae refer to ideals, counting conjugate prime ideals separately even when their rational norms agree.

## 1. Exact raw objects and the actual masks

Use the accepted rough v3 hypotheses: K=Q(omega), fixed S containing primes above2,3 and the defining conductor of the original nu, one fixed possibly complex W supported in[1,2], endpoint values0, and

    1<=U, U^2<=D, 2D<=7U^2.

Keep the ACTUAL finite literal/ray/capacity row family R, with Nu<=H, and its nonnegative weights w. Put R_w=sum_u w_u and B=||W||infinity. The original column-pair gcd sector is h=1; the U-smooth common-divisor factor below is a DIFFERENT variable f. For generic principal rows the original residue correction remains separate: the identities concern the raw slice. Nonprincipality of the intended first-factor blocks uses the original nu conductor supported in S.

For f squarefree good with every prime norm<=U write F=Nf and define, for REAL t>0,

    T_f(t;u)=sum_{a SF good,(a,f)=1}
          A_U(fa) nu(a) chi_a(u) W(F t Na/D),
    G_f(t)=sum_{u in R,(f,u)=1} w_u |T_f(t;u)|^2.             (1)

The original A_U(fa) is not factored. All raw chi_a(u) zeros survive, as do (a,fS)=1 and (f,u)=1. Literal-unit/S-ray/capacity restrictions remain in the actual row set. No independent marginal family is inserted. Arbitrary sixth-power factors, when present in an actual row, still enter these raw masks. The abstract identities below allow them; a later classical-operator corollary is explicitly narrower.

Define RAW sums

    K0=sum_{f SF good,U-smooth} mu(f)G_f(1),
    KS=sum_{f SF good,U-smooth} mu(f)
             sum_{p good prime ideal,Np>U} G_f(Np).           (2)

The sign mu(f) remains outside the coherent row norm. There is no extra mu(q), no free prime phase and no changing W. In KS the prime p is deliberately UNMASKED from a and u; this is not the original KT. The actual raw slice satisfies exactly

    S_AA^raw=(K0-KT+Ctwo)/D
             =(K0-KS)/D + Delta_mask+Ctwo/D,
    Delta_mask=(KS-KT)/D.                                  (3)

KT retains p not dividing a,b,u. Ctwo is the accepted UNIT-RESIDUAL unordered DISTINCT two-rough-prime correction with its actual row masks. It is kept intact here. A's separate mask theorem bounds Delta_mask and, in its v2 clean-main bookkeeping, Ctwo/D at target row-mass cost. That elementary correction bound is not an oscillatory estimate of the CLEAN main (K0-KS)/D.

Expanding G_f recovers the original coherent (a,b,u) sum including overlapping residuals. Since p is unmasked in KS, it enters only the radial common profile. This permits an untwisted prime-ideal counting measure. It does not justify replacing a fixed-row/ray Hecke character sum by a conductor-uniform prime theorem. No extra column-ray selection beyond the accepted full good-ideal/nu formulation is silently added or removed.

## 2. The exact operator-valued Stieltjes remainder

Let pi_K^S(x) count prime IDEALS p not in S with Np<=x. For U>=7 put

    E_S(x)=pi_K^S(x)-Li(x),
    delta_S(U)=sup_{x>=U}|E_S(x)|/x.                        (4)

This definition includes finite S deletions. It is not an assertion that growing T=S union supp(abu) has a uniform prime-theorem constant. Only the fixed S measure is approximated; all growing-mask errors stay in (3).

For each f with a nonzero rough branch, F<2D/U. On t>=U the union of active a is finite, Na<=2D/(FU). Thus G_f is C-infinity there, and vanishes for t>=2D/F; endpoint smoothness removes upper boundary terms. Define

    J=sum_f mu(f) integral_U^infinity G_f(t) dt/log(t).

Stieltjes partial summation gives the EXACT formula

    KS=J+EPIT,
    EPIT=sum_f mu(f)[-G_f(U)E_S(U)
                         -integral_U^infinity E_S(t)G_f'(t)dt].         (5)

The lower endpoint is pi(U), so Np=U is excluded exactly as required by Np>U. A norm with two conjugate prime ideals creates a jump of2, not1. Formula(5) holds before any absolute f sum or residual-column triangle. Consequently

    S_AA^raw=(K0-J)/D +Delta_mask+Ctwo/D -EPIT/D.             (6)

Even an exact prime density would leave K0-J as a signed coherent arithmetic quantity. Replacing it by independent marginal coefficient sums has not been justified.

## 3. Variation controlled by a TRUE positive row operator bound

Set M1(W)=max(||W||infinity,||xW'(x)||infinity). Let lambda(L) be a TRUE arbitrary-coefficient squared norm bound for the ORIGINAL specified positive row operator on squarefree good a with Na in[L,2L]. It must include the actual row weights or dominate their positive norm. The abstract result does not insert classical unweighted constants for arbitrary w.

On an active rough dyad put L=D/(Ft). Section6 gives the stronger exact |A_U(fa)|=1. Ideal counting and the operator input give the following convenient bounds; the displayed epsilon is harmless here and retains the accepted classical operator loss when that input is used (no coefficient-growth loss is necessary):

    G_f(t) << (HD)^epsilon M1(W)^2 lambda(L)L,
    |tG_f'(t)| << (HD)^epsilon M1(W)^2 lambda(L)L.            (7)

For the second bound differentiate only the common W: t*d/dt replaces W(x) by xW'(x). Weighted row Cauchy compares the two positive row norms; no coefficient, raw zero or phase is dropped in an equality. A common f-row mask may be enlarged only inside these positive norm estimates.

For 1/2<=L<1 the only possible a is the unit; use direct lambda_*(L)=R_w and #a<=2L. For L>=1 use the assumed lambda(L). There are no active columns for L<1/2. With L_f=D/(FU), (5) and(7) yield

 |EPIT|/D << (HD)^epsilon M1(W)^2 delta_S(U)
      sum_{f SF good,U-smooth,F<2D/U} (1/F)
        [lambda_*(L_f)+integral_(1/2)^(L_f)lambda_*(L)dL/L].            (8)

This is a coherent ERROR bound. The absolute f sum occurs here, after the exact operator identity; mu(f) remains unchanged in KS and J themselves. It is not a lower bound for the error and does not show actual errors cannot cancel.

For arbitrary nonnegative weights a completely unconditional choice is the Frobenius bound lambda(L)<<R_w L for L>=1, and R_w for the subunit interval. Then

 |EPIT|/D << (HD)^epsilon M1(W)^2 delta_S(U) R_w
                         [D/U+log^2(2D)].                  (9)

This bound alone is substantially too large for a target of order R_w when U~sqrt(D).

## 4. Accepted UNWEIGHTED two-pivot specialization and its exact cost

Now, ONLY for the accepted original A6=1 unweighted two-pivot block (or bounded natural literal multiplicities for which the same positive input is established), put

    R=A1 A2, P=max(A1,A2), A1 A2^2<=H.

The original actual unit/ray/capacity restrictions are retained. R_w<<R up to the accepted divisor/literal factors. The accepted arbitrary-coefficient inputs at L>=1 are

 lambda(L) << (HD)^epsilon min{
       R+LR/P+L^(2/3)R/P^(1/3), L+R^2}.                     (10)

No unweighted input is claimed for arbitrary row weights, varying sixth factors or enlarged primitive conductor families. Frozen extra column phases/masks can be absorbed only when the already established arbitrary-coefficient input actually permits it.

Using the first bound in(10), and the direct unit-column norm below L1, evaluate(8). The R term uses sum_(F<=X)1/F<<log(2X), while the linear and2/3 terms use convergent ideal sums sum F^-2 and sum F^-5/3. This gives

 |EPIT|/D << (HD)^epsilon M1(W)^2 delta_S(U) Bop,
 Bop=R log^2(2D)+(D/U)R/P+(D/U)^(2/3)R/P^(1/3).             (11)

The elementary prime-density integral has the inherited positive estimate

 |J|/D << (HD)^epsilon ||W||infinity^2 Bop/log(U),            (12)

obtained from the same positive norms and dt=-(D/F)L^-2dL. This is the KNOWN kind of high-gcd/pure-sector recovery cost, not a new signed gain. It does not bound K0-J at the target. One can keep the min in(10) inside(8) for individual blocks; using the first branch suffices to expose the surviving worst cost.

Capacity implies R<=H, R/P<=H^(1/3), R/P^(1/3)<=H^(2/3). For example the last inequality follows separately for A1>=A2 and A2>=A1, using A1 A2^2<=H and A_j>=1. Hence

 Bop << H log^2(2D)+(D/U)H^(1/3)+(D/U)^(2/3)H^(2/3).        (13)

At H=D^(3/4) and the REQUIRED near-root U~sqrt(D), the three displayed exponents are respectively3/4,3/4,5/6. The5/6 term occurs in this MAJORANT on admissible pure-scale lengths A1~H,A2=1 (take fixed capacity slack rather than an empty exact endpoint). Thus classical prime-density replacement is not automatically a target-size error: its available normalized bound is D^(5/6+epsilon)delta_S(U), while the target is D^(3/4+epsilon). This exposes a1/12 power deficit in THIS certificate. It is not an actual-error lower bound or a counterexample to another method.

## 5. What fixed-field PIT actually provides

The pinned primary source is Thorner--Zaman, A unified and improved Chebotarev density theorem, ANT13(2019),1039--1068, DOI10.2140/ant.2019.13.1039, Theorem1.1 on printed1040. Specialize the trivial extension K/K: n_L2,D_L3. Its counting function includes ALL prime ideals, including split multiplicity and inert prime norms.

For fixed K, the possible exceptional real zero is fixed. Retain its secondary Li(x^beta) contribution, or absorb it together with the fixed-parameter power error into fixed-K constants/threshold. Finite S deletions are included in delta_S. The theorem therefore supplies, for sufficiently large U depending on fixed K,S,

    delta_S(U) <<_(K,S) exp(-c_K sqrt(log U)).                (14)

No absence of an exceptional zero or GRH is assumed. No uniformity over a growing row conductor, growing deleted T or varying field is asserted. Initial bounded U may be treated directly; the asymptotic claim here is for U beyond this fixed threshold. Sharper classical subpower remainders or logarithmic refinements do not change the following power accounting.

The available bound D^(5/6)exp(-c sqrt(log U)) is NOT O(D^(3/4+epsilon)) for every epsilon: for fixed epsilon<1/12 the ratio of these displayed bounds grows. This diagnoses the failed inference that a pointwise o(1) prime-density error remains negligible after the coherent operator variation and f summation. It does not prove that the actual signed EPIT is this large.

A hypothetical delta_S(U)<<U^-1/6 would make the worst error in(11) target-budget size at this scale (up to D^epsilon). Such a fixed power error is NOT supplied by the cited unconditional theorem. Even if it were granted, the coherent signed K0-J would still need an original arithmetic estimate.

## 6. A stronger exact coefficient simplification for ALL U>=1

For every GOOD squarefree ideal g with Ng<=7U,

    A_U(g)=mu(g)[2*1_(Ng<=U)-1].                            (15)

Indeed every proper divisor x of nonunit g has Nx<=Ng/7<=U, since its complementary nonunit good ideal has norm>=7. The unrestricted sum over ordered disjoint x,y is product_(p|g)(1-1-1)=mu(g). If Ng<=U every assignment is admitted. If Ng>U the only excluded assignments are (x,y)=(g,1),(1,g), each of weight mu(g). Thus A_U(g)=mu(g)-2mu(g). For g=1, U>=1 gives A_U(1)=1 directly. This uses ideals, so equal rational prime norms and rational nonsquarefreeness do not change it.

On the rough branch t=Np>U, Nfa<2D/U<=7U. Consequently, for ALL U>=1,

 T_f(t;u)=mu(f) sum_{a SF,(a,fS)=1} mu(a)nu(a)chi_a(u)
          [2*1_(F Na<=U)-1] W(FtNa/D),                    (16)

and every active original A_U(fa) has absolute value1. This retains BOTH coupled cutoffs, every raw zero and the external mu(f). The factor mu(f) inside the absolute square cancels only its own magnitude; the original outer mu(f) in KS/J remains. It is not a general factorization of A_U(fa), nor a uniform Mertens theorem for growing actual row conductors. The coupled indicator depends on BOTH f and a.

This stronger local coefficient lemma does NOT extend the analytic Li/Stieltjes definition in Sections2--5 to U1: there we retain U>=7 (or an equivalent positive lower bound away from the Li singularity). For U<7 the original high window bounds D, so a separate finite-range treatment is available if needed; it is not invoked as an asymptotic prime theorem here.

## 7. Precise outcome

The valid result is(5),(8),(11) with fixed-profile seminorm and fixed-S prime error, plus the exact restricted coefficient identity(16). The unproved step is a quantitative estimate of the actual mean-retaining K0-J and/or cancellation in its signed prime error beyond the positive majorant. A's elementary mask correction and unit two-rough bound make those discarded-mask pieces affordable; they do not supply this oscillatory saving. The original7/6 envelope and missing5/12 global saving remain unchanged. The frozen279-page/233-path release and all old scientific artifacts are untouched.

Primary PDF/text/HTML snapshots are a local pinned reading cache only. Any later public artifact should include the citation, DOI and hashes of that cache, not redistribute the full publisher paper.
