# Actual sharp-row dual truncation with explicit derivative cost — v2

Research-only root lane, 6 November 2026 UTC. This is new work after the verified physical-sieve release. It does not alter that release, any canonical book source, the original common column profile, or an accepted earlier numerical trace. Its acceptance target is an honest uniform summable tail for the EXACT sharp-capacity interpolant, followed by an explicit test of whether it can close the proposed low-window attack. It is not the missing signed estimate.

## 1. Fixed inputs and actual scope

Use DRAFT-v8.md (cba96d347cd880cdead3a330ce5e39969b1950c049df1750f6444ce68a0d4ff7), together with the REQUIRED two-pivot scope addendum 5f576c22742d894536c7e8a843d29e3117be9c1e3534d5a5415aa8e130b80b11, and DUAL_UNIT_K_LEMMA-v3.md (abeee9010e2b500565ce857f930650c277999fecc2d6cc64b59e9b0ab1973744). The field is Q(omega), C=3/(4 pi^2). Only the displayed remaining two-pivot original family is used: v3=v4=v5=v6=O; u0 is a fixed literal unit/S-supported factor with no good-prime support. The original columns m,n are good squarefree IDEALS in D<=Nm,Nn<=2D, coprime to each other, not a generic conductor family. Their coefficients remain

 c_m=A_U(m) nu(m) (u0/m)_6 W(Nm/D),

with the actual ternary A_U, fixed nu/S, ONE common possibly complex W, every raw collision zero, and separate equal-norm/conjugate ideals.

For fixed v2 define a=ceil(A1) and b=min(ceil(2A1)-1,floor(H/(Nu0 Nv2^2))). Empty b<a is zero. A1>=1. FIX the same auxiliary sigmoid as the accepted v3: sigma(t)=exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) on 0<t<1, extended by 0/1. Importantly the v8 interpolant has scale FOUR:

 G(y)=sigma(4(A1 y-a+1/2)) sigma(4(b+1/2-A1 y)).

Its integer-node values are exactly the original sharp row/capacity weights. It is NOT the common column profile W. Its support lies in [1/2,5/2], 0<=G<=1. The two transition intervals are disjoint, since b>=a are integers. On each interval only one sigmoid factor varies, while the other is exactly1.

## 2. Explicit L1 derivative control of this interpolant

Let Lambda_r=integral_0^1 |sigma^(r)(t)|dt, for integer r>=1. Each is a fixed finite constant, independent of A1,D,H, the conductor and capacity endpoint. The two disjoint ramps give exactly

 ||G^(r)||_1 =2(4A1)^(r-1) Lambda_r.                         (2.1)

In particular TV(G)=2 because Lambda_1=1. For a concrete second-derivative bound, Lambda_2<=104. Proof: on 0<t<=1/2 put g(t)=-1/t+1/(1-t), so sigma=(1+exp(-g))^-1. Then sigma<=e^2 exp(-1/t), g'<=2t^-2, |g''|<=4t^-3. Hence

 |sigma''(t)|<=4e^2 exp(-1/t)(t^-4+t^-3).

The two integrals on (0,1/2] equal 10e^-2 and 3e^-2, by u=1/t. This half contributes at most52. The symmetry sigma(1-t)=1-sigma(t) doubles it. The bound is deliberately loose and explicit, not a numerical fit or a claim that derivatives are scale-uniform.

## 3. Repeated Bessel integration by parts

Use the already source-matched transform

 dotG(X)=C^-1/2 integral G(y) J_0(2sqrt(Xy/C))dy.

For every integer r>=1 and X>0,

 dotG(X)=(-1)^r C^(r/2-1/2) X^-r/2
             integral G^(r)(y) y^(r/2) J_r(2sqrt(Xy/C))dy.    (3.1)

Indeed d/dy[y^(r/2)J_r(2sqrt(Xy/C))]
 =sqrt(X/C)y^((r-1)/2)J_(r-1)(2sqrt(Xy/C)).
It follows termwise from the convergent Bessel series. Repeated integration by parts has no endpoint term because G is smooth compactly supported.

For completeness an elementary bound is

 |J_r(t)| <= (r*pi/2+2+2/pi)t^-1/2,  t>=1.                  (3.2)

Write J_r as the angular Fourier coefficient of exp(it cos theta). Delete intervals of total length4 delta about the two stationary points, delta=t^-1/2<=1. Their contribution after dividing by2pi is at most2delta/pi. On each of the two other arcs integrate by parts using phase derivative -t sin theta. The boundary terms and derivative of 1/sin contribute at most4/(t sin delta) per arc; derivative of exp(-ir theta) contributes at most r*pi/(t sin delta) per arc. Since sin delta>=2delta/pi, the remaining contribution is at most(r*pi/2+2)t^-1/2. This proves (3.2). In particular |J_2(t)|<=6t^-1/2.

For X>=1 the Bessel argument on supp G is >1. Combining (2.1), (3.1), (3.2) gives, for every fixed r,

 |dotG(X)| <= T_r A1^(r-1) X^(-r/2-1/4),                  (3.3)

where one explicit choice is

 T_r=2*4^(r-1)*(r*pi/2+2+2/pi)/sqrt2
       *C^(r/2-1/4)*(5/2)^(r/2-1/4)*Lambda_r.

For r=2 it is enough to take the fully explicit

 T=4992/sqrt2 * C^(3/4)*(5/2)^(3/4),

so |dotG(X)|<=T A1 X^-5/4. Neither T nor T_r is claimed optimal. The actual sharp scale in (3.3) is sqrt(X) comparable to A1; replacing it by a fixed-smooth scale1 would erase the derivative cost.

