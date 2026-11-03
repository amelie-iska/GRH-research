# Original sextic Mobius row Gram: masks, conductors and the short-row frontier

Independent read-only arithmetic audit, 2026-11-03. No shared source, manuscript, script, toolchain or output was edited. The result is an exact original-family expansion, a complete correlation calculation, and a counterexample to an explicitly stronger arbitrary-coefficient statement. It is **not** a counterexample to the fixed Mobius family and does not prove its MS_(3/4) estimate.

## 1. Original normalization and exact Gram identity

Let O=Z[omega]. Columns are nonzero integral ideals represented once by their primary generators. S is fixed and contains primes above2,3 and the conductor of the fixed finite-order Hecke character nu. Characters chi_n(u)=(u/n)_6 are extended by zero at primes shared with u; chi_1(u)=1, including u=0. The actual family is

M_u(D)=D^(-1/2) sum_((n,S)=1) mu(n)nu(n)chi_n(u)W(Nn/D).

W is one fixed smooth annular test. Set c_n=1_((n,S)=1)mu(n)nu(n)W(Nn/D), and let U_H={u in O:0<Nu<=H}. Then exactly

E(H,D)=sum_(u in U_H)|M_u(D)|^2
      =D^-1 sum_(n,m)c_n conjugate(c_m) K_H(n,m),
K_H(n,m)=sum_(u in U_H)chi_n(u)conjugate(chi_m(u)).

There is no primary restriction on rows and no division by the six element units. A prescribed row subset or nonnegative weight b(u) is retained inside K_H; positivity allows comparison with the full row set, but does not permit deleting a coprimality mask inside individual cross terms. If W itself varies with u, its two column weights remain inside the row sum; it is not the frozen-coefficient identity above without another separation step.

Only squarefree n,m survive. Write h=gcd(n,m), n=ha,m=hb. Then h,a,b are squarefree, pairwise coprime and prime to S. With psi_(a,b)=chi_a conjugate(chi_b),

chi_n(u)conjugate(chi_m(u))
 =1_((u,h)=1) psi_(a,b)(u).

At common primes the canceled root of unity leaves a **unit indicator**, not the constant one. The factors mu(h) and nu(h) do cancel in the column coefficient, since mu(h)^2=|nu(h)|^2=1. Therefore the exact original Gram is

D^-1 sum_(h,a,b pairwise coprime squarefree; (hab,S)=1)
 mu(a)mu(b)nu(a)conjugate(nu(b))
 W(Nh Na/D)conjugate(W(Nh Nb/D))
 sum_(0<Nu<=H)1_((u,h)=1)psi_(a,b)(u).

This contains all column S-masks, squarefreeness, pairwise coprimalities, primary counting conventions and original row zeros. The diagonal is a=b=1. There are no additional off-diagonal principal characters hidden among squarefree distinct columns.

A second exact identity retains the common-factor mask by its full Mobius expansion:

K_H(ha,hb)=sum_(d|h)mu(d)psi_(a,b)(d)
                 sum_(0<Nv<=H/Nd)psi_(a,b)(v).

Here u=dv uses the unique primary generator of the ideal divisor d. It is valid because(d,ab)=1. A row weight b(u) becomes b(dv) and cannot be silently replaced by b(v). One must sum every divisor term before using any identity that requires restored coprimality.

## 2. Primitive conductor versus the actual period

At every good prime p the sextic residue character has exact order six on the residue field, including inert rational primes whose residue field has size p^2. Thus psi_(a,b) is primitive with ideal conductor ab: at each prime of a it is the nontrivial sextic character, and at each prime of b its inverse. The full zero-extended pair function also carries the unit mask at h; a valid periodic modulus is

L=hab=lcm(n,m).

The underlying character conductor and its full periodic zero extension are different. If Nh is on scale G and Nn,Nm are on scale D, then

N(ab) is on scale D^2/G^2,
N(L) is on scale D^2/G.

Using D^2/G for both, or discarding h after canceling the characters, loses genuine arithmetic information. Conversely using the product nm is a valid but unnecessarily larger modulus, with an extra common-factor multiplicity. No reciprocity law is needed for these direct row-character statements.

## 3. Exact complete row correlation

Complete a row over O/L. CRT gives local factors. At a prime in a or b the local character is nonprincipal and its full field sum is zero. At a prime in h the local sum is the number of units, Np-1. Therefore

sum_(u mod lcm(n,m))chi_n(u)conjugate(chi_m(u))
 =0 if n!=m,
 =phi(n) if n=m.

