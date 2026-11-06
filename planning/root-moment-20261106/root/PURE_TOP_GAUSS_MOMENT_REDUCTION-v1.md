# Pure top-band principal mean as one actual Gauss-column moment

Research-only candidate v1, 6 November2026. This note does NOT prove the remaining signed estimate. It removes the Bessel and finite-k approximation errors in a restricted actual principal mean, with quantitative errors, leaving one explicit signed Gauss-column moment. All new derivations/checks run on Linux via SSH. No canonical book, PDF, UI, released worktree or old input is modified.

## 1. Scope and fixed parameters

Use the exact primitive kernel and actual root transport in papers/coherent-band-{core,details}.tex, the actual mean in planning/coupled-sixth-20261106/lane-a/COHERENT_SIXTH_PART_RAY_MEAN-v1.md, its accepted sharpened error, and planning/principal-mean-20261106/lane-a/PRINCIPAL_MEAN_COMPENSATION_AND_ROOT_SELECTOR-v3.md. Their source/ray/S hypotheses are not enlarged.

Specialize ONLY to the actual pure two-pivot block A2=1. Thus the second ideal is the unit, l=O, R=A1. The original first row annulus and capacity have integer endpoints a,b from cbk:nodal. If b<a there is no contribution and we define everything below as0. Otherwise b>=ceil(A1)>=A1, and the ORIGINAL pre-S cutoff is K=sqrt(b)>=sqrt(A1). Do not recompute K after e deletion or dual truncation.

The complete original good SF IDEAL columns satisfy D<=Nm<=2D,D>1; c_m=A_U(m)nu(m)R_m(u0)W(Nm/D), with actual A_U, original fixed nu, ONE possibly complex common fixed smooth W supported[1,2], and B=||W||infinity. u0 is the original fixed literal unit/S-supported factor with no good support. No extra good factors, varying-u0 sum, arbitrary row weights, learned columns or selected-column replacement occurs.

Let I be the original coprime ordered column pairs; optionally impose the ORIGINAL unequal-norm condition before the representation. Either choice is used consistently throughout. Keep every source class pair A,B and selected ray rho with rho^6=1. The actual primitive character eta=xi_m bar(xi_n) sigma has total type0, F=Nf_S Nm Nn, root epsilon(eta), all original good and S raw zeros, and coefficient h_ABrho(O). All other rho branches and the ray-count discrepancy remain in the original prefix and its accepted error; they are not estimated by this note.

Take X>=64 and the TOP GOOD-sixth-part band V=X^(1/6)/2. The accepted principal mean M_top is unnormalized; divide ONCE by D. At this band the sixth-free compensation has only a=O, since64<7^6. Consequently the exact retained mean sums ALL ideals w of norm<64 (including nonunit S modes), with interval length

 ell_w = [min(2V,(X/Nw)^(1/6))-V]_+
       = X^(1/6) t_w,   t_w=(Nw^(-1/6)-1/2)_+.

The boundary Nw=64 has length0; no actual discrete endpoint assertion is changed here. At fixed D,A1,capacity,U,nu,W,u0 and ray data, these t_w are independent of X.

## 2. The explicit remaining arithmetic moment

Let C0=3/(4pi^2), G the ACTUAL nodal capacity interpolant (not W),
g0=C0^(-1/2)integral G(v)dv, 0<=G<=1, suppG subset[1/2,5/2].
The derivative-free inputs are integralG<=2, integral vG(v)dv<=3.

For q=mn define precisely

 T=S union supp(q),
 Q_2^T(K;eta^2)=sum_(Nk<=K,(k,T)=1)mu(k)eta(k)^2/(Nk)^2,
 E_T(eta)=product_(p outside T)(1-eta(p)^2/(Np)^2),
 P_S(eta)=sum_(e|P_S)mu(e)eta(e)/Ne
        =product_(p in S)(1-eta(p)/Np),
 T_64(bar eta)=sum_(w integral,Nw<64)t_w bar(eta(w)).

E_T is absolutely convergent. Inducing eta^2 after squaring never restores T. The primitive eta(e) and eta(w) at S, including0, are retained; no division by an S value or nonprimitive Gauss sum occurs.

Define the ACTUAL column moment

 G_D = (kappa_S g0/D)
   sum_(A,B,rho^6=1) h_ABrho(O)
   sum_((m,n) in I of classes A,B)
    c_m bar(c_n) g(m)g(n) [epsilon(eta)/sqrt(F)]
              P_S(eta) E_T(eta) T_64(bar eta).                 (G)

Here g(m)=product_(p|m)(1-1/Np). Only on original coprime support g(q)=g(m)g(n). Different f_S/root weights remain INSIDE the component sum. Formula(G) includes all selected source/rho/S modes and orientation means. It is not PSD; the coprime projection is still present. It is not a bare unweighted character or root sum. All coefficients and primitive roots are actual, not chosen independent labels.

