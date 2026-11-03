# Perturbed low-energy application

## Result, scope and pinned input

The low estimate extends to ell=1/6+t, M=5/6−t, l_x=17/48−t/2, l_y=23/48−t/2 for0<=t<=1/30, **conditional on** the same general reflected-energy estimate, completed-row/sector identities, quantitative Gram estimate and finite low separation, with their stated smoothness and uniformity properties. The extension does not assume an improved zero-free boundary, or even the prior7/8 theorem. Those deep arithmetic identities and estimates remain independently uncertified. This is not a new unconditional zero-free theorem or a proof of GRH.

Pinned source: math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob268c4e3206d460c617d3d2129742a72b831b3def, repository commit4eaee87548250b2682affda7d05d947c05554bae. Focused passages: Gaussian partition1288–1334; sector identity2460–2515; exact low separation3435–3481; finite compensated expression6850–6930; reflection data7663–7804; general energy application8065–8342; quantitative Gram8345–8560; low assembly8563–8643. Existing source arithmetic data, excluded primes and all original zero extensions are retained.

For every fixed finite system of positive slot lengths of total ell, with the same disjoint physical prime windows and smooth weights, the conditional conclusion is

    |I_eta,modified,t(Z)| << Z^(3/16−t/4+epsilon)

for every epsilon>0. The implied constant and threshold may depend on the fixed slot system and tests. The exponent has no slot-mesh loss. No choice of a moving slot system or uniformity as its slot count tends to infinity is asserted.

## Geometry and actual rescaled subsets

Fix J and put d=sum_(i in J)ell_i, 0<=d<=ell. The rescaled product is q_(p_J)=Z^d r_J with r_J in one fixed compact subinterval of(0,infinity). Thus

    X'=Z^(l_x−d)/r_J, Y'=Z^(l_y−d)/r_J,
    M'=M−2d, ell'=ell−d, M'+ell'−1=−3d,
    Q=q_(b_*)X'Y'~Z^M', P_a=Y'^2/Q=q_(b_*)^(-1)Z^(1/8).

The exact finite two-term definition still makes sense at these positive real lengths; its algebraic rescaling is unchanged. The low separation is invoked with the SAME marked completed factor B^J after summing the surviving slots. It is not an estimate for a surrogate probe. In particular the fixed tuple p_J changes the row ball Q through X',Y', while B^J has no new tuple-dependent moving mask.

For all0<=t<=1/30 and every J,

    l_x−d>=11/80, l_y−d>=21/80, M'>=2/5,
    l_y−d−11(1/8)/6>=1/30.

