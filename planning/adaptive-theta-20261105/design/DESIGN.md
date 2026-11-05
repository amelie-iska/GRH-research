# Adaptive theta parameters and finite-precision termination

5 November 2026. Design and proof artifacts prepared only through SSH on
`iska-linux-vscode`, in `/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104`.
The new namespaces are `planning/adaptive-theta-20261105/design/` and
`outputs/checks/2026-11-05-adaptive-theta/design/`. This document specifies a
proposed adaptive extension; it does not itself claim that an implementation
has passed independent acceptance. Existing fixed producers, final-v5 labels,
final-v3 readouts, queues, environments, and publication targets are unchanged.

## Mathematical contract and provenance

An exact positive rational sample error `eta`, fixed integer conductor
`q in {3,4,5}`, and an exact rational complex point in
`D=[-1,2]+i[-4/3,4/3]` determine a finite certified sample. A circle-node
entry point may instead regenerate the enclosures of
`s_j=1/2+(6/5)exp(2*pi*i*j/m)` and its true root at each working precision.
The root/node uncertainty then belongs to the same interval-arithmetic term.
No fixed nondegenerate input rectangle is promised arbitrarily small output:
its mathematical input uncertainty need not vanish as arithmetic improves.

Characters and parities are exactly
`chi3=(0,1,-1),a3=1; chi4=(0,1,0,-1),a4=1; chi5=(0,1,-1,-1,1),a5=0`.
The primitive theta/Mellin transformation is the existing explicitly stated
classical input. Its Gauss sums are `i*sqrt(3),2i,sqrt(5)`, giving root number
one. Thus, putting `lambda_n=pi*n^2/q`,

`Lambda_q(s)=sum_{n>=1} chi_q(n)n^a integral_1^infinity exp(-lambda_n*t)
 [t^((s+a)/2-1)+t^((1-s+a)/2-1)]dt`.

The accepted proof and implementation are `papers/validated-oracle-{core,details}.tex`
and `examples/analytic_oracle/{theta_oracle,dyadic}.py`. The latter files have
SHA256 `c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1`
and `82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170`.
The final-v5 certificate is pinned by
`85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8`.
The requested-readout proof/design/review and current MASTER/CONTINUATION
were read. Their next analytic task is exactly adaptive tails and precision;
the independent arithmetic bridge remains open. The parameter checker hashes
all these inputs and uses Python standard-library exact fractions only.

## An inexpensive exponential upper bound

For exact `x>=0`, define `E(x)=2^(-floor(x))`. Since `e>2`,

`exp(-x) <= exp(-floor(x)) <= 2^(-floor(x)) = E(x)`.

`E` is nonincreasing, exact rational, and tends to zero. Also
`E(x) <= 2 exp(-(log 2)x)`. Its jumps cause no difficulty: each true
exponential in a proved majorant is replaced separately by its upper bound.
**No multiplicativity, differentiation, or integral identity for E is used.**
In particular `E(x)=1` on `[0,1)`. A geometric denominator must therefore
not be used with `x<1`. Set `N>=1`, `n0=N+1>=2`; then
`delta*n0 >=6/5`, where `delta=3/q`, and `1-E(delta*n0)>0` in all families.
All E calls below have nonnegative rational arguments; whole-panel left
endpoints are at least one and Cauchy radii use positive half-midpoints.

The old growth constants `M3=4,M4=10,M5=6` have an independent accepted
`U16` derivation. They remain available to a later readout and are not
recomputed by simply replacing `U16` with E: E is looser near zero and an
old strict integer comparison need not survive that substitution.

## Exact analytic budgets and finite search

On D both Mellin powers satisfy `abs(Re p)<=2`, `abs(Im p)<=2/3`.
Let `Q(x)=1/x+2/x^2+2/x^3`, `C0=1`, `C1=(1+1/delta)/2`.
For `N>=1`, the omitted-n budget is

`B_n=2 C_a Q(delta*n0^2) E(delta*n0^2/2)/(1-E(delta*n0))`.

To verify it, integration by parts gives
`integral_1^infinity t^2 exp(-x*t)dt=exp(-x)Q(x)`.
For a=0, `n^a exp(-delta*n^2/2)<=1`. For a=1, use
`n <=(1+n^2)/2` and
`n^2 exp(-delta*n^2/2)<=2/(e*delta)<=1/delta`; hence the same expression
is at most C1. Split the Gaussian into two halves, use decreasing Q, and
`(n0+j)^2>=n0^2+2*n0*j`. Sum the resulting *true* exponential geometric
series, then replace its numerator and ratio by E. Both substitutions
increase the positive fraction; its new denominator is positive as above.

