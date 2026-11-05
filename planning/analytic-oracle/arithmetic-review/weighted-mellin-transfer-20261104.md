# Weighted Mellin moment transfer and the remaining cutoff loss

2026-11-04. Focused arithmetic continuation. No source clone, production
script, model, environment or existing result was changed. This note proves
a conditional transfer lemma and identifies a precise primary-literature
interface; it does not prove the original signed short-row estimate or GRH.

## The retained original objects

Use the original K=Q(omega), fixed finite-order nu, excluded ideal set S,
primitive psi_u, independently primitive square psi_(u,2), full deleted set
T(u,d)=S union supp(u) union supp(d), and actual beta_U from
research/hecke-type-i.md. All nonzero Eisenstein elements with Nu<=H are
rows; no division by units or replacement with arbitrary primitive characters
is made. Write sigma=1/2+delta, 0<delta<1/2, U^2<=D and W supported in[1,2].
After shifting the already recorded type-I contour and extracting its
principal residue P_u, the exact remainder is

 E_u = D^delta/(2pi) integral_R W_hat(sigma+it) D^(it)
       sum_d beta_U(d)nu(d)chi_d(u) (Nd)^(-sigma-it)
       F_(u,d)(sigma+it) dt.

The finite d sum, every original zero, and both conductor-drop corrections
remain inside this identity. The short2a_U term and typeII are separate.

## A precise average input

For the SAME primitive characters, require the fixed-target estimate

 (AFM) sum_(0<Nu<=H) |L(sigma+it,psi_u)|^2
       <= C_(delta,nu,S,epsilon) H^(1+epsilon)(1+|t|)^(1+epsilon),

uniformly in H>=1 and t real. This is a numerator second moment, not a
reciprocal-L moment or a zero-free hypothesis. It does not include a profile
supremum. Principal rows are permitted because this contour misses s=1.
It must be proved for the actual Kummer identification, rather than inferred
from Q_u<<Nu or from all primitive characters of similar conductor.

## Proved conditional transfer lemma

Assuming AFM, the exact original type-I remainder obeys

 sum_(0<Nu<=H)|E_u|^2
   << M4(W)^2 D^(2delta) U^(2-4delta) H (HD)^epsilon.       (T)

All constants may depend on fixed delta, nu, S and epsilon.

Proof. For arbitrary small eta>0, the full-mask Euler ratio proved in the
existing note gives

 |F_(u,d)(sigma+it)| <= C_(delta,eta,nu,S)
                      (Nu Nd)^eta |L(sigma+it,psi_u)|.

The inverse independently-squared L-function, together with its SAME deleted
set, is an inverse incomplete Euler product on Re(2s)>1 and is bounded by
zeta_K(2sigma). The remaining finite numerator is at most a constant times
(N rad T)^eta. This is an upper bound after keeping the exact mask, not an
identity deleting original zeros.

Apply Minkowski to the finite d sum and Mellin integral in l2 of the actual
rows, use |nu(d)chi_d(u)|<=1, then AFM. This bounds ||E||_2 by

 C D^delta H^(1/2+epsilon)
 [sum_d |beta_U(d)|/(Nd)^(sigma-eta)]
 integral_R |W_hat(sigma+it)|(1+|t|)^((1+epsilon)/2) dt.

The actual truncated divisor convolution satisfies

 sum_d |beta_U(d)|/(Nd)^(sigma-eta)
 <= [sum_(Na<=U)(Na)^(-sigma+eta)]^2
 << U^(1-2delta+2eta).

Four integrations by parts bound the last integral by C M4(W), after
choosing internal losses small. Squaring and absorbing losses using U^2<=D
proves T. No interchange of profile supremum and energy is used.

## What T improves, and what it does not

The old pointwise-convexity route gave H^(3/2-delta+epsilon). AFM replaces
that by H^(1+epsilon). At H=D^(3/4), U=D^a, the old upper-envelope excess over
H was 3/8+5delta/4+(2-4delta)a; T has excess

       2delta+(2-4delta)a.

The formal gain is 3/8-3delta/4>0. It is an improvement of a proved
CONDITIONAL upper bound, not an energy lower bound. At any fixed a>0,
letting delta decrease to zero still leaves 2a. Thus even a Lindelof-on-average
numerator estimate does not by itself give the required all-epsilon bound
at a fixed positive-power cutoff after this absolute d sum. At fixed U,
delta can be chosen for a requested epsilon and the residue-subtracted
type-I remainder would satisfy H(HD)^epsilon. This neither controls P_u nor
reassembles II-I and the short term. It must not be promoted to MS_(3/4).

## Primary-literature interface, with exact boundaries

1. Blomer, Goldmakher, Louvel, arXiv:1112.1650v1, Theorem1.3 and
   Corollary1.4; Section5, equation(5.1) and its proof.
   https://arxiv.org/pdf/1112.1650v1
   The large sieve concerns their specified nth-order Hecke family on
   squarefree ideals, not all primitive characters. Corollary1.4 itself
   sums over all ideals in I(S), including nonsquarefree ones, and in degree2
   has H^(1+epsilon)(1+|t|)^(1+epsilon) size on the central line.
   Their AppendixII specifies the Artin-residue-symbol normalization.

2. Gao, Zhao, arXiv:2201.01885v2, Section2.8 Lemma2.9 and Section3.2
   equations(3.5)-(3.6).
   https://arxiv.org/pdf/2201.01885v2
   Their sextic specialization retains finite ray-class twists and handles
   valuation decomposition. Their central-density theorem assumes GRH;
   the large-sieve/numerator-moment inputs cited here do not use that theorem.

The relevant new lead is the ALL-IDEAL scope of BGL Corollary1.4. It makes
canonical-family nonsquarefree row multiplicity a theorem already available,
rather than another free conductor-counting assumption. It does not
automatically identify every psi_u in the project with that canonical family.

A concrete route to the missing identification is to write (u) as an
S-supported ideal times an ideal a prime to S. BGL's canonical Artin
character for a differs from the literal Kummer character of u by a class
in O_S^*/(O_S^*)^6, a finite group. One must write this comparison, its
unit/ray normalizations and every fixed nu twist explicitly. Fixed nu need
not have order dividing6, so it must not simply be declared a member of
BGL's finite character group Rc. Its fixed conductor may be absorbed in an
AFE/large-sieve proof only after redoing that proof, with the actual
primitive masks and all-ideal parameter decomposition. Extension from the
central line to sigma>1/2 likewise needs a uniform AFE or Poisson/strip
argument, not an unexplained substitution in a central-value theorem.
Those two interfaces have NOT been claimed proved by this short note.

## Exact next claim

Prove AFM for the actual primitive nu*Kummer(u) family by an explicit finite
S-unit/ray comparison and fixed-twist AFE argument, preserving unit rows,
S-prime powers, conductor drops and primitive L-function conventions.
If that succeeds, record T as a genuine new residual bound. Then attack the
d-weighted moment BEFORE taking the absolute beta_U sum, or the signed
II-I covariance; the remaining U^(2-4delta) loss shows why numerator
Lindelof-on-average alone is insufficient. No new zero-free region or
positive arithmetic determinant identity has been obtained.
