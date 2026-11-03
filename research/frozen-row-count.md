# Frozen-capacity row count

## Result and dependencies

The selected-row argument extends to the perturbed geometry with the fixed fourth-moment parameter kappa=3/4, without the source's Delta/4 capacity-comparison loss. This is a **conditional counting proposition** from the source's marked inverse moment, plain fourth moment, sixth-power amplification and simultaneous witness construction, with their stated masks, profiles and height uniformities. Those deep inputs and the prior7/8 theorem are not independently certified here. No new zero-free theorem or proof of GRH follows from this calculation alone.

Pinned input: math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob268c4e3206d460c617d3d2129742a72b831b3def in math commit4eaee87548250b2682affda7d05d947c05554bae. Relevant passages: witnesses4510–4552; actual bin ceiling6816–6831; marked moment9250–9270; fourth moment12532–12576; slot selection and counts15100–15443; height order15469–15491; balanced cutoff15959–15994. No primary arithmetic input is replaced by a numerical or GRH-conditional bound.

Assume beta_*<=7/8 as a separate, explicitly unverified source conclusion. Then the fourth moment's condition beta_*<=(1+kappa)/2 is satisfied at kappa=3/4. This does not assume the desired improved boundary. For retained bins above the floor a>51/100, the actual-zero ceiling gives

    1/50<delta=2a−1<=2beta_*−1<=3/4.

The floor bin itself need not have a witness and is excluded from this proposition. It must still be bounded separately in the final high estimate. We do not replace the source's dynamic Delta by beta_*−7/8<0 in its proposition: we reconstruct the selection proof with the admissible fixed capacity. The symbol tau below is the detector cutoff, not the small geometric perturbation t or an analysis-height exponent.

## Conditional statement

Quantifier order: for every requested epsilon>0 and bounded parameter ranges, first choose capacity decrements and a moment/rounding mesh threshold independent of the eventual fixed slot count. Then fix a finite physical slot system satisfying that threshold, with its required support and separation properties, and form a dynamic/amplitude bin of sixth-power-free rows q_u~U=Z^d, d>=d_min>0. The same arbitrary epsilon is not asserted for a previously fixed coarse slot system. Let x=q/delta in[0,1/2], where q is the length-weighted amplitude mean. Suppose total physical slot length ell/d exceeds7/37 by a fixed margin. Preserve all natural zero extensions, fixed finite ray-character coefficient expansions, prime-support disjointness, uniform smooth profiles, permitted polynomial-size masks fixed within each row sum, and the source's loss/height hypotheses.

For every tau in[1,3/2], the source moment and witness inputs then imply

    #B << U^[max(R_short(tau),L(tau))+epsilon] (1+T_1)^A,
    D=3−17x/9, P=(2−8x/9)(1−x), alpha=5/6,
    R_short(tau)=1−delta+delta P/D (3/2−tau),
    L(tau)=1−delta+(alpha−delta)(tau−1).

The order A is fixed before the external Fourier-tail order and before Z. It is uniform over moving rows and the permitted frozen outer labels. Constants may depend on the fixed slot system and epsilon. After fixing that system, choose its finite internal smoothness/height orders; the external Fourier-tail order is chosen later. Choosing

    J=(alpha−delta)D+delta P,
    tau_*=1+delta P/(2J),
    R_*=1−delta+(alpha−delta)delta P/(2J)

gives #B<<U^(R_*+epsilon)(1+T_1)^A. Here J>0 and1<tau_*<3/2 for physical delta>0. The no-prime alternative at tau=1 is

    #B << U^(1−2delta/3+epsilon)(1+T_1)^A,

with no slot-supply assumption. No statement includes floor-bin rows lacking actual witnesses.

## Derivation with fixed capacity

After subdivision by the fixed finite presentation and O((logU)^2) dyadic pairs, the witness inputs give actual lengths r,m, with r<=tau+o(1), r+m>=tau−o(1), m<=1/2+O(epsilon), and spikes |M_r|²>>U^(delta r−epsilon), |S_m|²>>U^(delta m−epsilon). Apply the uniform smooth-calculus input to the remaining rowwise parameters, after fixing the physical external parameters and the selected slot indices. This costs a fixed power of1+T_1, not a different exponent per row.

At base U, slot lengths are w_i=ell_i/d. Ordering the positive amplitudes g_i decreasingly and filling a requested length z fractionally gives gain at least qz. The reason is the weighted initial average is at least the total mean until all positive slots are exhausted; thereafter their full gain q ell/d is at least qz. Delete the at most one fractional slot. Its squared-amplitude loss is at most delta max_i w_i. Thus the retained whole-slot product has square at least U^(2qz−delta max_i w_i). A decrement nu_0 in the requested capacity costs at most2q nu_0, except where we instead use a no-slot moment. Since d>=d_min, a sufficiently fine fixed physical mesh gives uniformly small max_i w_i. It is selected after real losses and before the row sum, not adjusted to moving rows.

Dividing the marked inverse moment by the inverse and selected-slot spikes gives count exponent1−delta r−2qz. Dividing the plain fourth moment by |S_m|^4 and the same selected-slot spike gives1−2delta m−2qz. Using |S_m|² instead of its fourth power here would lose the claimed bound. The exact plain zero-loss capacity is now

    z_P(m)=(1−2m)/(6kappa)=2(1−2m)/9,
    2m+6(3/4)z_P(m)=1.

It equals the baseline capacity identically. There is therefore **no Delta/4 surcharge**, and no dependence on a positive bootstrap Delta at this step. The inverse capacity is z_M(r)=(1−r)/2.

