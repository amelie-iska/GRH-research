# Independent adversarial review of the fixed-twist AFM argument

2026-11-04. Remote-only review. Reviewed afm-20261104-fixed-twist-draft.md,
research/hecke-type-i.md and the exact pinned BGL1112.1650v1 primary PDF.
No production source, environment, model or credential was modified.

Verdict: the argument supplies the stated AFM for the original finite-order
nu scope, using the explicit classical inputs below, after the one character-
construction precision noted here is included. This is a prose analytic
proof audit, not a Lean verification or a GRH proof. The residual U cutoff
loss, principal residue, short term and II–I covariance remain unresolved.

## Character/family and primitive-mask audit

BGL explicitly adopts primitive characters, distinguishes arithmetic products
from primitive products, and in Lemma2.1 states multiplication for a product
that is sixth-power-free, as well as invariance under sixth-power parameters.
Thus the decomposition a=a0 a1 a2^6 has the required exact character identity
on ideals prime to S: a0 is squarefree, a1 has valuations2..5, and the first
two factors are coprime. No claim about arbitrary primitive characters or an
order-dividing-six restriction on fixed nu is required.

AppendixII writes a=(x)E g^6 and alpha_a=x m_E. Fix such a decomposition.
For any u with (u)_S=a and a generator y of g as an O_S ideal, alpha_a y^6/u
is an S-unit. Its class modulo sixth powers belongs to a finite group, so
the literal Kummer character is one of finitely many fixed S-supported twists
of the canonical family. Because AppendixII can choose g relative to a test
ideal b, state the equality as follows: compare with the fixed radicand on
all primes outside the finite set S,a,g and then invoke uniqueness of the
underlying Hecke/Artin character to extend it. This avoids treating an
arithmetic zero sentinel as a primitive identity.

For a fixed outside-S ideal a and an S-supported integral ideal b there are
at most six generators of (u)=ab. Summing the fixed-twist ideal bound at
X=H/Nb retains every original unit and S-prime-power row and converges by
the finite Euler product at exponent1+epsilon. Outside S, inertia has tame
order6/gcd(v,6), so the primitive product conductor is exactly the radical
of the sixth-power-free part there; S-local types are finite. Consequently
Q_rho is at most a fixed constant times N(a0 a1), uniformly in a2.

## Large sieve, AFE and masks

The fixed twist xi=nu*eta has conductor supported in S. At squarefree
columns prime to S its values have modulus one, so multiplying the column
sequence by xi preserves its l2 norm, whatever the finite order of nu.
Multiplication by the fixed chi_a1 values has modulus at most one. This is
an application of BGL's large sieve to a changed coefficient sequence, not
a claim that xi lies in their finite ray-class character group.

In the finite-order imaginary-quadratic scope all archimedean types are
zero. The primitive central AFE therefore has a common gamma kernel. On
Re z=eta, the normalized ratio Gamma(1/2+it+z)/(Gamma(1/2+it) T^z) is bounded
uniformly in t by a polynomial in |Im z| times exp(pi|Im z|/2), using Stirling
and |t+y|<=T(1+|y|). The Gaussian auxiliary factor supplies an integrable
majorant. Analogous bounds hold on each fixed positive shifted line.
The conductor phase is a bounded row multiplier after Minkowski; its
positive real part contributes only (HT)^O(eta). The dual AFE adds a
unit root-number/conductor phase, harmless after separating its l2 norm.
A common total-ideal cutoff B'=sqrt(X)T(HT)^eta has arbitrary inverse-power
tail after choosing the positive kernel-decay shift sufficiently large.
These are classical functional-equation/Stirling inputs, not GRH.

For b=bS b1 b2, the first and third factors have fixed support type and
summable weights at1/2+eta; b1 is squarefree and coprime to b2. The original
primitive factor rho_a(bS), including any conductor drop, stays as a row
multiplier of modulus at most one. On b1,b2 prime to S the canonical
factorization is valid; the chi_a0(b2) factor is also a bounded row
multiplier. Extra coprimality and shortened b1 cutoffs go into the fixed
column coefficients for each bS,b2,a1. They do not require replacing a
complex sum by a larger one: pad its coefficients by zero up to B'.
Minkowski and the convergent bS,b2 weight sum are precisely the mechanism
already used in the primary proof of Corollary1.4, now with the fixed twist.

For each a1,a2 the energy is (HT)^O(eta) times
M+B'+(MB')^(2/3), M=X/Na1. Summing squarefull a1 gives
X+B' sqrt(X)+(XB')^(2/3), because squarefull counting is O(sqrt(X)) and
its Dirichlet series converges at1 and2/3. Substitution gives O(XT)
up to the declared small losses. The a2 sum uses zeta_K(6). Principal rows
are excluded from the pole-free AFE and bounded directly using ordinary
zeta_K central convexity and O(H) row counting. Internal eta may be chosen
small for any requested final epsilon; constants depend on it and fixed nu,S.

