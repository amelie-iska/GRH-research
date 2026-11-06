# Coherent ray means of large sixth-power parts

Research-only draft v1, 6 November 2026. Independent review is required. This is a new quantitative replacement inside the ACTUAL finite primitive dual representation. It is not a new sieve, a full signed estimate, or a GRH/Lean result. The old fixed-s norm comparison is an input, not the claimed new work. No old control, build, browser, publication or environment operation is run.

## 1. Exact scope and the new statement

Work over K=Q(omega), O=Z[omega]. Keep fixed S containing the primes over2,3 and all original exclusions. The fixed source/ray data and the original finite-order nu remain. The original columns are the COMPLETE good SF ideal annulus D<=Nm<=2D, D>1, with

 c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),  1<=U<=sqrt(D),

and the original double short-divisor A_U, not a factored or shrunk substitute. W is ONE common possibly complex fixed smooth profile on[1,2], zero at endpoints, and B=||W||infinity. The rows are only the original unweighted two-pivot family: v3=v4=v5=v6=O, original good SF/coprime v1,v2, all literal/ray restrictions, fixed unit/S-supported u0 with no good support, and the exact capacity Nu0 Nv1(Nv2)^2<=H. Put R=A1 A2, A1,A2>=1. There is no new varying-u0 sum, extra good frozen factor, arbitrary row weight or selected-column indicator.

Use the accepted EXACT finite-k primitive kernel (coherent-band-core, cbk:exact-kernel), with every source pair A,B and ray rho, original coprime m,n, primitive eta=xi_m bar(xi_n) sigma, F=Nf_S Nm Nn, and

 L_e=A1/((Nk)^2 Nl Ne),   l|v2, Nl<=b,
 k good SF, (k,v2)=1, Nk<=sqrt(b/Nl),   e|P_S.

All original coefficients, mu(k),mu(l),mu(e), eta(k^2 l e), epsilon(eta), ray coefficients and raw collision zeros stay in this expression. No root is replaced by a generic conductor phase. No new condition k|s, (k,s)=1 or (v2,s)=1 is inserted. The primitive S zeros are never restored.

Every dual ideal uniquely has

 y=h r s^6,                                                (1)

where h is S-supported, r is GOOD and sixth-power-free, and s is GOOD. Overlap(r,s) is ALLOWED. This is the ordinary extraction of the sixth-power part at good primes; ALL S-supported frequency factors stay in h. In particular h is not restricted to sixth-power-free S exponents.

For X>=1,V>=1 let P_V(X) be the original finite primitive prefix Ny<=X, further restricted by V<Ns<=2V in(1). It is an EXACT representation-fixed signed quantity with all source/ray components, not a literal additive-frequency band or a positive energy. It can also be projected onto the ORIGINAL unequal-norm pairs Nm!=Nn before taking this representation. The following applies in either case.

There is an explicit coherent quantity M_V(X), defined in(8), such that

 |P_V(X)-M_V(X)|/D
  <<_(S,ray,step,epsilon)
       B^2 (D X A2)^epsilon R X V^(-11/2)
              [1+sqrt(A1 X/D^2)].                         (2)

It retains every k/ell/e sign, column/root gauge, h/r value and the exact Bessel weight; only the s sum has been replaced by its fixed-ray coprime IDEAL counting mean. Constants do not depend on A1 through derivatives of its nodal profile. This is an approximation with an explicit error, not a bound on M_V(X).

For the top good-sixth-part band V=X^(1/6)/2 (X>=64 so V>=1), (2) becomes

 |P_V(X)-M_V(X)|/D
    << B^2(D X A2)^epsilon R X^(1/12)
              [1+sqrt(A1 X/D^2)].                         (3)

At the pure critical scales R=A1=D^(3/4),A2=1,X=D^(3/8), the error power is25/32. The prior absolute s count gives13/16 for this top sector. The new error is smaller, but25/32>3/4: it is NOT the pure target for any growing power X in this top-sector estimate. The retained mean may still be as large under the old norm majorant as R X^(1/6). No whole13/12/global9/8 improvement follows.

## 2. The exact sixth-power phase

On GOOD ideals the source character is finite order dividing6. The accepted source/ray expansion reads

 eta(a)=rho(a) tilde(chi)_m(a) bar(tilde(chi)_n(a))

including raw zeros. Consequently, for GOOD s,

 bar(eta(s^6))=psi(s) 1_((s,q)=1),
 psi=bar(rho)^6,  q=m n.                                 (4)

Here q is squarefree precisely on the original coprime SF column support. This identity concerns TOTAL eta, not the possibly angular/radial individual xi_m. The fixed ideal ray character psi is independent of the columns. Its conductor is supported in the fixed exclusions. No claim is made that every rho branch has psi principal, or that a nonprincipal branch actually occurs in a particular original projector.

Keep bar(eta(h)) separately, including zero, and keep bar(eta(r)) including its raw good-prime zeros. Then(4) is valid also when r,s overlap. It does not remove a prime occurring in both r and s from q. The only good-prime s deletion here is (s,q)=1; the other primal/dual masks remain in their original factors.

