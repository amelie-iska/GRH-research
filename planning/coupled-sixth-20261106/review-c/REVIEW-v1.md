# Independent review of the coherent sixth-part ray mean

Reviewed governing source: planning/coupled-sixth-20261106/lane-a/COHERENT_SIXTH_PART_RAY_MEAN-v1.md, SHA256 4315f8d2fb10b5c0a5f91fb8ae4c1e3271582fb27bd2bc5ee5d44912e81621fd. Verdict: accepted in its stated finite-prefix, original unweighted two-pivot scope. This is outside the frozen coherent-book release.

The surviving new statement is a coherent arithmetic replacement of the large good sixth-part sum, with a retained principal-ray counting main and a quantitative error. It is not a bound for that main or an improvement of the full signed estimate.

## Character and ideal masks

I compared the proposed outer expression directly with cbk:exact-kernel and its row-inversion, finite S-deletion and primitive-Poisson proof. The coefficient L_e/sqrt(F), finite k cutoff, ell|v2, eta(k^2 ell e), root, ray coefficients and primitive S zeros agree. The factor 1/D is applied only after summing this raw kernel.

On good arguments, TOTAL eta is the finite-order source quotient times rho. Thus bar(eta(s^6)) = bar(rho(s))^6 times the raw indicator (s,mn)=1. This does not assert that the individual xi have finite order. The resulting psi is a fixed type-zero ideal ray character, independent of the columns. The good/S ideal factorization y=h r s^6 is unique prime by prime. The sixth-free r and unrestricted s may overlap; bar(eta(r)) and the full mn deletion are still present. No k|s condition follows.

The squarefree q=mn is an IDEAL product on the original coprime squarefree column support. Split conjugates remain distinct prime ideals; inert prime-ideal norms are squared rational primes. Neither the inclusion–exclusion nor the divisor count substitutes rational squarefreeness.

## Fixed-ray counting, including subunit terms

For a fixed finite ideal ray character of infinity type zero, its generator function is periodic modulo a fixed ideal and trivial on the six units. The lattice disk count, divided by six, has area coefficient pi/(3 sqrt(3)). Encoding the fixed S exclusions gives kappa_S. Finite character orthogonality makes the leading coefficient zero precisely for the nonprincipal good-ideal character. The fixed lattice boundary error is O(sqrt(t)+1) for t>=1. For 0<t<1 there are no integral ideals and t<=sqrt(t), which supplies the stated O(sqrt(t)) extension; t=0 is exact.

The exact ideal Möbius identity is
N_(psi,q)(t) = sum_(d|q) mu(d) psi(d) N_(psi,1)(t/Nd).
All ideal divisors occur. In particular Nd>t contributes a nonzero negative principal main correction inside its error even though the ideal count is zero. Keeping these terms yields exactly kappa_S g(q)t in the principal branch. Truncating this identity at t or 2V would be incorrect. The accumulated error is bounded by sqrt(t) product_(p|q)(1+Np^(-1/2)), which is O_epsilon(sqrt(t) D^epsilon), since Nq<=4D^2. This uses no varying-conductor prime theorem or scalar Mertens assumption.

## Endpoints and actual profile

For the interval V<Ns<=b, the exact Stieltjes boundary expression uses CLOSED prefixes at both V and b. It is w(b)E(b)-w(V)E(V)-integral E w'. This handles norm ties correctly with no half-weight.

For the actual real nodal G, 0<=G<=1 and support length at most two, the accepted Bessel transform gives
|dotG|<=2 C0^(-1/2),
|x dotG'(x)|<=2 sqrt(5/2) C0^(-1) sqrt(x).
The second formula follows directly from J0'=-J1 and |J1|<=1. Differentiation under the compact v integral is justified. It requires no derivative of G. Substituting x=a_hr t^6 gives an absolute-variation bound at most a fixed constant times sqrt(L_e X/F), because b/V<=2. With F>=D^2 and L_e<=A1, the error per fixed h,r and original outer parameter is therefore
O_epsilon(D^epsilon sqrt(V) [1+sqrt(A1 X/D^2)]).
The exact main still contains its actual G and capacity; it was not flattened to this majorant.

## Outer budget and surviving power

There are O(D) ideals in the complete column annulus. The two coefficients cost B^2 D^epsilon through the elementary divisor bound, and all other column/ray/raw phases have bounded modulus. The two column counts cancel precisely the D^(-2) obtained from L_e/sqrt(F) and the single final normalization 1/D, leaving A1 before the v2 count. The finite k sum is bounded only for the error by zeta_K(2); ell divisors cost A2^epsilon, and the original v2 family has O(A2) ideals with fixed literal/ray multiplicity.

The active condition b_hr>V implies Nh Nr<X/V^6. Counting good sixth-free r by all ideals and retaining every S-supported h gives
#(h,r) << X V^(-6) sum_(h S-supported) 1/Nh <<_S X V^(-6).
The empty subunit ranges contribute zero. Multiplication by sqrt(V) yields R X V^(-11/2) with R=A1 A2. All sums in the actual replacement are finite. There is no infinite dual interchange, no conductorwise triangle in the retained main, and no implicit additional smoothness cost.

For V=X^(1/6)/2, the X factor becomes X^(1/12). At the stated pure parameters the power is 3/4+(3/8)/12=25/32; the old absolute count is 3/4+(3/8)/6=13/16. At the stated mixed parameters it is 7/12+(3/8)/12=59/96. The extra Bessel bracket is bounded at both examples. These are error budgets, not observed lower bounds. The pure error still exceeds the target and the principal coherent mean remains.

## Scope and provenance

The result requires the complete original good squarefree column annulus and the original unweighted two-pivot row family, fixed source/ray/S data and the original common W. It is valid after projecting onto original unequal-norm column pairs because that projection is imposed before replacement. It does not transfer a whole equal-norm bound to an unrelated frequency sector.

The exact retained principal-density factor g(mn)=g(m)g(n) on coprime support is a bounded diagonal modulation. It does not factor A_U, a root, or the remaining coherent main. Principal rho^6 branches, especially same-class/rho=1, are not removed. Full signed13/12/global9/8, the infinite complement, determinant, Lean and GRH claims are unchanged.

The author's source-pins receipt binds two historical context files (README and MASTER) from before the separately approved release-metadata append. This does not change any technical proof source; the review records those as historical context, not failed current technical pins. No author controls, old numerical tables, builds, browser sessions or publication actions were run.
