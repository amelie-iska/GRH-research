# Joint orientation projection: exact limitation and structured signed-profile rotation

5 November 2026. Fresh bounded P7 attempt after the verified ordinary-conductor release. Read the latest post-release handoff and the joint Gauss, ordinary conductor, covariance-budget and high-window fragments pinned in source-pins-v1.json. All work is on the Linux research checkout, under the two authorized fresh joint-attempt directories.

## Outcome and boundaries

Projection onto the actual orientation-character span is an exact algebraic simplification, but its norm is precisely the original vector of coupled correlations Gamma. Projected Cauchy–Schwarz therefore supplies no new conductor/range factor by itself. Coherent-fiber restriction does not commute with this projection; its leakage has an explicit rank-one norm below.

The attempted stronger replacement by an orientation-variance budget is false on an actual permitted nonprincipal row family. For the selected rows u=epsilon beta_v^6, with epsilon=1+omega and principal nu, every orientation has the same correlation after removing its explicit epsilon phase. A common norm-radial profile can align the original A_U coefficients on those rows. The signed h=1 A–A contribution is then positive, even though the orientation variance of Gamma is exactly zero. This is a precise obstruction to that centering rule, not an obstruction to the fixed-profile target.

This rotation is compatible with the parent's candidate scale-dependent-profile lower bound. The present note verifies the exact joint-identity interface and masks, not its separate asymptotic coprime-triple count. The candidate lower bound D H^(1/6), if supplied by that count, is exponent9/8 at H=D^(3/4), still below7/6. No improved quantitative upper bound is obtained on the new A6=1 witness sectors (a1,a2)=(5/12,1/6) or pure a1=3/4. Those remain open.

## 1. Exact normalization of the orientation projection

Fix a good squarefree pair (h,q), q not1, and one common exact row weight F with every squarefree/ray/inter-factor/capacity mask. Keep the arbitrary sixth factor and its raw mask. Use the notation of papers/joint-gauss-details.tex:

    n=phi(q), ell=N(hq), Q=Nq,
    c_hq=Q^2 xi_q(-alpha) tau_beta(xi_q)/ell^6,
    A(K)=sum_(r in J) a_r conjugate(theta_r(K)).

Here J is precisely the active orientation set; excluded orientations have coefficient zero. The literal u0 phase is in a_r, as in the accepted formula. Define the correlation WITHOUT that separately displayed u0 phase by

    Gamma_r^F = c_hq sum_K B_F(K) conjugate(theta_r(K)).

This is exactly the orientation-by-orientation Fourier inversion underlying the accepted joint identity. The common nonzero c_hq is independent of orientation. In particular |c_hq|=Q^(5/2)/ell^6; at h=1 it is Q^(-7/2).

Use normalized inner product <f,g>=n^(-1)sum_K f(K)conjugate(g(K)), and let P_J project onto span{theta_r:r in J}. Distinct orientations are orthonormal. Consequently

    P_J B_F(K) = (c_hq n)^(-1) sum_(r in J) Gamma_r^F theta_r(K),
    sum_K |P_J B_F(K)|^2
          = (|c_hq|^2 n)^(-1) sum_(r in J)|Gamma_r^F|^2.       (1)

The bilinear pairing uses A in the conjugate span, so

    sum_K B_F(K) A(K) = sum_K (P_J B_F)(K) A(K).

Projected Cauchy therefore becomes EXACTLY

    |c_hq sum_K B_F A| <= ||a||_2 ||Gamma^F||_2.               (2)

After the original normalization it is D^(-1)||a||_2||Gamma^F||_2. The factors c_hq and phi(q) cancel. A factor such as sqrt(|J|/phi(q)) does not follow from the rank of P_J: projection rank alone never controls the fraction of a particular vector's norm in its range. For this actual B, any asserted bound on ||P_J B|| is, by (1), an asserted arithmetic bound on the very coupled Gamma vector being sought. This does not disprove a possible new arithmetic estimate; it identifies the exact missing estimate and prevents relabelling it as a projection consequence.

