# Independent analytic review of the actual critical-line dyadic bound

Governing root note: planning/intermediate-kernel-20261106/root/CRITICAL_MELLIN_DYADIC-v1.md, SHA256 62937830ef87cd1f802a0d29cd7961fbec0240eb503912d3759f5afc488d51cb. Verdict: PASS for exactly the same-source-class, rho=1, unweighted original two-pivot scope stated there. This is an independent written derivation, not a call to the author's controls. No old or new numerical experiment, phase table, build or browser was run. General-component H_ROOT work is separate and is not needed in this theorem.

The domain is D>1, A1,A2>=1 and Y>=1, with the original AU, fixed nu/S, full original ideal annulus, literal/ray/capacity constraints, squarefree/coprime filters, one common complex W, and B_W=||W||infinity. Empty sharp v1 blocks are zero. The fixed finite row-ray coefficient remains outside once, and is bounded only by the existing fixed-ray constant in the error estimate. Nothing assumes arbitrary weighted large-sieve rows.

## 1. Exact logarithmic vertical cost

For H(v)=e^(v/2)G(e^v) and y=e^v I obtain

 H'=e^(v/2)(G/2+yG'),
 H''=e^(v/2)(G/4+2yG'+y^2 G'').

In the dv=dy/y integral, the three second-derivative terms are bounded respectively by (1/4)||H||1, 2sqrt(5/2)TV(G), and (5/2)^(3/2)||G''||1. Using support[1/2,5/2], 0<=G<=1, TV<=2, ||G''||1<=832A1 gives exactly the root h0,h1,h2 estimates. The first two h2 terms are absorbed into h2*A1 only because A1>=1. No derivative of the original complex W is invoked: G is the actual auxiliary capacity interpolant.

Integration by parts has no boundary terms because the stated sigmoid is smooth and compactly supported. The three Fourier bounds h0, h1/|t| and h2*A1/t^2 are valid separately. Splitting the even integral at 1 and A1 gives precisely

 (2pi)^(-1) integral |Ghat(1/2-it)|dt
     <=(h0+h1 log A1+h2)/pi.

For A1=1 the middle interval is empty. This is a logarithmic derivative cost, not a claim of a uniformly fixed G as A1 varies. On s=1/2+it, Gamma(1-s)=bar Gamma(s), neither Gamma value has a zero or pole, and C0^(s-1/2) is a unit phase for positive C0=3/(4pi^2). Thus the field gamma factor has exact modulus one, with no missing C0 amplitude on this line.

## 2. Actual finite kernel and the two coefficient vectors

The accepted primitive identity has prefactor L_e/sqrt(F), F=NmNn, and transform argument L_e Ny/F. Mellin inversion therefore produces

 L_e^(1-s)(Ny)^(-s)(NmNn)^(s-1/2).

The last factor is exactly b_m(s) conjugate(b_n(conjugate(s))), with b as in the root note and in accepted v8 (5.2b). Replacing conjugate(s) by s would instead introduce opposite norm phases and a false PSD norm square. On the critical line both of the CORRECT vectors have the same pointwise absolute values, at most those of c_m. Fixed e/h primitive S phases are legitimate values at their actual good conductors, while the original k/ell/v2 collision factors remain literal zeros. The outer mu(k)mu(ell)mu(e)h_0 eta_C appears once, not in both coefficient vectors.

Only a finite ideal band and finite k,ell,e,v2 sums are interchanged with the vertical integral. The matrix has finitely many original columns and the above Mellin L1 cost is finite. This justifies that interchange directly; no infinite k-Euler/whole-dual interchange or contour shift is used. Coprime original columns are nonunit and give a nonprincipal primitive eta in this same-class component, so no omitted principal Poisson residue is being concealed.

## 3. The arbitrary-coefficient positive comparison and exact divisor budget

The all-good physical-row comparison Phi(Z,L) used here is a genuine arbitrary-coefficient norm bound, not a weighted assertion inferred from positivity. One can derive it directly from the accepted sixth-power-free input: write each good physical row uniquely as z=r6^6*zflat, with zflat sixth-power-free, and freeze r6. Its overlap with a column is a ZERO coefficient mask. Apply the accepted arbitrary-coefficient input to zflat up to Z/(Nr6)^6 and column norm up to 2L. Summing r6 costs convergent exponents 6,5,2 in the Z, Z^(5/6)L^(1/3), Z^(1/3)L^(5/6) terms; the L term costs the actual count O(Z^(1/6)). Hence, for Z,L>=1, the squared norm is bounded by

 (ZL)^epsilon [Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6)]

on any zero-extended coefficient subsequence. These are UNWEIGHTED row norms. For 1/2<=L<1, only the unit residual column can occur and its direct norm is O(Z), which the same displayed polynomial dominates up to an absolute constant. No row sieve below norm length 1 is required.

