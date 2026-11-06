# Equal-norm coherent off-diagonal columns: arithmetic localization and the failed angular route

New research-only lane, 6 November 2026. The surviving result is an elementary ORIGINAL-FAMILY sector theorem: equal-norm good squarefree COPRIME columns are conjugate split-prime orientations, so their FULL PRIMAL signed sector is already target-sized. Its exact full-orientation product is retained, not replaced by a variance or a zero mean. A direct all-component Poisson prefix estimate is also proved for this sparse sector. No fixed-field oscillatory estimate for the remaining UNEQUAL-norm coherent band has been found. This is not a new counting theorem, root law, sieve or GRH result, and no finished norm/root/control route is replayed as progress.

Read-after input: planning/intermediate-kernel-20261106/HANDOFF-v1.md SHA bb9463e074d822f68cc652ad20d255052536fd7c651febe6fb9a6d9bd2133e74; governing aggregate5470159d31d46bf5ce42fc52fcae4dc4013dc662b054f115f27fcc937ff62d63 and RUN_CLOSED66473a6f15d44c69c53c6aeed9df89c62f752286624c7dd0c5e86fb5fd3c7c4e. Current master instructions and all original masks/scope safeguards remain. Public303-page/9172MathML release and whole signed13/12/global9/8 are unchanged.

## 1. Exact objects and the equal-norm sector

Let O=Z[omega], omega^2+omega+1=0, Im(omega)>0. Let S be the original FIXED deleted prime-ideal set. We do not require S to be closed under conjugation and do not enlarge it. Original columns m are all good squarefree IDEALS in D<=Nm<=2D, D>1, with

 c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
 A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b).

The complete original cutoff U is unchanged. Nu and S are fixed as in the original family, and nu is unitary on good ideals. There is ONE common possibly complex W, B_W=||W||infinity. Rational-norm-squarefree is NOT a restriction on the complete original annulus.

Let R_actual be the actual UNWEIGHTED two-pivot row set, with v3=...=v6=O, fixed literal integral unit/S-supported u0 without good-prime support, literal primary generators alpha(v), original good SF/coprime v1,v2, original ray restrictions, A1<=Nv1<2A1, A2<=Nv2<2A2 and exact Nu0 Nv1 Nv2^2<=H. A1,A2>=1. Write R_w=#R_actual and R=A1A2. Empty blocks are zero. No weighted-operator extension or sum over all varying u0 is made.

Define the ORIGINAL raw h=1 A--A numerator's equal-norm off-diagonal part by

 D S_eq =sum_{(v1,v2) in R_actual}
     sum_{m,n good SF,(m,n)=1,Nm=Nn in[D,2D]}
        c_m bar c_n R_m(v1 v2^2)bar R_n(v1 v2^2).             (1)

All common-prime/full-union zeros are literal raw zeros. Since D>1 and (m,n)=1, this has NO coefficient diagonal m=n. It is an equal-NORM OFF-DIAGONAL sector of the indefinite coprime form, not a positive Gram diagonal. Put S_neq=S1AA-S_eq with the exact complementary Nm!=Nn restriction. These are primal algebraic definitions before any source-class/rho decomposition or Poisson transformation.

## 2. Complete classification by ideal prime valuations

Claim: good SF coprime m,n with Nm=Nn=N>1 satisfy

 n=bar m,
 N is rational-squarefree and supported on split rational primes p,
 m contains exactly one of pi_p,bar pi_p above every p|N.      (2)

Both primes above each such p must avoid the ORIGINAL S. Conversely each such orientation gives an ordered coprime pair(m,bar m) with equal norm. This condition is imposed ONLY by the equal-norm coprime sector; rational-nonsquarefree norm ideals remain in the full original annulus and are not discarded elsewhere.

Proof: factor the common rational integer N prime by prime. At an inert rational p there is only one prime ideal P=(p) of norm p^2. Squarefreeness makes its ideal valuations0 or1, and equality of norms forces the SAME valuation on both sides. Coprimality then forces both0. The same argument excludes a ramified prime, with its unique norm-p prime ideal.

At a split p, write valuations of m at pi,bar pi as x,y in{0,1}, and those of n as z,w in{0,1}. Norm equality gives x+y=z+w, while coprimality gives xz=yw=0. Sum0 means all0. Sum2 would put both primes on both sides and is forbidden. Sum1 forces the two sides to choose opposite prime ideals. This proves(2) and its converse at every rational prime. Unique ideal factorization completes the proof.

