# Independent review: norm-radial signed profiles and a sixth-power row block

Verdict: **PASS for the scoped theorem below**, as classical prose mathematics. This is a scope/sharpness consequence for D-dependent common smooth profiles. It is not a fixed-profile counterexample, a new large-sieve theorem, a GRH counterexample, or a Lean result. No production source or earlier scientific output was changed by this review.

## 1. Scope and source novelty

Read the actual polynomial/residue definitions in `papers/uniform-cutoff-moment-core.tex`, `papers/hecke-type-i-core.tex`, `papers/masked-moment-{core,details}.tex`; the high-window identity and ideal count in `papers/signed-bilinear-{core,details}.tex`; the old arbitrary-column counterexample in `planning/reviews/book/short-row-gram.md`; current ordinary-conductor research and master/open/continuation records; and the raw phase implementation convention. A focused inventory scanned390 current research/paper/planning Markdown/TeX files, excluding this new task; exact search records are in the output directory.

The formula A_U=mu(r_U−1), its odd/nonzero consequence, the ideal-count constant and O(sqrt(D)logD) error are ALREADY recorded. The old arbitrary-column-weight counterexample also uses coherent rows, but explicitly replaces the original coefficients. I did not locate the present norm-radial sign profile on the actual A_U, its nonprincipal literal-unit/sixth-power-row lower bound, or its derivative-cost consequence in that searched material. That is the limited repository novelty. Generic finite-node interpolation, ideal sieving and the counting method are classical; no comprehensive literature-priority claim is made.

## 2. Norm groups do not merge ideals

Fix K=Q(omega), O=Z[omega], principal nu and fixed finite S containing primes above2,3. For rational p≠3: split p gives two distinct prime ideals of norm p, while inert p gives one prime ideal of norm p². In a squarefree ideal, a split rational exponent e is0,1,2; e=1 chooses one conjugate and e=2 chooses both. An inert exponent is0 or2, with a single inert prime ideal in the latter case. Thus a rational norm N determines the MULTISET of prime-ideal norms, although it need not determine the ideal. Consequently it determines mu(m), the divisor-norm multiset INCLUDING multiplicities, r_U(m), and A_U(m). Additional fixed S exclusions may remove some conjugate ideals but do not change this constancy among those remaining.

For example inert norm25 is permitted and has mu=−1, divisor norms(1,25); split norm49 has mu=+1, divisor norms(1,7,7,49). Rational squarefreeness must never replace ideal squarefreeness. The construction retains every actual good squarefree ideal in each active norm group.

Take integer U→infinity and D=U². On D<Nm<2D the accepted high-window identity gives A_U(m)=mu(m)(r_U(m)−1). Alternatively, inclusion-exclusion in the two cutoff constraints proves it directly: in any disjoint assignment with both long factors, the leftover ideal has norm<2 and must be the unit. Swapping the two full factors is fixed-point-free on a nonunit squarefree ideal, so r_U is even and |A_U|≥1. Denote this norm-group value by A_N.

## 3. The literal unit, phase convention and exact primitive conductors

Put epsilon=1+omega=zeta6 and delta=1+2omega, so delta²=−3. At a good prime ideal of norm q, Euler's definition gives

    chi_p(epsilon)=epsilon^((q−1)/6).

All good ideal norms are1 modulo6. For a=1+6r,b=1+6s, (ab−1)/6=r+s+6rs, so multiplication preserves this exponent modulo6. Therefore, EXACTLY on every good ideal,

    chi_m(epsilon)=epsilon^((Nm−1)/6)=:chi_epsilon(m).

This is independent of the conjugate prime choice. The implementation uses the same epsilon=1+omega reduction and identifies its six powers in the residue field; its zeta6-coordinate PH table is consistent. Conjugating a residue-symbol convention would invert every phase; it would leave conductor conclusions unchanged, but the displayed W must then be conjugated consistently.

For odd N≡1 modulo3,

    chi_epsilon = chi4(N) * omega^((N−1)/3),
    chi_epsilon² = omega^(2(N−1)/3) = omega^(−(N−1)/3),
    chi_epsilon³ = chi4(N).

The squared cubic character has the INVERSE orientation of omega^((N−1)/3). The quadratic norm character has exact conductor(2)²: alpha≡1 mod4 implies Nalpha≡1 mod4, but 1+2omega≡1 mod2 has norm3 modulo4. The cubic norm character has exact conductor delta³. Indeed Tr(delta gamma) is divisible by3 for gamma∈O, so N(alpha+delta³ beta)≡Nalpha mod9. Yet 1+delta²=−2 has norm4 modulo9 and is1 modulo delta², giving a nontrivial cubic value.

