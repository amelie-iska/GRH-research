# Fixed-twist arithmetic-family moment: accepted finite-order proof note

2026-11-04. Status: proved in prose using the named classical inputs, with independent adversarial analytic review completed. This is not Lean verification.
Remote-only. No production source, environment, model or credential changes.
This is NOT a GRH proof and does not remove the positive-cutoff/covariance loss.

## Exact scope and classical inputs

K=Q(omega), O=Z[omega], n=6. Fix a finite-order Hecke character nu as in
research/hecke-type-i.md and research/short-row-pair-barrier.md. This draft
keeps that literal finite-order scope; a fixed angular/norm twist is not
silently identified with it. Let S contain primes above6 and f_nu. Its set
of prime ideals is fixed. O_S has class number1. Enlarge the fixed local
modulus if needed; no modulus grows with H, u, d or t.

Classical inputs: abelian Kummer/Artin identification with arithmetic
Frobenius and primitive character conventions; the usual completed primitive
Hecke functional equation and Stirling estimates; BGL1112.1650v1 Thm1.3
for its specified sixth-order family; BGL AppendixII's construction of those
characters. The analytic AFE reduction below is spelled out as the standard
Mellin derivation from this functional equation, not assumed GRH/Lindelof.
All finite-order characters have trivial infinity type on this imaginary
quadratic field, so their gamma factors are the same.

Theorem (fixed finite-order nu): for fixed 0<delta<1/2, any epsilon>0, H>=1, t real,

 sum_(0<Nu<=H) |L(1/2+delta+it, primitive(nu*kappa_u))|^2
   <<_(delta,epsilon,nu,S) H^(1+epsilon)(1+|t|)^(1+epsilon).   AFM

The row sum is over actual nonzero Eisenstein elements, not ideals modulo
units. No full deleted set T(u,d), square denominator or row mask is replaced
in the type-I expression: this theorem concerns only its primitive numerator.

## 1. Explicit finite S-unit comparison

Use BGL AppendixII notation. For each a in I(S), its defining radicand
alpha_a=x*m_E satisfies (alpha_a)_S=a*g^(-6), since
 a=(x)*E*g^6 and (m_E)_S=E. Choose y generating g in O_S.
For any u with outside-S ideal a, (alpha_a*y^6/u)_S=(1).
AppendixII permits choosing g relative to the tested denominator. Fix one
admissible global decomposition for a first. Its defining radicand agrees
with chi_a on every prime outside the finite set S union supp(a*g), where
that fixed decomposition is valid. Equality of the associated primitive
Hecke/Artin characters follows from uniqueness (equivalently Chebotarev
on their finite abelian quotient). We need no uniform tested-denominator
choice of g after this identification.
Thus e=alpha_a*y^6/u is an S-unit and in K*/K*6,
 [alpha_a]=[e*u]. Consequently
 kappa_u=kappa_(e^-1)*chi_a
as underlying primitive Artin characters, after matching the Frobenius/root
convention. If a symbol convention is conjugated, use the conjugate BGL
family; its large sieve follows by conjugating coefficients.

O_S*/O_S*6 is finite (rank |S|, roots of unity mu6). Choose its finite
representative set E_S. Each associated Kummer character is unramified
outside S; their conductors divide a fixed S-supported ideal. This proves
that every literal row numerator belongs to a finite union of fixed twists
primitive(nu*eta*chi_a), eta in {kappa_e:e in E_S}.

The equality is one of primitive characters, NOT of their independently
zero-extended array presentations at bad primes. Primitive products must
be taken before conductor-dependent Euler factors are evaluated.

For each outside-S ideal a and S-supported integral ideal b, there are at
most6 generators u with (u)=a*b, since O is a PID with6units. Hence a
central moment estimate for each fixed-twist canonical family with Na<=X
transfers to all literal rows with Nu<=H by

 6*sum_(b S-supported,Nb<=H) sum_eta sum_(Na<=H/Nb)
           |L(s,primitive(nu*eta*chi_a))|^2.

If each inner moment is <<X^(1+epsilon)T^(1+epsilon), T=1+|t|,
the b-sum is bounded by H^(1+epsilon)T^(1+epsilon) times
 prod_(p in S)(1-Np^(-1-epsilon))^(-1). All original unit and S-prime
powers are retained; no row-multiplicity assumption is needed.

## 2. Fixed twist in the squarefree large sieve

