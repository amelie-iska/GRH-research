# The actual signed common-divisor series: nine zeta factors and a finite numerator

Status: new analytic reduction and explicit auxiliary estimates, submitted for independent review. NO improvement of the original signed moment is asserted. The source hashes/protected states are in source-pins-v1.json. No publication, old control, compiler or dependency work is part of this attempt.

## 1. Start with the actual mean, retaining overlapping residual columns

Fix the original finite-order nu, fixed S above2,3 and its defining conductor, and ONE common possibly complex W in C_c^infinity supported in[1,2]. Let D>1,1<=U<=sqrt(D). Let B be the actual finite literal/ray/squarefree/capacity row block u=u0*v1*v2^2, with v1,v2 squarefree/coprime and the other good factors the unit ideal. No row is enlarged here. Write

    A_U(m)=sum_(r1*r2*r0=m;Nr1,Nr2<=U) mu(r1)mu(r2)       (m squarefree).

The accepted exact gcd identity gives the unnormalized actual mean

    Sbold := D*S_1^AA = sum_(d sf,good) mu(d) G_d^AA,
    G_d^AA = sum_(u in B,(d,u)=1) |T_d^A(u)|^2,
    T_d^A(u)=sum_(a sf,(a,dS)=1) A_U(da)nu(a)chi_a(u)W(Nd Na/D).       (1)

Expand (1) but do NOT take an absolute d sum. For fixed residual a,b and rowu the inner scalar is

    sum_(d sf,(d,Sabu)=1) mu(d) A_U(da)A_U(db)
                         W(Nd Na/D)overline(W(Nd Nb/D)).               (2)

Its outer coefficient is nu(a)overline(nu(b))*chi_a(u)overline(chi_b(u)). The residual ideals a,b MAY OVERLAP. They need only be squarefree and good. Their common primes stay in the full deleted set even if a quotient row character loses its conductor there. If the outer raw character is zero, the term stays zero. The d character disappears only through the exact identity |chi_d(u)|^2=1_(d,u)=1 and |nu(d)|=1 on good d. No primitive value restores any zero.

For fixed a,b,u put T=S union supp(abu) and define, initially Re(s)>1,

    D_U;a,b,u(s)=sum_(d sf,(d,T)=1) mu(d)A_U(da)A_U(db)(Nd)^(-s).       (3)

The divisor-assignment majorant is 3^(omega(a)+omega(b))*9^omega(d), so (3) converges absolutely there, uniformly in U. The fixed-profile target remains |Sbold| <<_(nu,S,W,epsilon) D H(HD)^epsilon. Nothing below proves it.

## 2. A new signed local factor, before cutoff inversion

Introduce four independent positive Perron lines v1,v2,w1,w2. For q=Np set

    alpha_i=q^(-v_i), beta_j=q^(-w_j), z=q^(-s),
    P_p(v)=1-alpha_1-alpha_2,  Q_p(w)=1-beta_1-beta_2.

For a fixed residual ideal, P_a=product_(p|a)P_p and Q_b=product_(p|b)Q_p. A common d-prime has NINE joint positions: absent from both short divisors, or in either of the two short divisors, independently in each column. Its mu(d) sign is essential. Therefore the actual joint generating function is

    F_a,b,T(s;v,w)=P_a(v)Q_b(w) E_T(s;v,w),
    E_T=product_(p notin T){1-z P_p(v)Q_p(w)}.                          (4)

If p divides BOTH a and b its finite contribution is P_p*Q_p, not one factor and not a deleted contribution. The d-primes avoid it to keep da and db squarefree. The factor in(4) is NOT the earlier global coprime-pair factor1+xP+yQ; it is the signed common-divisor factor after fixing the two residual columns.

Define incomplete zeta by zeta_K^T(t)=product_(p notin T)(1-(Np)^(-t))^-1. First-order Euler factorization of(4) gives, in its initial absolute domain,

    E_T = Z_T(s;v,w) H_T(s;v,w),
    Z_T = [product_i zeta_K^T(s+v_i) zeta_K^T(s+w_i)]
           /[zeta_K^T(s)*product_(i,j)zeta_K^T(s+v_i+w_j)].            (5)

There are four numerator and five denominator factors. Explicitly

    H_p = [(1-z P_p Q_p) product_i(1-z alpha_i) product_j(1-z beta_j)]
            /[(1-z) product_(i,j)(1-z alpha_i beta_j)].                (6)

