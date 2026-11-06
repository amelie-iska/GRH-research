# Actual full-A_U pure discrete top-prefix estimate

Research-only candidate v3, 6 November 2026 (v1/v2 preserved; opened B_U and literal prefix/long raw-mask factors are explicit). This is a NEW proof for the original full coefficient, using all short and Heath--Brown factors in ONE scale partition before any short-factor triangle. It does not replay the finished A_U-to-A_Y tail, residual-only TypeII, large-k, large-common-divisor or whole-prefix-localization experiments. Independent file-bound review is required before acceptance. The public333-page edition remains unchanged.

## 1. Exact object, hypotheses and external inputs

Let K=Q(omega), O=Z[omega]. "Good" means prime to the ORIGINAL fixed S (containing primes above2,3). All sums count IDEALS, not rational squarefree integers or one representative per norm. Use the unique multiplicative primary generator1mod3. Fix finite-order nu, original finite source/ray/literal-unit data, u0 with no good prime support, and ONE complex smooth W supported[1,2], with zero endpoints. Put B=sup|W|, M(W)=(2pi)^-1 integral_R |What(it)|dt, and V1(W)=B+integral|W'|. Constants may depend on these fixed character/source data and explicit profile seminorms; there is no all-conductor or varying-profile supnorm assertion.

Take D>=2^64, 1<=U<=sqrtD, original UNWEIGHTED PURE two-pivot rows A2=1, other good factors unit, and A1 comparable to H=D^(3/4). Keep the ORIGINAL exact capacity a_cap,b_cap, nodal G, pre-S finite Kcut=sqrt(b_cap), every original e/w primitive value, all rho components, and every raw zero. If b_cap<a_cap the piece is EXACTLY0.

The precise finite primitive-dual object P_X[A_U,A_U] and its j0 model L_X^K[A_U,A_U] are DIRECT_DISCRETE_TOP_CUTOFF-v2, equations(1.1),(2.1),(2.2), SHA4b42c00601073bb6f178daf862c244c8b096b4c17a7aaf66d00caf13f4dd498a. Here X=D^(3/8)>=64 and V=X^(1/6)/2=.5D^(1/16). The exact support is
 T_X={(w,s):w integral,Nw<64; s good integral; V<Ns<=2V; Nw(Ns)^6<=X}.
There is NO SF requirement on s, no inserted (k,s),(k,w),(w,s) condition, and no density g or principal-rho projection. All S-supported/nonunit w and all original rho means remain. P_X already includes the original1/D ONCE; the unnormalized numerator is D*P_X. Optional ORIGINAL Nm!=Nn is treated separately below, preserving conjugate ideals/equal-norm fibres.

Inputs are the existing exact J5 Heath--Brown identity, physical n3 cubic matrix bound Theta3(P,L)=P+L+(PL)^(2/3), exact Gauss CRT, full source/finite-S product-selector expansion, and DIRECT-v2 real Bessel error. These are pinned external/proved inputs, not new Lean or new sieve reproofs.

The NEW ramified source interface used here is the lane-C governing v2 605478df... WITH required coefficient addendum b601afb6..., lane-B explicit known27-cusp norm8231e155... WITH actual-a_j convention3da658fd..., and lane-A actual finite-family c70805fa... WITH REQUIRED rho precision1b154731.... It proves, for the ACTUAL fixed finite family and BOTH conjugate orientations,
 |F_psi(T;t;1,I)| <<_fixed,eps V1(W)(2+T Nt)^eps
                     min(sqrtT,T^(1/4)(Nt)^(3/8)).       (1)
Here t is any physical good SF frequency, I any exact interval in[T,2T], T>=1. Its literal unit rule extends it to T in[1/2,1); T<=1/2 is empty including W(2)=0. This is uniform over physical levels; no level<sqrt(T) premise is imported. The coarse dual cost is R^(3/2+eps), NOT the refined sqrtR claim.

Only exactly one own-column vartheta with angular order+1/-1 varies after absorbing the arithmetic mu into B_U=mu*A_U. Jacobi rho=mu*vartheta is NOT finite order. All remaining fixed finite residue factors, including higher3-primary nu and source/ray/Gamma/primitivee/w selectors, are handled by their FULL finite product expansions. Genuine common/prefix rho and root phases are retained as actual scalars; nothing is set to1 or centered. Growing n,k,s,w masks are literal, not put into the fixed conductor of kappa. No arbitrary bounded multiplicative function is asserted to satisfy(1).

