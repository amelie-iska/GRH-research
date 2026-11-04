# Independent review: full-mask type-I Hecke series and scalar contour

Reviewer `/root/mobius_split_review`, 2026-11-03. This is a new analytic
continuation of the signed type-I construction, not a repeat of the completed
U1 cutoff obstruction. Read `research/mobius-split.md`, the current frontier,
the earlier reciprocity/conductor report, both new `hecke-type-i` TeX
fragments in full, and the literal Lean/checker source. Reviewed the cached
Kudla Tate notes' Section4 Theorem4.3/Corollary4.4 and their stated proof
reference; this does not claim a fresh audit of Tate's whole thesis or every
normalization in incomplete displayed epsilon calculations. Classical abelian
reciprocity and the primitive finite-order Hecke analytic continuation/
functional equation remain explicitly named external theorems. The scalar
estimates below are independently derived from those inputs.

Only this report and reviewer-owned evidence in
`outputs/checks/2026-11-03-hecke-type-i/review/` were written. No source,
production code, environment, Git state, service, authentication or dependency
was changed.

## Character construction and zero presentation

Define the Kummer character of K(u^(1/6))/K using arithmetic Frobenius, then
multiply by the fixed finite-order nu and pass to its primitive inducing
character psi_u. This definition is independent of d. Outside6u the
Frobenius value is precisely the source's sextic numerator symbol. Its
finite-order archimedean component is trivial since C* is connected.
Let psi_{u,2} be the primitive character inducing its square, not the
pointwise square of its zero-extended primitive coefficient array.

At good primes outside S, nu is unramified. Tame inertia for v_p(u)=e has
order6/gcd(6,e), so psi_u is ramified iff e is nonzero modulo6; its square
is ramified iff e is nonzero modulo3. These assertions must not be applied
without qualification at primes in S where nu can be ramified and cancel
local characters. At the primes above6, sixth-power reduction and finiteness
of K_p*/(K_p*)^6 give a fixed maximum wild conductor. Tame one-dimensional
ramification elsewhere has conductor exponent1. Thus Q_u <<_nu Nu is
unconditional with fixed K and nu. This uses tame conductors rather than
applying the crude polynomial discriminant exponent25 at every growing
prime.

One small divisibility-wording refinement was sent to root: a displayed
product restricted to p outside S requires its fixed factor also to include
all extra good primes of S. Equivalently use the product over all p|u away
from6 with a fixed wild/fnu factor. The latter keeps the stated
S-independent conductor estimate transparent.

## Exact Euler ratio and principal residue

The deleted set T=S union supp(u) union supp(d) contains the primitive
conductors, but may contain strictly more primes. For p outside T, psi2(p)
=psi(p)^2 and the local squarefree factor1+psi(p)q^(-s) is exactly
(1−psi2(p)q^(-2s))/(1−psi(p)q^(-s)). At a deleted prime the same primitive
ratio multiplied by the proposed numerator/denominator correction is1.
This proves the displayed global identity in absolute convergence Re(s)>1.

The square's conductor can collapse. If psi(p)=0 while psi2(p) is an
unramified nonzero value, the primitive ratio has factor1−psi2(p)q^(-2s),
and the deleted correction must divide by it. If both characters are
unramified, the deleted correction is the reciprocal squarefree factor.
For principal nu and u=pi^3 at Npi7, the raw ratio48/49 and correction49/48
restore1. At u=pi^6 the raw ratio8/7 and correction7/8 restore1, despite
both primitive characters being principal. All original column zeros remain.

On Re(s)=sigma>1/2, the reciprocal of L^T(2s,psi2) is bounded by
zeta_K(2sigma) through its absolutely convergent Euler product, uniformly in
psi2,T and Im(s). No desired zero-free result at Re(s)<=1 is assumed.
The numerator finite product is bounded by R_T^eta times a fixed constant:
large prime factors each satisfy1+q^(-sigma)<=q^eta, while the finitely many
small prime ideals form a fixed constant. The only possible pole in this
half-plane is the principal numerator's simple pole at1. Its residue is
(res zeta_K(1))/zeta_K(2) times product_(p in T) q/(q+1), as stated.
There is no derivative factor2 from the regular denominator at s1.

## Four Mellin derivatives and uniformity

The finite-order primitive Hecke functional equation has one complex gamma
factor and analytic conductor Q_u(1+|t|)^2. On Re(s)=1+eta absolute
convergence gives a uniform zeta bound; on Re(s)=−eta the functional equation
and Stirling give Q_u^(1/2+eta)(1+|t|)^(1+2eta). Convexity on this strip
therefore gives the stated slightly relaxed exponents
Q_u^((1−sigma)/2+eta)(1+|t|)^(1−sigma+2eta). For principal psi regularize
by (s−1)/(s+1), with eta<1; dividing back on the fixed sigma<1 line is
bounded with constants allowed to depend on sigma. No Lindelof/subconvexity
or general Artin holomorphy enters.

Four integrations by parts with x d/dx give a bound by M4(W)(1+|t|)^(-4)
on the fixed strip. Smooth W supported in[1,2] has the required vanishing
endpoint terms. Choose internal eta small, for example at most
min(epsilon/4,1/8), before renaming losses. Then the polynomial vertical
growth is integrable and horizontal edges vanish. The crossed principal
pole yields exactly rho_T Y W_hat(1). This proves the claimed scalar error,
uniform in u,d,Y>=1 and families of fixed-support W with bounded M4.
Constants depend on fixed nu,S,delta,epsilon, not on a moving d or row.
No profile supremum has been exchanged with a signed arithmetic mean square.

