# Compensated principal residue at the perturbed geometry

Research heartbeat, 2026-11-02 local date. Target: the quantitative principal normalizer and residue estimate left open in the previous Euler-correction run.

Immutable input: September paper in math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, source commit4eaee87548250b2682affda7d05d947c05554bae, blob268c4e3206d460c617d3d2129742a72b831b3def. Focused rereading:1531–1642,5570–5835,6173–6328,7004–7044,8775–8905,9050–9097,15548–15669 and16270–16372. Sources remain unchanged.

## Status and inherited inputs

The local correction and its Euler identities are inherited from the displayed source formulas, with the larger region proved in euler-correction.md. The current result verifies their principal multiplier, normalizer and residue interface at the perturbed parameters. The contour comparison retains explicit inherited contracts: the same physical probe's exact high identity; the source's Mellin test holomorphy, rapid integrated and trace tails; and polynomial reciprocal control on Re s=beta_*+e. This is not an independent certification of all Poisson/Gauss identities, energy estimates, row counts or the claimed7/8 theorem. No smaller zero-free half-plane or GRH theorem is announced.

## Uniform local estimate

Let D2' be Re x>=3/4, Re w>=19/20, Re z>=33/200. At a principal row, the source's exact cancellation for B_p+1 and the residual E give the four error powers

    Q^(−Re x), Q^(−6Re z), Q^(4−5Re x−6Re z), Q^(1−Re w−6Re z).

The first two terms arise from V/(1−V)−D. The amplified residual costs Q^(Re x)|E|, producing the last two powers; the unamplified residual terms are smaller since Re x>0. After the uniform finite enlargement of P0 from the previous run, every individual H_p is bounded away from zero on D2', so B_p=G_p/H_p is holomorphic there. Thus

    B_p=−1+O(Q^(−kappa)),
    kappa=min(Re x,6Re z,5Re x+6Re z−4,Re w+6Re z−1)>=37/50.

This is uniform in all imaginary parts and target phases on the stated tube. On any fixed real box, G_p=H_p B_p=O(1). Ideal counting and the unselected product majorant give

    |mathfrak H_eta,1,Z(s,w,z)| << product_i P_i^(Re z)=Z^(ell Re z),

with height degree zero. The constant is for a fixed real box, not for unbounded Re z. This verifies the quantitative principal rectangle contract after replacing the old domain by D2'.

## Exact slot normalization and power saving

For fixed positive slot lengths ell_i summing to ell, let P_i=Z^ell_i and use the same nonnegative annular weights and disjoint identity-ray prime sets as the physical probe. Define

    S_i(Z)=sum_p W_i(Q/P_i)Q^(−5/6),
    A_T(Z)=(−1)^K Z^(−ell/6) product_i S_i(Z).

The unconditional fixed-extension prime ideal theorem implies

    S_i(Z) ~ P_i^(1/6)/(|T|log P_i) integral W_i(y)y^(−5/6)dy.

The integral is positive, so S_i>0 for sufficiently large Z. A further fixed finite deletion eventually lies outside each annular window. No uniformity in a moving ray modulus is used. A possible exceptional real zero is not excluded: for the fixed extension its beta1<1 contribution is asymptotically smaller. The primary theorem checked is Thorner–Zaman2019, Theorem1.1; only this fixed-extension consequence is needed.

Writing epsilon_p=B_p+1, the exact i-th residue slot is

    sum_p w_p B_p=−S_i(1+rho_i),
    rho_i=−sum_p w_p epsilon_p/S_i,
    w_p=W_i(Q/P_i)Q^(−5/6)>=0.

Hence |rho_i|<=C P_i^(−37/50), with constants for the fixed annular supports. Nonnegative individual weights, not merely a positive total mass, are essential. The same A_T is used in the low normalization and the high comparison. Its signed asymptotic is

    A_T(Z) ~ c_T(log Z)^(−K),
    c_T=(−1)^K |T|^(−K) product_i [ell_i^(−1) integral W_i(y)y^(−5/6)dy] !=0.

In particular |A_T|^(-1)<<_epsilon Z^epsilon; A_T is positive only when K is even. Elementary exponential growth dominates the fixed power of log Z, so this subpower loss does not invoke any zero-free estimate.

Let ell_min=min_i ell_i>0, with a nonempty finite slot system fixed before the target. For a common local error bound delta<=1, the finite product satisfies

    |product_i(1+rho_i)−1| <= (2^K−1)delta.

An induction using |1+rho_i|<=2 proves this inequality. Consequently R_eta,Z=product_i(1+rho_i)−1 is O(Z^(−mu)) with the explicit choice

    mu=(7/10)ell_min < (37/50)ell_min.

It is uniform on the entire line Re s=beta_*+e, with no height factor; its exponent is chosen before the target. At the double residue one obtains exactly

    mathfrak H_eta,1,Z(s,1,1/6)
       =H_eta(s) Z^(ell/6) A_T(Z)(1+R_eta,Z(s)).