## 2. Exact all-eleven-factor grouping of the ORIGINAL coefficient

For actual contributing good SF m with D<Nm<2D and1<=U<=sqrtD, the endpoint-exact original identity is
 B_U(m)=mu(m)A_U(m)=sum_(a*b*c=m,Na,Nb<=U)mu(c).          (2)
Here B_U is the OPENED coefficient mu*A_U, NOT the project's different original C_U. Historical helper notes that call the opened coefficient C_Y must be read only in their own explicit definition; they do not identify it with original C_U. This identity is asserted on the contributing annulus (Nm>U); it is not an identity for arbitrary small m, including the unit. Zero profile endpoints cause no added term. There is NO extra -mu. Apply the accepted EXACT J=5 finite HB identity to mu(c), valid on Nc<=2D with short-mu cutoff z0=(2D)^(1/5). Its j-th term has j short mu-factors and j-1 unrestricted coefficient1 factors, with the actual fixed binomial/sign. Including a,b gives at most2j+1<=11 factors. j=1 and all literal unit factors are retained.

Partition each factor into independent norm dyads [M_i,2M_i), with its own U/z0 endpoint cutoff. Choose TypeI/II from these SCALES only, never by a new product-dependent stopping rule. For any box meeting D<Nm<2D, with nfac<=11,
 D/2^11 <= Pbox=product M_i <=2D.                       (3)
Zero profile endpoints do not matter.

Elementary scale lemma: if no M_i>Pbox^(2/3), either one M_i lies in[Pbox^(1/3),Pbox^(2/3)], or all M_i<Pbox^(1/3) and greedily multiplying until first crossing Pbox^(1/3) lands below Pbox^(2/3). Thus there is a balanced subset. If no balanced subset exists, a unique M_i>Pbox^(2/3) exists and the product of the remaining scales is<Pbox^(1/3). Uniqueness follows since two such scales would have product>Pbox while all remaining scales>=1.

At D>=2^64, Pbox^(2/3)>=D^(2/3)/2^(22/3)>sqrtD. Therefore neither original short factor a,b can be that unique long factor. Nor can a truncated mu-factor, whose norm is at most(2D)^(1/5). The unique long factor v is consequently an UNRESTRICTED coefficient1 HB factor. The product p of ALL other actual factors obeys
                         Np << D^(1/3).               (4)
Indeed it is at most2^10 Pbox^(1/3). If j=1, no unrestricted factor exists, so its boxes are automatically balanced. Nothing is dropped as an allegedly empty j1 term.

For each box and long-index choice define H_p as the complete signed sum of assignments of all factors except v. Original a,b restrictions, all short-mu cutoffs, own dyad endpoints and HB signs remain in H_p; it depends on p only. On SFp its pointwise bound is
                     |H_p| <<_eps D^eps,               (5)
because the number of at-most-eleven-factor assignments is <=11^omega(p) times a fixed HB coefficient. There is no separate U/Y count. This is divisor counting, not cancellation or coefficient shrinkage. The number of dyadic/HB choices is a fixed power of logD, absorbed AFTER estimating their exact components.

## 3. Balanced WHOLE-factor boxes

Group a balanced subset into u and the remainder into v BEFORE any a,b triangle. Both physical SF macroindices have norm scales between fixed multiples of D^(1/3) and D^(2/3), with product comparable to D. Their own assignment coefficients obey(5); all internal SF restrictions are automatic from SFu,SFv, and the remaining cross-coprimality is encoded by the RAW cubic matrix entry.

Exact cubic CRT gives the same physical cubic matrix with the actual Gauss roots and arbitrary bounded coefficient diagonals. Every fixed other-column/numerator/deletion factor is multiplicative here and splits on u,v; full finite selectors have already been expanded with their total masses. Thus the physical norm, Mellin inversion of the SAME W, and the normalized l2 coefficients give the LINEAR bound
                        M(W) D^(1/3+eps).             (6)
There is NO old Y^(1/3) or U cost: both original short factors are inside this single balanced partition. Broad group dyads cost only fixed constants; original own-factor interval cutoffs stay in macrocoefficients. If equivalent bookkeeping introduces row intervals, the accepted logarithmic interval-Schur bound applies with full norm fibres, not a claimed norm1 contraction.

