# Bounded independent review: all-component exact BV--Mellin extension

Governing final note: planning/intermediate-kernel-20261106/lane-b/ALL_COMPONENT_EXACT_PREFIX-v3.md, SHA256 b978ac2f1cc3969d004c98afb94ad224dabef91eb1d4e9cda3c7fcd66829a07e. Verdict: PASS, now including the new Section7 ALL-COMPONENT BV--Mellin band and prefix results. This supplements, without replacing, the independent v1 all-j review/receipt dd0154f0314a166fd0e1e5f2004d1fcf6f3c5d0a85bf5fe5975c830fc56d3efd. The preserved v1 had no BV extension, and its receipt correctly said so. Its mathematical all-j body remains unchanged in final v3; the new proof is a separate addition.

A's same-class BV theorem985295dd and C's independent acceptanceca55abb4 are now explicit accepted inputs. Those establish the actual profile's uniform BV/Gamma integral and the small-positive-contour machinery. They do NOT by themselves establish different-class transport. The latter is checked directly here, using the exact general root, primitive S scalar and row-phase formulas from Sections2--4 and the two independently gated global root law25ad1b4a. There is no appeal to the companion same-class all-j proposal as an unproved theorem.

## 1. Actual full-class Mellin factor

Primitive eta has conductor f_S*m*n, where sigma=prim(rho psi_A bar psi_B) is FIXED for A,B,rho. Good conductor factors m,n are disjoint from S and from each other on the original support, so no variable S conductor is hidden. Eta's total angular and radial infinity types are zero. Its SAME field transform has argument L_e Ny/(F_S NmNn) and prefactor L_e/sqrt(F_S NmNn). Their exact Mellin product is

 F_S^(s-1/2)L_e^(1-s)(Ny)^(-s)(NmNn)^(s-1/2).

This independently verifies the sign of the exponent F_S^(s-1/2) in(7.1). On lambda=Re(s)<1/2 it has modulus F_S^(lambda-1/2)<=1, since F_S>=1. The factor is retained exactly before this upper bound, not set to1 or inverted.

The root factor is kappa*u_m*bar v_n with u_m=beta_m xi_m(f_S)rho(m) and v_n=beta_n xi_n(f_S)bar rho(n). Thus left and right vectors in Section7 are correctly DIFFERENT. The paired right vector is b(conjugate(s)) before conjugation, giving two factors Nm^(s-1/2), Nn^(s-1/2), not a spurious positive norm square. All fixed unitary angular/radial phases remain in these columns; none is discarded because it is not finite order.

## 2. Primitive S zeros and the actual good-dual row phase

The scalar is exactly sigma(k^2 ell e)*bar sigma(h). At good k,ell it is a unit phase; at S-supported e/h it can be ZERO. Those primitive zeros, including conductor-drop cases, remain. Xi_m(e/h) is instead a legitimate primitive good-conductor column value; it is not an original S-forbidden raw symbol. No division by sigma(e/h), rho(e/h) substitution, or zero restoration occurs.

Using the proved good-argument equality sigma(z)=rho(z)psi_A(z)bar psi_B(z) and source reciprocity tilde_chi_m(z)=gamma_A(z)R_m(z), the exact dual transport is

 bar sigma(z)bar xi_m(z)xi_n(z)
    =bar rho(z)bar gamma_A(z)gamma_B(z)bar R_m(z)R_n(z).

This is the displayed Omega(z), unit-modulus for good z, including a globally defined source phase when a column collision makes both sides zero. Neither equality of A,B nor class-constant rho is required. The correction is retained in the exact bilinear row form. Only in Cauchy is its modulus used. All k/ell collisions stay in the primitive column values and all original v2 collisions in R_m(v2^2), with the original finite pre-S K_ell and capacity b(v2) unchanged.

## 3. Distinct residual classes and the legal positive comparison

Exact ideal Mobius inversion is applied to the ORIGINAL coprime support. The off-coprime individual-column product is auxiliary and is never called its actual primitive eta/root. Full divisors cancel all overlaps and self-pairs. After m=da,n=db the coefficient supports have distinct classes A[d]^(-1),B[d]^(-1). Raw multiplicativity contributes only the exact shared (d,z) zero mask; AU(da), beta_da, primitive S values and the common W remain inside their own column vector.

For the band Y<NhNz<=2Y, the complex row weight Omega(z)(NhNz)^(-i tau) has modulus1, and its positive magnitude is <=Y^(-lambda). Bilinear row Cauchy is therefore valid for the two DIFFERENT coefficient vectors. Only inside the two positive squared norms are the row window and shared mask enlarged, with the legal prefix Z_h=2Y/Nh>=1. There is no PSD order claim on the coprime matrix and no arbitrary weighted-row large-sieve theorem.