For `J>=1`, `T=2^J`, the retained-n time budget is

`B_t=sum_{n=1}^N 2 n^a T^3 E(delta*n^2*T) Q(delta*n^2*T)`.

Substitute `t=T*u` in each tail, use `t^Re(p)<=t^2`, integrate u^2, then
replace the true exponential by E. Omitted n already use the full integral;
retained n use only t>T, so these tails do not overlap.

For each j=0,...,J-1 take four panels
`m=2^j(1+(2*ell+1)/8), h=2^j/8`, `ell=0,...,3`.
They cover `[1,T]` without gaps. With `rho=m/2`, `v=h/rho<=2/9`, put
`B(m)=max((m+rho)^2,(m-rho)^(-2),1)`. The quadrature budget is

`B_Q=sum_panels sum_{n=1}^N
 [2*n^a*2*h*3*B(m)*E(delta*n^2*m/2)*v^(2K+2)
 /((2K+3)*(1-v^2))]`.

This retains the accepted Cauchy proof: principal log is analytic on the
rho disk, `Re z>=m/2`, `abs(arg z)<=1`, and the angular multiplier is at
most `exp(2/3)<=3`. Cauchy's coefficient estimate, odd-power cancellation,
and a geometric sum give the displayed remainder after degree 2K.
The leading factor two covers both Mellin powers. Including n with zero
character and terms later discarded only increases this budget.

Select N as the first integer >=1 with `B_n<=eta/8`; for that N select J
as the first integer >=1 with `B_t<=eta/8`; for that N,J select K as the
first integer >=0 with `B_Q<=eta/8`. All comparisons use exact rationals.
The searches terminate: the Gaussian bound makes B_n tend to zero; for
fixed finite N, exponential decay beats T^3 as J increases; for fixed N,J,
every v is at most 2/9 so B_Q tends geometrically to zero as K increases.
No assumption on the zeros, sign of the character sum, or GRH is used.

For asymptotic size, with fixed q and `L=max(1,log(1/eta))`, one may choose
`N=O(sqrt(L))`, `T=O(L)`, `J=O(log L)`, `K=O(L)` as eta tends to zero.
For the time estimate, replace `Q(delta*n^2*T)` by its value at delta*T
and `E(delta*n^2*T)` by E(delta*T): the remaining sum n^a is polynomial
in N, so `T=C L` with sufficiently large constant dominates its logarithm
and the T polynomial. For quadrature, the sum of the pre-geometric factors
is at most a polynomial in N,T,J; its logarithm is O(log L), absorbed by
K=O(L). These rates describe finite truncation work, not a bit-complexity
claim for exact rational arithmetic or a bound on every precision retry.

## Whole-pair discards and total sample error

There are `P=4JN` potential (n,panel) pairs, including zero-character ones.
An identically zero character contributes exactly zero and needs no budget.
For any other pair, bound its **entire** contribution of both Mellin powers by

`b(n,m,h)=4*h*n^a*(m+h)^2*E(delta*n^2*(m-h))`.

For real t>=1 its t phase has modulus one and `t^Re(p)<=(m+h)^2`;
positivity and the panel length 2h prove the bound. Skip only when
`b<=eta/(8P)` and add that exact b to `B_discard`. Therefore
`B_discard<=eta/8`. This step precedes evaluation of exponential times
large recurrence coefficients, avoiding an amplified fixed absolute error.
It is a rigorously bounded truncation, not numerical underflow.

For all active pairs use the accepted recurrence, `u=h/m`,
`r_-1=0,r_0=1`,

`r_(j+1)=[u*(p-lambda*m-j)*r_j-lambda*m*u^2*r_(j-1)]/(j+1)`.

The integrated polynomial is
`2*h*exp(p*log(m)-lambda*m)*sum_{j=0}^K r_(2j)/(2j+1)`.
Matching coefficients in `t f'=(-lambda*t+p)f` proves the recurrence.
Multiply by the signed character weight n^a and add both powers outward.
Let the resulting rectangular sum have exact rational midpoint y and
L1 coordinate halfwidth R_arith. Accept only if `R_arith<=eta/4`. The raw
sample error is therefore at most

