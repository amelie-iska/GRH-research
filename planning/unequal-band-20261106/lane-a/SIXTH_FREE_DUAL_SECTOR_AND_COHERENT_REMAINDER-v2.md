# Sixth-power-free dual sectors and the remaining coherent power part

NEW research-only v2 (v1 preserved; good-argument raw-zero qualifier explicit), 6 November 2026. This is an application of the ALREADY PINNED physical sixth-power-free sieve to a new actual dual-frequency sector. It proves a scoped target-size estimate for the pure unequal-norm sector with sixth-power-free dual frequency through normD^(1/2), including the proposed D^(3/8) band. It does NOT bound the FULL proposed literal band, the remaining sixth-power-divisible frequencies or the full signed target. The current whole13/12/global9/8 bounds are unchanged. No old control, table, build, browser or publishing operation is rerun.

## 1. Inputs, actual family and exact frequency partition

Read the coherent-band HANDOFF-v1 90a6be03..., aggregate34b4f9a5..., RUN_CLOSED77a7ac3c... and current master e32be6af.... The primitive Poisson representation DRAFT-v8 plus its two-pivot scope addendum, global root normalization, all-component finite-prefix transport and equal-norm-sector bounds are accepted INPUTS. This note does not reprove those finished routes.

Keep the original complete good SF IDEAL annulus D<=Nm<=2D, D>1, original

 c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
 A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b),1<=U<=sqrtD.

There is ONE common fixed possibly complex W supported in[1,2], B_W=||W||infinity, fixed original nu/S/ray/source data and distinct equal-norm/conjugate ideal coordinates. Rows are ONLY the original UNWEIGHTED two-pivot family v3=v4=v5=v6=O, with fixed literal unit/S-supported u0 having no good-prime support, original SF/coprime v1,v2, ray/literal data and exact Nu0 Nv1 Nv2^2<=H capacity. All exact finite pre-S K_ell, k/ell/e signs and masks, primitive S values, roots and common-profile coefficients remain. No arbitrary extra row weights, good frozen factors or varying-u0 sum is inserted.

Let P_D=D S1AA be the actual signed numerator, with ALL original finite source-class/rho components of its accepted primitive Poisson representation. Write P_leX[Omega] for its exact finite primitive-ideal frequency prefix Ny<=X, restricted to y inOmega. Restricting an ORIGINAL column pair to Nm!=Nn defines P_neq,leX[Omega]. This is a representation-fixed projected signed quantity, not a positive energy. The old literal additive beta bands are NOT identified with these primitive ideal prefixes or sectors without a justified frequency map.

Every integral dual ideal has the UNIQUE decomposition

    y=r s^6,   r sixth-power-free, s integral,              (1)
    v_p(r) in{0,1,2,3,4,5}, v_p(s)=floor(v_p(y)/6).

Overlaps of r and s are ALLOWED: a prime exponent7 has exponent1 in r and1 in s. Put F6={y:all v_p(y)<=5}. The exact projected prefix partitions as

    P_leX=P_leX[F6]+sum_{1<Ns<=X^(1/6)}P_leX[s],           (2)

where P_leX[s] keeps precisely y=r s^6 with r sixth-power-free and Nr<=X/(Ns)^6. The same partition holds for unequal norms. No projected term is discarded or declared necessary to be small individually for the full kernel; different terms may cancel.

The external input, at physical ideal lengths Z,L, is precisely

 F6norm(Z,L)=Z+L+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6),
 sum_{r good6free,Nr<=Z}|sum_{a SF good,Na~L}b_a R_a(r)|^2
       <<_epsilon (ZL)^epsilon F6norm(Z,L)sum_a|b_a|^2,
                                                        Z,L>=1. (3)

