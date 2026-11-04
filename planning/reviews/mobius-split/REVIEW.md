# Independent review: signed Möbius splitting and its cutoff obstruction

Reviewer `/root/mobius_split_review`, 2026-11-03. Read the project instructions,
README, pinned Lean script/dependency declaration, current handoff and
`research/short-row-pair-barrier.md`, `research/short-row-high-gcd.md`, plus
October `paper2.tex` lines180–275 and the original-family Gram review. The
reviewer changed only this report and reviewer-owned evidence under
`outputs/checks/2026-11-03-mobius-split/review/`. No source, production code,
Git history/index, environment, authentication or service state was changed.
The production fragments/checker/Lean snapshot will be reviewed below when
supplied. This is not a new full source-paper audit.

## Exact convolution and regrouping

On the multiplicative monoid of nonzero integral ideals prime to the fixed
excluded set S, let ζ be the constant-one coefficient function and δ the
unit-ideal convolution identity. Ideal unique factorization gives μ*ζ=δ.
For a=μ1_(N<=U), b=μ−a, commutative convolution gives

b*b*ζ = μ*μ*ζ−2a*μ*ζ+a*a*ζ = μ−2a+a*a*ζ.

Thus μ=2a−a*a*ζ+b*b*ζ, with no analytic assumptions. This is a classical
Vaughan-type identity, not a new general arithmetic-function theorem.
The equality holds also for nonsquarefree ideals, but the intended row
application must keep μ²(n) before using squarefree factor conductor rules.
For squarefree n=abc the factors are automatically squarefree and pairwise
coprime. Multiplicativity of the original denominator symbol, including its
zero extension, and of the fixed ν factors then gives the proposed exact
row decomposition A=2A_short−A_I+A_II with W evaluated at the full product.

Regrouping d=ab in A_I gives β_U(d)=sum_(ab=d;Na,Nb<=U)μ(a)μ(b).
For squarefree d this is μ(d) times the number of the indicated ordered
factorizations. Its support implies Nd<=U², but that support bound alone
is not its exact definition. The remaining c must stay squarefree and
coprime to d; ν(c), every row zero and W(Nd Nc/D) remain present.

Regrouping s=bc in A_II gives g_U(s)=sum_(b|s;Nb>U)μ(b).
Here Ns>U>=1, so s is nonunit and the full divisor sum vanishes; hence
exactly g_U(s)=−sum_(b|s;Nb<=U)μ(b). The bilinear sum still requires
a,s squarefree, (a,s)=1, Na>U, Ns>U and full annular weight. No coefficient
sequence may be silently replaced by arbitrary bounded weights. TypeII is
empty when U²>=2D for the stated support, and its active range is not
uniformly balanced without further dyadic subdivision.

## Conductors and masks

For a,s squarefree, good and coprime, χ_a(u)χ_s(u)=χ_(as)(u), with an
exact nontrivial sextic local component at every prime dividing as. Its
primitive finite row conductor is as, not a or s alone. Splitting a column
into factors does not shorten this conductor. For two recombined columns
n,n', put h=gcd(n,n'); their oscillatory conductor is nn'/h² and their
zero-preserving periodic modulus is nn'/h. These are the already established
original-family conductor facts, now retained through the new decomposition;
they are not a new proof of a short-row cancellation estimate.

The common-factor and S masks remain exact. Row valuations divisible by six
can trivialize a local phase on units but cannot turn a genuine zero at that
prime into one. Fixed primary generators count each ideal once; row sums
are over actual Eisenstein elements with no quotient by the six units.

## A decisive but scoped cutoff obstruction

The principal ν=1 is allowed: October line215 fixes an arbitrary finite-order
Hecke character and the source explicitly includes the zeta case. Take U=1,
large D and a fixed nonnegative smooth W supported in [1,2], bounded below
by w0>0 on a closed subinterval [a,b] inside (1,2). The short term vanishes
on this annulus. On a squarefree n>1, TypeI coefficient is1 and TypeII
coefficient is μ(n)+1, which is either0 or2. At the actual unit row u=1,
χ_n(1)=1 with every original mask checked, so both sums are nonnegative.

