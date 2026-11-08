# Matched good-prime phases in the original Poisson cross

8 November 2026 UTC. Use the original unweighted nonprincipal two-pivot Eisenstein rows, fixed \(S,\nu,u_0\), full ordered cutoff \(Z=U^2\), \(U^2\le D\le7U^2/2\), \(1\le R=A_1A_2\le H\le D\), and one common smooth complex \(W\) supported on \([1,2]\). Keep \(Q_u\asymp R\) and all literal, squarefree, ray, capacity and raw character conditions. Put \(E=Nd\) for the intermediate squarefree Möbius divisor \(d\). Ideals and conjugate prime labels are distinct even when their norms agree.

Let \(V_d\) be the full original row vector and \(E_d\) its equal-norm middle Poisson projection from GROUPED_EQUAL_CROSS-v4. Consider the exact normalized cross \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle E_d,V_d-E_d\rangle\). Use the same Poisson formula also on the original direct part of the second side, discarding the same primal-zero allocations beforehand. The estimates concern selected pairs in this representation of the cross.

## Exact matching of the good exponent patterns

On both sides put \(h=re_0\). This is good squarefree and prime to \(d,z_0\). At fixed \(d,e_1,h,z_0,k\) the grouped coefficient is \(\mu(h)\sum_{e_0\mid h}\beta_{d,U,U^2}(e_0z_0)\) with the original allocation selectors. It is row independent and divisor bounded independently of \(k\); \(Nh\ll\sqrt{D/E}\) by the primal-zero test and \(Nz_0\le D\). The scalar is \(2D\gamma_u/(\sqrt3 E Ne_1 Nz_0 (Nh)^2\sqrt{Q_u})\), and the profile argument is \(D Nk/(E Ne_1 (Nh)^2 Q_u Nz_0)\). The row phase is \(\psi_u(h)^2\psi_u(e_1)\psi_u(z_0)\overline{\psi_u(k)}\), with the original sign \(\mu(e_1)\) and mask on \((d,u)\). All \(S\)-values and repetitions of \(k\) are retained.

Use subscript 0 on the equality side, where \(z_{0,0}=g\ell,\ k_0=g\bar\ell\), so its phase contains the mask \(|\psi_u(g)|^2\). Use subscript 1 on the partner side with \(z=z_{0,1}\), \(k=k_1=k_S k_{\rm g}\) split into \(S\)-supported and good parts. Write \(e_{1,i}=s_i j_i\) with \(s_i\mid\operatorname{rad}(S)\) and \(j_i\mid d\), and keep the full \(E_i=Ne_{1,i}\) for \(i=0,1\) in this note. Set \(h_0=f a,\ h_1=f b\) with \(f=(h_0,h_1)\). The factors \(f,a,b\) are pairwise coprime and squarefree, \(b\perp z,\ a\perp\ell\), and \(f,a,b,z,\ell\) avoid \(d\).

If the good exponent vectors of the two phases agree modulo six, the valuation of the partner good frequency must satisfy
\[
 v_p(k_{\rm g})\equiv v_p(z)+4v_p(a)+2v_p(b)-v_p(\ell)
       +v_p(\bar\ell_{\rm g})+v_p(j_1)-v_p(j_0)\pmod 6 .                \tag{1}
\]
Here \(\bar\ell_{\rm g}\) is the good part of the conjugate. Put \(j=(\bar\ell_{\rm g},d)\), \(c=(z,a,\bar\ell_{\rm g})\), \(a_0=a/c\), and \(\ell_0=\ell/(\ell,zb)\). Let \(q_d\) have exponent \(r_p\in\{0,\ldots,5\}\) at \(p\mid d\), the residue of \(v_p(j)+v_p(j_1)-v_p(j_0)\), and no other primes. Then the unique sixth-free representative is
\[
 k_\flat=\frac{z a^4 b^2 \ell_0^6(\bar\ell_{\rm g}/j)\,q_d}{\ell c^6}. \tag{2}
\]
At a prime of \(\ell\), the exponent before reduction is \(-1\) only when the prime is absent from \(zb\). At a prime of \(\bar\ell_{\rm g}\) outside \(d\), the only overflow is \(1+4+1=6\) on \(c\). On \(d\) only the conjugate and \(j_i\) factors in (1) may occur. This verifies (2) with valuations in \(0,\ldots,5\). Every matching \(k_{\rm g}\) is \(k_\flat v^6\) for a unique good integral ideal \(v\), with no disjointness condition on this sixth-power factor. Matching good exponents does not equate \(\nu\)-phases or the \(S\)-values and does not restore any raw zero.