On the new witness sectors one may insert the accepted operator norm and trace budget, but this is worse. If R is the raw row-count scale, tr G << R D and tr G^2 <= Lambda tr G. With Lambda << D^(7/6+eta), full coefficient Cauchy gives a Frobenius envelope D^(11/8+eta) on R=D^(7/12) (mixed witness) and D^(35/24+eta) on R=D^(3/4) (pure witness). Both exceed D^(7/6). These powers are bookkeeping consequences of already accepted norms, not new lower bounds or new analytic estimates. No accepted exponent grid was rerun.

## 2. The coherent cut is rank one and does not commute with projection

Put k=omega(q) and

    C={K:x_p(K)^2=1 for every p|q},  |C|=n/3^k.

On C all theta_r equal the same character x_q. Thus for any a,

    sum_(K in C)|A(K)|^2 = n 3^(-k) |sum_r a_r|^2,
    sum_K |A(K)|^2 = n sum_r |a_r|^2.                         (3)

If after the common signs/phases the actual a_r are nonnegative, the coherent fraction is at least3^(-k), and for equal coefficients it is |J|/3^k. No fixed conductor power follows just from this count; k may be fixed and the actual coefficient direction may be coherent.

More precisely let M_C be multiplication by1_C. In the normalized orthonormal theta basis,

    P_J M_C P_J = 3^(-k) 11*,
    lambda=|J|/3^k,
    ||(I-P_J) M_C P_J||^2 = lambda(1-lambda).                 (4)

Indeed the first matrix has every entry3^(-k), and the squared leakage is T−T^2 for T=P_J M_C P_J. Here0<lambda<1 for q not1 and nonempty J. In particular projection does NOT preserve fiberwise pairings. While the full pairing with A is unchanged, the error in first restricting to C is bounded only by

    |sum_C (B_F-P_J B_F) A|
       <= sqrt(lambda(1-lambda)) ||(I-P_J)B_F||_2 ||A||_2.     (5)

All function norms in (5) are UNNORMALIZED counting ell^2 norms. With normalized L2 norms the unnormalized sum on its left would require an additional factor n. Replacing the actual B by P_J B on a coherent subset without paying (5) is an invalid step. Neither (3) nor (4) is a lower bound for the actual signed pairing: B may have cancellation on C. A new signed estimate must prove that cancellation or control the corresponding orientation-mean contribution; it cannot discard C by a dimension argument.

## 3. Rotation to the actual structured A–A weight

In the accepted high window 2D/7<=U^2<=D,

    A_U(m)=mu(m)(r_U(m)-1),  |A_U(m)|>=1

on every good squarefree active column. To obtain A–A from the published C–C/C–mu identity, replace BOTH factors r_U by r_U−1. This is the exact expansion of (C−mu)(C−mu), not a positivity assertion about covariance.

For principal nu, the literal unit value is norm-radial:

    x_m(epsilon)=epsilon^((Nm-1)/6 mod6).

The same holds for A_U(m): for squarefree good ideals the multiset of prime-ideal norms is determined by Nm, including repeated split rational-prime norms and inert prime norms. Divisor norm multisets, mu and r_U are therefore determined by Nm. This permits ONE common nodal profile with values

    W_(D,U)(Nm/D)=sgn(A_U(m)) conjugate(x_m(epsilon)).          (6)

This is a scale/cutoff-dependent profile, not one W fixed as D grows. A smooth construction uses disjoint fixed bumps at the interior integer nodes with width O(1/D), so ||W||_infty<=1 and ||W^(j)||_infty=O_j(D^j). ENDPOINT CORRECTION: a smooth profile supported in[1,2] vanishes at1 and2; (6) must be imposed only at strict interior nodes D<N<2D, or on a fixed inner annulus. It cannot hold with unit modulus at N=D,2D for integer D. Removing those boundary norm fibers or using an inner annulus preserves the candidate lower-bound order, subject to the separate counting proof.

Take one exact literal class u0=epsilon, set v1=...=v5=1, and let v6=v range over any finite set V of good ideals with chosen generators beta_v. These are actual rows u=epsilon beta_v^6, not principal rows: kappa_epsilon has order6 (already x_p(epsilon)=epsilon at a norm7 prime), and multiplication by a sixth power leaves its primitive character unchanged. Hence for nu=1 the principal residue is zero. The raw symbol is nevertheless

    x_m(epsilon beta_v^6)=x_m(epsilon)1_((m,v)=1),

