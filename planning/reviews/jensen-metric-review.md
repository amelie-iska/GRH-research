# Independent review: Jensen approximants and positive-metric attempt

2026-11-02. Read-only adversarial review by the project_review agent. No reviewer edits.

The reviewer checked the universal coefficient-defect bound, including j>d, and the entire-function errors R²F''(R)/(2d) and T^4F''(T²)/(2d). It confirmed the multiplication-by-x companion orientation, Newton-sum indexing, HC=C^T H, and exact block-determinant factor (-1)^d gamma(d)/d^d with sqrt(dS). The GORZ normalization differs by8; the documents state this. Strict metric positivity is kept separate from PSD, and the inverse square root is never used under a merely semidefinite hypothesis. Repeated roots and the insufficiency of leading-minor-only PSD tests are documented.

The reviewer confirmed the negative atomic witness, Gaussian-smoothed moment formulas and variance-independent Turan gap-7/1200. The distinction between ordinary kernel moment Hankel forms and Newton-sum Hermite matrices is substantive and correctly stated. The Jensen criterion is labeled RH-equivalent, not a proof, and the construction's scope is zeta only.

Independent compilation of the literal JensenMetric.lean passed all7declarations with warnings as errors. Only propext, Classical.choice and Quot.sound occur in their axiom reports. The reviewer executed the literal check_jensen_metric.py arithmetic in memory, stopping before report creation; all Newton, symmetrization, LDL, counterexample, singular-case and finite coefficient-bound assertions passed. These are model checks, not xi coefficient enclosures. No substantive mathematical or implementation defect was found. The requested README count/scope update to25was applied.

This is an internal independent check, not external peer review of RH or of the cited deep asymptotic theorems.

A final separate check confirmed Romik1902.06330v3 equations1.8–1.11 match the explicit full-line Fourier kernel. Differentiating yields Xi^(2j)(0)=(-1)^j integral_R u^(2j)Phi(u)du=(-1)^j xi^(2j)(1/2), confirming the sign, factorial and absence of an additional factor2. Positivity on the half-line, evenness extension and differentiation using double-exponential decay are valid. The representation remains an external classical dependency.
