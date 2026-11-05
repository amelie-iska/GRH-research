# Independent adversarial review: genuine double Perron

5 November 2026. Remote Linux only. **ACCEPTED under the stated finite-order, fixed-nu/S hypotheses.** Reviewed derivation SHA256: `e8549e3c576defc7a96b703240a9e51ad9daf6cc1e3ce8077ec37effbbce4e97`. No load-bearing gap or required correction was found. This acceptance covers the exact Euler factorization, the sufficient correction domain and its uniform upper bounds, sharp finite-cutoff Perron inversion, and the diagnosis that the available absolute contour bounds reproduce the older cutoff loss. It does not establish an improved energy estimate, BT_sigma, reciprocal-L estimates, zero-freeness, a lower bound for the actual arithmetic energy, new Lean statements or GRH.

Read-only context included the repository README, current continuation/implementation-loop instructions, accepted centering/signed-target note and its clarification acceptance, masked-moment core/details, weighted-cutoff core/details, research/weighted-cutoff-moment.md, arithmetic-cutoff README, and the author checker/report/manifest. No repository AGENTS.md or relevant Python lockfile was found. Existing unrelated changes were preserved. The assigned new review planning/check directories are the only write targets.

## 1. Local algebra and full original mask

For each surviving prime, the four placements (absent, in c, in a, in b) give E=1+q-q alpha-q beta. Pairwise coprimality excludes the a=b placement. Multiplication by (1-q) gives exactly
(1-q alpha)(1-q beta)-q^2(1-alpha)(1-beta).
Thus the displayed L(s)/[L(s+z)L(s+w)] times R is correct initially in the absolute domain. The omitted-R factorization and the unconstrained mollifier square are both false in explicit exact controls.

The independently primitive psi_2 is needed in F0=L^T0(s,psi)/L^T0(2s,psi_2). At each prime outside T0 the primitive phases agree by psi_2(p)=psi(p)^2, giving local F0 factor 1+q. At a deleted prime both incomplete Euler factors are 1, regardless of either primitive conductor. Cubic and sixth-power drops therefore cannot restore original raw zeros. The independent controls explicitly check primitive local ratios 48/49 and 8/7 at norm 7, with full-mask corrections 49/48 and 7/8, and raw zeros on those rows.

Consequently J_U=F0 B_U follows first in Re s>1 and continues by the finite B_U sum. Its local denominators 1+q are nonzero for Re s>0. On Re s>1/2 the 2s denominator has an absolutely convergent nonzero Euler product. Nonprincipal J_U is holomorphic there; principal J_U is meromorphic with its only possible pole at s=1. The note does not silently apply a holomorphic principal-row assertion through that pole.

## 2. Correction convergence and uniformity

The bounds |1-alpha|<=2(Np)^(-min(x,0)) and |1-q alpha|>=1-2^(-eta) prove the displayed |R_p-1| majorant. The condition kappa>1 implies sigma>1/2. On compact subsets of Omega, positive eta and epsilon margins exist, so the prime-ideal majorant is summable. Normal convergence gives a holomorphic product and its uniform upper bound. This uses only absolute Euler convergence; it requires no zero-free statement for L in the critical strip.

The bound is independent of all three imaginary variables, surviving unitary phases, and deleted set, since that set only removes terms from the majorant. No uniformity in varying nu, S or a vanishing positive margin is inferred. Nonvanishing of R is unnecessary and was not assumed. An independent finite local test even has R_p=0 inside Omega: Np=7, sigma=2, q=1/49, alpha=48, beta=2. The positive local-denominator conditions follow from 48,2<49, and kappa>1 from 96<7^3.

The expression in (F) is a meromorphic continuation on Omega, not a proof that reciprocal L factors are bounded there. The finite deleted factors 1-psi(p)(Np)^(-v) have no zeros for Re v>0; surviving primitive L zero divisors are not removed by a conductor-drop convention.

## 3. The second series and exact Perron

For fixed sigma>1/2, |t_p|<=(Np)^(-sigma)/(1-(Np)^(-sigma)). Hence the coprime a,b coefficient series has absolute local majorant
1+|t_p|(Np)^(-x)+|t_p|(Np)^(-y),
which is summable when sigma+x>1 and sigma+y>1. This proves G there with uniformity in all vertical variables on fixed margins. F=F0 G in this region follows by local algebra/continuation, without evaluating the original infinite c sum in a region where it is not absolutely convergent.

In the inversion theorem the explicitly fixed range 1/2<sigma<1 makes c,d>1-sigma positive. For V=floor(U)+1/2 all integer ideal norms obey Na<=U iff Na<V, including integer equality endpoints. This also covers distinct coprime ideals with equal norms in both variables. Direct use of U in the kernel instead gives the half weight in each coordinate and a quarter weight at a double endpoint; both corrections are needed.

For lambda=log(v) nonzero, integration by parts bounds each omitted oscillatory half-tail by
[1/sqrt(c^2+T^2)+integral_T^infinity dt/(c^2+t^2)]/|lambda|
<=2/(T|lambda|).
After both 1/(2pi) normalizations this gives exactly the kernel error 2v^c/(pi T|lambda|). The kernel identity is a symmetric oscillatory limit; no absolute infinite-height integral is asserted.

