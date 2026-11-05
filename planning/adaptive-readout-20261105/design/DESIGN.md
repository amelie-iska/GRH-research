# Requested-error readout from preserved certified labels: design and proof

2026-11-05. This document is a design/proof artifact only. All inspection,
creation and checking took place through SSH on `iska-linux-vscode`, in the
existing Linux repository. No production source, frozen experiment, queue,
publication, dependency, environment, GPU or credential was changed.

## Selected implementation alignment

The new implementation inspected later in the same session uses the fixed
R=7/10 compact and the existing224bit outward dyadic Fourier rectangle
operations, rather than the optional exact-endpoint rectangle propagation
considered below. Its literal rational loop has the same midpoint target.
Its selected simpler budgets are E_opt=(3/4)^k sum|t_n|_1u^n and
E_arithmetic=A_d (independent of k), yielding
E_total=C_d+(3/4)^k sum|t_n|_1u^n. This follows by writing
b^k-b*=(b^k-t)+(t-b*) and is fully rigorous. The shared TeX proposals in
this directory describe this selected implementation. The sharper H_d/A_d
formula below and adjustable R/exact-endpoint rectangles are optional
design alternatives, not claims about the delivered executable.

## Accepted input and honest next extension

Use the preserved final-v5 certificate, not a new call to the fixed theta
producer. Its SHA256 is
`85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8`.
For each q=3,4,5 it supplies 64 rational complex labels y_j, disk radii eta_j,
and dyadic rectangles Z_j enclosing the **true** roots zeta_j=exp(2*pi*i*j/64).
The completed primitive quadratic function F_q is entire by the stated
classical theta/Mellin theorem. The independently accepted growth proof gives
|F_q(1/2+z)| <= M_q on |z|<=12/5, with M_3=4,M_4=10,M_5=6.
The source snapshots have hashes

* theta_oracle.py: c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1
* dyadic.py: 82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170

The feasible next deliverable accepts an exact rational requested error eps>0
and rational compact radius 0<=R<=7/10, chooses degree d<64 and an actually
executed finite GD trace, and returns either a certificate <=eps or an
explicit, evidenced refusal. Restricting R to the already accepted compact
is a deliberate versioned scope contract. The formulas below remain valid
for the larger open range R<rho, but that is not needed for this release.
Do not convert a JSON float/display summary into a proof endpoint.

The limitation is substantial: these labels have **certified** radii near
1e-17 to 1e-16, even though diagnostic observed errors were much smaller.
No number of GD updates, degree increase or readout arithmetic precision can
remove their certified error or the 64-node alias error. Refusal means this
fixed-data proof cannot certify the request; it does not prove that no
polynomial, tighter majorant or more accurate oracle could meet the request.

## Exact rational rectangle construction

Set c=1/2, rho=6/5, r=12/5, m=64, a=3/4, u=R/rho, v=R/r,
w=(rho/r)^m=2^-64. Define S_d(x)=sum_{n=0}^d x^n; use this sum directly at
x=0. Let eta=max_j eta_j. Rational endpoints of all input dyadic rectangles
are exact fractions with denominator 2^224; check the recorded bits.

Using outward **exact rational endpoint** addition/multiplication, compute

    B_n = (1/m) sum_j y_j conjugate(Z_j)^n, 0<=n<64.

Rectangles need no new repeated dyadic rounding. Exact rational interval
arithmetic only creates interval dependency overestimation. Since the true
roots belong to Z_j, their exact Fourier coefficient
b*_n=(1/m)sum_j y_j conjugate(zeta_j)^n belongs to B_n, by induction on every
operation. Use exact rational midpoint t_n=mid(B_n), coordinate-halfwidth
sum e_n=rad_1(B_n), and endpoint magnitude h_n=mag_1(B_n). Then
|t_n-b*_n|<=e_n and |b*_n|<=h_n. Moreover h_n>=e_n since on each real
interval max(|lo|,|hi|)>= (hi-lo)/2.

Define A_d=sum_n e_n*u^n, H_d=sum_n h_n*u^n. In particular H_d>=A_d>=0.
These are certified quantities, not estimates based on midpoint decimals.
Use exact Fractions or unbounded integers; at degree near63 decimal integer
representations may exceed Python's default 4300-digit conversion limit.
Choose a documented bounded conversion allowance or a compact exact dyadic
serialization; this is not a mathematical precision limit.