With \(L_i=D/(E E_i R)\), the equality and partner profile scales, respectively, are comparable by fixed constants to
\[
 y_0=\frac{L_0}{(Nf)^2(Nc)^2(Na_0)^2},\qquad
 y_1=L_1\frac{(Na_0)^4}{(Nf)^2(Nc)^2}(N\ell_0 Nv)^6
                               \frac{Nq_d}{Nj}\,Nk_S .                \tag{3}
\]
The quotient \(N\bar\ell_{\rm g}/N\ell\) omitted from \(y_1\) lies in a fixed compact positive interval since \(\ell\) is squarefree and the missing factors are in fixed \(S\). The \(b\)-factor cancels only in the argument. The actual arguments retain \(Q_u\). The two normalized scalars, after the \(O(R)\) row count, have absolute product bounded by
\[
 \frac{O(D)}{E^2 E_0 E_1\,Ng N\ell Nz\,(Nf)^4(Na)^2(Nb)^2}.
 \tag{4}
\]
Here \(Q_u^{-1}\) has been bounded by \(O(R^{-1})\). The common root cancels. Keep the two profile bounds \(\mathcal M_{12}(W)(1+y_i)^{-4}\). Absorb the divisor costs for polynomial labels in \((DH)^\epsilon\).

## Target bound for the matched pairs

For the matched pairing, use both radial profiles in (3), bounded by \(O(\mathcal M_{12}(W)^2 y_0^{-1/2}y_1^{-1/2})\). In (4) this leaves the scale \(R/(E\sqrt{E_0E_1})\) and the weight
\[
 \frac{(Nj)^{1/2}}{(Nq_d)^{1/2}}\,
 \frac{1}{Ng N\ell Nz\,(Nf)^2 (Na_0)^3 (Nb)^2 (N\ell_0)^3 (Nv)^3\, (Nk_S)^{1/2}}.
 \tag{5}
\]
The \(c\)-power cancels and the \(v\)-sum converges without clipping. The harmonic \(g,z,\ell\) counts have only logarithmic cost since their original lengths are polynomial. There are divisor-many \(c\mid\bar\ell_{\rm g}\). At fixed \(j\mid d\), \(\bar j\mid\ell\) pays \((Nj)^{-1}\) in the harmonic sum. The \(f,a_0,b,v\) sums converge and \(k_S\) costs a fixed geometric product. The \(j,j_0,j_1\) choices have divisor cost. Thus the per-divisor normalized matched contribution is \(O((DH)^\epsilon\mathcal M_{12}(W)^2 R/E)\), even in absolute value over its pairs. Sum harmonically in \(d\).

For the stronger unit-divisor value one can sum \(f\) first, using
\(\sum_f (Nf)^{-4}(1+A/(Nf)^2)^{-4}\ll A^{-3/2}\) for \(A>0\). For \(A\ge1\) split at \(\sqrt A\), and for \(A<1\) use the trivial convergent sum. With \(d=1\), (3)–(4) now give scale \(R^{3/2}D^{-1/2}\) and powers \(Nc^{1}, (Na_0)^{-8}, (Nb)^{-2}, (Nv)^{-9}, (Nk_S)^{-3/2}\), in addition to the harmonic factors. The factor \(Nc\) is paid by \(c\mid z\) in the harmonic \(z\)-sum. The \(e_{1,i}\) are fixed \(S\)-supported choices. The resulting bound at \(d=1\) is \(O((DH)^\epsilon\mathcal M_{12}(W)^2R^{3/2}/\sqrt D)\), with pure power \(5/8\). No cancellation of signed \(d\)-terms is used. Both estimates allow arbitrary eligible or ineligible equality \(\ell\) and include the re-expressed direct partner.


## Nonprincipal good phase with bounded conductor

For this section use the complete original row interval: for each fixed \(v_2,u_0\), the variable \(v_1\) runs over all good squarefree ideals in the original norm and capacity interval, with the stated ray and common-prime restrictions. Finite row classes are permitted. No arbitrary additional subset or row weight is inserted. In the critical pure and mixed blocks \(v_1\ne1\), so the nonprincipal condition follows from the good conductor. All bounds here are for these blocks with \(A_1 A_2^2\ll H\).

