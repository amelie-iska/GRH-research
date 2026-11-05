# Actual h=1 two-pivot completion and the surviving angular gauge

Status: exact application and scoped limitation, with a new explicit fixed-conductor identification submitted for independent review. Version1 is retained unchanged. All source pins are in source-pins-v1.json. This uses the accepted period-four phase law in research/reciprocity-period.md section2 and the elementary Gauss--Jacobi identities already proved in papers/theta-jacobi-{core,details}.tex. It is not a new evaluation of a Gauss/Jacobi sum, a CM priority claim, an upper saving, or a GRH result. The fixed-conductor ideal character below is constructed directly, without assuming a CM theorem. No old reciprocity/joint tables are rerun.

## 1. Existing central quadratic phase, with the actual pairing

Let O=Z[omega], omega^2+omega+1=0, delta=1+2omega. For a good squarefree ideal q=(beta), beta=a+b omega, Q=Nq odd, use exactly

    e_beta(z)=exp(2 pi i Tr(z/(delta beta))),
    xi_q(z)=x_q(z)^3,  tau_beta(xi)=sum_(z mod q) xi(z)e_beta(z).

Characters are zero on nonunits. If z=x+y omega, then

    Tr(z/(delta beta))=(-b x+a y)/Q.                         (1)

At every prime of q, the number of square roots of z is 1+xi_p(z), including z=0, with the first term the literal constant1. CRT consequently gives

    sum_(x mod q)e_beta(x^2)
      =sum_(d|q) sum_(z mod q) xi_d(z)e_beta(z)
      =tau_beta(xi_q).                                      (2)

Here xi_d is inflated to q as a function of its d-coordinate and is the literal constant1 on the complementary CRT coordinates. For d proper, summing one complementary coordinate annihilates that term because e_beta is primitive; the last term is the raw primitive xi_q. This proves (2) even when q contains inert primes or both conjugates of a split rational prime. It is NOT valid to replace the root count by 1+xi_q on a composite ring. The q=1 convention gives both sides1.

The already accepted Gaussian evaluation, with this same delta pairing, is

    gamma(beta)=tau_beta(xi_q)/sqrt(Q)
      =[1+i^(-b)+i^a+i^(b-a)]/2.                            (3)

For clarity, (3) is reused from research/reciprocity-period.md section2, whose fixed-beta Gaussian/Poisson proof and finite mod4 components are already accepted. The present new step is (2) and its insertion in the actual moment. No new phase theorem or formalization is asserted. Equivalently gamma=1 when Q=1 mod4; when Q=3 mod4, gamma=i(-1)^((b+1)/2) for b odd, and gamma=i(-1)^((a-1)/2) for b=2 mod4. These are the twelve unit residues beta mod4.

In the FULL six-variable jdq identity at h=1, alpha=1 and ell=Q. Its scalar is exactly

    mu(q) Q^2 xi_q(-1) tau_beta(xi_q)/Q^6
       =mu(q) Q^(-7/2) varpi(beta),
    varpi(beta)=(-1)^((Q-1)/2)gamma(beta).                   (4)

Thus on each fixed beta mod4 ray the central Gauss root of unity is constant. The Mobius sign, all orientation coefficients, fixed literal-unit/S phases, and the actual Fourier weight remain. Formula(4) does not remove any raw zero or prove cancellation. In particular the central character in (3)--(4) is QUADRATIC, not cubic.

## 2. The Jacobi factor belongs to the correctly oriented prime

For a good prime ideal p, let k=O/p, n=Np, and let chi=x_p be the LITERAL positive sixth-power-residue character: reduction of chi(z) in k is z^((n-1)/6). Define

    j(p)=J_p(chi,chi^2)=sum_(x in k)chi(x)chi(1-x)^2 in O,
    j(s)=product_(p|s) j(p)                                (5)

for squarefree good s. Both zero branches in (5) are retained. The standard grouping-by-x+y identity gives

    G(chi)G(chi^2)=j(p)G(chi^3),  |j(p)|^2=n.               (6)

All three characters in (6) are nontrivial, so no exceptional trivial-character Gauss norm is being used. This is the already established elementary finite-field Gauss argument, independent of the choice of nontrivial additive character.