The linear coefficient in the numerator and denominator is the SAME,

    -1-alpha_1 beta_1-alpha_1 beta_2-alpha_2 beta_1-alpha_2 beta_2.

This fixes the signs in (5). At all auxiliaries zero, P=Q=-1, E_T=1/zeta_K^T(s), Z_T=1/zeta_K^T(s), and H_T=1. At v2=w2=0 it is exactly1/zeta_K^T(s+v1+w1), again with H_T=1. These are generating-function slice checks, not a replacement of the finite cutoff by an untruncated slice.

There is a uniform quantitative correction bound. For sigma>=1/2+eta and all four auxiliary real parts>=0,

    |H_p-1| <= C_eta (Np)^(-1-2eta),
    C_eta=172/[1-7^(-1/2-eta)]^5.                                    (7)

To prove it, write the numerator and denominator of(6) as degree-five polynomials R(z),D(z). Constants and linear coefficients cancel. With |P Q|<=9 and |alpha|,|beta|<=1, the total coefficient majorants from degrees2..5 are146 for R and26 for D. Hence |R-D|<=172|z|^2 when |z|<=1. The five denominator factors have modulus at least1-|z|. Good prime norms are>=7. This proves(7). Ideal counting makes the product normally convergent at fixed positive margins, uniformly in deleted primes and vertical phases, with

    |H_T| <= exp(C_eta*sum_p (Np)^(-1-2eta)).                          (8)

Finite local H factors can vanish; no nonvanishing/inverse-H bound is claimed. Normal convergence of H does NOT make the nine-zeta ratio holomorphic in this region. Zeta zeros, poles and any crossed residues remain. Identities are proved in the absolute domain and continued only where the named functions have the required continuation.

## 3. Finite heights first: an exact Perron-limit insertion with an error bound

Let V=floor(U)+1/2, so every actual integer short norm is separated from V. For four positive real lines c_j and finite heights T_j, define I_T(s) by integrating F_a,b,T times

    product_(j=1..4) V^(z_j)/z_j /(2pi i)^4

over the four finite vertical segments, where z_j=(v1,v2,w1,w2). Finite-height Fubini is justified at sigma>1 by the absolutely convergent9^omega(d) majorant. The four infinite vertical integrals are NOT asserted absolutely convergent.

Let Delta_V=min_(n>=1 integer)|log(V/n)|>=1/(2V+1). The standard one-variable truncated Perron bound (with the same halfinteger convention as the accepted source) gives

    |I_T(s)-D_U;a,b,u(s)|
      <= V^(sum c_j) A_abs(sigma,c)
          {product_j[1+2/(pi*T_j*Delta_V)]-1},                         (9)

where

    A_abs = product_(p|a)(1+q^-c1+q^-c2)
            *product_(p|b)(1+q^-c3+q^-c4)
            *product_(p notin T){1+q^-sigma
                  (1+q^-c1+q^-c2)(1+q^-c3+q^-c4)}
           <=3^(omega(a)+omega(b))*zeta_K(sigma)^9.                   (10)

Here T in the Euler products means the DELETED prime set; T_j are heights. To prove(9), expand the four products of truncated kernels versus their indicator products. Each indicator is at most(V/n)^c and each error at most2(V/n)^c/(pi*T*Delta_V). Sum all nonempty error subsets and then the absolute placement series. This proves(9), including uniformity in vertical s and in deleted primes, on sigma>1. The displayed V/Delta dependence is retained; no uniform critical-strip tail is inferred.

Successive positive-line Perron LIMITS therefore give (3). For fixed finite U, the same halfinteger gap supplies a height-uniform C_U(V/n)^c kernel majorant, so these limits can be justified by dominated convergence in the initial absolutely convergent d-series. No silent Fubini of four infinite Perron integrals past a Mellin integral is used below.

## 4. A finite eight-state numerator over ONE principal zeta factor

There is a useful exact finite-U version of(5), requiring no infinite auxiliary integrals. Partition each fixed squarefree residual into its three positions:

    a=a0*a1*a2, b=b0*b1*b2,