If S is not conjugation-stable, a p with either prime in S cannot occur in this sector: one member of the conjugate pair would violate the EXISTING good condition. This is a consequence of the original two-column masks, not an enlargement of S. At every admissible N, ALL2^omega(N) orientations remain in the complete norm fibre; their ordered pairs are counted once each, including both reversals, with no factor1/2.

In particular each eligible m has at most ONE partner n. Elementary ideal counting therefore gives

 #ordered equal-norm coprime annular pairs
       <=#{m integral:Nm<=2D}<<_K D.                       (3)

One may use the already accepted A_K(x)<=2x to make the right side4D. This is much thinner than the O(D^2) unrestricted pair set and needs no angular cancellation.

## 3. FULL primal sector theorem and exact localization

For every epsilon>0,

 |S_eq| <<_(K,nu,S,epsilon) B_W^2 R_w D^epsilon
          << B_W^2 R(DH)^epsilon.                         (4)

Proof: the ternary bound |A_U(m)|<=3^omega(m)<<_epsilon D^epsilon is uniform in the original U. Apply it with a sufficiently small preliminary epsilon so that the PRODUCT of two coefficients costs D^epsilon. Every fixed nu/raw symbol has magnitude at most1, and |W_m bar W_n|<=B_W^2. For EACH actual row there are O(D) eligible ordered pairs by(3). Taking the absolute triangle only in this sparse sector and dividing ONCE by the original D proves the first bound. It does not assume positivity or replace a signed mean by a marginal variance.

The original sharp/SF/coprime/ray/capacity masks only select rows from the O(A1A2) dyadic product, so R_w<<R. A nonempty block satisfies Nu0 A1A2^2<=H, hence R<=H/(Nu0 A2)<=H. Thus (4) is already target-sized for this sector. No profile derivative is used, and no D-dependent fixed-seminorm premise is silently added.

Consequently, for EACH FIXED common W, the full scoped h=1 target

 S1AA=O_(nu,S,W,epsilon)(H(DH)^epsilon)

is equivalent, up to the proved supremum-norm-controlled elementary sector term, to S_neq=O_(nu,S,W,epsilon)(H(DH)^epsilon). The desired full/unequal-norm constants may depend on fixed W or on appropriate explicitly declared profile seminorms; no uniform full-target assertion over varying profiles with only B_W control is made. This is a useful ORIGINAL-FAMILY localization, not a new whole-slice bound. It does not remove unequal-norm orientation means, other gcd sectors, principal/residue/short assembly or varying-u0 obligations. Nor does it assert a lower bound for S_neq: the original coprime form remains indefinite.

## 4. Raw norm induction and the complete orientation mean

The literal positive sextic symbol satisfies, for every alpha in O,

 chi_bar m(alpha)=bar chi_m(bar alpha),
 chi_m(alpha)bar chi_bar m(alpha)
       =chi_m(alpha bar alpha)=chi_m(N(alpha)).             (5)

Proof at a prime ideal: conjugate the defining residue-field equality for the unique value in mu_6. Conjugation takes both the ideal and the root of unity to their conjugates. The relation then extends multiplicatively over the squarefree ideal factors. At collisions both sides of the product equality are ZERO: for split m as in(2), a rational p|N divides N(alpha) exactly when alpha meets at least one of pi_p,bar pi_p. Therefore(5) retains the full original union mask; no zero is restored. A unit multiplying alpha has norm1, so the product is independent of literal generator section without averaging units.

For an eligible m of norm N, restriction to rational integers defines

 psi_m(t)=chi_m(t), a primitive Dirichlet character modulo N.

Indeed Z/NZ -> O/m is a ring isomorphism, prime by prime since exactly one prime of norm p is chosen above each rational p|N. The local residue character has EXACT order6, so the Dirichlet conductor is N, not a smaller claimed radical. Equation(5) says the original paired row character is the norm pullback psi_m(N(alpha)). Its Hecke conductor is (N)=m*bar m: at a split p both local norm factors have the same nontrivial primitive character, and no other finite prime ramifies. Its infinity type is trivial. This is an exact primal structural description, not an assertion that arbitrary class/rho Poisson prefix transforms share one frequency grid.