Let \(\mathfrak q\ne1\) be the squarefree good ideal of primes at which the exponent vectors differ, and \(Q=N\mathfrak q\). Fix its nonzero difference residues, at most \(5^{\omega(\mathfrak q)}\) choices. The good frequency has a unique sixth-free representative \(k_\flat'\) with the valuations \(\beta'_p\in\{0,\ldots,5\}\) obtained from (2) by changing the residues on \(\mathfrak q\) alone. Write \(\beta_p=v_p(k_\flat)\). Applying the same two radial profile weights as in (5), the ratio at \(p\in\mathfrak q\) is \((Np)^{(\beta_p-\beta'_p)/2}\).

The local changes can be paid from (5), leaving a net \(Q^{-1/2}\). Partition the labels at primes of \(\mathfrak q\) into the following states, at divisor cost.

- Off \(d\), if \(\beta_p=0\), the new positive \(\beta'_p\) gives the saving directly. For \(p\mid\ell\) and \(\beta_p>0\), either \(\beta_p=5\) and \(p\mid\ell_0\), or \(\beta_p=1\) and \(p\mid b\). Their respective inverse cube and inverse square weights pay the change and the saving.
- Off \(d\ell\), if \(p\mid a\) and \(\beta_p>0\), then \(p\mid a_0\) and \(\beta_p\in\{4,5\}\), paid by the inverse cube on \(a_0\). If \(p\mid b\), then \(\beta_p\le3\), paid by the inverse square on \(b\). In the remaining case \(\beta_p\) comes from \(z\) and \(\bar\ell_{\rm g}\), with exponent one for each incidence. Use the harmonic \(z\)-count for \(p\mid z\) and the harmonic \(\ell\)-count for \(\bar p\mid\ell\), using both when both occur.
- On \(d\), after the \(\bar j\)-divisibility in the harmonic \(\ell\)-sum, the local exponent is \(-(\beta'_p+v_p(j_0)+v_p(j_1)+v_p(j))/2\). If \(\beta'_p=0\), the residue changed, so at least one of \(j,j_0,j_1\) contains \(p\).

For \(a_0,b\) one can retain a convergent sum after paying the specified powers by using the forced divisibilities: \(\sum_{q'\mid a_0}(Na_0)^{-3}\ll (Nq')^{-3}\), and likewise for \(b\) at exponent two. Each harmonic sum uses the product of the forced distinct ideals. The \(\ell\)-divisibilities from off \(d\) use conjugates of primes outside \(d\), distinct from the conjugates of primes in \(j\). The cases \(p\mid\ell\) charge only \(b\) or \(\ell_0\), without demanding a second \(\ell\)-divisor. Once the \(Nc\) power cancels in (5), \(c\) is only a divisor choice at fixed \(\ell\), requiring no payment from \(z\). Thus before cancellation in the rows, the normalized comparison at fixed \(\mathfrak q,d\) is \(R/(E Q^{1/2})\) up to the stated profile and subpower costs. All row phases and masks have been retained; enlargements occur only in the positive counts.

We now replace the trivial row count by a signed estimate. At fixed labels the good part of the phase product is a primitive residue character on the literal element \(\alpha_{v_1}\) modulo \(\mathfrak q\): each nonzero local exponent gives a nontrivial character of the good residue field. Fix \(v_2\) and partition \(\alpha_{v_1}\) into the finite congruence classes at a fixed modulus supported on \(S\) that determine the literal ray and local Kummer types. This uses units at \(S\) and a fixed sufficiently deep congruence of sixth powers there. It freezes the primitive \(S\)-values, including zeros, and \(Q_u/(Nv_1Nv_2)\). The good conductor of the original row is exactly \(v_1v_2\). The common Gauss root cancels. Factors on \(u_0,v_2,\nu\) remain fixed multipliers in these sums.

It suffices for this row estimate to use \(Nk\le D^5\). In fact on a live grouped term the primal-zero test gives \(D/(E E_1(Nh)^2)>1/4\), so its profile argument is \(\gg Nk/D^2\) since \(Nz\le D,\ Q_u\ll D\). The absolute profile sum for \(Nk>D^5\) is \(O(D^{-7}\mathcal M_{12}(W))\) by ideal counting and four powers of decay. Summing the other variables by their harmonic or convergent scalar weights in (4) costs \(O(D(DH)^\epsilon)\). This tail is negligible for the whole cross or any restriction on its pair labels. All raw deletion labels in the row completion are therefore polynomially bounded, and no conductor term depends on an unbounded divisor multiplicity.

Expand the squarefree row condition by \(s^2\mid v_1\), with \((s,\mathcal F)=1\), where \(\mathcal F\) is the complete good forbidden-prime union from the two summands, \(d,v_2\) and \(\mathfrak q\). This restriction is valid on the original raw support. Expand the remaining good deletion over \(e\mid\operatorname{rad}(\mathcal F\setminus\operatorname{supp}\mathfrak q)\); the character handles the primes of \(\mathfrak q\). Hence \(e\perp s,\mathfrak q\). Write \(\alpha_{v_1}=\alpha_e\alpha_s^2 x\) with the primary generators. The \(S\)-congruence of \(x\) is then fixed, and the row interval becomes a clipped norm interval with upper scale \(L\asymp A_1/(Ne(Ns)^2)\). The residue-character factors at \(e,s\) are retained.

Here is an elementary sharp disk estimate for that fixed congruence. For a disk of norm bound \(L\) with \(L\ge 1/2\), the primitive \(\mathfrak q\)-character sum is
\[
 \ll (DH)^\epsilon\min\{L,(LQ)^{1/3}\}                               \tag{6}
\]
with the trivial unit convention. For the smooth comparison, if \(Q\le L^2\), convolve the disk indicator with a smooth bump of unit integral and spatial width \(\Delta=Q^{1/3}L^{-1/6}\le\sqrt L\). The difference from the exact indicator is supported in a shell of integer norms of width \(O(1+\sqrt L\Delta)\). Each norm has at most divisor-many lattice elements, so the difference costs \(O((DH)^\epsilon(1+\sqrt L\Delta))\), including any exact boundary nodes. Complete the smoothed sum modulo the product of \(\mathfrak q\) and the fixed \(S\)-modulus, and apply lattice Poisson with the fixed inverse-different pairing. CRT and primitive Gauss sums give normalized coefficient at most \(O(Q^{-1/2})\), no zero mode, and a dual lattice with spacing comparable to \(Q^{-1/2}\). The disk transform is \(O(L^{1/4}|\xi|^{-3/2})\) for \(\xi\ne0\); it follows by integrating the circular slices \(2\sqrt{1-x^2}\) of the unit disk once by parts and splitting the endpoint singularity at distance \(|\xi|^{-1}\) before one further integration in the interior. Scaling gives the stated \(L\) factor. The bump gives \((1+\Delta|\xi|)^{-M}\) for fixed \(M>2\). Counting dual points in annuli bounds the nonzero sum by \(O(L^{1/4}Q^{1/2}\Delta^{-1/2})\). Both costs are \(O((DH)^\epsilon(LQ)^{1/3})\). For \(Q>L^2\) the trivial count suffices. Subtract two such estimates for the original annulus, choosing open or closed endpoints and retaining the counted boundary shell.

Sum (6) over \(s\) for each \(e\), using the split \(Ns=\sqrt{A_1/(Ne\sqrt Q)}\). Below it the \((Ns)^{-2/3}\) count gives \(O(\sqrt{A_1/Ne}\,Q^{1/4})\), and above it the \((Ns)^{-2}\) tail has the same bound. If the split is subunit the trivial sum suffices. After the divisor cost of \(e\), the sharp row sum is \(O((DH)^\epsilon\sqrt{A_1}Q^{1/4})\) per fixed \(v_2,S\)-class. The profile product times \(Q_u^{-1}\) is a function of \(Nv_1\) on that class. Its supremum plus variation on the interval is \(O(R^{-1}\mathcal M_{16}(W)^2(1+y_0)^{-4}(1+y'_1)^{-4})\), by one log derivative of the radial Schwartz estimates, with the actual perturbed partner scale \(y'_1\). Exact partial summation transfers the signed row estimate to this weight. Summing the \(O(A_2)\) fixed \(v_2\) choices thus replaces the trivial row count in (4) by a relative \(O((DH)^\epsilon Q^{1/4}/\sqrt{A_1})\).

Combining the local \(Q^{-1/2}\) saving, the signed row estimate and the harmonic \(d\)-sum, the normalized contribution of all \(1<N\mathfrak q\le F_0\) is
\[
 \ll (DH)^\epsilon\mathcal M_{16}(W)^2
               \frac{R}{\sqrt{A_1}}\,F_0^{3/4}.                    \tag{7}
\]
Here \(Q^{1/4-1/2}=Q^{-1/4}\) and the additional power one is the ideal count, including the divisor cost of residue choices. In the critical pure and mixed blocks \(R/\sqrt{A_1}\ll D^{3/8}\) by the physical capacity. Therefore \(F_0=D^{1/2}\) gives \(D^{3/4+\epsilon}\) for the selected cross, including \(d=1\) and arbitrary eligible equality overlap. This cutoff refers to the good primitive conductor of the character on the row variable in the pairing, rather than either original \(Q_u\). The matched sector \(\mathfrak q=1\) was bounded separately. The signed large-\(\mathfrak q\) pairing and the whole original signed estimate remain open.