The inner estimate can also be extended to small positive Y by the same
contour or a trivial finite-support argument, but that alone does not give
the full source scale-supremum. In the original decomposition with fixed U,
a smaller scale D'<=U restores the previously vanishing2a_U term. Any
smaller-scale reassembly must retain that short term and its normalization.
This caveat was sent to root; no full source supremum is certified here.

## Actual beta_U aggregation and the insufficient energy envelope

For U²<=D and d in the actual beta_U support, Y=D/Nd>=1. The radical bound
R_T<=C_S Nu Nd and Q_u<<_nu Nu give the stated conductor factors. The
beta_U sum is controlled without replacing it by a free coefficient family:
its absolute value is at most the count of its actual short factorizations,
so the weighted d sum is at most
(sum_(Na<=U) (Na)^(-1/2−delta+eta))².
The fixed-field ideal countO(X) and 0<1/2+delta−eta<1 give
U^(1−2delta+2eta). After choosing internal losses small enough and renaming
them, the normalized error is
D^delta U^(1−2delta+epsilon) Nu^(1/4−delta/2+epsilon), times M4(W).
The principal-residue sum retains beta_U and all outer nu(d)chi_d(u) factors;
no positivity or zero-free arithmetic identity is inferred from it.

Squaring and summing all Eisenstein elements with norm<=H yields
D^(2delta) U^(2−4delta+epsilon) H^(3/2−delta+epsilon), times M4(W)².
The lattice count isO(H); rows are not divided by the six units. At
H=D^(3/4), U=D^a, the power relative to H is
3/8+5delta/4+(2−4delta)a, positive throughout0<delta<1/2,0<=a<=1/2.
This is a limitation of the derived scalar envelope, not a lower bound on
the actual error and not a counterexample to Kummer-family averaging,
coefficient-sensitive covariance or the signed short-row target.

## Independent formal and finite checks

Fresh focused compilation of `HeckeTypeI.lean` with warnings as errors
passes seven printed statements with standard foundational axioms only.
The definitions are actual complex ratios and finite products. Nonzero
denominator hypotheses and the equality of primitive squares only outside
the deleted set are explicit. They do not claim an ideal Hecke-function
object, infinite Euler product, conductor theorem or Mellin contour in Lean.

The reviewer wrote a no-production-import SymPy/finite-field oracle with
six distinct actual split prime ideals (including conjugates with equal
rational norm). It checks288 exact local Euler restorations and3072
squarefree-support coefficients for row pi^e,e1..6, principal and fixed
Kummer(2) twists and four deleted sets. The e3/e6 naive-factor failures and
the residue factorq/(q+1) are exact controls. It constructs no analytic
L-values and does not independently establish local/global class field
or functional-equation theorems.

Separately replayed the production checker to reviewer-only outputs:
1488 cases,93 rows,128 squarefree finite-support columns over7 prime ideals
including inert norm25,78016 nonzero terms,29120 original zero encounters,
32 quadratic conductor-drop encounters and16 sixth-power mask encounters
pass. The primitive values after stripping the local prime power are
consistent with the tame Kummer/Frobenius rule; square-drop values are not
obtained by squaring a sentinel zero. The checker remains a finite algebraic
diagnostic, not an infinite-series or contour certificate.

Evidence: `review/local_oracle.py`, `local-oracle.json/log`, `lean.log`,
`production-exact.json`, `production.log`, and `reviewed-snapshots.json`.
Final prose acceptance is pending the small conductor-product wording and
explicit shrinking-scale caveat sent above. No other mathematical or executed
program blocker was found. Full source analytic assembly, typeII, signed
low-gcd mean square and the arithmetic positive determinant/GRH bridge remain
open; integrated build/browser/privacy gates remain with root.


## Final acceptance

All review refinements are resolved. The conductor divisibility now uses all
primes dividing u away from6, avoiding accidental loss of extra fixed primes
in S while retaining Q_u<<_nu Nu. The internal Mellin eta is explicitly
smaller than min(epsilon/8,1/8), and the smaller-scale discussion restores
the short2a_U term when a fixed cutoff meets the shrinking annulus. The
core correctly says that K(u^(1/6)) constructs the sextic factor before
multiplication by nu, and the principal local examples explicitly specialize
nu to1. The two primitive conductors, full T presentation and all formal
scope boundaries remain distinct.

Fresh final focused Lean compilation again passes seven statements with
warnings as errors and standard foundational dependencies only. Lean source
SHA-256: `a506fb6d63050d0c29ddf3b55a5174df653136f578dd2c4469a69349e32a3447`.
The production checker snapshot is unchanged from the independent successful
1488-case replay. Final prose/source/checker hashes are recorded in
`review/reviewed-snapshots-final.json`; earlier snapshots and evidence remain
preserved.

The full literal final fragments are accepted in the assigned mathematical
scope: exact Euler restoration, primitive conductor upper bound, scalar
Hecke/Mellin estimate with four-derivative uniformity, actual beta_U summation
and the explicitly insufficient elementary energy envelope. No outstanding
mathematical or executed-program finding remains. The abelian/Hecke analytic
inputs are named external classical theorems, not fully kernel-checked here.
No original signed short-row estimate, typeII/covariance reassembly, complete
scale-supremum argument, arithmetic positive determinant or GRH theorem is
established by this slice. Integrated PDF/HTML/browser/privacy/push checks
remain with root.
