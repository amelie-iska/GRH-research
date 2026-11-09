# Fixed equality-label overlap in the full-frequency unit-pair correction

8 November 2026 UTC. Use the exact selected unit-pair correction of UNIT_PAIR_FULL_FREQUENCY-v1, its raw masks, original unweighted literal rows, primitive \(Q_u\asymp R\), common complex \(W\), and original middle equality. This is a full partner frequency result. It keeps the compensating equality term even when the partner coefficient is selected separately for each equality label. The pure exponent statements use \(A_1\asymp R\asymp D^{3/4}\) and \(A_2\asymp1\).

## 1. Select overlap before forming the two partner arrays

Write the original equality amplitude as a sum of its actual row-vector terms \(E_d=\sum_\lambda F_{d,\lambda}\). A label \(\lambda\) includes the original equality \(g,\ell,h_0,e_{0,0},e_{1,0},J\) and all fixed allocation tests. This is the ungrouped form of formula (2) of GROUPED_EQUAL_CROSS-v4. The split in \(e_{0,0}\mid h_0\) only costs a divisor factor in the upper comparison. Fix \(d=mn\), with \(m,n\) an ordered pair in the exact partner unit correction, and fix \(\lambda\). Choose a row-independent ideal \(J_\lambda\) of polynomial norm, determined by these fixed labels only. For example one may use the radical of the product of the equality ideals \(g,\ell,\bar\ell,h_0,e_{1,0}\). Conjugate prime ideals remain distinct. The construction permits a larger fixed union as long as its norm stays polynomial and it does not depend on the partner cutoff factors or the row.

In the primal unit-pair expression use the exact classification
\[
 q_i=(\zeta_i,J_\lambda),\qquad \zeta_i=q_i a_i,\qquad i=1,2 .
\]
The optional selector on \(q_1,q_2\) may depend on the fixed labels. It is independent of partner frequency. The original squarefreeness and \((\zeta_1,\zeta_2)=1\) imply that \(q_i\) are good squarefree and coprime to \(d\), and \(q_1\perp q_2\). Both \(a_i\) avoid \(J_\lambda\) and \(d\). Conversely these conditions, with \((a_1,a_2)=1\), give the exact two gcd's and original coprimality. There are at most \(3^{\omega(J_\lambda)}\) choices of \(q_1,q_2\), since a prime of \(J_\lambda\) may be assigned to either cutoff or neither. This is a divisor cost, uniform in the sizes of the selected \(q_i\).

The full partner frequency sum again becomes the primal unit array, since the original strict unit-pair cutoff conditions give \(E N\zeta_1N\zeta_2>U^2\), where \(E=Nd\). The original unused good ideal therefore has norm less than seven on the profile support and is the unit. In that primal array the original cutoff signs factor as \(\mu(q_1q_2)\mu(a_1)\mu(a_2)\). The fixed good raw factor \(\psi_u(q_1q_2)\) is retained. For example on a factor \(q\mid\ell\) contained in \(q_1q_2\), the paired phase uses \(\psi_u(\ell)\overline{\psi_u(q)}=|\psi_u(q)|^2\psi_u(\ell/q)\), including its zero. On a factor of \(h_0\), the square character retains its literal product with the conjugate partner value. The proof does not require replacing any such phase by a new primitive character with a smaller raw mask.

Expand the remaining common-prime projector by \(w\mid(a_1,a_2)\), where \(w\) is good squarefree and prime to \(dJ_\lambda\) before stripping. Set \(a_i=w b_i\), with the squarefree \(b_i\) avoiding \(dJ_\lambda w\). Keep \(\mu(w)\), the fixed signs \(\mu(q_1q_2)\) and \(\mu(d)\), the raw factor \(\psi_u(q_1q_2)\psi_u(w)^2\), and the actual original row mask \(\mathbf1_{(d,u)=1}\). The lower bounds \(N\zeta_i>L_i\) with \(L_1=U/Nm,L_2=U/Nn\) stay strict. The exact profile implies \(N\zeta_i<7L_i\), in addition to the individual upper bound \(U\). The shortened lengths are \(L_i/(Nq_iNw)\). Their nonempty subunit cases have length bounded below by \(1/7\) and use direct counting. The common complex profile in \(E N(q_1q_2)(Nw)^2Nb_1Nb_2/D\) separates by the original Mellin integral with bounded absolute mass. No variable character phase or sign is changed by this separation.

## 2. Coherent row comparison with the actual equality labels

