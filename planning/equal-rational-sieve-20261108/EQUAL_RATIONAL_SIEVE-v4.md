# A rational large sieve on the equal-norm side of the signed dual cross

8 November 2026 UTC. Original unweighted nonprincipal two-pivot Eisenstein rows. All comparisons below concern the counting norm on those rows.

## Exact projection and character

Use the middle Poisson window of LOW_DUAL_CUTOFF-v1 and the conjugate reduction of CONJUGATE_DUAL_OVERLAP-v2. Keep fixed \(S,\nu,u_0\), one common smooth complex \(W\) supported on \([1,2]\), \(U^2\le D\le7U^2/2\), and the full cutoff coefficient \(\beta_{d,U,U^2}\). The letter \(d\) is the intermediate squarefree ideal in the exact signed Möbius form. The original capacity, squarefree, literal ray, and common-prime selectors remain. With \(A_i\le Nv_i<2A_i\), the literal row is \(u=u_0\alpha_{v_1}\alpha_{v_2}^2\), \(R=A_1A_2\), \(Q_u\asymp R\) is the primitive conductor norm, and \(H\) caps \(Nu\).

Write \(z_0=g\ell a'\) and \(k=g\bar\ell b'\) with the original \(g=(z_0,k)\) and conjugate overlap \(\ell\). Here \(\gcd_{\mathbb Z}(Na',Nb')=1\). The equal-norm projection \(E_d\) is \(Na'=Nb'=1\), so \(z_0=g\ell,\ k=g\bar\ell\). Take it in the original middle window before disjoint assignments that remove the whole unit reduced denominator. One can keep prior selectors on \(z_0,k\) inside this projection. The primitive dual phase is
\[
 |\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)} .
\]
Each prime of \(\ell\) is split, \(\ell\) is squarefree, and \((\ell,\bar\ell)=1\). Select a divisor \(t\mid\ell\) with both \(t,\bar t\) prime to \(S\), and with \(Nt\) in a prescribed band. If more than one divisor qualifies, choose exactly one by a fixed order on the ideal labels. This is a partition of terms, including distinct equal-norm orientations. Let \(E_{d,\mathcal B}\) be the selected amplitude. Terms with no qualifying divisor remain in the complementary amplitude. No conjugation invariance of \(S\) is needed.

Write \(\ell=t w\). The \(w\)-factor, including any primitive value at \(\bar w\) supported on \(S\), stays exact. For \(t,\bar t\) good the phase is
\[
 \psi_u(t)\overline{\psi_u(\bar t)}
   =\nu(t)\overline{\nu(\bar t)}\,\chi_t(Nu),
 \qquad \chi_t(n)=\left(\frac{n}{t}\right)_6 .
 \tag{1}
\]
Conjugating the local symbol at \(\bar t\) changes the input to \(\bar u\) at \(t\). The product is then the symbol of \(u\bar u\) by multiplicativity with zero extension. A common prime with either orientation makes \(\chi_t(Nu)=0\). In particular (1) covers the case when \(t\) itself is prime to \(u\) but \(\bar t\) is not. No primitive zero is removed in this operation.

The Dirichlet character \(\chi_t\) has primitive conductor \(Nt\). At each split prime of \(t\), reduction of integers surjects onto \(\mathbb F_p\) and the sixth-power map \(n\mapsto n^{(p-1)/6}\) on the nonzero residues has image of order six. Thus the local character is nontrivial and primitive modulo \(p\). CRT gives primitivity at the squarefree product of these rational primes. The conjugate orientation gives the inverse local character, distinct from the original order-six character. The pair \((Nt,\chi_t)\) identifies \(t\) within this support. The same statements hold for \(\chi_t^2\) with local order three.

## Row estimate for a divisor dyad