This step can use arbitrary bounded multiplicative coefficient diagonals. The sharp mean(1) below cannot: it uses the actual finite-family phase list only.

## 4. TypeI with a large COMPLETE prefix

For a box with the long coefficient1 variable v and whole prefix p, split assignments by Np>Z or Np<=Z, for real Z>=1. This selection is on the auxiliary expansion assignments, not a new primal row filter; norm ties are retained. On Np~P, Nv~D/P, exact CRT and(5) give normalized l2 masses D^eps and O(1). The physical cubic norm yields
 M(W)D^eps sqrt(P+D/P+D^(2/3)).
By(4), sqrtP<<D^(1/6), and on the clipped tail P>Z/2. Summing the finite dyads gives
 |C_TypeI,>Z| << M(W)D^eps [D^(1/3)+sqrt(D/Z)].          (7)
All actual fixed/growing coefficient diagonals and raw zeros remain. No new numerical tail experiment or finished localization is reused as a new result; the NEW domain here has original a,b<=U, grouped with ALL other factors at the outset.

## 5. Small COMPLETE prefix: freeze the original other column FIRST

For each original n in its COMPLETE annulus, and each exact k,e,w,s/source/rho component, freeze n BEFORE the left TypeI estimate. Do NOT open a common long divisor d. The original pair mask is EXACTLY
 1_((p*v,n)=1)=1_((p,n)=1)*1_((v,n)=1).
Keep the FIRST factor explicitly in the actual p coefficient, together with every original prefix/k/s/w or fixed-numerator raw zero and prefix phase. Thus the actual coefficient is H_p times these bounded outer factors (including1_((p,k)=1)); H_p itself remains the intrinsic assignment coefficient defined in Section2. No fixed original n enters kappa. At a forbidden prefix the entire term remains zero. The remaining LONG-variable raw zeros are retained through
                         Q=rad_good(p*n*k*s*w).         (8)
The condition(v,Q)=1 alone is NOT a substitute for the prefix mask(p,n)=1. Analogous original n/k/s/w scalar zeros remain outside. This factorization precedes every positive estimate; the coefficient bound(5) survives because each outer factor has modulus at most1.
Fixed exclusions remain in psi. On a nonzero actual branch p,k are goodSF and coprime by the original eta(k)^2 raw zero. The physical moving frequency is t=p*k. No k/s/w coprimality is inserted.

Open the full deletion(v,Q)=1 by exact Mobius inclusion-exclusion with h|Q. The surviving raw cubic factor forces(h,t)=1. Each h contribution has the literal outer1/sqrt(Nh), length T'=D/(Np Nh), and frequency p*k*h. Original n primes appear in Q, even when they occur in other parameters. They are not replaced by a conductor radical or omitted as redundant. The identity
                          T' N(pkh)=D Nk              (9)
is exact. h may be as large as the support permits: the uniform all-level form of(1), including the unit/empty fallback, is required.

INCLUDE the original prefix weight1/sqrt(Np). The bound is
 (Np)^(-1/2)(Nh)^(-1/2)
 (D/(Np Nh))^(1/4) N(pkh)^(3/8)
 =D^(1/4)(Nk)^(3/8)(Np)^(-3/8)(Nh)^(-3/8).             (10)
Omitting the first factor would give the WRONG prefix exponent+1/8. Its presence is essential.

By elementary ideal counting,
 sum_(h|Q)(Nh)^(-3/8) <=tau(Q)<<_eps(NQ)^eps,
 sum_(p goodSF,Np<=Z)(Np)^(-3/8+eps)<<Z^(5/8+eps).
On support Nn<=2D,Ns<=2V,Nw<64,
                         NQ << D Z V Nk.              (11)
The full raw fixed exclusions only add a fixed multiplier. Allocate epsilon separately to each polynomial material factor and Nk; no upper-polynomial restriction on Kcut is required. With(5),(9)-(11), the one-column small-prefix bound is
 |C_TypeI,<=Z| << V1(W)(DXA1)^eps
                     D^(1/4)(Nk)^(3/8+eps) Z^(5/8).    (12)
A finite source/ray Fourier term is an auxiliary coefficient extension; the FULL finite sum reconstructs original primitive zeros. No forbidden local class is individually relabelled a genuine original row.

## 6. Actual once-normalized top-prefix assembly

