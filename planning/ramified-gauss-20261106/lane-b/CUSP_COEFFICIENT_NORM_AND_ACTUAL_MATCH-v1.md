# Known cusp coefficient norms, full finite-character matching, and the finite top prefix

NEW research-only candidate v1, 6 November 2026. Independent review is REQUIRED.
The new quantitative survivor is an explicit absolute norm for EVERY KNOWN
DR integral cusp coefficient family, its exact transport through the rational
translate construction, and an exact actual-family matching/assembly.
The complete actual top-prefix conclusion below requires acceptance of the
new root/lane-C rational-cusp/angular Mellin identity; it is NOT imported
from the old away-3 source theorem. No whole h1/global/GRH conclusion follows.

All work is SSH Linux in the new lane's owned paths. Prior scientific
controls, tables and tails are not replayed. Existing pinned primary bodies
stay private/local; only their already public bibliographic/version metadata
and hashes belong in any future public closure.

## 1. Exact primary data and a uniform bound for all27 known cusps

Primary: Dunn--Radziwill arXiv2109.07463v3, UNCONDITIONAL Section5 and
AppendixA. PDF SHA256 df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0;
text SHA256 636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767.
The GRH-conditional prime theorems are not inputs.

Let lambda=1+2omega, Nlambda=3. Use the source primary1mod3 generators
and source Fourier pairing. The KNOWN functions F_j=theta(gamma_j*w),
j=1,...,27, have the exact (5.12)--(5.16) nonconstant expansions.
AppendixA gives each coefficient d_j(mu) as ONE unit multiplier times
tau(epsilon*mu), tau1(epsilon*mu), or tau2(epsilon*mu), times an explicit
unit-modulus additive phase; epsilon is a cubic unit. The first9 use tau,
the next9 tau2 and the last9 tau1. Their constant terms are not included
in the absolute series below. No coefficient bound for an unknown new
cusp is assumed.

For real sigma>1 put
 A_j(sigma)=sum_(mu!=0)|d_j(mu)| (Nmu)^(-sigma).
The sign/conjugate convention d_j(-mu) has the SAME bound. Write
 Z_SF(sigma)=sum_(c primary,SF,(c,3)=1)(Nc)^(-sigma)
 <=zeta_K^((lambda))(sigma).
The cube d is arbitrary primary good atlambda; c,d may overlap.

From (5.7), on the first lambda family
 mu=+/- epsilon lambda^(3n-4)c*d^3, n>=1,
 |tau(mu)|<=3^(n/2+2)*sqrt(Nd).
There are at most6 listed unit/sign branches. On the second family
 mu=+/- lambda^(3n-3)c*d^3, n>=0,
 |tau(mu)|<=3^(n/2+5/2)*sqrt(Nd),
with at most2 branches. These follow from the actual unnormalized primitive
Gauss magnitude |g(a,c)|=sqrt(Nc) for SF c and the fixed lambda-numerators,
combined with the explicit |d/c| factor. It would be WRONG to replace this
by an arbitrary bound (Nmu)^(1/6) and lose convergence at sigma just above1.

Set z=3^(1/2-3sigma). Then
 A_tau(sigma)<=
 [6*3^(2+4sigma)*z/(1-z)
       +2*3^(5/2+3sigma)/(1-z)]
      Z_SF(sigma)*zeta_K^((lambda))(3sigma-1/2).          (1)

Equations (5.13),(5.14) each have3 unit branches at mu=lambda^-4*c*d^3,
with magnitude at most9*sqrt(Nd), so
 A_tau1(sigma),A_tau2(sigma)
 <=27*3^(4sigma) Z_SF(sigma)
                       *zeta_K^((lambda))(3sigma-1/2).  (2)

In particular, for 1<sigma<13/12,
 z<=1/9, 3^(2+4sigma)<=3^7, 3^(5/2+3sigma)<=3^6,
 27*3^(4sigma)<=3^8.
