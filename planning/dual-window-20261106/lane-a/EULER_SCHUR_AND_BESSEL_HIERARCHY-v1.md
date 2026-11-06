# Actual deleted Euler multipliers and a Bessel--Euler hierarchy

DRAFT v1 for independent review. New research only, outside the frozen physical-sieve release. No new target power is claimed. The delivered global 9/8 and original unweighted two-pivot signed 13/12 bounds remain current.

## 1. Actual family and convention

Use the current postrelease handoff (SHA256 2e193a69decd3b70921728dbcb5e3aca91fc7588125353d8382ef81e804b6076), accepted dual-unit lemma v3 (abeee9010e2b500565ce857f930650c277999fecc2d6cc64b59e9b0ab1973744), and required v8 scope addendum (5f576c22742d894536c7e8a843d29e3117be9c1e3534d5a5415aa8e130b80b11). Their primitive Poisson identity and Bessel normalization are inputs, not new audits.

Work over O=Z[omega], fixed original S containing primes above 2,3 and the original S-supported ray data. The ACTUAL row family here has v3=v4=v5=v6=O. The fixed u0 is a literal unit/S-supported factor with no good-prime support. Additional frozen good row factors would require their full primal finite deletion/rescaling, not merely a larger k mask; that extension is not made here.

The column set I is any finite subset of the original complete good squarefree annulus D<=Nm<=2D, D>1; applying results to a subset is a matrix restriction, not a change in the asserted original family. Full I is used in the original form. Each ideal is a distinct coordinate even at equal norm. chi_m(k) is the accepted actual source family with its literal zero for (m,k)>1 on good k. It is multiplicative in k, including these zeros. No arbitrary primitive-conductor family or radical-norm comparison is introduced.

Fix one actual v2, ell|v2, e|P_S, and one finite ray character rho after the full exact ray expansion. Its Fourier coefficient h_rho is the coefficient BEFORE t=k^2 ell is substituted; rho(t) remains in the primitive eta. For coprime original columns m,n put eta_mn=prim(rho chi_m conjugate(chi_n)). On good k coprime to mn,

    eta_mn(k)^2=rho(k)^2 chi_m(k)^2 conjugate(chi_n(k)^2).

The full deleted union is T_mn=S union supp(mn v2 ell), with ell redundant in v2. It is not just the conductor of eta_mn^2. Hence the actual deleted Euler factor has the raw extension

    E_mn(w)=sum_(k good,(k,v2)=1)
       mu(k)rho(k)^2 (Nk)^(-w) chi_m(k)^2 conjugate(chi_n(k)^2), Re w>1. (1)

This equals E_Tmn(w,eta_mn^2) on the original coprime support. Away from that support, (1) is only a convenient full-union matrix extension. In particular it is not a claim that a primitive conductor equals mn on the diagonal or at overlapping columns. Every original coprime zero-pattern will stay in the matrix being multiplied.

The actual column coefficient remains

    c_m=A_U(m)nu(m)(u0/m)_6 W(Nm/D),
    A_U(m)=sum_(ab|m,(a,b)=1,Na,Nb<=U) mu(a)mu(b),

with one fixed possibly complex W. No factorization, new radial profile, centering or changed raw sentinel is used.

## 2. Exact Schur multiplier, uniform inverse and finite cutoffs

Let D_k=diag(chi_m(k)^2) on ell2(I), so ||D_k||<=1 and D_k D_l=D_kl EXACTLY, including common-prime zeros. Define, on matrices indexed by the actual I,

    M_w(A)=sum_(k good,(k,v2)=1)
       mu(k)rho(k)^2/(Nk)^w * D_k A D_k^*.                         (2)

This is exactly E(w) entrywise-multiplied by A. Primitive roots, conductor factors, the coprime mask, column collision masks and finite-capacity kernels may all be inside A; no factorization of any of them is assumed. Entrywise masks commute with (2), so every fixed zero-pattern is preserved. The same statement holds for a rectangular block I_C1 by I_C2, using D_k,C1 on the left and D_k,C2^* on the right.

Write Z_w for the SAME series with mu(k) replaced by 1, summing ALL integral good k coprime to v2, including every prime power. Both series converge absolutely in operator norm when Re w>1. Their composition is the identity: multiplicativity of D and rho reduces each ideal r coefficient to

    rho(r)^2/(Nr)^w * sum_(k|r) mu(k)=1_(r=O).

Absolute convergence justifies this regrouping. Restricting the inverse to squarefree k would be incorrect. Thus Z_w=M_w^(-1), with no use of inverse-L continuation, a zero-free hypothesis or an assumed conductor-family theorem.

At w=2 the bounds are completely uniform. The accepted elementary count A_K(X)<=2X gives sum_(Nk>K)(Nk)^(-2)<=4/K. Every nonunit good ideal has norm at least 7; therefore

    sum_(k good,(k,v2)=1) 1/(Nk)^2 <=1+4/7=11/7.

