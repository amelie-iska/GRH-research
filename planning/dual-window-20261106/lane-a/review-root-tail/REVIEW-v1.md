# Independent mathematical review of the sharp-row dual tail

PASS on governing SHARP_ROW_DUAL_TAIL-v2.md, SHA256 bb2c8277cdcd7673bbca87470bd0d7047cc9eb6bdeace9a1d8423fa9acf31ae1. I read the complete v1 argument, rederived the derivative/Bessel/tail calculations independently, and inspected the exact v1-to-v2 difference. This is a new all-dual high-tail certificate for the actual finite row-divisor expansion. It does not bound the retained signed main or improve the current global9/8/scoped13/12 powers.

## Exact scope and derivative constants

The family is the accepted remaining two-pivot block v3=v4=v5=v6=O, with u0 unit/S-supported and no hidden extra frozen good factors. Original A_U, fixed nu/S, common complex COLUMN W, all raw zeros, primitive conductors/root numbers and exact capacity remain. The auxiliary ROW interpolant is the factor-FOUR construction, with the specific bounded sigmoid; it is not W.

For a nonempty integer fibre b>=a, the two ramps are disjoint. On the rising ramp the falling factor is identically one, and conversely. After dy=dt/(4A1), their derivative contributions give exactly 2(4A1)^(r-1)Lambda_r. The ramps lie inside the positive support, so no integral is lost at zero. Monotonicity gives Lambda_1=1 and TV(G)=2.

On 0<t<=1/2 the logarithmic sigmoid exponent g=-1/t+1/(1-t) satisfies sigma<=e^2 exp(-1/t), g'<=2t^-2 and |g''|<=4t^-3. Differentiating sigma gives |sigma''|<=sigma[(g')^2+|g''|]. The two integrals are 10e^-2 and 3e^-2; their half-interval contribution is at most52. Reflection doubles it to Lambda_2<=104. No numerical quadrature or derivative-uniformity assumption is used.

## Bessel integration and all-ideal tail

Differentiating y^(r/2)J_r(2sqrt(Xy/C)) gives sqrt(X/C)y^((r-1)/2)J_(r-1). Repeated integration by parts therefore has coefficient (-1)^r C^(r/2-1/2)X^-r/2. All endpoint terms vanish by smooth compact support.

The angular J_r bound also checks with the stated constant. Remove stationary arcs of total length4delta, delta=t^-1/2. Each complementary arc has boundary-plus-reciprocal-phase-derivative cost at most4/(t sin delta), and amplitude derivative cost at most r*pi/(t sin delta). Two arcs, division by2pi and sin delta>=2delta/pi give (r*pi/2+2)t^-1/2; removed arcs add 2/pi times t^-1/2. For r=2 this is less than6t^-1/2.

For X>=1, every argument on supp(G) is above one. Combining the Bessel bound with the exact derivative norm gives the displayed T_r and exponent s_r=r/2+1/4. For r=2, 8A1*104 times6/sqrt2 gives exactly T=4992/sqrt2*C^(3/4)*(5/2)^(3/4) and |dotG(X)|<=T A1 X^-5/4.

The finite k convention is the original pre-S cutoff K=sqrt(b/Nell). Empty fibres or Nell>b are zero. For Z>=max(1,K^2/x), with x=A1/(Nell Ne F), every Ny>Z, Nk<=K has transform argument>1. The two all-ideal estimates are 10Z^-1/4 for the y tail and 2K^(3/2) for the k half-power sum. Thus the error is 20T A1 x^-5/4 K^(3/2)Z^-1/4. The y sum is over ALL nonzero integral ideals, including S-supported factors, so no h>O component is omitted.

Multiplying by the exact primitive Poisson prefactor A1/(Nell Ne sqrt(F)) produces

    20T A1^(3/4)b^(3/4) Nell^-1/2 Ne^(1/4) F^(3/4) Z^-1/4.

This confirms every normalization power in (4.3). Since F<=4F_S,max D^2 and b<2A1, summing original column pairs contributes D^2 and division by D contributes D^-1. Summing v2 contributes A2. The result is D^(5/2) A2 A1^(3/2)Z^-1/4, with coefficient and ell-divisor losses retained as (D A2)^epsilon. That last general-parameter qualification was my sole v1 finding and is explicit in v2; absorbing A2^epsilon into D^epsilon requires the additional stated polynomial relation.

## Higher order and cutoff powers

For s=s_r>1, the same count gives the inner constant 4s/(s-1) times T_r A1^(r-1)x^-s K^(2s-1)Z^(1-s). After the primitive prefactor it is proportional to

    A1^(r-s)b^(s-1/2) Nell^-1/2 Ne^(s-1) F^(s-1/2) Z^(1-s).

Use b<2A1, r-1/2=2s-1, original pair count and normalization to obtain D^(2s) A2 A1^(2s-1)Z^(1-s), with full (D A2)^epsilon. This rederives (5.1).

At A1=D^a,A2=D^b,H=D^(3/4), the sufficient power cutoff is

    z >= [2s+b+(2s-1)a-3/4]/(s-1)
       = 2+2a+(5/4+a+b)/(s-1),

up to the stated fixed constants and epsilon factors. At r=2 this is23/2 for the pure endpoint and61/6 for the mixed witness. Higher FIXED r approach2+2a from above, hence7/2 and17/6 respectively; one cannot let r grow with D while discarding Lambda_r. These are sufficient upper-error cutoffs, not supports or necessary tail sizes.

## Accepted conclusion and limits

The note supplies a valid uniform summable high-frequency tail for the exact sharp-row interpolant with its true growing derivative cost. Absolute values are used only on the omitted-error certificate. Primitive additive/root normalization, all S/union masks and actual coefficients remain. No positivity or arbitrary weighted-row theorem is used.

The retained coherent intermediate range remains unbounded by this argument. No target gain, nonvanishing, energy lower bound, determinant/zero-location, Lean or GRH conclusion follows. Author numerical controls were neither rerun nor used as a substitute for the derivation. No mathematical table, build, browser, environment, auth or publication operation was run. The companion source pins and receipt bind current bytes and all twelve protected HEAD/index states.