For n=m=1 the quotient has one element and the value is1, consistent with the explicit chi_1 convention. If a common multiple modulus Q is used, the diagonal is multiplied by NQ/Nn. In particular completing modulo n^2 on the diagonal gives Nn phi(n), not phi(n).

The character nonprincipality proof is elementary: multiplication of the complete sum by an element with character value different from1 leaves the sum unchanged by permutation and also multiplies it by that value. The local unit count proves the remaining factor. This is the universal proof, not an extrapolation from residue tests.

For Fourier frequencies there is a useful stronger ledger. Under the exact CRT-scaled local additive pairings, a factor at p in ab is zero if that local frequency is zero, and otherwise has Gauss magnitude sqrt(Np). At p in h it is Np-1 at zero frequency and-1 otherwise. These are the genuine multiplicative-character and Ramanujan-sum factors. The CRT phase scalars matter in a subsequent theta identification; the magnitude/vanishing statements do not specify them away.

## 4. Original zero mode, diagonal size and what positivity does not prove

For a smooth row weight Phi(u/sqrt(H)), ordinary two-dimensional lattice Poisson with normalized finite Fourier coefficient N(L)^-1 times the complete sum gives zero mode

(H/covol(O)) Phi_hat(0) 1_(n=m) phi(n)/Nn.

The Fourier prefactor has no extra period-volume loss. Excluding u=0 subtracts only the n=m=1 contribution, because every other relevant pair vanishes there. For large D the annular column support excludes the unit column anyway. Thus the original zero frequency is exactly diagonal and contributes O(H) after the D^-1 normalization.

This same bound can be checked without Poisson. With c_O=2pi/sqrt(3), lattice counting gives R(X)=#{0<Nu<=X}=c_O X+O(sqrt(X)+1). Hence

K_H(n,n)=c_O H phi(n)/Nn
 +O(sum_(d|n)(sqrt(H/Nd)+1)).

On Nn comparable to D the error is O_epsilon((sqrt(H)+1)D^epsilon). There are O(D) columns, so the normalized diagonal is O_W(H), with the stated harmless subpower error. This does not bound the full energy.

The Gram matrix is Hermitian positive semidefinite. If E=Diag+Off, positivity gives Off>=-Diag. It gives **no upper bound** Off<=0 or Off=O(H). Dropping the off-diagonal terms would use positivity in the wrong direction. Per-row Cauchy followed by ideal counting gives only the elementary normalized bound E=O_W(HD), a factor D short of the desired scale.

Complete orthogonality also cannot be applied as if the short ball were a complete period. For the coprime bulk h=1, the period norm is about D^2, with linear period scale D. At H=D^(3/4) the row radius is only D^(3/8). Smooth mean-zero periodic cancellation is powerful when the sampling scale exceeds the period, not here. Crude fundamental-cell tiling gives at best a boundary bound O(sqrt(H N(L))+N(L)), to be combined with the trivial O(H); it supplies no desired saving in this short regime. The smaller primitive conductor ab can help some large-gcd blocks after the exact divisor-mask decomposition, but does not address the coprime bulk automatically.

Accordingly the positive diagonal O(H), the off-diagonal zero complete mean and the PSD property are compatible with much larger short-row energies for other coefficient vectors. The arithmetic problem is cancellation for the **particular** vector mu(n)nu(n)W(Nn/D), not a generic operator-norm estimate for the whole Gram matrix.

## 5. Decisive counterexample to an arbitrary bounded-column-weight strengthening

Choose one nonnegative nonzero smooth W supported in a fixed positive annulus. Introduce a fixed completely multiplicative weight b with

b(p)=-conjugate(nu(p)) for p outside S, |b(p)|=1.

This b is independent of the row and of D. On squarefree columns,

mu(n)nu(n)b(n)=mu(n)^2.

It is not an additional finite-order Hecke character. Standard elementary squarefree-ideal counting gives

sum_((n,S)=1)mu(n)^2 W(Nn/D)=c_(S,W)D+o(D), c_(S,W)>0.

For completeness that count follows by inserting mu(n)^2=sum_(d^2|n)mu(d) into the ideal lattice count; the main constant has the positive Euler factor1/zeta_K(2) and finite S adjustments, and the error is O_W(sqrt(D)log D) using the ideal-count O(sqrt(X)) error. Smooth partial summation handles W. No prime cancellation or GRH input is used.

