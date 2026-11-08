# Deleted-prime Mertens input and the ordered unit correction

Research-only lane C, outside the frozen153-file release and current book. The surviving result is an exact artificial-Euler-deletion transfer, a fixed-field uniform subpower corollary, and an elementary unit-residual correction. It does not prove a new sieve, a signed KS or K0-KS estimate, a fixed power saving, GRH, a determinant comparison, or a Lean result. All quantities count IDEALS; conjugate prime ideals are separate even when their rational norms coincide.

## 1. Actual rough-prime objects and the scalar that is eligible

Use the COMPLETE original good squarefree annulus and the accepted rma hypotheses: fixed finite S containing primes above2,3 and the original defining conductor, one common complex smooth W supported on[1,2] with endpoint values zero, U>=1, U^2<=D and2D<=7U^2. The original literal/ray/squarefree/coprime/capacity row family is unchanged. Keep every raw character zero. Principal-row residues, if allowed in a generic raw family, still need their separate assembly; the intended first-factor blocks are nonprincipal under the original conductor-supported-in-S condition. The elementary identities below allow nonnegative actual row weights; the later inherited classical row-operator input is not extended to arbitrary weights.

Write A=Na, Bn=Nb, M=max(A,Bn), F=Nf and P=Np. In a nonzero rough-P profile term, F A,F Bn<=2D/P<7U. The accepted restricted identity on good squarefree g, including g=1, is

 A_U(g)=mu(g)(2*1_(Ng<=U)-1), Ng<=7U.

Since(a,f)=(b,f)=1, the ACTUAL coefficient product therefore equals

 A_U(fa)A_U(fb)=mu(a)mu(b) q_a(F)q_b(F),
 q_a(F)=2*1_(F A<=U)-1, q_b(F)=2*1_(F Bn<=U)-1.       (1)

No mu(f) factor is removed from the outer signed sum. Residual a,b may overlap. Their full deleted set is T=S union supp(abu), even where a primitive quotient character drops a conductor prime. The fixed residual outer coefficient remains nu(a)conj(nu(b))*chi_a(u)conj(chi_b(u)); a raw zero stays zero.

For any nonunit residual pair, M>=7. The same support gives F M<7U, hence F<U; the U-smooth restriction on f is AUTOMATIC there. Thus the eligible scalar is a squarefree Mertens sum prime to the FULL T against the radial common profile times the two threshold signs in(1). A separate lane supplies its endpoint-sensitive two-jump Abel formula and coupled residual-scale analysis. The signs use <= exactly at an integer norm cutoff; no half-weight convention or smooth replacement is permissible.

This restricted radialization is only for the rough-P branch. It does not replace A_U(fa) in K0, where active N(fa) can be as large as2D rather than7U. It also does not prove multiplicativity of A_U in general, or apply to separate C-mu channels.

## 2. Artificial Euler deletions are not new primitive conductors

Put M_K(x)=sum_(Nc<=x)mu(c) and M_T(x)=sum_(Nc<=x,(c,T)=1)mu(c), including the unit. Let D_T be the multiplicative monoid of ALL ideals supported on T, with prime powers allowed, and for sigma>0 define

 E_T(sigma)=product_(p in T)(1-(Np)^(-sigma))^-1.

Absolute Euler multiplication on Re(s)>1 gives the EXACT coefficient identity

 1/zeta_K^T(s)=1/zeta_K(s)*product_(p in T)(1-(Np)^(-s))^-1,
 M_T(x)=sum_(d in D_T,Nd<=x) M_K(x/Nd).                 (2)

The d in(2) are not restricted to squarefree ideals. This is a positive-coefficient deletion convolution; replacing it by a primitive conductor-uniform Hecke estimate is incorrect. In Re(s)>0 the finite deletion product has no poles; its possible poles lie on Re(s)=0. The primitive analytic zeta function is still the ONE fixed zeta_K. None of the full T raw zeros are restored by passing to a smaller primitive conductor.

