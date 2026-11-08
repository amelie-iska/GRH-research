# Exact factorization of the wide cutoff correction

8 November 2026 UTC. Keep the original selected equality-versus-complement cross and all masks of DIVISOR_SIGN-v1. This note treats its wide above-cap correction at fixed row and fixed remaining Poisson labels. It gives an exact short list of small-prime corrections and a uniform subpower estimate for the resulting scalar when the free divisor norm has polynomial size. The coherent masked row comparison remains open.

## 1. Only the unit and primes of norm seven or thirteen enter the inner correction

For one original live allocation, write \(\zeta=e_0z_0=\zeta_1\zeta_2\), \(T_i=U/N\zeta_i\ge1\), \(E=Nd\), \(E_1=Ne_1\), and \(h=re_0\). Use the notation
\[
 s(E)=\mathbf1_{E\le T_1}+\mathbf1_{E\le T_2}-1,\qquad
 \Omega=\frac{E}{T_1T_2}=\frac{E N\zeta}{U^2}.
\]
The original dyadic primal-zero test and \(e_0\mid h\) give
\[
 \Omega<\frac{14}{E_1Nh}.
\]
This is a bound on the actual allocations retained in the Poisson representation.

In (1) of DIVISOR_SIGN-v1, a correction label \(m\mid d\) has \(T_1<Nm<E/T_2\), hence \(m\ne1\). The inner sum can be evaluated by subtracting its complementary divisors from the full zero sum:
\[
 \sum_{\substack{a\mid m\\Na\le T_1}}\mu(m/a)
   =-\sum_{\substack{c\mid m\\Nc<Nm/T_1}}\mu(c).
\]
The upper bound \(Nm/T_1<\Omega<14\) is strict. Every good nonunit ideal has norm at least seven. In \(\mathbf Q(\omega)\), the only good prime ideals of norm below fourteen are the allowed ideals over the split rational primes \(7,13\). The primes above \(2,3\) lie in \(S\), and every remaining inert prime has norm at least \(5^2\). Let \(\mathcal P\) be these at most four actual prime ideals after the \(S\)-deletion. Since two good prime factors already have product norm at least \(49\), the complementary sum contains only the unit and some of \(\mathcal P\).

Writing \(n=d/m\), the exact coefficient is therefore
\[
 \begin{split}
 F_d(T_1,T_2)&=\mu(d)\{s(E)+C_d(T_1,T_2)\},\\
 C_d(T_1,T_2)&=
 \sum_{\substack{mn=d\\Nm>T_1,\ Nn>T_2}}
 \left(1-\sum_{\substack{p\in\mathcal P\\p\mid m}}
                         \mathbf1_{Nm>T_1Np}\right).            \tag{1}
 \end{split}
\]
All pairs are ideal factorizations of squarefree \(d\), so the two factors are coprime automatically. Equal rational norms do not merge ideal labels. The term \(Nn>T_2\) is exactly the old \(Nm<E/T_2\), and the prime cutoff remains strict at equality. The condition \(Np<Nm/T_1\) is automatically impossible for any \(p\in\mathcal P\) when \(E_1Nh\ge2\). In that case \(C_d\) is a nonnegative unweighted factorization count, and for \(E_1Nh\ge14\) it is zero. In particular the unit divisor has no correction.

If a small-prime subtraction is present, then \(\Omega>Np\ge7\), so \(E N\zeta>7U^2\ge2D\). Its individual original primal \(b\)-sum has zero profile at every \(Nb\ge1\), since the actual profile argument there is \(E E_1 (Nh)^2 Nz_0\,Nb/D\ge E N\zeta/D>2\). Such terms can still occur in the dyadic Poisson decomposition because the original primal-zero removal is on the whole dyad. Equation (1) retains them in that representation. Cancelling their entire frequency sum would require all original modes, and does not delete them from the selected equality-versus-complement cross.

## 2. Fixed-label scalar comparison including the wide correction

Fix the actual row and all primal and dual labels on both sides, including \(e_0,e_1,h\), the two ordered cutoff factorizations and their dyadic tests. Keep both original erasure selections and all other restrictions of that fixed-label cell. Let \(\mathcal L\) be the finite prime union of \(S\), the row, all fixed labels on both sides, and \(\mathcal P\). Select one exact intersection of \(d\) with \(\mathcal L\), represented by a squarefree ideal \(\delta\). This is a selection of the actual terms, and must obey all original required memberships and deletions. The active good \(e_{1,i}\)-primes, \(j\)-primes and support of the exact \(\widetilde q_d\) are then fixed in \(\delta\) whenever present. All primes outside \(\mathcal L\) see zero valuations in the fixed labels. For each fixed intersection, the original raw phase and all required fixed label memberships are independent of the free part of \(d\). A raw zero on the fixed row remains zero. The remaining condition on the free part is coprimality to the complete \(\mathcal L\). The norm of its radical is polynomially bounded on the inherited original clipped support.