Let delta_psi be1 if psi is the principal character on good ideals, and0 otherwise. Define

 kappa_K=pi/(3 sqrt(3)),
 kappa_S=kappa_K product_(p in S)(1-1/Np),
 g(q)=product_(p|q)(1-1/Np).                              (5)

The factor g(q) occurs ONLY in the principal-psi counting main. On the original coprime support g(q)=g(m)g(n), a bounded diagonal column modulation; this does NOT factor A_U, beta or any root.

## 3. Elementary fixed-ray count with the FULL q deletion

For t>=0 let

 N_(psi,q)(t)=sum_(s good,Ns<=t,(s,q)=1) psi(s).

The following uniform estimate is sufficient:

 N_(psi,q)(t)=delta_psi kappa_S g(q)t+E_(psi,q)(t),
 |E_(psi,q)(t)|<=C_(S,psi) sqrt(t)
                     sum_(d|q)(Nd)^(-1/2).               (6)

The divisor sum includes EVERY divisor of q, even Nd>t or Nd>2V. Truncating the inclusion-exclusion at2V would leave a spurious principal main tail and is not used.

Proof of the undeleted fixed-ray count: a finite ideal ray character of infinity type0 in this class-number-one field is a periodic multiplicative function of an integral generator modulo a FIXED ideal, trivial on the six units. Enlarge that fixed modulus to encode good-S deletion. For each residue coset of its lattice, the number of lattice points in the disk |alpha|<=sqrt(t) equals disk area divided by covolume plus O_(fixed modulus)(sqrt(t)+1). Cover the disk boundary by lattice fundamental cells: only O_(fixed modulus)(sqrt(t)+1) cells meet it. Divide the nonzero element count by6. The principal finite-character average is the proportion of good-S residues; the nonprincipal average is0 by finite character orthogonality. O has covolume sqrt(3)/2, so the principal coefficient is kappa_K times the S Euler density in(5). Thus

 N_(psi,1)(t)=delta_psi kappa_S t+O_(S,psi)(sqrt(t)), t>=0.

For0<t<1 the ideal count is0 and t<=sqrt(t), so the same bound holds after enlarging the fixed constant; t=0 is exact. No asymptotic assumption on t is hidden.

Now use the EXACT finite identity

 N_(psi,q)(t)
   =sum_(d|q) mu(d)psi(d) N_(psi,1)(t/Nd).

For principal psi its main is kappa_S t sum_(d|q)mu(d)/Nd, which is exactly kappa_S g(q)t; otherwise the main is0. The triangle of the undeleted errors proves(6), INCLUDING its Nd>t terms. This is not a Mertens or GRH input. Since q is SF and Nq<=4D^2,

 sum_(d|q)(Nd)^(-1/2)=product_(p|q)(1+(Np)^(-1/2))
                         <<_epsilon D^epsilon.          (7)

To verify the last elementary bound, for each chosen epsilon absorb the finitely many small primes into a fixed constant and use1+P^(-1/2)<=P^epsilon for all larger P, adjusting epsilon for Nq<=4D^2.

## 4. Exact coherent main, endpoints and Bessel variation

Denote by C_outer the ORIGINAL product preceding the dual sum in cbk:exact-kernel:

 c_m bar(c_n) R_m(v2^2)bar(R_n(v2^2)) h_(ABrho)(v2)
 *mu(k)mu(l)mu(e) eta(k^2 l e) epsilon(eta) L_e/sqrt(F).

Its indices and masks are exactly those in section1. For fixed h,r put

 b_hr=min(2V,(X/(Nh Nr))^(1/6)),
 a_hr=L_e Nh Nr/F.

Terms with b_hr<=V are empty. Define

 M_V(X)=sum_outer C_outer
   sum_(h S-supported,r good6free,b_hr>V)
       bar(eta(h))bar(eta(r))
       delta_psi kappa_S g(q)
            integral_V^b_hr dot(G)(a_hr t^6)dt.          (8)

The same original unequal-norm projection, when desired, is imposed in outer, before this definition. No source component is centered or discarded. All primitive S values, finite k cutoffs and original capacity remain. Equation(8) is neither a primitive character of an overlapping-column extension nor a PSD assertion. It does not take any conductorwise absolute value in its main. Only its rigorously bounded error below uses triangles.

The exact inner sum being replaced is

 sum_(s good,V<Ns<=b_hr,(s,q)=1)
                     psi(s) dot(G)(a_hr (Ns)^6).         (9)

Both endpoint conventions are literal: V<Ns and Ns<=b_hr. They remain correct at integer ideal norm ties; no half-weight is substituted. Stieltjes summation by parts gives the difference between(9) and its integral main as

 w(b_hr)E(b_hr)-w(V)E(V)
                          -integral_V^b_hr E(t)w'(t)dt,

where w(t)=dot(G)(a_hr t^6) and E is(6). This formula uses closed-prefix N(t) at both endpoints, so it preserves the open-lower/closed-upper convention exactly.

For the ACTUAL nodal capacity profile0<=G<=1 supported in[1/2,5/2], the accepted Bessel formula is

 dot(G)(x)=C0^(-1/2) integral G(v)J0(2 sqrt(xv/C0))dv,
 C0=3/(4pi^2).

