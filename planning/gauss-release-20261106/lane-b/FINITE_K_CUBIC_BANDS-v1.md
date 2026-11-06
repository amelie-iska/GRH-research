# Coupled physical-cubic bounds for the original finite-k bands

NEW research-only v1,6 November2026. This is a finite-frequency partial bound on the ACTUAL exact-discrete pure top prefix, including the remaining BOTH-TypeI piece. The new step transposes the already accepted physical cubic sieve to the ORIGINAL k frequency and applies it to the two columns jointly after exact gcd inversion. No other-column triangle is taken. This does not estimate the unit/very-short-k remainder or the whole small-cutoff model. Independent review is required.

No old theorem/experiment/control is rerun or counted as new evidence. No paper is downloaded, dependency installed, source/book/UI/queue/index/release/auth operation performed. The current gauss-book HANDOFF and its accepted direct-v2/HB-v2/root-phase notes are INPUTS. Any future git reads in this lane require GIT_OPTIONAL_LOCKS=0; this derivation uses no git command.

## 1. Actual scope and normalization

Work in O=Z[omega], with original fixed S above2,3, fixed source/ray/literal data and fixed finite-order nu. Columns are ALL good squarefree IDEALS in D<=Nm<=2D, D>1; conjugate/equal-norm ideals stay separate. Keep the original ordered coprime column mask. The original unequal-norm mask may optionally also be imposed consistently. W is ONE fixed possibly complex smooth common profile supported[1,2], with B=||W||infinity. The original cutoff satisfies1<=U<=sqrt(D).

Only original UNWEIGHTED PURE two-pivot rows are asserted: A2=1,v2=O and all other good factors unit, fixed literal unit/S-supported u0 with no good support. The original row capacity and its integer endpoints are fixed. If b_cap<a_cap the representation is defined to be0. Otherwise K=sqrt(b_cap) is the ORIGINAL pre-S square-divisor cutoff, with K<=sqrt(2A1). It is not recomputed using e,s,w,Y or a frequency band. The actual nodal row profile G obeys0<=G<=1,support[1/2,5/2]; C0=3/(4pi²),g0=C0^(-1/2)int G, so |g0|<=2C0^(-1/2), without any derivative bound.

Fix X>=64,V=X^(1/6)/2 and the exact finite support from accepted DIRECT-v2:

 T_X={(w,s): w integral,Nw<64; s good integral,
              V<Ns<=2V, Nw(Ns)^6<=X}.                    (1.1)

The good part of w is automatically sixth-free. All S-supported w modes are included; s is arbitrary good, not necessarily squarefree. Overlaps w/s,k/s and k/w are ALLOWED, and no new coprimality is imposed on them. All original rho are present, not merely rho^6=1. The actual primitive factor eta=xi_m bar(xi_n)sigma has total type0 and conductor norm F=F_S NmNn on original coprime columns. Its identity

 bar eta(s^6)=bar rho(s)^6 1_((s,mn)=1)                   (1.2)

is the accepted total-character statement, not an order-six assumption on the individual xi.

Let B1(m),B2(m) be actual original coefficient choices, and put C_i(m)=mu(m)B_i(m). For the BOTH-TypeI application, C_i is instead the exact TypeI part of mu(m)A_Y(m) in the accepted HB decomposition,1<=Y<=min(U,D^(1/8)); D>=2^64 is required for the stated one-long-factor classification. The TypeI assignment uses only original factor dyadic scales, not k,n,s or the other column. Consequently it is an actual function of its OWN column m, and

 |C_i(m)| <<_epsilon D^epsilon.                         (1.3)

This follows from the accepted bounded number of factor assignments; original short factors have coefficient1 and the residual HB factors retain their genuine signs. There is NO extra mu(m) multiplying C_i. Original mu*A_Y, mu*A_U and their differences also satisfy(1.3). Below coefficients are never replaced by arbitrary favorable vectors; the external norm may of course be applied to their actual vectors.

P_J[C1,C2] denotes the corresponding part of the NORMALIZED exact-discrete prefix(2.1) of DIRECT-v2, retaining only good SF k with

                  J<Nk<=min(2J,K), J>=1.                (1.4)

Thus its original1/D occurs ONCE. L_J is the same expression with dotG replaced by g0. No Euler completion is performed. The raw numerator is D P_J. An empty capacity or band has value0. Absence of actual SF rows in a nonempty integer interval alone does not make a selected dual piece0.

## 2. New statement and inherited external input

For every epsilon>0, the actual leading band satisfies

 |L_J[C1,C2]| << B²(DKX)^epsilon A1 V
       { J^(-2)+(DJ)^(-1)+D^(-1/3)J^(-4/3) }.           (2.1)