Let C_K be such that the ideal count is at most C_K x for x>=1, and define rho_K(t)=sup_(y>=t)|M_K(y)|/(C_K y), so0<=rho_K<=1 and rho_K is nonincreasing. For any x>=1 and0<delta<1, splitting(2) at Nd=sqrt(x) and using Rankin on the complementary positive monoid yields the unconditional transfer

 |M_T(x)|<=C_K x E_T(1-delta)
                  [rho_K(sqrt(x))+x^(-delta/2)].          (3)

For the first part, x/Nd>=sqrt(x) and sum1/Nd<=E_T(1)<=E_T(1-delta). For the second, sum_(Nd>sqrt(x))1/Nd<=x^(-delta/2)E_T(1-delta). All mask dependence is explicit, with no hypothesis on the varying number or sizes of deleted primes. Formula(3) remains valid when its numerical bound is worse than trivial; one may always take its minimum with C_K x.

## 3. Fixed-field zero-free input and the honest uniform factor

The already pinned primary source is Thorner--Zaman, A unified and improved Chebotarev density theorem, Algebra & Number Theory13(2019),1039--1068, DOI10.2140/ant.2019.13.1039. Its Theorem3.1 on printed1051 supplies the classical zero-free region with a possible single fixed exceptional real zero. Here specialize only the trivial extension K/K with K=Q(omega), absolute degree2 and discriminant3. T is not inserted as a varying field discriminant or primitive Hecke conductor. This use is distinct from quoting its prime-counting theorem as if that theorem directly stated a Mobius bound.

For completeness the fixed-field contour deduction is as follows. The Euler bound to the right of1, the fixed-degree functional equation/convexity bound in a strip of width O(1/log(|t|+3)), and Borel--Caratheodory applied to an analytic log(zeta_K) on a smaller zero-free disk give

 |1/zeta_K(sigma+it)| <<_K log^A(|t|+3)
 for sigma>=1-c_K/log(|t|+3),

after shrinking c_K; bounded t is handled on a fixed compact zero-free neighborhood of1. A fixed exceptional zero is left outside that neighborhood. Truncated Perron at the half-integer floor(x)+1/2 can then be shifted to1-c_K/log(T+3). There is no residue at s=1, since1/zeta_K has a zero there. The ideal annular count O_K(h+sqrt(x)) controls the Perron near-integer error; it follows from planar lattice counting in this class-number-one quadratic field. The resulting bound is

 M_K(x) <<_K x log^A(2x)
       [exp(-c_K log(x)/log(T+3))+1/T]+sqrt(x)log^A(2x).

