# Summing the smooth divisor first in the nonunit rough kernel

This is a fresh post-publication analytic attempt. The surviving results are an exact endpoint-sensitive masked-Mertens functional and an explicit residual-scale budget in terms of a scalar deleted-prime Mertens envelope. A hypothetical power-Mertens estimate controls one restricted part, but does not close the remaining coherent kernel: a whole active residual region admits only the unit smooth divisor. No new global exponent, GRH/zero-location result, finite-table experiment, or publication is claimed.

## 1. Actual scope and difference from the recorded history

Use exactly rma:KS, rma:T and rma:shortcoef (the latter is labelled rma:coefficient in the accepted details): Eisenstein ideals, fixed finite S containing primes above 2 and 3, one common complex smooth W supported on [1,2] and zero at both endpoints, fixed unitary multiplicative nu, actual nonzero rows u with Nu<=H, and their original nonnegative weights w_u. Put R_w=sum w_u, B=||W||infinity and M_1=max(B,||xW'(x)||infinity). Require 1<=U, U²<=D<=7U²/2. The columns are the COMPLETE original good squarefree annulus, with no extra selected-column or column-ray indicator. All original row rays, literal units, squarefree/internal-coprime/capacity/sixth-factor restrictions stay in the row family. Raw chi_a(u) zeros are never replaced by primitive surrogates. The identity is a raw AA identity; principal-row residue assembly remains separate.

The accepted rough-mask proof already gives the exact short coefficient and its T_f rewrite. The accepted smooth-f tail note uses an absolute positive norm after a cutoff in F=Nf. Neither records the following two-jump closed-prefix formula, its explicit deletion-uniform residual-scale budget, or the exact unit-f limitation of this scalar route. The nine-state signed-divisor numerator is not replaced on the general K0 branch: the simplification here is restricted to the active rough-prime KS branch. The separate unit residual (a,b)=(1,1) and the original C2 correction are NOT included in this note's nonunit restriction. In particular, no argument below drops the unit two-rough correction or identifies its distinct-prime unordered pairs with an auxiliary ordered pair sum.

## 2. Exact radialization, with full masks and coupled cutoffs

Expand KS in residual ideals a,b before taking any absolute value in f, a conductor, or a row. Define

    eta_ab(u)=nu(a) conjugate(nu(b)) chi_a(u) conjugate(chi_b(u)),
    T=S union supp(a b u),   M=max(Na,Nb), alpha=min(Na,Nb).

The ideals a,b are individually good squarefree but may overlap. Every prime of a common support remains in T even if their quotient character loses that prime. The outside rough prime p is restricted only by p notin S and P=Np>U, exactly as in the auxiliary KS; it may divide a,b or u. The smooth f still avoids T. Common nu(f) and chi_f(u) phases cancel only to their original raw (f,u)=1 restriction.

If (a,b)!=(1,1) and both profile factors are nonzero, then M>=7 and

    F M P < 2D <= 7U²,  P>U,
    F M < 7U,  hence F<U.                                    (1)

Therefore EVERY such f is automatically U-smooth. Removing that redundant restriction does not restore an original raw zero. Since fa and fb remain squarefree and have norms <7U, the accepted exact short lemma yields

    mu(f) A_U(fa) A_U(fb)
      =mu(f)mu(a)mu(b) s(F Na)s(F Nb),
    s(z)=2*1_(z<=U)-1.                                      (2)

This is not unrestricted coefficient multiplicativity. It uses only the active rough branch and (f,ab)=1. Put

    X=D/(P M), r=alpha/M, c=U/M, d=U/alpha.

At r<=1/2 the profile is identically zero, including equality. Otherwise r in (1/2,1]. If Na=M use Phi_r(v)=W(v)conjugate(W(rv)); for the opposite orientation use its conjugate. Let h(t)=Phi_r(t/X). It is supported in [X/r,2X] with zero endpoint values. The EXACT coupled cutoff product, including ties, is

    s(F Na)s(F Nb)=1-2*1_(c<F<=d).                          (3)

If alpha=M, c=d and this interval is empty. Write

    M_T(t)=sum_(good f, Nf<=t, (f,T)=1) mu(f),
    M_T(t)=0 for t<1.

The scalar kernel in the expanded nonunit KS is exactly

    I_ab,u(P)=sum_(f, (f,T)=1) mu(f) h(Nf)
                          [1-2*1_(c<Nf<=d)].              (4)

The original contribution is mu(a)mu(b) eta_ab(u) I_ab,u(P), summed over the actual rows and primes. This finite equality retains the coherent mean; no independence of residual supports or row phases has been imposed.

## 3. Closed-prefix Abel identity and variation

Ordinary finite Abel summation, using the CLOSED prefix M_T(y), gives

    sum_(Nf<=y,(f,T)=1) mu(f)h(Nf)
        =h(y)M_T(y)-integral_0^y M_T(t)h'(t) dt.

Consequently (4) is EXACTLY

    I = -integral_0^infinity M_T(t)h'(t) dt
        +2 integral_c^d M_T(t)h'(t) dt
        +2 h(c)M_T(c)-2 h(d)M_T(d).                       (5)

No half-weight is allowed at an integer norm equal to c or d. Both boundaries are closed-prefix values: their difference implements c<Nf<=d. When c=d the two boundaries and the restricted integral cancel. Values of c,d outside the profile give zero h there; this also treats small/subunit scales without a sieve input.

The derivative term combines to a multiplier of absolute value one almost everywhere. In log coordinates,

    integral |h'(t)|dt <= 2 B ||xW'(x)||infinity log(2r)
                       <= 2 log(2) M_1².

The two point terms cost at most 4B². Thus, with

    Mloc_T(X)=sup_(X<=t<=2X) |M_T(t)|,

one has the valid finite bound

    |I_ab,u(P)| <= (4+2log2) M_1² Mloc_T(X)
                <= 6 M_1² Mloc_T(X).                     (6)

The point terms need M_T only when h(c) or h(d) is nonzero, hence in the same [X,2X] interval. The weak final inequality includes W=0 and all other degenerate cases. This argument requires one derivative of W. The earlier mask-error theorem needs no derivative; those distinct statements must not be conflated.

## 4. An explicit uniformity quantity and a quantitative restricted budget

For Q>=1 and Y>0 define the scalar deleted-prime envelope

    m_Q(Y)=sup_(E finite good primes outside S, Nrad(E)<=Q)
                 sup_(t>=Y) |M_(S union E)(t)|/t.           (7)

This is a precisely specified uniformity requirement, not an asserted cancellation theorem. Elementary ideal counting gives m_Q(Y)<=16 for every Q,Y: below t=1 the numerator is zero, and above it its absolute value is at most the number of ideals <=t. A useful cancellation estimate must be uniform as Q grows, rather than only for each fixed deleted set. The independent parallel lane treats the deleted-prime convolution and the exceptional unit residual; no such external theorem is needed for the elementary bound below.

Restrict the expanded nonunit KS to X=D/(PM)>=Y, with Y>=1/2, and call the resulting SIGNED expression KS[nonunit;X>=Y]. This is a restriction after residual expansion; it is not an original selected-column family or a positive submoment. Y here cuts X, NOT the smooth divisor F in the previously accepted positive-tail note. On support,

    Nrad(T outside S)<=Na Nb Nu <=(2D/P)²H <=14DH.           (8)

Let Q=14DH. Equations (6)--(7) give |I|<=12M_1² X m_Q(Y). For a fixed P put Z=D/P. Since X>=Y, M<=Z/Y. The elementary ideal bound A_K(t)<=16t implies, for T0>=1,

    number of ordered (a,b) with max(Na,Nb)<=t <=256t²,
    sum_(max(Na,Nb)<=T0) 1/max(Na,Nb) <=512T0.

The latter follows by one-dimensional partial summation, and is zero if T0<1. Therefore the residual absolute sum at this stage is <=6144 M_1² m_Q(Y) Z²/Y. Independently,

    sum_(prime ideals P>U) P^(-2)
      <=sum_(all ideals Ng>U) (Ng)^(-2) <=32/U.

Only now use the triangle over residuals, primes and actual rows, and divide by D. This proves the unconditional, fully specified budget

    |KS[nonunit;X>=Y]|/D
       <=196608 M_1(W)² R_w [D/(U Y)] m_(14DH)(Y),
       Y>=1/2.                                            (9)

Every full-union deletion remains in (5)--(7); the triangle in (9) does not remove it before summation. Arbitrary nonnegative original row weights are allowed because (9) uses only |eta|<=1 and their total mass, not an unproved weighted BGL operator extension. The unused capacity/ray conditions remain in the actual row family. If Y>=D/(7U), the nonunit restriction is empty, since P>U and M>=7 imply X<D/(7U). Equality is harmless.

A CONDITIONAL corollary makes the required power uniformity explicit. If, for a fixed 0<theta<=1 and every epsilon>0,

    |M_(S union E)(t)| <= C_(theta,epsilon,S)
                           (Nrad E)^epsilon t^theta
    for all finite E and t>=1,                             (10)

then for Y>=1,

    |KS[nonunit;X>=Y]|/D
      <<_(theta,epsilon,S) M_1² (DH)^epsilon R_w
                          (D/U) Y^(theta-2).              (11)

The proof is m_Q(Y)<=C Q^epsilon Y^(theta-1) in (9). Theta=1 has the elementary C=16 version. No theta<1 hypothesis is assumed or proved here, and the fixed-field PIT statement in the accepted book is not such a Mertens theorem. A fixed-S Mertens bound alone must first be transferred with its explicit deletion factors; the parallel lane owns that step. In particular (11) is a conditional restricted-kernel result, not an unconditional signed saving.

## 5. The decisive failed step at bounded f-length

For the full nonunit residual range, X>1/2; applying (9) at Y=1/2 gives only O(M_1² R_w D/U), since m_Q(1/2)<=16. In the high window D/U is comparable to sqrt(D). A power Mertens estimate, even one much stronger than currently granted, gives no power improvement from this residual triangle: after summing M near Z=D/P, the powers of Z from X^theta and the residual pair count still combine to Z².

This is not merely a coarse estimate of a long signed sum. On the entire active region 2X<=7, every possible nonunit good f has Nf>=7 and is excluded by strict endpoint support. Therefore ONLY f=1 contributes, and exactly

    I_ab,u(P)=h(1)[1-2*1_(c<1<=d)].                       (12)

The full raw mask of f=1 is one. In particular a=b nonunit gives r=1 and I=|W(1/X)|², which can be nonzero for 1/2<X<1. No cancellation in f exists in this region. This diagonal observation is an exact limitation of a proposed scalar summation route; it is not a new diagonal budget or a lower bound for the complete signed slice. Off-diagonal outer phases and coherent row means still matter and may cancel across residual sectors.

Thus the failed inference is: a scalar masked-Mertens bound controls a long f sum, therefore it controls the complete nonunit KS at target size after residual absolute Cauchy/triangle. The bounded-length region invalidates that inference. Equations (5) and (9) are genuine surviving reductions; they do not estimate K0, the unit residual, the full KS or K0-KS at the target scale. They neither prove impossibility of a coherent method nor an uncancelled zeta pole. The original 7/6 envelope and missing 5/12 saving remain unchanged. Any successful use of this swap must additionally estimate the actual mean-retaining residual/row combination in the bounded-X region (and its combination with K0), instead of asking M_T to cancel a sum with only one term.

## 6. Evidence and preservation

The companion source pin records the exact current rma/signed-divisor sources, governing handoff, tail review and all ELEVEN old HEAD/index states. The only fresh finite checks are synthetic rational coefficient checks of the two-jump Abel identity, including exact threshold ties, complex profile values, c=d and omitted-boundary negative controls. They do not enumerate arithmetic ideals, phases, old tables or saved trajectories and do not prove the analytic estimate by fitting. The proof above is self-contained apart from the already accepted coefficient and elementary ideal-count lemmas, whose derivations and exact source bytes were read.

All canonical papers/book/data, prior planning/history and public/frozen release files remain unchanged. No new source literature, dependency, compiler, browser, authentication or publication action was used. The note is not integrated or independently accepted merely because it is written.