## What the executed GD trace actually optimizes

Represent C^(d+1) as R^(2d+2), with the ordinary real Euclidean metric. Execute

    b_n^0=0,
    b_n^(k+1)=(3/4)b_n^k+(1/4)t_n.

Every coordinate is rational, so all updates can be exact rational operations.
Store every iterate, the fixed target vector, step1/4, the exact objective

    L_mid(b)=(1/2)sum_{n=0}^d |b_n-t_n|^2,

its exact rational value at each iteration, and sufficient dimensions and
provenance to replay every update. Its real Euclidean gradient is b-t,
so this is literal executed GD for the declared diagonal Fourier-coordinate
objective. Exact loss obeys L_mid(b^(k+1))=(9/16)L_mid(b^k).
Do not generate trace values only by the closed form and call that a loop.
A separate replay can compare against b^k=(1-a^k)t as a diagnostic identity.

For comparison, the original ideal-root sample-label objective is

    L_y(b)=(1/(2m))sum_j |sum_n b_n*zeta_j^n-y_j|^2.

Because d<m, A* A=mI and its true gradient is b-b*. The original gradient minus the
executed midpoint-target gradient is t-b*, enclosed coefficientwise by e_n.
Thus the rational trace is a certified perturbed-gradient implementation of
this original objective, **not** its literal exact-gradient trajectory.
Equivalently, its target is an explicitly certified rational Fourier
surrogate. Naming this distinction is necessary: exact nontrivial roots
cannot generally be encoded as rational coefficient vectors.

If an exact-original-objective GD claim is wanted later, execute and retain
an outward interval recurrence enclosing beta^(k+1)=a beta^k+(1-a)b*, and
label that object a validated enclosure of the exact trajectory. Interval
midpoints need not obey the exact original recurrence. The rational
surrogate trace already supplies an actual reproducible optimization run.

## Five exact compact-uniform budgets

The exported polynomial after k executed updates is literally

    P_k(s)=sum_{n=0}^d b_n^k*((s-c)/rho)^n.

The normalized basis is indispensable. All five following budgets are exact
nonnegative rationals:

    E_opt(k) = a^k H_d,
    E_oracle = eta S_d(u),
    E_alias = M_q w/(1-w) S_d(v),
    E_Taylor = M_q v^(d+1)/(1-v),
    E_arithmetic(k) = (1-a^k) A_d.

No extra coefficient-midpoint rounding occurs when the exported loop
coordinates remain exact Fractions. E_arithmetic is the inherited
root-rectangle/DFT midpoint error; its name does not imply hardware roundoff.
Additional decimal/float export requires a new exact coefficient conversion
budget. Do not use a float coefficient to evaluate a claimed literal rational
polynomial without accounting for that conversion.

Proof: exact labels at the true circle have Fourier coefficients
sum_{ell>=0} alpha_{n+ell*m}rho^(n+ell*m), where
F_q(c+z)=sum_l alpha_l z^l. This follows by uniform convergence on |z|=rho
and finite Fourier orthogonality. Cauchy's |alpha_l|<=M_q*r^-l gives the
alias term above when n<=d<m. Changing true function values to y_j perturbs
each Fourier coefficient by at most eta, giving E_oracle. Omitted Taylor
terms give E_Taylor. The actual loop yields b^k=(1-a^k)t, hence

    b^k-b* = -a^k b* + (1-a^k)(t-b*).

Triangle inequality, rectangle inclusion, and |(s-c)/rho|<=u give the
optimization and arithmetic terms. Sum all five to prove

    sup_{|s-c|<=R}|P_k(s)-F_q(s)| <= E_total(k).

This proof does not use a small empirical loss as an oracle certificate.

## Parameter selection, termination, and the exact attainable range

For every candidate 0<=d<64, define the finite-data floor

    C_d = E_oracle + E_alias + E_Taylor + A_d.

Then the very same five budgets satisfy the exact identity

    E_total(k)=C_d+a^k(H_d-A_d).

