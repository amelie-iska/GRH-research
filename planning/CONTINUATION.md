# Continuation: arithmetic approximation and the spectral bridge

Authorized by the user's instruction to continue necessary/helpful improvements. Sources stay immutable; private milestone pushes continue. No promise or assumption of a GRH proof.

1. Prove a precise no-go theorem for zero-free finite Euler products and reciprocal products near a target zero. Make its boundary-error lower bound explicit.
2. Construct valid compact-uniform arithmetic approximants using bounded character sums and pole-subtracted zeta sums. Quantify the error and all domains. This supplies convergence for a different class, not a self-adjoint model.
3. Formalize the general integer trace equation in standalone Lean. Add a separate, pinned mathlib4.24 analytic layer for actual complex Euler weights and a reciprocal maximum-modulus estimate. Do not change the supplied math/lean environment or its4.34.1pin.
4. Extract the exact exponent constraints in the7/8and11/12papers and determine whether their printed estimates can be iterated to1/2. Record the missing inequality rather than merely suggesting stronger estimates.
5. Independently review additions, compile both editions, inspect changed layout, run focused Lean/integrity checks, push substantive findings.

Unresolved target: prove that arithmetic approximants can be made self-adjoint with the correct zero divisor, or prove an equivalent positivity property without assuming GRH. The existing zero-free truncations are structurally unsuitable near zeros.

## Current frontier after the finite arithmetic test

The latest completed attempt is research/arithmetic-zero-certificate.md. The primitive modulo3 character's fifth partial sum has one certified simple zero in the disk centered at0.337261+11.027504i with radius1e−4, lying strictly left of the critical line. This excludes its exact local representation as a nowhere-zero holomorphic factor times the determinant of a fixed positive Hermitian pencil. It does not exclude convergence of the partial sums, later truncations/subsequences, or modified approximants, and says nothing adverse about zeros of the full L-function.

Resume by specifying a different arithmetic approximation class and testing an actual positive-metric certificate, or by proving a particular short-row mean-square estimate identified in research/exponent-frontier.md. A symmetry-preserving polynomial construction is a possible experiment, not an established positive family. Do not rerun the completed S5 certificate as new research or assume functional-equation symmetry forces real zeros. The arithmetic spectral bridge, full analytic formalization and intended GRH scopes remain open.

Evidence: exact-rational certificate and all18 analytic Lean declarations pass; the new Lean statements cover disk location and rational margin only. Both paper editions contain the argument. Run-specific logs are preserved under outputs/checks/2026-11-02-arithmetic-zero/.

## Current frontier after the Jensen-metric attempt

Read research/jensen-metric.md next. We constructed a precise symmetry-preserving zeta approximation family, its explicit compact error and a coefficient-defined metric. The self-adjoint block determinant is conditional on strict metric positivity. The attempted generic proof from positive Fourier moments fails, even for strictly positive smooth Gaussian-mixture densities. The exact -7/1200 Turan gap is independent of smoothing variance. Universal arithmetic Newton-Hermite PSD remains an RH-equivalent condition; no unconditional positivity was obtained. Seven additional Lean components pass, bringing the analytic layer to25; their exact scope is in lean-analytic/README.md.

Rotate to a genuinely arithmetic input. One finite next target is the local correction-product extension in research/exponent-frontier.md section3e: extract the exact good/ramified prime factors of sept's H_eta, prove all defect estimates and uniform nonvanishing at sigma_t=349999/400000, and record which contour/high-identity hypotheses remain. This would address one explicitly missing perturbation interface; it would not by itself certify the source7/8 theorem or prove GRH. Alternatively derive an arithmetic all-degree principal-minor/Schur-complement inequality for the specified Jensen metrics; do not infer it from ordinary kernel moments, assume leading minors alone certify PSD, or repeat low-degree model checks as new arithmetic progress.

## Current frontier after the Euler-correction extension

The concrete local task suggested above is completed for the displayed scalar factors; read research/euler-correction.md. All valuation cases give an extension to Re x>=3/4, including normal convergence and holomorphy of the selected finite tuple formula. At the principal point H_eta=A L^S(6s-3,alpha^(-6)eta^6), with A holomorphic and nonzero on Re>1/2. Classical Hecke completion inputs imply zeros of the unchanged correction at real part at least7/12, blocking indefinite extension of its nonvanishing premise toward1/2. The scalar arithmetic identification and classical analytic inputs are explicit inherited/external dependencies; no7/8 theorem or GRH proof was certified. The analytic Lean suite now has33 checked declarations, with exact scope in its README.

Next concrete claim: verify the quantitative compensated principal-residue approximation on sigma_t=349999/400000 from the September source6173–6306and9050–9100, including slot-scale losses, relative error, derivative/height uniformity and the principal correction's exact normalization. The larger Euler region supplies holomorphy but not these bounds. If that interface closes, return to the frozen-capacity row count/general energy assumptions of exponent-frontier.md; do not declare the tiny numerical refinement proved before every interface is checked. Any later plan to cross7/12 with the same common-signal criterion must change or account for the shifted angular factor. Preserve every source and existing experiment.