Explicit coprime local witnesses isolate the two parts. Alpha2=13+6omega has norm127, is1+2omega modulo4, and alpha2−1=2omega delta³; its character is−1 and its cubic part is1. Alpha3=−11 has norm121, is1 modulo4 and−2 modulo delta³, with alpha3−1=4delta² not divisible by delta³; its character is omega and its square is omega². Thus the local conductor exponents are minimal, not only upper bounds. The two conductors are coprime, so

    f_epsilon=(2)² delta³, Nf_epsilon=432;
    Nf_(epsilon^j)=432 for j=1,5; 27 for j=2,4; 16 for j=3.

All global units have norm1, so the norm characters are unit trivial and define finite Hecke characters of trivial infinity type in this class-number-one field. Norm7 gives value epsilon, proving order6 and nonprincipality of powers1…5. For a larger S, CRT supplies good representatives of the same nontrivial ray classes while avoiding the extra excluded primes; finite S deletion does not principalize the character.

The older real-profile choice uses the literal row−1: chi_m(−1)=chi4(Nm), with conductor16 and nonzero powers not all nonprincipal. It remains valid for its one-row bound. The epsilon upgrade avoids the principal-square issue.

## 4. A genuine common smooth profile and retained raw masks

Use phi(t)=exp(1−1/(1−t²)) for |t|<1, and0 otherwise. Define

    w_N=sign(A_N) conjugate(epsilon^((N−1)/6))

when at least one good squarefree ideal of norm N exists and D<N<2D, and w_N=0 otherwise. Set

    W_D(y)=sum_(D<N<2D) w_N phi(4(Dy−N)).

Distinct supports are disjoint and lie strictly inside(1,2), so this is one common C_c^infinity((1,2)) profile, independent of the row v. Its sup norm is1 for sufficiently large D. All its integer norm nodes have exactly the declared values; no exponential evaluation or per-ideal weight replacement is involved. For every fixed k,

    ||W_D^(k)||_infinity ≤ (4D)^k ||phi^(k)||_infinity,
    M_k(W_D)=sum_(j≤k)||(y partial_y)^j W_D||_infinity ≤ C_k D^k.

The Euler derivative estimate follows by the finite Stirling expansion and1≤y≤2. A version on any fixed smaller annulus is obtained by keeping only centers there; endpoint proximity is not essential.

For every nonzero good ideal v choose any generator beta_v and put u_v=epsilon beta_v^6. This is independent of the generator because every unit has sixth power1. The map v→u_v is injective, and Nu_v=(Nv)^6. The ideal v is ARBITRARY, may have repeated prime factors and may overlap column primes. Exact raw multiplicativity gives

    chi_m(u_v)=chi_epsilon(m) 1_((m,v)=1).

This retains, rather than deletes, the sixth-power collision mask. Every such row has the SAME underlying primitive row character chi_epsilon. Hence the actual source principal-residue indicator is zero, so P_(u_v)=0 and E_(u_v)=I_(u_v), with the original D^(−1/2) normalization. The independently primitive square has conductor27; S still deletes2 and3, including the2-prime even though it is unramified in that square.

At every selected row,

    E_(u_v)=D^(−1/2) sum_(m sf good;D<Nm<2D;(m,v)=1) |A_U(m)|.

The sum is real and nonnegative. No residue normalization, factor6, unit quotient or character-zero restoration has been inserted.

## 5. Exact triple density and the selected h=1 contribution

Let V_X={v good:Nv≤X}, with X→infinity and X≤D. Let T(D,X) count ordered triples(m,n,v) with m,n squarefree good in the open D-annulus, v∈V_X arbitrary, and m,n,v pairwise coprime. The ideal lattice count is

    A(Y)=kappa Y+O(sqrt(Y)+1), kappa=pi/(3sqrt3),

because the element lattice has covolume sqrt3/2, each ideal is principal, and exactly six unit generators represent it. In particular A(Y)≤C Y for Y≥1.

For a finite set of prime ideals, the local conditions are a finite Boolean combination of divisibility by p and p² in m,n and by p in v. Applying the lattice count to each fixed ideal multiple gives the joint density, uniformly along every sequence D,X→infinity. For t=(Np)^−1, a good local factor is

    (1−t)^3 [1+2t+t/(1−t)]
      =(1−t)^2(1+2t−2t²)
      =1−5t²+6t³−2t⁴.

Here the geometric series is essential: v is not assumed squarefree. At p∈S all three valuations are0, giving(1−t)^3. The infinite product

    C_S=prod_(p in S)(1−1/Np)^3
        prod_(p notin S)(1−5/Np²+6/Np³−2/Np⁴)

is positive: every factor is positive and its deviation from1 is O((Np)^−2).

To justify passing from finitely many primes to all, every omitted failure belongs to one of five events: p²|m, p²|n, p|gcd(m,n), p|gcd(m,v), or p|gcd(n,v). A(Y)≤CY bounds each event by C D²X/(Np)², even when a quotient scale is<1 (then the count is0). Thus the total tail is at most

    C D²X sum_(Np>P) (Np)^−2 = o_P(D²X),