Constants depend only on the fixed S/source/ray/nu data and the fixed divisor-bound exponents of the declared coefficient pieces. They are uniform in the original K, all retained finite e/w/s modes, primitive conductor drops and the common profile except B. This is not a new arbitrary-row-weight theorem.

For the exact Bessel band, define Lambda=A1X/D². Then

 |P_J-L_J| << B²(DKX)^epsilon A1 V Lambda/J.              (2.2)

For any1<=J0<K, summing the literal dyadic partition of J0<Nk<=K gives

 |P_(Nk>J0)[C1,C2]| << B²(DKX)^epsilon A1 V
  {J0^(-2)+(DJ0)^(-1)+D^(-1/3)J0^(-4/3)+Lambda/J0}.    (2.3)

It is only this finite part of the original representation. The sign of mu(k) is retained in the identity and then lost inside a stated Cauchy bound; no signed-Mobius theorem or lower bound is asserted.

The ONLY deep analytic input is the existing pinned de Faveri arXiv:2610.04045v1, Theorem1.1/Example2.2 at n=3, already mapped to the physical primary cubic matrix in cbk:cubic-norm:

 sum_(k SFgood,J<Nk<=2J) |sum_(a SFgood,L<=Na<=2L)
                      z_a chi_3,a(alpha_k)|²
  <<_epsilon (JL)^epsilon [J+L+(JL)^(2/3)] sum_a|z_a|²,
                                                J,L>=1. (2.4)

Both indices are actual squarefree ideals, hence cube-free. The generators alpha_a,alpha_k are the unique multiplicative primary1mod3 generators. The raw cubic symbol is0 at a common prime. Reciprocity gives the required transpose with NO conductor/radical replacement. Deleting S or retaining a source-class subset is a restriction of a positive norm; arbitrary COMPLEX coefficients are allowed. Unit/small residual lengths can be handled directly as in Section4. The external result is an INPUT, not a proof supplied here. PUBLIC citation metadata b0b3eae7 pins the exact primary version; primary cache stays private/local and is not redistributed.

## 3. Exact all-component separation of the k dependence

The accepted Gauss/Jacobi root identity and all-component phase package give, on original coprime m,n,

 epsilon(eta)= theta_S(alpha_m alpha_n)theta_q(gamma_S)
   [tau_(gamma_S)(theta_S)/sqrt(F_S)] Gamma(alpha_m alpha_n)
   mu(m)mu(n)vartheta(m)bar vartheta(n)bar G_m G_n,
 theta_q=chi_6,m bar chi_6,n.                            (3.1)

Here theta_S is the ACTUAL primitive finite S component at its OWN conductor, including every drop and unit-conductor convention. Its finite root factor has modulus1. No primitive S Gauss sum is divided out or evaluated at an induced modulus. The original e and w factors retain the SEPARATE actual primitive values theta_S(gamma_e) and bar theta_S(gamma_w); a0 kills its summand. Good-denominator fixed-numerator symbols at gamma_e/gamma_w/gamma_S retain raw collisions, and are not quotiented into a ratio which restores a zero.

The important new observation for the coupled estimate is exact:

 eta(k²)=theta_S(alpha_k)² chi_3,m(alpha_k)
                                  bar chi_3,n(alpha_k). (3.2)

ALL other dependence on k is its ORIGINAL mu(k)/(Nk)² and finite cutoff. No unbounded k-dependent coefficient function is placed in a fixed column vector. theta_S(alpha_k)² is a bounded scalar. This total-type0 identity holds for every retained rho by accepted DIRECT-v2 Section3, including nonprincipal rho^6. Individual xi can have infinite type.

To separate Gamma jointly, let H=(O/4)^times,|H|=12 and expand

 Gamma(t)=sum_(chi in Hhat) gamma_chi chi(t),
                   sum|gamma_chi|<=sqrt(12).             (3.3)

Hence Gamma(alpha_m alpha_n) is an EXACT finite sum of a left multiplier chi(alpha_m) and a right multiplier chi(alpha_n). The right column gauge must therefore be conjugated appropriately in the linear-first convention; the two vectors need NOT coincide. Original class indicators remain zero coefficients. Source pairs/rho, e and this finite Fourier sum have fixed total coefficient mass.

For fixed component omega (including source pair,rho,e,w,chi), and fixed s allowed by(1.1), the band is therefore a fixed bounded scalar times A1 g0/D times

 sum_(k SFgood,J<Nk<=min(2J,K)) mu(k)zeta_omega(k)/(Nk)²
  sum_(m,n SFgood annulus) 1_((m,n)=1)
       x_m(omega,s) bar y_n(omega,s)
                  chi_3,m(alpha_k)bar chi_3,n(alpha_k), (3.4)

