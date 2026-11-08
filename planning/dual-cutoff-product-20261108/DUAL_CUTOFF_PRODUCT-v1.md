# Averaging the dual of the unused factor in the cutoff product

8 November 2026 UTC. Author checked, independent review pending. The small cutoff-product amplitude of SMALL_CUTOFF_PRODUCT-v2 admits a stronger bound if the dual sum from Poisson is averaged over the actual rows. The resulting estimate treats larger cutoff products at the mixed scales and the unit product at the pure scales.

## 1. Setting and estimate

Keep the original Eisenstein field, the fixed set \(S\) and finite-order \(\nu\) supported there, one \(W\in C_c^\infty((0,\infty))\) supported on \([1,2]\), and the original good squarefree annulus. Use \(U^2\le D\le 7U^2/2\). Use the original unweighted two-pivot rows with fixed literal \(S\)-part \(u_0\), \(A_i\le Nv_i<2A_i\), and all original coprimality, ray and capacity selections for the good part \(v_1v_2^2\). The primitive row character \(\psi_u\) induced by \(\nu(\cdot)\chi_{\cdot}(u)\) is assumed nonprincipal on every row in the block. Write \(R=A_1A_2\), \(Q_u=N\mathfrak f_u\) for its primitive conductor norm, and
\(\mathcal M_{12}(W)=\max_{0\le j\le12}\|(x\partial_x)^jW(x)\|_\infty\).
The original family has \(Q_u\asymp_{S,\nu,u_0} R\). Indeed the good conductor is \(v_1v_2\) since the two good valuations \(1,2\bmod 6\) give ramified local characters, with tame conductor exponent one, and the \(S\)-part is bounded. The norm comparison below uses the physical \(v_1\)-sieve with \(v_2\) fixed. It does not use an identification of the full mixed family with its conductor radical.

For a good squarefree intermediate divisor \(d\), \(V_{d,\le Z}\) is the row amplitude of SMALL_CUTOFF_PRODUCT-v2 from the actual ordered cutoffs \(Nx,Ny\le U,\ N(xy)\le Z\). We prove
\[
 \frac{\|V_{d,\le Z}\|_2^2}{D}
 \ll_\epsilon (DH)^\epsilon \mathcal M_{12}(W)^2\,
       \frac{Z}{Nd}\,A_2\Phi_6(A_1,\sqrt R), \tag{1}
\]
where \(\Phi_6(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}\) is the pinned sixth-free sieve of phy:input. Constants also depend on the fixed arithmetic data. A zero amplitude makes the estimate trivial. The sum over all \(d\), optionally with any real selector between zero and one, satisfies the same estimate without \(1/Nd\) after harmonic summation. This is a bound on the positive squared norm of the specified part of the coefficient.

## 2. A row norm for the masked ordinary ideal sum

We first use a direct consequence of phy:input. At a length \(B\ge1/2\), bounded coefficients of magnitude at most one, supported on good ideals of norm at most \(2B\), give a squared row norm
\[
 \ll_\epsilon (A_1A_2\max(1,B))^\epsilon\,
             B A_2\Phi_6(A_1,\max(1,B)).
 \tag{2}
\]
Here the characters are \(\psi_u\) on good ideals, or their conjugates. To prove this, fix \(v_2\). On good ideals \(\psi_u\) agrees with the literal raw symbol times \(\nu\), including zeros since all good primes of \(u\) are in its primitive conductor. Split an arbitrary good column \(b=b_0 q^6\) by the unique valuation remainders, with \(b_0\) sixth-free. Fix \(q\), keeping its sixth-power raw row mask and its fixed \(\nu(q)^6\), even if \(q,b_0\) share primes. The coefficients of \(b_0\) after fixing \(v_2,q\) and the fixed \(u_0\)-part are independent of \(v_1\). The squared coefficient mass is \(O(B/(Nq)^6)\) for a nonempty block. Use the true sixth-free comparison at scale \(O(B/(Nq)^6)\), and count the unit directly at subunit lengths. Apply Minkowski over \(q\) and sum \((Nq)^{-3}\). The final sum of squared norms over \(v_2\) costs \(O(A_2)\). Conjugation preserves this argument. Any original restrictions on the rows are only enlarged inside the positive norms. Row factors of modulus at most one can multiply the resulting row vector.