not the constant primitive value with its restored primes.

For fixed h,q the pair mask is1_((v,hq)=1), independent of orientation. Put

    Z_(h,q)=#{v in V:(v,hq)=1}.

The corresponding exact F has its first five variables fixed at1. Directly, Gamma_r^F=Z_(h,q) for EVERY orientation. By the accepted Gauss completion,

    c_hq sum_K B_V(K) conjugate(theta_r(K))=Z_(h,q).           (7)

For h=1, m=r,n=q/r, the actual A–A coefficient is

    a_r^AA=(r_U(m)-1)(r_U(n)-1) W_m conjugate(W_n)
                                     theta_(m,n)(epsilon).

Substituting (6) gives EXACTLY

    mu(q) a_r^AA=|A_U(m)A_U(n)|.                              (8)

All unit/ray phases are accounted for by the displayed theta(epsilon); it may be nontrivial. In particular

    E_(selected,h=1)^AA
      =D^(-1) sum_q Z_(1,q) sum_(active orientations)
                                      |A_U(m)A_U(n)| >=0.    (9)

This is the exact joint h,q,K realization of the parent's selected-row/coprime-pair count. No hidden ray exclusion occurs: the first-five unit ideals are allowed, one literal unit class is explicitly allowed, and v is arbitrary rather than squarefree. Arbitrary overlaps are removed only by the original mask1_((v,hq)=1). Averaging the six units before selecting epsilon would be a DIFFERENT row weight. Pair-column conductor q has norm~D^2 at h=1, while the primitive character of each selected row has fixed S conductor; these are distinct conductors.

It now follows that the proposed orientation-VARIANCE replacement

    |c_hq sum B_V A^AA|
       <= ||a^AA||_2 [sum_r|Gamma_r^F-mean(Gamma^F)|^2]^(1/2)

is false whenever Z_(1,q)>0 and at least one interior active A–A orientation has NONZERO coefficient: its right side is zero and (8) gives a positive left side. A nonempty index set containing only zero-profile coefficients would not suffice. The exact orientation mean cannot be deleted as a principal residue; these selected rows have nonprincipal primitive character. This does not refute the desired fixed-W target or any properly proved signed estimate. It refutes this specific mean-centering shortcut on actual permitted data.

The full h=1 contribution over OTHER row classes may be negative and cancel (9). Positivity of the selected h=1 block does not lower-bound the full h=1 sum. Full A–A energy is a positive row sum, so it can be lower-bounded by a selected-row energy once its diagonal and other gcd contributions are included. The parent's separate coprime-triple argument is responsible for any c D X asymptotic lower bound from (9); that count is not proved here. With H=X^6 this is D H^(1/6), not D^(7/6) at H=D^(3/4).

## 4. Fresh exact control, not a repeated old audit

The new deterministic check uses D4000,U63 and five explicitly specified good split primes of norms7,13,79,67,97. There are exactly four orientations of their product with both column norms in[4000,8000]: the ordered pairs6097/7663 and7189/6499. Each r_U is2 and A_U is−1 on the three-prime columns and+1 on the two-prime columns. Their epsilon phases are not all equal. The common values (6) make mu(q)a^AA=1 at every orientation; omitting theta(epsilon) gives an incorrect signed coefficient sum−1 instead of4.

Four complete good primary ideals of norms13,13,19,19 form V with10<=Nv<=20. One13-prime collides with q; exactly three survive, for every orientation. Direct raw symbols at the four nonprincipal rows epsilon beta_v^6 agree with (7) and give selected h=1 contribution12/4000=3/1000. The orientation variance is zero. Finite phase-group evaluation checks (3) and (4) with k5,J4: lambda4/243 and leakage squared956/59049. The complete residue group is NOT enumerated, no B tail is estimated, and no old991 Gauss or learned216/200 trajectory is rerun.

This finite control verifies signs, masks and normalization only. The unchanged infinite analytic obligations are the actual signed estimate on the A6=1 mixed/pure witness sectors, common FIXED-profile uniformity, short/principal target assembly, determinant/zero-location comparison, full analytic/category formalization and GRH. No new Lean/compiler, package, GPU, authentication, publication, production or queue action accompanies this attempt.
