# Independent adaptive-theta review

5 November 2026. This review was performed only over SSH on iska-linux-vscode.
The reviewer wrote only the assigned new review planning/output directories.
Existing producer files, accepted certificates, environments, sources and data
were read and preserved. No package installation, MCP activation, credentials,
GPU job, production integration, publishing or queue mutation was performed.

## Scope and current acceptance

The reviewed sampler provides exact rational point and true-circle-node samples
for the three fixed primitive quadratic completed Dirichlet functions q3/4/5.
It retains the already accepted classical primitive theta/Mellin identity and
elementary Gaussian/Cauchy estimates. No zeros are assumed. The arithmetic and
analytic mechanisms below are accepted at the source snapshots listed in the
exact check receipts. Later source edits require fresh source pins/checks.
An independent review of a downstream full requested-error readout, if supplied,
will be recorded separately. A small sample error alone does not remove the
fixed-node alias floor of an older readout.

The exact-point contract validates the rational coordinates against the closed
domain [-1,2]+i[-4/3,4/3] before interval conversion. The actual point therefore
satisfies the analytic assumptions even when an enclosing dyadic box slightly
overshoots the boundary. The circle wrapper regenerates the true root and point
from pi/exp at every arithmetic retry. It never substitutes a fixed rational
point for the true circle or promises shrinking uncertainty for an arbitrary
fixed nondegenerate input box.

## Interval and tail arguments

Each immutable context carries its own precision. Addition, products, signed
integer division and reciprocal endpoints use outward integer floor/ceiling.
Mixed precisions, floats and bools are rejected, including typed-cache aliases.
Atan uses the signed alternating next term, log uses a nonnegative geometric
series remainder after exact binary range reduction, and exp uses a rational
Taylor tail after halving followed by outward squaring. All series remainders
shrink with precision. The chosen per-series tolerance delta=2^(-p-16) need not
be a total primitive error: Machin weights give at most20delta and logarithm
range weights at most(1+abs(k))delta, in addition to dyadic rounding. The final
observed interval width is the acceptance test.

E(x)=2^(-floor(x)) bounds exp(-x) for x>=0 because e>2. It is nonincreasing,
convergent and deliberately not multiplicative. The code evaluates it at each
actual exponent argument. N starts at1, so delta_q*(N+1)>=6/5 and the omitted-n
geometric denominator is positive. The n tail covers omitted n on the full time
interval; the time tail covers only retained n beyond T. These tails are disjoint.
The dyadic panels cover [1,T]. The accepted Cauchy disk at half the panel center
and the even Taylor remainder give the recorded quadrature bound. The recurrence
agrees with a separate generalized-binomial times exponential convolution.

Every discarded (n,panel) pair is omitted as a whole, with both Mellin powers
bounded by4*h*n^a*(m+h)^2*E(delta_q*n^2*(m-h)). With4JN potential pairs and
threshold eta/(8*4JN), their sum is at most eta/8. Character-zero terms vanish
exactly. The first-success N/J/K searches each allocate eta/8.

The arithmetic search requires the actual complete-sum rectangle L1 halfwidth
at most eta/4. Let B be chosen so5*2^-B<=eta/8. Each of the four analytic and
one arithmetic components is rounded upward to a B-bit dyadic rational. Every
rounding excess is less than2^-B. The literal sum of the five reported components
therefore bounds the error and is at most7eta/8. This gives finite serialized
endpoints without the earlier fixed180-bit floor or huge odd-denominator tails.
All raw analytic terms are recoverable from q,N,J,K and the pinned source;
the raw arithmetic width is separately recorded. Decimal integer chunking
avoids changing Python's global digit-conversion limits and works for tested
15000-bit endpoints.

For fixed finite N/J/K and a fixed true target, all primitive enclosures shrink.
The finite expression uses fixed nonzero integer denominators; continuity and
outward arithmetic imply its width tends to zero. Doubling precision with fresh
point/node enclosures terminates mathematically. This is not a practical bit-
complexity guarantee for extreme tolerance requests.

## Independent evidence so far