## 4. A complete finite-k, all-dual-ideal tail

Fix actual m,n,v2,ell|v2,e,rho and the actual primitive eta, F=Nf. Keep its primitive root number and all fixed coefficients outside the following sum. If Nell>b the term is zero. Otherwise use EXACTLY the natural pre-S-removal cutoff

 K=sqrt(b/Nell)>=1,  x=A1/(Nell Ne F),
 Tdel=S union supp(mn v2 ell).

No k beyond this cutoff is inserted, and deleted primes are not restored after any power-conductor drop. Define

 R_>Z=sum_(Ny>Z) conjugate(eta(y))
          sum_(Nk<=K,(k,Tdel)=1)
           mu(k)eta(k)^2/Nk^2 dotG(x Ny/Nk^2).              (4.1)

The y here ranges over ALL nonzero integral ideals. Thus it includes the S-supported factor h and good factor z of y=h z; it is not a good-z-only truncation discarding h>1. For

 Z>=max(1,K^2/x)=max(1,b Ne F/A1),

equation (3.3), r=2, proves

 |R_>Z| <=20 T A1 x^-5/4 K^(3/2) Z^-1/4.                  (4.2)

Proof: the elementary all-ideal count A_K(t)<=2t gives
 sum_(Ny>Z) Ny^-5/4<=10 Z^-1/4
and
 sum_(Nk<=K) Nk^(1/2)<=2K^(3/2).
All character/raw-mask values have modulus<=1. The k sum is finite; r=2 proves absolute convergence of the full tail, so no unjustified interchange on a conditionally convergent Mellin line occurs. The exact signed outer kernel remains unchanged; absolute values are used here ONLY to certify the omitted high-frequency error.

The actual prefactor is A1/(Nell Ne sqrt(F)). Multiplying (4.2), substituting K and x, gives its concrete high-tail error at most

 20 T A1^(3/4) b^(3/4)
        Nell^-1/2 Ne^(1/4) F^(3/4) Z^-1/4.                (4.3)

Multiply this by the absolute value of the actual c_m conjugate(c_n), h_rho, primitive root/local raw factors, and sum over the ORIGINAL finite m,n,v2,ell,e,rho/class terms for a finite explicit certificate. A vanishing raw factor still contributes zero. Formula (4.3), not a generic character family, is the precise error accounting.

Uniformly F<=4 F_S,max D^2, b<2A1, ell|v2, and with the original coefficient bound |A_U(m)|<<epsilon D^epsilon (uniform in U), summing these certification errors yields

 |S1^AA(high tail >Z)|
   <<_(S,nu,epsilon) B^2 (D A2)^epsilon D^(5/2)
                            A2 A1^(3/2) Z^-1/4,          (4.4)

provided Z exceeds the finite maximum threshold above. Here S1 is NORMALIZED by1/D. Fixed finite ray coefficients and S-deletions are in the implied constant; no additional varying-conductor hypothesis is hidden. The (D A2)^epsilon loss explicitly retains the ell|v2 divisor bound. It can be absorbed into a renamed D^epsilon only after stating A2<=D^C, as in the original critical capacity range. One may instead use the exact finite sum in (4.3) and actual coefficient norms, without this coarsening. No positive operator input or arbitrary-weight extension is needed for this error-only triangle.

## 5. General derivative order and the failed low-window attack

Let s_r=r/2+1/4>1 (r>=2). The same calculation gives

 |S1^AA(high tail >Z)|
   <<_(r,S,nu,epsilon) B^2 (D A2)^epsilon D^(2s_r)
                   A2 A1^(2s_r-1) Z^(1-s_r),             (5.1)

with explicit fixed-step constants obtainable from T_r and the elementary ideal count. This is a valid uniform sharp-interpolant truncation bound, not a new estimate for the retained signed main.

At H=D^(3/4), write A1=D^a,A2=D^b, a+2b=3/4, suppressing fixed feasible capacity constants and epsilon. With r=2, target-size normalized truncation error <=H is certified at cutoff exponent

 log_D Z >=10+6a+4b-4*(3/4).

This is23/2 in the pure endpoint(a,b)=(3/4,0), and61/6 at the mixed witness(5/12,1/6). Higher fixed r can approach the sufficient threshold log_D Z>2+2a (7/2 pure,17/6 mixed), with r-dependent constants. These are sufficient HIGH-TAIL cutoffs, not support statements or necessary lower bounds for the actual tail.

In contrast the separate proposed low-window k-Euler approximation has a target-sized certification budget only for a much smaller window (lane B derives its actual conditions). A huge coherent intermediate range remains. One cannot use the tiny low-frequency model for the entire kernel, remove the complement, or pretend sharp-capacity derivatives cost no power.

Attempted closure therefore FAILS: this result makes a finite truncation of the actual full kernel reviewable with explicit error, but does not bound the retained root/Euler/Bessel-weighted signed intermediate/main sum. Unit modes, S-supported modes, means/equal-norm fibres and all nonunit frequencies remain. The current global9/8 and scoped two-pivot signed13/12 are unchanged. No target-power gain, lower bound, determinant/zero-location, Lean or GRH conclusion follows. No prior table/trace/publication/build/auth check was rerun.

Next exact research object: the joint m,n,v2,ell,k,rho Bessel-character partial sums BETWEEN the low window and a justified high-tail cutoff, before per-conductor or per-column absolute Cauchy, retaining original fixed common W and explicit seminorms, all raw zeros and every capacity/S/ray/squarefree/conductor uniformity.
