# A classical smoothed-circle error in the actual sixth-part mean

Research-only v1, 6 November 2026. This is a self-contained proof of the classical planar disk discrepancy of order R^(2/3), followed by its application to the accepted actual finite primitive kernel. No priority is claimed for the lattice bound. The new surviving statement is a sharper ERROR for the same retained coherent mean; the mean itself is not estimated.

This note is outside the frozen coherent-book release, its Main selection, canonical sources and browser data. Whole signed13/12/global9/8, determinant/zero-location, Lean and GRH obligations are unchanged.

## 1. Actual statement and retained main

Use the accepted COHERENT_SIXTH_PART_RAY_MEAN-v1, SHA4315f8d2fb10b5c0a5f91fb8ae4c1e3271582fb27bd2bc5ee5d44912e81621fd, with independent gate d81ca8a1c90098d7a64a784599aacfdd81d7cd5e099fa6ec31eeb02e2342fa04. Its exact primitive kernel, conductor and normalization are inputs; their statements are repeated here to specify the new application.

Work in O=Z[omega], embedded in C, with fixed finite S containing the primes over2,3 and the original source/ray exclusions. Original columns are the COMPLETE good squarefree ideal annulus D<=Nm<=2D, D>1. Keep the actual double short-divisor coefficient A_U, fixed finite-order nu, fixed unit/S-supported u0 with no good support, and ONE possibly complex common W on[1,2], zero at endpoints. Put
c_m=A_U(m)nu(m)R_m(u0)W(Nm/D), B=||W||infinity.
Only the original UNWEIGHTED two-pivot rows are asserted: v3=v4=v5=v6=O, actual good squarefree/coprime v1,v2, every literal/ray restriction and exact capacity Nu0 Nv1(Nv2)^2<=H. A1,A2>=1 and R=A1 A2.

On original coprime squarefree columns let q=mn. For each original source-class/ray component,
eta=xi_m bar(xi_n) sigma, F=Nf_S Nm Nn,
L_e=A1/[(Nk)^2 Nl Ne],
where l|v2, Nl<=b(v2), k is good squarefree, (k,v2)=1 and Nk<=sqrt(b(v2)/Nl), and e|P_S. All finite cutoffs, primitive S zeros, original phases and signs are retained.

Let C_outer denote exactly
c_m bar(c_n) R_m(v2^2)bar(R_n(v2^2)) h_(ABrho)(v2)
 times mu(k)mu(l)mu(e) eta(k^2 l e) epsilon(eta) L_e/sqrt(F).
The exact dual transform is
dotG(x)=C0^(-1/2) integral G(v) J0(2 sqrt(xv/C0)) dv,
C0=3/(4pi^2),
for the ACTUAL sharp-row nodal interpolant G=G_v2: 0<=G<=1, support in[1/2,5/2]. It is not the column profile W.

Every dual ideal uniquely decomposes as y=h r s^6, with h S-supported, r GOOD sixth-power-free and s GOOD, allowing overlap(r,s). All S exponents stay in h. On good s the TOTAL finite-order source identity gives
bar(eta(s^6))=psi(s)1_((s,q)=1), psi=bar(rho)^6.
Only psi is the fixed type-zero ray character here; individual xi need not have finite order. No k|s or additional primal mask is introduced.

For X,V>=1 let P_V(X) be the exact Ny<=X primitive prefix restricted to V<Ns<=2V. Put
b_hr=min(2V,(X/(Nh Nr))^(1/6)), a_hr=L_e Nh Nr/F.
Empty b_hr<=V contributes zero. Define the SAME coherent main as the accepted note:
M_V(X)=sum_outer C_outer
 sum_(h S-supported,r good6free,b_hr>V)
 bar(eta(h))bar(eta(r)) delta_psi kappa_S g(q)
 integral_V^b_hr dotG(a_hr t^6)dt,                         (1)
where
delta_psi=1 if psi is principal on good ideals and0 otherwise,
kappa_S=pi/(3sqrt(3)) product_(p in S)(1-1/Np),
g(q)=product_(p|q)(1-1/Np).

The new estimate is
|P_V(X)-M_V(X)|/D
 <<_(S,ray,step,epsilon)
 B^2(D X A2)^epsilon R X V^(-17/3)
                       [1+sqrt(A1 X/D^2)].              (2)
