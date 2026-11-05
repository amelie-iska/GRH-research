# A uniform-cutoff envelope for the exact residue-subtracted type-I family

4 November 2026. New application of the pinned BGL squarefree/all-ideal sieve, not a new proof of that external theorem. Everything below concerns the original finite-order fixed-nu Eisenstein family and the literal nonzero element rows. No GRH, Artin holomorphy or desired positivity is assumed. This is an informal analytic proof with independent adversarial review requested, not Lean.

## Statement and exact objects

Retain K=Q(omega), O=Z[omega], fixed finite-order nu, fixed S containing the primes above6 and conductor(nu), primitive psi_u and independently primitive psi_(u,2), actual zero-extended chi_d(u)=(u/d)_6, full T(u,d)=S union supp(u) union supp(d), and beta_U(d)=sum_{ab=d,Na,Nb<=U}mu(a)mu(b). Every d,c,m ideal below is squarefree and prime to S unless otherwise specified. Take H,D,U>=1, U²<=D, W smooth supported[1,2]. Let I_u=P_u+E_u be the exact normalized original type-I decomposition in the previously accepted weighted-mellin-transfer-20261104.md, with its complete primitive masks and principal residue.

For every epsilon>0 one has

 sum_{0<Nu<=H}|E_u|²
 <<_{nu,S,epsilon} ||W||_infinity² (HD)^epsilon
        [H + D H^(1/3) + (HD)^(2/3)].                         (UC)

The constant is independent of U. No supremum over row-dependent profiles is inserted. The theorem concerns the residue-subtracted type-I piece alone; it does not control the separate type-II piece or signed covariance. The contour identity defining E is used, not any locally uniform cutoff limit on Re s>1/2.

Combining with the accepted AFM transfer gives, for fixed0<delta<1/2,

 sum |E_u|² << M4(W)²(HD)^epsilon
 min{D^(2delta) U^(2-4delta) H,
     H + D H^(1/3) + (HD)^(2/3)}.                            (MIN)

At H=D^(3/4), U=D^a,0<=a<=1/2, its excess over H is at most min{2delta+(2-4delta)a,1/2}, up to epsilon. As delta decreases to0 the new envelope improves the earlier bound for a>1/4, but still loses exponent1/2. This is a proved upper-envelope improvement, not a lower bound or the desired original signed MS3/4 estimate.

## 1. Recombine the ACTUAL finite divisor convolution before inequalities

On Re s>1, expand the full masked F_(u,d) using its defining squarefree series, not independently squared zero sentinels. The conditions (c,T(u,d))=1 include (c,d)=1. Multiplying the original symbol factors gives exactly

 J_U(s,u)=sum_d beta_U(d)nu(d)chi_d(u)(Nd)^(-s)F_(u,d)(s)
        =sum_m A_U(m)nu(m)chi_m(u)(Nm)^(-s),
 A_U(m)=sum_{d|m}beta_U(d).

If m meets u, both sides retain zero. No primitive denominator/Euler factor was discarded: this equality is obtained from its fully restored initial series and then Mellin inversion on an absolutely convergent line. The actual smoothed piece is the finite polynomial

 I_u=D^(-1/2)sum_m A_U(m)nu(m)chi_m(u)W(Nm/D).              (I)

Each prime dividing m has three choices: it belongs to a, to b, or to neither, with signs from mu(a)mu(b) and the actual norm restrictions Na,Nb<=U. Hence |A_U(m)|<=3^omega(m)<<_eta (Nm)^eta, uniformly U. For Nm<=U all truncations are inactive and A_U(m)=mu(m), but this special identity is not imposed at the length-D columns. Thus the length-D coefficient sequence in (I) has squared norm <<_eta ||W||∞²D^eta by ideal counting. It is never evaluated as an infinite series on the critical strip.

## 2. The exact all-ideal-row sieve input and derivation

Let vartheta_a denote BGL's primitive canonical sextic family. For squarefree columns m and ALL ideal rows a prime to S define

 B2^1(X,D)=sup_lambda sum_{Na<=X}|sum_{m~D}lambda_m vartheta_m(a)|² / sum|lambda_m|².

Dyadic versus cumulative cutoffs cost logarithms only. Pinned primary BGL arXiv:1112.1650v1 §3.1 definitions, Lemma3.4 and proof(3.6)-(3.9), together with Theorem1.3 as proved simultaneously for powers j in §3.2, give

 B2^1(X,D)<<_eta(XD)^eta[X+D X^(1/3)+(XD)^(2/3)].          (B2)

Here is the full reduction, so no all-conductor character counting is inferred. Write each row uniquely a=a1*a2²*a3³*a4⁴*a5⁵*a6⁶, a1..a5 squarefree and pairwise coprime, a6 arbitrary. Dyadically fix A_j<=Na_j<2A_j; put R=product A_j and M=max(A1,A2). Pivot ell=1 if A1>=A2, else ell=2. Keep every other factor fixed and absorb vartheta_m(a/a_ell^ell) into lambda_m. Its modulus<=1. Multiplicativity here is evaluation of the COLUMN character vartheta_m, so a sixth-power factor still supplies zero at primes of m. There is no false identity vartheta_(a6^6)(m)=original sentinel.

The squarefree pivot energy is bounded by

 (XD)^eta [M+D+(MD)^(2/3)]sum|lambda_m|².

For ell1 this is BGL's stated theorem. For ell2 it is the same powered-family bound proved in §3.2: the iteration is simultaneous over finite j=1..5 and uses B1^(j ell); its E_(4/3) bound plus reciprocity/duality(3.2) gives M+D+(MD)^(2/3) for every j. More explicitly, if M<=D then M^(4/3)<=(MD)^(2/3) in E_(4/3); if M>D use its transposed estimate. This is an identified external result, not assumed automatically for arbitrary primitive characters.

