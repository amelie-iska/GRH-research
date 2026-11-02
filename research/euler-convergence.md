# Finite Euler products: a precise obstruction and constructive replacements

## Scope and source inspection

This note is read-only mathematical research for the GRH workspace. I read all of the current `papers/core.tex` (182 lines), `papers/details.tex` (189 lines), and the repository README (52 lines) under `/Users/amelieschreiber/Documents/LaTeX-projects/GRH`. I did not edit them, install software, use MCP, authenticate, or publish. This requested `/tmp` report is the sole generated artifact for this task.

The main conclusions are rigorous elementary complex-analysis deductions. They neither assume nor prove GRH. They sharpen the current research interface: **the same finite prime-diagonal Euler determinants, multiplied only by nowhere-vanishing holomorphic normalizations, cannot converge locally uniformly through a nontrivial zero.** There are, however, explicit arithmetic approximants that do converge there unconditionally once one permits additive cancellation and unrestricted finite-level zeros.

## 1. Definitions, parity, and domains

Let χ be primitive of conductor q, set a=(1−χ(−1))/2∈{0,1}, and use the convention already in `core.tex:2–8`:

Gχ(s)=(q/π)^((s+a)/2) Γ((s+a)/2),
Λχ(s)=Gχ(s)L(s,χ).

The positive real logarithm defines the conductor factor. Put H+={Re(s)>0} and S={0<Re(s)<1}.

For both even characters (a=0) and odd characters (a=1), Gχ is holomorphic and nowhere zero on H+. Its possible gamma poles lie at s=−a−2j, j≥0, outside H+. Consequently Λχ and L(s,χ) have exactly the same zeros, with the same multiplicities, in S. Gamma's lack of zeros and its pole locations are recorded in [NIST DLMF §5.2](https://dlmf.nist.gov/5.2).