Use a dyad \(B\le Nt<2B\), \(B\ge1\). For fixed \(d,r,e_1,e_0,J\) use \(X=D/(Nd(Nr)^2)\), \(E_i=Ne_i,\ E=E_0E_1,\ z=e_0z_0\), and \(J'=J/E_0\). Set \(L=X/(EE_0)\). The argument of the actual radial transform is \(L/Q_u\) because \(Nk/Nz=1/E_0\). The exact prefactor is \(2X\gamma_u/(\sqrt3 E Nz\sqrt{Q_u})\). After placing \(J/Nz\) in the column coefficient, its row part times the profile has modulus
\[
 \ll \mathcal M_{12}(W)\frac{X}{EJ\sqrt R}(1+L/R)^{-4}.
 \tag{2}
\]
It is independent of \(t\). The conditions \(X'>B_*\) and \(K_0<Nk\le MD^\eta\) use the same scales as in LOW_DUAL_CUTOFF-v1 and remain exact selectors. On each fixed \(g,w\) the additional cutoff predicates, the deterministic assignment of \(t\), and the exact \(\beta_{d,U,U^2}(e_0gtw)\) are independent of the row. The factors on \(r,e_0,e_1,d,g,w,\bar w\) and the Gauss root stay in the row multiplier. Coprimality of the selected column with the row is represented by its original character zeros. In particular \((r,k)=1\) is not imposed. There are \(O((J'/B)\log(2+2J'))\) pairs \(g,w\) on live dyads by the elementary ideal count and \(\sum_{Ng\le 2J'/B}1/Ng\ll\log(2+2J')\). Indeed \(N(gw)\le 2J'/B\), and a live dyad forces \(J'/B\ge1/2\).

We use the one-dimensional primitive character large sieve in dual form. Here is the version used. For integer \(1\le n\le L_0\) and distinct primitive characters with \(q\le 2B\),
\[
 \sum_{n\le L_0}\left|\sum_{q,\chi}c_{q,\chi}\chi(n)\right|^2
       \ll (L_0+B^2)\sum_{q,\chi}|c_{q,\chi}|^2 .
 \tag{3}
\]
For the forward inequality expand each primitive character by its Gauss sum. The expansion uses the same zero at nonunits, and \(|\tau(\bar\chi)|=\sqrt q\). At a fixed \(q\), enlarging the resulting squared Fourier expression to all characters of \((\mathbb Z/q)^\times\) bounds the sum by \((\varphi(q)/q)\sum_{(x,q)=1}|S(x/q)|^2\), where \(S\) is the integer additive transform. The reduced fractions for all \(q\le2B\) are separated on \(\mathbb R/\mathbb Z\) by \(\rho\gg B^{-2}\). For the dual additive inequality, majorize the integer interval by a constant times \(\exp(-\pi n^2/T^2)\), \(T=\max(1,L_0)\). Poisson summation gives kernel \(T\sum_{j\in\mathbb Z}\exp(-\pi T^2|x/q-y/q'+j|^2)\). At each fixed fraction the absolute row sum is \(O(T+\rho^{-1})\) by counting points on the \(\rho\)-separated lifted line in intervals of length \(1/T\) and summing Gaussian tails. Schur's inequality and finite duality prove the additive estimate, then duality yields (3). This is the dimension-one proof of the comparison used in mcs:additive, with integer moduli in place of Eisenstein ideal denominators.

The squared mass of the \(t\)-coefficients for fixed \(g,w\) is \(O_\epsilon((DH)^\epsilon B)\). There are three ways to choose the integer row variable in (3).

1. Freeze \(v_2\) and use \(n=Nv_1\le 2A_1\). Absorb \(\chi_t(Nu_0(Nv_2)^2)\) in the \(t\)-coefficient including its zeros. There are at most \(\tau(n)\) Eisenstein ideals of norm \(n\), and the original generator multiplicity is fixed. Sum squared bounds over the \(O(A_2)\) choices of \(v_2\).
2. Use the full integer \(n=Nv_1(Nv_2)^2\le H/Nu_0\) without freezing \(v_2\), absorbing \(\chi_t(Nu_0)\). For a fixed \(n\), the candidate norms \(Nv_2\) have squares dividing \(n\). Each choice determines \(Nv_1\), and the two ideal fibres are bounded by divisor counts. The total row multiplicity over \(n\) is \(O_\epsilon((DH)^\epsilon)\).
3. Freeze \(v_1\), absorb \(\chi_t(Nu_0 Nv_1)\), and use \(\chi_t^2\) and \(n=Nv_2\le 2A_2\). The squared norm over \(v_1\) costs \(O(A_1)\).

The row subsets and contractions, including exact \(Q_u\) and the original capacity, are bounded only in the positive norm after (1). Repeated row norms are counted, with no claim of independent phases. In the second choice one may use \(H_b=\min(H,8A_1A_2^2)\) as an upper bound for \(n\).

Apply (3), (2), and the count of frozen pairs. The scalar common to the three resulting row bounds is, up to subpowers and \(\mathcal M_{12}(W)\),
\[
 \frac{L}{\sqrt R}(1+L/R)^{-4}\le C\sqrt L.
\]
The remaining factor is the square root of
\[
 \mathcal Q(B)=\min\{ A_2(A_1/B+B),\ H_b/B+B,\ A_1(A_2/B+B)\}.
 \tag{4}
\]
Since \(\sqrt L=\sqrt X/(E_0\sqrt{E_1})\), the inherited sum over \(r,e_0,e_1,J\) gives
\[
 D^{-1}\|E_{d,B}\|_2^2
 \ll_{\epsilon,\eta,S,\nu,u_0}
 (DH)^\epsilon\mathcal M_{12}(W)^2\,\mathcal Q(B)/(Nd).
 \tag{5}
\]
On each dyad of \(Nr\) the \(O(Nr)\) count cancels \((Nr)^{-1}\) in \(\sqrt X\). The \(e_0\)-weight is harmonic, the \(e_1\) choices have divisor cost, and the number of cutoff dyads is logarithmic. This also gives the band estimate by taking the maximum of the appropriate bounds on its dyads at subpower cost. The same sum over \(d\) is harmonic. The bound concerns the original selected terms rather than the larger unweighted model of a complete row interval.

## Cross with the original amplitude

Use the exact \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle E_{d,\mathcal B},\,V_d-E_d\rangle\). Here \(V_d\) is the full original amplitude and \(V_d-E_d\) includes every nonequal term. The same proof applies with \(V_d-E_{d,\mathcal B}\) in the second slot. The inherited positive comparison for \(V_d\) is phy:divisor-proof, and the positive energy of \(E_d\) is bounded by the unit-length case of CONJUGATE_DUAL_OVERLAP-v2. The norm triangle and absolute Cauchy therefore bound the cross using (5) and the inherited \(D^{13/12+\epsilon}\) budget at \(H\asymp D^{3/4}\). All estimates also hold with any restriction on the intermediate divisor sum, including \(d=1\). This gives the following bounds up to subpowers and the displayed profile costs.

| Row regime and input | Band for \(Nt\) | Upper energy power for the selected equality terms | Cross power |
|---|---|---:|---:|
| Mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\), first pivot | \([D^{1/6},D^{1/4}]\) | \(5/12\) | \(3/4\) |
| Mixed, first pivot | \([D^{7/40},D^{29/120}]\) | \(49/120\) | \(179/240\) |
| Mixed or pure \(A_1\asymp D^{3/4},A_2\asymp1\), full norm | \([D^{1/3},D^{5/12}]\) | \(5/12\) | \(3/4\) |
| Mixed or pure, full norm | \([D^{41/120},D^{49/120}]\) | \(49/120\) | \(179/240\) |
| Mixed, first pivot | \(Nt\asymp \sqrt{A_1}\) | \(3/8\) | \(35/48\) |
| Mixed or pure, full norm | \(Nt\asymp D^{3/8}\) | \(3/8\) | \(35/48\) |

The narrower first-pivot interval leaves a margin in the feasible \(1/2000\) mixed pivot neighborhood. The full-norm comparison uses the original physical capacity throughout. If the eligible part of \(\ell\) has norm at least the lower endpoint of a narrower band and all its prime norms are at most \(D^{1/15}\), multiplying its primes until the lower endpoint is first reached produces a divisor in that band. Ineligible conjugate factors of \(\ell\) are held fixed in \(w\).

As a diagnostic, applying (5) to a mixed first-pivot divisor of norm \(D^{3/10}\) without any divisor in either stated band gives cross power \(23/30\) by the better of the first two choices. The large sieve is a comparison for the selected equality part. Its complement can still have the full inherited equal-energy power, and restricting the second slot to an arbitrary individual Poisson projection requires a separate positive estimate for that projection.

## A separate far ratio bound from the small radial argument

In the actual middle off-equal amplitude \(T_{d,\Lambda}\), select \(Na'\ge\Lambda Nb'\), \(\Lambda\ge1\), with equality of the norms still excluded. The exact ratio condition is a column predicate at fixed \(g,\ell,b'\). In the notation of CONJUGATE_DUAL_OVERLAP-v2, let \(P=J'/(CB),\ T=K/(CB),\ y=K/M\) in its \(g,\ell,k\) dyads. On a live selected dyad \(P\ll Z\), \(T\ll Z/\Lambda\), and \(T/P\ll1/\Lambda\). Since
\[
 y=\frac{X'}{E_1R}\frac{T}{P},\qquad X'=X/E_0^2\le D/Nd ,
\]
we have \(y(1+y)^{-8}\ll\min(1,D/(NdR\Lambda))\). Use the original one-column bound (3) of that note, its full profile, and its harmonic sums to get
\[
 D^{-1}\|T_{d,\Lambda}\|_2^2\ll
 (DH)^\epsilon\mathcal M_{12}(W)^2
 \frac{A_2}{Nd}\frac{Z}{\Lambda}\Phi(A_1,Z)
 \min\{1,D/(NdR\Lambda)\}.
 \tag{6}
\]
Here \(1\le Z\le U^2\); \(Z=U^2\) in the full coefficient. Subunit live dyads cost a fixed factor by ideal counting, and a bound \(Z/\Lambda\) below a sufficiently small constant forces empty support. These steps leave both ideal coprimalities, the precise original selectors and all \(S\)-supported values in the amplitude. They use the asymmetry of the profile and do not apply with the numerator and denominator reversed.

At the exact mixed point and \(Z=U^2\asymp D\), \(\Phi(A_1,Z)\ll D\). With \(\Lambda=D^{5/6}\), the power of (6) after the divisor sum is \(11/12\). The exact cross with the whole equal-norm projection, of energy power \(7/12\), is then \(D^{3/4+\epsilon}\) by absolute Cauchy. Slack \(\Lambda=D^{101/120}\) gives cross power \(89/120\) in the same calculation and retains the target in the feasible \(1/2000\) mixed neighborhood. At the exact pure point \(\Phi(A_1,Z)\ll D^{13/12}\). With \(\Lambda=D^{19/24}\), equation (6) gives energy \(3/4\) and hence cross \(3/4\) with the pure equality energy. The pure slack choice \(\Lambda=D^{4/5}\) gives cross power \(89/120\). Both results include \(d=1\) and allow small rational content in \(a',b'\).

In the remaining small-content long ratios, the two equal/unequal Poisson terms share the same primitive Gauss phase \(\gamma_u\) and it cancels in their product. On the live support, the good phase of that product is the character of the quotient of the two \((re_0)^2 e_1 z_0/k\) factors. At any rational prime below neither \(S\) nor \(d\), the \(r,e_0\) factors contribute even rational norm valuations, and the \(e_1\) factors contribute none. The conjugate-overlap ratios have rational norm one. An odd norm valuation of \(a'\) at such a prime, which cannot occur in \(b'\) by their integer norm coprimality, forces an odd valuation of the full rational norm quotient. Thus at least one prime ideal above it has an exponent not divisible by six. In particular, for squarefree \(a'\) this holds if \(Na'>C_S c(a')^2\operatorname{rad}_{\mathbb Z}(Nd)\), where \(C_S=\prod_{p\text{ below }S}p^2\) bounds the removed norm factors. This excludes a principal good sextic phase on that selected support. It supplies no short-conductor or incomplete row bound. The unselected equality cross, the remaining far and long leading terms, the whole signed estimate and the determinant bridge remain open.

## Cubic Gram improvement of the rational comparison

The same oriented rational family has the stronger squared operator budget
\[
 (L_0 B)^\epsilon (L_0+B^{5/3})                                    \tag{7}
\]
in (3), for either \(\chi_t\) or \(\chi_t^2\). The primary input is the pinned \(n=3\) de Faveri comparison already used in POWERED_DUAL_ROOT-v1, with \(\Phi_3(A,B)=A+B+2(AB)^{2/3}\), together with the literal finite-class reciprocity of wc:literal-reciprocity and phy:family.

For a proof, majorize \(1\le n\le L_0\) by \(e^\pi e^{-\pi n^2/L_0^2}\) on \(\mathbb Z\). Expand this positive Gram sum. For a pair \(t_1,t_2\), let \(c=(t_1,t_2)\) and \(j=(t_1,\bar t_2)\), so \(t_1=cja,\ t_2=c\bar j b\). The rational prime supports of \(c,j,a,b\) are pairwise disjoint. Put \(F=Na Nb Nj\). For \(s=1,2\) the exact product is
\[
 \chi_{t_1}(n)^s\overline{\chi_{t_2}(n)^s}
 =\mathbf1_{(n,Nc)=1}\chi_a(n)^s\overline{\chi_b(n)^s}\chi_j(n)^{2s}.
\]
The last three characters form a primitive rational character \(\theta\) of conductor \(F\): all its local exponents are nonzero modulo six. The diagonal \(F=1\) is exactly \(t_1=t_2\), and its contribution is \(O(L_0)\) per squared coefficient.

Off the diagonal expand the first indicator by \(\sum_{e\mid (n,Nc)}\mu_{\mathbb Z}(e)\). Each \(e\mid Nc\) is prime to \(F\). Substituting \(n=e x\) and applying the primitive rational Gauss identity followed by one-dimensional Gaussian Poisson gives the exact summand, up to the fixed Gaussian majorant constant,
\[
 \mu_{\mathbb Z}(e)\theta(e)
 \frac{L_0}{e\sqrt F}\frac{\tau(\theta)}{\sqrt F}
 \sum_{m\ne0}\overline{\theta(m)}
              \exp\!\left(-\pi\left(\frac{L_0m}{eF}\right)^2\right).
 \tag{8}
\]
There is no zero mode off the diagonal. The values at nonunit \(m\) remain zero. CRT separates the normalized Gauss factors and their crosses involving \(j\) into products of one-side factors at fixed \(j\). The only coupled edge is \((\chi_a(Nb)\overline{\chi_b(Na)})^s\). For the multiplicative primary generators,
\[
 \chi_a(Nb)\overline{\chi_b(Na)}
 =
 \frac{(\alpha_b/a)_6}{(\alpha_a/b)_6}
       (\bar\alpha_b/a)_6\,(\alpha_a/\bar b)_6
 \quad\text{on the coprime support.}
\]
Here \(\alpha_{\bar b}=\bar\alpha_b\) by uniqueness. In each of the finitely many choices of reciprocity classes and finite Kummer twist labels of \(a,b,\bar b\), literal reciprocity turns the quotient into a fixed scalar times one-side unitary factors, and the last two factors into \((\bar\alpha_b/a)_6^2\) times factors of the same kind. For example the \(\eta_{\alpha_b}(a)\) and \(\eta_{\alpha_a}(b)\) terms separate once the actual finite \(\eta\) labels are frozen. The separation keeps the actual finite Kummer twist labels along with the ray labels. For \(s=2\) the resulting matrix is the conjugate cubic matrix. Both matrices supply the zero when \((a,\bar b)>1\). The mask \((a,b)=1\) is still required. Expand it with \(\sum_{q\mid a,b}\mu(q)\). At fixed \(q\), put \(a=qA',\ b=qB'\). The cubic factor splits by multiplicativity into the fixed factor on \(\bar q,q\), two one-side factors, and the shortened cubic matrix on \(A',\bar B'\). Keep all of their zero values. This defines a separable extension of the off-diagonal edge for the Möbius expansion. It uses the CRT identity only on the actual coprime support.

For fixed \(c,j\), the two residual lengths are each comparable to \(B/(Nc Nj)\) on live pairs, and \(F\asymp F_*:=B^2/((Nc)^2 Nj)\). The actual \(F^{-1/2}\) separates as a product of factors on \(a,b\) times the fixed \(Nj\)-factor. Separate the Gaussian in (8) on a fixed compact interval of \(\log(F/F_*)\) by Fourier inversion with a smooth cutoff. Its Fourier absolute integral is \(O_M((1+|m|/Y)^{-M})\) for each fixed \(M\), \(Y=eF_*/L_0\). This follows by two integrations by parts with the Gaussian derivative bounds, and the Fourier phases separate in \(Na,Nb\). For \(M>2\), the sum over nonzero integer \(m\) is \(O(Y)\), also for \(Y<1\). Thus the scalar after the absolute \(m\)-sum is \(O(\sqrt{F_*})\), at most \(O(B)\). After fixing \(q\) and all one-side factors, the pinned cubic comparison gives operator norm \(O_\epsilon(B^{2/3+\epsilon})\) on the shortened good squarefree ideals, since both lengths are \(O(B)\) and the conjugation of one indexing set is a permutation. The fixed primitive Gauss factors, \(\theta(e)\), \(\theta(m)\), and the fixed classes are diagonal multipliers in the separated arrays.

When \(j\) is the unit, the simultaneous unit residuals are removed by splitting into the two disjoint cells \(a\ne1\) and \(a=1,b\ne1\). Each is compatible with the same masks. For fixed \(c,j,e,q\), the maps from the residual labels to \(t_1,t_2\) are injective on their respective arrays. Each original label \(t\) can occur only for divisor choices of \(c,j,q\) on its side (using \(\bar j\) on the right), and \(e\mid Nc\), so this multiplicity is divisor bounded. Cauchy in the products of the two restricted squared coefficient norms, after the uniform \(B^{5/3+\epsilon}\) bound, gives the off-diagonal budget in (7). The same-side support restrictions and fixed classes are never treated as statistically independent.

Use (7) in the three row averages in (4). This replaces each \(B\) summand inside its braces by \(B^{2/3}\). The proof of (5) still applies. One may further retain a factor \(O(\min(1,(B/R)^{-7}))\) in its squared bound. In fact the surviving primal-zero cutoff \(X/(EJ)>1/2\) gives \(L>J'/2\). Since \(Nt\le Nz_0<2J'\), one has \(L/R\gg B/R\), and the squared profile scalar \((L/R)(1+L/R)^{-8}\) gives the factor. This uses the original primal-zero removal. It does not require \(Nk\) to be comparable to \(L\) or \(R\).

At mixed, select \(t\) to be the entire eligible part of \(\ell\), formed by keeping the prime factors whose conjugates also avoid \(S\). Then the \(D^{3/4+\epsilon}\) cross bound holds whenever \(Nt\ge D^{7/40}\). For \(D^{7/40}\le Nt\le D^{11/30}\), the first pivot comparison gives equality energy at most \(D^{37/90+\epsilon}\) and cross \(D^{269/360+\epsilon}\). For \(Nt\ge D^{41/120}\), the full physical norm comparison with the profile factor gives equality energy at most \(D^{49/120+\epsilon}\) and cross \(D^{179/240+\epsilon}\). For this second estimate, \(H_b/B\ll D^{49/120}\), and \(B^{2/3}\min(1,(B/R)^{-7})\ll R^{2/3}\ll D^{7/18}\). The two intervals overlap. Both have slack in the feasible \(1/2000\) mixed neighborhood. This is an independent estimate for a portion of the mixed equality cross, which is handled in full by GROUPED_EQUAL_CROSS-v4.

At the exact pure point the full physical norm comparison gives target cross for \(D^{1/3}\le Nt\le D^{5/8}\) and also for \(Nt\ge D^{29/38}\) in the original middle window using the profile factor. The smaller interval contains the optimum \(Nt\asymp D^{9/20}\), which gives equality energy \(D^{3/10+\epsilon}\) and cross \(D^{83/120+\epsilon}\), even at \(d=1\). This remains a partial pure result. For example \(Nt\asymp D^{7/10}\) alone gives cross \(D^{31/40+\epsilon}\) by this comparison. It may still contain a suitable divisor of shorter length, which can be selected by the same exact rule. The cubic Gram estimate concerns a rational-argument family under the stated oriented split support and does not bound the missing pure cross for arbitrary \(\ell\).