There are O(R/M) choices of the fixed other ideals. The block energy is at most

 (XD)^eta [R+D R/M+D^(2/3)R/M^(1/3)]sum|lambda|².

Because A_j>=1 and product A_j^j<=X, the following elementary inequalities apply:
 R<=X; (R/M)^3<=X; R³<=X² M.
For the first ratio inequality, pivot1 uses A2<=A1 and pivot2 uses A1<=A2; every j>=3 has weight at least3. For the last inequality, dividing R³/(product A_j^j)^2 by M gives
 A1/(M*A2*A3³*A4⁵*A5⁷*A6⁹)<=1.
Therefore the three block terms are at most X,D X^(1/3),(XD)^(2/3). The O(logX)^6 dyadic blocks are absorbed by choosing the internal eta small for the requested epsilon. This proves(B2), retaining the all-ideal row multiplicities and original masks.

## 3. Transfer B2 to literal elements without losing sixth-power zeros

For the outside-S ideal a=(u)_S, the accepted finite S-unit comparison gives kappa_u=eta_u*vartheta_a as primitive characters, eta_u in a finite fixed set. On coprime (a,m), BGL reciprocity gives

 chi_m(u)=eta_u(m)*C([a],[m])*vartheta_m(a).

Here the chi_m on the left is the project's ORIGINAL symbol (u/m)_6; the vartheta_m on the right is BGL's primitive column character. If (a,m)>1, the original symbol vanishes. The right side also vanishes because squarefree m has outside-S conductor EXACTLY m. This is the crucial orientation: primitive vartheta_a(m) could have restored a sixth-power prime, but primitive vartheta_m(a) retains its zero.

Split the rows into the finite eta_u and [a] classes; for each fixed class multiply column coefficients by eta_u(m)C([a],[m]), phases of modulus1. Extra row restrictions only reduce a nonnegative row sum. For each S-supported ideal b and outside-S ideal a there are at most6 generators of ab. Thus literal rows are bounded by a finite multiple of

 sum_{b S-supported,Nb<=H} B2^1(H/Nb,D) sum|lambda|².

Each S-smooth sum converges at its positive power1,1/3 or2/3. Insert(I)'s coefficient norm to obtain the right side of(UC) for sum|I_u|². No quotient by units, no loss of S-powers and no arbitrary-conductor replacement is used.

## 4. Principal rows and the residue-subtracted remainder

On a row where primitive psi_u is principal, nu is unramified outside S. Tame sextic Kummer conductor therefore forces every outside-S valuation vp(u) to be divisible by6. Consequently the number of such actual rows with Nu<=H is at most

 C_K H^(1/6) product_{p in S}(1-Np^(-1/6))^(-1).

This is an upper bound, not an assertion all these rows are principal. For finite-order nu the exact residue is

 P_u=1_(psi_u=1)*sqrtD*W_hat(1)
      sum_d beta_U(d)nu(d)chi_d(u)/(Nd)*rho_T(u,d),
 rho_T=(res_(s=1)zeta_K(s))/zeta_K(2)*product_{p in T}(1+Np^-1)^(-1).

No positivity is imposed on P. Since |rho_T|<=C_K, |W_hat(1)|<=||W||∞ and sum_d|beta_U(d)|/Nd <= (sum_(Na<=U)1/Na)² << log²(2U),

 sum |P_u|² << D H^(1/6)||W||∞² log⁴(2U).

Under U²<=D its log factor is absorbed by(HD)^epsilon and H^(1/6)<=H^(1/3). Finally |E|²=|I-P|²<=2|I|²+2|P|² proves(UC). This does not separately establish the sharper principal-residue target of the full signed program.

## Exact failure frontier and next claim

A naive fixed-squarefull-row decomposition loses D sqrtH. The all-ideal pivot reduces this to D H^(1/3). That term is still not the required all-epsilon energy at H=D^(3/4). Elementary sieve block bookkeeping alone cannot remove it: the monomial constraint is saturated by A1=A2=X^(1/3), all others1. This shows sharpness only of this particular block bound, not a lower bound for the actual arithmetic energy. Likewise |A_U|<=3^omega does not exploit its signed cancellations.

Next load-bearing claim: use the actual signed A_U(m) and its mu*mu truncations inside an improved original-family bilinear/mollified second moment, or obtain signed type-II minus type-I covariance; do not repeat the now-finished numerator AFM or this worst-case coefficient sieve as a complete solution. The inverse-L cutoff identity on Re>1 remains distinct from any locally uniform continuation into Re>1/2. Full arithmetic determinant positivity, original signed low-gcd uniformity and GRH remain open.

## Source pin and verification scope

Primary: Blomer, Goldmakher, Louvel, arXiv:1112.1650v1, https://arxiv.org/pdf/1112.1650v1, Lemma2.1; §3 definitions; Lemma3.4 and(3.6)-(3.9); simultaneous powered bounds in§3.2; AppendixII. The already cached source is preserved unchanged. A separately fetched Goldmakher-Louvel1112.1642v2 confirms quadratic-family background but is NOT additionally required by our pivot1/2 argument; its files remain preserved under primary/.

Finite exact checks cover the actual beta_U coefficient recombination with Eisenstein split-prime symbols, original zero sentinels, all dyadic monomial inequalities and cutoff-exponent comparisons. They do not prove the external analytic large sieve or provide Lean formalization. No production/source/model/env/auth/publication file was changed.