It is the already pinned de Faveri arXiv2610.04045v1 Theorem1.1 at n=6 on the matched primary residue family, both physical indices sixth-power-free. Residual SF columns are a permissible subset; ray/source-class restrictions are zero coefficients inside the positive comparison. This is not the all-ideal Phi norm: extracting an arbitrary sixth-power part from the ROWS of(3) is precisely what creates its extra L Z^(1/6) term. There is no generic conductor substitution.

## 2. New finite-sector estimate

For EVERY finite X>=1,

    |P_leX[F6]|/D
      <<_(fixeddata,epsilon) B_W^2(DXA2)^epsilon
                                (A1A2/D)F6norm(X,D).      (4)

The SAME bound holds for the unequal-norm projected prefix:

    |P_neq,leX[F6]|/D
      << B_W^2(DXA2)^epsilon(A1A2/D)F6norm(X,D).            (5)

A finite annular sector Y<Ny<=2Y follows by taking the difference of two such exact prefixes, with X=2Y and the same sixth-free restriction. All nonunit/S-supported/class/rho modes WITHIN THAT restriction remain; the dual unit is included in a prefix and is never centered away.

In the pure critical block A2=1,A1 comparable to H=D^(3/4), (4)--(5) are target-sized for X<=constant*D^(1/2), up to epsilon. Indeed every term of F6norm(X,D) is O(D) there; the bottleneck is X^(1/3)D^(5/6). Thus the actual unequal-norm sixth-free primitive band Y comparable to D^(3/8) is controlled at the target. This does NOT identify or bound the FULL literal additive B_Y from the preceding note, and does not account for the omitted nontrivial sixth-power parts in(2).

For reference, at the critical mixed scales(A1,A2)=(D^(5/12),D^(1/6)) the same sixth-free sector is target-sized for X<=constant*D, since F6norm(X,D)<=O(D^(7/6)). No new whole mixed-beyondD gain is asserted.

## 3. Proof of the all-component sixth-free prefix bound

Fix an original source pair A,B and ray rho, with its proved distinct root gauges and primitive fixed S character sigma_ABrho. Their true primitive product has conductor F_S mn and total infinity type0. Use the accepted Mellin formula for the ACTUAL sharp-capacity G_v2 at a FIXED line0<lambda<1/2. Its product with the field gamma factor is integrable in the vertical variable uniformly in capacity/A1. We use that already proved input, not a new smoothness assumption.

For the prefix Ny<=X, the modulus of its Mellin row weight(Ny)^(-lambda-it) is <=1, since Ny>=1. Keeping it before Cauchy gives the same positive comparison with this upper bound. There is no contour at0, no dropping of the dual unit and no summation of an infinite-dual series.

First insert the original coprime-column identity, with its full signs and the auxiliary individual-column extension as previously accepted. On m=da,n=db, a,b are SF and coprime to d but may overlap EACH OTHER. Actual A_U(da), beta_da, primitive S phases, nu(da) and W(Nd Na/D) remain UNFACTORED. For the two source-Mellin vectors, the original-annulus coefficient norms are

    ||b_d(lambda+it)||_2^2,||c_d(lambda-it)||_2^2
          <<B_W^2 D^(2lambda+epsilon)/Nd.                 (6)

They are bilinear different-class vectors; no PSD assertion is used. Raw(d,r) is kept in the identity and removed only inside the two positive norms. Each residual-class common primitive row phase is cancelled INSIDE its own norm before the raw finite-order family(3) is applied; individual xi_a is not assumed sixth-order.

If y is sixth-free, write y=h r with h S-supported and good r. Each S-prime exponent in h lies between0 and5. Hence h ranges over a FIXED finite set of at most6^|S| ideals. At a fixed nonempty h term, Nh<=X and Z_h=X/Nh>=1. The good r remains sixth-free, and(3) gives F6norm(Z_h,D/Nd). Primitive sigma(h) zeros suppress the actual term; they are never restored to a raw forbidden S value. Primitive xi_da(h) values stay actual bounded column phases.