internally pairwise coprime. Cross-column intersections are allowed. For the common d, separate its (0,0) portion e and eight squarefree atomic ideals h_ij, (i,j) in{0,1,2}^2 minus{(0,0)}. These eight ideals are pairwise coprime, and all avoid T. Their product is h. Define

    h_i^L=product_(j=0..2)h_ij (i=1,2),
    h_j^R=product_(i=0..2)h_ij (j=1,2).

The four SHORT divisors h_i^L,h_j^R are NOT globally pairwise coprime: an h_ij with i,j nonzero lies in both columns. Imposing that extra disjointness would destroy the actual signed sum. The correct finite constraints are

    N(a_i h_i^L)<=U (i=1,2), N(b_j h_j^R)<=U (j=1,2).                 (11)

The four single-short states carry sign+1. The four double-short states carry their Mobius signs. Summing the remaining e gives the following EXACT identity for sigma>1:

    D_U;a,b,u(s)=N_U;a,b,T(s)/zeta_K^T(s),                             (12)

where the finite numerator is the sum over the residual partitions and all eight-state tuples satisfying(11) of

    mu(a1*a2)mu(b1*b2)mu(h11*h12*h21*h22)
      *(Nh)^(-s)*product_(p|h)(1-(Np)^(-s))^-1.                       (13)

Proof: e is squarefree, coprime to T*h, has coefficient mu(e), and enters neither short divisor. Its absolutely convergent series is1/zeta_K^T(s) times the finite product in(13). At a d-prime the sign is(-1)^[1+1_(i>0)+1_(j>0)]: negative for(0,0), positive for the four single-short states, negative for the four double-short states. This gives(12)--(13) with no missing global Mobius sign.

Every nonzero state enters at least one short divisor. Multiplying the four constraints shows Nh<=U^4 (double states are counted twice in that product), so the numerator is FINITE. It is holomorphic for sigma>0. Its local denominators cannot vanish there, but the numerator itself can vanish. At U=1 only the unit short divisors and h=1 survive, and N_U=1 exactly, for any fixed a,b,u. This is a boundary identity, not a high-window counterexample or a claim of a global zero obstruction.

There is a valid uniform estimate, for sigma>=sigma0>0 and every epsilon>0:

    |N_U;a,b,T(s)| <<_(K,sigma0,epsilon)
         (Na*Nb)^epsilon U^[4*max(1-sigma,0)+epsilon].                 (14)

Indeed residual partitions have multiplicity3^(omega(a)+omega(b)), atomic assignments at a fixed h at most8^omega(h), and product_(p|h)(1-q^-sigma)^-1 <<_(sigma0,epsilon)(Nh)^epsilon. Use the standard divisor bound, Nh<=U^4 and ideal counting/partial summation, with smaller internal epsilons. Deleting primes only shrinks this absolute majorant. There is NO uniformity claimed as sigma0 tends to0. Near sigma=1/2+eta this costs U^(2-4eta+epsilon), reproducing an old type of cutoff loss, not a new power saving.

For later use the full deletion factor remains explicit:

    1/zeta_K^T(s)=[1/zeta_K(s)] product_(p in T)(1-(Np)^(-s))^-1.       (15)

At fixed sigma0>0 its finite product is <<_(S,sigma0,epsilon)(Nrad(abu))^epsilon, hence at most(HD^2)^epsilon in the actual annular support. This controls the mask dependence, not the central reciprocal or its residues.

## 5. The common fixed profile permits a uniform ONE-Mellin reduction

For residual a,b set M=max(Na,Nb), r=min(Na,Nb)/M. If r<=1/2 the product of the two original profile values vanishes (also at equality, since W vanishes at its endpoints). For r>1/2 let t=Nd*M/D. If Na>=Nb put

    Phi_r(t)=W(t)overline(W(rt));

if Nb>=Na use its conjugate. Its support is[1/r,2] subset[1,2]. With M_k(W)=max_(j<=k)|| (t d/dt)^j W ||infinity, the Mellin transform is entire and obeys, for sigma in any fixed compact strip I,

    |Phihat_r(sigma+i tau)| <=C_(I,k) M_k(W)^2(1+|tau|)^(-k),          (16)

uniformly in r in[1/2,1] and both orientations. Leibniz and log-coordinate integration by parts prove it; there is no r-dependent profile optimization or hidden derivative blowup.