So Q,Y',P_a>=1 eventually, uniformly in the fixed tuple ratios, and P_a²/Y'<<P_a^(1/6). This supplies the actual Gram hypotheses, not just the final low exponent equality. The source Gram estimate then gives

    sum_(q_m<<Q)|A_(m,sigma,nu)(Y')|²
       << (1+|nu|)^J_Gr (Q/Y') P_a^(1/6) Z^epsilon.

The source's allowed fixed polynomial ranges for Q,Y' apply. Its test profiles and fixed ray class are unchanged.

## General reflected-energy hypotheses

The marked completed series has completed scale Z q_(p_Jc), hence nominal log-length N_*=1+ell' before Gaussian annular recentering. Apply the fixed translate partition to the entire joint profile

    w_(k,J)(x,rho)=chi(log x) W_G(e^k x/product rho_i) product W_i(rho_i).

All log ratios lie in fixed compact sets. For each fixed seminorm order j and exponential weight A, the Gaussian gives a summable total sum_k exp(A|k|)p_j(w_(k,J)). Annuli outside |k|<=kappa_G logZ+O(1) have smaller than any prescribed polynomial total row norm after fixing the tail order; this follows from quadratic decay in k versus polynomial counting. Keep whole annuli and separate a COMMON joint Fourier density. Do not choose a different density for each tuple or row. At a retained annulus,

    N_*=1+ell'+theta, |theta|<=kappa_G+O_fixed(1/logZ).

The normalization q_c^(-1/2)q_n^(-1) is not recentered; no unexplained exp(k) factor is inserted. The separated coefficients remain bounded product-form and independent of the moving row and other slots. Their norm twists have finite polynomial height cost, integrable against the weighted common Fourier density. Use Minkowski before squaring the row norm.

For the arithmetic application, f=1 and puncture rho=1. Fixed ray sectors handle all nonzero element rows including those meeting S, with every original zero extension; no extra xi(m) or S mask is imposed in this row norm. Freeze the actual powerful and S-supported parts before taking a residual-row dyad H. The fixed row ball and its actual annular cutoff are independent of surviving active slots and dual variables. The explicit primal row/mark collision mask is the permitted one in the energy statement, not an arbitrary pair-dependent mask.

All non-slot moving primes in A_0 belong to the powerful row part with valuation at least two. With epsilon_Z=O_fixed(1/logZ)>=0 containing the fixed support/conductor offsets, the actual lengths satisfy

    −epsilon_Z<=O, H<=M'−O+epsilon_Z, 2A_0<=O+epsilon_Z,
    0<=N_0<=A_0, S_0,B_0>=0, 0<=z_a<=ell'.

The dual centers v,ell_b can be chosen nonnegative as the energy statement requires, while e_lambda>=−epsilon_Z. The source dual ideals retain all permitted S primes and may share primes; no new coprimality between n and b is introduced. The count of frozen parts is already included in E_ref through O/2, and is not counted twice. The small kernel amplitude is extracted from the common density on the ACTUAL H dyad before any positive row enlargement. Recomputing it on rows added later would not justify the same saving.

## A uniform exponent bound with explicit offsets

Write z=z_a, S=S_0,N=N_0,B=B_0,e=e_lambda, and

    T=2H+2A_0+2z−1−ell'−theta−N−3B,
    y=v+3ell_b+e, u=min(v,z,(v+z)/3).

Retention is y<=T+tau, tau>=0. The actual reflected exponent is

    E=O/2+max(H,v+ell_b)−S−B+z−u−ell_b−2e/3−(T−y)_+/2.

The support inequalities and M'+ell'<=1 give

    T<=H+2epsilon_Z+|theta|,
    max(H,v+ell_b)<=H+3epsilon_Z+|theta|+tau.

Since v>=0, either u=z or u>=v/2. In the first case the remaining z−u vanishes, and the nonpositive kernel can be discarded using its sign. In the second case,

    T/4<=y/4+(T−y)_+/2,
    u+ell_b+2e/3+(T−y)_+/2>=T/4−5epsilon_Z/12.

The negative unit-length allowance is necessary: at v=ell_b=0,e=T=−epsilon_Z the last error5epsilon_Z/12 is exact. After substitution of T and use of2A_0−N+B+4S>=0, both branches give the uniform bound

    E <= M' + ((1+3ell'−2M')/4)_+
             +6epsilon_Z+2|theta|+tau.

This formula is proved in Lean for the displayed REAL exponent and explicit support/retention hypotheses. It does not assert that the arithmetic sum has that exponent; the general source energy lemma remains the analytic input. The conservative constants absorb the source's bounded negative unit dyads and do not require any zero-free premise.

For an explicit allocation, choose kappa_G<=epsilon/32 and tau<=epsilon/16, then take Z large enough that the combined support/annulus offset epsilon_Z<=epsilon/128. Since |theta|<=kappa_G+epsilon_Z, the displayed offset6epsilon_Z+2|theta|+tau is at most3epsilon/16. Allocate the remaining allowance to the source output, common separation and dyad-count losses (for example at mostepsilon/4 collectively to each), keeping a positive reserve. All lengths remain in fixed bounded ranges, so the general lemma applies uniformly. Gaussian tails, finite local/sector choices and logarithmically many actual dyads fit the loss budget. Consequently, conditional on that lemma and the stated identities,

    sum_(0<q_m<<Q)|B^J_(m,sigma)(Z)|²
       << Z^[M'+s_t(d)+epsilon],
    s_t(d)=((-1/6+5t+d)/4)_+.

The individual claim s_t(d)=0 for every perturbed subset would be FALSE. For example at t=1/100000,d=ell, its formal envelope is3t/2>0, although the empty-mark special case can admit a sharper bound. The argument needs no such uniform zero-loss assertion; it keeps the harmless envelope and the tuple saving.

## Assembly and height order

Cauchy–Schwarz with the actual Gram estimate and the common row ball gives the unscaled tuple bound

    Q^(-1/2) [(Q/Y')P_a^(1/6)]^(1/2) Z^[(M'+s_t(d))/2+epsilon]
       << (X')^(1/2) P_a^(1/12) Z^[s_t(d)/2+epsilon].

The bounded factor involving r_J and fixed q_(b_*) is absorbed into the constant. Norm-twist height on the Gram side is integrated against the Mellin transform of the fixed smooth W_0. Internal reflection/Gram seminorm and polynomial-height orders are fixed BEFORE choosing that external transform order. The same common-density argument handles the completed row; no Z-dependent height constant is introduced.

There are at mostZ^(d+epsilon) rescaled tuples, each with coefficient O(Z^(−3d/2)); also (X')^(1/2)~X^(1/2)Z^(−d/2). Hence the additional subset exponent is

    F_t(d)=−d+s_t(d)/2.

For t<=1/30 and d>=0, s_t(d)<=d/4. Therefore

    F_t(d)<=−7d/8<=0.

This is an exact whole-interval inequality. At d=0 the loss is zero; for nonempty subsets the saving is strictly positive. For each fixed finite slot system, sum its finitely many subsets after allocating local losses. The final exponent is

    l_x/2+(1/8)/12=3/16−t/4,
    C_t(s)=s+l_x/2−1+h_t/6=s−11/16,
    C_t(7/8−t/4)=3/16−t/4.

This verifies the conditional low interface at t=1/100000. The source moments, Gram/correlation proof and exact arithmetic low/high identities are not independently certified. The earlier frozen row count and principal interface remain conditional on their separate inputs. No common-signal theorem can yet be invoked unconditionally.

## Verification and next task

LowEnergy.lean checks the hybrid dichotomy, kernel charge, full reflected real exponent with offsets, exact rescaled identities, universal scale margins, absorbed subset loss and actual real-power inequality. The same pinned mathlib is used; its already-present real-power module cache suffices, with no download or dependency change. Python performs deterministic Fraction tests of feasible abstract dyads and geometry, not certificates of arithmetic tuples or moment estimates. Failed elaboration probes are retained locally, separately from final passing logs.

Next concrete task: reconstruct the nonprincipal shared central-contour interface below7/8 (source5811–6171,6345–6581and15695–15927), including the correction main/error decomposition, buffered zero rectangles, derivatives, retained height orders and normalized exponent. Use actual source capacities and new local Euler bounds, not a claim that a numerical exponent automatically supplies a contour theorem. After those interfaces, the remaining deep scalar/reflection/Gram/moment inputs still require independent certification before even the tiny zero-free refinement can be called proved. Rotate to a specific arithmetic failure or replacement if the shared contour step does not close.
