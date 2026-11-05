# Moving common profiles and coherent orientation means

5 November 2026. This is an original-family scope result, not a new signed upper bound or a fixed-profile counterexample. The canonical derivations are `papers/profile-uniformity-{core,details}.tex`; the independent mathematical design review is `planning/signed-profile-20261105/review-design/REVIEW-v1.md`.

For principal nu=1, fixed S containing the primes above2,3, and U²=D, the actual high-window coefficient A_U(m)=mu(m)(r_U(m)−1) is odd/nonzero. The multiset of prime-ideal norms of an ideal-squarefree m depends only on Nm, including repeated split-prime divisor norms and inert prime ideals of rational-square norm. Therefore A_U(m) is norm-radial without replacing any original column weight.

The literal unit epsilon=1+omega has raw symbol eta(m)=epsilon^((Nm−1)/6), also norm-radial. Its exact primitive conductor is(2)²(1+2omega)³, norm432. Nontrivial powers have norms432,27,16,27,432; all remain nonprincipal. The squared cubic phase is the inverse of omega^((Nm−1)/3). Explicit local witnesses and norm congruences prove exactness; this is prose mathematics, not Lean verification.

At every strict interior norm node choose W_D(N/D)=sign(A_U(N))*conjugate(eta(N)). Disjoint C-infinity bumps of radius1/(4D) give ONE common complex smooth profile, supported strictly inside(1,2), supnorm1, with k-th derivatives O_k(D^k). It varies with D and is independent of the row. Endpoints are zero. On every actual row u=epsilon*beta_v^6, v an arbitrary good ideal, the primitive row character remains eta but the original collision mask still deletes every column sharing a prime with v. Thus P_u=0 and

    E_u = D^(-1/2) sum_(m sf,good,D<Nm<2D,(m,v)=1) |A_U(m)|.

A new application of elementary ideal counting gives a positive density of pairwise-coprime triples(m,n,v), with m,n ideal-squarefree in the D-annulus and arbitrary good Nv<=X. The density constant is kappa³ C_S, kappa=pi/(3sqrt3),

    C_S=product_(p in S)(1−1/Np)^3
        *product_(p notin S)(1−5/Np²+6/Np³−2/Np⁴)>0.

The proof uses finite local inclusion-exclusion and a uniform tail for the five failures p²|m,p²|n,p|(m,n),p|(m,v),p|(n,v). It needs no prime-number theorem, GRH, or finite numerical extrapolation. The geometric valuation series for v is essential; v is not squarefree.

Consequently the full original E energy is at least(c_S+o(1))D H^(1/6) for H=D^theta,0<theta<1. This already comes from a single literal-unit class of nonprincipal sixth-power rows. Its selected h=1 A−A contribution is positive, but the h=1 contribution over OTHER rows need not be. The full lower bound uses positivity of the outer sum of squared row values. Row conductor432 and pair-column conductor q=mn~D² are distinct.

This shows necessity of the D H^(1/6) term in the supnorm/varying-profile envelope for theta<2/3. At theta=3/4 its exponent9/8 is BELOW the accepted upper exponent7/6; there is no new upper saving or proof of7/6 sharpness. A hypothetical bound uniform through M_k(W)^alpha H(HD)^epsilon for every positive epsilon would need k*alpha>=1−5theta/6, hence3/8 at theta3/4. For one fixed epsilon the additional(1+theta)epsilon term must be retained. Fixed-W bounds, bounded-seminorm classes, nonnegative-real-profile restrictions and existing M4(W)^2 dependencies are not refuted.

## A failed shortcut and the surviving exact statement

The bounded attempt to estimate the new A6=1 upper-envelope witnesses through orientation projection did not produce a saving. With n=phi(q), c=Q² xi_q(−alpha)tau(xi_q)/ell⁶ and Gamma_r=c sum B conjugate(theta_r), exact projection has counting norm squared (|c|² n)^(-1) sum|Gamma_r|². Projected Cauchy is exactly the original ||a||2||Gamma||2. No group-size gain follows from rank alone.

On the coherent subset C where each local cubic character is one, the compression is3^(-omega(q))*11*, with eigenvalue lambda=|J|/3^omega(q) and leakage squared lambda(1−lambda). Thus coherent restriction and orientation projection do not commute. The exact note and fresh controls are `planning/signed-profile-20261105/joint-attempt/JOINT_PROJECTION_AND_PROFILE-v2.md` and `outputs/checks/2026-11-05-signed-profile/joint-attempt/projection-profile-v1.json`.

A variance-only replacement is false on actual permitted weights. Set the first five row factors to one and keep arbitrary v in the sixth factor. Then Gamma_r=Z_(h,q), the number of v coprime to hq, for every orientation. In A−A, retaining the literal epsilon phase gives mu(q)a_r=|A_U(m)A_U(n)|. A positive nonzero orientation mean survives on nonprincipal rows and cannot be deleted as a principal residue.

The new exact D4000/U63 fixture uses q-prime norms7,13,79,67,97 and four complete active orientations:6097/7663,7189/6499 and reversals. Four v with norms13,13,19,19 leave Z=3. Orientation variance is zero and the actual selected h1 moment is3/1000. Omitting the literal unit phase incorrectly gives−3/4000. Coherent fraction4/243 and leakage956/59049 are exact finite phase-space quantities, not estimates for the infinite dual tail.

## Reproducibility and remaining task

The separate exact implementation is `examples/profile_uniformity/`. Its immutable v2 run at `outputs/experiments/2026-11-05-profile-uniformity-v2/` covers D256,1024,4096,16384,65536,262144, all complete norm groups and all40 arbitrary ideal rows through norm64. Nineteen rows are good-S at X64. Capacity-matched X=floor(floor(D^(3/4))^(1/6)) is only2..4 here and honestly contains only the good-S unit; fixed-X64 is a separate range. The three norm49 ideals have different split-prime masks. No seed, randomness, model training, quantum execution or new dependency is involved.

Run manifest SHA256:a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460. Source-freeze SHA256:eeb405583fbd9256a1a8a54ffa4a56b79ad4e3e70b3ff1abd0f9c83cf5001f54. Preserve the failed v1 manifest attempt and every prior output. The compact web inspector is a hash-bound projection of these exact files; it performs no browser training. Finite ratios do not prove the density theorem.

The genuine arithmetic task remains a bound on actual joint signed h,q,K weights BEFORE per-conductor absolute Cauchy, with fixed common profiles, coherent means and all union/common-prime/ray/squarefree/capacity/conductor restrictions. The A6=1 mixed and pure upper-envelope neighborhoods remain open. This new obstruction concerns a different A6-varying family and does not settle those sectors. Short/principal target assembly, independent positive determinant/zero-location comparisons and separate Dirichlet/Hecke/Dedekind/elliptic/Artin obligations remain open. Actual analytic/category Lean awaits the separately requested pinned Linux compiler approval. No new Lean declaration, positive determinant, zero location or GRH proof is claimed.
