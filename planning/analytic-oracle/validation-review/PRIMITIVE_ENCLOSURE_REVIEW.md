# Independent interval-oracle primitive review

Remote-only 2026-11-04. This is an adversarial proof review, not full Lean
formalization. The standard primitive Dirichlet theta/Mellin identity is an
explicit external analytic input. No assertion about zero locations occurs.

## Machin pi without a floating endpoint

For 0<x<1, the N-term alternating arctangent sum and the sum plus its signed
next term enclose atan(x). The signed next term is (-1)^N*x^(2N+1)/(2N+1).
Apply interval scaling to pi=16*atan(1/5)-4*atan(1/239), reversing the second
interval under its negative multiplier. For the identity, tan(2 atan(1/5))
=5/12 and tan(4 atan(1/5))=120/119. Subtracting atan(1/239) gives tangent1
exactly, and the angle lies between0 andpi/2. Hence it equals pi/4.
All input fractions and outward endpoint rounding must remain exact.

## Real logarithm

For rational x>0, write x=2^k*v, 1<=v<2 and z=(v-1)/(v+1). Then
log(v)=2*sum(j=0..N-1,z^(2j+1)/(2j+1))+R, with
0<=R<=2*z^(2N+1)/((2N+1)*(1-z^2)). Here0<=z<1/3.
For log2 use z=1/3; for k<0 its enclosing interval must be multiplied with
reversed endpoints. log1 is exactly0. For an input interval [l,u] with l>0,
monotonicity gives [lower(log l),upper(log u)]. Cache keys must include the
arithmetic precision/context if changing precision is supported.

## Complex exponential

Let Z be a rectangle, and A an exact upper bound on |Re z|+|Im z| for z in Z.
Scale by2^k until A/2^k<=1/2. Evaluate the Taylor polynomial to degree N using
outward complex interval operations. At the scaled argument the modulus of
the omitted tail is at most
(A_s^(N+1)/(N+1)!)/(1-A_s/(N+2)), where A_s=A/2^k.
This follows because successive absolute tail terms have ratio<=A_s/(N+2).
Add plus/minus that bound to both real and imaginary intervals; then square
k times with outward arithmetic. Interval squaring is not ordinary endpoint
squaring when0 lies in the interval. A general interval product or correct
square enclosure is required. exp0 should contain exactly1+0i; negative and
pure-imaginary arguments and range-scaling boundaries require tests.

## Dyadic endpoints and domains

For dyadic precision P, lower(x)=floor(2^P*x)/2^P and
upper(x)=ceil(2^P*x)/2^P. Python integer // is floor for negative numerators;
ceil is -((-numerator*SCALE)//denominator), not truncation toward zero.
Division requires a denominator interval excluding0. Absolute-value bounds
must take both endpoints. Interval computation must reject floats when its
advertised input contract is exact Fraction/integer. Sign-aware multiplication
and reciprocal ordering are primary adversarial test targets.

## Panel recurrence and safe discard

For f(t)=exp(-lambda*t)*t^p on a panel center m, halfwidth h, u=h/m,
q_-1=0,q0=1 and
q_(j+1)=[u*(p-lambda*m-j)*q_j-(lambda*m)*u^2*q_(j-1)]/(j+1).
The even polynomial integral is
2h*exp(-lambda*m)*exp(p*log(m))*sum(j=0..K,q_(2j)/(2j+1)).
The recurrence follows by comparing coefficients in t*f'=(-lambda*t+p)*f.
Using m>h>0 fixes the principal-log branch and the Cauchy disks stay in the
right half-plane. Natural complex interval dependency widens the result but
does not invalidate enclosure when every operation is outward.

For real t in [left,right] with left>=1 and |Re p|<=2,
|exp(-pi*n^2*t/q)*t^p|<=right^2*exp(-(3/q)*n^2*left).
Both Mellin powers integrated over length2h have total contribution at most
4h*n^a*right^2*U128((3/q)*n^2*left). It is valid to omit a pair whose
certified bound is below2^-90 and add the bound to the final absolute error.
Even keeping the all-panel Cauchy quadrature bound then only overcounts.
Check the s parameter-box domain BEFORE this optimization.

Without discards, absolute dyadic rounding of extremely small exponentials
can be amplified by huge Taylor coefficients in late/high-n panels. The
original180bit tail-bound rounding is not automatically sufficient for a
full integrand oracle. Certified discard or adaptive/higher precision is
required, with final interval widths checked explicitly.

## Fourier-circle nodes and final certificate

The true sampling point is s=1/2+(6/5)*exp(2*pi*i*j/m). Its rectangle must be
formed with an enclosed pi and exponential; a rounded rational substitute
alone is not a certificate for the actual circle. The exact circle lies
inside [-1,2]+i[-4/3,4/3], allowing outward room. Both Mellin powers then
satisfy the stated |Re p|<=2 and |Im p|<=2/3 bounds.

If the computed finite quadrature lies in X+iY, its rational rectangle center
has complex error at most halfwidth(X)+halfwidth(Y). Add n-tail, t-tail,
quadrature-tail and discard bounds to obtain the absolute complex radius.
Export the center as exact rational/dyadic values. If converting that center
to an IEEE float for training, add the exact Fraction.from_float conversion
errors; the float is not itself the exact dyadic center by default.
Interval sample certification is still distinct from FFT/GD coefficient
rounding and from the independent arithmetic determinant/GRH bridge.
