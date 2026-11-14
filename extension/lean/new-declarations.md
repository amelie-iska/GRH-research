# New declaration-to-manuscript map

This map covers exactly **33 added declarations**. Current source SHA-256
hashes, actual printed theorem types and axiom dependencies are in
[`final-verification/verification.json`](final-verification/verification.json)
and its two named module logs. The corresponding machine-readable map is
[`new-declarations.json`](new-declarations.json). A component mapping does not
assert that every prose statement in the target environment is formalized.

## ReductionContracts — 16 declarations

Source: `ReductionContracts.lean`. Namespace prefix `ReductionContracts.` is
omitted below. Actual types: `final-verification/ReductionContracts.log`.

| Declaration | Manuscript anchor | Precisely checked component |
|---|---|---|
| `factorization_iff_fiber_constant` | `thm:reduction-fiber-factorization` | Exact set-theoretic equivalence for a surjective observation map |
| `reduced_output_unique` | `thm:reduction-fiber-factorization` | Uniqueness on the surjective observed state space |
| `discrete_closure_iff` | `thm:reduction-fiber-factorization` | Specialization to a discrete state update |
| `mismatched_fiber_excludes_closure` | `thm:reduction-fiber-factorization` | Two indistinguishable inputs with different outputs exclude every deterministic closure |
| `discrete_trajectory_preserved` | `prop:reduction-trajectory` | Exact intertwining at every natural-number step |
| `fiber_error_lower_bound` | `prop:reduction-error-diameter` | Triangle-inequality error lower bound in a seminormed additive group |
| `fiber_diameter_le_twice_error` | `prop:reduction-error-diameter` | Uniform epsilon error implies at most twice-epsilon pair separation |
| `signedPartner_constant_coefficient` | `prop:reduction-signed-order` | Constant coefficient of the explicit rational polynomial |
| `signedPartner_linear_coefficient` | `prop:reduction-signed-order` | Linear coefficient of the explicit rational polynomial |
| `signedPartner_ne_zero` | `prop:reduction-signed-order` | The second summand is nonzero |
| `signedPartner_order` | `prop:reduction-signed-order` | The second summand has order one |
| `signed_cancellation_identity` | `prop:reduction-signed-order` | The sum is exactly the prescribed higher monomial |
| `signed_cancellation_sum_ne_zero` | `prop:reduction-signed-order` | The residual polynomial is nonzero |
| `signed_cancellation_order` | `prop:reduction-signed-order` | Its order is the arbitrary integer k+2 |
| `signed_cancellation_strict` | `prop:reduction-signed-order` | The residual order strictly exceeds the minimum summand order |
| `no_universal_minimum_rule` | `prop:reduction-signed-order` | There is no universal exact minimum rule for signed polynomial addition |

The proofs do not establish continuous-time existence, differentiability of
arbitrary observation maps, a kinetic limit, a small-divisor estimate, or
the stability of an external Navier–Stokes solution. The signed example concerns
actual rational polynomials; no generic theorem about every tropicalization or
every valuation ring is inferred from it.

## TransportContracts — 17 declarations

Source: `TransportContracts.lean`. Namespace prefix `TransportContracts.` is
omitted below. Actual types: `final-verification/TransportContracts.log`.

| Declaration | Manuscript anchor | Precisely checked component |
|---|---|---|
| `suffix_transport_telescope` | `thm:typed-transport-telescope` | Arbitrary finite path with all arrows acting on the same module |
| `closed_path_residual` | `thm:typed-transport-telescope` | Closed-path endpoint residual |
| `flat_closed_path_zero` | `thm:typed-transport-telescope` | Identity holonomy makes the closed residual zero |
| `two_arrow_transport` | `thm:typed-transport-telescope` | Two-arrow noncommutative telescope |
| `fixed_vector_closed_path_zero` | `thm:typed-transport-telescope` | Fixing the initial vector suffices without full flatness |
| `scalar_counterexample_flat` | `prop:transport-prefix-counterexample` | The counterexample has identity holonomy |
| `scalar_prefix_counterexample` | `prop:transport-prefix-counterexample` | The incorrect prefix sum is exactly 3/2 |
| `scalar_suffix_correction` | `prop:transport-prefix-counterexample` | Correct suffix transport gives zero for the same data |
| `positive_damping_bound_not_contracting` | `prop:transport-damping-obstruction` | The displayed upper bound is at least one for L≥1 and eta≥0 |
| `expanding_scalar_damping` | `prop:transport-damping-obstruction` | The scalar multiplier is greater than one for positive damping |
| `trace_preserving_composite_nonzero` | `prop:transport-trace-zero-obstruction` | Two real linear trace-preserving maps cannot have zero composite if a trace-one vector exists |
| `nonnormal_shear_square_zero` | `prop:nonnormal-jvp` | The explicit real matrix `[[0,M],[0,0]]` squares to zero |
| `nonnormal_shear_unit_image` | `prop:nonnormal-jvp` | Its image on the explicit Euclidean unit vector `(0,1)` is `(M,0)` |
| `nonnormal_shear_gain_squared` | `prop:nonnormal-jvp` | Exact coordinate squared norm of that image is `M²` |
| `nonnormal_shear_strict_gain` | `prop:nonnormal-jvp` | This one-step squared gain exceeds one when `M>1` |
| `nonnormal_shear_second_jvp_zero` | `prop:nonnormal-jvp` | A second Jacobian-vector product is zero on every input |
| `nonnormal_shear_not_normal` | `prop:nonnormal-jvp` | For `M≠0`, the matrix does not commute with its transpose |

The varying-fiber telescope in prose and its rectangular-matrix regression are
stronger in typing scope than the one-module Lean specialization. The damping
proofs certify scalar inequalities, not a complete normed-space fixed-point
theorem. The trace obstruction needs no positivity hypothesis, so it applies
to suitable channel representations; complete positivity, trace-norm
contractivity and the operational instrument construction remain separate
written arguments. No analytic continuation or arithmetic conclusion follows
from these finite identities alone.

The final six statements establish an explicit counterexample to interpreting
plain Jacobian power iteration as a general singular-value upper certificate.
They formalize finite real matrix identities and squared Euclidean gain only;
they do not prove spectral-radius characterizations, convergence of `J*J`
iteration, floating-point error bounds, or a certified operator-norm algorithm.