Fix xi=nu*eta (primitive underlying character) with f_xi supported in S.
For (b,S)=1, xi(b) has modulus1. Thus multiplying a column coefficient
lambda_b by xi(b) preserves its squared norm. For another fixed a1,
multiplication by chi_a1(b) has modulus<=1 and cannot increase that norm.
Therefore BGLThm1.3 also bounds

 sum_(a0 squarefree,Na0<=M) |sum_(b1 squarefree,Nb1<=B)
            lambda_b1 * xi(b1)*chi_a1(b1)*chi_a0(b1)|^2
 <<(MB)^epsilon (M+B+(MB)^(2/3)) sum|lambda_b1|^2.

Both ideal families are prime to S. Any extra restriction on a0 is a
subset of the positive outer sum. Coprimality with a fixed b2 is absorbed
in lambda. The order of xi need not divide6: xi is a fixed multiplier of
column coefficients, not asserted to be a character of BGL's finite Rc.

## 3. Central AFE, conductors and all-ideal parameters

For a in I(S), write uniquely a=a0*a1*a2^6, where a0 is squarefree,
a1 is squarefull and sixth-power-free, and (a0,a1)=1. BGL's stated
multiplicativity/invariance identify chi_a with chi_a0*chi_a1 away from S.
Alternatively finite S-unit comparisons as in section1 yield the same
exterior equality after a finite partition into additional fixed S-unit
twists; this does not alter any estimate below.

Outside S, the primitive product rho_a=primitive(xi*chi_a) has conductor
exactly rad(a0*a1): the good primes are tame, xi is unramified there, and
exponents1..5 give nontrivial sixth-order inertia. At S, the possible
characters chi_a|K_p* form a finite set (sixth-order local classes), so
rho_a has one of finitely many S-local conductor types. Split rows into
these types if desired. Uniformly Q_rho <=C_(xi,S)*N(a0*a1).
For a2 fixed put X=H/(Na2)^6; thus Q_rho<=C*X.

For a nonprincipal rho, at s=1/2+it the balanced primitive functional
equation yields two weighted Dirichlet polynomials, with unit root number
on the dual term. Their common maximal length can be truncated at
 B'=(X^(1/2)*T)*(HT)^eta
for any fixed tiny eta>0, with negligible O((HT)^(-A)) error. Here all
fixed xi/S conductor constants are absorbed. Pole/principal rows are
handled separately below.

The weights are common gamma-ratio kernels V_t(Nb/(sqrt(Q_rho)*T)).
To remove their row dependence, insert their Mellin integral on Re z=eta.
The factor (sqrt(Q_rho)*T)^z is independent of b and lies outside the
Dirichlet polynomial absolute value; its modulus is <=(C*X*T^2)^(eta/2).
The remaining column coefficient is (Nb)^(-1/2-eta-it-iy), or its dual
conjugate. Stirling and an entire auxiliary e^(z^2) give an integrable,
rapidly decreasing y-majorant uniform in t after the T normalization.
Cauchy/Minkowski therefore cost only (HT)^O(eta).

This standard reduction can be justified directly by defining
 V_t(x)=(2pi i)^(-1) integral_(eta) e^(z^2)
          Gamma(s+z)/Gamma(s) * T^(-z) * x^(-z) dz/z
(and the conjugate-dual gamma kernel). The 1/z supplies the residue at0.
For the convention gamma_K(s)=2*(2pi)^(-s)*Gamma(s), the exact x is
2pi*Nb/(sqrt(Q_rho)*T); the preceding expressions suppress only this
fixed field constant, absorbed in the cutoff C. Shift the original completed
integral past z=0 and use the primitive functional equation. On every
fixed shifted line, Gamma(s+z)/(Gamma(s)T^z) is bounded by a polynomial
in |y| times exp(C|y|), uniformly in t, so e^(-y^2) dominates. Moving to
large positive real z gives arbitrary inverse powers of x and the stated
uniform cutoff. No root-number independence is assumed; |epsilon_rho|=1
suffices after splitting the two sums. Different S-conductor types do
not change the gamma kernel in the finite-order scope.

Now decompose b=bS*b1*b2, with bS supported in S, b1 squarefree prime to S,
b2 squarefull prime to S and (b1,b2)=1. For each fixed bS,b2, the factors
rho_a(bS) and chi_a0(b2) depend on the row but have modulus<=1. Pull them
outside that b1-polynomial, use Minkowski over bS,b2, and apply section2
to its squarefree b1 columns. The absolute weights have finite sum:
 sum_(bS,b2) N(bS*b2)^(-1/2-eta)<infinity.
This step does not identify bad-prime primitive factors with a product of
zero-extended characters; it only uses the original primitive values as
bounded row multipliers. The b1 cutoffs depending on bS,b2 can be enlarged
to common B' after standard dyadic decomposition; coefficients supported
in the shorter interval are still permitted by the large sieve.

After this reduction, for each fixed a1,a2 the row energy is at most
 (HT)^O(eta) * [M+B'+(MB')^(2/3)], M=X/Na1.