After exact gcd-Mobius inversion, write m=da. The arbitrary coefficients b_da are left intact, including AU(da), beta_da, original class/ray and collision restrictions. Their squared norm is O_epsilon(B_W^2 D^epsilon D/Nd), independently of t, since |AU(m)|<=3^omega(m) and the residual count is O(D/Nd) for D/Nd>=1/2. No multiplicativity of AU or beta is needed.

The raw (d,z) mask remains before bilinear row Cauchy. The weight (NhNz)^(-it) has modulus one, and on the actual band its magnitude part is at most Y^(-1/2). The lower band and mask may be removed only in each resulting positive squared norm. For fixed S-supported h use the UPPER prefix Z_h=2Y/Nh, with Nh<=2Y; thus Z_h>=1 even when the lower parameter Y/Nh is subunit.

The exact d comparison has four sums

 Z_h D sum_d(Nd)^(-1),
 Z_h^(1/6)D^2 sum_d(Nd)^(-2),
 Z_h^(5/6)D^(4/3) sum_d(Nd)^(-4/3),
 Z_h^(1/3)D^(11/6) sum_d(Nd)^(-11/6).

The first is logarithmic and the other three converge. Absorbing only the D logarithm into the arbitrarily small epsilon yields exactly

 O_epsilon(B_W^2 D^(1+epsilon)Y^(-1/2)Phi(2Y/Nh,D)).

The off-coprime entries used for this finite inversion are algebraic extensions of the separated expression; they are not assertions about actual primitive conductor/root values when m,n share primes. Their Möbius sum reconstructs the original coprime support exactly, including cancellation of self-pairs. Ideal divisors, not rational-norm squarefreeness, govern the identity.

Finally y=h*z is UNIQUE with h S-supported and z good. Each Phi term has positive power alpha in Z, namely 1,1/6,5/6,1/3. Therefore

 sum_{h S-supported} (Nh)^(-alpha)
     =product_{p in S}(1-(Np)^(-alpha))^(-1)<infinity.

This proves the claimed fixed-S Phi(Y,D) comparison, with no extra log(Y) count and no restoration of forbidden original S values. The fixed-S constants need not be uniform over varying S.

## 4. Finite k, remaining outer sums, normalization

For active ell, K_ell=sqrt(b/Nell)>=1 and K_ell<=sqrt(2A1). Partial summation of the accepted A_K(x)<=2x ideal count gives

 sum_{Nk<=K_ell}1/Nk <=2+2log K_ell <=2+log(2A1).

This is a FINITE harmonic sum. It is not zeta_K(1), and its logarithm cannot be replaced by an infinite absolute Euler product. Exact squarefree/good/k collision restrictions can remain before the upper bound; enlarging them for this positive absolute estimate is valid.

The finite squarefree S-removal e sum of (Ne)^(-1/2) is a fixed-S constant. The active ell divisor sum is at most tau(v2), and summing the actual dyadic v2 ideals contributes O(A2) with the standard A2^epsilon divisor loss. The critical-line amplitude L_e^(1-s) contributes sqrt(A1)/(Nk sqrt(Nell Ne)), exactly once. Combining the joint D^(1+epsilon) bound with original normalization 1/D gives

 B_W^2(DYA2)^epsilon A2 sqrt(A1/Y) Phi(Y,D)
       *(1+log(2A1))^2.

This is the stated theorem. Epsilon losses in D,Y,A2 can be relabelled in the usual way; the two A1 logarithms remain explicit without an unproved polynomial A1/D relation. The argument never replaces a full-family bound by the value at one selected coefficient vector, nor admits arbitrary positive row weights.

## 5. Scope and surviving failure

The band(Y,2Y], Y>=1, excludes the unit dual ideal by explicit support decomposition. It retains every other ideal in the band, including S factors and sixth powers. The separate unit/prefix term and all original means remain in the full primitive identity. There is no centering or mean deletion.

The Phi term Y makes the asserted error-only majorant grow as sqrt(Y); its dyadic sum is not a complete signed bound. The genuine fixed-D transform decay and its derivative-dependent high tail are separate accepted inputs. No positivity, actual lower bound, new global exponent, GRH/determinant conclusion or missing intermediate cancellation is proved. General class/rho extensions require their own precise assembly even after the separately reviewed H_ROOT normalization proof. This acceptance does not silently enlarge the theorem beyond same-class/rho=1.

All source/HEAD/index protection and exact governing-note hashes are recorded in the acceptance receipt. No author controls, finite arithmetic datasets, historical phase runs, new Gaussian fixtures or builds were executed by this reviewer.