Fix once one prime pi_p above every admissible split p and define

 chi_p(t)=(t/pi_p)_6,
 a_p=nu(pi_p)bar nu(bar pi_p), |a_p|=1,
 t=Nu0 Nv1 Nv2^2.

For every allowed ORIGINAL row (including all its literal/ray/capacity restrictions), the COMPLETE ordered norm-N fibre in(1) is EXACTLY

 a_U(N)^2 |W(N/D)|^2
       *product_{p|N}[a_p chi_p(t)+bar(a_p chi_p(t))],        (6)

where

 a_U(N)=sum_{rs|N,(r,s)=1,r,s<=U}mu_Z(r)mu_Z(s).             (7)

Here r,s in(7) are rational positive divisors, not rescaled ideal cutoffs. Divisor norms and ideal-Mobius signs of an orientation m are exactly the subset products of the distinct rational primes p|N, so A_U(m)=a_U(N) for EVERY orientation. The single common complex W is essential to the exact factor |W|^2; it has not been replaced by a different orientation weight.

To prove(6), write the original literal u=u0 alpha(v1)alpha(v2)^2, so N(u)=t. At each p the m-orientation pi_p contributes a_p chi_p(t); the opposite orientation contributes its complex conjugate. Multiplicativity and expansion of the product give ALL2^omega(N) choices for m, with n=bar m uniquely. This is the ORDERED original sum, not half that sum. Every source class is included; there is no restriction to a convenient same-class component. Original row-ray projectors remain outside the pointwise identity as part of the actual row set.

There is NO automatic zero and NO positivity theorem for(6). For nu=1 and gcd(N,t)=1, every local character factor2Re chi_p(t) lies in{2,1,-1,-2}, so the character product is a nonzero real integer. A raw collision instead makes it0. This is a pointwise statement about the orientation factor, not a lower bound for the coefficient fibre (a_U or W may vanish), not a global signed-energy lower bound, and not an impossibility theorem for cancellation between N or rows. For general nu, local real factors can also vanish. Products can have either sign even when nu=1.

## 5. Exact all-component dual prefix bound for this thin sector

Let P_eq(<=Y) denote the same representation-fixed primitive-Poisson numerator as in accepted v8 and intermediate handoff, restricted FIRST to the equal-norm coprime pairs in(1), with ALL original source classes/rho, ALL S-supported dual modes, exact finite K_ell, all e/ell/v2 signs and masks, and Ny<=Y. No completed Euler factor or primitive-conductor zero restoration is made. This definition is valid by linearity of the exact finite primal pair identity; it does not require a selected-pair positive sieve.

For every finite Y>=1,

 |P_eq(<=Y)|/D,
 |P_eq((Y,2Y])|/D
    <<_(fixed data,epsilon) B_W^2(DYA2)^epsilon R*Y/D.        (8)

Proof: each primitive class/rho term has actual conductor f_S*m*n, with F_S=Nf_S>=1. On this sector its norm is F_S*N^2>=D^2, and eta is nonprincipal because the original good ramified column supports are disjoint and nonempty. Its exact field kernel is

 dotG(X)=C0^(-1/2)integral G(u)J0(2sqrt(Xu/C0))du,
 C0=3/(4pi^2), 0<=G<=1, suppG subset[1/2,5/2].

The angular integral representation gives |J0(real)|<=1, so |dotG(X)|<=2C0^(-1/2) uniformly in X>0, with NO derivative cost. This bound uses the actual auxiliary capacity G, not W. The exact Poisson amplitude obeys

 L_e/sqrt(F)<=A1/[(Nk)^2 Nell Ne D].

Count ALL integral dual ideals once: A_K(Y)<<Y for a prefix, and A_K(2Y)<<Y for a band. This keeps every S-supported ideal and all raw primitive zeros, whose absolute values only suppress terms. No independent flat S-volume factor is introduced.

Use O(D) ordered column pairs from(3), coefficient product O_epsilon(B_W^2D^epsilon), and the primitive root's modulus1 at its ACTUAL conductor. No root gauge or root-phase cancellation is required. The ORIGINAL finite k sum has positive majorant sum(Nk)^(-2)<infinity; its signed cutoff is not changed to an Euler factor. The finite S e sum is fixed. The active ell divisor sum is at most tau(v2); summing actual v2 costs A2 with its standard subpower divisor loss. Finite source-class/rho Fourier coefficients cost only the fixed original ray/family constant, with all primitive sigma(e/h) zeros left intact in the identity. Combining these factors and dividing ONCE by the original D gives(8).