`R_raw=R_arith+B_n+B_t+B_Q+B_discard<=3*eta/4`.

The interval term includes pi/log/exp approximation, node uncertainty when
applicable, recurrence propagation, and every outward rounding operation.
This is the raw inclusion inequality. The implementation uses the stricter
acceptance and dynamic serialization procedure below. If a consumer wants
finite-precision decimal values instead of exact endpoints, it needs a
separate conversion-error bound.

## Dynamic exact serialization

Raw tails can have enormous exact rational denominators even when their
numerical sizes are negligible. The implementation retains them internally
and chooses an output dyadic scale B depending on eta. It initializes
`B=max(32,bit_length(eta.denominator)-bit_length(eta.numerator)+8)` and
increments B until `5*2^(-B)<=eta/8`. This finite search always terminates.
Define `up_B(x)=ceil(2^B*x)/2^B` by exact integer arithmetic. Apply this to
**each of the five components**, including the successful raw interval
radius, and serialize the rounded components. The reported sample radius
is literally their exact sum, rather than a separately rounded sum.
Since `0<=up_B(x)-x<2^(-B)`,

`R_reported=sum_components up_B(component)
 <=3*eta/4+5*2^(-B)<=7*eta/8<eta`.

Every rounded component dominates its raw mathematical bound, so this
additional rounding preserves inclusion. The output stores B, the raw
interval radius and its complete rectangle, N/J/K, the discard threshold
and pair counts, exact point/node metadata, and source hashes. From these,
the raw analytic bounds and the complete active/discarded pair sets are
recomputed exactly; huge raw tail fractions need not be serialized.
The exact parameter checker below independently verifies these rounded
bounds at the practical requests. For fixed q, B=O(max(1,log(1/eta))) as
eta tends to zero. It replaces the inherited fixed180-bit floor.

This serialization specification concerns exact mathematical integers and
rationals. The practical output avoids the Python decimal conversion limit
encountered by a pilot's huge raw-tail denominators; exceptionally large
requests or endpoints still require an exact integer encoder supporting
their digit count. This is distinct from the finite mathematical precision
and truncation termination argument.

## Variable primitives and precision termination

Use an isolated precision context p; never change a global scale during an
expression or reuse a cached interval from another p. Reject floats, bools,
unsupported q and nonpositive eta before any typed cache can bypass a guard.
Real endpoints are integers scaled by `2^-p`; the accepted floor/ceiling
addition, multiplication, division and complex rectangle rules apply unchanged.
Their rounding width tends to zero as p tends to infinity.

The primitive series truncations must also vary. One concrete sufficient
rule sets `delta_p=2^(-p-16)` and uses the following **per-series** bounds:

* Machin pi: choose each arctangent length independently until its
  alternating next-term bound is <=delta_p. The weighted analytic tail
  widths are therefore <=`16*delta_p+4*delta_p=20*delta_p`, before
  additional outward dyadic rounding. Lengths are O(p).
* Rational positive logarithm: range-reduce `x=2^k v`, `1<=v<2`, and choose
  the existing nonnegative log-series tails for log(v) and log(2)
  independently <=delta_p. Their combined analytic remainder is bounded
  by `(1+abs(k))*delta_p`, before outward rounding. For fixed x the lengths
  are O(p); sign-aware multiplication handles negative k.
* Complex exponential: halve to interval L1 bound A<=1/2, choose H with
  `A^(H+1)/(H+1)!/(1-A/(H+2))<=delta_p`, add a symmetric enclosure to
  **both** coordinates, and square outward. The denominator is positive.
  A search over H terminates; for bounded fixed A one may take H=O(p).

Choosing a remainder only proportional to the final absolute eta is not a
substitute for refining it during retries: recurrence and squaring may
amplify that error. Conversely the fixed guard16 is not claimed sufficient
by itself. The observed complete-sum radius is the acceptance criterion.

For each fixed finite N,J,K and fixed target point, all exact rational
constants, pi, log(m), and exponentials have shrinking enclosing intervals.
Arithmetic operations are continuous at the expression's exact values;
all denominators in the recurrence are fixed positive integers. Each
primitive's input is bounded for sufficiently large p; exponential halving
counts are bounded, even if a branch changes, so the finite outward
squaring also has width tending to zero. Structural induction through the
finite expression gives `R_arith ->0`. The same proof applies when the
true-root and circle-node intervals are regenerated and shrink at each p.
Starting with any positive precision and doubling it after an unsuccessful
radius comparison therefore terminates at the stricter `R_arith<=eta/4`
condition. The successful precision p, retry precisions/radii, and budget
serialization scale B are recorded. Individual primitive series lengths
are not explicitly serialized: they are determined exactly by the recorded
precision, source bytes and inputs, and may be reconstructed by replay.