There is a useful exact arithmetic orientation check. Reduce (5) modulo the SAME p:

    j(p) mod p = sum_(x in k) x^((n-1)/6)(1-x)^((n-1)/3)=0. (7)

After expansion every exponent lies between (n-1)/6 and (n-1)/2, strictly between0 and n-1; all corresponding power sums vanish. Hence j(p) lies in p. Since N(j(p))=n by (6),

    (j(p))=p,  j(p)=epsilon_p pi_p, epsilon_p in mu6,       (8)

for any specified ideal generator pi_p. This includes an inert rational prime p: its ideal norm is p^2, and j((p)) is a unit times p. Inverting the literal character conjugates j and gives the conjugate prime ideal; it must not be silently identified with the same split prime.

This is not a second new Jacobi norm theorem. With rho=chi^2, eta=chi^3, the OLD theta section uses J_old=J(rho,eta) and j_theta=-eta(-1)J_old. In fact

    J(chi,chi^2)=J(chi^2,chi^3)=J_old.                      (9)

To check the normalization directly, divide the two Gauss--Jacobi identities. Their quotient is G(chi)G(chi^5)/G(chi^3)^2=chi(-1)n/[chi^3(-1)n]=1. Thus the new local factor is exactly -eta(-1) times the old theta Frobenius normalization. The relevant finite ray law can in fact be proved directly, as follows; it is not inferred merely from the norm.

### Explicit fixed conductor, including the local unit signs

Put f=(2 delta), of norm12. The ideals (2) and (delta) are coprime. The six Eisenstein units map BIJECTIVELY onto (O/f)^*: modulo2 they map onto F4^* with kernel{1,-1}, and modulo delta they map onto F3^* with kernel mu3. The combined kernel is1 and the target has order6. Therefore every ideal a prime to f has a UNIQUE generator Psi(a) congruent1 mod f. This applies first to integral ideals by the PID property and extends multiplicatively to fractional ideals prime to f. Uniqueness proves Psi(ab)=Psi(a)Psi(b), with |Psi(a)|=sqrt(Na). For a principal ideal (alpha) prime to f, if u_f(alpha) is the unique unit with u_f(alpha)=alpha mod f, then

    Psi((alpha))=alpha/u_f(alpha).                          (9a)

Thus this is an algebraic Hecke character with principal value alpha on alpha=1 mod f (the convention called infinity type(1,0)). Its unitary normalization is Psi(a)/sqrt(Na). Equation(9a) explicitly supplies the finite part, not just a claim of finite conductor.

The local Jacobi sum has precisely this normalization. Modulo delta, a sixth root v satisfies v=v^3 while v^2=1, and the raw zero branches at x=0,1 are excluded before this replacement. Consequently

    j(p) = sum_(x not0,1) eta(x) = -1 mod delta.

Modulo2, a sixth root v satisfies v=v^4. Thus reduction of j is reduction of J(chi^4,chi^2). These two nontrivial characters are inverse, and the elementary inverse-character Jacobi identity gives J(chi^4,chi^2)=-chi^4(-1)=-1. That identity follows by the bijection x/(1-x) from k minus{0,1} to k^* minus{-1}, so it also retains the exact zero convention. Therefore

    j(p)=-1 mod2,  j(p)=-1 mod delta,
    -j(p)=1 mod f,  -j(p)=Psi(p).                          (9b)

Here (j(p))=p from (7)--(8), so uniqueness of the generator proves the last equality at split AND inert primes. The reduction arguments take place in the CHARACTER VALUE ring O/(2) and O/(delta), not in the characteristic-p residue field used in (7); these are different operations. For inert rational p, (9b) in particular gives j((p))=p and Psi((p))=-p.

The finite conductor is EXACTLY f. It divides f by (9a). A proper divisor omits2 or delta: if it divides(delta), omega is a nonidentity unit congruent1 modulo that divisor; if it divides(2), -1 is such a unit. The required principal value would then give Psi((omega))=omega or Psi((-1))=-1, contradicting that these are the unit ideal with value1. This proves primitivity with the stated infinity type. It makes no appeal to elliptic modularity, a Frobenius comparison, GRH, or an unproved distribution of prime arguments.

For squarefree good s, and ONLY asserting the Mobius identity there,

    mu(s)j(s)=product_(p|s)(-j(p))=Psi(s).                  (9c)