The squarefree coefficient norm sum (Nb1)^(-1-2eta) is bounded by zeta_K(1+2eta),
independent of B'. Restricted row subsets are harmless. Apply the same
bound to conjugate characters/coefficient sequences for the dual polynomial.

## 4. Sum the squarefull parameters

For squarefull ideals c, sum (Nc)^(-s) converges for s>1/2, and
 #{c squarefull:Nc<=X}<<X^(1/2). One elementary proof writes c=d^2*e^3
with e squarefree and bounds by zeta_K(3/2)*X^(1/2).
Consequently summing the preceding estimate over a1 gives

 (HT)^O(eta) * [ X + B'*X^(1/2) + (X*B')^(2/3) ]
 <<(HT)^O(eta) * X*T,

since sum_a1 Na1^-1 and sum_a1 Na1^(-2/3) converge and T>=1.
Summing a2 with X=H/(Na2)^6 uses zeta_K(6), giving
 sum_(a in I(S),Na<=H)|L(1/2+it,rho_a)|^2
   <<_(xi,S,epsilon) H^(1+epsilon)T^(1+epsilon).
Choose every internal eta small enough for the requested epsilon.

Primitive principal rows cause no difficulty: their count is O(H), and
|zeta_K(1/2+it)|^2<<epsilon T^(1+epsilon) by ordinary scalar convexity.
They were not subjected to a pole-free AFE. This completes the central fixed-twist proof. Independent review checked
the explicit AFE uniformity, common cutoffs and primitive-mask reduction.

## 5. Off-central extension without another AFE

Assume the SAME finite primitive family has central energy
 <<H^(1+epsilon0)(1+|v|)^(1+epsilon0), choose 0<epsilon0<1/2.
For each nonprincipal member define
 F_rho(s)=L(s,rho)/(s+1)^(5/4),
using the principal logarithm, holomorphic for Re(s)>=1/2. For a principal
member additionally multiply by (s-1)/(s+1), removing its pole.
Ordinary degree2 convexity, with its individual fixed conductor, makes F
bounded, continuous on the closed half-plane and tending to0 at infinity.
Its real/imaginary parts have the Poisson representation; Jensen gives

 |F_rho(1/2+delta+it)|^2
 <= integral_R P_delta(t-v)|F_rho(1/2+iv)|^2 dv,
 P_delta(y)=delta/(pi*(delta^2+y^2)).

The principal pole-removal factor has boundary modulus<=1. Summing exact
rows and using the central input yields
 <<H^(1+epsilon0) integral P_delta(t-v)(1+|v|)^(-alpha)dv,
 alpha=3/2-epsilon0 in(1,2).
For t>=2 split |v-t|<=|t|/2 and its complement. In the first region the
weight is <<(1+|t|)^(-alpha) and P has mass1. In the complement P is
<<delta*(1+|t|)^(-2), while the weight is integrable; since alpha<2 this
is again <<(1+|t|)^(-alpha). Bounded t is immediate. Negative t follows
by symmetry. Hence P_delta*w_alpha<<_(delta,alpha)w_alpha.

Multiplying by |1/2+delta+it+1|^(5/2) restores the target T^(1+epsilon0).
For principal rows the inverse pole-removal ratio is uniformly bounded
by C_delta because 0<delta<1/2 fixes distance to the vertical line through1.
This proves off-central AFM from the same-family central input without
assuming anything about zeros. Combine sections1--4 for the literal rows.

An explicit transfer constant is available. If epsilon0 in(0,1/4], then
alpha=3/2-epsilon0 lies in[5/4,3/2). For |t|>=2 the near contribution is
<=2^alpha*w_alpha(t); the far contribution is
<=2*delta*3^alpha/[pi*(alpha-1)]*w_alpha(t). For bounded |t|<=2 it is
<=3^alpha*w_alpha(t). Since delta<1/2, pi>3, 2^alpha<3, 3^alpha<6 and
alpha-1>=1/4, the Poisson convolution is <=11*w_alpha uniformly.
Also |3/2+iv|>=2^(-1/2)*(1+|v|), so the boundary denominator costs
2^(5/4)<3; |3/2+delta+it|<2*(1+|t|) costs2^(5/2)<6.
Thus if the central moment constant is C0, an admissible off-central
constant is
 200*C0*((3/2+delta)/(1/2-delta))^2.
This includes all principal rows. The bound is uniform as delta decreases
to0 but not as the contour approaches the pole line sigma=1.

## Boundaries and exact next step

The AFE reduction and primitive-mask bookkeeping were independently
accepted in adversarial-afm-review-20261104.md. The result supplies AFM
only. Combining it with the previously conditional transfer proves the
residual bound below; the actual
short term, principal residue and signed II-I covariance remain separate.
No new zero-free region, positive determinant, Artin holomorphy or GRH
claim follows. All analytic statements here are prose, not new Lean proofs.