On the ORIGINAL annulus the two vector squared norms are each O(B_W^2 D^(2lambda+epsilon)/Nd), uniformly in tau. The accepted raw arbitrary-column-coefficient Phi comparison applies separately to their class-supported subsequences; after transport the row family is finite-order R, not primitive xi. Any class-common xi/psi row phase may equivalently be cancelled separately within its own positive norm. No equality of the two residual classes is needed. At residual length[1/2,1) use the direct unit-column bound, not a subunit sieve.

The same four d sums at exponents1,2,4/3,11/6 then give D^(2lambda)Y^(-lambda)Phi(2Y/Nh,D). The UNIQUE S-supported h sum has strictly positive exponents1,1/6,5/6,1/3 and a fixed geometric constant; the scalar sigma(h) only suppresses terms. No flat log(Y) S-volume factor arises.

## 4. Remaining factors and the all-component band

The complex finite k weight (Nk)^(-2+2s) in the exact formula has ABSOLUTE value (Nk)^(-2+2lambda). Thus its finite positive majorant is zeta_K^S(2-2lambda), finite for fixed0<lambda<1/2. The wording 'norm weight' in Section7 denotes this complex Mellin weight followed by its stated absolute majorant; no identity with a completed Euler factor is used. The original signed cutoff and all raw zero masks remain in the exact expression.

Finite ell/e weights have magnitude (Nell Ne)^(lambda-1); ell is bounded by tau(v2) only after its actual restriction, e is a fixed finite S sum, and actual v2 counting costs A2 with its stated divisor loss. The scalar h_ABrho is used ONCE and is bounded by fixed finite Fourier data. The factor A1^(1-lambda) and original normalization ONCE1/D give exactly(7.3), with the accepted BV/Gamma integral and no growing derivative cost in the implicit constant.

Summing the FINITELY MANY original A,B,rho with their actual coefficients reconstructs the full original two-pivot representation band for fixed u0. The number of components and fixed conductor/class data affect constants, not a norm power. Rho need not factor sourceGamma, and no unproved H_ROOT remains after the independently gated normalization theorem. The proof is thus an explicit all-component derivation, not a same-class assertion by analogy.

## 5. Finite prefixes, unit mode and the final epsilon

For fixed0<lambda<1/6, each Phi exponent minuslambda is positive. Finite dyadic summation (with the last partial interval) produces(7.4). The dual UNIT is kept separately: h=z=O, the same primitive scalar zeros remain, and the positive row prefix is exactly1. Every class pair is still treated bilinearly, so no positivity or equal-class requirement appears in this unit bound. This is not deletion or centering of an arithmetic mean.

For requested final eta0>0, the explicit fixed choice lambda=min(1/12,eta0/4)>0 and input epsilon=eta0/2 yields

 D^(2lambda)(A1X)^(-lambda)<=D^(eta0/2),
 (DXA2)^(eta0/2)D^(eta0/2)<=(DXA2)^eta0.

The contour is never lambda=0, and it is not fitted as a D-dependent parameter. The constants may depend on eta0. Therefore the stated FINAL all-component bound(7.5) is valid for every FINITE X>=1, with no Taylor-I condition and no X<=sqrt(H) approximation hypothesis. Actual G, finite K and sharp capacity remain exact.

The same four sufficient target inequalities follow from (A1A2/D)Phi(X,D)<=H. Removing the earlier all-j Taylor condition is valid for this BV theorem. The full mixed prefix X~D has target power3/4, while the full pure prefix there has upper power11/12; at X=D^(3/8) the powers13/16 and31/48 are unchanged. These are representation-prefix upper bounds, not physical energy measurements, lower bounds or complete signed-slice exponents.

## 6. Remaining scope and protection

The Ny>X complement remains in the full exact identity. The Phi majorant grows with X, so finite-prefix bounds do not produce a whole infinite-dual target. Unit/S-supported/sixth-power modes remain in their actual places. This acceptance covers the original fixed u0/ray two-pivot family; it does not sum all u0 blocks or supply principal/residue/short assembly. Whole signed13/12, global9/8, determinant/GRH/Lean status remain unchanged.

V1 and its independent all-j acceptance remain historical; the source-freeze v1->v2->v3 chain and all exact input hashes were checked without rerunning any controls. No scientific table, phase fixture, build, browser, source/public/index mutation or dependency/auth operation was executed. All twelve protected HEAD/index states still match.
