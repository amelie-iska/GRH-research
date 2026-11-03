# Independent review: Euler correction and angular factor

2026-11-02. Read-only adversarial mathematical and implementation review by the project_review agent. No reviewer edits.

The reviewer checked the inherited local scalar formulas against the source and independently derived the residual identity and every valuation exponent. It confirmed constants656<1024 for good primes and24<32 for primes dividing the row, the explicit open neighborhood, divisor-product bound, principal specialization and fixed-half-plane cutoff dependence. It also checked the selected G_p denominators and the finite compensated tuple formula against source8686–8712. These checks do not independently verify the source's earlier Gauss/reciprocity proof or its main mean-square theorem.

The A-factorization, local convex nonvanishing and normal convergence on Re>1/2 are sound. The reviewer confirmed theta=alpha^(-6)eta^6 is an infinite-order angular Hecke character; no conjugation or norm-shift defect occurs. Under the explicitly listed classical completion/order-one/functional-equation/conjugation inputs, Hadamard growth supplies a zero with Re>=1/2, and the shifted correction has a zero with Re>=7/12. Finite prime deletion cannot cancel it. This is a limitation of the unchanged correction, not GRH or all replacement constructions. White's Theorem2 covers pure angular characters and does not by itself certify finite-conductor twists or order one; this qualification is retained.

Independent compilation of the literal latest EulerCorrection.lean passed all8declarations with warnings as errors and only propext, Classical.choice and Quot.sound. The explicit complex infinite-product hypotheses and zero-transport inputs are accurately documented. The reviewer executed the actual Python arithmetic in memory before report construction: all assertions and24exact Q(sqrt(-3)) local samples passed. This is not verification of Hecke zero existence or analytic contour estimates.

A precision correction was requested and applied: the sharp149/100and7/10defect exponents are explicitly restricted to the displayed closed region; the larger open neighborhood uses137/100and68/100. Its divisor-product estimate now uses68/100. The O_epsilon(q_u^epsilon) conclusion holds in both.

No substantive mathematical or implementation defect remained. Source worktrees were clean. This is internal independent review, not external peer review or a complete proof audit of the classical inputs.