with |zeta_omega(k)|<=1. The scalar retains bar rho(s)^6, all h_ABrho(O), 1/sqrt(F_S), mu(e)/Ne, separate primitive e/w values, the S root and Fourier coefficient. The actual x,y retain C_i, ONE W per original column, nu, vartheta, cubic Gauss roots, the distinct S/source gauges, all numerator zeros and the mask1_((m,s)=1) or1_((n,s)=1). In particular

 |x_m|,|y_m| << B D^epsilon/sqrt(Nm).                    (3.5)

They are INDEPENDENT OF k. They may depend on omega,s arbitrarily with(3.5); we do not claim their phases disappear. The finite original sum over omega,s reconstructs L_J exactly. Formula(3.4) is an equality only on the original coprime support. Its separable off-coprime extension below is auxiliary, never the primitive root of overlapping conductors.

This reduction is more specific than a generic Schur norm of the finite-k map: that older map estimated the whole k series by its absolute l1 mass. Here the actual cubic-frequency matrix is retained until a two-column norm has been taken across the physical k band.

## 4. Coprime inversion and simultaneous two-column norm

Initially omit only the OPTIONAL unequal-norm projection; Section5 restores it. Insert the EXACT identity

 1_((m,n)=1)=sum_(d|m,n)mu(d).                           (4.1)

Every ideal divisor is included. d is good SF,Nd<=2D. On writing m=da,n=db, coefficients x_da,y_db are0 unless da,db are original SF annular columns. In particular(a,d)=(b,d)=1 are retained. They are NOT factored: neither C_i(da),A_Y(da),Gauss_da nor the source gauge is replaced by a multiplicative value.

Raw denominator multiplicativity gives, INCLUDING collisions,

 chi_3,da(alpha_k)=chi_3,d(alpha_k)chi_3,a(alpha_k).        (4.2)

Thus (3.4) is the exact sum over d of mu(d) times the k pairing

 sum_(k in band) mu(k)zeta_omega(k)/(Nk)²
           |chi_3,d(alpha_k)|² F_d(k)bar H_d(k),
 F_d(k)=sum_a x_da chi_3,a(alpha_k),
 H_d(k)=sum_b y_db chi_3,b(alpha_k).                     (4.3)

The residual a,b may overlap AFTER this inversion; (4.3) is an auxiliary Gram extension, not a primitive-character assertion at their overlapping product. The full signed d sum alone recovers the original mask.

Now, and only now, triangle in d and apply bilinear Cauchy in k. Since Nk>J, the absolute value of each d pairing is at most

 J^(-2) [sum_(k in band)1_((d,k)=1)|F_d(k)|²]^(1/2)
          [sum_(k in band)1_((d,k)=1)|H_d(k)|²]^(1/2).    (4.4)

This keeps BOTH actual coefficient vectors through the k average; there is NO pointwise column estimate followed by an absolute count of the other column. Dropping(d,k)=1 or the last clipped k endpoint is legal only inside these positive norms. No arbitrary positive row weight is asserted: this is the original unweighted SF k set of the cubic theorem.

Put L=D/Nd. For L>=1, actual subsequence counting and(3.5) give

 sum_a|x_da|², sum_b|y_db|² << B²D^epsilon/Nd.             (4.5)

For example there are O(D/Nd) residual ideals and each squared coefficient is O(B²D^epsilon/D). All original masks may be kept as zero coefficients. Applying(2.4) to each of the two norms yields a d contribution

 << B²(DK)^epsilon J^(-2)/Nd
                         [J+D/Nd+(JD/Nd)^(2/3)].         (4.6)

For D<Nd<=2D, L in[1/2,1) and the only possible residual is the unit (a nonunit good ideal has norm at least7). Direct counting O(J) k rows gives O(B²D^epsilon J^(-1)/Nd), with no application of an external norm below length1. Summing these d contributes O(B²D^epsilon/J), already covered below.

Elementary ideal counting gives

 sum_(Nd<=D)1/Nd <<log(2D),
 sum_d(Nd)^(-2), sum_d(Nd)^(-5/3) <<1.                  (4.7)

Consequently the full actual coprime pairing(3.4) is bounded by

 B²(DK)^epsilon J^(-2) [J+D+(JD)^(2/3)].                 (4.8)

Only absolute d counts in(4.7) were used; no cancellation of mu(d) is claimed. The physical lengths in the cubic theorem are J and D/Nd. This is not the older identity-source-class d-by-a cubic application: k is now the ORIGINAL frequency row, d is merely inverted, and no class restriction on d or factorization of C_i(da) is required.

## 5. Original equal-norm projection, finite s and Bessel error

