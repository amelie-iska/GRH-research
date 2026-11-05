# AFM mathematical handoff, 2026-11-04

Attempted claim: establish the original-family AFM numerator moment rather
than assume a conductor-counting implication or insert arbitrary nu into
BGL's finite ray-class set. Result: prose proof independently accepted,
with explicit external classical dependencies and no zero hypothesis.

Finite-order theorem: for fixed 0<delta<1/2, epsilon>0, H>=1 and real t,
sum_(0<Nu<=H) |L(1/2+delta+it,primitive(nu*Kummer(u)))|^2
<< H^(1+epsilon)*(1+|t|)^(1+epsilon), constants depending on fixed
nu,S,delta,epsilon. Exact proof is afm-20261104-fixed-twist-final.md.

Derivation: finite S-unit comparison with BGL AppendixII plus six unit
rows per principal ideal; fixed nu incorporated into squarefree columns
without changing their l2 norm; primitive-conductor AFE with common gamma
kernel and common maximal cutoff; S-supported and squarefull columns kept
as bounded primitive row multipliers and summed by Minkowski; all-ideal
squarefull/sixth-power row summation; same-family Poisson transfer off
central line. Principal rows are handled separately. Corrected displayed
kernel has dz/z and exact fixed-field2pi normalization.

Separate fixed-unitary extension is independently accepted in
 afm-20261104-fixed-unitary-extension.md.
It defines nu(a)=nu0(a)*(Na)^(-i*tau), includes angular parameter m,
uses the common shifted gamma factor, and separates pure norm rows with
pole1-i*tau. No uniformity in fixed nu is claimed.

Evidence: independent adversarial-afm-review-20261104.md; exact finite
checker afm-20261104-checks.py passed96valuation/support cases,
94squarefull coordinates,7exponent comparisons,15Poisson envelopes and
an S-smooth product comparison. Its source-hashed JSON is in
outputs/checks/2026-11-04-validated-oracle/arithmetic/.
Checks are not Lean or proofs of external CFT/AFE/large-sieve theorems.

Consequence: the earlier conditional masked residual transfer is now
proved with H exponent1+epsilon, but still costs D^(2delta)U^(2-4delta).
For U=D^a at fixed a>0, delta->0 leaves a 2a exponent loss. Principal
residue, short term, signed II-I covariance, full arithmetic determinant
comparison and GRH remain open. Next claim: bound the original d-weighted
moment before the absolute beta_U sum, or prove signed covariance
cancellation. No production/source/env/model/auth changes or pushes.
