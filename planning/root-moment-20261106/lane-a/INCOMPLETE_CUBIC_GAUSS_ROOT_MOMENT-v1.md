# Actual root moments as incomplete cubic Gauss averages

Research-only draft v1,6 November2026. Independent review required. This attempts the ACTUAL finitew<=64 root/column/k mean, not another compensation/Schur/norm proof. The surviving reduction exposes a concrete cubic-Gauss average with original short-divisor coefficients. No signed target estimate is proved. Every finished theorem cited here is an INPUT, not new controls or a newly proved sieve.

## 1. Original mean and exact local conventions

Use principal-mean HANDOFF-v1 SHA2b923adf.../aggregate-v2 bbe4a216, accepted top mean5624e5bb, its source4315f8d2 and all current cbk primitive conventions. Columns are the COMPLETE good SF ideal annulus D<=Nm<=2D, original m,n coprime, with OPTIONAL original Nm!=Nn projection only. Original

 c_m=A_U(m)nu(m)R_m(u0)W(Nm/D), 1<=U<=sqrt(D)

stays. W is ONE fixed possibly complex common profile supported[1,2], B=||W||infinity; nu,S/ray/source data fixed. Rows are only original unweighted two-pivot, other fourgoodfactors unit, u0 fixed unit/S-supported withoutgood support, all literal/SF/coprime/capacity masks retained. No new row weights, good frozen factors, varying-u0 sum or selected columns.

All source classes A,B and rho^6=1 branches, primitive eta with total type0, actual f_S q conductor,F=F_S NmNn, roots, primitiveS zeros and finite e|P_S/l|v2/k remain. k is good SF, (k,v2)=1, Nk<=sqrt(b(v2)/Nl), BEFORE e deletion. The top good-sixthpart band has V=X^(1/6)/2 and y=h r s^6 with V<Ns<=2V. Accepted exact inversion gives ONLYa1 and w=hr of norm<=64. h includes all S-supported factors, r good; no unit-only replacement is made. In the exact mean the integral for w is

 integral_V^(X^(1/6)(Nw)^(-1/6))
                   dotG(L_e Nw t^6/F)dt,                (1)

empty if Nw>=64, with L_e=A1/[(Nk)^2NlNe]. The capacityG, root and each endpoint remain. This note does not redo root's concurrent j0/Q2 reduction; it targets its root-weighted column average.

Put delta=1+2omega. For each good ideal m use its multiplicative primary generator alpha_m=1mod3 and literal finite character

 chi_6,m(x)=(x/m)_6, chi_3,m=chi_6,m^2,
 tau_m(chi)=sum_(x modalpha_m)chi(x)
                     exp(2pi i Tr(x/(delta alpha_m))).

These are AUXILIARY finite character/Gauss objects at their exact good modulus. They are not individual primitive xi_m atS and restore no forbidden row value. For good SF m, chi_3,m is primitive at m and chi_3,m(-1)=1. Define

 G_m=tau_m(chi_3,m)/sqrt(Nm),
 g_m(z)=tau_m(chi_3,m;z)/sqrt(Nm).

Primitive finite Fourier gives, for EVERY integral z,

 g_m(z)=bar(chi_3,m(z))G_m, |G_m|=1,
 bar(g_m(z))=chi_3,m(z)bar(G_m).                          (2)

At a collision(m,z)>1 both sides are0. We never replace that zero by a unit. The unit-conductor convention is1.

## 2. Exact good-q root calculation; S is kept separately

Let q=mn, Q=NmNn, gamma_q=alpha_m alpha_n and

 theta_q=chi_6,m bar(chi_6,n).

Its powers theta_q,theta_q^2,theta_q^3 are all primitive at GOODq: every local exponent is respectively +/-1,+/-2,3mod6, hence nonprincipal and conductor exponent1. Let gamma_S generate the ACTUAL f_S and theta_S be the ACTUAL primitive finite S-component of eta. Since eta has total angular/radial type0, its finite character at f_S q is theta_S theta_q, unit-trivial as a whole.

The identification of its GOOD local part with theta_q follows directly from the accepted source reciprocity transport: on primary ideals eta=the fixed S/ray phase times R_m bar(R_n). Choosing a principal generator1mod the complete fixed S presentation and arbitrary modq identifies the local character by CRT. No primitive S-component is guessed from a generic conductor. Its actual conductor and possible drop stay.

For the whole type0 eta, root normalization and CRT give

 epsilon(eta)=S_(m,n,rho) tau_q(theta_q)/sqrt(Q),
 S_(m,n,rho)=theta_S(gamma_q)theta_q(gamma_S)
                         tau_(gamma_S)(theta_S)/sqrt(F_S).    (3)

The finite S Gauss sum is at its OWN primitive conductor, including f_S=O convention. Thus |S|=1. This is NOT epsilon(sigma) with angular/radial factors silently erased: it is the finite local factor in the total type0 character. Choosing another generator changes the finite factors compatibly and leaves(3) unchanged. Auxiliary theta_q(gamma_S) is legitimate because(q,f_S)=1; it is not a raw original row symbol atS. Primitive eta(e) or eta(w) may still be0 and are retained outside(3).