If the original mask also requires Nm!=Nn, subtract the SAME component's equal-norm fibre before applying its final bound. There are O(D^(1+epsilon)) ordered equal-norm pairs in the annulus (at most D^epsilon ideals at each fixed rational norm); no rational-squarefree replacement is used. Each product of coefficients has modulus O(B²D^(-1+epsilon)). The ORIGINAL k band has absolute weighted count O(1/J). Its normalized contribution is therefore

                    <<B²D^epsilon A1 V/(DJ),            (5.1)

which is already one term of(2.1). No false multiplicativity of the equal-norm indicator or unrelated whole-sector subtraction is used.

There are finitely many w of norm<64, and for each such w the exact good s set in(1.1) has O(V) elements, with the upper endpoint clipped EXACTLY at X^(1/6)(Nw)^(-1/6). The original bar rho(s)^6, s/mn zeros, w/s and k/s overlaps are preserved in(3.4) before that absolute count. Fixed e/source/rho/S/Fourier sums have bounded total mass. Multiplying(4.8) by A1 g0/D and O(V), and including(5.1), proves(2.1).

For(2.2), use ONLY the accepted real-axis pointwise input

 |dotG(x)-g0|<=3C0^(-3/2)x,
 x=A1 Nw(Ns)^6/[(Nk)² Ne F]<=Lambda.                    (5.2)

No Taylor experiment or derivative-uniformity assumption is introduced. The two actual annular coefficient counts, |C_i|<=D^epsilon and the single normalization give the usual B²D^epsilon A1V Lambda, while the restricted finite k band now has absolute weight O(1/J). This proves(2.2). It is intentionally a safe coarse bound: the additional factor(Nk)^(-2) inside x is not needed or optimized. No finite endpoints or nonunit S modes are discarded.

Finally partition J0<Nk<=K by (2^j J0,min(2^(j+1)J0,K)] until the ORIGINAL K, with no infinite or Euler continuation. The convergent geometric bounds for each displayed negative power prove(2.3), with constants independent of the number of bands. Empty final bands remain empty.

## 6. Critical consequence and exact remaining obstruction

For K<=C sqrt(D), in particular the original nonempty pure capacity with A1<=D, all three leading terms in(2.3) are O_C(J0^(-2)) for1<=J0<K. Thus

 |P_(Nk>J0)[C1,C2]| << B²(DKX)^epsilon A1V
                                  [J0^(-2)+Lambda/J0]. (6.1)

Compare the available elementary k-band count: applying pointwise |Gauss|<=1 and separate column absolute sums gives only A1V/J0. The improvement in(6.1) arises from the actual physical cubic-frequency norm across k BEFORE a separate-column triangle, not from a generic completed Euler multiplier. The earlier root Schur note only gave the full finite-k l1 constant; it did not prove this frequency-band estimate. Balanced HB TypeII is a different application with cubic variables inside the residual c. This new bound applies in particular to the exact BOTH-TypeI piece without claiming that those long factors have smooth fixed-twist means.

At the declared pure scales A1~H=D^(3/4), X=D^(3/8), V=X^(1/6)/2, Lambda~D^(-7/8), take J0=D^(1/32). If K<=J0 the selected large-k part is exactly0. Otherwise (2.3) has the four normalized exponent budgets

 A1V/J0²:3/4;
 A1V/(DJ0):-7/32;
 A1V D^(-1/3)J0^(-4/3):7/16;
 A1V Lambda/J0:-3/32.                                  (6.2)

All are upper bounds, not actual sizes or an existence assertion. The corresponding raw numerator is multiplied by D. The leading large-k piece alone is target-sized. This does NOT improve the whole fixed-s13/12 or unsigned9/8 envelope, prove a target for the small A_Y model, or bound every dual sector.

The explicit remaining object is the ORIGINAL both-TypeI form(3.4), or its exact Bessel version, with the FINITE short set Nk<=min(K,D^(1/32)), including the unit k=O, all original mu(k), every exact s and w endpoint, all root/rho/source/S coefficients and the same coprime/optional unequal slice. For these short frequencies the same norm has a D term and gives only the inherited A1V~D^(13/16) certificate at the unit-scale band. Nothing here proves those terms large. A sufficient additional coherent estimate is a D^(-1/16+epsilon) gain for that actual short-frequency signed form after its once-only normalization, or compensation with other original pieces. Its source/orientation means cannot be centered away, and no individual component lower bound is promoted to an energy lower bound.

This surviving large-k bound and the precisely retained short-frequency form are the result of this attempt. No GRH/Artin holomorphy, positive energy/determinant, spectral bridge, fixed-conductor Gauss mean, desired zero or unprovided root cancellation is assumed. No old controls are rerun. All new notes/checks stay outside canonical and current publication scope.
