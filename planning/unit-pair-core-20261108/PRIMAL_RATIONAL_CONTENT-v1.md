# Rational content in the primal cutoff of the full-frequency unit-pair term

8 November 2026 UTC. Keep the actual original unweighted nonprincipal two-pivot rows with \(R=A_1A_2\), \(Q_u\asymp R\), fixed \(S,\nu,u_0\), one common complex \(W\) supported on \([1,2]\), and \(U^2\le D\le 7U^2/2\). All raw zeros, literal ray, capacity and ordered cutoff tests are inherited. This concerns the full-frequency partner unit-pair wide correction of UNIT_PAIR_FULL_FREQUENCY-v1, with the original middle equality compensation. It selects one designated primal cutoff factor, on either side of its ordered factorization, by its actual rational content. It also allows a row-independent selection of \((d,m,n)\).

Let \(E=Nd\), \(d=mn\), \(L_1=U/Nm\), \(L_2=U/Nn\), and \(L_i^\#=\max(1,L_i)\). On the actual nonzero primal support the unused good ideal is the unit, and both cutoff factors satisfy
\[
 L_i<N\zeta_i\le U,\qquad N\zeta_i<7L_i,\qquad
 (\zeta_1,\zeta_2)=1,\quad (d,\zeta_1\zeta_2)=1 .
\]
Each factor is good and squarefree. These are the arrays in (1) of UNIT_PAIR_FULL_FREQUENCY-v1. They keep the common \(W(E N\zeta_1N\zeta_2/D)\) and the factor \(\mu(d)\mathbf1_{(d,u)=1}\). The upper bound \(7L_i\) follows only after the full-frequency primal reduction.

## An exact rational-content projector

For a good squarefree ideal \(\alpha\), let \(c(\alpha)\) be the largest positive rational integer \(q\) with \((q)\mid\alpha\). Equivalently, a split good prime \(p\) divides \(q\) if both ideals over \(p\) divide \(\alpha\), and an inert good prime \(p\) divides \(q\) if the prime ideal \((p)\) divides \(\alpha\). The prime over \(3\) is excluded with \(S\). Distinct prime ideals of equal norm retain distinct labels. Thus \(q\) is squarefree, \(N(q)=q^2\), and
\[
 \alpha=(q)a,\qquad ((q),a)=1,\qquad c(a)=1.
\]
This expression is unique. In particular a one-sided split prime in \(a\) does not enter \(q\).

For the designated side put \(\alpha=\zeta_1\), \(\beta=\zeta_2\), and impose \(c(\alpha)\ge B\), where \(B\ge1\) is an arbitrary real threshold for the rational integer. The other designation follows by interchanging the two ordered sides and their respective capacities. Expand exactly
\[
 \mathbf1_{(\alpha,\beta)=1}
   =\sum_{v\mid((q),\beta)}\mu(v)\sum_{w\mid(a,\beta)}\mu(w).
\]
These are finite ideal Möbius sums, with \(v,w\) good squarefree and coprime to each other and to \(d\). For each term write
\[
 a=wx,\qquad \beta=vwy,\qquad
 \alpha/w=(q)x.
\]
Set \(r=\prod_{p:\;\mathfrak p\mid v,\ \mathfrak p\mid(p)}p\), the product of distinct underlying rational primes of \(v\), with \(r=1\) at \(v=1\). Then \(v\mid(q)\) is exactly \(r\mid q\). It is not a condition \(Nv\mid q\). In particular for a conjugate pair over \(p\), \(Nv=p^2\) and \(r=p\).

At fixed \(v,w\), form the first column array indexed by \(z=(q)x\) and the second indexed by \(y\). The first array retains \(q\ge B,\ r\mid q,\ ((q),w)=1,\ ((q),x)=1,\ (w,x)=1,\ c(wx)=1\) and \((wz,d)=1\), with all good squarefree requirements and original strict and weak endpoints for \(\alpha=wz\). In this array \(c(z)=q\) and each \(z\) has at most one eligible \(q,x\). The second retains good squarefree \(y\) prime to \(vwd\) and all original endpoints for \(\beta=vwy\). The common profile now has argument \(E(Nw)^2Nv\,Nz\,Ny/D\). Every constraint not in these arrays is either fixed at \(v,w,d,m,n\), the common profile, or a row multiplier. No cross-coprimality constraint is discarded from the exact formula. The signs of the two cutoff coefficients and both projectors combine to
\(\mu(w)\mu(z)\mu(y)\). The raw row multiplier is exactly \(\psi_u(v)\psi_u(w)^2\), in addition to the two raw column values and \(\mathbf1_{(d,u)=1}\); both zero factors remain. There is no assumption that the rational character phase is one.

## Two physical moments with a rational-content gain

Mellin separate the common profile as in UNIT_PAIR_FULL_FREQUENCY-v1. Its row-independent transform has absolute integral controlled by the stated profile seminorm. Each separated power of the actual norm has modulus one. At fixed \(v,w\), the first ideal array is supported at length \(O(L_1/Nw)\), with coefficient magnitude at most one, and
\[
 \#\{z\ {\rm eligible}\}
 \ll \frac{L_1}{Nw}\sum_{\substack{q\ge B\\ r\mid q}}q^{-2}
 \ll \frac{L_1}{Nw\,r\max(B,r)}.                 \tag{1}
\]
For each eligible \(q\), count \(x\) by the elementary ideal counting bound at \(7L_1/(Nw\,q^2)\); an upper bound below one has an empty ideal support. For the last inequality write \(q=rj\) and use the tail of \(\sum j^{-2}\), with the inclusive lower bound interpreted literally. The second ideal array has mass \(O(L_2/(NwNv))\). The two formed arrays are indexed by actual squarefree ideals. Apply the same pinned physical sixth-order moment at fixed second pivot as in UNIT_PAIR_FULL_FREQUENCY-v1, with no estimate on arbitrary weighted row families. The shortened norm lengths give sieve factors bounded by constant multiples of \(\Phi_6(A_1,L_i^\#)\). Every live subunit length is at least \(1/7\) by its actual cap; count it directly. This also covers empty arrays.

Use Cauchy on the two formed row arrays after keeping the original equality-side pointwise envelope, then sum the original \(O(A_2)\) second pivots. The sharpened pointwise equality factor of UNIT_PAIR_SHARPENING-v1 supplies
\(\sqrt{D/E}\min(1,\sqrt{D/(ER)})\) up to the common subpower and profile factor. The scalar \(\sqrt{D/E}\sqrt{L_1L_2}/D\) is \(O(1/E)\). The remaining \(v,w\) cost is bounded by a subpower times
\[
 \sum_w\frac1{Nw}\sum_{v}\frac1{\sqrt{r\,\max(B,r)\,Nv}}
 \ll_\epsilon (DH)^\epsilon B^{-1/2}.
\]
Indeed \(Nv\ge r\). At fixed squarefree \(r\) there are at most \(3^{\omega(r)}\) choices of \(v\) (for each split prime, choose one of its two ideals or both; an inert prime gives one choice). On the polynomial clip this is a subpower. The \(w\) sum is harmonic. Splitting the \(r\) sum at \(B\) gives \(B^{-1/2}\sum_{r\le B}1/r+\sum_{r>B}r^{-3/2}\). All sums with empty or infeasible terms were enlarged only in positive comparison.

Consequently the normalized primal pairing at fixed \(d,m,n\) is bounded by
\[
 \ll_{\epsilon,S,\nu,u_0}(DH)^\epsilon\mathcal M_{24}(W)^2
 \frac{A_2}{E}\,
 \frac{\sqrt{\Phi_6(A_1,L_1^\#)\Phi_6(A_1,L_2^\#)}}{\sqrt B}
       \min\{1,\sqrt{D/(ER)}\}.                       \tag{2}
\]
Both outer divisor signs stay in the exact formula before the comparison. For the separately compensated middle equality term, the modified cutoff coefficient is still row independent, frequency independent and divisor bounded: at fixed cutoff label it counts only eligible ordered factorizations. The original elementary equality comparison therefore gives normalized cost \(O((DH)^\epsilon \mathcal M_{24}(W)^2 R/E)\), also for a selection of ordered divisor pairs. It does not give the factor \(B^{-1/2}\) for that term.

## Pure scoped consequences

At \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), the unshortened sieve factors in (2) have exponents at most \(3/4+\Delta(l_i)\), where \(\Delta(l)=\max(0,l/3-1/8)\) and \(l_i=\log_D L_i^\#\le 1/2\), up to fixed scale constants. Writing \(e=\log_D E\), a sufficient rational-content threshold exponent \(\gamma=\log_D B\) is
\[
 \gamma\ \ge\ \max\{0,\Delta(l_1)+\Delta(l_2)-(e-1/4)_+\}.
\]
Thus \(c(\alpha)\gtrsim D^{1/12}\) reaches the target over all intermediate divisors, and \(c(\alpha)\gtrsim D^{1/24}\) suffices on \(Nd\gtrsim D^{1/8}\). One can take the union over the two designations by assigning their intersection to the first designation. The additional below-threshold restriction on the other array is then row independent and retains its exact norm bounds. The \(m,n\) count and the outer harmonic divisor sum cost only subpowers, and the middle equality compensation has target size throughout.

This selects a part of the actual primal support by rational content before the prime projectors. It does not estimate the small-rational-content wide core or recover the same conclusion on a restricted set of partner dual modes. The sharper joint divisor sign estimate, equality-wide beyond-prefix problem, and whole signed form remain open.
