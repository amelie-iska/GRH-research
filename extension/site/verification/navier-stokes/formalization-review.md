# Formalization review: finite fluid, reduction, and order interfaces

## Result and scope

`extension/lean/FluidInterfaces.lean` adds **34 named declarations**, all freshly
checked with Lean **4.24.0** and mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The check exited successfully with
zero warnings. Every theorem has both its full type and its foundational axiom
dependencies printed in the authentic log. The dependencies are confined to
`propext`, `Classical.choice`, and `Quot.sound`; there is no `sorryAx`, new
project axiom, or unproved placeholder.

The source SHA-256 is
`9ac752e3450fd07f9fb23cb4d0283ecee1b70d7a3188ece1cdcff5d8b66934b2`.
The verification log SHA-256 is
`8ebef3ba31ea4979aa3cc37ec26749dfe4a94c13468fb7f21f1faad978e34f77`.
The extracted, unmodified axiom-report lines have SHA-256
`9f63084dbdaff023a9d8cfb545bf46b759a92f156bc046228cfd13bd3dd0c7a5`.

These are selected interfaces for the new chapters. They neither import nor
recheck the released continuum Navier–Stokes formalization. Their purpose is to
make the project's finite geometric, reduction, and arithmetic connections
precise without claiming that those connections establish continuum regularity
or reproduce the complete singularity construction.

## 1. Finite fluid energy: eleven declarations

For an arbitrary finite real vector `u`, the energy is exactly

\[
E(u)=\tfrac12 u^{\mathsf T}u.
\]

The declarations `dot_self_nonneg` and `kineticEnergy_nonneg` establish
nonnegativity by summing squares. `transpose_work` proves

\[
u^{\mathsf T}L^{\mathsf T}v=(Lu)^{\mathsf T}v
\]

for every rectangular real matrix `L`. This identity is then used to derive,
rather than assume, the cancellation and dissipation laws:

\[
J^{\mathsf T}=-J\Longrightarrow u^{\mathsf T}Ju=0,
\qquad
u^{\mathsf T}L^{\mathsf T}Lu=\|Lu\|_2^2\geq0.
\]

These are `skew_transport_work`, `factorized_viscosity_work`, and
`factorized_viscosity_nonneg`. The pressure theorem `pressure_work_zero`
likewise derives `uᵀBᵀp = 0` from the actual matrix constraint `Bu = 0`.

The work identity is

\[
u^{\mathsf T}\bigl(Ju-\nu D^{\mathsf T}Du-L^{\mathsf T}Lu+f\bigr)
=u^{\mathsf T}f-\nu\|Du\|_2^2-\|Lu\|_2^2.
\]

`finite_fluid_work_identity` allows any real viscosity in the equality;
`unforced_work_nonpositive` explicitly assumes `ν ≥ 0` for the sign conclusion.
This distinction prevents a positive-dissipation conclusion from silently
covering a negative viscosity.

The last two declarations are actual calculus results. If each coordinate
`u_i(t)` has derivative `v_i` at a time `t`, `kinetic_energy_derivative` proves

\[
\frac{d}{dt}E(u(t))=u(t)^{\mathsf T}v.
\]

It uses the product rule, division by two, and the derivative of a finite sum.
`finite_fluid_energy_derivative` substitutes the displayed semidiscrete vector
field into these coordinate derivatives. The ODE is a genuine premise about
the trajectory; the energy balance is the proved consequence. The theorem
does not assume the desired energy balance as an axiom or hypothesis.

The matrices can be evaluated at the current state. Thus a learned nonlinear
closure `Lθ(u)` still dissipates energy pointwise when it enters as
`−Lθ(u)ᵀLθ(u)u`; differentiating `Lθ` is not required to evaluate `dE/dt`.
This observation does not prove well-posedness of that nonlinear ODE.

**Important integration boundaries.** The metric in this file is the
Euclidean metric. A positive mass matrix requires a justified coordinate
transformation or a corresponding weighted version. Arbitrary `J`, `D`, and
`L` do not automatically preserve `Bu = 0`. One must separately construct a
constraint-preserving vector field or apply a justified pressure projection.
A dissipation inequality on each fixed mesh does not give a uniform derivative
bound, consistency, compactness, convergence, or a continuum singularity test.

## 2. Orthogonal reduction: five declarations

For a finite real matrix `P`, the assumptions are stated as actual identities
`Pᵀ = P` and `P² = P`. They imply

\[
P(u-Pu)=0,\qquad (u-Pu)^{\mathsf T}Pv=0,
\]

and the exact decomposition

\[
E(u)=E(Pu)+E(u-Pu).
\]

The corresponding names are `projection_residual_kernel`,
`projection_residual_orthogonal`, and `projection_energy_split`.
`projection_energy_nonincrease` proves that retained energy cannot increase.
`projection_best_approximation` proves

\[
Pv=v\Longrightarrow E(u-Pu)\leq E(u-v).
\]

This supplies a precise finite meaning of information discarded by an
orthogonal reduction. It is not a quantum channel theorem, an entropy
inequality, or a proof that POD modes approximate nonlinear trajectories.
In particular, small discarded energy alone does not bound a derivative or
the error of a nonlinear reduced dynamics. The theorem assumes exact matrix
identities, so a floating-point implementation requires a separate residual
and rounding-error audit.

## 3. Chain-complex continuity: two declarations

For composable boundary matrices `B` and `C`, the assumption `BC = 0` implies

\[
B(Cq)=0,\qquad B(u+Cq)=Bu.
\]

`boundary_flux_divergence_zero` and
`boundary_flux_update_preserves_divergence` derive these identities from
matrix associativity. They hold for every flux `q`, so `q` may be the output
of a classical or quantum learned function. The algebraic constraint is then
independent of training success.

