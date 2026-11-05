# Actual coprime kernel: weighted divisor-incidence lift and exact evaluation

This is an application of elementary divisor inversion and Hilbert-space Cauchy, not a new sieve, signed power saving or literature-priority claim. It generalizes the accepted actual signed-slice baseline to arbitrary coefficient vectors and supplies a finite error certificate. The genuinely signed estimate is still open.

## Objects and hypotheses

Keep the actual Eisenstein field, finite deleted S, original literal units and primary/ray restrictions. Let C be any finite collection of the ORIGINAL squarefree good ideals m in [D,2D], with D>1, and let R be the actual finite row block u (possibly with fixed other factors), with nonnegative multiplicities w(u). Repeated actual rows are counted with their multiplicity. All field characters are the original literal positive sextic symbols, extended by raw zero at every shared prime. Other frozen factors, including arbitrary overlapping sixth factors, remain inside u. No primitive-conductor deletion restores a zero. The actual computational experiment uses literal unit1 and nu1; the lemma permits any common coefficient vector, absorbing nu(m) and the common complex W(Nm/D) in it.

For arbitrary complex vectors x,y supported on C define

D Q_1(x,y) = sum_u w(u) sum_{m,n in C,(m,n)=1} x_m conjugate(y_n) chi_m(u) conjugate(chi_n(u)).

This is linear in x, conjugate-linear in y. It is Hermitian but need not be positive on x=y. No monotonicity under deleting entries is assumed.

For each squarefree ideal d dividing at least one column, let

F_d(x;u) = sum_{m in C,d|m} x_m chi_m(u),
Z_d(x,y) = sum_u w(u) F_d(x;u) conjugate(F_d(y;u)).

Exact finite ideal-divisor inversion gives

D Q_1(x,y) = sum_d mu(d) Z_d(x,y).

There is NO additional mu(mn) or mu(q) factor: x,y are the original coefficients. Every ideal divisor d is retained, including the full divisor d=m, which is necessary to cancel all self-pairs m=n>1. Divisor squarefreeness and mu(d) refer to prime IDEALS; rational norm squarefreeness is insufficient.

If m=da and (d,u)=1, chi_m(u)=chi_d(u)chi_a(u). Multiplication by chi_d(u) is a rowwise unit phase, and at (d,u)>1 it is the original zero. Thus F_d is, equivalently, the accepted T_d on the actual restricted row support, multiplied by that row phase. The coefficient x_da is not factored. Residual a,b may share primes; only their individual coprimality with d follows from squarefreeness.

## Weighted operator theorem

Suppose lambda_d>=0 is a TRUE arbitrary-coefficient squared operator-norm upper bound for F_d:

sum_u w(u)|F_d(x;u)|^2 <= lambda_d sum_{m in C,d|m}|x_m|^2

for every vector on that d-divisible subsequence. It must bound the entire specified support, not a selected trained vector. Set

B(m) = sum_{d|m} lambda_d.

Then

|D Q_1(x,y)| <= sqrt(sum_m B(m)|x_m|^2) sqrt(sum_m B(m)|y_m|^2).

Proof: take the absolute triangle in the EXACT d identity; row Cauchy gives |Z_d| <= lambda_d ||x_d||_2 ||y_d||_2. Cauchy over d with weights lambda_d gives the displayed bound, since sum_d lambda_d ||x_d||_2^2 = sum_m B(m)|x_m|^2. Zero lambda_d terms vanish. This is a weighted divisor-incidence argument, not a deduction from positivity of a larger Gram matrix.

In particular B(m)<=lambda_max tau_ideal(m), where tau_ideal(m) is the number of ideal divisors, 2^omega(m) for squarefree m. The usual subpolynomial bound only recovers the existing exponent after the accepted sieve input; it does not prove the missing5/12 saving. Retaining the exact B(m) rather than replacing it by its maximum is useful for coefficient errors, not a signed cancellation theorem.

For the original A6=1 two-pivot block one may use the EXISTING accepted arbitrary-coefficient positive-row inputs at L=D/Nd>=1, with R=A1 A2 and M=max(A1,A2):

lambda_d <= C_epsilon (HD)^epsilon min{R+L R/M+L^(2/3)R/M^(1/3), L+R^2}.

