# Finite-cutoff Schur transfer for the actual ternary coefficient

NEW research-only theorem, 6 November 2026. This is a quantitative finite-matrix repair for a proposed original-family cubic d-by-a estimate. It is not the earlier infinite-d Perron/zeta continuation or a new signed/GRH saving. No accepted scalar/Perron/finite-table experiment is rerun.

## 1. Exact finite theorem and acceptance scope

Work in K=Q(omega), with its actual nonzero integral IDEALS and fixed good-prime deletion S. Let X>=2 and 1<=U<=X. Let I,J be finite sets of good squarefree ideals d,a of norm<=X. A complex matrix K=(K_da), acting from ell2(J) to ell2(I) with counting norms, is assumed zero unless (d,a)=1 and Nd Na<=X. Every additional original full-union/raw-zero/ray/capacity mask may already be in K. No positivity of K or arbitrary weighted-row large sieve is assumed.

Define the ACTUAL coefficient on its supported squarefree product by

    A_U(da)=sum_{r s | da,(r,s)=1,Nr<=U,Ns<=U} mu(r)mu(s).

The cutoff is not rescaled to a. Define H_m(v,w)=product_{p|m}(1-Np^(-v)-Np^(-w)), and

    G_IJ=max_{d in I}3^omega(d) * max_{a in J}3^omega(a).

If a set is empty the operator is zero. Put c=1/log(4X), U#=floor(U)+1/2, and choose any finite T>=8X. With

    L_T=asinh(T/c)/pi,

the following explicit operator-norm bound holds:

    || A_U(da) K_da ||
      <= G_IJ [e^2 L_T^2 + 32 X^(3/2)/T] ||K||.             (1)

Here juxtaposition inside the left matrix means entrywise multiplication, not an entrywise factorization of A_U. In particular for each fixed epsilon>0, choosing T=(4X)^4 gives

    || A_U circ K || <<_(epsilon,Kfield,S) X^epsilon
                                          log(4X)^2 ||K||. (2)

Absorb the logarithm into a renamed epsilon if desired. This does NOT mean A_U is small or multiplicative, and gives no row-energy lower bound. The operator K remains the original masked kernel; no other worker's row or coefficient is replaced.