For fixed good squarefree \(d,z\) and \(C>0\), consider
\[
 J_{d,z}(C;u)=
   \sum_{(b,\,S d z u)=1}\psi_u(b)W(Nb/C).
\]
Since the good primes of \(u\) already give primitive zeros, and \(\psi_u\) is extended by zero on nonunits of its conductor, the full deletion is exactly
\[
 J_{d,z}(C;u)=
 \sum_{e\mid \operatorname{rad}(S d z)}\mu(e)\psi_u(e)
        \sum_a\psi_u(a)W(Na/(C/Ne)).
 \tag{3}
\]
Here the notation \(\operatorname{rad}(S d z)\) denotes the ideal product of the distinct primes in \(S\cup\operatorname{supp}(dz)\). The divisor list is common to the rows, including the fixed primes in \(S\) at which the primitive conductor may vary. In particular deleting a prime of \(S\) from the original amplitude is not undone when it drops out of the primitive conductor. Formula (3) uses multiplicativity with zero extension and does not need any primitive character information on \(e\) beyond that property.

We claim for the unmasked inner sum \(I(L;u)=\sum_a\psi_u(a)W(Na/L)\) that
\[
 \|I(L)\|_2\ll_\epsilon (DH)^\epsilon\mathcal M_{12}(W)
           \sqrt{L A_2\Phi_6(A_1,\sqrt R)},\qquad 0<L\le D. \tag{4}
\]
Changing the upper endpoint \(D\) to \(2D\) costs constants only. If \(L<1/2\) the sum vanishes. For \(1/2\le L\le\sqrt R\), split the ideals in \(I\) by their \(S\)-supported factor \(\mathfrak s\), and apply (2) to the good factor of length \(L/N\mathfrak s\) with the coefficient \(W(N\mathfrak s\,N b/L)\). The row multiplier \(\psi_u(\mathfrak s)\) stays with each \(\mathfrak s\), including zeros. Minkowski and
\(\sum_{\mathfrak s\ S\text{-supported}}(N\mathfrak s)^{-1/2}<\infty\)
give (4).

For \(L>\sqrt R\), use radial Poisson at the primitive conductor. Let \(h(z)=W(|z|^2)\) on \(\mathbb C\simeq\mathbb R^2\) and take the Euclidean Fourier transform with phase \(e^{-2\pi i x\cdot\xi}\). With \(f_u\) any ideal generator of \(\mathfrak f_u\), the trace pairing \(\operatorname{Tr}(kz/(\delta f_u))\), \(\delta=1+2\omega\), corresponds to a Euclidean frequency of squared length \(4Nk/(3Q_u)\). The lattice \(f_u\mathcal O\) has covolume \((\sqrt3/2)Q_u\). Since the finite-order ideal character is unit-trivial, an ideal sum is \(1/6\) of its nonzero element sum. Poisson on every residue class, followed by the primitive Gauss identity mcs:gauss, gives
\[
 I(L;u)=\frac{2L}{\sqrt3\,\sqrt{Q_u}}\gamma_u
         \sum_{k\ne0\ {\rm ideal}}\overline{\psi_u(k)}
                       G(LNk/Q_u),\qquad
 G(x)=\widehat h\bigl(\sqrt{4x/3}\,e_1\bigr). \tag{5}
\]
Here \(|\gamma_u|=1\) is the normalized primitive Gauss sum in this pairing. Radiality removes the rotation of the generator. Both sides count ideal labels, including distinct ideals of equal norm. The dual zero frequency is absent by nonprincipality. The primitive Gauss coefficient is zero at every nonunit frequency, including at the \(S\)-part of its conductor.

For \(0\le j\le2\), compact support and Fourier integration by parts give
\(\|(x\partial_x)^jG(x)\|\ll \mathcal M_{12}(W)(1+x)^{-4}\) pointwise. For \(x\ge1\) this follows by differentiating the transform at most twice in the Euclidean frequency and integrating by parts at least ten times. Multiplication by the frequency of degree at most two still gives the required decay. For \(x\le1\) the transform and its first two radial derivatives are bounded. In a dyad \(K\le Nk<2K\), \(K=1,2,4,\ldots\), multiply \(G(e^x)\) by a smooth cutoff in \(x-\log(LK/R)\) equal to one on the fixed interval containing all \(\log(LNk/Q_u)-\log(LK/R)\). This interval is fixed by the conductor comparability. Two log derivatives give Fourier \(L^1\) mass
\(O(\mathcal M_{12}(W)(1+LK/R)^{-4})\).
Inverting on this dyad separates the row factor \(Q_u^{-it}\) and column factor \((Nk)^{it}\), both of modulus one. This step does not replace \(Q_u\) by \(R\) inside the profile. The factor \(\gamma_u\) stays with its row, and \(Q_u^{-1/2}\ll R^{-1/2}\) is used only in the row norm.