It also holds after first projecting the ORIGINAL column pairs onto Nm!=Nn. All component/root/r/k/l/e/h/capacity means in(1) stay signed and coupled. Formula(2) is not a bound for(1).

## 2. An elementary angular estimate

Define, for real u,
J1(u)=(1/(2pi i)) integral_0^(2pi) cos(theta) exp(iu cos(theta))dtheta.
This convention gives J0'=-J1 by differentiation of the angular J0 integral. Directly |J1(u)|<=1. For u>=4 set h=u^(-1/2)<=1/2. The stationary arcs
[0,h], [pi-h,pi+h], [2pi-h,2pi]
have total length4h, so their unnormalized integral is bounded by4h.

On each complementary interval integrate by parts using
d exp(iu cos(theta))/dtheta = -iu sin(theta) exp(iu cos(theta)).
The amplitude divided by sin(theta) is cot(theta), whose derivative is -csc(theta)^2. The boundary and derivative terms on [h,pi-h] are at most
2cot(h)/u + (1/u) integral_h^(pi-h)csc(theta)^2dtheta
=4cot(h)/u<=4/(u h).
The other interval has the same bound. Thus the complete integral is at most
4h+8/(u h)=12u^(-1/2).
After division by2pi this is less than2u^(-1/2). The crude bound covers0<u<4, hence
|J1(u)|<=2u^(-1/2), u>0.                                 (3)
This is a proved first-derivative angular argument, not an invoked stationary-phase theorem.

For the Euclidean closed disk B_T and Fourier convention
hatf(xi)=integral_R2 f(x) exp(-2pi i<x,xi>)dx,
a boundary integration in the xi direction gives, for xi!=0,
hat(1_B_T)(xi)=T J1(2pi T|xi|)/|xi|.
One obtains the formula by writing the boundary point as T(cos(theta),sin(theta)); the outward normal contributes cos(theta), and the signs agree because J1 is odd. Therefore(3) gives the uniform bound
|hat(1_B_T)(xi)|<=C T^(1/2)|xi|^(-3/2).                   (4)
At xi=0 the transform is pi T^2. There is no complex-frequency or varying-conductor assertion.

## 3. Fixed translated lattices: smoothing and Poisson

Let Lambda be a fixed full rank lattice in R2, with covolume v_Lambda and dual Lambda*. Translation z is arbitrary. Choose once a nonnegative smooth mollifier phi supported in the unit disk and of total integral1; for example normalize exp(-1/(1-|x|^2)) inside that disk and extend by0. Put phi_delta(x)=delta^(-2)phi(x/delta).

For every M, Fourier integration by parts gives
|hatphi(delta xi)|<=C_(phi,M)(1+delta|xi|)^(-M).
For example apply (1-Delta)^2 to phi to obtain M=4. All its constants are fixed.

For R>=1 choose delta=R^(-1/3)/2, so0<delta<=R/2 and delta<=1. Pointwise, INCLUDING disk boundary points,
1_B_(R-delta)*phi_delta <= 1_B_R <= 1_B_(R+delta)*phi_delta.  (5)
The upper convolution equals1 on B_R because every translated mollifier point remains in B_(R+delta). The lower convolution is0 outside B_R. These are unweighted real inequalities; no complex character sum is being sandwiched.

For smooth compact f, periodize over Lambda. Its Fourier coefficient at xi in Lambda* is hatf(xi)/v_Lambda, obtained by integrating over one fundamental cell and translating. Smoothness gives an absolutely and uniformly convergent Fourier series by integration by parts in lattice coordinates. Evaluating it at z proves
sum_(lambda in Lambda+z) f(lambda)
 =v_Lambda^(-1) sum_(xi in Lambda*) exp(2pi i<xi,z>)hatf(xi). (6)
This supplies the needed Poisson identity from ordinary periodic Fourier series. In our application f=1_B_T*phi_delta is smooth compact, so no sharp-indicator Poisson limit is assumed.