The bracket in (1) is at most3^8/2. Thus EVERY known cusp obeys
 A_j(sigma)<=3^8 zeta_K^((lambda))(sigma)
                         zeta_K^((lambda))(3sigma-1/2). (3)

This is an explicit coefficient norm at sigma=1+eta,0<eta<1/12.
Its dependence on eta is honest and it is independent of every moving
translate, moving good level, primitive-S state and ideal length. The
lambda geometry and cube support, rather than fixed dimensionality,
prove its finiteness.

## 2. Exact affine coefficient transport; keep the ramified scale

For any of these KNOWN F_j and fixed A!=0,B in K, the H3 affine map is
 (z,v) -> (A*z+B, |A|*v).
A Fourier index mu becomes nu=A*mu, and its nonconstant coefficient is
 EXACTLY
 a_(j,A,B)(nu)=|A| d_j(mu) e(Tr(mu*B)), nu=A*mu.          (4)

Consequently
 sum_(nu!=0)|a_(j,A,B)(nu)| (Nnu)^(-sigma)
       =|A|^(1-2sigma) A_j(sigma).                     (5)
For an angular unit weight Theta_ell(nu), the extra factor is the explicit
unit (A/|A|)^ell. A pure differential derivative has its own known A powers;
the angular Dirichlet coefficient after the source Gamma normalization
has no hidden growing absolute coefficient.

In lane-A's primitive high-lambda translate construction B0=f-2,
the fixed state is F_j U(-b/lambda^B0) A_(lambda^-B0).
Here A=lambda^-2B0, so nu=lambda^-2B0*mu and
 a(nu)=3^-B0 d_j(mu)e(-Tr(mu*b/lambda^B0)).
Its norm factor is3^(B0*(2sigma-1)), fixed once f is fixed.

The moving translation must be placed with the CORRECT order:
 F_j U(-b/lambda^B0) U(-lambda^4*c/r) A_(lambda^-B0)
 = [F_j U(-b/lambda^B0) A_(lambda^-B0)]
                               U(-lambda^(4+2B0)*c/r).
Thus its phase is EXACTLY e(-Tr(lambda^4*mu*c/r)).
Omitting lambda^(2B0) after moving the translation past the diagonal is
wrong; it changes actual phases. No phase is set to1 in (4).

The root/lane-C general rational construction is even simpler for the
coarse bound: it uses only known F_j translated by -D/C, with NO unknown
cusp series. There (5) has A=1 and the arbitrary rational translation
changes no absolute norm, solely because its explicit phase has modulus1.

## 3. General rational transform and the coarse dual norm

This section uses the NEW exact identity independently derived by root
and lane-C, rather than the old DR unit-Fourier-support corollary.
For a reduced a=A/C choose integral gamma=[[A,B],[C,D]] of determinant1.
With U(x)=[[1,x],[0,1]], W_C=[[0,-1/C],[C,0]], matrix multiplication gives
 gamma^(-1) U(a)=U(-D/C) W_(-C).
Write its actual known coset gamma=delta*gamma_j, delta inGamma2.
Then
 theta(U(a)w)=chi(delta) F_j(U(-D/C)W_(-C)w).             (6)
The Kubota multiplier chi(delta) is retained EXACTLY; its absolute value
is1 only because source automorphy supplies that value. It is not an
arbitrary primitive-S root or a freely chosen scalar.

Lane-C RATIONAL_CUSP_CONSTANTS_AND_MELLIN-v1 gives the full-z angular
chain rule. For ell!=0 its Mellin identity is
 Lambda_a(s,ell)=chi(delta)(-1)^|ell|(C/barC)^ell
                     (NC)^(1-2s)
              Lambda_(j,-D/C)(1-s,-ell).                (7)
The factor1-2s includes the Jacobian. The known radial constants are
killed by PURE nonzero-angular derivatives at z=0, not by calling a
character noncubic. For ell=0 retain the actual residues; no pole-free
claim is made. The independence and exactness of (6),(7), including those
constants, are required separately reviewed inputs to the actual theorem.

