# Local order and directed exponent changes in the signed Poisson cross

8 November 2026 UTC. This continues MATCHED_POISSON_CROSS-v2 (SHA256 8634bdac8792c95c057d79742551caa945b3885707424a3c5b039f923404cf99). Use exactly its original unweighted two-pivot rows, fixed \(S,\nu,u_0\), full ordered cutoff \(Z=U^2\), range \(U^2\le D\le7U^2/2\), and a single common \(W\in C_c^\infty\) supported on \([1,2]\). Write \(R=A_1 A_2\ll H\le D\), \(A_1 A_2^2\ll H\), \(E=Nd\), and \(E_i=Ne_{1,i}\). We estimate selected pairings of the actual normalized cross \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle E_d,V_d-E_d\rangle\), in the same exact re-Poisson representation of its partner. The row set, sharp endpoints, primal-zero tests, two \(Q_u\) factors, literal ray, capacity, primitive \(S\)-phases, raw zero union, original allocation coefficients and divisor signs are retained. The same all-frequency tail argument applies to each selected pair restriction, so below we clip the partner \(Nk\le D^5\). All harmonic factors and finite local state counts are absorbed in \((DH)^\epsilon\). Profile cost is \(O(\mathcal M_{16}(W)^2)\).

## A one-parameter conductor comparison

Use the notation of (1)–(5) in the matched cross note. Thus \(h_0=fa,h_1=fb\), \(j=(\bar\ell_{\rm g},d)\), \(a_0=a/c\), \(c=(z,a,\bar\ell_{\rm g})\) and \(\ell_0=\ell/(\ell,zb)\). The equality side has \(z_{0,0}=g\ell,\ k_0=g\bar\ell\), with \((\ell,\bar\ell)=1\) by the conjugate reduction. If \(e_{1,i}=s_i j_i\) then \(s_i\) is supported at fixed \(S\) and \(j_i\mid d\). The matched partner representative is \(k_\flat\). At each good prime put \(\beta=v_p(k_\flat)\) and \(\beta'=v_p(k'_\flat)\), where \(k_{\rm g}=k'_\flat v^6\) is the exact actual frequency with \(0\le\beta,\beta'\le5\). The defect support \(\mathfrak q\) consists of \(\beta'\ne\beta\). Write \(Q=N\mathfrak q\). One has the same primitive residue character on the literal row element at good conductor \(\mathfrak q\) as in that note. Its local order is the order of \(\delta=\beta'-\beta\bmod6\) in \(\mathbb Z/6\). Conjugating the entire row pairing inverts the character and does not change its conductor. The directed residue here always means the change from the matched representative to the actual partner.