A disjoint-small-ball count gives
#(Lambda* intersect B_L)<=C_Lambda(1+L^2).
The shortest nonzero dual vector has fixed positive length. Dyadic shells below delta^(-1) yield
sum_(0<|xi|<=delta^(-1)) |xi|^(-3/2) <<_Lambda delta^(-1/2).
For shells |xi|~2^j/delta beyond that scale, the bound with M=4 gives
sum |xi|^(-3/2)(1+delta|xi|)^(-4)
 <<_Lambda delta^(-1/2) sum_(j>=0)2^(-7j/2).
Consequently the whole nonzero dual sum is O_Lambda(delta^(-1/2)). Equations(4),(6) imply, uniformly in translation,
sum_(lambda in Lambda+z)(1_B_T*phi_delta)(lambda)
 =pi T^2/v_Lambda+O_(Lambda,phi)(T^(1/2)delta^(-1/2)).     (7)

Apply(7) at T=R-delta and R+delta. They are comparable with R. The zero-mode areas differ from pi R^2 by O(R delta+delta^2). The two sides of(5) therefore prove
#((Lambda+z) intersect B_R)
 =pi R^2/v_Lambda
  +O_Lambda(R delta+delta^2+R^(1/2)delta^(-1/2))
 =pi R^2/v_Lambda+O_Lambda(R^(2/3)), R>=1.                (8)

Translation changes only unit-modulus phases in(6), so it does not affect the constant. The assertion(8) is NOT extended to arbitrarily small R for arbitrary translated lattices; the subunit IDEAL range is handled separately below.

## 4. Fixed ideal ray characters, with full S deletion

Choose a fixed ideal modulus c supported on S which both induces psi and includes every prime of S. It is nonunit since S contains the primes over2,3. On generators coprime to c, the type-zero ideal character is a periodic finite character theta modulo c, trivial on all six units. Extend it by0 on nonunits. Thus theta(0)=0.

Every nonzero integral ideal has exactly six generators, all of the same norm. For t>=1, apply(8), with R=sqrt(t), to each individual residue coset modulo the lattice c. Only AFTER these unweighted estimates multiply by theta(a) and sum the finitely many cosets. The principal finite-character sum is phi_K(c), and a nonprincipal character sums to0 by finite group orthogonality. The lattice c has covolume Nc sqrt(3)/2, while
phi_K(c)=Nc product_(p in S)(1-1/Np).
Dividing by6 proves
N_(psi,1)(t)
 :=sum_(s good,Ns<=t)psi(s)
 =delta_psi kappa_S t+O_(S,psi)(t^(1/3)), t>=1.           (9)

A nonprincipal psi on good ideals really gives a nontrivial finite theta: every unit residue has a nonzero generator representative coprime to c, so if theta were trivial the ideal character would be principal. No cancellation estimate for a varying conductor has entered.

For0<t<1 there are no nonzero integral ideals, since ideal norms are positive integers. In the principal case its error is -kappa_S t, and t<=t^(1/3); in the nonprincipal case both terms vanish. At t=0 everything is0. Thus(9) holds for ALL real t>=0 after enlarging the fixed constant. This small-t conclusion uses integrality, not a false small-radius uniform translated-coset estimate.

## 5. ALL ideal divisors of q, including Nd>t

For any good squarefree q, the exact identity is
N_(psi,q)(t)
 =sum_(d|q)mu(d)psi(d)N_(psi,1)(t/Nd).                   (10)
The sum is over ideal divisors, distinguishing split conjugate primes and allowing inert prime-ideal norms. There is no rational-squarefree replacement.

For principal psi, the leading sum in(10) is
kappa_S t sum_(d|q)mu(d)/Nd=kappa_S g(q)t.
For a nonprincipal psi it is0. Taking only the errors from(9) yields
|E_(psi,q)(t)|
 <=C_(S,psi)t^(1/3) sum_(d|q)(Nd)^(-1/3)
 =C_(S,psi)t^(1/3) product_(p|q)(1+(Np)^(-1/3)).          (11)
EVERY divisor remains, including Nd>t and Nd>2V. For such subunit arguments, their ideal count is0 but their principal leading term is not0; it is included in the error in(11). Omitting those divisors would alter g(q).

On the actual support Nq<=4D^2. For any epsilon, the finitely many small prime ideals are absorbed into a fixed constant, while1+P^(-1/3)<=P^epsilon for sufficiently large P. Rescaling epsilon gives
product_(p|q)(1+(Np)^(-1/3))<<_epsilon D^epsilon.           (12)
This is a finite elementary divisor bound, not a prime ideal theorem, Mertens assertion, zero-free estimate or averaged conductor theorem.

