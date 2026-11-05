# Independent divisor-incidence lift review

Status: PASS exact root-note DIVISOR_INCIDENCE_LIFT-v2.md, SHA256 a062a9b85603c0e7b300c219db10724c4b33f57c060eb51e6a5b5f201faa3732. Reviewed the whole version1 source and every version2 diff; the two edits precisely fix weighted bit-growth and input phase storage accounting. Small-data controls remain a separate pending acceptance. This is a standard triangle/Cauchy/incidence application, not a new sieve exponent or literature priority claim.

Let M be the fixed actual squarefree good ideal-column set and R a common finite row set with nonnegative weights (in the trial, its exact indicator). For d in the complete active divisor union, x_d and y_d are the restrictions of arbitrary coefficient vectors to d|m. Suppose T_d is the actual positive-row map on this subsequence and ||T_dc||²<=lambda_d||c||² for EVERY coefficient vector, lambda_d>=0. The identity is D*S1(x,y)=sum_d mu(d)<T_dx_d,T_dy_d>, using the LINEAR-FIRST inner product. The coefficients include their original nu/W/Mobius factors once; no X(m) multiplicativity is needed.

Absolute triangle and row Cauchy give

    |D*S1(x,y)| <= sum_d lambda_d ||x_d|| ||y_d||.

Weighted Cauchy in d bounds this by the square root of

    (sum_d lambda_d ||x_d||²)(sum_d lambda_d ||y_d||²)
      =(sum_m B(m)|x_m|²)(sum_m B(m)|y_m|²),
    B(m)=sum_(d|m) lambda_d.

All rearrangements are finite. B is a nonnegative diagonal incidence weight; no claim that the coprime Gram matrix is positive occurs. If lambda_d<=lambda_max, then B(m)<=lambda_max*tau_ideal(m), and tau_ideal(m)=2^omega_ideal(m) on squarefree columns. Neither tau nor omega is to be read from rational prime factorization of Nm.

When factoring m=d*a in the raw symbols, chi_m(u)=chi_d(u)chi_a(u), and |chi_d(u)|²=1_((d,u)=1). Keep that indicator in T_d or the exact permitted row restriction. Dropping it is allowed only as a POSITIVE norm enlargement for an upper bound, never as an identity or a restoration of actual zero character values. The fixed S/presentation masks and the surviving coefficient subsequence likewise remain. If the actual Fourier weight is complex, it is not itself a nonnegative row measure; the positive-map argument applies to the literal rows, not automatically to arbitrary complex Fhat.

For L=D/Nd<1, the supported quotient ideals have Na in[L,2L] and at most the unit ideal because 2L<2. Thus the direct row-count bound is valid there. In a general many-column endpoint, row count alone would be false; one would also need the column count or a valid operator estimate. For L>=1 the chosen sieve lambda must actually be uniform for arbitrary subsequence coefficients and the declared row/capacity restrictions.

Define ||x||_B²=sum_m B(m)|x_m|² and delta_x=x-tilde_x. Finite bilinearity gives a valid coefficient-error certificate even when the coprime matrix is indefinite:

    |S1(x,y)-S1(tilde_x,tilde_y)|
      <= D^-1(||delta_x||_B ||y||_B
                +||tilde_x||_B ||y-tilde_y||_B).

For an A-A energy approximation this is also

    <= D^-1(2||tilde_x||_B ||delta_x||_B+||delta_x||_B²).

These estimates use unnormalized coefficient/row counting norms, with the single outer1/D from the stated moment. They do not obtain a signed saving, and a small computational tail must be certified rather than inferred from positivity of the full energy.

If a high-omega truncation is used later, a purely finite optional inequality for any t>1 is

    sum_(omega>K) B(m)|x_m|²
       <=lambda_max*t^(-K)*sum_m (2t)^omega(m)|x_m|².

This only converts a COMPUTED or separately PROVED weighted moment into a tail certificate. It makes no assertion that the moment is small, no estimate uniform in arbitrary changing profiles, and no new analytic power gain. The actual signed asymptotic P7 estimate remains open.

The finite unconditional choice lambda_d=E_d is also correct: the F_d matrix has entries sqrt(w(u))*chi_m(u), and its squared Frobenius norm is the sum of w(u) over nonzero entries. Its operator norm squared is at most that Frobenius count. The exact positive B_E weights therefore give a computable finite coefficient certificate. For compressed integer weights, accumulated coordinate growth uses sum_u w(u), not merely the number of listed rows; version2 now states this and separates weight-bit costs. Phase-table input/streaming storage and character/factorization costs are likewise correctly distinguished. No mathematical correction beyond those two precision edits is required.
