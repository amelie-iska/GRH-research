# Independent adaptive-readout acceptance

Accepted on 2026-11-05 within the finite scope below. All project work and
review artifacts were performed over SSH on iska-linux-vscode in this
repository. Production code, preserved final-v5 labels, previous experiments,
environments and dependencies were not edited by this reviewer.

The final producer is examples/analytic_oracle/adaptive_readout.py, SHA-256
dc64e37cdadac8ffadaa666cdd0e6a0941580f89f3674817c803e8c89ee7e274.
Accepted experiments are 2026-11-05-adaptive-readout-1e-12-v3 and
2026-11-05-adaptive-readout-1e-15-v3. Their source snapshots are byte-identical
to the reviewed live sources. The exact receipt is
outputs/checks/2026-11-05-adaptive-readout/review/final-acceptance.json.

## Mathematics and object certified

For fixed conductors 3, 4 and 5, all 64 preserved circle labels are used.
The actual polynomial is
P(s) = sum b_n^k ((s-1/2)/(6/5))^n on |s-1/2| <= 7/10.
It is the literal exact-rational GD trajectory for
J(b)=1/2 sum |b_n-t_n|^2, with rational rectangle-midpoint Fourier targets,
zero initialization and step 1/4. Its real Euclidean gradient is b-t.
The true-root label least-squares gradient is b-b*; their difference is
t-b*, bounded coordinatewise by the rectangle L1 radii. These are different
objectives and optimizer trajectories. The production proof makes this
distinction explicitly.

Cauchy and exact root orthogonality yield the alias term
M w/(1-w) sum v^n and Taylor term M v^(d+1)/(1-v),
where u=7/12, v=7/24, w=2^-64, and M=4,10,6.
Label uncertainty contributes eta sum u^n. Rectangle midpoint displacement
contributes sum e_n u^n; executed optimization contributes
sum |b_n^k-t_n|_1 u^n. Their exact sum bounds the uniform error.
The code uses the conservative whole rectangle-radius term, without claiming
a sharper factor from the contraction.

All 64 base budgets are scanned. The first degree with strict budget slack
is selected, and the first iterate whose optimization residual fits that
slack is returned. Every request at or below the exact minimum base budget
is refused. Approximate floors are 7.29285359e-17, 1.73697600e-16 and
3.37409122e-16, attained at degrees 56, 56 and 55. These are floors of this
certificate majorant, not lower bounds on actual approximation errors.
The strict slack condition proves finite termination by geometric decay.

## Evidence

check_adaptive_independent.py imports no producer or dyadic helper
arithmetic. It rebuilds outward integer rectangle operations and all 192
Fourier rectangles, reconstructs all 192 degree-base budgets using exact
Fractions, and checks the complete six-model JSON records. All 666 vector
updates and 18,802 stored complex coefficient pairs pass exact recurrence,
objective, residual, first-stop, minimum-degree, minimum-floor and five-term
sum checks. The final report is:

outputs/checks/2026-11-05-adaptive-readout/review/independent-exact-1793878787336531027.json

Existing mpmath 1.4.1 in the approved tokengt environment, at 110 decimal
digits, independently contains all 166 selected true-root DFT coefficients
in their exported rectangles. All 288 compact-boundary comparisons lie
inside the certificates. These are numerical diagnostics, not proof of a
uniform bound. The exact interval/analytic argument supplies that bound.

check_guards_independent.py passes 68 negative controls, including 12
mutations of objectives, iterates, total bounds, component budgets, degree,
stopping count, normalization, DFT rectangles, floors, degree scans and
provenance hashes. It also checks malformed inputs, primed-cache types,
immutable cached intervals, supplied-label/hash tampering, simulated source
drift, refusal without artifacts, and unchanged existing output hashes.
Requests only 1e-80 above each independently recomputed floor terminate
correctly (639/641/641 steps). The request 3.4e-16 passes for all conductors
(degrees 30/31/34; steps 126/130/144). The final report is:

outputs/checks/2026-11-05-adaptive-readout/review/independent-guards-1793878793049647292.json

The seven focused producer unit tests pass. Production TeX was read in full:
papers/adaptive-readout-core.tex and
papers/adaptive-readout-details.tex agree with the reviewed code and exact
budget semantics; their hashes are in the acceptance receipt.

## Corrections and limits

Review found and the author fixed three concrete public-API issues:
mutable cached Fourier rectangles could corrupt later certification;
a huge exact rational's optional float display could overflow; and a valid
generator of targets was consumed by validation and silently trained an
empty vector. The final source returns immutable cached rectangles, handles
display overflow without changing exact endpoints, and explicitly rejects
non-list/tuple targets. Regression controls pass.

This review reuses the independently accepted final-v5 primitive
theta/Mellin, growth and sample-enclosure arguments; it does not re-prove
their external classical analytic inputs. The 192 source labels and their
source hashes remain pinned. This is a bounded fixed-label interface,
with fixed analytic tails, primitive series and interval precision.
It does not supply arbitrary requested-accuracy theta sampling, an exact
ideal-root LS training trajectory, neural/quantum training, quantum
advantage, zero-location results, a positive arithmetic determinant, a new
Lean declaration or a GRH proof. The runtime and informal argument remain
outside a proof-assistant kernel. No unresolved correctness defect remains
in the reviewed finite producer/proof/certificate scope.