(The tail starts at norm7; obtain the weak-endpoint estimate by K increasing to 7 from below.) Consequently, for every matrix A on these ACTUAL coordinates,

    ||M_2(A)|| <=(11/7)||A||,
    ||Z_2(A)|| <=(11/7)||A||,
    (7/11)||A|| <=||M_2(A)|| <=(11/7)||A||.                     (3)

The bounds hold for operator norm, all Schatten p norms with 1<=p<=infinity, and every matrix amplification: each map A->D_k A D_k^* is contractive in each of these norms. They also hold on any fixed zero-pattern subspace, because M and Z preserve that pattern. Equal-norm fibres have not been merged.

For the exact finite pre-S-removal K=Kcut>=1 define M_w,K by Nk<=K in (2). At w=2,

    ||M_2,K-Id|| <=4/7,
    ||M_2,K|| <=11/7,
    ||M_2,K^(-1)|| <=7/3,
    (3/7)||A|| <=||M_2,K(A)|| <=(11/7)||A||,                    (4)
    ||(M_2-M_2,K)(A)|| <=(4/K)||A||.

The finite inverse bound uses a norm-convergent Neumann series; it is not obtained by truncating the infinite inverse. As always, empty b<a or Nell>b terms in the actual row inversion are zero and have no attached main term.

## 3. Why positivity is unavailable even for the natural Euler extension

Take rho=1, and let m,n be an ACTUAL distinct coprime nonunit squarefree annular pair with (mn,v2)=1. This is a statement when such a pair occurs, not a fabricated pair of character labels. For p notin S union supp(v2), put t_p=(Np)^(-2) and d_m=chi_m(p)^2, d_n=chi_n(p)^2, which have modulus 0 or1. The local Euler factors satisfy the exact identity

    |1-t_p d_m conjugate(d_n)|^2
      =(1-t_p|d_m|^2)(1-t_p|d_n|^2)+t_p|d_m-d_n|^2.           (5)

All local diagonal factors are positive. Taking convergent products yields

    |E_mn(2)|^2 >= E_mm(2) E_nn(2),

strictly: a prime dividing m but not n or v2 has d_m=0 and |d_n|=1. Thus the natural two-by-two full-union E matrix has negative determinant, although both diagonal entries are positive. M_2 is not a positive Schur multiplier on this extension; applying it to the all-ones positive matrix already gives an indefinite matrix.

These diagonal extension entries are not original h=1 diagonal terms, which are absent. This observation does not produce a negative original energy, show that every alternative completion fails, or establish any lower bound for actual A_U coefficients. It specifically prevents interpreting the displayed natural Euler factor as a positive covariance weight or dropping signed terms by that interpretation.

## 4. Consequence for the actual coherent mean

For the original convention Q_A(c)=sum c_m conjugate(c_n) A_mn, (2) says EXACTLY

    Q_M2(A)(c)=sum_(k good,(k,v2)=1)
          mu(k)rho(k)^2/(Nk)^2 * Q_A(D_k c).                  (6)

This retains the mean; it does not replace it by a variance or an absolute mass. It also explains the remaining issue. The actual phase-modulated vectors D_k c are not one new fixed nu/S family with a common bounded conductor. An estimate for the single original prescribed vector cannot be applied uniformly to them without a new hypothesis. Using an arbitrary-coefficient norm instead gives only (3) times that norm.

In particular no uniform replacement ||M_2(A_D)||<=D^(-delta)||A_D||, delta>0, can hold for nonzero matrices on these actual spaces: (3) rules it out. The same conclusion holds for the constant-profile finite-k map by (4). This is a limitation of a norm-only Euler-multiplier mechanism, not a proof that 13/12 is optimal or that the actual signed quadratic form cannot improve. A new weighted norm estimate would transfer to the unweighted matrix norm up to a constant. Special cancellation of the fixed A_U vector, roots and remaining dual frequencies is still possible and unestimated here.

## 5. All finite dual modes: exact Bessel--Euler hierarchy

The fixed E_2 multiplier is only the zero-Fourier-profile main. To retain nonunit modes, work on one finite actual class-pair/rho block. The accepted primitive conductor is

    F_mn=Nf_S * Nm*Nn,

where the fixed finite S factor depends on that displayed block. Keep the ACTUAL primitive root and every remaining factor; do not extend a same-class beta factorization to other blocks. Fix a dual y=h z with h supported on S and z good, and define

    t=A1*Nh*Nz/(Nell*Ne*Nf_S*D^2),
    R_j=diag((D/Nm)^j),  ||R_j||<=1,
    M_j=integral y^j G(y)dy,  C=3/(4pi^2).                    (7)

Use different left/right R_j on a rectangular class block. Let A be the actual k-independent matrix factor, including, for example, 1_(m,n)=1, primitive epsilon_mn/sqrt(F_mn), eta_mn(ell)eta_mn(e), conjugate(eta_mn(hz)), the original raw v2 factors and any other fixed masks. Outer mu(ell)mu(e)h_rho and A1/(Nell Ne) stay outside once; c_m remains the original column coefficient. Define P_t,K(A) entrywise by multiplying its m,n entry by

    sum_(Nk<=K,(k,Sv2)=1) mu(k)rho(k)^2/(Nk)^2
      *chi_m(k)^2 conjugate(chi_n(k)^2)
      *dotG(t D^2/(Nm*Nn*(Nk)^2)).                           (8)