At row u=1 all chi_n(1)=1, so this weighted family has |M_1(D)|^2 asymptotic to c^2D. Therefore an arbitrary-weight version of

sum_(0<Nu<=H)|M_u(D)|^2 << H(HD)^epsilon,
H=D^(3/4),

is false already at one row, for any sufficiently small fixed epsilon (for example epsilon<1/7). This does not refute the actual family: the counterexample deliberately cancels the original Mobius signs.

Sixth-power prime rows give an even stronger obstruction. Put Y=H^(1/6). For primary prime ideals p outside S with Y/2<Np<=Y, chi_n(p^6)=1_(p does not divide n). Removing columns divisible by p costs O_W(D/Y), so the same nonnegative weighted sum is at least cD/2 at every such row for large D,Y. The fixed-field prime ideal theorem gives at least cY/log Y distinct such rows. Hence

E_b(H,D) >= c D H^(1/6)/log H.

Thus the arbitrary-weight square-root mean square fails for H=D^h whenever0<h<6/5, allowing epsilon small relative to h. This even includes the manuscript's printed long-row exponents1+theta<=1.1. That is not a contradiction of the printed proposition, which fixes the Mobius coefficients. It shows why extending that proposition to arbitrary original column weights would destroy its essential arithmetic content. The fixed-field prime ideal theorem used in this optional strengthening is the same classical input cited explicitly in October's amplification; the one-row counterexample does not need it.

The September statement allowing arbitrary bounded prime-slot coefficients is different: it retains the original Mobius polynomial and only varies the prescribed auxiliary prime slots. It does not permit replacing every original column coefficient by the b(n) above. Likewise rowwise analytic test parameters with controlled seminorms are not arbitrary row-dependent prime coefficients.

## 6. Relation to the preserved reflected Gram notes and the new task

The latest research/gram-poisson.md concerns a different, reflected column:

A_m=Y'^(-3/2) sum_s c_sigma(s)W1(Ns/Y')(Ns/Y')^(-1+i nu)g_(chi_s)(s,-m).

Its shared factors may have higher prime powers, and its exact Poisson/full-correlation normalization, original zeros and stipulated artificial common kernel are essential. The report's two-column periodic lemma and research/reciprocity-period.md do not by themselves identify that column with the original D^-1/2 Mobius family or prove MS_(3/4). In particular their nonexceptional Fourier zero-mode result and exceptional sixth-power count are not additional principal pairs in the original squarefree Gram above. The two calculations must not be conflated.

October301–348 describes precisely an additional arithmetic transformation: the sextic Gauss factor absorbs mu via a Gauss–Jacobi identity and becomes a cubic theta coefficient, with common factors and ray phases restored later. Its schematic dual scale is D^2/H, equal D^(5/4) at the proposed short-row endpoint. Certifying those transformations with all masks and treating the resulting unfavorable scale is new arithmetic work; neither positivity nor generic periodic orthogonality replaces it.

A constructive next target is therefore an upper bound for the actual off-diagonal quadratic form in Section1, preserving its mu(a)mu(b) signs, or an exactly equivalent completed cubic-theta mean square with every prefactor and common-factor mask specified. A bound uniform for arbitrary full column weights is not a plausible substitute, as Section5 proves. No claim here establishes that actual off-diagonal bound or disproves MS_(3/4).

## 7. Exact coverage and diagnostics

Read October190–305,301–364,655–700; September12315–12480, including the exact sixth-power column identity and its rowwise-parameter limitations. Read research/exponent-frontier.md's MS target and final Gram updates, research/gram-poisson.md, research/reciprocity-period.md, research/finite-correlation.md and research/theta-tame-descent.md. This is not a fresh audit of every upstream theta/reflection proof. The September /tmp copy was byte-compared equal to the immutable current build/paper.tex.

Exact CRT tests used the actual split-field sixth roots at norms7,13,19, reductions of1+omega equal3,4,8 respectively. Seven column-pair patterns, including common factors, disjoint supports, unit columns and diagonal two-prime columns, exhausted3739 residue tuples. Every complete correlation equaled the stated0 or phi(n), with exact Z[omega] integer-pair arithmetic. No numerical complex approximation, random seed, dependency installation or shared output write was used. These finite checks corroborate the elementary universal proof above.

Pinned input hashes: October /tmp/grh-math-audit/quasi-oct.tex has169005bytes,3988lines, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d; September quasi-sept.tex/current build source has766316bytes,16677lines, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3. No actual MS estimate, new zero-free region, arbitrary iteration or GRH proof is claimed.