For L=D/Nd>=1 the divisor sum is

    sum_{Nd<=2D}(Nd)^(-1)F6norm(Z,L)
       <<_epsilon D^epsilon F6norm(Z,D),                  (7)

because the four d exponents are1,2,4/3,11/6; only the first is logarithmic. For1/2<=L<1 the possible residual unit is counted directly, yielding the same comparison, not a subunit sieve. Empty subsequences contribute0. The finite h sum costs only a fixed S constant. This is a new use of the power-free input(3), not of the finished all-ideal Phi estimate.

As before, the exact finite k weights are bounded AFTER the joint column estimate by the positive majorant zeta_K^S(2-2lambda), lambda<1/2. This does not complete the actual finite k sum. E finite weights, ell's actual cutoff/divisor loss, the v2 count and the actual BV--Gamma integral have the accepted bounds; normalizing ONCE byD gives

    |P_leX[F6]|/D
       <<_(lambda,epsilon) B_W^2(DXA2)^epsilon
           A2 A1^(1-lambda)D^(2lambda-1) F6norm(X,D).      (8)

Here we deliberately bounded Ny^(-lambda) by1. We do NOT claim the sharper X^(-lambda) version for a prefix: the constant-row L term of F6norm has exponent0 and cannot be dyadically summed with exponent-lambda as an increasing geometric series.

Given a final loss eta>0, choose fixedlambda=min(1/12,eta/4)>0 and inputepsilon=eta/2. Since A1>=1, D^(2lambda)A1^(-lambda)<=D^(eta/2). Absorb this in(DXA2)^eta to obtain(4). Constants may depend on eta; the contour never becomes0. Summing the actual FINITE number of class/rho components reconstructs the full original frequency sector, with their fixed primitive F_S^(lambda-1/2)<=1 retained in the identity. No all-component root phase is silently replaced by1.

## 4. Unequal norms without a false positivity subtraction

Let P_eq,leX[F6] be the SAME projected frequency sector restricted to the ORIGINAL coprime equal-norm off-diagonal pairs. Then exactly

    P_neq,leX[F6]=P_leX[F6]-P_eq,leX[F6].                 (9)

The accepted elementary equal-norm argument gives O_K(D) ordered pairs, with n=bar m and split-only rational-squarefree norm. For completeness its prefix upper bound uses only pair counting, not a high-tail theorem: |c_m bar c_n|<=B_W^2 D^epsilon; sqrt(Nm Nn)>=D; the actual dotG is uniformly bounded by C0^(-1/2)int G=O(1); there are O(X) integral ideal frequencies Ny<=X; finite k absolute weights sum at exponent2, e is fixed and ell costs its original divisor factor. Counting v2 and normalizing byD therefore gives

    |P_eq,leX[F6]|/D
       << B_W^2(DXA2)^epsilon(A1A2 X/D).                 (10)

Restricting to sixth-free y only reduces this absolute count. No equality-norm fibre, S mode, root or original sign is deleted in(9); the modulus comparison occurs only in its bound. Since F6norm(X,D)>=X, (4),(9),(10) prove(5). This is not a claim that the whole signed kernel or its different bands are positive.

## 5. Fixed nontrivial sixth-power part and exact recovery of the old cost

At fixed s in(1), primitive multiplicativity gives

    conjugate(eta(r s^6))
        =conjugate(eta(r))conjugate(eta(s))^6,            (11)

with actual zeros at primes of the primitive conductor. Individual xi_m need not have sixth power1. On a general rho component the S/ray correction in eta(s)^6 is NOT discarded: the scalar sigma_ABrho(s^6), the individual xi_m(s^6)/xi_n(s^6) column phases and all(mn,s) collision zeros are retained. On good s COPRIME TO mn it induces the fixed ray character rho^6 after the source order-six parts cancel. At a good prime of mn the original value is still ZERO, not rho(s)^6; this conductor-drop deletion and all S values stay as written. Overlap(r,s) remains allowed.