For each fixed n the entire left column is the sum of the EXACT balanced and two TypeI pieces, so(6),(7),(12) apply directly to B_U, not to an A_Y proxy. The other original column, with its true A_U and all raw phases, has elementary l1 bound B D^(1/2+eps). Taking this triangle AFTER the left bound does not discard orientation means before proving the left estimate.

The original leading-model normalization is A1/D ONCE. The s family is the actual finite set T_X and has O(V) terms for each fixed w<64; rho(s)^6 is retained, with no ray-density approximation or principal projection. The fixed e/w/source/rho/selector masses remain explicit fixed constants. |g0| is bounded by the accepted0<=G<=1/support bounds and may be0; it is never divided out.

The identity still uses the ORIGINAL finite sum Nk<=Kcut. Only its positive bound is majorized by
 sum_(k SFgood,Nk<=Kcut)(Nk)^(-13/8+eps)
                      <=zeta_K(13/8-eps)<infinity,     (13)
after allocating eps<5/8. Balanced/large-prefix terms use the still easier Nk^-2 majorant. This is no Euler completion of the model and no mu(k) cancellation.

Set Z=D^(2/9). Then
 sqrt(D/Z)=D^(7/18)=D^(1/4)Z^(5/8),                    (14)
and balanced D^(1/3) is smaller. Consequently
 |L_X^K[A_U,A_U]| <<_fixed,eps
 B[M(W)+V1(W)](DXA1)^eps A1 V D^(-1/9)
       +O(B^2 A1V D^(-1+eps))                          (15)
if the optional original unequal-norm projection is imposed. For that projection subtract exactly the fixed-n norm fibre, with O(D^eps) ideal coordinates, actual bounded Gauss phases and true divisor-bounded coefficient. The total normalized fibre cost is the displayed O(B^2 A1V D^-1+eps); conjugate ideals remain distinct. No radial orthogonality or unrelated equal-norm block is invoked.

Use ONLY DIRECT-v2(2.3) with the ORIGINAL coefficients A_U,A_U:
 |P_X[A_U,A_U]-L_X^K[A_U,A_U]|
            << B^2(DX)^eps A1V Lambda, Lambda=A1X/D^2. (16)
There is NO A_U-to-A_Y error in this new argument. Combining(15),(16) proves the scoped bound
 |P_X[A_U,A_U]| <<_fixed,eps (DXA1)^eps A1V
 { B[M(W)+V1(W)]D^(-1/9)+B^2[Lambda+D^-1] }.            (17)

At A1~D^(3/4),X=D^(3/8),V=.5D^(1/16), A1V~D^(13/16). The normalized leading power is
 13/16-1/9 =101/144 <3/4, margin7/144.                  (18)
The balanced power is31/48, Bessel power-1/16 and equal-norm correction-3/16, all smaller. Subpower notation(DXA1)^eps is conventional; for any requested D^delta first allocate eps/delta among the polynomial factors. This is a target-sized result for the DECLARED representation-fixed pure finite primitive-dual TOP PREFIX only.

## 7. Scope, unfinished work and acceptance

The proof keeps actual A_U for every1<=U<=sqrtD, full original annular ideal columns, all orientations/means/equal-norm fibres, all original rho, inverse-different/source/Jacobi phases, full finite-S product selectors, primitivee/w zeros, fixed nu/S/W, all original ray/capacity endpoints, arbitrary original finiteK and legal k/s/w overlap. Its quantitative dependencies include fixed finite-character conductors and W seminorms. No hidden positivity/GRH/Artin-holomorphy/zero-location premise is used.

The old routes remain preserved and finished. The NEW step is the whole-eleven-factor scale partition of the ORIGINAL coefficient plus the now constructed ramified sharp one-row theorem, with direct freezing of the original opposite column and fullQ. No large-k/common-d/tail/scalar/control rerun is needed.

This does NOT bound the full infinite dual-frequency complement, all pure sectors, mixed/neighboring two-pivot blocks, short/principal assembly or a weighted-row operator. Whole signed13/12/global unsigned9/8 stay current. Determinant positivity, zero-location comparisons, separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes, actual analytic/categoryLean and GRH remain OPEN. No proof schedule is promised.

Acceptance requires independent review of(2)-(18), the exact phase/finite-family/source match and new sharp interface, root source/hash closure, and fresh focused exact classification/exponent checks for THIS new grouping. Such finite checks are not actual-family energy data or full Lean. All project edits/checks SSH-Linux; no canonical scientific build, index/release/publication/dependency/auth/MCP/Lean action.