For TypeI, good prime ideals n in [aD,bD] give ≫D/logD terms. For TypeII,
fix one good prime ideal q0 outside S and take n=q0 p with p distinct from
q0 and Np in [aD/Nq0,bD/Nq0]. All these n are squarefree with μ(n)=1 and
contribute at least2w0. The unconditional fixed-field prime-ideal theorem
gives ≫D/logD such p. This is a named classical external analytic input,
not a GRH-level uniform prime estimate and not a theorem proved by finite
experiments. Nonnegativity permits restricting the TypeII sum to this
subfamily, unlike the signed original μ sum.

Both normalized piece amplitudes are therefore ≫sqrt(D)/logD. Their
individual row energies are ≫D/(logD)², since the full nonnegative energy
contains u=1 once H>=1. At H=D^(3/4) this refutes a proposed separate-piece
bound H D^epsilon for epsilon<1/4. For the exact recorded convention
H(HD)^epsilon the numerical threshold is instead epsilon<1/7. Statements
may equivalently reparameterize epsilon, but must not mix these thresholds.

This refutes a newly proposed **all-cutoff, separate-piece** estimate only.
It does not refute the signed original MS_(3/4), any existing source theorem,
or a method with a suitably growing cutoff. The full original sum is the
difference of these large pieces, so its cross cancellation remains essential.
No lower bound on the full signed energy follows from the piece lower bounds.

## Why the first one-Cauchy envelope is insufficient

For a dyadic block with lengths A and S, D comparable to AS, apply Cauchy
to the a sum before using its coefficient signs. If one grants, only as an
optimistic explicit hypothesis, a per-a row energy bound
C(H+S) sum_s|g_U(s)|² for the full masked annular slice, then the resulting
bound is D^-1 ||α||² times A times that slice bound. With ||α||²<=A and
||g_U||²<=S D^epsilon this is at best order A(H+S)D^epsilon. In the range
where A grows, it does not yield H D^epsilon. This is a failure of that
particular upper-bound route, not a lower bound for the actual bilinear
energy and not an assertion that the assumed slice theorem is available.

## Independent exact finite checks

The reviewer wrote a separate oracle, with no production imports. It uses
a divisor-closed prime-support subset of actual split prime ideals
(7,ω−2),(7,ω−4),(13,ω−3),(13,ω−9),(19,ω−7),(19,ω−11).
The exact integer sixth-root table retains collisions and denominator
multiplicities. Both principal coefficients and the fixed Kummer-numerator
λ=1+2ω twist are exercised; no arbitrary phase table is advertised as a
new Hecke-character construction. Its finite annular integer profile is
expressly not claimed C-infinity; the identities are pointwise for any
weights and the asymptotic proof uses a separate fixed smooth W.

Results:292 convolution cases including nonsquarefree ideals,152 squarefree
regrouping cases and792 weighted row comparisons pass. Six-power collision
zeros remain zero. The oracle does not certify ideal counting, infinite
conductor uniformity, Mellin/supremum estimates, MS_(3/4) or GRH. Evidence:
`review/oracle.py`, `review/oracle.json`, `review/oracle.log`.

No substantive mathematical blocker was found in the proposed scoped
construction. Final literal-source/Lean/production-check review is pending
receipt of those artifacts, and integrated build/browser/private-push gates
remain with the root worker.

## Production snapshot and literal-source review

Independently compiled `lean-analytic/MobiusSplit.lean` in the existing pinned
Lean4.24/mathlib workspace with `-DwarningAsError=true`: exit0. All eight
printed statements use standard foundations only, with no `sorryAx` or
custom axiom dependency. They use the actual natural-number arithmetic-function
Dirichlet ring, plus a universal commutative-ring inverse identity. They do
not claim to have constructed the ideal Dirichlet ring, finite-order Hecke
characters or analytic estimates in Lean. The distinction is explicit in the
source header and literal theorem types. The fixed-cutoff coefficient and
nonnegativity statements hold on all integers n>1, and the ideal application
retains its additional squarefree support separately.