For fixed \(q_i,w\) and fixed second pivot, apply the physical sixth-order moment to the two formed shortened squarefree arrays. The first-pivot row bound is the product
\[
 O\!\left((DH)^\epsilon
   \frac{\sqrt{L_1L_2}}{Nw\sqrt{Nq_1Nq_2}}\,
   \sqrt{\Phi_6(A_1,L_{1,q})\Phi_6(A_1,L_{2,q})}\right),
 \qquad L_{i,q}=\max(1,L_i/Nq_i),
\]
after Cauchy in the actual rows. The fixed raw factors are contractions at this step. The individual positive moments use the true shortened lengths, with monotonicity to remove \(Nw\) from the displayed sieve factors. The \(w\)-sum is harmonic, the second pivot count is \(O(A_2)\), and the \(q_i\) choices at fixed \(\lambda\) cost a divisor factor.

The pointwise argument of UNIT_PAIR_FULL_FREQUENCY-v1 and UNIT_PAIR_SHARPENING-v1 in fact bounds the sum of the uniform envelopes of the individual \(F_{d,\lambda}\):
\[
 \sum_\lambda\|F_{d,\lambda}\|_\infty
 \ll (DH)^\epsilon\mathcal M_{12}(W)
             \min\{\sqrt{D/E},D/(E\sqrt R)\}.                     \tag{1}
\]
Indeed \(Q_u\asymp R\) gives the same absolute radial majorant at each label for every row. The harmonic \(g,\ell\)-sums and the inverse square \(h_0\)-sum with \((1+D/(E Ne_{1,0}R(Nh_0)^2))^{-4}\) are unchanged. For fixed \(e_{1,0}\), splitting that \(h_0\)-sum at \(\sqrt{D/(E Ne_{1,0}R)}\) gives the minimum used in the cited proof. The \(e_{0,0}\) and \(e_{1,0}\) choices have divisor cost. This argument can take the row supremum of each label separately. In particular it does not infer (1) from an inequality for the supremum of the sum.

Multiply the two-array row bound by \(\|F_{d,\lambda}\|_\infty\) and use (1). Since \(L_1L_2=U^2/E\), the normalized primal comparison is bounded by the maximum of
\[
 (DH)^\epsilon\mathcal M_{24}(W)^2\,
 \frac{A_2}{E}\min\{1,\sqrt{D/(ER)}\}\,
 \frac{\sqrt{\Phi_6(A_1,L_{1,q})\Phi_6(A_1,L_{2,q})}}
      {\sqrt{Nq_1Nq_2}}                                          \tag{2}
\]
over the fixed label and ordered pair choices. The absolute \(m,n\) sum costs a divisor factor at fixed \(d\). The original \(\mu(d)\) is kept in the exact pairing.

The original middle compensation must be performed separately for each \(\lambda\). The modified partner coefficient at fixed \(\lambda\) is still row independent and divisor bounded, since it depends only on the actual cutoff, \(d,m,n,J_\lambda\) and the selected gcd's. Thus its original middle equality vector has squared norm divided by \(D\) bounded by \(O((DH)^\epsilon\mathcal M_{24}(W)^2 R/E)\), uniformly in \(\lambda\), by the elementary comparison in GROUPED_EQUAL_CROSS-v4. Also \(\sum_\lambda\|F_{d,\lambda}\|_2\ll\sqrt R\sum_\lambda\|F_{d,\lambda}\|_\infty\), since the actual row count is \(O(R)\). Cauchy and (1) bound this summed compensating term by \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\). No projection on partner frequencies is made when replacing its original full amplitude by the primal unit array.

## 3. Pure overlap ranges

At the pure scales, put \(e=\log_D E\), \(l_i=\log_D\max(1,L_i)\) and \(\sigma_i=\log_D Nq_i\). At exponent level the comparison (2) reaches \(R/E\) whenever
\[
 \Delta((l_1-\sigma_1)_+)+\Delta((l_2-\sigma_2)_+)
       \le \sigma_1+\sigma_2+(e-1/4)_+,
 \qquad \Delta(l)=\max(0,l/3-1/8).
\]
Fixed dyadic and field constants affect only the common implied constants. The divisor sum is then harmonic. In particular select a longer cutoff scale \(L_i\) by a deterministic index in ties. When \(E\gtrsim D^{1/8}\), overlap \(Nq_i\gtrsim D^{1/32}\) on that longer scale suffices. The original excess sum is at most \(1/24\). If the longer scale retains a positive excess after shortening, it loses \(\sigma_i/3\), and \(1/24-\sigma_i/3\le\sigma_i\). If it becomes flat, its original excess, and thus that of the shorter scale, is at most \(\sigma_i/3\). The same proof with original excess sum at most \(1/12\) gives the sufficient longer-scale overlap \(Nq_i\gtrsim D^{1/16}\) without an \(E\)-restriction. A shorter-scale overlap alone also contributes via the exact criterion, which requires no ordering of \(q_1,q_2\).

These are bounds for a selected part of the original full-frequency unit-pair wide correction. They leave the wide unbalanced cells with small overlaps, and the earlier selected partner defect modes, open at target power.