The elementary Gauss--Jacobi identity at exact GOODq is

 tau_q(theta_q)tau_q(theta_q^2)
                       =J_q(theta_q,theta_q^2)tau_q(theta_q^3).

No division by an induced S Gauss sum occurs. Accepted correctly oriented Jacobi input gives

 J_q=j(m)bar(j(n)),
 j(m)/sqrt(Nm)=mu(m)vartheta(m),
 vartheta=Psi/sqrt(N), cond(Psi)=(2delta), Ncond=12.       (4)

Psi has infinity type(1,0), not finite order; formula(4) is ONLY on original SF columns. All conductor12/Jacobi proofs are already accepted input.

Cubic reciprocity with the primary1mod3 convention gives

 chi_3,m(alpha_n)=chi_3,n(alpha_m).

Therefore the two cubic CRT cross factors for theta_q^2 cancel EXACTLY, so

 tau_q(theta_q^2)/sqrt(Q)=G_m bar(G_n).                   (5)

The quadratic finite Gauss phase is the accepted period-four input

 Gamma(gamma_q)=tau_q(theta_q^3)/sqrt(Q)
 =[1+i^(-b)+i^a+i^(b-a)]/2, gamma_q=a+bomega.             (6)

It is a unit phase. It is not assumed to factor multiplicatively; it depends on gamma_q mod4 and is kept. Applying(4)--(6) yields the exact ACTUAL root

 epsilon(eta)
 =S_(m,n,rho) Gamma(alpha_m alpha_n)
      mu(m)mu(n)vartheta(m)bar(vartheta(n))
                           bar(G_m)G_n.                 (7)

No extra theta_q^3(-1) appears in this two-Gauss identity. The original coefficient c_m is unchanged; the displayed mu(m) factors COME FROM THE ROOT GAUGE and are not a new mu inserted into the original kernel. Formula(7) is an application of accepted Gauss/Jacobi facts, not a new phase theorem.

## 3. The finite k variable is a genuine cubic-Gauss frequency

For goodk, total type0 gives

 eta(k^2)=theta_S(alpha_k)^2
                   chi_3,m(alpha_k)bar(chi_3,n(alpha_k)),

including q raw zeros. Multiplying(7) with the ORIGINAL factors
R_m(v2^2)bar(R_n(v2^2)) therefore changes

 bar(G_m)G_n chi_3,m(alpha_k alpha_v2)
                     bar(chi_3,n(alpha_k alpha_v2))
       =bar(g_m(alpha_k alpha_v2))g_n(alpha_k alpha_v2).  (8)

The scalar theta_S(alpha_k)^2 is retained; k is still SF with its ORIGINAL cutoff and(k,v2)=1. Equation(8) adds no relation k|w, k^2|y or(k,w)=1. A repeated primal prime in k,v2 is still excluded by the ORIGINAL mask, not by a supposed Gauss-frequency zero.

The remaining eta(l e)bar(eta(w)) are ACTUAL primitive values. They can be0 atS orq and are not divided out. If represented using chosen integral generators gamma_le,gamma_w, the combined finite S and q factors are generator-independent because total eta is unit-trivial. No primary generator for an S-supported w is asserted.

Equations(7)--(8) turn the top mean into a concrete finite-k INCOMPLETE CUBIC-GAUSS modulus average: all original c_m, densityg(m)g(n), the fixed Hecke gauge vartheta, source/rho and finite S factors, w<64 and the EXACT Bessel integral(1) multiply

      bar(g_m(alpha_k alpha_v2))g_n(alpha_k alpha_v2)

on the original coprime column support. If Gamma is to be separated, partition the EXISTING columns by alpha_m mod4 and alpha_n mod4 and keep all finitely many blocks; this neither changesS nor adds a new column restriction to the total expression. It makes Gamma constant per block, while theta_S(gamma_q) factors into its two genuine column factors. They are DISTINCT m/n gauges (the S phase on n is not silently conjugated). Root transport to different source classes is not a PSD assertion.

This is an exact arithmetic reorganization before any positive-d/conductor triangle. To bound it uniformly one needs a signed modulus-average estimate for THESE actual coefficients and finite frequencies, rather than the pointwise fact |g_m(z)|<=1 or a generic primitive-conductor family statement.

## 4. Attempted short-divisor/metaplectic substitution and its exact failure

It is tempting to insert a smooth-coefficient cubic-Gauss first-moment bound after(7), treating A_U as another smooth cutoff. This changes the hypothesis. No such external theorem is invoked or asserted in this note.

For SFm the EXACT short-divisor identity is

 mu(m)A_U(m)=sum_(a b c=m,Na,Nb<=U)mu(c),                 (9)

with a,b,c pairwise coprime and SF, all good; their product is in the original annulus. This is the accepted ternary assignment identity, not new multiplicativity of A_U. The density g, fixed Hecke gauge vartheta and fixed multiplicative twists split on these coprime factors, but the original common W stays W(NaNbNc/D).