This proves the principal normalizer and relative-error hypotheses rather than assuming that an unnormalized finite sum already has the desired scalar signal.

## Extending the principal contour comparison

Assume the inherited exact high identity and Mellin/reciprocal contracts stated above. Replace the old second Euler domain in that interface by D2'. For any sigma0>=3/4 with beta_*>sigma0, the proof moves the principal row from the absolute lines to

    Re s=beta_*+e, Re w=1+e, Re z=1/6+e.

Next move w to19/20, crossing only w=1. In its residue move z to33/200=1/6−1/600, crossing only z=1/6. The unresidued w integral leaves z at1/6+e. All paths remain in D2'; the reciprocal stays strictly to the right of beta_*, using only its definition. At a principal pole the reciprocal has a zero and adds no residue. The Mellin factors supply the independent rapid-decay height directions; their trace tails justify horizontal joins, not merely vertical integrated tails. The arithmetic correction has height degree zero on these real boxes.

For general positive l_x,l_y,h=1−l_x+ell and C(s)=s+l_x/2−1+h/6, the outside exponent is

    l_x/2+Re s−1+h Re z+l_y(Re w−1).

After division by c_S A_T, the two leftover integrals and the residue error are therefore bounded by

    Z^[C(beta_*)+(1+h)e−l_y/20+epsilon]
    + Z^[C(beta_*)+e−h/600+epsilon]
    + Z^[C(beta_*)+e−mu+epsilon].

Here epsilon includes the normalizer's subpower allowance. Only the main double-residue integral moves right to Re s=2; no continuation of the relative error away from the global line is needed. The same c_S contains the factor1/6 from the zeta(6z) residue. These steps introduce no new7/8 restriction once the larger correction domain is supplied.

For t=1/100000, use the previously specified geometry ell=1/6+t, l_x=17/48−t/2, l_y=23/48−t/2, h=13/16+3t/2. It has C(s)=s−11/16 and target sigma_t=349999/400000>3/4. All three losses are positive before choosing e and epsilon. Choose e=epsilon bounded by the minimum of1/10000, (l_y/20)/(8(1+h)), (h/600)/8 and mu/8. Each remainder has a fixed positive saving relative to C(beta_*). The remaining nonprincipal contour, low energy and frozen-capacity row-count extensions are not verified by this principal calculation.

## A separate pointwise boundary

At the residue put v=Q^(−1), d=eta(p)Q^(−s), r=alpha(p)^(−6)eta(p)^6 Q^(3−6s), N=1−vr−(1−v)d. Exact simplification gives

    B_p+1=(1−v)[r/d−vr−(1−v)d]/N,
    (B_p+1)/(r/d)−1=[−v(1−r)+(1−v)^2 d(1−d/r)]/N.

For fixed1/2<sigma=Re s<=3/5 and Q>=4, |N|>=1/4, |r|<1, and

    |(B_p+1)/(r/d)−1|
       <=8Q^(−1)+4Q^(−sigma)+4Q^(4sigma−3) ->0,
    |B_p+1| ~ Q^(3−5sigma).

The bounds are uniform in phases and heights on that vertical line. Thus a pointwise negative-power error around−1 fails at or below3/5.

There is an exact arithmetic example at the boundary. For eta=1 and an inert rational prime p≡2(mod3), its ideal has norm Q=p² and primary generator−p, hence alpha^(−6)=1. At real s=3/5 one has r=d, so P_p*=0 and B_p=−1/Q exactly. This remains compatible with a fixed identity-ray restriction: choose a positive integer M with M O contained in its modulus, and take rational primes p≡−1(mod3M). The fixed progression has infinitely many primes and gives primary generators−p congruent to1. The local error tends to1 along these primes.

This rejects the pointwise local approximation in that range, not cancellation in prime averages. Inert prime ideals have density zero among prime ideals ordered by norm; their existence does not contradict the slot average or a different normalizer. The earlier global7/12 obstruction for the unchanged correction is a distinct statement. Neither is a GRH counterexample.

## Verification and handoff

PrincipalResidue.lean checks the exact multiplier identities (including r=d), finite complex weighted normalization, transfer of a uniform error through nonnegative weights, and a finite-product error estimate. It does not formalize fixed-ray PNT, the arithmetic identification r=d at s=3/5, uniform prime-power asymptotics, or the contour integration. The Python checker uses exact fractions and Q(sqrt(-3)) samples at prime norms7and13, verifies the rectangle gaps, and checks illustrative positive loss allocations. Its sample slot counts are not certificates for the nonprincipal row-count admissibility conditions.

Result: the principal normalizer and principal-residue interface extend to the perturbed geometry under the explicitly inherited scalar/high/Mellin/reciprocal inputs. No new zero-free theorem is established. Next concrete task: prove the frozen-kappa=3/4 row-count extension in exponent-frontier.md section3b from the actual source capacities, preserving masks, fixed prime slots and all height orders; or verify the general reflected-energy application. Do not redo the completed local principal normalizer or infer full GRH from these partial interfaces.
