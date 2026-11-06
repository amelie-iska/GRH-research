# Independent review of exact cusp states, actual finite family and all-k/all-d transfer

6 November2026. Reviewer lane-c. These are independent reviews of lane-A geometry/family and lane-B coefficient/assembly; lane-C's OWN angular Mellin theorem requires the separate A/B/root gates and is not self-accepted here. All scientific work SSH-Linux/owned paths; no old scientific control or canonical/index/publication action rerun.

## A. Exact rational geometry and actual finite family — PASS

Read EXACT_RATIONAL_CUSP_STATE_AND_MULTIPLIER-v1 (006c4dc7),
ACTUAL_FINITE_RESIDUE_FAMILY-v1 (c70805fa), and REQUIRED
RHO_SCOPE_PRECISION-v1 (1b154731). The rho companion is part of this acceptance.

Independently checked: for primitive A,C with AD-BC=1,
 U(A/C)W_r=gamma U(-D/C)A_(r/C).
When C=c0*r and D=b*r+9*c0*d, the ordered output is exactly
 [F_j U(-b/c0)A_(1/c0)] U(-9*c0^2*d/r).
The moving translation acquires c0^2 after commuting the diagonal; it cannot be kept unchanged. The primitive-lambda specialization has b=h^-1*r^-2 modulolambda^(B0+4), and its gamma mod3 is independent of the moving Fourier variable. Low-conductor/nonunit cases use the general reduced-fraction identity, not an inverse at a nonunit.

The exact phase algorithm is legitimate: the source has Gamma2=SL2(Z)Gamma1(3), Gamma1(3) the principal kernel. For gamma and chosen integral left representative gamma_j, g=gamma gamma_j^-1 lies inGamma2. Choose sigma inSL2(Z) with same mod3 reduction, then delta=sigma^-1*g is inGamma1(3). The source weight-zero Kubota phase is EXACT chi(delta), (c/a)_3 for c!=0 and1 for c=0; it is a genuine known modulus-one character value, not an omitted primitive S root. Changes from a BFS basis to published representatives carry their actual fixed unit multipliers. No new cusp coefficient bound follows merely from27 labels.

The source R_c is verified in the pinned deFaveri primary Section2.3.2: H_c is the fixed ray group and R_c=H_c tensorZ/6, so source characters have a real fixed ray-modulus realization. The original nu is fixed FINITE ORDER (physical-sieve-core), so typezero. Gamma modulo4 and local source/primitive-S tests are finite functions; the latter must first be expanded on the FULL product finite group, retaining coefficient mass and forbidden primitive e/w zeros in the full sum. General fixed Kummer numerator symbols give finite-order Hecke characters with fixed conductor/raw support; no moving k/opposite column is put into that modulus. The suggested Hensel safe exponents exceed2*v_p(6), and the sextic polynomial discriminant6^6*zeta^5 is a valid safe fixed ramification bound. No general Artin holomorphy is used.

IMPORTANT rho is NOT finite: Jacobi rho=mu*vartheta is infinite order. The complete accepted TypeI list77660bde has exactly ONE own vartheta after the arithmetic mu has been incorporated into mu*A/HB. Thus own angular order is+1 or-1; there is no additional unrecorded rho(v). Common rho(d)^2, prefix and opposite-column phases remain outer at fixed variables, with their actual unit values, not1. The rho companion makes this scope precise.

The fixed residue functions after angular extraction therefore match the new general finite-character/source theorem, with raw modulus zeros and possibly imprimitive/overlapping support. Their constants may depend on the original FIXED conductors/source data. Arithmetic mu, HB coefficients, nonperiodic density g, growing Q or sharp norm masks are not made periodic. There is NO densityg in the governing DIRECT model.

The new root geometry receipt6338ee1f/producer41405478 was read, not rerun:648 mod3 matrices,24 integer subgroup elements,27 left cosets,4680 rational cases,4329 fixed-affine cases and3942 wrong-diagonal negative controls. Its v1 serialization-only failure remains preserved. These controls do not evaluate Kubota symbols or prove a theta FE; the source automorphy proof above is separate.

## B. Explicit known-cusp norm, actual match and all-k/all-d transfer — PASS

Read CUSP_COEFFICIENT_NORM_AND_ACTUAL_MATCH-v1 (8231e155) TOGETHER WITH REQUIRED ACTUAL_CUSP_COEFFICIENT_CONVENTION-v1 (3da658fd) and receipt19bbb38b. The required convention binds governing lane-Cv2 (605478df) and its notation addendumb601afb6. Exact transported coefficients use a_j(mu), the ACTUAL Fourier coefficient of the chosen theta-cusp function, not an unqualified table d_j(mu).