This decreases to C_d since H_d>=A_d. Scan all64degrees (the floor need not
be minimized at63). Choose the smallest d with C_d<eps. If none exists,
refuse with the exact list or minimum of these floors, separate inherited
oracle/alias/Taylor/DFT components, and the fixed-input scope. A request
at equality can be conservatively refused: finite k need not attain the
limit. A degenerate H_d=A_d case may be accepted if its exact bound<=eps,
but is not needed for the simple strict-slack contract.

Once d is selected, let delta=eps-C_d>0. Starting k=0, execute updates until
all five recomputed terms sum to <=eps. This terminates: if H_d>A_d,
choose any finite k with a^k <=delta/(H_d-A_d); powers of3/4 tend to0.
There is no need for logarithms or an unjustified hardcoded step cap.
The implementation should recompute the five exact terms and compare them
as rationals after each step. Any operational step/resource cap must return
`resource_limit`, without claiming the mathematical request was impossible.
An optional safe precomputed step upper bound uses (3/4)^4=81/256<1/3:
choose integer l>=0 by the exact loop 3^-l*(H_d-A_d)<=delta, then k=4l
suffices. This gives a priori finite trace size without floating logs.

The strict supported range is eps>min_{0<=d<64} C_d for each q and R.
For all three conductors together, require eps>max_q min_d C_(q,d).
There is also a precision-independent positive floor E_alias>=M_q*2^-64/
(1-2^-64), and E_oracle>=eta. These lower bounds are floors of this chosen
certificate, not lower bounds on actual approximation errors.

At R=7/10, the analytic-only (excluding tiny A_d) exact scan gives minima
approximately:

|q|degree at minimum|oracle|alias|analytic-only minimum|
|---|---:|---:|---:|---:|
|3|56|7.262240824511955e-17|3.061276722312013e-19|7.292853591735253e-17|
|4|56|1.729322804710350e-16|7.653191805780031e-19|1.736975996516175e-16|
|5|55|3.369499303690379e-16|4.591915083468019e-19|3.374091218773938e-16|

These displays are approximate; use the exact output JSON for comparisons.
The check script also computes the inherited DFT widths and actual floors.
Requests eps=1e-15 are comfortably inside this finite-data range; arbitrarily
small positive rational eps are not.

## Input, provenance, failure, and replay guards

Preserve the existing producer and final-v5 data unchanged. A new versioned
readout should reject malformed dimensions, duplicate/missing/out-of-order
indices, conductor mismatch, unsupported root count, root or node dyadic
precision mismatch, reversed intervals, negative radii, nonpositive errors,
unsupported compacts, bool/float aliases for exact integer/Fraction fields,
and root/source/frozen hash mismatch. Parse integer numerator/denominator
strings without first converting through floats. Verify denominator>0.
Require exactly the pinned192sample rows in the frozen canonical order or
strictly validate/canonicalize all indices, rather than silently accepting
truncated families. Verify the known node construction against the accepted
snapshot, or pin the whole certificate hash and inspect its source hashes.
Only pinning source names without their bytes is inadequate.

Capture producing/replay source bytes and hashes at entry, check unchanged
before emission, and copy those entry bytes into a fresh output directory.
Refuse overwrite. Record requested rational R and eps, input and source
hashes, exact targets/intervals, all actual iterates and losses, degree/step
selection, exact final budgets, the normalized polynomial convention, the
stated theta identity input, no GRH proof, and no new Lean declarations.
A separate checker should recompute every update and loss from input,
independently recompute exact budgets and confirm their literal sum<=eps.
Adversarial mutation checks should catch changed trace coordinates, budget
terms, root endpoints, radius, source hash, input hash and request tolerance.
Keep diagnostic high-precision comparisons clearly separate from the proof.

Current source inspection found useful guards already present: domain
checked before panel discard; negative/noninteger orders rejected; typed
lru_cache prevents float alias bypass; readout requires a complete indexed
family and checked roots; all reported180bit budget parts are rounded first
then exactly summed; input source bytes are captured and checked unchanged.
The new readout must preserve their intent while avoiding the producer's
fixed 5e-15 assert and fixed degree/step values as an adaptive API contract.

## Full adaptive theta oracle: feasible mathematics, separate implementation

