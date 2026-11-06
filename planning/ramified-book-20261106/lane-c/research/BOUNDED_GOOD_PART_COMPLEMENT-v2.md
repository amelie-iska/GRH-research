# A new complementary cone: bounded good sixth-free part, arbitrary S part

NEW research-only candidate v2,6 November2026 (v1 preserved; the enlarged fixed-numerator family is derived explicitly). This estimates an ORIGINAL primitive-dual sector outside the accepted top-sixth band. It does not rerun the ramified FE, full-A_U proof, scalar/counting-mean split, accepted tails or old controls. The new ingredients are an exact finite-order audit of the TOTAL primitive character, compression of unbounded S-supported frequency phases WITHOUT restoring zeros, and a convergent weighted S-cone count.

Acceptance criteria: (i) audit the literal finite ray character and cancellation of auxiliary angular/radial extensions before choosing a common period; (ii) define the exact original projection and its lower-open/closed endpoints, including all rho and nonunit S modes; (iii) prove the phase identity with the indispensable raw conductor mask and all fixed-family dependencies; (iv) bound this genuinely larger sector using the accepted actual one-column theorem BEFORE the opposite-column/outer absolute counts; (v) keep the original finite k/capacity/Bessel/all primitive e-values; (vi) independent adversarial review and only fresh bounded support/phase controls. No book/canonical/global/queue/index edits are authorized by this note.

## 1. Original kernel, scope and exact new projection

Work in the ORIGINAL unweighted PURE two-pivot scope of FULL_AU_PURE_PREFIX-v3 (668f71eb), with its required coefficient/prefix-mask/control precisions. Fix K=Q(omega), original S, finite-order nu, source/ray/literal u0 with no good support, and ONE common complex smooth column W on[1,2], zero endpoints. Keep D>=2^64,1<=U<=sqrtD,A1~H=D^(3/4), exact capacity and ORIGINAL pre-S finiteK. B=||W||infinity, M(W) its stated Mellin norm, V1(W)=B+integral|W'|. The exact row interpolant G is NOT W; only0<=G<=1,support[1/2,5/2] and its accepted real Bessel remainder are used. If the original capacity is empty, define both projected pieces to be exactlyzero, as in the original representation.

The source primitive Poisson sum is over ALL nonzero integral dual ideals y, including S-supported ones (coherent-band-core cbk:exact-kernel; original derivation DRAFT-v8 cba96d34, Section5). For every y write its UNIQUE extraction
 y=h*r*s^6,
where h is S-supported, r good with every good valuation0..5, and s arbitrary good. The ideals r and s MAY overlap. All S valuations go in h. No SF condition is imposed on s or r; r is SIXTH-free, not squarefree. Equal rational norms never identify ideals.

Set X>=64,V=X^(1/6)/2, and fix B0=64. Define the cone
 C_64(X)={y=h*r*s^6: Nr<64, Ny<=X}
and its lower-sixth complementary part
 C_low(X)={y in C_64(X): Ns<=V}.                        (1)
All inequalities are literal: r bound is strict, total cap is closed, lower part has upper CLOSED Ns<=V. There is NO upper bound Nh*Nr<64 in C_low. Both sets are finite for each X; h is unbounded as X grows.

Let P_cone(X),P_low(X) be the normalized ORIGINAL primitive kernel with its y-sum restricted to the corresponding set(1), all other parameters unchanged. They include the original1/D ONCE. The raw numerators are D times these quantities. No density g, rho^6 projector, primal-row filter, positive energy or original sign change is introduced.

The accepted top piece P_X is an EXACT subprojection:
 C_64(X) = T_X disjoint_union C_low(X).                 (2)
Indeed Ny<=X implies Ns<=X^(1/6)=2V. If Ns>V then Nh*Nr<X/V^6=64, so w=h*r has Nw<64 and one obtains EXACTLY the accepted top support. Conversely any accepted w<64 has good sixth-free part r<64. The endpoint Ns=V, including Ny=X and N(hr)=64, belongs to C_low and not T_X. Thus (1) is an actual complement, not a renamed top band. For example its support contains y=(2)^3 at X=64,r=s=O,Nh=64; no nonzero-value assertion is made for a primitive component where that frequency is raw-zero.

