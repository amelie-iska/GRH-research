# Nonprincipal central-contour interface

## Conditional result and remaining dependencies

The fixed-bin contour transformation and central accounting extend below7/8. They use only the first Euler region D1, not the principal second region D2. In particular they apply at sigma_t=7/8−t/4 for t=1/100000. This is a **conditional analytic interface**, retaining the exact arithmetic high identity, D1 local-factor bounds, buffered detector bounds, external integrated AND trace tails, and pointwise row-count/moment contracts. No new unconditional zero-free theorem or GRH proof is established.

Pinned input: math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob268c4e3206d460c617d3d2129742a72b831b3def at math commit4eaee87548250b2682affda7d05d947c05554bae. Relevant passages: exceptional rows4240–4282; exact high data5554–5640; external tails5660–5800; fixed-bin move5811–5910; aggregate accounting6024–6171; late height closure6520–6581; local full correction8645–8839; simultaneous errors8840–9052; high-bin application15698–15839. These source estimates/identities are explicit inputs, not newly certified by their use here.

The statement needs beta_*>sigma0>=51/100, beta_*<=1, fixed positive l_x,l_y,ell>=0 and h=1−l_x+ell>0. Fix bounded d_min<=d<=d_max with d_min>0 and a retained nonprincipal physical bin at U=Z^d before moving any contour. Retain the same original physical rows, masks, excluded set and probe as in the high identity. The detector's bounded exceptional rows, where some inducing presentation is principal, are excluded; they require separate outer-row treatment. The floor bin a=51/100 is allowed in the contour/accounting result, but is counted directly rather than by a witness theorem. Take T_1=Z^tau>2 with0<tau<=d_min/100 and the retained detector height ceiling; tau is fixed after its internal orders and before N and Z.

For a=bin boundary, delta=2a−1, e in(0,1/1000), z0=17/50, the retained contours remain

    Re s=a+16e, Re w=1−a−6e, Re z=z0.

If the aggregate retained bound for a finite piece/pointwise-set decomposition is

    sum_(u in C)|L^S(w,chi(u)) H^(lambda)_(eta,u,Z)(s,w,z)|
      << U^(R+delta/2+epsilon_c)
         Z^[ell(z0−1/2)+g+epsilon_c](1+T_1)^A,

uniformly over all retained points and labels, with epsilon_c>=0, at most polynomially many logarithmic pointwise sets and bounded R,g, then for any epsilon_d,epsilon_p>0 the ORIGINAL bin integral is bounded by

    Z^[C(sigma0)+sup E_sigma0(d;R,g)
       +(16−6l_y)e+(1+d)epsilon_c+d epsilon_d+epsilon_p] (1+T_1)^A
       + O_(eta,N)(Z^B T_1^(−N)),

where

    C(s)=s+l_x/2−1+h/6,
    E_sigma(d;R,g)=a−sigma+h(z0−1/6)−a l_y−ell/2+g
                       +d(R+delta/2−z0).

The first displayed term bounds the retained central integral; the additional term is kept for the original bin until a later height/tail choice absorbs it. All discarded pieces and horizontal joins are O_(eta,N)(Z^B T_1^(−N)), for each fixed N, with B and the internal height order fixed BEFORE N. This proves no negative value of the supremum by itself. The separate endpoint envelope, outer rows, principal signal and deep arithmetic inputs still need their own evidence.

## The fixed-bin move really stays in D1

D1(epsilon0) is Re s>=51/100, Re z>=17/50, Re w>=−1/100 and Re(s+w)>=1+epsilon0. Start on(s,w,z)=(3,3,2). With the ORIGINAL full holomorphic tuple correction, move z to z0, then s to beta_*+20e, keeping w=3. The reciprocal remains to the right of beta_* by its definition. No improved numerical boundary is used. At beta_*+20e move w to1−a−6e. Since a<=beta_*,

    Re(s+w)>=1+(beta_*−a)+14e>=1+14e.

The numerator of every retained row is entire and nonprincipal. No numerator or zeta pole is crossed;6z0>1. The finite bin is kept fixed throughout.

Now discard the tails of the THREE ORIGINAL height coordinates while the reciprocal is still global. Use the global numerator/deletion and full-correction majorants there. Only then move the retained s segment to a+16e. Every point of this rectangle has

    Re s>=51/100, Re w>=−6e>−1/100, Re(s+w)>=1+10e.

The buffered actual-zero rectangles exclude reciprocal zeros there; the reciprocal argument is s alone. On s-horizontal joins, its buffered height remains valid while the other two axes may be extended using GLOBAL numerator/correction bounds. No w or z join extends an already moved, merely buffered s-axis. Integrated tails alone would not justify those joins: retain the explicit trace-tail contract. Increasing external integration-by-parts order never differentiates the arithmetic row factor.

Neither this path nor its power accounting uses Re s>=7/8. D2 and the principal correction belong to a different deformation and remain governed by the earlier principal-residue report. The threshold51/100 is part of the present detector/Euler machinery, not a new zero-free boundary or a claim that this construction reaches1/2.

## Full correction first, quotients only on the retained region

The correction used for movement is the quotient-free finite tuple sum with selected G_p and unselected H_p. Its holomorphy and all-height majorant permit movement even at zeros of individual P_p or H_p. No piecewise subdivision or quotient is used for continuation.

On the retained dynamic lines, the D1 local estimates give H_p−1=O(Q^(−1−10e)) when p does not divide u and O(Q^(−10e)) when it does. Choose P0(e) large enough to make every selected H_p nonzero there. Only there define B_p=G_p/H_p, and split each slot into main Q_i and error D_i. The full correction then equals H_base product_i(Q_i+D_i). Neither this factorization nor its local divisions supplies a tail estimate or continuation outside the retained region.

