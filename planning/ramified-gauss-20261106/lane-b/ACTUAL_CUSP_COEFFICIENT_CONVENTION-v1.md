# Required exact chosen-cusp coefficient convention

6 November2026. REQUIRED bounded companion to lane-B
CUSP_COEFFICIENT_NORM_AND_ACTUAL_MATCH-v1.md SHA256
8231e155708cc0a49b5571dd612f47356f9082f16bd853fbb850e9eca1ce6411.
It also updates the exact-source convention in the lane-B independent
C-interface review without altering any estimate or scientific check.

For the EXACT chosen theta-cusp function F_j=theta(gamma_j*w), define
 a_j(mu) by its ACTUAL nonconstant Fourier expansion
 F_j^*(z,v)=sum_(mu!=0) a_j(mu) v K_(1/3)(4pi|mu|v)e(Tr(mu z)).

Use THIS a_j(mu) everywhere an exact coefficient is transported.
In particular lane-B Eq(4) is read EXACTLY as
  a_(j,A,B)(nu)=|A| a_j(mu)e(Tr(mu B)), nu=A*mu.
The ramified fixed-state formula is
  a_(j,b,B0)(lambda^-2B0*mu)
       =3^-B0 a_j(mu)e(-Tr(mu*b/lambda^B0)).
The exact dual translate series is
  sum_mu a_j(mu)e(Tr(-mu D/C))
          (mu/|mu|)^(-ell)/(Nmu)^(1-s).
No unqualified d_j(mu) or d_j(-mu) is substituted into these exact formulas
without first identifying the source's chosen sign/conjugation convention.

The governing full Mellin source is NOW lane-C
RATIONAL_CUSP_CONSTANTS_AND_MELLIN-v2.md SHA256
605478dfe81524f50e4cc53274812cc6739d38115476c9553142e1a7489e5f77,
TOGETHER WITH its coefficient-convention-addendum-v1.json. Historical
C-v1 remains preserved and is not the standalone governing convention.

The AppendixA table, its sign-index counterpart and complex conjugates
all have the SAME absolute bounds: rotations/reflections preserve Nmu,
and conjugation/additive phases preserve magnitudes. Consequently every
absolute Dirichlet norm in lane-B(1)--(3),(5),(11) is unchanged, with a_j
in place of the historical table-placeholder d_j. No estimate, moving
power, angular constant/pole identity or actual-family matching changes.
The literal lambda^(4+2B0) moving translation after a diagonal is unchanged.

This is an exact-notation precision after independent review, not a
scientific reexecution. No completed controls were rerun or relabelled.
The scoped pure finite DIRECT prefix, all raw primitive/unit/source/
rho/Gamma phases and all-k/all-d assembly retain their stated scope.
Whole signed13/12/global unsigned9/8 and GRH remain unchanged.