At fixed original parameters G_D is independent of X. Its definition still depends on A1 and the exact row capacity through g0, and on all actual c_m/root/ray/conductor data. The elementary count gives merely |G_D| <<_(fixed data,eps) B^2 D^eps. This is not the missing cancellation.

## 3. A target-sized reduction error in the low-Bessel range

Set lambda=A1 X/D^2. Then uniformly in the original data,

 |M_top(X)/D - A1 X^(1/6) G_D|
  <<_(fixed S/ray/source/step,eps)
       B^2 (DX)^eps A1 X^(1/6) [lambda+K^(-1)]
  << B^2 (DX)^eps [A1^2 X^(7/6)/D^2
                            +sqrt(A1) X^(1/6)].               (R)

Weak inequalities include B=0 and G=0. The formula holds for all finite X>=64; calling the remainder small requires the displayed powers, not an unstated small-X assumption.

Proof. For x>=0 the angular formula for J0 and |1-cos y|<=y^2/2 give
 |J0(2sqrt z)-1|<=z.
Thus
 |dotG(x)-g0|<=C0^(-3/2) x integral vG(v)dv
             <=3 C0^(-3/2)x.
On EVERY actual w,t,k,e support, x=A1 Nw t^6/[(Nk)^2 Ne F]<=lambda.
Replace dotG by g0 ONLY in an error estimate, keeping the actual principal mean until this step. The exact root/modulation factor has modulus A1/[Nk^2 Ne sqrtF]; original column count O(D^2), once-only /D and sqrtF>=D cancel those column scales. The original finite k sum has absolute budget sum Nk^(-2)<=zeta_K(2), e/source/rho are fixed finite, and there are finitely many w<64 with ell_w<=X^(1/6). The actual bound |A_U|<<D^eps, uniformly in U, is used ONLY in the error. This gives the first error A1 X^(1/6)lambda. No derivative of G or its sharp nodal capacity appears.

The constant-Bessel main has EXACT finite Q_2^T(K;eta^2), multiplied by every original root/c_m/e/w/rho weight. Use the already accepted ideal count A_K(t)<=2t solely in the ABSOLUTELY CONVERGENT comparison
 |Q_2^T(K;eta^2)-E_T(eta)|<=sum_(Nk>K)(Nk)^(-2)<=4/K.
The main E_T stays signed/complex with all q deletions; this is not the failed fractional-moment completion at exponent5/3 and drops no endpoints. The same outer error count gives A1 X^(1/6)/K. Only after this bound do we use K>=sqrt(A1). Summing e is the exact finite P_S, and summing w is the exact finite T_64. This proves(R) and(G). No signed inequality was assumed to obtain either error.

## 4. Quantitative meaning and the unsuccessful next step

Write A1 comparable to H=D^theta and X=D^x, suppressing constants and allowed epsilons. The two remainder powers in(R) are

 2theta+7x/6-2,   theta/2+x/6.

They are at most theta if x<=min((6/7)(2-theta),3theta). This is a sufficient budget for errors ONLY. At the critical pure theta=3/4 and the previously studied x=3/8, they are -1/16 and7/16, both below3/4. The elementary principal-main budget remains A1 X^(1/6), power13/16. Obtaining the principal target from(R) therefore requires the ACTUAL signed moment |G_D| << B^2(DX)^eps X^(-1/6), i.e. a D^(-1/16) saving at those scales. With errors already target-sized, this is equivalent to a target bound for THIS principal mean alone. It is NOT a necessary condition on the original full signed assembly or on each split component.

The restricted remainder budget extends up to x15/14 for theta3/4; this is NOT a new finite-prefix or actual-band range. It concerns only approximation of a retained mean by an UNESTIMATED G_D. In particular the inherited fixed-s actual-band bound and whole signed13/12/global9/8 are not improved.

Even a successful G_D estimate alone would not prove a target bound for the original top prefix using the accepted separate ray error: its bound is
 |P_top-M_top|/D << B^2(DX)^eps A1 X^(1/18)
                         (1+sqrt(A1X/D^2)).
At theta3/4,x3/8 its leading power is37/48, still1/48 above3/4. That is an UPPER certificate, not an actual error lower bound or impossibility statement. The actual root/column moment and the discrete-s discrepancy must be bounded jointly or the separate error must be improved by a genuinely signed argument.

Taking absolute values in(G) only returns |G_D|<<B^2D^eps and the old13/16 principal-majorant. The finite number of w values, convergent E_T, bounded densityg and two unitary root gauges supply no D^(-1/16) automatically. Treating them as random phases, deleting w=O, centering, dropping orientation means, or applying a positive complete-row norm to the coprime slice is the FAILED next step. We have not shown the target bound for G_D or nonvanishing/lower bounds for G_D/M/P/energy. Its signed cubic/Gauss-column content with actual A_U remains the arithmetic research task.

No new analytic/category Lean or GRH statement. All short/principal/full target assembly, determinant/zero-location and scope-specific Dirichlet/Hecke/Dedekind/elliptic/general Artin obligations remain open.
