# Background research and scope

Primary sources consulted on 2026-11-02:

- Clay Mathematics Institute, [Millennium Problems](https://www.claymath.org/millennium-problems/): current problem-status page, inspected; RH remains listed as unsolved. This does not by itself adjudicate a supplied proof.
- Jeffrey C. Lagarias, [Li coefficients for automorphic L-functions, v4](https://arxiv.org/abs/math/0404394v4), Annales Institut Fourier57(2007),1689–1740: bibliographic record/abstract inspected, not a full-paper review. Use for a precise family-dependent positivity criterion; positivity remains an obligation.
- Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function](https://arxiv.org/abs/math/9811068), Selecta Math.5(1999),29–106: record/abstract inspected, not a full-paper review. Its trace-formula reduction is a research interface, not a proved GRH theorem.
- [mathlib RiemannZeta documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html): definitions and functional-equation API inspected. `RiemannHypothesis` is a definition, not a proof. Pin a compatible mathlib revision before future analytic formalization.
- [Official Lean4.24.0 release](https://github.com/leanprover/lean4/releases/tag/v4.24.0): local standalone verification toolchain; release digest checked.

Supplied papers are tracked separately in SOURCES.json and reviews/. Classical Rouché, Montel, identity, and Hadamard factorization theorems are used explicitly in prose and are not claimed as new results or as formally verified by the small standalone Lean module.

Next primary-source work: inspect actual theorem statements for Selberg trace formula, Eichler–Shimura, Artin/Brauer induction, and Li/Weil test spaces. The exact counterexamples in the audit already disprove the specific overstatements without requiring a literature consensus argument.

Continuation references checked: [DLMF5.2](https://dlmf.nist.gov/5.2) for gamma's nonvanishing and poles, and [DLMF25.15](https://dlmf.nist.gov/25.15) for Dirichlet analytic continuation, Euler product scope, parity and functional equation. The new partial-sum error formulas are derived explicitly in the papers, not inferred from a finite numerical test.

Positive-pencil verification uses the pinned primary mathlib source [Matrix.PosDef](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/LinearAlgebra/Matrix/PosDef.lean), [Matrix.Hermitian](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/LinearAlgebra/Matrix/Hermitian.lean), and [kernel/determinant equivalence](https://github.com/leanprover-community/mathlib4/blob/f897ebcf72cd16f89ab4577d0c826cd14afaafc7/Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean), inspected locally. The real generalized spectrum and inverse estimate are classical deductions explicitly derived in the papers; no novel theorem or external GRH claim is attributed to this source.