Cubic CRT and primary reciprocity imply

 bar(G_(abc))
 =bar(G_a)bar(G_b)bar(G_c)
                chi_3,a(alpha_b)chi_3,a(alpha_c)
                                   chi_3,b(alpha_c).     (10)

Thus even one expanded column contains an ACTUAL inner family of the form

 sum_(c SFgood, Nc~D/(NaNb), (c,a b k v2)=1)
   mu(c) vartheta(c)nu(c) g(c) bar(G_c)
   chi_3,(ab k v2)(alpha_c) *chi_fixed,l,e,w,u0(c)
                          W(NaNbNc/D)/sqrt(Nc),          (11)

up to fixed finite class selectors/column factors and the external1/sqrt(NaNb). The character labelled chi_fixed includes the exact original bounded-w/S/l/e/u0 symbols or gauges; when v2/l/k vary, those twists/masks are NOT declared fixed-conductor. The good product abkv2 in the cubic factor is SF only on the nonzero original masks; collisions must be killed first. Individual c and ab may not be treated as independent arbitrary labels. Source/ray constraints remain. Formula(11) is a statement of the required family, not a theorem about its size.

The remaining mu(c), the growing physical twist abkv2, the full deleted union and the shifting short length are absent from a naive smooth-column first-moment input. A theorem for smooth coefficients with fixed twist does NOT establish(11). This is the exact unsupported step, not a proof that an appropriate uniform theorem is impossible.

Even a deliberately OPTIMISTIC hypothetical bound, for every actual(a,b) and all its phases/masks,

 |inner unnormalized c-sum with the SAME weights but no1/sqrt(Nc)|
                            << L^(5/6+epsilon), L=D/(NaNb),

would, after partial summation in1/sqrt(Nc) and absolute(a,b), give only

 D^(1/3+epsilon)sum_(Na,Nb<=U)(NaNb)^(-5/6)
                       <<D^(1/3+epsilon)U^(1/3).         (12)

The elementary ideal count proves sum_(Na<=U)(Na)^(-5/6)<<U^(1/6); restricting to original product/masks only decreases this positive majorant. For U~sqrt(D), (12) is D^(1/2+epsilon), restoring the trivial normalized-column exponent. Moreover it is only an auxiliary COLUMN estimate, not an estimate of the original coprime bilinear moment; it discards the short-divisor signs and has not estimated its virtual d terms.

The numerical exponent5/6 above is a HYPOTHETICAL illustrative input, not a cited available metaplectic theorem. No pole at5/6 or uniform cubic-Gauss bound is asserted without primary proof/hypothesis matching. Root independently derives the more general short-divisor-triangle diagnostic; the(12) calculation is included only to state why the naive smooth-coefficient insertion does not supply a target estimate at the actual high cutoff.

## 5. What completion/orthogonality would really require

Expanding the auxiliary finite sums in(8) produces, at fixed coprimem,n,

 (NmNn)^(-1/2)
 sum_(x modalpha_m,y modalpha_n)
   bar(chi_3,m(x))chi_3,n(y)
   e( alpha_k alpha_v2
             [y/alpha_n-x/alpha_m]),                    (13)

with the inverse-different pairing in e. The original finite weighted k sum is consequently an INCOMPLETE primary-lattice additive Möbius sum inside(13), with a varying frequency of denominator alpha_m alpha_n. It is not a complete additive residue sum, and its1/(Nk)^2 weights and natural cutoff cannot be replaced by a uniform residue average. The primitive S scalar theta_S(alpha_k)^2 stays.

Orthogonality of additive characters on a FULL q residue ring cannot be applied to that actual weighted k set. The k range is bounded in norm by the ORIGINAL sqrt(b/Nl), while Nq~D^2; w<=64 does not complete this ring. Summing the finite w coefficients first also does not give a full residue system modulo growing q. This diagnoses the proposed free-local-Gauss-completion step, not an impossibility theorem or a new rank/Schur claim.

With |g_m(z)|<=1 and the accepted original comparisons the surviving top-sector budget is still O(B^2 eps R X^(1/6)); this is the OLD inherited fixed-s norm/direct-count bound, not the new result of this attempt. No local recombination here gives the D^(-1/16) signed factor needed by the pure critical top mean. A sufficient missing input is a joint bound for the EXACT cubic-Gauss modulus-average described by(1),(7)--(8), with(9)--(11)'s actual short-divisor coefficients and all original masks, or a coupled estimate with the other original sectors. It is not necessary that each individual block be small.

The actual mean may cancel through roots/columns/k/w or other source pieces; no lower bound or nonvanishing is asserted. Whole two-pivot13/12/global9/8, principal/short assembly, determinant/zero-location/Lean/GRH remain unchanged. The finite reorganization is a new application/criterion only and does not count as a new signed power saving. No old controls, phase tables, synthetic data, lattice estimates, build/browser/publication/dependency/auth/index/canonical operation is run.