Apply (1) to both sides. Their two factors of \(\mu(d)\) leave the single outer \(\mu(d)\). The step-step term has no factorization constraint. Each step-correction term has the two factors \(m,n\) of (1). For a correction-correction term write \(d\) uniquely as the product of four coprime ideals indexed by the membership bits of each prime in \(m_0,m_1\). The two \(m_i\)'s and their complements \(n_i\) are products of the corresponding two cells. Thus every term after opening the finite sums over \(\mathcal P\) uses at most four pairwise coprime factors. These decompositions count the exact multiplicity of the original factorizations. The finitely many small-prime constraints have no free ideal variables beyond those cells.

Distribute the primes of the fixed \(\delta\) among the cells, at most \(4^{\omega(\delta)}\) allocations. The requirements \(p\mid m_i\) for \(p\in\mathcal P\) are now fixed, since every such prime dividing \(d\) belongs to \(\delta\). All cell factors have the form \(\delta_j q_j\), where the free \(q_j\)'s avoid \(\mathcal L\). The sign is \(\mu(\delta)\prod_j\mu(q_j)\). On a physical divisor dyad \(Y\le E<2Y\), write \(Y'=Y/N\delta\) and suppose \(Y'\ge D^\kappa\) for a fixed \(\kappa>0\). Fix the index of a largest free cell by a deterministic index order on ties, and fix the other free cells. The norm \(t\) of the remaining free ideal is at least \((Y')^{1/4}\), since there are at most four cells. The remaining free ideal avoids \(\mathcal L\) and all primes in the other free cells. This is the full original fixed-label deletion together with the coprimalities imposed by the exact factorization. Its forbidden radical still has polynomial norm.

Every norm condition in (1) is an exact interval condition in \(t\) after fixing the other cells, because each \(m_i,n_i\) either includes that cell or is fixed. The largest-cell tie rule also gives an exact interval endpoint. The original primal and middle tests and the capacity steps give only a bounded number of intervals, as in DIVISOR_SIGN-v1. In particular the complement removes only the original middle equality, and the physical equality equation is fixed at these fixed ideal labels. Both radial arguments are fixed positive constants divided by \(E\). After removing the fixed scalar and row phase, the weight is \(E^{-2}G_W(c_0/E)\overline{G_W(c_1/E)}\). With \(t\) on its remaining dyad of length scale \(L=Y'/\prod_{\rm other}Nq_j\), its supremum plus integrated absolute derivative is \(O(\mathcal M_{24}(W)^2Y^{-2})\). All endpoints and norm fibres are kept.

Apply the inherited fixed-field deleted Möbius bound, equation (7) of DELETED_PRIME_MERTENS_AND_UNIT_CORRECTION-v1, by exact partial summation in that largest free cell. On a nonempty interval \(L\gg(Y')^{1/4}\), so the exponential factor can be bounded uniformly by \(\exp(-c_\kappa\sqrt{\log(2Y')})\). The sum at fixed other free cells is bounded by the common profile factor times
\[
 O\!\left(Y^{-2}L\,\log^C(2D)\exp(-c_\kappa\sqrt{\log(2Y')})\right).
\]
Summing the remaining at most three free cells uses the harmonic weights \(1/Nq_j\) from \(L\). These add only logarithms. The original fixed-label scalar, including both wide corrections, is therefore bounded by
\[
 O\!\left(
  \mathcal M_{24}(W)^2
  \frac{4^{\omega(\delta)}}{Y\,N\delta}\,
  \log^{C'}(2D)\exp(-c_\kappa\sqrt{\log(2Y')})
 \right).                                                       \tag{2}
\]
The fixed-data constants include the original polynomial clip and the stated \(\kappa\). The same argument bounds each of the three terms involving at least one wide correction. The passive case \(\delta=1\) and fixed bounded active intersections are included.

This uses only the existing fixed-field input after an exact change of the divisor variables. The saving in (2) is subpower. The comparison fixes the actual row and other ideal labels before summing the remaining divisor, so it does not estimate the coherent cross in which those labels and the row must still interact. In particular the wide correction remains unestimated at the target power in the full selected pure core.