This is the exact finite row-divisor kernel for that dual mode, not its absolute majorant. For the actual G use its exact integer-node/capacity construction and K=sqrt(b/Nell), BEFORE e removal. Its support is in [1/2,B0], B0=5/2, and 0<=G<=1 with derivatives possibly growing as A1^j.

The Bessel series, integrated against G, gives the exact operator identity

    P_t,K(A)=C^(-1/2) sum_(j>=0) (-t/C)^j M_j/(j!)^2
                   * R_j M_(2+2j),K(A) R_j.                 (9)

For a fixed t>=0 the series converges absolutely in operator norm. Indeed |M_j|<=B0^j integral|G|, ||R_j||<=1, and the k sums are absolutely bounded by zeta_K(2); the factorial squares dominate. The power of Nk is 2+2j because the Poisson prefactor supplies Nk^(-2) and each Bessel power supplies Nk^(-2j). This is an exact hierarchy of deleted Euler multipliers, not E_2 acting on the full profile. All roots, finite classes, raw zeros and coherent ideal fibres remain in A. At t=0 the identity reduces to g0 M_2,K(A), g0=C^(-1/2)M_0.

Define the entire positive function

    V(x)=sum_(r>=0) x^r/((r+1)!)^2,  V(0)=1,  V(x)<=exp(x), x>=0.

Since |M_j|<=B0^(j-1) M1_abs for j>=1, with M1_abs=integral y|G(y)|, and sum (Nk)^(-2-2j)<=zeta_K(4)<=8/3 for j>=1, (9) gives the genuinely dimension-free bound

    ||P_t,K(A)-g0 M_2,K(A)||
       <=(8/3) C^(-3/2) t M1_abs V(B0 t/C) ||A||.             (10)

Completing only the j=0 multiplier to the infinite Euler product gives

    ||P_t,K(A)-g0 M_2(A)||
       <=[4|g0|/K +(8/3) C^(-3/2)t M1_abs V(B0 t/C)]||A||.   (11)

No entry count, column dimension or unproved uniform derivative seminorm is hidden here. The signed/complex M0 remains in g0; if M0=0 it is zero. This improves the *form* of a low-frequency error certificate over an entrywise D^2 triangle: it is an operator error relative to the actual retained matrix A. It does not estimate ||A||, sum the other outer parameters, or improve a target power.

For each j, completion of M_(2+2j),K to its infinite Euler multiplier has the explicit operator tail 2w/(w-1) K^(1-w), w=2+2j. All such tails must be retained if that additional completion is made. In particular the exact original finite cutoff has not disappeared from (9)--(11).

## 6. The precise whole-kernel failed step

Every finite good-dual window and finite set of S-supported h can be reorganized by (9) before absolute Cauchy. This is new information on all its nonunit modes. It does NOT justify swapping the j-series with the full unweighted dual ideal sum. After absolute values the positive V(B0 t/C) majorant grows rather than decays with Nz; even a single coefficient j has polynomial Nz^j. No summable infinite dual tail follows from this hierarchy. Fixed-D rapid decay of the ORIGINAL transform still holds, but replacing it by the absolute power-series majorant discards that cancellation. A separate derivative/Bessel tail analysis may certify a cutoff with its actual growing constants; none is silently supplied by (9).

There is a parallel Mellin obstruction to a blind absolute-Fubini argument. Separating dotG makes the k exponent 2-2s. Infinite k-Euler absolute convergence is available for Re(s)<1/2, whereas the complete good-dual absolute Dirichlet sum uses Re(s)>1. These elementary absolute regions do not overlap. The original finite k sum and ordered finite-block Poisson identities remain valid; there is no claim that analytic continuation or a more refined joint oscillatory estimate is impossible.

Thus the precise missing estimate is a signed bound for the retained primitive-root/eta-deletion dependent outer matrix and dual partial sums, together with an honest complementary tail. Neither a positive interpretation of E_2, a generic conductor substitution, nor its bounded Schur norm proves that bound. All nonunit and S-supported dual modes, the endpoints, full original capacity and prescribed A_U/nu/common W stay in the problem.

## 7. Surviving result and stopping point

New proved reductions for review: the actual E_2 factor is a uniformly bounded and uniformly invertible Schur multiplier; its natural full-union extension is not positive; every finite dual mode admits the exact Bessel--Euler hierarchy and the uniform operator error (10)--(11). These give concrete controls and a sharp limitation of the proposed norm-only mechanism. They do not yield any saving over the existing scoped 13/12 bound.

There is no actual-energy lower bound, fixed-W counterexample, new sieve theorem, zero-free input, Lean/GRH result, or extension to extra frozen good row factors. No old arithmetic table, build, compiler, auth, publication, index or environment was touched. All work and receipts are in the fresh lane-a directories only. Independent review is pending.