Validate the *exact rational point* against closed D before conversion.
A dyadic enclosure of Im(s)=4/3 extends microscopically outside D; rejecting
that rectangle would incorrectly reject a valid boundary point. Analytic
remainder bounds apply to the true point in D, while interval inclusion is
safe even if its enclosing rectangle extends outside. For circle nodes the
exact bounds `Re(s) in [-7/10,17/10]`, `abs(Im(s))<=6/5` give a strict margin
inside D for every m,j.

## Practical exact selections

The following table uses the exact first-success searches, not floating
estimates. P includes zero-character pairs; active pairs exclude them and
exclude rigorously discarded pairs. Working precision is selected by the
actual finite-sum radius and cannot be fixed from this parameter table alone.
The implementation's serialization rule selects B=87 for eta1e-24 and B=114
for eta1e-32, independently of q.

| eta | q | N | J | T | K | P | active |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1e-24 | 3 | 12 | 7 | 128 | 19 | 336 | 71 |
| 1e-24 | 4 | 14 | 8 | 256 | 20 | 448 | 65 |
| 1e-24 | 5 | 16 | 8 | 256 | 20 | 512 | 111 |
| 1e-32 | 3 | 14 | 7 | 128 | 25 | 392 | 84 |
| 1e-32 | 4 | 16 | 8 | 256 | 26 | 512 | 72 |
| 1e-32 | 5 | 18 | 8 | 256 | 26 | 576 | 129 |

| eta | q | B_n (display) | B_t (display) | B_Q (display) | B_discard (display) |
| --- | --- | --- | --- | --- | --- |
| 1e-24 | 3 | 6.19178879e-28 | 9.78128849e-35 | 5.15233620e-26 | 6.00277106e-28 |
| 1e-24 | 4 | 7.23723295e-28 | 2.81328231e-53 | 6.87342956e-27 | 3.17407320e-29 |
| 1e-24 | 5 | 1.50950533e-28 | 1.93831366e-41 | 1.28470145e-26 | 2.49468152e-28 |
| 1e-32 | 3 | 1.72727530e-36 | 9.78128849e-35 | 5.77885142e-34 | 4.11423914e-37 |
| 1e-32 | 4 | 3.34881737e-35 | 2.81328231e-53 | 7.79252430e-35 | 1.14520173e-36 |
| 1e-32 | 5 | 2.87312268e-35 | 1.93831366e-41 | 1.45643496e-34 | 2.19003702e-37 |

Run on Linux from the repository root, choosing a nonexistent output:

`PYTHONDONTWRITEBYTECODE=1 python3 planning/adaptive-theta-20261105/design/check_serialized_design.py --output outputs/checks/2026-11-05-adaptive-theta/design/rounded-parameters-v3.json`

The revised checker recomputes the first-success choices, raw analytic
fractions and whole-pair sets, and checks each dynamic rounded component,
its upward inclusion and rounding increment, and the exact literal sum.
Its interval input is the worst-case admitted eta/4, so it proves an output
majorant whenever an actual finite-sum evaluation passes that radius test;
it is not itself a sampler execution. It uses no decimal integer-limit
change, random seed or special-function oracle. The earlier check_design.py
and exact-parameters-v2.json remain prior evidence of the same truncation
choices and67 structural controls, using the original raw budget convention.
The prior design/TeX/checker are copied byte-identically in `prior-v1/`;
the original check manifest and compile artifacts remain unchanged.

## Scope and handoff

This removes the mathematical fixed-N/T/K/precision obstruction for exact
point samples of the three fixed classical completed functions, conditional
only on their existing stated theta/Mellin identity and elementary arithmetic.
A delivered executable needs its own independent interval/primitive and
parameter/certificate review. A downstream arbitrary-error readout additionally
needs adaptive node count, degree, Fourier arithmetic and optimization budgets;
new small sample eta alone does not remove the frozen64-node alias floor.
The original arithmetic/covariance and positive determinant bridge remain
separate; no new zero-location assertion, all-conductor result, Lean theorem,
training advantage, dependency installation, publication or GRH proof follows.