For a good selected prime the four error exponents are

    −a−4e, −51/25+12e, 49/25−5a−68e, a−51/25+12e.

For51/100<=a<=1 and0<e<=1/1000 they are all at most−51/100. The identity-ray restriction fixes the ray phases but does not set eta(p)=1. Original zeros at primes dividing the row remain zeros. The already bounded ramified terms have exponents at most−1/2 after normalizing Q^z. The potentially larger strict ramified term occurs only for row valuation j_p>=2.

For the primitive inducing numerator character, the source's local conductor description implies ONE simultaneous bound, for the distinct strict labels J0,

    q_f <<_S q_u product_(p in J0) Q_p^(−(j_p−1)).

With w_r=1−a−6e and A*=1/2−w_r=a−1/2+6e>=0, the functional equation and buffered reflected numerator cost q_f^A* times a fixed polynomial height and small row power. For every strict label,

    −w_r−(j_p−1)A*=−1/2−(j_p−2)A*<=−1/2.

Allocate these excess valuations simultaneously before summing labels. Paying the numerator bound separately per slot would invalidate the stated exponent. Distinct slot supports prevent reusing a label. Divisor-many ramified choices cost a small row power; good-prime errors have the stronger51/100 exponent. This yields the central joint numerator/error estimate with zero amplitude assigned to every error slot. The arithmetic conductor identification, functional equation and buffered bounds remain explicit inputs; Lean verifies the actual real-power spending inequality, not those arithmetic assertions.

Main slots have Qmain_i=−P_i^(z−1/2)Q_i and |Q_i|<=P_i^(g_i+vartheta). Thus the total main amplitude is sum_i ell_i g_i=q ell, including assigned zeros at error slots. This is a base-Z exponent g=q ell, NOT d q ell. Multiplying by the pointwise row cardinality gives the aggregate hypothesis above. Derivatives used for fixed internal profiles insert only the allowed logarithmic weights; the external tail order is selected later and cannot change that internal order.

## One cumulative height allowance and one original integral

List each external coordinate once. If a buffered argument is gamma_j+sum_k a_jk v_k, choose c_k=1/[2m(1+max_j|a_jk|)] and retain |v_k|<=c_k T_1. Then sum_k|a_jk v_k|<=T_1/2 for every argument. Since |gamma_j|<=(3i+1)T_1, the argument lies within(3i+3/2)T_1, leaving a fixed half-T_1 reserve in the(3i+2)T_1 buffer. Fixed bounded shifts fit after increasing the threshold. This allowance is not renewed at successive witness, prime or row estimates.

Internal coefficient measures known only at a fixed weighted L1 order stay integrated inside the arithmetic factor. Such a measure is not thereby a pointwise rapidly decaying external trace density. Extra integrals used in a central estimate must be included in its FULL left-side bound; discarded pieces must remain on global or absolute lines and be bounded before asserting it. These requirements are part of the retained source contracts, not consequences of numerical geometry.

Pointwise amplitude and witness sets can vary with the contour point. At each point apply triangle and the aggregate inequalities, dominate their bounded exponents by one supremum and the count by a fixed logarithmic multiplicity, and integrate only the original analytic bin sum. No separate integrability or measurability of the pointwise partition labels is needed. The new Lean Bochner-integral theorem bounds that original integrable complex function by an integrable scalar kernel. It does not formalize the contour deformation or assert an arithmetic majorant without proof.

## Exact normalization and perturbation

Before the row bound, the outside real power is

    l_x(1/2−z0)+a+z0−1−a l_y−d z0+(16−6l_y)e.

Adding the row power and subtracting C(sigma0) gives the displayed E_sigma and losses exactly. Also

    E_sigma(d;R,g)−(beta_*−sigma)=E_beta_*(d;R,g).

For the perturbed geometry, frozen algebraic values delta,q,R and fixed d,

    E_t(d)=E_0(d)+t(13/50+delta/4+q).

At the moving upper endpoint h_t=h0+3t/2 this becomes

    E_t(h_t)=E_0(h0)+t(−1/4+delta+q+3R/2).

These identities do not identify the actual pointwise row sets for two different probes, or certify the negative endpoint envelope. They verify the exponent that must be estimated. After a positive common saving m is independently established, choose a target-dependent positive height exponent tau within the detector ceiling and m/[4(A+1)]. Then choose N so B−N tau<C(beta_*)−m/2. Both choices occur after fixed internal orders and before Z; the exponent m remains common, not target-dependent. Lean verifies these existential real/Nat choices.

## Verification and next research claim

CentralContour.lean verifies retained-rectangle geometry, the actual finite summed height budget and buffer inclusion, strict and simultaneous real-power conductor spending, normalized central powers, reference/perturbation identities, an actual Bochner-integral envelope, and late height/tail choices. All assumptions are visible. Arithmetic high identity, D1 local-factor derivation, conductor identification, buffered detector estimates, trace tails and row moments remain inherited inputs. Python uses exact deterministic rational geometry and exponent checks, not L-function samples or a proof of any mean square.

Result: no additional7/8 wall is present in the conditional nonprincipal central interface. The low, principal, counting and central applications are now reconstructed separately; the deep source assertions and remaining outer-row/final closure estimates are not collectively certified. Next change direction from interface bookkeeping to an arithmetic input: independently audit the prime-power Fourier and common-factor finite correlation identities in source7055–7330, which feed the Gram estimate, with all zero extensions, phase factors and repeated prime powers. Seek a proof or an exact counterexample before adding another conditional global theorem. Keep the outer-row/final assembly obligations explicit and do not call the tiny refinement or GRH proved.
