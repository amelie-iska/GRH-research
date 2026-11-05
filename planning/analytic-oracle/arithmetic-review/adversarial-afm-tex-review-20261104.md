# Independent literal-TeX AFM review, 4 November 2026

Verdict: accepted at the source hashes in the accompanying review receipt.
I read both complete fragments against the accepted derivation and the
independently checked primary BGL input. No load-bearing mathematical
correction was found. Compilation/layout are assigned to the parent and
are not certified by this mathematical review.

## Exact hypotheses and family comparison

The core initially fixes a finite-order Hecke character, Kummer characters
over the Eisenstein field, S containing the conductor and primes above6,
and all actual nonzero element rows, including units and S-prime powers.
The separate fixed-unitary assertion explicitly declares nonuniformity in
the infinity type/conductor and does not silently alter the finite-order
type-I residue formula.

The details give a fixed global AppendixII decomposition before primitive
character uniqueness, the S-unit quotient comparison, and the factor6
literal-element multiplicity. The S-supported norm sum converges. The
squarefree large sieve is applied only to its canonical family; fixed xi
and canonical a1 are column multipliers, respectively of modulus1 and at
most1. No claim that arbitrary nu belongs to BGL's ray-class set appears.

## Conductors, common weights and all-ideal sums

The unique a0*a1*a2^6 decomposition, tame inertia orders, exact outside-S
radical and finite S-conductor possibilities are stated. At bad columns,
the actual primitive rho_a(bS) remains a bounded row multiplier.
Coprimality/cutoff conditions belong to the fixed column sequence; padding
uses zeros, not a pointwise monotonicity assertion for a complex sum.

The displayed kernel includes dz/z and exact
x=2*pi*Nb/(sqrt(Qrho)*T). The normalized gamma ratio cancels the artificial
T in x, and the stated uniformly integrable Gaussian majorant is valid.
The common cutoff has a negligible absolute ideal-counting tail after a
sufficiently large positive kernel shift. Summability of S-supported and
squarefull columns, squarefull row counting, the two convergent squarefull
series, and the a2 exponent6 sum reproduce the accepted moment bound.
Principal rows are excluded from the pole-free AFE.

## Poisson and fixed-unitary extension

The correct pole-removal factor and holomorphic denominator are present.
The Poisson proof treats the fixed-H row family as finite, uses the
integrable weight with exponent in[5/4,3/2), and derives the advertised
constant200 from 11*3*6<200. The contour excludes the principal pole line.

For fixed-unitary nu, the explicit ideal convention is
nu(a)=nu0(a)*(Na)^(-i*tau), giving zeta_K(s+i*tau) on pure norm rows.
The common gamma shift, dual vertical sign, fixed-nu comparison of Tnu
with T, and shifted pole-removal factor are all consistent. The same
numerical transfer factor is relative to the nu-dependent central
constant, without claiming uniformity in nu.

## Exact masked remainder and limitations

The independently primitive square and full T(u,d) Euler mask are retained.
The local examples at valuations3 and6, with norm7, have the correct
primitive/restoration ratios. The finite-order residue and the retained
beta_U(d), nu(d), chi_d(u) expression have the correct D normalization.
The reciprocal incomplete Euler product is bounded only in absolute
convergence at2sigma>1, so no critical-strip zero hypothesis is used.
The actual truncated coefficient sum and four Mellin integrations give
the stated D^(2delta) U^(2-4delta) H(HD)^epsilon envelope.

The fragments explicitly retain the positive cutoff loss, extracted
residue, short-scale term, signed covariance, contour uniformities and
determinant/zero-location obligations. They do not infer a lower bound
from an upper-bound limitation or conflate Dirichlet/Hecke/Artin scopes.
They explicitly say that no new Lean declarations prove these analytic
moment estimates.

## Nonblocking exposition notes

The symbol eta is reused for a finite S-unit character and a later small
positive Mellin exponent. Their roles are distinguished by context;
different symbols would improve reading. In the details' AFE paragraph,
"two Dirichlet polynomials with smooth weights" precedes the explicit
truncation; "two weighted Dirichlet series, then truncated polynomials"
would be more literal. Neither affects the estimates or this acceptance.

Post-read clarification: the author explicitly restricted the moving cutoff
U=D^a to 0<a<=1/2, as required by U^2<=D. This clarification was checked
and accepted; the receipt hashes were updated to those exact sources.

## Final v5 hash addendum

The final-v5 build record was read and its two AFM source hashes match the
live fragments. Reversing only the two recorded AFM editorial replacements
reproduces both previously reviewed SHA-256 hashes exactly. Thus there is
no unreviewed mathematical change. The explicit 0<a<=1/2 restriction is
present in the core moving-cutoff paragraph. The details retains "fixed
a>0" under the already imposed U^2<=D hypothesis; its upper restriction is
implicit rather than printed a second time. That exposition difference
does not change the theorem or this acceptance.

Final accepted core SHA-256:
63a6ee49d2dcee3b87977541f90995fa5a9c2d3ad584328ebed5059223cea0ff

Final accepted details SHA-256:
cb5c0f58189a2c5f5b47658902b10026556603281799b94313617bc89804a76c

The final source acceptance and build-record hash are recorded in the
JSON receipt. The parent reports clean five-page and fourteen-page builds;
this addendum certifies the source/review correspondence, rather than
claiming a separate compilation or layout inspection.
