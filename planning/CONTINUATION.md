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