For nonsquarefree s, mu(s)=0 whereas Psi(s) need not vanish; (9c) must not be extended to arbitrary ideals. Psi itself is of course defined multiplicatively on all ideals prime to f. The literal inverse orientation in t is its complex conjugate, not a second choice of infinity type hidden in j(p).

## 3. Exact two-pivot identity with all original masks

Work at h=1 in the ACTUAL jdq C--C term: r,t are coprime squarefree column ideals, q=rt not1, theta=x_r conjugate(x_t). Retain every excluded orientation by coefficient zero. Freeze the literal u0 and v3,v4,v5,v6, putting

    Z=u0 v3^3 v4^4 v5^5 v6^6.

Let F(v1,v2) be the exact finite weight of the remaining actual rows. The first five factors are squarefree and pairwise coprime; v6 is arbitrary, with its allowed overlaps. F retains the chosen literal/ray classes, pairwise and fixed-factor restrictions, and the sharp weighted capacity. It is independent of the column ORIENTATION r|q; if a restriction depends on r, it must stay in that orientation's coefficient and cannot be hidden in this common F. For residues x,y mod q, F_q(x,y) is the sum of the actual finite weights with those residues, allowing repetitions. Define

    Fhat_beta(k1,k2)=sum_(actual v1,v2) F(v1,v2)
                       e_beta(-k1 v1-k2 v2),
    T_(q,F)(theta)=sum_(k1,k2 mod q, (k1 k2,q)=1)
                    Fhat_beta(k1,k2) conjugate(theta(k1 k2^2)).

Finite Fourier inversion and primitivity give, INCLUDING all nonunit zeros,

    sum F(v1,v2)theta(v1)theta(v2)^2
      =Q^(-2)tau_beta(theta)tau_beta(theta^2) T_(q,F)(theta)
      =Q^(-2)tau_beta(xi_q) J_q(theta,theta^2) T_(q,F)(theta), (10)

because theta^3=xi_q on every local component. The two first characters are primitive on q, including the inverse orientations. Every nonunit-frequency Gauss sum is zero; no inverse character is evaluated there. This is a two-variable completion, not the old five-variable completion with the other three factors deleted.

Jacobi sums CRT without any additive-generator multiplier. At p|r the local orientation is chi, and at p|t it is conjugate(chi). Thus

    J_q(theta,theta^2)=j(r) conjugate(j(t)),
    mu(q)J_q=(mu(r)j(r))conjugate(mu(t)j(t)).               (11)

The quantities j(p) themselves do not depend on a choice of additive generator beta. With

    lambda(s)=j(s)/sqrt(Ns),  |lambda(s)|=1,
    c(s)=r_U(s)nu(s)W(Ns/D),
    b(s)=mu(s)lambda(s)c(s)
        =[Psi(s)/sqrt(Ns)]c(s) on the actual SF columns,    (12)

the source's selected h1 C--C slice is EXACTLY

    S_(1,F,Z)=D^(-1) sum_(q sf good, q not1) gamma(beta_q)/Q
                   sum_(r t=q, (r,t)=1)
                     b(r)conjugate(b(t)) theta_(r,t)(Z)
                     T_(q,F)(theta_(r,t)).                 (13)

For the source C--mu term, replace the second r_U by1; in the high-cutoff A--A expansion replace both by r_U-1. The passage to that A--A formula requires the source's stated high-cutoff window; (13) does not extend its coefficient identity beyond its hypotheses. The common possibly complex W remains the actual fixed profile and is never optimized by q or orientation.

Unlike the FULL six-variable formula(4), (10)--(13) contain gamma and NO extra xi_q(-1). The latter in the six-variable formula came from pairing the completed powers1/5 and2/4. Here powers3/4/5 are uncompleted literal factors in Z, so inserting that sign again would be a normalization error.

The zero branch theta(Z)=0 retains every common prime of q and the fixed factors, including v6 at sixth-power valuation. Such a factor is NEVER replaced by1 because its exponent is6. The first-five disjointness and arbitrary-v6 masks remain in F and theta(Z). In an A6=1 dyadic sector v6 can still have any literal representatives permitted by that block; fixing it here is a slice, not the assertion v6=1.