A full arbitrary-requested-eps oracle is a larger, separately reviewed task.
The current source hardcodes N=11,T=128,P=224,series lengths60/92/60,
discard2^-90 and budget dyadic precision180. Changing only GD degree/steps
cannot remove these floors. Raising BITS alone also leaves nonzero
transcendental remainder floors. Global/cached precision must never be
changed in place while retaining caches from another precision context.

For these same three conductors only, there is a constructive future
parameter proof; it is not a claim that the present code implements it.
Let delta=3/q, U(x)=(1+x/128)^-128, Q(x)=1/x+2/x^2+2/x^3 and
C_0=1,C_1=(1+1/delta)/2. Retaining1<=n<=N gives omitted-n bound

    T_n(N)=2 C_a Q(delta(N+1)^2)
           *U(delta(N+1)^2/2)/(1-U(delta(N+1))).

This tends to0 as N tends to infinity, since U(x)=O(x^-128), Q(x)=O(x^-1),
and the denominator tends to1. For T=2^J, the retained-time bound is

    T_t(N,T)=sum_{n=1}^N 2 n^a T^3 U(T delta n^2) Q(T delta n^2),

which tends to0 for fixed N as T tends to infinity. Partition [1,T] into
four equal panels on each dyadic block. For fixed finite N,J the exact
Cauchy remainder is a finite sum of positive constants times
(h/(m/2))^(2K+2)/((2K+3)(1-(h/(m/2))^2)), with ratio<=2/9<1,
so it tends to0 as K increases. Every discarded whole pair uses the
already proved bound4h*n^a*(m+h)^2*U(delta*n^2*(m-h)). For at most4JNpairs,
a discard threshold beta/(4JN) ensures total discarded error<=beta.
For J=0 there are no finite panels; an implementation can require J>=1.

For a target label radius eta_target, allocate its rational budget among
n-tail,time-tail,Cauchy-tail,discard and actual interval radius, leaving
strict slack for serialization. Select N,T,K by exact rational comparisons
and discard by the whole-pair rule; never discard only an unstable factor.
Then the remaining expression graph is finite, with rational nonzero
constant denominators and exponential/logarithm on their proven domains.
Its interval widths tend to0 when both primitive series lengths and
outward dyadic precision increase. Induction over this finite continuous
expression graph proves a precision-search termination argument.

One explicit future series schedule uses P>=2 bits and Pterms for each
atan/log/exp series. Before dyadic rounding, the Machin width is at most
16*5^(-2P-1)/(2P+1)+4*239^(-2P-1)/(2P+1).
After the two atan endpoint roundings, an additional width<=40*2^-P
suffices. A reduced log with z<=1/3 has tail<=
9/[4(2P+1)3^(2P+1)]; range reduction multiplies the log2 tail by |k| and
its interval-rounding width by the same factor. The scaled exponential
remainder is A^(P+1)/(P+1)!/(1-A/(P+2)), A<=1/2, before finitely many
outward squarings. All these explicit terms vanish with P, and each exact
rational primitive operation contributes at most one outward ulp at its
chosen dyadic scale. The interval run itself certifies the resulting widths;
no universal floating error estimate is substituted for that check.
For budget serialization at Bbits, each upward rounding adds less than2^-B;
the five final terms add less than5*2^-B. Choose B by an exact power-of-two
comparison with the reserved slack. An unchanging B=180 is a genuine
serialization floor for sufficiently tiny requests.

After such a genuinely adaptive oracle exists, choose d so Taylor<=eps/10,
then m>d so alias<=eps/10 (w=(rho/r)^m), then eta_target so
eta_target*S_d(u)<=eps/10. Carry out the oracle selections above with strict
slack, choose readout precision to ensure A_d<=eps/10, and execute GD until
E_opt<=eps/10. Round final budget pieces within the reserved slack, making
the exact printed total<=eps. Cauchy geometric convergence and the preceding
finite-expression precision proof justify parameter-search termination.
This is a credible mathematical future design, but requires new code,
new provenance/configuration schemas and independent validation. It is not
certified by reusing the fixed final-v5 labels, nor by rerunning the current
producer with only a different m.

No part of this design proves zero location, an arithmetic determinant,
all-conductor uniformity, Artin holomorphy, Lean formalization or GRH.