The theorem is
 |P_low(X)|, |P_cone(X)|
 <<_(fixedS,nu,source/ray,epsilon) (DXA1)^epsilon A1 X^(1/6)
 { B[M(W)+V1(W)]D^(-1/9)
                   +B^2[A1X/D^2+D^-1] }.              (3)
The constants also depend on the fixed actual finite character family determined below. At X=D^(3/8), leading normalized power is101/144, Bessel power-1/16 and norm-fibre correction-3/16. These are upper budgets, not actual sizes or lower bounds. This is NOT all dual ideals Ny<=X: their unbounded good sixth-free part remains outside the theorem.

## 2. Order audit from literal finite characters, not 'type zero alone'

This audit does NOT infer finite order merely from the words type zero. The exact original derivation DRAFT-v8, Section4 lines79--85, obtains rho by expanding the COMPLETE original source/ray function AND every original fixed ray restriction in the FULL character basis of a FIXED FINITE ray-class group. Let G_ray be one fixed ray group dominating this actual finite family, and E_ray its exponent. No norm/radial Mellin character is inserted into this finite projector; sharp capacity is retained separately in G.

The pinned primary deFaveri2610.04045v1, Section2.3 and especially2.5.1, states that chi_a has order DIVIDING6 and trivial infinity type, and that chi-tilde_a is its primitive inducer. This includes the original good squarefree m,n family under the accepted physical identification. In the literal derivation eta is the primitive inducer of
 rho*chi_m*conjugate(chi_n).                            (4)
Thus its underlying unitary group character has order dividing
                       L=lcm(6,E_ray),                 (5)
uniformly in D,m,n and the actual source component.

The later auxiliary notation does NOT contradict(4):
 xi_m=chi-tilde_m/psi_A,
 barxi_n=bar(chi-tilde_n)/barpsi_B,
 sigma=prim(rho*psi_A*barpsi_B).
Multiplying gives eta=rho*chi-tilde_m*bar(chi-tilde_n) on the common unit domain; primitivization only changes the zero extension at dropped conductor primes. BOTH auxiliary angular and radial psi_A/psi_B factors cancel exactly. Individual xi or psi need not have finite order. This audit uses the literal finite row-ray basis and finite-order source characters, not Jacobi rho=j/sqrtN, which is a DIFFERENT infinite-order function already accounted for by vartheta.

Every original ray rho is retained. E_ray need not divide6, so rho^6 may be nonprincipal. No projection to rho^6=1 or substitution of a sixth-order individual xi occurs. If an additional continuous radial projector were ever introduced, (5) would have to be reproved; it is not part of the declared original finite projector.

Important raw convention: eta(a)^L=1 ONLY on ideals coprime to its actual primitive conductor. With its original zero extension,
 eta(a)^L=1_((a,f_eta)=1).
Do NOT replace it by the primitive principal character after taking a power.

## 3. Exact compression of unbounded S-supported h

Write uniquely
 h=h0*b^L,
where h0 is S-supported with0<=v_p(h0)<L, and b is S-supported arbitrary. The h0 possibilities form one FIXED FINITE family, independently of D,X or the good column conductors. Since b has no good support, the raw power law from Section2 gives EXACTLY
 bar eta(h)=bar eta(h0)*1_((b,f_S)=1).                  (6)
If h0 meets the actual primitive S conductor its literal value is0. If h0 does not but b does, the extra mask in(6) is0. Omitting that mask would wrongly restore primes when their exponents in h are multiples ofL.

Equation(6) does NOT divide by eta(e), eta(h0) or any primitive Gauss value. The original e|P_S value eta(e) stays separate. The original primal S exclusion and row/capacity masks are unchanged. A dual S-prime whose primitive value is permitted was present in the original full dual kernel; this is not restoration of a forbidden primal row value.

The actual nonzero character factor for y is still
 bar eta(h0*r) * bar rho_ray(s)^6
      *1_((s,m*n)=1)*1_((b,f_S)=1),                    (7)
with every original good r collision also retained. The source rho in(7) is the original ray component, not the Jacobi column rho. Formula(7) is the accepted total-character sixth-power identity together with(6); its means are not centered away.