For primitive q>1, χ is nonprincipal and the completed function is entire. For q=1, χ is trivial and Λ1(s)=π^(−s/2)Γ(s/2)ζ(s) has poles at 0 and 1. The entire Riemann target is ξ(s)=s(s−1)Λ1(s)/2. In H+, Λ1 is holomorphic on the connected punctured domain H+\{1}; ξ is holomorphic throughout H+. At a nontrivial zero ρ, choose a closed disk entirely in S; it meets none of these poles or pole-clearing zeros. Standard Dirichlet-function analytic facts and the distinction between even/odd trivial zeros are summarized in [DLMF §25.15](https://dlmf.nist.gov/25.15).

Connectedness is needed for a global identity-theorem continuation or to infer that a nonzero target has isolated zeros. The local obstruction below only needs a common disk on which all relevant functions are holomorphic and the approximants are zero free.

## 2. The zero-free finite Euler products

For a finite set of primes P, define

D_P(s)=∏_{p∈P}(1−χ(p)p^(−s)),
E_P(s)=D_P(s)^(−1),
T_P(s)=diag(χ(p)p^(−s))_{p∈P}.

Thus det(I−T_P)=D_P=E_P^(−1). Primes dividing q contribute the factor 1, since χ(p)=0. For other primes |χ(p)|=1.

**Lemma.** Both D_P and E_P are holomorphic and nowhere zero on H+.

**Proof.** For σ=Re(s)>0,

|χ(p)p^(−s)|=p^(−σ)<1

at an unramified prime. Thus no denominator or factor vanishes. Each p^(−s)=exp(−s log p) is entire. The finite products and reciprocal products therefore have the stated property. In fact, writing χ(p)=exp(iθp), every zero of an individual factor is

s=i(θp−2πk)/log p, k∈Z,

on Re(s)=0. The reciprocal product has poles there, and no zeros anywhere. ∎

This statement holds regardless of how the prime cutoff grows, and regardless of GRH.

On Re(s)>1, increasing prime cutoffs give E_P→L and D_P→1/L locally uniformly. The orientation does not change under analytic continuation. For any finite P, the canonical logarithm on H+ satisfies

log D_P(s)=−∑_{p∈P}∑_{k≥1} χ(p)^k/(k p^(ks)),
log E_P(s)=+∑_{p∈P}∑_{k≥1} χ(p)^k/(k p^(ks)).

The determinant identity already stated at `core.tex:132–148` is therefore indispensable.

## 3. Precise no-go theorem, including a quantitative boundary obstruction

**Theorem.** Let Ω be a connected open subset of H+. For each N let A_N be either D_{P_N} or E_{P_N}, and let h_N be holomorphic and nowhere zero on Ω. Suppose h_N A_N converges locally uniformly on Ω to a holomorphic f. Then either f≡0 or f is nowhere zero on Ω.

In particular, if f is a completed Dirichlet L-function, or the Riemann ξ-function, is not identically zero, and Ω contains one of its nontrivial zeros, this convergence is impossible.

**Proof by Rouché.** Suppose f≢0 has a zero ρ of multiplicity m≥1. Choose r>0 such that the closed disk D={|s−ρ|≤r} lies in Ω, f has no other zeros in D, and f is nonzero on ∂D. Put

b_D=min_{s∈∂D}|f(s)|>0.

The functions h_N A_N have no zeros anywhere in D. If

sup_{∂D}|h_N A_N−f|<b_D,

Rouché's theorem says that h_N A_N and f have the same number m of zeros inside D, a contradiction. Local uniform convergence would give this inequality for large N. ∎

The proof yields the stronger fixed lower bound

sup_{∂D}|h_N A_N−f|≥b_D for every N.

Equivalently, max_{∂D}|(h_N A_N−f)/f|≥1. Thus convergence fails already on an enclosing boundary circle; it is not merely a failure to hit the center exactly. This is the zero-free case of Hurwitz's theorem, here proved directly rather than used as a black box.

**Local version.** It is enough that h_N be holomorphic and nonzero on a neighborhood of this particular closed disk. The normalizations may have zeros or poles elsewhere. Therefore fixed pole-clearing factors s(s−1), conductor factors, gamma factors, root-number phases, and exp(α_N+β_Ns) do not remove the obstruction at any nontrivial zero.

**No GRH assumption.** Even if every nontrivial zero lies on Re(s)=1/2, raw finite Euler products still have no zeros near those points. Hence the proposed convergence is impossible even in a world where GRH is true. This is a stronger objection to these particular approximants than merely observing that their convergence would imply GRH.

**Connected overlap consequence.** If a zero-free family h_N A_N matches Λ on an open Euler-product region V⊂Ω and is locally uniformly bounded on a connected Ω reaching a nontrivial zero, Montel plus the identity theorem gives local uniform convergence to Λ throughout Ω, contradicting the theorem. Thus these simultaneous assumptions are inconsistent for this family. At least local boundedness, the matching assertion, or the proposed family must fail. Merely adding “prove stronger uniform bounds” to the same approximation plan cannot solve it.

Removing ρ from the convergence domain does not help if the approximants remain holomorphic and zero free across the full disk and convergence is still asserted on an enclosing circle. A slit domain excluding that circle can support a branch of log Λ, but supplies no convergence statement through ρ.

## 4. Reciprocal determinants, poles, and gamma factors

Three different targets must not be interchanged:

| Finite object | Initial limit on Re(s)>1 | Behavior at a zero ρ of Λ |
|---|---|---|
| D_P=det(I−T_P) | 1/L | Analytic continuation of 1/L has a pole |
| E_P=det(I−T_P)^(−1) | L | Continued L has a zero |
| Gχ E_P | Λχ | Same zero and multiplicity as L in S |

Multiplying a determinant by a nonzero gamma/conductor factor cannot exchange a zero and a pole. The completed reciprocal target is 1/Λχ=Gχ^(−1)/L, so its natural finite orientation is Gχ^(−1)D_P, not Gχ D_P.

An ordinary locally uniform limit of holomorphic functions is holomorphic, so zero-free finite D_P cannot converge in the ordinary sense to the reciprocal L-function on a neighborhood of its pole. Passing to spherical/meromorphic local uniform convergence does not evade the local zero obstruction either: if zero-free holomorphic D_P converged spherically to 1/Λ near ρ, their reciprocals E_P would converge spherically to Λ. Since Λ is finite and bounded on a smaller closed disk, this implies ordinary uniform convergence there, and Hurwitz/Rouché gives the same contradiction.

For q=1 one must also handle the pole at 1 at the finite level. The naive functions

(s(s−1)/2)G1(s)E_P(s)

vanish at s=1 for every finite P because E_P(1) is finite, whereas ξ(1)=1/2. Thus simply multiplying a finite Euler product by the target's pole-clearing factor creates an additional persistent wrong zero. A meaningful approximant to a meromorphic target must reproduce its principal part before pole clearing, or use a different entire approximation scheme.

## 5. Ordinary multiplicative regularization does not create missing zeros

One can obtain genuine convergence further left by a regularized determinant, but it does not produce L's zeros. For an integer m≥2 put

D_{P,m}(s)=∏_{p∈P}(1−z_p(s)) exp(∑_{j=1}^{m−1}z_p(s)^j/j),
z_p(s)=χ(p)p^(−s).

Every finite factor is zero free on H+. On each compact subset of Re(s)>1/m,

log D_{P,m}(s)=−∑_{p∈P}∑_{k≥m}z_p(s)^k/k

converges absolutely and uniformly as P exhausts the primes, because |z_p|≤p^(−δ) and ∑_p p^(−mδ)<∞ for δ>1/m. The limit is exp of a holomorphic function, hence nonzero there.

This is a valid constructive regularization, not a contradiction to the no-go theorem. On Re(s)>1 its identity is

D_m(s)=L(s,χ)^(−1) exp(∑_{j=1}^{m−1}(1/j)∑_p χ(p)^j p^(−js)).

The removed lower prime powers carry essential analytic information. Their continuations cannot be silently treated as globally holomorphic, nowhere-zero normalizations across L zeros. The regularized determinant of the same prime diagonal cannot become a completed L-function merely by being called a regularized determinant.

## 6. Constructive replacement for every nonprincipal character

This gives unconditional locally uniform approximation through all nontrivial zeros using coefficients χ(n), without knowing any zero locations.

Let χ be any nonprincipal character modulo q (in particular every primitive character of conductor q>1). Define

Aχ(x)=∑_{1≤n≤x}χ(n),
Bχ=max_{0≤r<q}|∑_{n=1}^r χ(n)|≤q,
S_N(s,χ)=∑_{n=1}^N χ(n)n^(−s).

The sum over a complete period is zero, so |Aχ(x)|≤Bχ for all x≥0. Each S_N is entire in s.

**Proposition: exact Abel tail and bound.** For σ=Re(s)>0,

L(s,χ)−S_N(s,χ)
=−Aχ(N)N^(−s)+s∫_N^∞ Aχ(x)x^(−s−1) dx,

and consequently

|L(s,χ)−S_N(s,χ)|
≤Bχ(1+|s|/σ)N^(−σ).

**Proof, including the sign.** Partial summation between integers N<M gives

∑_{N<n≤M}χ(n)n^(−s)
=Aχ(M)M^(−s)−Aχ(N)N^(−s)
 +s∫_N^M Aχ(x)x^(−s−1) dx.

The first endpoint tends to zero when σ>0, and the integral converges absolutely there because Aχ is bounded. This proves the exact tail and shows that the Dirichlet series itself converges in this half-plane. It agrees with L on Re(s)>1, hence represents its continuation on H+ by uniqueness. Bounding the endpoint and using ∫_N^∞x^(−σ−1)dx=N^(−σ)/σ gives the inequality. ∎

For a compact K⊂H+, set

δ_K=min_K Re(s)>0,
M_K=max_K |s|,
G_K=max_K |Gχ(s)|<∞.

Then the completed approximants

Λ_{N,χ}^{sum}(s)=Gχ(s)S_N(s,χ)

are holomorphic on H+ and satisfy the explicit compact-uniform bound

sup_K|Λχ−Λ_{N,χ}^{sum}|
≤G_K Bχ(1+M_K/δ_K)N^(−δ_K).

This formula handles both parities: a=0 for even χ and a=1 for odd χ. The correct gamma factor is bounded and nonzero on each such K; it introduces no new nontrivial zeros. The constants are explicit in q, the character's partial-period sums, and the compact set. This is not a uniform-in-conductor GRH estimate.

The finite sums have cancellations and can have zeros in S. Rouché therefore permits, rather than forbids, convergence to L zeros. If D is a small disk around a zero ρ of multiplicity m and b_D=min_{∂D}|Λχ|>0, then every N satisfying

G_D Bχ(1+M_D/δ_D)N^(−δ_D)<b_D

gives exactly m zeros of Λ_{N,χ}^{sum} inside D, counted with multiplicity. The construction uses only χ(n); zero locations are used in the convergence proof, not as input data.

These finite completed sums need not be entire on all of C: their gamma poles at nonpositive points need not be canceled by a finite Dirichlet sum. The proved domain is H+, which already includes the whole open critical strip.

## 7. Constructive replacement for zeta: reproduce the pole first

For N≥1 let

S_N^ζ(s)=∑_{n=1}^N n^(−s),
Z_N(s)=S_N^ζ(s)+N^(1−s)/(s−1).

Z_N is meromorphic with precisely the desired simple pole at s=1 and residue 1. Define the remainder on H+ by

R_N(s)=−s∫_N^∞ {x} x^(−s−1) dx,

where {x}=x−floor(x). The integral is holomorphic on H+ and satisfies

|R_N(s)|≤(|s|/σ)N^(−σ).

**Exact formula.** On H+\{1},

ζ(s)=Z_N(s)+R_N(s)
=∑_{n=1}^N n^(−s)+N^(1−s)/(s−1)
 −s∫_N^∞ {x}x^(−s−1)dx.

**Proof, with the sign checked.** For σ>1, the counting function for n>N is floor(x)−N. Partial summation gives

∑_{n>N}n^(−s)
=s∫_N^∞(floor(x)−N)x^(−s−1)dx.

Substitute floor(x)−N=(x−N)−{x}. Direct integration gives

s∫_N^∞(x−N)x^(−s−1)dx=N^(1−s)/(s−1),

leaving the minus-sign remainder displayed above. Since its integral converges locally uniformly on H+, this identity continues meromorphically there. The bound follows from 0≤{x}<1. ∎

This elementary Euler summation formula is also recorded as [DLMF equation 25.2.8](https://dlmf.nist.gov/25.2.E8).

Now clear the pole at the finite level. Set g(s)=π^(−s/2)Γ(s/2) and

ξ_N^{sum}(s)
=(s g(s)/2)[(s−1)S_N^ζ(s)+N^(1−s)].

**Proposition.** Every ξ_N^{sum} is holomorphic throughout H+, including s=1, and ξ_N^{sum}→ξ locally uniformly there. Moreover ξ_N^{sum}(1)=1/2 for every N.

**Proof.** The bracket is entire, g is holomorphic on H+, and no division by s−1 remains. At s=1 the bracket is 1 and g(1)=1, giving 1/2 exactly. Away from 1,

ξ(s)−ξ_N^{sum}(s)=(s(s−1)g(s)/2)R_N(s).

Both sides extend holomorphically through 1. For every compact K⊂H+,

sup_K|ξ−ξ_N^{sum}|
≤[max_{s∈K}|s²(s−1)g(s)|/(2δ_K)] N^(−δ_K).

This tends to zero and proves the assertion, including compact sets containing 1. ∎

Again, the approximants may have zeros anywhere in H+, so zero convergence follows by Rouché without locating zeros on the critical line. There is no false fixed zero at 1.

The restriction to H+ matters. These particular approximants should not be advertised as a global entire approximation scheme: at s=0 their removable extension gives zero for every N, whereas ξ(0)=1/2. This boundary issue does not affect any nontrivial zero or the asserted H+ convergence. For global entire approximation use the Taylor scheme below, or a separately controlled higher-order continuation scheme.

## 8. What minimal change is necessary, and what remains unresolved

### Necessary change in zero structure

If a nonzero holomorphic target has a zero of multiplicity m, every locally uniformly convergent holomorphic approximation must eventually have m zeros in each sufficiently small enclosing disk. Thus **zeros must be allowed in the approximants**. Changing only a nonvanishing normalization cannot suffice.

Possible changes include additive tail corrections, integer Dirichlet partial sums, Taylor polynomials, or a genuinely different global operator family. Calling an additional factor a “normalization” does not remove its mathematical role: if it introduces the missing zeros, it carries the essential zero information and is no longer nowhere vanishing.

Simply shifting each local factor to 1−χ(p)p^(−(s−1/2)) moves its zeros onto the critical line but changes the Euler identity to the shifted L-function's reciprocal on its convergence half-plane. It does not preserve the desired arithmetic identity. Any proof of convergence of such critical-line-only approximants to Λ would again carry the full GRH obligation.

### A global entire benchmark without assuming GRH

For primitive q>1, Λχ is entire; for q=1 use ξ. For either entire target f, its Taylor polynomials about any fixed center converge locally uniformly on all of C. This is unconditional and does not use its zero locations as input: coefficients are derivatives of the known analytic function, which may be computed from independently established continuation formulas. Taylor polynomials have unrestricted zeros. They give a convergence benchmark, not a self-adjoint Hilbert–Pólya construction.

Likewise the Dirichlet-sum approximants above genuinely establish convergence from explicit arithmetic coefficients on H+. What remains is a separate spectral/positivity theorem.

### Residual self-adjointness obligation

Neither S_N(s,χ) nor Z_N(s) is automatically the centered characteristic polynomial of a fixed self-adjoint matrix. They are finite sums of exponentials in s; multiplication by gamma does not change that fact. A scalar representation as det(1−A_N(s)) with A_N(s)=1−F_N(s) is formally always possible and supplies no self-adjoint spectral content.

To use `core.tex:24–45`, one still needs a new independently defined sequence with all finite-level zeros on Re(s)=1/2 and locally uniform convergence to the same target. Replacing an arithmetic transfer by its Hermitian part is not determinant preserving, as the current paper already proves. Imposing unknown critical-line zero locations as input would be circular.

The positive results here solve **a convergence subproblem with unrestricted zeros**. They do not solve the conjunction of correct arithmetic determinant, self-adjoint spectral realization, and critical-line zero location.

## 9. Implications for the current papers, without source changes

- `core.tex:112–130` currently excludes an absolute prime-tail shortcut. The new theorem strengthens this: for nowhere-vanishing normalized raw finite Euler products, compact-uniform convergence through a nontrivial zero is structurally impossible, not merely unsupported by that tail estimate.
- `core.tex:55–71` is a valid normal-family interface. Its hypotheses cannot all hold for those raw Euler approximants on a connected zero-containing domain matching the Euler region.
- `details.tex:137–154` Tracks A/B should explicitly distinguish preserving a raw prime diagonal from changing the approximation scheme. A regularized prime diagonal alone still cannot supply the target zeros. The arithmetic Dirichlet-sum and pole-subtracted zeta constructions provide a concrete alternative convergence benchmark.
- `details.tex:114–134` correctly warns that canonical products built from hypothetical critical-line zeros can restate RH. The constructive sums above avoid importing zero locations but do not provide self-adjointness.
- A useful next acceptance criterion is an identity or a provable error bound relating a new spectral determinant to these independently convergent arithmetic approximants, while retaining control of the finite-level zero structure. Without that bridge, neither family transfers its useful property to the other.

## Status

Proved here: finite-Euler zero-free obstruction with an explicit boundary-error lower bound; reciprocal/pole clarification; a convergent but zero-free regularized-prime model; exact Abel tails and compact-uniform completed approximants for nonprincipal characters; exact pole-subtracted zeta tails and holomorphic ξ approximants at 1; and the separation of convergence from the remaining self-adjointness obligation. All are classical-analysis deductions, not a new proof of RH/GRH. Original sources remain unchanged.