Use the two radial bounds \(y_0^{-(1-\theta)} (y'_1)^{-\theta}\), \(1/6\le\theta\le1\), where \(y'_1\) is the actual perturbed partner scale, and multiply by (4) of the matched note. Relative to the weight written using the matched \(y_1\), this introduces \(\prod_{p\mid\mathfrak q}(Np)^{\theta(\beta-\beta')}\). The matched weight for this comparison, before that ratio, is
\[
 \frac{R}{E}\,\frac{(Nj)^\theta}{E_0^\theta E_1^{1-\theta}(Nq_d)^\theta}\,
 \frac{1}{Ng\,N\ell\,Nz\,(Nf)^2 (Na_0)^{6\theta}
               (Nb)^2(N\ell_0)^{6\theta}(Nv)^{6\theta}(Nk_S)^\theta}.
 \tag{1}
\]
In particular the \(c\)-power cancels. This follows from the two factors \(L_i=D/(E E_i R)\) and the original \(f^{-4}a^{-2}b^{-2}\) in the scalar. The compact comparability \(N\bar\ell_{\rm g}\asymp_S N\ell\) is unchanged. For a signed row estimate the variation bound from the matched note applies to the actual profile product, prior to these radial inequalities. The supremum plus variation costs the same radial majorant on a fixed \(v_2\) and fixed \(S\)-type class. There is no change in which pair restrictions depend on row variables.

Fix \(d,\mathfrak q\) and the finite state at each defect prime. In the following table the charge means a forced prime power in (1) or a forced divisibility in a harmonic count. The resulting factor is \((Np)^{-\kappa_p(\theta)}\).

| Good prime state | Charge | \(\kappa_p(\theta)\) |
| --- | --- | --- |
| \(p\mid d\) | \(\bar j\mid\ell\) and the \(E_i,q_d\) factors | \(\theta(\beta'+j_{0,p})+(1-\theta)(j_p+j_{1,p})\) |
| \(p\nmid d,\ \beta=0\) | none | \(\theta\beta'\) |
| \(p\nmid d,\ p\mid\ell,\ \beta=5\) | \(p\mid\ell_0\) | \(\theta(1+\beta')\) |
| \(p\nmid d,\ p\mid\ell,\ \beta=1\) | \(p\mid b\) | \(2-\theta+\theta\beta'\) |
| \(p\nmid d\ell,\ p\mid a,\ \beta>0\) | \(p\mid a_0\), \(\beta=4,5\) | \(\theta(6-\beta+\beta')\) |
| \(p\nmid d\ell,\ p\mid b\) | \(p\mid b\), and \(\bar p\mid\ell\) if \(\beta=3\) | \((1-\theta)\beta+\theta\beta'\), \(\beta=2,3\) |
| \(p\nmid d\ell ab,\ \beta>0\) | \(p\mid z\) and/or \(\bar p\mid\ell\), one per incidence | \((1-\theta)\beta+\theta\beta'\), \(\beta=1,2\) |

Here \(j_p=v_p(j),\ j_{i,p}=v_p(j_i)\). In the first row \(\beta\equiv j_p+j_{1,p}-j_{0,p}\pmod6\). The \(j\)-divisibility gives \((Np)^{-j_p}\) and the remaining local exponent is the stated one, also at nondefective primes of \(d\), where it is nonnegative. Off \(d\ell\), \(b\) is disjoint from \(z\) and the value \(3\) is exactly the contribution of \(b\) and \(\bar\ell_{\rm g}\) together. This permits both the inverse square on \(b\) and the harmonic conjugate charge. In the last row \(\beta=v_p(z)+v_p(\bar\ell_{\rm g})\). If \(p\mid\ell\), then \(p\nmid \bar\ell_{\rm g}\) and \(p\nmid a\), so \(v_p(z)+2v_p(b)-1\) is \(-1,0,1\). These are precisely the relevant cases of the table.

Distinct charged \(p\) have distinct conjugates. The charges to the harmonic \(\ell\)-sum off \(d\) do not overlap \(\bar j\). The rows with \(p\mid\ell\) only charge \(b\) or \(\ell_0\). The latter is an explicit weighted divisor, separate from the harmonic count on \(\ell\). It suffices to pull its forced product out of that weight and discard the remaining inverse power. The same argument at \(a_0,b\) uses the usual sum over multiples of their respective forced products. For example, \(\sum_{B\mid a_0,\,Na_0\ll D^C}(Na_0)^{-6\theta}\ll (NB)^{-6\theta}\log(2D)\), uniformly in the fixed range of \(\theta\). There is only divisor multiplicity from \(c\mid\bar\ell_{\rm g}\) once its power has canceled. The sums over \(g,z,\ell\) use ordinary ideal counting, the \(k_S\)-sum is geometric for \(\theta\ge1/6\), and \(v\) is polynomially bounded by the exact factorization of \(k_{\rm g}\). The estimates hold with an empty fiber interpreted as zero. These positive estimates use arbitrary ideals only as a counting enlargement after absolute values and do not change the actual phases, zero masks or coefficients.

For fixed \(d,\mathfrak q\) and a state pattern the normalized budget after the row count is \(R/E\) times the product of the table factors. Alternatively apply the prior signed squarefree row completion, with relative cost \(Q^{1/4}/\sqrt{A_1}\). This estimate is for the complete original clipped rows, using CRT with the fixed \(S\)-type, the primitive nontrivial character at each defect prime, both raw unions, the squarefree divisor split, and exact radial partial summation. It is uniform up to the same polynomial label divisor cost. Sum \(1/E\) over the actual \(d\)'s in absolute value, preserving the sign in the underlying expression. At every prime the finitely many state choices cost only a divisor factor. There are finitely many types \(\tau\) in the table after the values \(\beta,\beta',j_p,j_{0,p},j_{1,p}\) are specified. On dyads \(F_\tau\le N\mathfrak q_\tau<2F_\tau\) of the disjoint products of defect primes of each type, counting all ideals gives the comparison
\[
 (DH)^\epsilon\mathcal M_{16}(W)^2\,
 \min\left\{
 R\prod_\tau F_\tau^{1-\kappa_\tau(\theta)},\
 \frac{R}{\sqrt{A_1}}\prod_\tau F_\tau^{5/4-\kappa_\tau(\theta)}
 \right\}. \tag{2}
\]
A unit factor contributes 1. There are only logarithmically many choices per type, so bounds uniform over permitted dyads sum at subpower cost. Comparability constants at cutoffs may be enlarged by fixed factors. Formula (2) is a selected pair estimate on the original signed cross. No assumption on arbitrary additional row weights enters.

## Local orders and rational content

At \(\theta=1/2\), the table gives \(\kappa_p\ge \min(\delta,6-\delta)/2\) for \(\delta\in\{1,\ldots,5\}\). For the off-\(d\) rows this follows from \(\beta+\beta'\), \(6-\beta+\beta'\), or the stronger \(4-\beta+\beta'\) in the \(\ell,b\) row with \(\beta=1\). For \(p\mid d\) use the triangle inequality for circular distance on \(\mathbb Z/6\), since \(\beta'-\beta\equiv\beta'+j_{0,p}-j_p-j_{1,p}\). Thus \(\kappa_p\ge1/2,1,3/2\) for local order \(6,3,2\), respectively. Put \(\mathfrak q=\mathfrak q_6\mathfrak q_3\mathfrak q_2\) according to these orders. When \(\mathfrak q_6=1\), the absolute count suffices for all conductors. The cubic norm weight is harmonic and the quadratic norm weight converges, so the result is \(O(R(DH)^\epsilon\mathcal M_{16}(W)^2)\) on this whole sector. The product character may still have order six when both local orders two and three occur.

More generally use the signed alternative, which has weights \((N\mathfrak q_6)^{-1/4}(N\mathfrak q_3)^{-3/4}(N\mathfrak q_2)^{-5/4}\) prior to ideal counting. Extract the rational integer content \(\mathfrak q_i=(m_i)\mathfrak q_i^\circ\) of each order factor. Here \(m_i\) is the largest positive integer for which \((m_i)\mid\mathfrak q_i\). The factorization is unique. An inert prime ideal and each simultaneous pair of conjugate split primes go into the rational part, with norm \(m_i^2\). Good squarefreeness excludes the ramified primes. After dropping coprimalities only in the positive count, the \(m_3\)-sum has weight \(m_3^{-3/2}\) and converges. Sum \(\mathfrak q_2\) directly. Put \(F_i^\circ\) for an oriented norm dyad and \(M_6\) for the integer dyad of \(m_6\). Then the signed bound on each block is
\[
 (DH)^\epsilon\mathcal M_{16}(W)^2\,
 \frac{R}{\sqrt{A_1}}\,(F_6^\circ)^{3/4}(F_3^\circ)^{1/4}M_6^{1/2}.
 \tag{3}
\]
The \(M_6\)-power follows from \(\sum_{m\asymp M}m^{-1/2}\ll M^{1/2}\). In both critical pure and mixed blocks \(R/\sqrt{A_1}\ll D^{3/8}\) by the physical capacity. Thus the selected signed cross reaches \(D^{3/4+\epsilon}\) under
\[
      (N\mathfrak q_6^\circ)^3 (N\mathfrak q_3^\circ)m_6^2 \le D^{3/2}.
 \tag{4}
\]
The actual pair predicate (4) implies the corresponding bound on dyad lower endpoints. There is no size condition on the quadratic part or cubic rational content. A purely rational order-six defect with norm \(m_6^2\le D^{3/2}\) lies in this sector, extending the previous \(D^{1/2}\) cutoff for these defects. This factorization concerns the conductor in the signed pairing. It leaves the literal Eisenstein prime labels and the residue exponent at every prime untouched.

## Directed comparisons

With \(\theta=1\), every defective prime with \(\beta'>0\) has \(\kappa_p(1)\ge1\), including the \(p\mid d\) states. With \(\beta'=0\), the only cases in which this can fail are the ordinary \(\beta=1,2\) harmonic states, the off-\(\ell\) \(b\)-states with \(\beta=2,3\), and the \(d\)-states with \(j_{0,p}=0\). In the last case, if the residue changed then \(\beta=j_p+j_{1,p}\in\{1,2\}\). Therefore the first alternative in (2) gives \(O(R(DH)^\epsilon\mathcal M_{16}(W)^2)\) without a conductor cutoff whenever every defect prime has \(\kappa_p(1)\ge1\). In particular this holds when no changed exponent is erased to zero. It also holds if every directed residue is \(1\) or \(2\). Indeed an erased prime of one of these two residues must have \(\beta=5\) or \(4\), so it lies outside the failing states just listed.

In the reverse unit sector \(\delta=5\) at every defect, take \(\theta=1/6\). Off \(d\), the possibilities are \(\beta=0,\beta'=5\) or \(\beta'\!=\!\beta-1\). The first pays \(5/6\). In the second, the \(6-\beta+\beta'\) row pays \(5/6\), the linear rows pay \(\beta-1/6\ge5/6\), and the exceptional \(\ell,b\) row with \(\beta=1\) pays \(2-1/6\). On \(d\) the nonnegative integers \(u=\beta'+j_{0,p}\), \(w=j_p+j_{1,p}\) have \(u-w\equiv5\pmod6\), hence \(u\ge5\) or \(w\ge1\). The local weight pays \(u/6+5w/6\ge5/6\). After the signed completion the ideal weight is \(Q^{-7/12}\). Extract \(\mathfrak q=(m)\mathfrak q^\circ\) as above. The sum in \(m\) with weight \(m^{-7/6}\) converges and the oriented sum through \(F\) costs \(F^{5/12}\). Thus the bound is
\[
 (DH)^\epsilon\mathcal M_{16}(W)^2 \frac{R}{\sqrt{A_1}}F^{5/12}.
 \tag{5}
\]
The critical target holds for \(N\mathfrak q^\circ\le D^{9/10}\), independently of the rational content. This includes partner frequencies obtained by removing all the changed \(\beta=1\) primes and allows all other local states of directed residue \(5\). The signs in the directed residue refer to the exact choice of matched representative. They cannot be interchanged by simply taking the conjugate row character.

There is also a sharper absolute bound on the sector where no exponent decreases as an integer, so \(k_\flat\mid k'_\flat\). Use \(y_0^{-1/2}(y'_1)^{-1}\) instead of (1). The new scale is \(R^{3/2}/(\sqrt D\sqrt E)\) with weight
\[
 \frac{Nc}{E_0^{1/2}}\frac{Nj}{Nq_d}\,
 \frac{1}{Ng\,N\ell\,Nz\,Nf\,(Na_0)^5(Nb)^2
          (N\ell_0)^6(Nv)^6\,Nk_S}\,
 \frac{Nk_\flat}{Nk'_\flat}.
 \tag{6}
\]
Here \(Nf\) is polynomially bounded and harmonic. Pay \(Nc\) using \(c\mid z\) in the harmonic \(z\)-sum. This charge is independent of all defect weights, which come from the final ratio and are at most \(Q^{-1}\). Pay \(Nj\) by the original \(\bar j\mid\ell\) harmonic charge. The remaining sums converge or are harmonic, and all defect conductors can be summed at subpower cost. For \(d=1\) the bound is \(O(R^{3/2}D^{-1/2}(DH)^\epsilon\mathcal M_{16}(W)^2)\), pure power \(5/8\). For \(Nd\le X\) it costs at most \(X^{1/2}\) times this expression by ideal counting. For the full \(d\)-sum one can instead use (1) at \(\theta=1\), which gives \(R\) up to subpowers. Pure insertions are a special case of (6).

## Open range and failed uniform estimate

A single profile split cannot settle all weak local states by these absolute dyadic comparisons. A fresh exponent \(0\mapsto1\) pays \(\theta\). An ordinary one-incidence erasure \(1\mapsto0\) pays \(1-\theta\). If both types have comparable oriented conductor norms \(F\), their signed counting monomial in (2) is \((R/\sqrt{A_1})F^{3/2}\) for every \(\theta\). At \(F>D^{1/4}\) it exceeds the target at the critical capacity. This is a cost of the majorant, with no assertion that all such dyads occur or carry energy of this order. It isolates the lost step: the two local factors are summed by independent ideal counts after the character sum, whereas an adequate estimate must use their joint row cancellation or tighter coupled support. Large oriented erasures and mixtures outside the selected regions, the whole off-equal assembly, determinant, zero-location and Lean obligations remain open.