For each actual primitive-S type the last mask in(7) is a literal0/1 scalar. Across types retain the exact finite joint selector and expand it in the FULL fixed product residue-character basis BEFORE a one-column estimate, as in the required finite-S refinement. Dependence on supp(b) gives only finitely many S-subsets, hence no growing conductor or new coefficient mass. Forbidden primitive values remain zero in the full finite sum.

Now w0=h0*r ranges over a FIXED FINITE set: h0 exponents<L and Nr<64. This is generally LARGER than the old w<64 family; that old finite-family constant is NOT silently reused. Here is the exact new match.

Choose the actual fixed integral generator gamma_w0 of w0, not assumed primary at S. The TOTAL eta has both angular and radial types zero by the audited product(4). Its finite primitive CRT component is theta_S*theta_q, theta_q=chi_(6,m)*bar chi_(6,n). Therefore EXACTLY
 bar eta(w0)=bar theta_S(gamma_w0)
              *bar chi_(6,m)(gamma_w0)*chi_(6,n)(gamma_w0).  (7a)
Every factor uses its actual conductor/convention. theta_S is evaluated at its OWN primitive f_S, including zero. The good-q symbols in(7a) are the primitive finite LOCAL factors in the CRT decomposition, NOT the original raw row symbols at S. A generator-unit change cancels in their total because eta is unit-trivial; no single factor's unit dependence is discarded. Equation(7a) is the all-component primitive finite-value identity already used for fixed e,w, now applied to each specified w0.

For a fixed nonzero gamma_w0, the denominator function m->chi_(6,m)(gamma_w0) is a finite-order Kummer Hecke character away from its literal bad support. The explicit arbitrary-FIXED-numerator construction in ACTUAL_FINITE_RESIDUE_FAMILY-v1(c70805fa), Section2, supplies a safe fixed conductor through the sextic polynomial discriminant ideal(6)^6(gamma_w0)^5; a fractional convention can first be cleared by a fixed sixth power. Keep original good-r collision zeros as well, even if the primitive character's conductor drops. Norm49 and repeated ideal factors are not replaced by rational squarefreeness or a radical-conductor family.

Take a NEW common modulus including the actual/safe conductors and raw supports for ALL these finitely many gamma_w0, together with the original nu/source/ray/Gamma/local-type data. Apply the GENERAL ramified fixed-finite-character theorem to this NEW family, rather than claiming the old w<64 family already contains it. Across primitive S types, bar theta_S(gamma_w0), the b-mask and the separate eta(e) are all retained in the exact finite selector with its full product Fourier expansion; no eta(e) division or replacement by a raw chi_m(S) occurs.

Constants may grow with this NEW FIXED family, S,L and the cutoff64, but not with b,h,D or X. This explicitly justifies unbounded S-supported frequencies using fixed support and the audited period, not a uniform theorem for arbitrary growing-conductor characters.

## 4. A convergent count of the genuine enlarged support

Let A_good(T) count good integral ideals of norm<=T. The elementary fixed-field lattice estimate gives A_good(T)<<_K T for T>=1, with zero count below1. All norm-fibre multiplicities, split primes and inert rational-square norms remain ideal counts.

Therefore
 #C_64(X)
 <=C_K X^(1/6)
    sum_(r good SIXTH-free,Nr<64)(Nr)^(-1/6)
    sum_(h S-supported)(Nh)^(-1/6)
 = C_(K,S,64) X^(1/6),                                (8)
where the last positive MAJORANT is
 sum_(h S-supported)(Nh)^(-1/6)
           =product_(p in S)(1-(Np)^(-1/6))^(-1)<infinity.
Only a nonnegative COUNT is extended to this infinite geometric majorant. The original finite dual kernel is not Euler-completed, and no signed sum or Mellin integral is interchanged.

The same bound applies to C_low by retaining its exact Ns<=V condition. One may equivalently sum h=h0*b^L first; its weighted product is exactly the same finite-S geometric factor, so counting all h0 residue phases does not insert a power ofX. Unit ideals in r,s,h are included. r/s and k/s overlaps remain legal; no rational squarefree substitution is made.

## 5. Leading-model estimate before the outer frequency triangle

Replace dotG by its actual bounded g0, keeping all original supports. For EACH fixed actual source/e/k/r/h0/b/s and original opposite n, (6),(7) put the left column in the accepted actual finite-character family. Its only growing masks include
 Q_long=rad_good(p*n*k*s*r).