Primary pins: BGL1112.1650v1, Section2 Lemma2.1, Thm1.3, AppendixII and
Section5 proof ofCor1.4; GZ2201.01885v2 Lemma2.9 and Section3.2.
Own proofs above adapt the large-sieve input; they do not quote or claim
that BGL's corollary directly includes arbitrary fixed nu.


## Review corrections and finite checks

The initial displayed weight omitted the necessary1/z. It is now dz/z,
which supplies the central-value residue; uniform line bounds remain valid
because Re z=eta>0. The exact2pi scaling of x is also stated rather than
silently identifying it with the conductor normalization. Independent review
requested that the AppendixII decomposition be fixed globally before using
primitive-character uniqueness outside a finite set; this is now explicit.
These corrections change the presentation of the AFE/identification, not a
claim that a failed version was already certified.

Executed afm-20261104-checks.py (stdlib Fraction, no production imports):
96valuation/support decompositions,94squarefull-coordinate decompositions,
7height-exponent comparisons,15Poisson integer-envelope cases and a fixed
S-smooth geometric-series comparison all pass. A T<1 exponent negative
control is retained; the theorem uses T=1+|t|>=1. The source-hashed report is
outputs/checks/2026-11-04-validated-oracle/arithmetic/afm-20261104-finite-checks.json.
These are consistency checks, not a formal proof of AFM/CFT/AFE or GRH.


## 6. Consequence for the exact masked type-I remainder

Combining AFM above with the proved transfer in
weighted-mellin-transfer-20261104.md, using the exact E_u, W, beta_U,
primitive psi_u, independently primitive psi_(u,2) and complete deleted
T(u,d) defined there, gives for 0<delta<1/2 and U^2<=D:

 sum_(0<Nu<=H) |E_u|^2
   <<_(delta,nu,S,epsilon) M4(W)^2 * D^(2delta)
                          * U^(2-4delta) * H * (HD)^epsilon.

This residual estimate is now unconditional relative to the ordinary
classical theorems named above; the AFM hypothesis of that earlier note
has been discharged for the specified original finite-order nu family.
Every conductor-drop correction remains inside the identity before
bounded inequalities are applied. This result does not bound the extracted
principal residue, original short term or signed II-I covariance.
For U=D^a with fixed a>0, its exponent excess at H=D^(3/4) is
2delta+(2-4delta)*a. Letting delta decrease to zero leaves2a, so the
fixed positive-power cutoff obstruction survives. At fixed U one may
choose delta for a requested epsilon to control this remainder alone.
This is not MS_(3/4), an arithmetic positive determinant, or GRH.

The next concrete claim is a second moment for the complete d-weighted
numerator sum before applying Minkowski to the d rows, retaining the
original beta_U, nu(d), chi_d(u), square-denominator/Euler mask and all
primitive conductor drops; alternatively prove sufficient signed II-I
covariance cancellation. Repeating the unweighted numerator AFM no longer
addresses the remaining cutoff gap.

## 7. External dependencies, evidence and scope ledger

- Abelian Kummer/Artin identification, tame local inertia, finite S-unit
  quotient and uniqueness of Hecke/Artin characters outside a finite set.
- The ordinary primitive Hecke functional equation/analytic continuation,
  uniform Stirling bounds on the stated fixed vertical lines, and scalar
  Dedekind-zeta convexity for the separately treated principal rows.
- Blomer-Goldmakher-Louvel, arXiv:1112.1650v1,
  https://arxiv.org/pdf/1112.1650v1, Thm1.3; Lemma2.1; AppendixII;
  Section5 provides the source method for the explicitly redone AFE proof.
  No assertion that its corollary directly covers arbitrary fixed nu is used.
- Gao-Zhao arXiv:2201.01885v2,
  https://arxiv.org/pdf/2201.01885v2, Lemma2.9 and Section3.2 serve only
  as comparison references. No GRH-conditional density theorem is invoked.

Independent review: adversarial-afm-review-20261104.md. Executable exact
finite checks: afm-20261104-checks.py; source-hashed output
outputs/checks/2026-11-04-validated-oracle/arithmetic/afm-20261104-finite-checks.json.
These check finite bookkeeping and constants, not the external theorems.
No new Lean declarations were made. The independent reviewer also accepted
a separately written fixed-unitary-infinity-type extension; it is stored in
afm-20261104-fixed-unitary-extension.md and does not silently enlarge the
finite-order theorem in this note. Constants in that extension depend on
fixed nu, with no conductor or infinity-type uniformity in nu.
