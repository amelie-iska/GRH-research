# Coprime pair-square obstruction and the signed arithmetic frontier

2026-11-03. P7-low-gcd arithmetic rotation. **Proved:** a finite matrix
inequality, its weighted version and its application to actual prime-ideal
sextic columns. **Refuted:** the proposed absolute pair-square estimate used
below. **Open:** the signed original-family mean square and every GRH scope.

## The attempted claim

Keep the pinned October family (paper2.tex:240–275), not a new coefficient
family:

    M_u(D)=D^(-1/2) sum_n mu(n) nu(n) W(Nn/D) chi_n(u),
    chi_n(u)=(u/n)_6,   0<Nu<=H.

Here n is squarefree, primary and prime to the fixed excluded set S (including
2,3 and the fixed character conductor); nu is the original finite-order Hecke
character. Rows are **all elements**, with no division by the six units.
Characters have their actual zero extension. c_n denotes the entire fixed
mu(n)nu(n)W(Nn/D), including the column annular factor. Fix W supported in [1,2] in its norm argument for this trial, so the stated
column annulus is exactly its support; a different fixed annulus requires
the corresponding rescaling throughout. Nothing below replaces c_n in an
alleged estimate for M_u.

The previous high-gcd note/book accidentally called this original chi_n
cubic. The pinned source and its existing independent Gram review specify
**sextic**; the cubic character is chi_n^2. This label is corrected in the
current exposition. The previous high-gcd proof only needs primitive
nonprincipal residual characters and unit modulus, so that proof survives
for the actual sextic family.

For the low-gcd quadratic form, try Cauchy on all off-diagonal column pairs
before using coefficient signs. With C_D=sum_n |c_n|^2=O(D), this gives

    |D^(-1) sum_(n!=m,(n,m)=1) c_n conjugate(c_m) K_H(n,m)|
      <= D^(-1) C_D B_1(H,D)^(1/2),
    B_1=sum_(n!=m,(n,m)=1) |K_H(n,m)|^2.

Thus B_1 << H^2 D^epsilon would suffice for this particular attempt at
O(H D^epsilon), after rescaling epsilon. It is a sufficient **new proposed
input**, not an estimate asserted by the supplied papers. We prove it false
at H=D^(3/4), including for the unchanged original sextic kernels. This is
not a lower bound on the signed quadratic form.

## Universal finite matrix identity

Let A=(A_ui) be an R-by-N complex matrix. Set
K_ij=sum_u A_ui conjugate(A_uj) and F_uv=sum_i A_ui conjugate(A_vi).
These conventions may transpose the usual column Gram; absolute squares are
unchanged. Expanding the four finite sums, commuting complex scalar factors
and reordering them gives exactly

    sum_(i,j) |K_ij|^2 = sum_(u,v) |F_uv|^2.

No spectral theorem, independence or arithmetic conjecture is needed.
Suppose |A_ui|^2=w_u for every i, allowing arbitrary row weights, and write
S=sum_u w_u, Q=sum_u w_u^2. The column diagonals are S and row diagonals
are N w_u. Dropping only nonnegative **row-Gram squares** gives

    sum_(i!=j) |K_ij|^2 >= N^2 Q - N S^2.                 (1)

For w_u=1 this becomes

    sum_(i!=j) |K_ij|^2 >= N R (N-R).                    (2)

The bound is vacuous when N<R; no finite example with a negative right-hand
side is advertised as positive cancellation information. Equality in (2)
holds exactly when distinct rows are orthogonal, i.e. F=N I_R. A rectangular
Fourier matrix supplies examples for 0<R<=N. This is the elementary first
Welch/frame-potential bound, not a new general matrix theorem. The new step
here is its application to the project's coprime arithmetic pair-square
proposal. Datta–Howard–Cochran, arXiv:0909.0206v2, §2.1 Theorem2.2, gives the
classical frame interpretation. The proof above is self-contained.

## Original prime columns force a large coprime pair square

Take columns all prime ideals p outside fixed S with D<=Np<=2D; let N be
their number. Take the full original row ball U_H and R=|U_H|, with H<D.
If p divides a nonzero u, then Nu>=Np>=D. Hence **every original mask is
one on this specified ball**; this is proved by norms, not an artificial
extension. In particular |chi_p(u)|=1. Distinct prime columns are coprime,
and chi_p conjugate(chi_q) has primitive finite residue conductor pq, with
norm in [D^2,4D^2]. All these pairs are genuinely in h=1.