-3428 exact primitive/serialization checks at32/80/160/320bits: rational interval
 corners, signed division, independent alternating atan/Machin brackets,
 independently range-reduced logarithms, direct unscaled rational complex-exp
 Taylor brackets, exp(log x) and Euler identities, cache/context guards, and
 independent digit-wise decimal encoding versus chunked encoding for positive
 and negative15000-bit integers. Receipt precision-independent-1793882554218898584.json.
-1151 exact adaptive-parameter/guard checks: all q at eta1e-6/24/32 and17e-31,
 independently reconstructed tails, first-success N/J/K, whole-pair discard sets,
 complete panels, positive denominators and984 recurrence/convolution identities.
 Receipt sampler-independent-1793882557500879489.json.
-142 certificate/secondary diagnostic checks over8 freshly evaluated samples.
 Each q has eta1e-24 and1e-32 samples; q5 includes the exact closed boundary
 point -1+(4/3)i and asymmetric true circle node7/64. Starting from32bits forces
 retries32->64->128 at1e-24 and then256 at1e-32. All exact rounded budgets and
 centers are reconstructed. Existing mpmath1.4.1 at140digits independently
 evaluates completed Dirichlet targets inside every radius. These comparisons
 are diagnostics, not the proof of interval inclusion or uniform error.
 Receipt sample-diagnostics-1793882573719712172.json.
-85 saved-artifact checks over all6 pilot-v2 samples: exact radius components,
 source-copy hashes, centers, true circle root/node boxes and130digit target
 diagnostics. Circle size8, stride4 and evaluated count2 per family agree.
 Receipt saved-samples-2026-11-05-adaptive-theta-pilot-v2-1793882430011933882.json.
-14 source-provenance/output/failure controls, including both imported-module
 snapshot mismatches rejected before creating an output directory. Source change is simulated by a
 read-return patch, never by editing a producer. Drift during a run rejects a
 certificate, failure metadata remains explicitly uncertified, and rerunning an
 existing directory leaves every saved byte unchanged. Receipt
 provenance-independent-1793882554269720920.json.

The receipts are under outputs/checks/2026-11-05-adaptive-theta/review/. The
arithmetic/source snapshots for this check set are:
precision.py 897716c550e96ab667661a4fc89257e6e9fb0b3ffb0fec4b85a3597033cf20bd
adaptive_theta.py 63c1ea69c68c864eaaeeb23b0860dc670d0779d9ea841398fd7f761f3f12b0d4
Module-import source snapshots are compared at run entry and all source bytes
are compared again at successful emission. Historical fixed producers and
certificates retain their accepted original hashes.

The final192-sample artifact is accepted: outputs/experiments/2026-11-05-adaptive-theta-samples-final-v1/. All three conductors use complete64-node circles at
requested1e-32 sample error. All192 exact records, five rounded components,
raw rectangle widths, centers, root/node enclosures, source-copy pins and
130-digit diagnostic targets pass2506 checks. Receipt
saved-samples-2026-11-05-adaptive-theta-samples-final-v1-1793882625279692283.json.
This artifact is a complete sample-circle certificate, not a readout certificate.

## Corrections and practical limits

Review found float0/boolFalse acceptance when reusing a Complex with an explicit
imaginary argument; the author fixed it and regression controls pass. Review
also identified extreme integer serialization failure under Python's standard
digit limit and misleading sparse-sample count metadata. The author introduced
local exact chunked decimal conversion/parser and separate circle-node/evaluated
counts; independent checks pass. The dynamic five-component dyadic rounding
revision is mathematically sound and independently reconstructed.

A deep parameter-only stress run including eta1e-80/200 was stopped after more
than3minutes of CPU inside exact Fraction quadrature-tail summation. Its note
is preserved as deep-tolerance-check-interrupted.txt. No acceptance of those
executions or practical extreme-tolerance runtime is claimed. The finite-search
proof remains separate from performance.

The implementation and proof are outside a Lean kernel. All-conductor results,
unknown zero locations, a positive arithmetic determinant, the signed covariance
bridge, GRH and a quantum/training advantage are not established by this sampler.

## Downstream family acceptance

The separately reviewed end-to-end1e-24 construction is now accepted in
FAMILY_REVIEW.md and final-acceptance.json. That receipt also binds all four
production adaptive-theta/adaptive-family core/details TeX files. It keeps
the sampler-only receipt and this sample-circle acceptance distinct.