For each fixed s, its extra factors are legitimate bounded column/scalar modulations. Apply the SAME proof to the remaining sixth-free r prefix Nr<=X/(Ns)^6; all original finite K and G profiles remain, now with their exact scaled frequency. Bounding Ny^(-lambda) by1 again gives, uniformly for1<=Ns<=X^(1/6),

    |P_leX[s]|/D
      << B_W^2(DXA2)^epsilon (A1A2/D)
                                  F6norm(X/(Ns)^6,D).  (12)

The same elementary equal-norm subtraction yields(12) for the unequal-norm component. This is uniform only for the stated fixed original data, not over new good frozen primal factors or new row weights.

If the s sum is now estimated absolutely, elementary ideal counting and the convergent sums at exponents6,5,2 give

 sum_{Ns<=X^(1/6)}F6norm(X/(Ns)^6,D)
    << X +D X^(1/6)+X^(5/6)D^(1/3)+X^(1/3)D^(5/6)
     =Phi(X,D).                                         (13)

The constant-row D term costs the NUMBER of s, not a convergent reciprocal sum. Equation(13) reproduces the finished all-ideal prefix majorant exactly. Calling the s=1 result a bound for the complete band, or replacing the D count by a convergent sum without a new signed estimate, would be the failed step.

## 6. Attempted coupled s/k cancellation and its exact limitation

Could the ORIGINAL mu(k) square-divisor sum cancel those nontrivial s contributions before(13)? The masks do not give a divisor convolution in s. The original k is an independent good SF ideal with Nk<=K_ell and(k,v2)=1; it is NOT restricted by k|s or k^2|y. Imposing either relation changes the actual Poisson expression. Raw(k,mn) and raw(s,mn) are retained, but there is no original raw(k,s) deletion to invent.

At a single good prime p, a formal completed local product on the pure r=O branch would be

    [1-eta(p)^2(Np)^(-2+2z)]
       /[1-conjugate(eta(p))^6(Np)^(-6z)].                (14)

This is only an AUXILIARY algebraic diagnostic in the common initial domain where the two local series converge; it is NOT substituted for the actual finite-k/Bessel expression. The latter has its exact cutoff and nonseparable profile, and its r/s truncation is not multiplicative. At the formal sixth-power mean location Re z=1/6, the numerator exponent is5/3, so a single local factor is nonzero (|eta(p)|<=1); a mu(k) factor is not a termwise annihilator of the sixth-power frequency series. No claim of an uncancelled global pole of the actual form follows, and no reciprocal-L/GRH barrier is asserted.

In the SAME-class/rho1 component specifically, eta is the finite-order primitive character inducing the original order-six quotient. Thus for good s coprime to its conductor,

    eta(s^6)=1.                                         (15)

This concerns the TOTAL eta, not the individual xi_m or the generalrho component. The full raw(s,mn) mask remains. The nontrivial sixth-power frequencies can therefore replicate the unit character mean; there is no new varying character oscillation in s supplied by(15). Their root/A_U/W/dual-profile outer pairing can still cancel, including with other r/s or class/rho pieces, and that is exactly the still-missing arithmetic estimate.

The precise surviving theorem is(4)--(5),(12). The genuine signed task remains to control the sum of the nontrivial s parts together with their actual r/k/root/column orientations before the s, d or conductor triangles. A fixed-field scalar PIT, generic conductor sieve, sixth-power independence, finite-ray mean-zero assertion or positivity of an auxiliary d extension does not provide that estimate. This note does not prove its impossibility; it identifies the exact unsupported convolution/cancellation step and retains the current whole signed13/12/global9/8 bounds.

These projected primitive-ideal results are OUTSIDE the concurrently implemented book material until independently reviewed. No literal additive-band match, all-u0/extra-factor/principal assembly, physical energy lower bound, determinant/zero-location/Lean/category or GRH conclusion is asserted. This lane writes only its fresh owned directories and does not edit root/canonical/queue/book/UI files.