After(12) has been proved on its own initial half-plane, ordinary Mellin inversion gives (for any c>1)

    sum_d mu(d)A_U(da)A_U(db)Phi_r(Nd M/D)
      =(2pi i)^-1 integral_(Re s=c) Phihat_r(s)(D/M)^s
                                      N_U;a,b,T(s)/zeta_K^T(s) ds.    (17)

This integral is absolutely convergent vertically by(16) and the initial d-series majorant. In the original annular sum, M<=2D, so the residual a,b sum is finite; the actual row set is also finite. Thus (17), multiplied by the exact outer raw character/nu coefficient from(2), yields an exact mean-retaining representation of Sbold. All capacity/ray/first-five masks remain in the outer actual row set. It applies to both the mixed and pure A6=1 sectors, without claiming separate positivity.

Equivalently insert(15), sum the finite residual/row terms, and write

    Sbold=(2pi i)^-1 integral_(c) D^s A_(D,H,U,W)(s)/zeta_K(s) ds,      (18)

where A is the FINITE coherent sum of the explicit numerators(13), M^-s, Phihat_r(s), full local deletion products and original outer raw character coefficients. For fixed D,H,U it is holomorphic on sigma>0 and rapidly decreasing on fixed vertical strips there, with constants depending on those finite parameters. This is not a uniform target estimate for A. It does not justify shifting the contour past zeros or poles of the displayed ratio without actual residue/cancellation control.

## 6. An actual annular eight-state omission control

Take good prime ideals pi7,pi13,pi19,pi31,pi43 with primary generators

    (1,3),(4,3),(-2,3),(1,6),(7,6)

in the basis1,omega. Their norms are7,13,19,31,43. Set D=1500,U=25,

    d=pi7, a=pi13*pi19 (Na247), b=pi13*pi31 (Nb403),
    u=pi43, unitclass1, A1=37,A2=1,H=floor(1500^(3/4))=241.

The row belongs to the actual pure A6=1 block, is nonprincipal by its first good valuation1, and is coprime to all the column/common factors. The columns da,db have norms1729,2821 in[D,2D]. U is in the accepted high window. One fixed smooth profile plateau on[1.1,1.9] makes both actual values1. No principal unit or raw-zero row is used.

Direct ternary assignments give

    A_U(a)=A_U(b)=-1, A_U(da)=1, A_U(db)=-1.

The actual d coefficient mu(d)A_U(da)A_U(db) is+1. The d-(0,0) state alone gives-1. The eight other-state contributions, after summing the fixed a,b placements, have only(1,0) and(2,0) nonzero, each+1: their sum is+2. Thus a proof retaining only cancellation from a LONG residual e would omit an actual nonzero e=1 correction. This illustrates the NEW eight-state decomposition, not a new claim of old coefficient nonmultiplicativity.

The original pair has gcd pi7*pi13. Its signed gcd expansion cancels across d=1,pi7,pi13,pi7*pi13. Consequently this selected sector does NOT obstruct cancellation in the full h1 sum, prove an uncanceled global zeta pole, or give an energy lower bound. That cross-sector cancellation must remain available in any estimate of(18).

## 7. The attempted estimate and precise stopping point

The proposed useful step would bound the COMPLETE integral/coherent sum in(17)--(18) by D H(HD)^epsilon with fixed nu/S/W seminorms, keeping all original masks and every mean. The nine-zeta factorization and finite numerator supply no such bound. In particular:

* Dropping the eight short states and invoking a scalar Mertens bound is invalid; section6 gives an actual annular omitted term.
* Treating the finite numerator as bounded independently of U near the half-plane loses the explicit U^(2-4eta) cost in(14).
* Normal convergence of H does not control nine reciprocal zeta factors, numerator poles or residues. No zero-free/GRH assumption is allowed.
* A fixed-residual central reciprocal is NOT a proof of a global GRH barrier: original gcd sectors and coherent residual sums can cancel, as the same example demonstrates.

The surviving results are the exact signed common-divisor local factor and nine-shift ratio, explicit uniform correction bound(7)--(8), finite eight-state numerator(12)--(14), the honest finite-height/limit statement(9), and uniform common-profile Mellin reduction(16)--(18). The original signed5/12 improvement remains OPEN. This is neither root's unsigned incidence lift nor a relabelled diagonal/high-gcd estimate, generic Mertens theorem, previous gauge identity or a new global exponent.