Checked the primary AppendixA table: each known coefficient family is one tau/tau1/tau2 value at a rotated/signed index times unit/additive phases. Their exact magnitudes are as claimed. Theta support is SF c times arbitrary cube d^3 (c,d can overlap). The two tau lambda branches give the author's geometric bracket, and tau1/tau2 have3 fixedlambda^-4 branches. For1<sigma<13/12, replacing z by1/9 gives firstbracket at most3^8/2 and all three families at most
 3^8*zeta_K^lambda(sigma)*zeta_K^lambda(3sigma-1/2).
This is a proved absolute norm of KNOWN coefficient formulas, not an unknown cusp bound or a crude N(mu)^(1/6) shortcut.

For a fixed affine state(z,v)->(A*z+B,|A|v), index nu=A*mu has exact coefficient |A|a_j(mu)e(Tr(muB)); its absolute norm scales by |A|^(1-2sigma). The primitive-lambda state has scaling3^(B0(2sigma-1)) and the moving phase retainslambda^(4+2B0) after the diagonal; this agrees with A's state identity. Actual angular/translate/Kubota factors are retained before taking absolute values.

The general finite projector uses x=lambda^3*mu, notlambda^4. It selects the plus primary lowestvaluation branch and gives the GENERALIZED cube L(kappa^3 Theta3ell,3s-1/2) with all rawlambda/F/t primes deleted. Full Fourier Parseval for literal periodF*t, including overlap/imprimitive cases, gives masssqrt(NF*Nt); denominatorNC<=fixedNt. Together with the separately accepted lane-C Mellin factor(NC)^(1-2s), this yields the conservative left costR^(3/2+Oeta), not a refinedsqrtR claim. Pole absence comes from pureangular/radial constant calculation, not noncubic character terminology. The actual finite-family match in A and the rho precision apply. Conjugating the WHOLE theorem covers barG and both actual angular signs.

For ALL original finiteK and ALL common-long divisors, the exact support still has d<=2D and physical t=p*d*k squarefree on nonzero branches. Freeze opposite r,b first. Keep cross(p,b) in its actual coefficient; do NOT put b in Q after the long-long mask was opened. Q=rad_good(p*r*d*k*s*w) and surviving h is coprime t. Exact deletion changes scale T/h and levelh*t with productD*Nk and literal h^-1/2. The coarseH(3/4,3/8) yields h^-3/8; no hypothetical uniform deletion theorem is inserted. Unit/subunit[1/2,1) cases are bounded literally; smaller lengths empty.

The author's p sum gives
 Cleft << V1(W)D^(1/4)d^(1/8)k^(3/8)Z^(5/8)
with allocated subpowers. Right elementary column count is
 B sqrt(D/d) times a harmonic prefix sum. The ORIGINAL once-only normalizationA1/(D*d) therefore gives d^-11/8,k^-13/8; both ideal majorants converge after an explicit small epsilon allocation. NQ<=C*D*Z^2*V*Nk controls all divisor costs; no polynomial-K assumption or new cutoffs are needed. Exact original finite sums, common rho/Gamma/general finite-S means, capacity and raw overlaps remain until the stated triangles. No mu cancellation or positive energy claim is used.

At Z=D^(1/8), the small-prefix leading component has normalized power41/64. Optional unequal-norm subtraction is the SAME auxiliary piece and costs B^2*A1V/D up to subpowers. Distinct conjugate ideals remain distinct. Combining this with the NEW required whole-prefix tail, inherited exact DIRECT AU-to-AY/Bessel reduction and balanced HB input gives the stated scoped finite primitive-dual P_X target at X=D^(3/8), NOT the entire infinite dual kernel or original full h1 signed form. Fixed W dependence includes B,M(W),V1(W) and inherited explicit seminorms. No varying-profile supnorm claim is made.

This gate accepts the exact coefficient/assembly theorem subject to the separately reviewed new C-interface, already independently accepted by A (99b4cc05) and B's own C review. It does not claim a self-verifying administrative theorem checker. Root may assemble the final scientific milestone only after all independent source/interface gates are bound.

Whole signed13/12/global unsigned9/8, other dual complements/mixed-neighbor blocks/short-principal assemblies, independent positive determinant/zero-location, separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes and actual analytic/categoryLean/GRH remain OPEN. No original data, source body cache, environment, protected state, index, canonical book/UI/PDF or release changes occurred.