On finite rectangles, the absolutely convergent G series permits termwise integration. Expanding the two kernel errors and using h(v)<=v^c yields ERR with the stated sum A and constants. The closest integer logarithmic distance is at least 1/(2V+1); the claimed explicit bound is valid. Thus ERR tends to zero for independently diverging heights. No zero-free assumption or unproved interchange of an infinite c sum is hidden here. The excluded original principal pole is correctly explicit.

## 4. Available contour estimate and height weights

On the positive lines, both reciprocal factors are bounded by absolute Euler products, and R has the vertical-uniform bound above. The two kernel absolute integrals are O(log(2+T_i)). Also A is uniformly bounded on fixed margins and
|F0(s)| <= C_(sigma,eta,nu,S) (Nu)^eta |L(s,psi)|
by the absolute 2s denominator and the finite numerator-deletion product. Taking T_i=V^2 in ERR costs no additional positive power of V: Delta_V^(-1)=O(V). These facts establish (B).

Letting c,d approach 1-sigma with fixed positive margins, and absorbing logarithms in an arbitrarily small U exponent, gives amplitude U^(2-2sigma+epsilon). At sigma=1/2+delta its square is U^(2-4delta+epsilon), exactly the previous AFM cutoff loss.

More explicitly, insertion into the existing common-W Mellin remainder and Minkowski gives the previously scoped bound
||E||_2^2 << C M_4(W)^2 D^(2delta) H^(1+epsilon) U^(2-4delta+epsilon),
with small row losses absorbed in the usual (HD)^epsilon when U^2<=D. The inherited numerator moment supplies height (1+|t|)^(1+epsilon) after squaring; its square root times the M_4(W)(1+|t|)^(-4) Mellin decay is integrable. This statement uses the common smooth W and its Mellin/derivative seminorm. It does not replace that seminorm by the infinity norm used in the separate direct-sieve envelope. Constants are for fixed delta in (0,1/2), fixed positive auxiliary margins, nu and S. In particular the inherited principal-row Poisson constant is not uniform as delta approaches 1/2. No additional height or principal-pole uniformity is being granted.

Accordingly the “no improvement by the available safe absolute contours” conclusion is justified. It is a limitation of this specific upper-bound method, not an impossibility theorem for averaging or a lower bound for the actual signed energy.

## 5. Reciprocal divisors and contour residues

At w=0, R=1 and F(s,z,0)=1/L^T0(s+z,psi) as a meromorphic slice; similarly at z=0. For fixed s away from its L zero/pole, any zero rho with Re rho>sigma lies at z=rho-s inside the relevant part of Omega, and the w=0 slice precludes a globally presumed R cancellation. The note properly treats possible singularities as auxiliary-variable divisors. They are not singularities of the finite J_U as a function of s.

The simple-zero residue coefficient follows from differentiating L^T0(s+z) and multiplying the remaining w integrand. Higher multiplicities require the higher residues stated in the note. A principal pole of L at 1 produces a reciprocal zero, not a reciprocal pole. Sequential shifting also leaves the single-kernel-residue boundary integrals and any zero residues. The double origin value 1/L^T0(s,psi), away from its zero/pole, is not the whole answer. No missing cancellation or reciprocal bound is supplied by the numerator moment. The note rejects precisely that unsupported contour step.

## 6. Independent finite evidence and disposition

The independent checker imports neither author nor project code. It implements Fraction arithmetic in Q(omega), ideal divisibility and sextic residue evaluation directly. Its actual distinct split/inert prime ideals have norms 7,7,13,13,25. There is no random seed or nonstdlib dependency.

The run passed 960 local factorizations, 192 finite G/triple-series identities, 800 asymmetric sharp-cutoff tests, 25,600 half-integer endpoint comparisons, 384 raw-mask terms and 96 coordinate slices. It also checked 33 sixth-power unit-phase and 33 cubic-phase-order cases. Negative witnesses: 96 omitted-R cases, 128 forbidden-overlap cases and 756 uncorrected-halfweight cases, together with the explicit independent conductor-drop and equal-norm controls. These are finite diagnostics, not proofs of normal convergence, Hecke continuation, reciprocal bounds or zero location. Those analytic steps were audited above from the stated inherited classical input.

Command:
```sh
PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/signed-bilinear-20261105/review-perron/check_independent_perron.py --output outputs/checks/2026-11-05-signed-bilinear/review-perron/independent-exact-controls-v1.json
```

The author suite was read and its source/report hash bindings were checked; it was not rerun as if it were independent evidence. No new Lean or production build was relevant to this planning-only proof audit. No installation, MCP, credential/auth, queue, production, GPU or publication action was performed.

**Disposition:** accepted for integration at the exact reviewed hash, with no required fixes. Preserve the author evidence and cite this source-bound acceptance. BT_sigma, a new analytic saving, reciprocal/residue control and GRH remain open.