## 6. Replacing the actual s sum and retaining every mean

For each fixed outer parameter and h,r the exact inner sum is
sum_(s good,V<Ns<=b_hr,(s,q)=1) psi(s)w(Ns),
w(t)=dotG(a_hr t^6).
Closed counting prefixes at BOTH endpoints give its difference from the principal integral in(1) as
w(b_hr)E(b_hr)-w(V)E(V)-integral_V^b_hr E(t)w'(t)dt.       (13)
Thus norm ties preserve the original open-lower/closed-upper convention exactly.

The Bessel transform and |J0|,|J1|<=1 give
||dotG||infinity<=2 C0^(-1/2),
|x dotG'(x)|<=2sqrt(5/2) C0^(-1)sqrt(x).
These follow directly from the compact v integral, with no derivative of G. Because b_hr<=2V and
a_hr t^6<=L_e X/F<=A1 X/D^2,
the variation of w on[V,b_hr] is at most a fixed constant times sqrt(A1 X/D^2). Combining(11)--(13), the per-h,r error is
<<_epsilon D^epsilon V^(1/3)[1+sqrt(A1 X/D^2)].           (14)

For completeness, the outer budget is unchanged from the accepted note. The complete original annulus has O(D) ideals; its two A_U coefficients are bounded for the ERROR by3^omega<<D^epsilon, and its two W factors byB^2. Other raw phases have modulus at most1, including their zeros. L_e/sqrt(F)<=A1/[D(Nk)^2 Nl Ne]. The SINGLE final normalization byD and the two annular counts therefore leave A1. Only in the error, sum the finite k weights by zeta_K(2), the fixed e divisors by a fixed constant and l|v2 by A2^epsilon. The actual unweighted v2 family has O(A2) ideals with fixed literal/ray multiplicity.

Finally b_hr>V implies Nh Nr<X/V^6. Counting good sixth-free r by all ideals, with no r below norm1, gives
#(h,r) << X V^(-6) sum_(h S-supported)1/Nh <<_S X V^(-6). (15)
All S-supported h are retained, not just h=O; their geometric sum is finite for fixed S. Multiplying(14),(15) and the outer budget proves(2), with the several subpower losses absorbed into the stated arbitrary epsilon.

All actual h,r,k and dual sums are finite at fixed X. Full primitive S zeros, r/s overlaps, exact q deletion, literal/ray restrictions and capacity remain. No full-root factorization, coefficient multiplicativity or conductorwise absolute bound is used for the principal mean. Restricting first to original unequal-norm pairs only reduces the ERROR count and leaves the same signed replacement identity on that projection.

## 7. Powers and the surviving obstruction

At V=X^(1/6)/2 with X>=64, the ERROR in(2) is
<< B^2(D X A2)^epsilon R X^(1/18)[1+sqrt(A1 X/D^2)].      (16)
The factor2^(17/3) is absolute. Empty sectors remain allowed; no existence of a good s in each top band is assumed.

At the pure critical scales R=A1=H=D^(3/4), A2=1, X=D^(3/8), the bracket is bounded and the error exponent is
3/4+(3/8)/18=37/48>3/4.
The prior square-root raycount error was25/32; the original absolute count was13/16. These are upper error exponents, not numerical observations or lower bounds. At the stated mixed scales R=D^(7/12),A1=D^(5/12),A2=D^(1/6), the new error power is29/48, again only an error statement.

The retained principal mean(1) is unchanged. Under its old absolute majorant it can still cost R X^(1/6); no cancellation of its root/column/r/k means is shown here. Nonprincipal psi branches have no counting main by fixed finite-group orthogonality, but no branch is discarded and no assertion that a nonprincipal branch occurs is required. In particular the same-class/rho1 principal mean survives.

The result is a classical lattice-count APPLICATION to a genuinely coherent arithmetic replacement, not a new lattice discrepancy theorem, a full-family norm bound, an impossibility theorem or a whole signed saving. The unresolved next step remains an estimate of(1), coherently across its actual root phases, orientations, r/k sums and other sectors.