The coefficient and mask requirements remain essential. Write the common negative-orientation witness row as nu(n) conjugate(chi_n(u)), nu in Theta. Its selected physical slot coefficient is conjugate(nu(p))1_(p in1_T), a fixed finite expansion in Theta. For the plain moment conjugate the entire product, both witness profiles and every selected prime factor. This yields the required positive orientation and coefficients nu(p)1_(p in1_T), preserving all zero extensions and support disjointness. No moving mask is made part of a fixed modulus. The moments must retain the same admissible mask in both plain copies and all selected slots. Large retained sixth-power-free rows induce outside Theta by ramification outside S; the finite exceptional physical rows remain separate. This is the same arithmetic family condition used in the source, not a conclusion of the exponent algebra.

For r>=1, inverse amplification gives exponent1−alpha+(alpha−delta)r<=L(tau)+O(epsilon), since delta<=3/4<alpha. It has a uniform limit at r=1; the marked moment is not invoked with a collapsing1−r margin. If m>=1/2, the no-slot plain moment gives at most1−delta. For r<1,m<1/2 the ideal selected exponents are

    A_I(r)=1−delta[x+(1−x)r],
    S_tau(r)=1−delta[4x/9+(2−8x/9)(tau−r)].

The second follows from m>=tau−r−o(1) and its uniformly negative derivative−2delta+8q/9. They cross at

    r_*(tau)=[(2−8x/9)tau−5x/9]/D,
    23/37<=r_*<=1,  1/3<=tau−r_*<=1/2.

Use the plain count for r<=r_* and the inverse count for r>=r_*. Because the former is increasing in r and the latter decreasing, both chosen counts are at most their crossing value R_short(tau). These inequalities hold on the entire stated parameter rectangle, not just on a rational grid.

On the inverse side, request z=z_M(r)−nu_0 if positive. Then1−r−2z=2nu_0, and3−2r−8z=4(1−r−2z)+(2r−1)>=9/37. These are fixed positive marked-moment margins. On this side z_M(r)<=7/37. On the plain side m>=1/3−O(epsilon), so z_P(m)<=2/27+O(epsilon). The assumed supply margin therefore permits either choice. If a capacity is at mostnu_0, the no-slot inverse or plain count is at most1−delta+O(nu_0), already below the claimed envelope. These cases include the limiting r=1 and m=1/2 without negative capacities or shrinking moment margins.

The no-slot calculation sets gain zero, regardless of the amplitude-bin x. At tau=1, the two short exponents1−delta r and1−2delta(1−r) cross at r=2/3 with value1−2delta/3; long witnesses have exponent at most1−delta. Thus that alternative does not request any prime supply.

Finally D>=37/18 and P>=7/9. Since alpha−delta>=1/12, J>delta P>=0. The displayed tau_* lies in[1,3/2), and direct subtraction gives

    D(R_short(tau)−L(tau))=delta P/2−J(tau−1).

At tau_* the two bounds equal R_*. R_short decreases in tau and L increases, so this is the minimum of their maximum on[1,3/2]. The delta=0 endpoint is included only in the algebra checks; physical bins have delta>1/50.

## Perturbed supply and heights

For t=1/100000, ell_t=1/6+t and h_t=13/16+3t/2. The required supply is valid through d<=h_t+zeta whenever

    0<=zeta<37ell_t/7−h_t=23/336+53t/14.

This is a strictly positive target-independent room for the upper extension. All physical slots are the same fixed slots used in the probe; errors with g_i=0 do not falsely acquire a positive spike. The mesh can meet max_i ell_i/d_min below the moment threshold and rounding-loss budget. The geometric supply calculation does not establish the moment or nonprincipal contour estimates.

After every internal moment/detector seminorm and height order is fixed, let A_ht dominate the finite height exponents. Choose an analysis-height exponent omega_ht>0 at most d_min epsilon_ht/[20(A_ht+1)] and all inherited detector ceilings. For T_1=Z^omega_ht and U>=Z^d_min,

    (1+T_1)^A_ht <=2^A_ht Z^(d_min epsilon_ht/20)
                    <=U^(epsilon_ht/10)

eventually. The remaining factor2^A_ht is absorbed in the eventual threshold; if A_ht=0 the conclusion is immediate. Only then increase the external Fourier-tail order. No internal order or physical profile may depend on that later choice. This preserves the source's order-of-choices contract, rather than asserting a height-free moment uniformly without a ceiling.

## Verification and next step

FrozenRowCount.lean verifies an actual finite complex moment-to-cardinality inequality, the exact plain capacity, coefficient/crossing bounds on the full real rectangle, the exact short crossing, the balanced cutoff and supply inequality. All hypotheses are explicit; these are not Lean proofs of the arithmetic moment bounds or the detector. scripts/check_frozen_row_count.py performs exact deterministic rational checks of the formulas, boundary cases and finite moment arithmetic; it does not certify the underlying analytic estimates. Independent adversarial review is recorded separately.

Result: the frozen-capacity row-count interface closes **conditional on** the listed source moments, witnesses and prior7/8 bound. It is not an unconditional new zero-free region. The scalar identity, low reflected-energy application, remaining shared nonprincipal central contours and their height/tail contracts still need verification. Next concrete task: inspect the general reflected-energy application at the perturbed rescaled geometry (source7747–7804,8239–8342,8590–8633), tracking subset losses and seminorm dependencies. If it cannot be justified, isolate the precise missing estimate or counterexample. Do not repeat the completed frozen-capacity algebra as new progress.