The arbitrary S part h contributes no good primes; its residual phase was compressed exactly, not discarded. Prefix(p,n), prefix/k/s/r zeros remain in the outer prefix coefficient, as in the accepted full-A_U proof. No growing n or s is moved into kappa. The opposite original column is frozen before the one-column estimate.

The completed full-A_U linear estimate is already PROVED; it is an INPUT, not rerun here. It gives balanced/large/small-prefix bounds
 M(W)D^(1/3+epsilon),
 M(W)D^epsilon[D^(1/3)+sqrt(D/Z)],
 V1(W)(D Nk X)^epsilon D^(1/4)(Nk)^(3/8)Z^(5/8),
uniformly over this FIXED enlarged phase family. The last Q divisor cost is controlled by
 NQ_long <<_64 D Z X^(1/6) Nk.
All exact scalar zeros from(7) remain before these estimates. The finite-family constants are independent of b. No per-conductor absolute Cauchy or counting-density replacement is used in lieu of this actual angular Gauss estimate.

Set Z=D^(2/9), as in the accepted theorem. AFTER the first-column bound, the true opposite A_U column costs B sqrtD D^epsilon. The original normalization is A1/D ONCE. The exact finite original k sum is retained; only its positive majorant Nk^(-13/8+epsilon) is bounded by a convergent ideal series. There is no mu(k) cancellation, new k cutoff or completed eta Euler factor.

ONLY NOW count the actual frequency support with(8); every ray phase bar rho_ray(s)^6 and primitive e/h0 value was retained through the column estimate. This gives the leading term of(3). The optional original unequal-norm projection has the SAME fixed-n norm-fibre subtraction, contributing at mostB^2 A1 X^(1/6)D^(-1+epsilon), with distinct conjugate ideals retained.

## 6. Exact Bessel error; no nodal-profile variation shortcut

For Ny<=X the actual argument satisfies
 A1 Ny/[(Nk)^2 Ne F]<=Lambda=A1X/D^2.
Use ONLY the accepted derivative-free real-axis bound
 |dotG(x)-g0|<=3C0^(-3/2)x.
There are O(D^2) actual annular column pairs, original prefactor at mostA1/D^2, true coefficient products B^2D^epsilon, finite source/e mass and original k absolute budget sum Nk^-2. Count the enlarged ORIGINAL y support by(8). The resulting error is
 << B^2(DX)^epsilon A1 X^(1/6)*Lambda.                  (9)
This estimates the actual G transform, with its sharp-capacity nodal derivatives never assumed uniform or replaced by W derivatives. The g0 value may vanish and is never divided out. All derivative costs of the original row profile remain outside any unproved infinite-tail conclusion.

Combining Sections5--6 proves(3) for BOTH the new lower complementary piece and the whole bounded-good-part cone. At X=D^(3/8), it is target-sized with the declared fixed profile seminorms. The same finite set of original e/k/capacity/ray data appears in every expression.

## 7. Exact remaining failure and next sector

Attempting the same argument for ALL original dual ideals Ny<=X would let the good sixth-free r grow withX. Although eta has bounded ORDER(5), the fixed-numerator character at r can have growing CONDUCTOR as a function of the column. Bounded character order does not make that family fixed or justify the constant in the accepted sharp mean. The finite-S h compression does not compress new good primes. That is the exact unsupported step, so no full-ball estimate is claimed.

The survivor is the NEW actual C_low(X) cone complement (and C_64(X)), including all S-supported frequencies up to the true total cap and all original rays/means. Good sixth-free part Nr>=64, the rest of the finite/infinite frequency complement, mixed/neighboring sectors, short/principal assembly, positive arithmetic determinant/zero-location, separate Dirichlet/Hecke/Dedekind/elliptic/generalArtin scopes, actual analytic/categoryLean and GRH remain OPEN. Whole signed13/12/global unsigned9/8 remain unchanged. There is no nonzero-energy lower bound, automatic positivity, quantum/learning/Lean result or proof schedule.

All original source/cache/environment/history/index and public canonical artifacts remain preserved. This candidate is outside the frozen ramified-book integration until its own independent review and source/hash closure.