This statement does not infer exactness from the complex condition. It
does not assert that every divergence-free velocity lies in `im C`; on a
positive-genus surface there can be harmonic/cohomological modes. Nor does
it identify a gentle-quiver algebra with a de Rham complex without an
explicit construction.

## 4. Exact linear elimination and memory: four declarations

For a block system

\[
Ax+By=f,\qquad Cx+Dy=g,
\]

`schur_elimination_iff` proves the equivalence

\[
\begin{cases}
(A-BD^{-1}C)x=f-BD^{-1}g,\\
y=D^{-1}(g-Cx).
\end{cases}
\]

`D` is an actual linear equivalence in the theorem's type. No inverse is
invented for a singular operator, and no conditioning estimate follows from
the existence of this algebraic inverse.

For the exact discrete recurrence

\[
p_{n+1}=Ap_n+Bq_n,\qquad q_{n+1}=Dq_n+Cp_n,
\]

`hidden_recurrence_expansion` proves by induction that

\[
q_n=D^nq_0+\sum_{k=0}^{n-1}D^{n-1-k}Cp_k.
\]

`resolved_memory_identity` then proves

\[
p_{n+1}=Ap_n+BD^nq_0+
\sum_{k=0}^{n-1}BD^{n-1-k}Cp_k.
\]

The sum is finite and the statement is exact over arbitrary vector spaces
over a field. No continuous-time semigroup, unbounded generator, integral,
or interchange of limits is being smuggled into this result. It is the
finite algebraic analogue that motivates a separate Mori–Zwanzig discussion.

`hidden_state_prevents_autonomous_closure` gives a useful obstruction:
if some `y` has `By ≠ 0`, there is no function `F(x)` that equals `Ax+Bz`
for **all** retained states `x` and hidden states `z`. The proof compares
the hidden states zero and `y` at retained state zero. Exact autonomous
closure can still hold on a specified invariant manifold, a restricted
state family, or after including additional state variables; this theorem
does not rule those out.

## 5. The nilpotent block mechanism: one declaration

Define `N_L(x,y)=(0,Lx)` and a block-diagonal map
`D₀(x,y)=(D_Xx,D_Yy)`. Then

\[
N_LD_0N_M=0
\]

for arbitrary `L` and `M`. `lower_diagonal_lower_zero` proves this as an
identity of actual linear maps. It specializes to the four-plus-two block
decomposition described in the released proof's Volterra stage. Allowing
`L` and `M` to differ is essential for the variant involving a parameter
derivative of one lower block.

The formal statement does not verify the source paper's identification of
its operators with these blocks, bounds on the remaining Volterra words,
convergence of the series, or its differentiability estimates. Those need
the separate source-level analysis.

## 6. Quadratic order and toral renormalization: eleven declarations

The file constructs the exact integer matrices

\[
A=\begin{pmatrix}-1&1\\1&1\end{pmatrix},\qquad
J=\begin{pmatrix}3&1\\1&5\end{pmatrix},\qquad
M(a,b)=\begin{pmatrix}a-b&b\\b&a+b\end{pmatrix}.
\]

The verified identities include

\[
A^2=2I,\quad J=M(4,1),\quad J^2-8J+14I=0,\quad
\det J=14,\quad\det J^k=14^k,
\]

as well as

\[
\begin{aligned}
M(1,0)&=I,\\
M(a,b)+M(c,d)&=M(a+c,b+d),\\
M(a,b)M(c,d)&=M(ac+2bd,ad+bc),\\
\det M(a,b)&=a^2-2b^2.
\end{aligned}
\]

`quadratic_order_representation_injective` proves that the pair `(a,b)` can
be recovered uniquely from its matrix. Together these identities give the
coordinate realization of the quadratic order `Z[√2]`; the file does not
create a separate Lean `RingHom` from an algebraic-number-field object.

`no_commuting_complex_structure` is a useful obstruction to an incorrect
geometric interpretation. If a real `2×2` matrix `I` commutes with `J`, it
cannot satisfy `I²=−1`. The proof extracts the diagonal commutation equation,
obtains `I₀₁=I₁₀`, and observes that the first diagonal entry of `I²` is
`I₀₀²+I₀₁²`, which cannot be `−1`. Thus the real toral map in this stage
cannot simply be declared a complex-linear endomorphism of an elliptic
curve by choosing a different linear complex structure.

The determinant-of-powers theorem alone is not a formal proof of the
topological degree of a toral covering, nor does it prove the source
paper's Fourier/small-divisor estimates. These connections require the
stated geometric and analytic arguments in the chapter.

## Reproducibility and integration

Run, from the repository root:

```sh
python extension/review/navier-stokes/formalization-verify.py
```

The script verifies the exact Lean/mathlib pins before checking the source,
rejects proof placeholders and unexpected axiom dependencies, records all
theorem types, checks that the source did not change during compilation,
and writes the three evidence files under `extension/lean/`. Optional
`--toolchain` and `--mathlib` arguments select another installation of the
same versions. It performs no network downloads or remote actions.

The old three theorem modules and their verification records were not
modified by this subtask. Register `FluidInterfaces` as an additional
`lean_lib` and default target when integrating the complete release. The
34 new declarations and the earlier 48 selected declarations total 82;
this arithmetic is not a claim that the entire monograph has been
formalized or that the previous 48 were freshly checked in this subtask.

The primary implementation dependency is the pinned
[mathlib source tree](https://github.com/leanprover-community/mathlib4/tree/f897ebcf72cd16f89ab4577d0c826cd14afaafc7).
All claims of new kernel verification are supported by the actual local
source, full types, and authentic logs rather than by literature citations.