## Off-central Poisson transfer

For a finite row family, divide each L by (s+1)^(5/4); for principal rows
also multiply by (s−1)/(s+1). Classical continuation/convexity makes these
bounded analytic functions on Re s>1/2 with continuous bounded boundary.
The principal pole is removed before applying Poisson/Jensen. Their boundary
squared moments decay with weight (1+|v|)^(-alpha), alpha=3/2−epsilon0.
For epsilon0 in(0,1/4], alpha is in[5/4,3/2). Poisson convolution with that
weight is at most11 times the same weight, uniformly0<delta<1/2:
for |t|>=2 the near region costs at most2^alpha<3, while the far region costs
at most2 delta 3^alpha/[pi(alpha−1)]<8; bounded t costs at most3^alpha<6.
Symmetry covers negative t. The boundary denominator comparison costs less
than3, and restoring the interior denominator costs less than6 T^(5/2).
The inverse principal pole-removal ratio is at most
(3/2+delta)/(1/2−delta). Hence the advertised constant
200 Ccentral [(3/2+delta)/(1/2−delta)]^2 is valid (11*3*6=198<200).
No zero-location hypothesis is used. The exclusion delta=1/2 is essential:
that line would pass through the principal pole.

## Evidence and remaining boundaries

The exact-controls JSON records61 valuation decompositions and the rational
constant inequalities; those finite checks do not prove the analytic theorem.
The source-pin JSON records the primary PDF hash and reviewed ranges. The
fundamental theorem uses the ordinary primitive Hecke functional equation,
Stirling, character uniqueness/class-field identification, and BGL's proved
large sieve, all external analytic/algebraic dependencies. No new Lean,
Artin-holomorphy, arithmetic positivity or complete spectral determinant
comparison is obtained. AFM improves the conditional transfer's H exponent,
but its D^(2delta) U^(2−4delta) loss still prevents claiming MS3/4 at fixed
positive cutoff, let alone GRH.

## Final kernel reread and scope extension boundary

The corrected draft was reread at its displayed Mellin kernel: it now has
`dz/z`, supplying the residue at zero, and uses
`x = 2*pi*Nb/(sqrt(Q_rho)*T)` with the normalized gamma ratio `T^(-z)`.
These factors combine to `(sqrt(Q_rho)/(2*pi*Nb))^z`, so no extra factor of
T is inserted into the actual completed-L kernel. Its coarse maximal
length remains `sqrt(X)*T` up to fixed constants and the stated small loss.
The fixed-global-radicand paragraph is also present. No further load-bearing
obstruction was found in the finite-order-nu AFM argument reviewed here.

A separate extension to a fixed unitary Hecke character with nontrivial
infinity type is plausible by the same proof, but is not silently part of
this review's finite-order verdict. It requires stating the actual common
shifted gamma factor, its primitive functional equation, and separating any
norm-twisted principal rows before the pole-free AFE. With a convention
`L(s,Norm^(i*tau)) = zeta_K(s+i*tau)`, its pole is at `1-i*tau`; the factor
`(s-1+i*tau)/(s+1+i*tau)` cancels it and has boundary modulus at most one
on Re(s)=1/2. Constants may depend on the fixed infinity type; no uniformity
in nu has been reviewed or established. This is an extension boundary,
not a new formalization or a claim about GRH.

## Written fixed-unitary extension audit

I subsequently read the separate extension at draft lines264--321. It now
explicitly fixes the ideal-character convention
`nu(a)=nu_0(a)*(Na)^(-i*tau)`, common gamma factor
`2*(2*pi)^(-(s+abs(m)/2+i*tau))*Gamma(s+abs(m)/2+i*tau)`,
and the primitive conductor/functional-equation input. With that convention
the pure norm L-function is exactly `zeta_K(s+i*tau)`. This explicit ideal
formula supersedes any ambiguous shorthand involving a power of "Norm" in
the preceding boundary discussion.

The extension is accepted in this separately stated fixed-unitary scope:
the finite-order Kummer factors do not alter m or tau, the primal and dual
gamma arguments have opposite vertical parts at s and 1-s, and
`1+abs(t+tau)+abs(m)` is comparable to `1+abs(t)` with constants depending
on the fixed nu. The large-sieve column twist still has modulus one.
Conductor alternatives at S remain finite. The only polar rows are the
pure norm rows, which are excluded from the pole-free AFE, bounded by
ordinary shifted Dedekind-zeta convexity, and treated in the Poisson step
with the explicitly shifted factor h_tau. Its boundary modulus and inverse
interior bound are independent of tau. Thus the numerical Poisson factor
200 remains valid relative to the now nu-dependent central moment
constant.

This acceptance invokes the stated classical primitive Hecke analytic
continuation and functional equation for the fixed infinity type, in
addition to the large-sieve and algebraic inputs already listed. It gives
no constant uniform in nu or varying infinity type, no Lean verification,
and no removal of the residual cutoff, signed-covariance or determinant
obligations.