Apply (2) to A_up=chi_p(u). The positive sum defining B_1 contains this prime
subsum, regardless of what the other squarefree kernels do. The elementary
Eisenstein lattice count gives R=(2*pi/sqrt(3))H+O(sqrt(H)+1). The classical
unconditional prime-ideal theorem in this fixed field gives
N~D/log D; equivalently one can use the prime number theorem for rational
primes congruent to1 modulo3 and their two split ideals. This asymptotic is
an explicit classical external input, not formally proved here and not GRH.
The primary publication is Landau, *Neuer Beweis des Primzahlsatzes und
Beweis des Primidealsatzes*, Math. Ann.56 (1903),645–670,
[DOI10.1007/BF01444310](https://link.springer.com/article/10.1007/BF01444310).
Its publisher record is verified; the historical full proof is an external
dependency, not claimed newly audited or formalized.
For H=D^(3/4), R=o(N), so

    B_1(H,D) >= (1-o(1)) N^2 R
              >> D^(11/4)/(log D)^2.                   (3)

Consequently B_1 << H^2 D^epsilon is impossible for any fixed epsilon<5/4.
Its required upper side has size D^(3/2+epsilon). The unrestricted
Frobenius/Cauchy envelope with coefficient square mass comparable to D is
at least order D sqrt(H)/log D, larger than H by D^(5/8)/log D. For a
prime-only coefficient vector with square mass N the corresponding envelope
has another log denominator. Neither envelope is an energy lower bound.

For a nonzero annular W, restrict primes to a closed subannulus where
|W| is bounded below if a weighted pair-square attempt includes W. Such a
subannulus still has N asymptotic to a positive constant times D/log D.
Fixed nu factors have modulus1 off S and do not alter absolute kernel
squares. This does **not** let us isolate the prime part of the original
energy as a positive summand: cross terms with composite columns can cancel.
It also does not justify deleting a prime collision outside H<D, changing
conductors, discarding auxiliary masks or claiming moving-profile uniformity.
For finite nonnegative row profiles, (1) is the exact weighted obstruction;
it says nothing unproved about infinite Schwartz tails with new collisions.

## Checks and formal scope

ShortRowPairBarrier.lean proves four universal results on actual finite
complex matrices: finite frame-potential duality, row diagonal lower bound,
weighted pair-square lower bound and unimodular specialization. Types and
axioms are printed. The ideal-to-matrix character application, lattice
count, prime-ideal theorem and the asymptotic exponent comparison are prose
or explicitly external inputs, not falsely labelled wholly formalized.

scripts/check_short_row_pair_barrier.py uses the existing approved CPU
Python environment and integer arrays. It constructs **sextic** symbols at
both actual split prime ideals (p,omega-w), using zeta6=1+omega and modular
powers. It checks every row's original zero condition, integer Gram duality,
weighted and unweighted lower bounds, and 256 independent scalar pair sums.
The finite diagnostics use the allowed specialization nu=1 and S consisting
of primes above2,3; they compute kernels, not a signed mu-nu energy. There
is no random seed or learned component. The case (D,H)=(256,64) has
H=D^(3/4) but N<R, so its bound is correctly negative. The larger positive
finite cases illustrate (2), not the asymptotic theorem by numerical fit.
The explicit norm7 collision control records why masks cannot generally be
removed. Exact results are in outputs/checks/2026-11-03-low-gcd-pair/.

## Surviving next route

The failed step is replacing the signed coprime kernel quadratic form by
its absolute pair-square mass. Retain mu, nu, W and all zero masks **before**
any Cauchy step in the next attempt. A concrete next construction is the
exact truncated divisor-convolution identity

    mu = 2a - a*a*1 + b*b*1,  a=mu 1_(Nn<=U), b=mu-a,

in ideal Dirichlet convolution (mu*1=delta). On squarefree n, each divisor
factorization retains pairwise coprimality and the row characters' original
zeros. Develop its type-I/type-II kernels and their exact character
conductors before estimating them; the identity itself supplies no
cancellation. No low-gcd signed estimate, positive arithmetic determinant,
new zero-free region or proof of GRH has been obtained by the pair-square
route. Rotate back to the pending P4 linear-relations construction while
keeping this explicit signed arithmetic task active for the next P7 run.