The elementary angular integral representations give |J0|,|J1|<=1 on the real axis. Hence

 ||dot(G)||infinity<=2 C0^(-1/2)=C_G0,
 |x dot(G)'(x)|<=C0^(-1) sqrt(x) integral G(v)sqrt(v)dv
                         <=2 sqrt(5/2) C0^(-1) sqrt(x).

There is NO derivative of G in either bound. Since t<=b_hr,

 a_hr t^6<=L_e X/F<=A1 X/D^2.

Thus on[V,b_hr],

 integral |w'(t)|dt
   <=6 log(2) *2sqrt(5/2) C0^(-1) sqrt(L_e X/F)
   <<sqrt(A1 X/D^2).                                    (10)

The case b_hr<=V is0. Combining(6),(7),(10) proves, uniformly in every original outer parameter,

 |(9)-delta_psi kappa_S g(q) integral_V^b_hr w(t)dt|
   <<_epsilon D^epsilon sqrt(V)
                         [1+sqrt(A1 X/D^2)].             (11)

The interval cutoff is handled by its two boundary terms; it is not smoothed away, and no capacity derivative cost is hidden.

## 5. Full outer normalization and all nonunit modes

For the original columns, the elementary short-divisor count gives

 |A_U(m)|<=3^omega(m)<<_epsilon D^epsilon,

uniformly in U; no coefficient is replaced by that bound in(8). The complete good annulus has O(D) ideals by the same lattice-cell argument. Therefore there are O(D^2) possible original ordered column pairs; retaining the coprime/source/unequal restriction only reduces this count in the ERROR estimate.

The modulus of L_e/sqrt(F), including its correct primitive conductor, is at most

 A1/[D (Nk)^2 Nl Ne].

Normalize ONCE byD. Sum (11) absolutely only for the error: the two annular column counts cancel the resulting D^(-2). The original finite square-divisor sum is bounded by

 sum_(k original) (Nk)^(-2)<=zeta_K(2),

AFTER (11); its signs and its finite cutoff were kept in(8). The e sum is fixed. The actual l divisor sum costs at most tau(v2), hence A2^epsilon. The complete unweighted actual v2 annulus has O(A2) ideals.

It remains to count h,r with b_hr>V. Necessarily

 Nh Nr<X/V^6.

The number of GOOD sixth-free r of norm<=Z is at most the number of all ideals, O_K(Z) for Z>=1; below1 there is no r. Consequently

 sum_(h S-supported) #r with b_hr>V
   << X V^(-6) sum_(h S-supported)(Nh)^(-1)
   <<_S X V^(-6).                                      (12)

ALL S-supported h, not just h=O, are present in this bound and in(8). Their individual primitive zeros remain exact; absolute value<=1 is used only in the error. The geometric Euler sum over h in(12) is finite for fixed S.

Equations(11),(12), the original row count and the once-only normalization prove(2). At each fixed X these h,r and k sums are FINITE; no infinite-dual interchange, omitted high-frequency tail, primitive-vs-induced conductor replacement or higher-G-derivative assumption is used. The argument applies unchanged with the original unequal-norm pair restriction, without subtracting an unrelated whole equal-norm bound from an individual frequency sector.

## 6. What this does and does not repair

For a general dyadic good-sixth-part band the ERROR ALONE is target-sized whenever

 R X V^(-11/2)[1+sqrt(A1 X/D^2)]<=H

up to the explicitly permitted epsilon loss. This condition is a sufficient error budget, not a condition on the true signed kernel or a bound for its main. For example, at the critical mixed scales R=D^(7/12),H=D^(3/4),A1=D^(5/12),X=D^(3/8), the top-band error has power59/96, below3/4; the principal coherent mean is still present. At pure R=H and X a growing power in the low-Bessel regime, the top-band error R X^(1/12) does not certify target size.

The genuinely new surviving result is(2): an actual coherent arithmetic s-average main with full q deletion and a quantitative error. It halves the counting exponent for the top good-sixth-part sector, from X^(1/6) to X^(1/12) IN THE ERROR. It is not the old fixed-s comparison retold: (8) now contains the integrated s profile and the exact principal-density column modulation g(m)g(n), with every r/k/root/column mean still coupled.

A failed next step would be to call the principal mean0, to discard rho branches, or to sum its modulus and assert that the X^(1/6) count has disappeared. In the same-class/rho1 branch delta_psi=1 and the retained mean is generally present. The original finite mu(k) sum is still independent of s, so no k|s convolution or local termwise annihilation has been proved. A further signed estimate for(8), jointly with its remaining r/k/root/column orientations and other sectors, is required. The approximation does not rule out such cancellation and proves no impossibility theorem.

All source/primal masks and class/ray/capacity conventions are those stated, with the complete original annulus and fixed W. The current whole two-pivot13/12/global9/8 bounds, principal/short/full assembly, positive determinant/zero-location and all GRH/Lean obligations remain unchanged. This research note is OUTSIDE the concurrently published book milestone and requires independent adversarial review.