Taking T=exp(c'_K sqrt(log(2x))) with a sufficiently small fixed c'_K and absorbing logarithms proves the classical fixed-field corollary

 |M_K(x)| <<_K x exp(-c''_K sqrt(log(2x))).                (4)

Constants and the starting threshold are fixed-K constants; a possible fixed exceptional zero is absorbed only by that fixed threshold. Nothing here is a uniform assertion as a conductor or field varies, and no fixed power x^(1-c) or GRH-quality error follows from this contour.

To quantify the deletion factor, set R_T=Nrad(product_(p in T minus S)p), Z=log(e^3 R_T)>=3. For0<delta<=1/2, elementary ideal counting and splitting deleted primes at Q=Z^2 give

 log E_T(1-delta)
    <= C_(K,S)[1+Z^(2delta)log Z].                       (5)

Indeed the small-prime sum is bounded by the sum over all ideals up to Q, which is O_K(Q^delta log Q). For deleted primes P>Q, use sum log P<=log R_T and monotonicity of P^(1-delta)log P: their reciprocal-power sum is at most log R_T/(Q^(1-delta)log Q), bounded here. Fixed S factors cost only a fixed constant.

In particular delta log Z<=1 gives E_T(1-delta)<<_(K,S) Z^A. Combining(3)--(5), and choosing delta=min(c/sqrt(log(2x)),1/log Z,1/2), gives, for x>=3,

 |M_T(x)| <<_(K,S) x Z^A
  exp(-c min{sqrt(log(2x)),log(2x)/log Z}).                (6)

The explicit product version(3) is the primary uniform statement; (6) is a convenient possibly weak corollary. Both remain bounded above by the trivial alternative. When R_T<=D^C and x>=D^v for FIXED C,v>0, the condition delta log Z<=1 holds at large D and

 |M_T(x)| <<_(K,S,C,v) x log^A(2D)exp(-c sqrt(log(2x))).   (7)

This is uniform over the artificial deletions in that polynomial range and supplies a usable scalar subpower cancellation input. It gives no fixed power saving in x.

For active KS residuals, A,Bn<2D/U, so R_T<=Na Nb Nu<4D^2 H/U^2<=14DH. Thus the polynomial mask range in(7) holds at the critical H<=D^(3/4). It still requires a genuinely long scalar f range, not x around1. All full T masks remain in(2)--(7).

## 4. The unit residual: ordered rough-prime correction

For a=b=1, the coefficient product in(1) is1 and residual phases are1. Every active F<2D/P<7U. If a squarefree good f in this support has a rough prime q with Q>U, any further nonunit factor would have norm at least7, contradicting F<7U. Hence a nonsmooth f is EXACTLY one prime q>U, with mu(f)=-1.

Let K_all denote KS with its smooth-f restriction removed, using the actual coefficient product(1), full(f,abuS) mask and original residual outer phases. Then the exact identity is

 KS=K_all+P2,
 P2=sum_u w_u sum_(p notin S,P>U)
                  sum_(q notin S,Q>U,q not dividing u)
                       |W(PQ/D)|^2.                    (8)

The pair(p,q) is ORDERED, p=q is allowed, and p is STILL deliberately unmasked from u. The restriction q not dividing u comes from the original f mask. These conventions are essential. P2 is NOT the accepted unordered distinct unit-semiprime correction C2, whose original row mask is(u,pq)=1.

Using A_K(X)<=16X, each prime in a nonzero pair has norm<=2D/U. Therefore

 0<=P2/D<=1024 B^2 R_w D/U^2<=3584 B^2 R_w.             (9)

This elementary count includes repeated and conjugate primes and does not assert that they are original squarefree column pairs. The accepted original identity remains

 S_AA^raw=(K0-KS)/D+Delta_mask+C2/D
         =(K0-K_all)/D+Delta_mask+C2/D-P2/D.             (10)

Both original C2 and the distinct P2 correction are kept, with their exact signs and masks. This is target-row-mass bookkeeping only; it does not estimate the coherent main.

## 5. Why scalar Mertens does not close the actual sum

For a comparable residual pair and rough P, the f profile is supported on length X=D/(P M), up to fixed factors. Equations(3)--(7) can be inserted by exact partial summation against the common profile and the two actual threshold signs, retaining their integer endpoints. They produce subpower improvement on genuinely long X; they do not make the coherent outer(a,b,u,p) sum small by themselves.

In particular residuals M comparable with D/P leave X comparable with1, so f=1 survives and the scalar Mertens bound is only a constant. Even a hypothetical square-root Mertens bound is a constant at X=1. The remaining raw character/nu coefficients, residual supports and literal rows still have to cancel in the outer coupled sum. An absolute residual triangle has the elementary inherited scale O(BV-profile-cost * R_w D/U), or O(R_w D^(1/2)) at the critical U~sqrt(D), before a genuine long-length restriction. This is not a target-size bound and can be weaker than the already accepted7/6 operator envelope; recovering that envelope with the old classical positive input would not be a new gain. The other lane retains the precise length-restricted theta-power budget rather than treating this coarse triangle as a theorem of cancellation.

No conclusion that the actual energy is large, the target false, or a global zeta barrier unavoidable follows. Cross-sector/coherent cancellations remain possible. This lane establishes the deletion transfer and ordered unit correction, while the signed KS and K0-KS estimates remain open. It does not silently promote a scalar Mertens input into the required outer operator estimate.

## Provenance and protected progress

Only the already present primary publisher text was read remotely; no full third-party source is copied to public inputs. Citation/SHA metadata only is saved beside this note. No old experiment, old finite table, publication audit, browser, package/compiler/install/auth, or canonical/source/index edit is part of this attempt. All11 protected SOURCE/release HEAD and index byte states are checked unchanged.