Let kappa be any fixed finite denominator character on the actual primary
section, with all original raw modulus zeros. Separate its lambda and
away-lambda factors. Choose f>=max(2,cond_lambda kappa) and
 Phi(x)=kappa_lambda(x)*1_(x congruent1 modlambda^2),
 zero on nonunits. It has normalized Fourier coefficient mass at most
3^(f/2), with the perfect pairing denominatorlambda^(f+1).

For a moving SF cubic level t (unit allowed), R=Nt, take the literal
period M=F*t, where F is the FIXED away-lambda modulus including all raw
fixed-prime exclusions. This is a PERIOD, not a primitive conductor.
Even when t meets F, or kappa_away is imprimitive, the bounded function
 psi_M(x)=kappa_away(x)*chi_(3,t)(x)^(+/-1)
is periodic moduloM. Normalized Fourier inversion and Parseval give
 sum_u|q_u|<=sqrt(NM).                                 (8)
No primitive Fourier-support hypothesis or nonzero kappa(t) is needed.

Apply Phi and psi_M to the integral index x=lambda^3*mu of theta.
The exact additive translations are
 a_(h,u)=h*lambda^(2-f) +/- lambda^3*u/alpha_M,           (9)
with signs consistent with the chosen Fourier convention. Their total
coefficient mass is at most3^(f/2)*sqrt(NM). Every reduced denominator
C_(h,u) divides a fixed lambda-power times M; hence
                 1<=NC_(h,u)<=C_(f,F)*R.              (10)
Nonunit Fourier residues simply reduce that denominator. They are NOT
discarded or declared to be original nonzero states.

At s=-eta+i*yau,0<eta<1/12, (3), (7), the source two-Gamma quotient and
(8)--(10) give the NONCONSTANT dual absolute estimate
 sum_(h,u)|b_h q_u| (NC_(h,u))^(1+2eta)
                  A_(j(h,u))(1+eta)
   <=C_(f,F,eta) R^(3/2+2eta).                         (11)
It uses the exact known cusp norm before taking absolute values. Every
Kubota, angular, source/unit and translate phase remains in the exact
finite expression and is bounded only after that expression is written.
No refined R^(1/2+eps) assertion or Ramanujan cancellation is claimed.

## 4. Exact primary branch and coefficientwise cube completion

The integral index Phi(lambda^3*mu) selects EXACTLY the source subset
 S={lambda^-3*c*d^3:c,d primary1mod3,c SF}.
Indeed all other valuation families in DR(5.7) make lambda^3*mu nonunit;
the minus n=0 branch is -1mod3; only the plus branch is1mod3.
This tests actual unit states, not only ideal norms.

On S, tau(mu)=3^(5/2)gtilde(c)*sqrt(Nd), and
 Phi(lambda^3*mu)psi_M(lambda^3*mu)
 =kappa(c)kappa(d)^3 chi_(3,t)(c)^(+/-1)
                                      1_((d,t)=1).
The source angular factor oflambda^-3 is i^ell. Thus initially Re(s)>1,
 the completed numerator is EXACTLY
 D_H(s,ell)=3^(5/2+3s)i^ell
   L^(RAW)(3s-1/2,kappa^3 Theta_(3ell)) R_(kappa,t,ell)(s), (12)
where R has coefficients gtilde(c)kappa(c)chi_(3,t)(c)^(+/-1)Theta_ell(c).
ALL primes in the original lambda/F/t zero support stay deleted in L,
even if cubing or taking a primitive character lowers its conductor.
There is no kappa(lambda), no division at a zero and no radical height
substitution. Complex conjugation of the WHOLE construction covers the
actual conjugate Gauss root and opposite orientation.

The new (6),(7),(11),(12) give a right-line bounded completed numerator,
an entire angular Mellin for ell!=0, and left cost
 R^(3/2+Oeta)(1+height)^(2+Oeta).
The already independently reviewed completed-convexity and sharp Perron
argument therefore yields, for every physical SF t and exact interval,
 |F_psi(T;t;1,I)| <<_fixed,eps
 V1(W)(T Nt)^eps min(sqrt T,T^(1/4)(Nt)^(3/8)).          (13)
