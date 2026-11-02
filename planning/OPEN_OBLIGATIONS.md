# Remaining mathematical obligations

No complete GRH proof has been established. A proof must discharge these, not assume them.

| ID | Obligation | Acceptance evidence | Status |
|---|---|---|---|
| O1 | Specify arithmetic Hilbert space and operator independently of unknown zeros | Complete domain, measure, action, closure, adjoint and convergence definitions | Open |
| O2 | Recover full completed L-function from that operator | Exact determinant/trace identity with conductor, gamma, ramified factors and multiplicities | Open; proposed source identity refuted |
| O3 | Preserve O2 under a self-adjoint realization | Explicit intertwining/determinant identity, not arbitrary Hermitian extraction | Open; unrestricted preservation refuted |
| O4 | Prove locally uniform convergence on a domain with overlap | Uniform trace-norm or normal-family estimates, all constants quantified | Open for spectral operators; partial-sum arithmetic approximants now have explicit compact-uniform convergence |
| O5 | Apply closure with nonzero holomorphic target | Rouché/Hurwitz argument after O1–O4 | Proved conditionally in prose |
| O6 | Extend from primitive Dirichlet to finite-order Hecke | Field/infinity type/conductor-specific construction and estimates | Open |
| O7 | Extend to general Artin with correct analytic scope | Holomorphy or meromorphic/pole analysis, valid induction and no hidden automorphy assumptions | Open |
| O8 | Formalize the actual proof | Pinned mathlib build, kernel-checked analytic definitions and complete dependency/axiom report | Open; finite obstructions and local analytic convergence lemmas checked |

A sequence of upper bounds β_n→1/2 on zero real parts could provide another route, but a fixed7/8 or11/12 region cannot. No mechanism producing such a sequence with valid constants has been established here. Numerical zeros up to a finite height cannot replace any of the universal obligations.

## Continuation findings

- Simply improving compact bounds on the existing finite Euler-product family cannot work: it is zero-free on Re>0 and cannot approximate a target zero locally uniformly. This proposed repair is rejected, not just unfinished.
- Nonprincipal Dirichlet partial sums and pole-subtracted zeta sums give convergent arithmetic approximants on Re>0, independently of unknown zeros. They do not have a proved critical-line zero divisor or self-adjoint realization.
- The separate mathlib layer now proves finite complex Euler-factor nonvanishing and a genuine boundary-uniform-limit nonvanishing theorem with explicit local assumptions. Root isolation and the entire GRH closure remain prose/unresolved as documented.
- The exponent report identifies a missing short-row mean square and explicitly conditional parameter extension; neither has been established as a new unconditional zero-free theorem.

- Holomorphic pointwise-Hermitian matrix rigidity is now kernel-checked. A nonconstant complex-holomorphic transfer cannot become a complex-holomorphic Hermitian family by ordinary pointwise extraction. A fixed H_N independent of spectral s remains permitted. Hermitian dilation loses phases/spectral imaginary parameter for the prime diagonal; real-axis Hermitian pencils require a separate zero-location theorem.

- A positive generalized-pencil criterion is now proved and formalized: fixed Hermitian A and positive-definite B yield only real z-zeros, hence centered s-zeros on the critical line. This supplies a valid sufficient mechanism for O3 but does not discharge the arithmetic construction/matching in O1–O2. A strict-imaginary-form nonvanishing criterion and an exact indefinite off-line witness are also checked. Next test a specified arithmetic candidate for a positive metric or the necessary Herglotz logarithmic-derivative sign, with normalization fixed independently of unknown zeros.