A fixed common complex W in C_c^2((0,infinity)), supported in[1,2], can be included as W(Nd Na/D) for any D>0. Put F(v)=W(exp(v)) and

    J(W)=(1/(2pi)) integral_R |Fhat(t)|dt
         <= (||F||_1+||F''||_1)/pi
         <= (log2/pi)[||W||_infinity
                         +||x W'(x)+x^2 W''(x)||_infinity].

Then the right side of(1) is multiplied by J(W). This is an explicit fixed-profile seminorm, not an unsupported varying-profile supnorm assertion. A Gram or signed quadratic form using this coefficient twice costs the SQUARE of the transfer constant, not the constant once.

Acceptance requires: exact integer endpoints, finite-height error, norm rather than entrywise comparison, all original masks retained, and no global signed saving inferred. The independent arithmetic input for a proposed cubic norm is a separate obligation.

## 2. Endpoint-exact one-dimensional Perron estimate

For x>0,x!=1 and c>0 write

    I_T(x)=(1/(2pi)) integral_{-T}^T x^(c+it)/(c+it) dt.

The full vertical integral equals 1_(x>1). One proof is Fourier inversion of exp(-cv)1_(v>=0); the point x=1 is excluded. Integration by parts in each discarded oscillatory t tail gives

    |I_T(x)-1_(x>1)| <= 2 x^c/(pi T |log x|).              (3)

Indeed on t>=T the boundary of exp(it logx)/(c+it) contributes <=1/(T|logx|), and the differentiated denominator contributes <=1/(T|logx|); the negative tail has the same bound. This also proves convergence without an unrecorded pole-free contour shift.

For every divisor ideal r of a supported da, Nr is a POSITIVE INTEGER <=X. The half-integer U# has distance>=1/2 from Nr, so

    |log(U#/Nr)| >= 1/(2X+1) >= 1/(3X),
    (U#/Nr)^c <= e.

Thus (3) gives a UNIFORM finite error e_T<=6X/T<=3/4. Moreover 1_(U#/Nr>1)=1_(Nr<=U), including Nr=U when U is an integer. No endpoint half-weight is lost.

If J_r=1_(Nr<=U), then |I_T(U#/Nr)|<=1+e_T and

    | I_T(U#/Nr) I_T(U#/Ns)-J_r J_s |<=2e_T+e_T^2
                                                  <=18X/T. (4)

The number of disjoint ordered divisor assignments r,s of a squarefree m is3^omega(m).

## 3. Diagonal integral and a genuine operator error bound

For each finite supported coprime pair, H_da=H_d H_a. Expanding the FINITE products and using(4) proves that

    A_U(da)=A_T(da)+R_T(da),
    A_T(da)=(1/(2pi i)^2) int_{c-iT}^{c+iT} int_{c-iT}^{c+iT}
            (U#)^(v+w)/(v w) H_d(v,w)H_a(v,w) dv dw,
    |R_T(da)|<=18X/T *3^omega(d)3^omega(a).                (5)

Only supported coprime pairs use this identity. On forbidden pairs K_da=0 both before and after any diagonal multiplication. It is not necessary or legitimate to interpret H_dH_a there as A_U of a nonsquarefree product.

For Re(v)=Re(w)=c, each factor satisfies |H_m(v,w)|<=3^omega(m). The integrand is exactly

    diag(H_d(v,w)) K diag(H_a(v,w)),

with an ordinary right diagonal, not an assumed Hermitian conjugate. Both diagonal operator norms are their maximum absolute values. Since (U#)^(2c)<=e^2 and

    (1/(2pi)) integral_{-T}^T |c+it|^(-1)dt=L_T,

the finite integral has operator norm <=e^2 L_T^2 G_IJ ||K||.

The residual in(5) cannot be bounded in operator norm merely by its maximum entry times ||K||. Use instead

    ||R_T circ K|| <= ||R_T circ K||_F
           <= max|R_T| ||K||_F
           <= max|R_T| sqrt(min(#I,#J)) ||K||.

The accepted fixed-field all-ideal count is # {Nb<=X}<=2X; it is reused, not a new asymptotic audit. Consequently sqrt(min(#I,#J))<=sqrt(2X), and the residual norm is <=18sqrt2 X^(3/2)G_IJ||K||/T, which is bounded by the32 term in(1). This establishes(1) with a concrete finite T.

For completeness 3^omega(m)<<_delta (Nm)^delta uniformly on good squarefree ideals. This follows by splitting the FINITE set of prime ideals Np<3^(1/delta) from the others and using3<=Np^delta on each remaining prime. Apply delta=epsilon/2 to the two maxima. With T=(4X)^4, L_T<<log(4X), proving(2). Choosing higher fixed polynomial T makes the finite approximation error arbitrarily small as a mathematical bound, but no efficient extreme-precision runtime or numerical certificate is asserted.

## 4. The common complex column profile

Use Fourier inversion F(v)=(1/(2pi))int Fhat(t) exp(itv)dt, with Fhat(t)=int F(v)exp(-itv)dv. Two integrations by parts yield |Fhat(t)|<=min(||F||_1,||F''||_1/t^2); splitting at |t|=1 proves the stated J(W) bound.

Substitute v=logNd+logNa-logD. Each integrand multiplies K by unitary row/column norm diagonals and a scalar of modulus one. Therefore

    || W(NdNa/D) circ K || <= J(W)||K||.

Compose this Schur multiplier with(1); they commute entrywise. Every raw zero and coprime/source-class/capacity mask already in K remains zero. The support of W also retains the original annulus exactly. Fixed unitary multiplicative nu(da)=nu(d)nu(a), raw u0 factors and separable norm powers can be kept as the corresponding actual diagonal multipliers. This statement does not factor a primitive beta_da phase: its actual arithmetic splitting must be proved separately.

## 5. Actual use and remaining obstacle

For original dyadic d and residual a blocks with Nd~E, Na~D/E, a bounded number of rectangular covers has NdNa<=O(D), so take X to be that explicit constant times D. The common W is the ORIGINAL common W. The lemma permits AU(da) and that profile in a true unweighted cubic d-by-a character norm at subpower/logarithmic cost, once the actual primitive root/generator/reciprocity kernel and masks have been established. It repairs the false shortcut of applying a fixed-column-vector theorem directly to an arbitrary d-dependent vector.

It does not supply a new character large sieve, cancellation of mu(d), a full signed estimate, a spectral determinant or zero-location comparison. The small-d sector, unequal-norm coherent bands and complete original target assembly remain open. No Artin holomorphy/GRH/desired positivity/zeros assumption, no Lean declaration, no dependency installation, no build/browser/publication/index mutation. The pinned external arithmetic input and any new cubic-block estimate require independent verification in their own lane.