The constant is the existing classical-input constant, not a computed number. The deleted d-row mask is removed only inside the stated positive norm. At 1/2<=L<1 the only possible ideal column a is the unit (Na in [L,2L]); use the DIRECT actual row-count bound, not an unstated subunit-length sieve. If no column survives, lambda_d=0. No different conductor family, reciprocity hypothesis or character mask is substituted.

## Entirely computable finite certificate

For a finite literal phase table and integer row multiplicities, take

E_d = sum_u w(u) # {m in C:d|m, chi_m(u)!=0}.

The actual matrix for F_d has entries sqrt(w(u)) chi_m(u), so its squared Frobenius norm is exactly E_d. Therefore lambda_d=E_d is an unconditional, exactly computable bound. Its B_E(m)=sum_{d|m}E_d is a certified finite weighted norm, with no unknown sieve constant. It may be very loose; no new asymptotic exponent follows from a Frobenius count.

For approximations tx,ty and errors ex=x-tx, ey=y-ty,

|Q_1(x,y)-Q_1(tx,ty)| <= D^-1 [ ||ex||_B ||y||_B + ||tx||_B ||ey||_B ].

For AA with x=t+e, a convenient symmetric certificate is

|Q_1(x,x)-Q_1(t,t)| <= D^-1 [ 2||t||_B||e||_B + ||e||_B^2 ].

These statements remain valid when the coprime matrix is indefinite. They certify the specified finite coefficient perturbation only. They neither supply spectral positivity nor bound a varying-family analytic remainder. Large derivatives of a study profile must be reported separately.

## Complete-column exact evaluation algorithm

Given the immutable literal phase table and complete ideal-divisor incidence lists, stream each actual row u. For each column m add x_m chi_m(u) to every bucket indexed by d|m. Compute the nine X/Y bucket products for X,Y in {A_U,C_U,mu}, then accumulate Z_d. Finally multiply each by the actual mu(d), sum over d and divide by D. No character-mask zero is replaced by phase zero, and no norm-duplicate ideal is merged. The full original family for the specified row block includes EVERY active annular squarefree ideal, not just selected q fibers.

Let M be the number of columns, r the number of listed rows, K the number of distinct active divisors and I=sum_m tau_ideal(m). With a fixed three coefficient channels, the bucket stage costs O(r(I+K)) arithmetic operations, O(K) streaming working storage plus the input incidence lists and either a streamed row of phases or the separately stored phase table, and can optionally retain row audit states. Literal-character construction and ideal factorization costs are additional; they are not declared free. This is a specialization of standard divisor accumulation, not a new general algorithm or quantum advantage.

For integer Z[omega] coefficients of magnitude at most C and unit/zero phases, bucket coordinates are bounded by O(M C), cross-product coordinates by O(M^2 C^2), and accumulated coordinates by O(r M^2 C^2) when w=1 on every listed row. With compressed nonnegative integer row multiplicities, replace r in this bit-size bound by r_total=sum_u w(u); the bit lengths of those weights and their multiplication are accounted separately. The arithmetic-operation count uses the number of listed rows, not r_total. An integer-operation count is not a constant-bit runtime claim. The sparse bucket identity must be compared against direct ordered coprime-pair evaluation on a small complete family, with independent field arithmetic and all cross-channel conjugations.

## Fixed finite-grid profile and boundaries

For the proposed finite experiment choose ONCE delta=1/240000 and W_*(y)=s((y-1)/delta)s((2-y)/delta), where s is the standard C-infinity step, zero for t<=0, one for t>=1. It has support[1,2], supnorm1 and derivatives O_k(delta^-k). For every integer-norm strict node D<Nm<2D at D<=60000, the distances from the endpoints are at least1/D>delta, hence W_*=1 exactly; endpoints vanish. This choice remains fixed throughout the finite grid but has large fixed derivative constants. It gives no bounded-seminorm or scale-uniform asymptotic saving, and it differs from the earlier broad plateau profile in the selected-q example.

The initial pure blocks must use A1>1 so every row has a prime ideal valuation1 outside S. The optional block37/7 has nonprincipal rows by the stored outside-S valuation witnesses. This is not the same as calling the tame conductor exponent the valuation modulo6. If a unit-only/principal row is ever included, its original residue subtraction must be restored; E=I is not assumed there. Only the declared literal class and finite row block are covered; other row sectors and principal assembly remain open.