This statement is new for ramified lambda characters because its actual
projector and rational-cusp transform have now been constructed. It is
not a reuse of an away-3 equation for an unknown local state. Final
acceptance still requires the independent (6),(7) and actual-family gates.

Literal subunit T in[1/2,1) is handled by its possible unit coefficient,
bounded by a fixed multiple of the same RHS; T<1/2 is empty on the
original annulus with zero endpoints. This is not an external theorem
invoked below its length range.

## 5. Exact ACTUAL finite-family match

The accepted actual all-component TypeI factor list has, after the
genuine Jacobi angular factor, the original FIXED FINITE-ORDER nu,
source/ray characters, Gamma finite characters, primitive-S-type residue
factors and fixed numerator e_S/w/u0 symbols. All w have norm<64 and
e_S ranges over the original fixed finite set. Thus these are a FIXED
FINITE family of finite residue factors on the primary section, not a
uniformity assertion across growing finite conductors.

The phase normalization is kept: vartheta(c)=Theta_1(c)barChi_(3,c)(2)
and G_actual(c)=Chi_(3,c)(lambda)G_source(c).
Their exact product gives the source general-frequency12t. The fixed12
correction is absorbed into this FIXED kappa family; it is NEVER treated
as a good SF moving level. Remaining moving frequency t is precisely the
physical SF ideal p*d*k (and h*t after exact deletion). General finite
order nu has no angular component, but need not have order dividing6.
Both actual angular signs are+1/-1, so the constant-term gate applies.

Every joint finite-S conductor-drop/e_S/w selector is first expanded in
the fixed PRODUCT residue-character basis, with its actual total mass.
This creates own-column finite characters covered by (13), retaining
their full Fourier reconstruction. Forbidden primitive values stay zero
in the original full sum. The common d scalar retains rho(d)^2,
Gamma-square and the general chi(d)psi(d), none set to1.

Growing other-column/s/k raw deletions are NOT hidden in kappa: they are
opened by the exact row Q transfer below. Finite k/w overlap can make
kappa(t)=0, but (8)--(13) never divide that value and allow overlapping
raw F/t directly. No primitive-S value, source class or angular mean is
dropped, restored or centered.

This match depends on the accepted fixed-family factor list and exact
normalizations, not an assertion that any arbitrary bounded
multiplicative function is periodic. Such an arbitrary function would
NOT be covered by (13).

## 6. ALL original finite k and ALL common-long divisors

Keep the ORIGINAL finiteK and exact capacity; impose NO new k or d cutoff.
After the independently reviewed NEW entire-prefix localization,
 Np,Nr<=Z=D^(1/8).
Open only the original long-long coprimality with v=d*a,z=d*b, ALL SF
common divisors d. The residual a,b MAY overlap; d is not necessarily
greatest common divisor. On nonzero assignments d<=2D and
t=p*d*k is SF (all original raw p/k/d zeros retained).

Fix opposite r,b BEFORE the left sum. The crossmask(p,b)=1 belongs in
the p/level coefficient; do not insert b into the left a-deletion Q.
The latter remains
 Q=rad_good(p*r*d*k*s*w).
Every surviving h in the exact opening is coprime to t and divides
rad_good(r*s*w); coefficient includes the literal (Nh)^(-1/2).

With T=D/(Np Nd), apply (13) at residual scale T/Nh and frequency h*t:
 (Nh)^(-1/2)(T/Nh)^(1/4)N(ht)^(3/8)
     =T^(1/4)(Nt)^(3/8)(Nh)^(-3/8).                    (14)
Only terms T/Nh>=1/2 are active; units/empty sums use the literal rule.
No large-level/short-length restriction is needed because (13) has its
trivial fallback. Norm product(T/Nh)N(ht)=D Nk remains exact.

Pointwise actual prefix coefficients are D^eps. Sum p<=Z using the
positive ideal exponent -3/4+3/8=-3/8:
 C_left << V1(W)(DX)^eps D^(1/4)
                   (Nd)^(1/8)(Nk)^(3/8) Z^(5/8),       (15)