Replayed the production checker to reviewer-owned `production-exact.json`
with bytecode writes disabled. Its157 good ideals through norm512 include
inert prime ideals. All785 coefficient/regrouping cases,4704 zero encounters
and900 conductor exponent ledgers pass. The helper uses actual split and
inert sextic residue arithmetic from the existing pinned local checker.
The finite profile is ((N−D)(2D−N))²/D⁴; its amplitude-square normalization
is D⁹ after the original D^(-1/2) factor. The saved vector ordering is
[original,2*short,TypeI,TypeII]. Current annular examples all have short0.
No finite data establishes the smooth-weight asymptotic theorem.

Read both new TeX fragments in full. Three precise wording/normalization
refinements were sent to root: the proposition title should say the
all-cutoff strengthening is false rather than suggest failure at every U;
the smooth W's lower bound must be explicitly positive; and the finite
numerator example must consistently distinguish M1 from A1=sqrt(D)M1 and
normalize I1,II1 with the same convention. The derivations, retained masks,
primitive/period distinction, epsilon thresholds and generic-Cauchy limitation
otherwise match the reviewed mathematics. Snapshot hashes and pending textual
refinements are recorded in `review/reviewed-snapshots.json`.


## Final acceptance

All three textual findings are resolved in the final fragments. The proposition
now refutes the all-cutoff strengthening via U=1 only; its smooth W has a
strictly positive lower bound on a positive-length closed subinterval. The
finite example consistently scales (M1,I1,II1) by D^(9/2), and the relation
is II1−I1=M1. The production record now declares its component ordering
[original,2*short,TypeI,TypeII]. Both epsilon conventions and the limitation
on moving-cutoff arguments remain explicit.

Independently reran the final production checker to reviewer-only files and
compiled the final Lean source again with warnings treated as errors: both
exit0. Eight printed formal statements have only standard foundational axiom
dependencies. Final Lean source SHA-256: `d2b357fe65ab0d02c1a9edf2518eae082a2eadf71e837522350ccd65ea142651`.
The complete final source hashes are in `review/reviewed-snapshots-final.json`.
The earlier snapshot and failed/pending review records are preserved.

No outstanding mathematical or executed-program finding remains in this
assigned scope. The exact ideal decomposition, conductor ledger, fixed-cutoff
separate-piece obstruction and generic-Cauchy failure are accepted as stated.
This is not a proof or refutation of the original signed short-row estimate,
not a new zero-free region, and not a positive arithmetic determinant or GRH
completion. General ideal/Hecke/analytic formalization remains explicitly
outside the eight natural-number/ring statements. Integrated PDF/HTML/browser,
credential/integrity/privacy and authorized-push checks remain with root.


## Targeted robustness addendum: third distinct prime and cutoff sign

Replayed the extended production checker through norm1024 to separate
reviewer-owned `production-exact-1024.json`:307 good ideals,1535 coefficient/
regrouping checks,19680 original zero encounters and900 conductor ledgers
all pass. The new D512/H64 diagnostic includes columns with three distinct
prime-ideal factors. These replace no previous evidence; old logs remain.

Independently verified the concrete primary generator7−21ω. Its norm is
637=7²·13, and its ideal factors are (7,ω−2), (7,ω−4), (13,ω−9), each once.
The first two are distinct conjugate prime ideals, so this is squarefree
as an ideal despite its nonsquarefree rational norm. At U7 the only short
ideal divisors are1 and those two norm7 primes. Thus the TypeI coefficient
is1−4+2=−1; using μ(n)=−1 and the exact identity gives TypeII=−2. An
independent call to the no-production-import divisor oracle reproduces both
values. Evidence: `review/sign-control-637.json`.

The new paragraph in the final TeX describes this as a coefficient sign
control at a different fixed cutoff. That is correct. It does not determine
the sign of the whole unit-row sum or any mean-square estimate at U7, and
does not refute a moving-cutoff method. The U1 nonnegative-subfamily proof
must not be reused verbatim once coefficients have both signs. Lean is
unchanged from the independently compiled eight-statement snapshot; hashes
of the extended checker and final fragments are recorded in
`review/reviewed-snapshots-1024.json`. No new outstanding finding remains.