For each separated column coefficient split \(k=\mathfrak s b\) into its \(S\)-supported and good parts. The row multiplier \(\overline{\psi_u(\mathfrak s)}\) keeps the exact \(S\)-phase or zero. Apply (2) to the good dyadic subsequence at length \(K/N\mathfrak s\), then sum square roots using the convergent product over \(S\). The bound on the dyadic dual row norm before its profile factor is \(O_\epsilon((A_1A_2 K)^\epsilon\sqrt{K A_2\Phi_6(A_1,K)})\). Put \(M=R/L\), so \(M\le\sqrt R\) in the dual range. For \(K\le M\) one can bound \(\Phi_6(A_1,K)\) by its value at \(\sqrt R\) and sum the square roots of the relative lengths. For \(K\ge M\) use
\[
 \Phi_6(A_1,K)\le \max(1,K/M)\,\Phi_6(A_1,\sqrt R).
\]
The dyadic sum with the factor \((1+K/M)^{-4}\) is then bounded by a constant times \(\sqrt{M A_2\Phi_6(A_1,\sqrt R)}\) up to subpowers. If \(M<1\) this uses only the latter inequality and works with the first dyad \(K=1\). Infinite-frequency subpowers are absorbed by the same decay. Multiplying by \(L/\sqrt R\) proves (4).

For (3), apply (4) with \(L=C/Ne\). The extra row multiplier \(\psi_u(e)\) is bounded by one and retains its own zeros. By Minkowski and the divisor bound, whenever \(C\le 2D\) and \(N(dz)\le2D\),
\[
 \|J_{d,z}(C)\|_2\ll_\epsilon (DH)^\epsilon\mathcal M_{12}(W)
                   \sqrt{C A_2\Phi_6(A_1,\sqrt R)}. \tag{6}
\]
This proof performs the direct or dual comparison at the length **after** each deletion factor. It covers all \(C\) in the displayed range with the same fixed profile seminorm.

## 3. Inserting the exact squarefree projector

Use the exact \(d,z\) allocations of SMALL_CUTOFF_PRODUCT-v2, with coefficient \(\beta_{d,U,Z}(z)\) independent of \(u\) and of the unused factor. Expand that unused squarefree factor as \(r^2 b\) by Möbius inversion. The exact \(b\)-sum is \(J_{d,z}(C;u)\) at \(C=D/(Nd\,Nz\,(Nr)^2)\). The external row factor includes \((d,u)=1\), the raw \(z\)-symbol, \(\psi_u(r)^2\), and the full \((r,Sdzu)=1\) condition. Its magnitude is at most one after removing \(\beta_{d,U,Z}(z)\) and \(\mu(r)\). In particular there is no additional disjointness between \(r\) and \(b\). All actual norms and cutoffs are kept. If this sum can be active, \(N(dz)\le2D\).

Use dyads \(J\le Nz<2J\) and \(T\le Nr<2T\) up to the exact original support. Estimate the \(b\)-sum by (6) and take Minkowski over \(z,r\) in the actual row norm. There are \(O(J)\) and \(O(T)\) ideals in the respective dyads. After squaring and dividing by \(D\), their contribution is bounded by a constant times
\[
 \frac{J^2 T^2}{D}\frac{D}{Nd\,J T^2}\,
       A_2\Phi_6(A_1,\sqrt R)
\]
with the profile and subpower factors of (1). The coefficient divisor bound and the dyadic sums are absorbed by smaller internal subpowers. Since \(J\le Z\), this proves (1).

## 4. Consequences and signed cross term

At the mixed scales \(A_1\asymp D^{5/12}\), \(A_2\asymp D^{1/6}\), the four powers in \(A_2\Phi_6(A_1,\sqrt R)\) are \(7/12,11/24,11/18,79/144\). Thus the positive sum over intermediate divisors costs
\(O((DH)^\epsilon\mathcal M_{12}(W)^2 Z D^{11/18})\).
The cutoff \(Z=D^{1/8}\) gives power \(53/72\), with margin \(1/72\) below the critical \(3/4\). This conclusion is stable when each mixed pivot log exponent varies by \(1/2000\) with feasible capacities. At the exact mixed scales, \(Z=D^{5/36}\) attains the target up to subpowers. The fixed-field \(7/8\) hypothesis is unnecessary.

At the pure point \(A_1\asymp D^{3/4}\), \(A_2\asymp1\), the four powers are \(3/4,3/8,3/4,9/16\). The unit product \(Z=1\), or any bounded \(Z\), now meets the target in the positive sum over \(d\). This conclusion uses the nonprincipal pure block and the pinned sieve. The factor \(Z\) in (1) remains for growing cutoff products.

For \(d=1\), at these cutoffs the full amplitude meets its target if and only if its exact complementary larger-product amplitude does, by the norm triangle in both directions. For the signed sum over \(d\), combining the new mixed small-product bound with the inherited complementary positive bound \(D^{13/12+\epsilon}\) only gives a cross bound \(D^{61/72+\epsilon}Z^{1/2}\) with fixed profiles. This remains above the target. The larger-product amplitude, its signed cross term, and the full signed form remain open. The new row comparison applies to the unused factor with its actual masks and profile. It does not supply cancellation in the two cutoff divisors themselves.