with a small additional (Nd Nk)^eps allocation from divisor/product
losses. For global control, on support
 NQ<=C (Np Nr)(Nd)(Nk)(Ns)(Nw)
      <=C D Z^2 V Nk.
No upper-polynomial assumption onK is needed: allocate its Nk^eps
explicitly to the convergent k majorant. Other material factors are
polynomial inD,X,A1 and fixed data. d<=2D handles d^eps.

The right coefficient sum, INCLUDING its prefix harmonic sum, is
 <=B D^eps sqrt(D/Nd), with the same unit/empty rule for subunit lengths.
Original normalization is A1/(D Nd) ONCE. Hence the remaining small-
whole-prefix model satisfies
 << B V1(W)(DXA1)^eps A1 V D^(-1/4) Z^(5/8)
   sum_(d SF,Nd<=2D)(Nd)^(-11/8+eps)
   sum_(k SF,Nk<=K)(Nk)^(-13/8+eps).                   (16)

Both positive majorants converge after allocating eps<3/8 andeps<5/8.
Every exact sum remains finite in the identity; no Euler completion
changes the actual model. No mu(d) or k cancellation is claimed. At
A1~D^(3/4),X=D^(3/8),V=.5D^(1/16),Z=D^(1/8), (16) has
                    NORMALIZED power41/64.            (17)

This new derivation does NOT invoke or rerun the accepted large-k or
large-d tail as a new solution; it bounds ALL original k and d directly,
conditional only on final acceptance of the new ramified interface.
The exact s/w support and every originalrho/source/primitiveS mean
remain; count actual s byO(V) only LAST.

For optional original unequal norms, first use the unprojected bound,
then subtract THIS SAME all-d auxiliary equal-norm component. There are
O(D^(1+eps)) ordered equal-norm ideal pairs, with distinct conjugates
retained, D^eps HB/divisor assignment count, pairweightO(B^2/D), one
originalA1/D and finite k majorant Nk^-2. The normalized cost is
O(B^2 A1V D^(-1+eps)), covered. No primitive root is assigned to an
overlapping auxiliary product.

## 7. Exact DIRECT top-prefix boundary

The actual object is the finite primitive-dual top prefix P_X[A_U,A_U]
of DIRECT-v2, with exact w/s set, allrho, ORIGINAL finiteK/capacity, not
the full infinite dual kernel or all original h1 rows. DIRECT's Bessel
and A_U-to-A_Y errors are previously proved target-sized at Y=min(U,D^1/8).
The new whole-prefix tail is target-sized at Z=D^1/8. Existing balanced
residual TypeII pieces are target-small. The remaining full small-prefix
piece is (16), with all k/d included, once its new ramified gate is accepted.

Therefore final independent acceptance of the new interface would give
 |P_X[A_U,A_U]| <<_(nu,S,source/ray,W,eps) H (D X A1)^eps,
 A1 comparable toH=D^(3/4), X=D^(3/8),
for this DECLARED original UNWEIGHTED PURE two-pivot prefix. Its raw
numerator has one extraD. This is a scoped finite dual-prefix theorem,
not the whole original h1 signed estimate, global bound, arbitrary
row-weight assertion, fixed-profile sharpness or determinant theorem.

The old unconstructed ramified-cusp step has been replaced by known
integral cusps and explicit coefficient norms; if any exact actual-family
or angular transform gate fails, (3)--(5) remain proved coefficient
survivors while (13),(16) and the DIRECT conclusion must be withheld.
No source/body cache is published. Whole signed13/12/global unsigned9/8,
other dual-frequency complements, mixed/neighboring blocks, target
assembly, independent determinant/zero-location and separate
Dirichlet/Hecke/Dedekind/elliptic/generalArtin/analytic-categoryLean/GRH
obligations remain OPEN. No zero/positivity/Artin-holomorphy premise or
proof schedule is assumed.