This direct sparse-sector estimate uses neither the finished Phi norm theorem nor any fictitious equality of residual classes. It is a different elementary pair-count mechanism. Its bound for the WHOLE primal sector is (4), not the growing prefix expression(8).

## 6. Complementary dual sector and critical ranges

For fixed parameters the accepted smooth primitive Poisson identity and its rapidly decaying transform give the EXACT equality

 D S_eq=P_eq(<=Y)+P_eq(>Y).

The full sum is valid at fixed parameters with its actual (possibly large) G derivatives. No uniform derivative bound is inferred. Equations(4),(8) therefore imply

 |P_eq(>Y)|/D
   << B_W^2[D^epsilon R_w+(DYA2)^epsilon R*Y/D].             (9)

This is a signed complement identity and triangle, not a positivity assertion that the whole bound controls every window. In particular when R*Y/D<=H with polynomially bounded parameters, BOTH prefix and whole equal-norm complement are target-sized. At H~D^(3/4), this includes pure R~H with Y~D, and mixed R~D^(7/12) with Y~D^(7/6), up to the original feasible fixed capacity constants. The new mixed equal-norm window lies beyond normD, but it controls ONLY this thin sector. Equal-norm annular pieces at arbitrary larger Y still have only(8); a bound on the whole sector alone does not bound every arbitrary representation window because windows may cancel.

No additional high-tail cutoff has been proved, and none is needed for the whole-primal equal-norm statement. The potentially difficult unequal-norm band and its coherent intermediate complement remain the genuinely unestimated part.

## 7. Why the proposed fixed-angular cancellation does not close the remaining route

The attempted step was to recombine all source classes/rho, regard the actual root/orientation factor as one fixed nontrivial angular Hecke character, and apply fixed-field cancellation before positive Cauchy. The exact structure shows why that inference is unavailable.

Already on equal-norm pairs the original raw character is the norm-induced psi_m(Nu), with VARIABLE rational conductor N~D and trivial angular infinity type. On an unprojected complete norm fibre of the dual ideal, its character value depends only on the norm, so angular orientations are coherent, not a source of a nontrivial angular phase. The full pointwise orientation mean is(6), not zero. Fixed row-ray restrictions may be expanded into finitely many S twists; they must retain their own primitive S conductors and transform scales, not be treated as one common truncated frequency lattice. None of that turns the variable conductor N into a fixed Hecke character.

The prescribed coefficient a_U(N)^2 has its original two cutoff constraints, and for unequal norms there is no common norm fibre with a product like(6). Root factors and actual primal characters still vary with BOTH original columns and the actual row. A fixed-field prime/ideal theorem for ONE fixed angular character does not supply the required uniform coupled average over those varying conductors, especially with the original AU/full-union/common-prime/ray/SF/capacity masks and one common W retained. We have not proved such an averaged estimate, nor substituted an assumed scalar power-Mertens or zero-free strip.

This does not rule out genuine cancellation across norms, rows, class/rho components or the prescribed root-weighted dual variables. It records the exact failed fixed-angular reduction. The actual new surviving theorem is(2)--(9): equal-norm OFF-DIAGONAL means are retained and bounded by sparse arithmetic, and the remaining full scoped h=1 target can be localized to unequal norms. No finished norm-gauge/root-identity or finite-table audit is being presented as that missing oscillatory theorem.

## 8. Novelty and protected scope

A focused search of317 named project mathematical source/note files found no prior version of this complete equal-norm classification/full-sector target bound; the old selected-q variance example is a different statement and was not rerun. This is not an exhaustive literature search or a priority claim: prime ideal factorization, residue conjugation and the counts are elementary standard facts, applied here to the exact original family.

No old controls, table/phase/Gaussian runs, fresh numerical fixtures, builds, browser, dependency/compiler/Lean install, auth/publication or index mutation were performed. All inputs and all12 protected HEAD/index states are bound in the accompanying author record. No canonical/book/UI/master/README edits were made. Independent proof review is still required before calling this new sector theorem accepted. Whole signed13/12/global9/8, short/principal assembly, determinant/zero-location bridges and scope-specific GRH obligations remain unchanged and open.