uniformly in D,X. Taking D,X→infinity first at fixed P, then P→infinity proves

    T(D,X)=kappa³ C_S D²X+o(D²X).

Strict/inclusive norm endpoints do not change the main term. Restricting v to[X/2,X) gives exactly half the volume in the asymptotic; that finite dyadic set may be empty at small X.

For these SELECTED rows, every full A–A pair term after alignment is nonnegative. Keeping only(m,n)=1 therefore gives the actual selected h=1 contribution at least T(D,X)/D. Consequently the full original E energy satisfies

    sum_(0<Nu≤H)|E_u|² ≥ sum_(v∈V_X)|E_(u_v)|²
      ≥ selected-h1 ≥ (kappa³ C_S+o(1)) D X,
    X=H^(1/6).

The first inequality uses positivity of the OUTER sum of squared row values; it does not assert that the h=1 contribution over OTHER rows is nonnegative. No positive-semidefinite claim is made about the h=1-truncated Gram by itself. The result is for A–A, not a positive density claim for the C–C long-long weights, which can vanish.

The primitive ROW conductor432 must be distinguished from the PAIR character conductor q=mn of norm comparable to D² when h=1. A fixed row conductor does not turn that pair conductor small. The original raw v mask remains present throughout.

## 6. Sharpness and derivative cost, with the correct quantifiers

For H=D^theta with fixed0<theta<2/3, the current envelope H+D H^(1/6)+(DH)^(2/3) is dominated by D H^(1/6). The new D-dependent profiles show that term is attained up to constants/subpower losses within this profile-varying class. At theta=3/4 the lower exponent is9/8, whereas the current global upper exponent is7/6: the result does NOT prove global7/6 sharpness. Its gap above the H target is3/8.

Suppose alpha≥0 and, for EVERY epsilon>0, one claimed a bound uniform in these common profiles of the form

    energy ≤ C_epsilon M_k(W)^alpha (HD)^epsilon H.

The preceding lower bound and M_k(W_D)≤C_kD^k imply

    k alpha ≥ 1−5theta/6.

For a single fixed epsilon the necessary inequality is only
k alpha≥1−5theta/6−(1+theta)epsilon. With a D^epsilon loss instead, replace(1+theta)epsilon by epsilon. At theta=3/4 the all-epsilon requirement is k alpha≥3/8; a supnorm-only H(HD)^epsilon target is contradicted for epsilon<3/14. This is a NECESSARY tradeoff, not a sufficient estimate or a proof that a particular derivative order is optimal.

W_D changes with D and has unbounded derivatives. The theorem does not refute fixed-W bounds, bounded-seminorm profile classes, a nonnegative-real-W restriction, GRH, or any source estimate whose implicit constant depends on the actual profile/seminorms. The one-row−1 real variant has a weaker necessity k alpha≥1−theta. Unit/sixth-power rows are absent from the project's outside-S-nonunit guaranteed-subset fixture and from row blocks that exclude them; no lower bound for those restricted moments is inferred.

## 7. Independent diagnostics and acceptance checklist

Fresh standalone checks used no production imports or old audit entry points. `independent_check_v2.py` enumerated5647 actual squarefree good ideals through norm20000, retaining both split-prime labels, and6782 annular coefficient cases. It checked norm-group mu/divisor/r constancy, nonsquarefree rational norms, the raw−1 identity, actual ternary A_U, high-window parity and signed-profile positivity. It includes N8281,U90,A_U=3, so divisor multiplicity is exercised. The first smaller fresh diagnostic remains preserved.

`upgrade_check.py` independently checks the implementation's epsilon convention in split and inert residue fields,119 actual annular columns,13 arbitrary ideal v rows through norm80 (including both norm49 prime-square ideals),1547 raw sixth-power symbols, exact alignment, injective literal rows,155300 coprime triples and selected-h1/full-energy positivity. These finite checks do not prove the universal asymptotic count; the proof above does.

Required final-claim criteria: keep nu principal and S fixed; retain the complete ideal norm groups and arbitrary v; specify W_D as one common complex profile independent of v; preserve all raw masks and original normalization; state P=0 through the actual primitive character; keep the inverse orientation of the squared cubic character; use ball volume X versus dyadic volume X/2 correctly; claim positivity only on selected rows; separate fixed row and large pair conductors; state the all-epsilon derivative quantifier and profile-varying scope; identify the previously recorded count/parity lemmas as reused. Any production draft should be checked against these exact statements and frozen separately before integration.

No compiler/install, authentication, MCP activation, production edit, old-output rewrite or publication occurred. Primary BGL metadata was verified remotely against arXiv:1112.1650v1; its pinned full paper supplies the existing family convention, not a new imported analytic saving. This review is prose/finite bookkeeping, not Lean.