Generator changes provide another check. If beta becomes u beta, tau becomes xi_q(u)tau. Meanwhile Fhat_new(k1,k2)=Fhat_old(u^-1 k1,u^-1 k2), and changing variables in T multiplies T by conjugate(theta(u^3))=xi_q(u). These signs cancel. Equations(10) and(13) are therefore independent of a generator choice even though gamma is not. Formula(1) retains the inverse different throughout.

## 4. Surviving budget and the exact failed shortcut

Let

    B2_q(K)=sum_(k1,k2 units, k1 k2^2=K) Fhat_beta(k1,k2),
    a_g(r)=b(r)conjugate(b(q/r))theta_(r,q/r)(Z).

Then T is the exact orientation transform of B2. Distinct orientations have nontrivial cubic quotient, as in jdq, so orthogonality gives the surviving bound

    |S_q| <= sqrt(phi(q))/(D Q)
              (sum_(r|q)|a_g(r)|^2)^(1/2) ||B2_q||_2.     (14)

All norms here use unnormalized counting measure. Since mu and lambda have modulus1 on surviving columns,

    sum|a_g(r)|^2=sum|c(r)c(q/r)theta(Z)|^2.                (15)

Every unit-product fiber has phi(q) points, but B2 is the actual weighted sum, not uniform fiber averaging. The coherent orientation mean remains. Neither the finite gamma phase nor (8) licenses treating B2 as independent of the columns.

Precisely, multiplication of any column vector by lambda(s) is a diagonal unitary map. Any matrix with entries multiplied by lambda(r)conjugate(lambda(t)) is a unitary conjugate and has exactly the same operator norm; this remains true with arbitrary retained masks and capacity weights already in the matrix. Thus ABSORBING the normalized Jacobi factors into arbitrary coefficients preserves every previous coefficient norm/operator bound. It supplies no numerical gain by itself. This is an exact limitation, not a claim that the actual arithmetic b(s) cannot cancel.

A genuinely new estimate would have to bound the ACTUAL sum in(13), with its now explicitly identified fixed-conductor spin-one Hecke/r_U/nu/common-W coefficients and q-dependent masked T, before taking conductor-wise absolute values. For example an h1 contribution at target scale would require a bound of the form |sum_q gamma(beta_q) Q^-1 sum_r b(r)conjugate(b(t))theta(Z)T| << D H (DH)^epsilon, after the actual row slices are summed, with the required fixed-profile derivative/ray/cutoff uniformity. This is a sufficient h1 budget to pursue, not a necessary separate bound if other h or signed C--mu terms can cancel it. The original residue-subtracted moment also needs the actual signed C--C/C--mu/mu--mu assembly and the remaining h. No such signed inequality is proved here. The published unsigned7/6 envelope is unchanged; the mixed and pure A6=1 neighborhoods remain open.

## 5. Exact boundary check when the second pivot has length one

This is a normalization/limitation check for the pure-A1 sector, not a repeat of the accepted old phase audit. Suppose the actual slice fixes v2=c with (c,q)=1 and F(v1,v2)=F1(v1)1_(v2=c). Then Fhat=Fhat1(k1)e_beta(-k2 c), so direct Gauss inversion in k2 gives

    T_(q,F)(theta)=theta(c)^2 tau_beta(conjugate(theta^2))
                     sum_(k1 units)Fhat1(k1)conjugate(theta(k1)).

The equality uses theta^2(-1)=1. Substitution into (10), and tau(theta^2)tau(conjugate(theta^2))=Q, yields EXACTLY the original one-pivot formula

    sum F1(v1)theta(v1)theta(c)^2
       =theta(c)^2 Q^-1 tau_beta(theta)
                    sum_(k1 units)Fhat1(k1)conjugate(theta(k1)).

Thus the extra completion's Jacobi/central factors are undone by the literal length-one Fourier factor. It is invalid to keep their putative cancellation while discarding that factor. If (c,q) is nonunit, the original slice is zero; the corresponding Gauss identity also gives zero. This check uses no independent profile or positivity assumption. It explains concretely why the two-pivot rewriting alone cannot repair the pure-A1 upper-envelope witness. A coupled arithmetic estimate for the actual fixed Hecke-twisted coefficients and Fourier weight is still missing.
