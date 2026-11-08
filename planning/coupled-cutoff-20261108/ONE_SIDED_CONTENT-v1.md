# One-sided rational content in the coupled pure cross

8 November 2026 UTC. Candidate corollary of the coupled cutoff and joint powerful insertion proof in this directory. Work only at the pure critical scales \(A=A_1\asymp R\asymp D^{3/4}, A_2\asymp1\) and \(B,K\asymp R\), in the original selected erasure sector. Keep all increments 1 through 5, the actual \(d\)-residues, the common \(W\) and every original raw row restriction. Inherited factor: \(O_{\epsilon,S,\nu,u_0}((DH)^\epsilon\mathcal M_{24}(W)^2)\). Nothing below alters the other dyads or the whole signed bound.

Let \(b\) be the exact rational content of the erased cutoff ideal \(x\): \((b)\mid x\) and no larger rational integer divides \(x\) as a principal ideal. Take \(D^c\le b<2D^c\), \(0\le c\le1/24\). The relative rectangular loss over \(R\) can be taken as \(D^\rho\) with
\[
 \rho=\frac1{17}-\frac{25c}{102}.
\]
For this content dyad the normalized selected all-divisor bound is \(D^{3/4+\rho+\epsilon}\); the target holds on \(Nd\le D^{1/4-2\rho}\) and separately on \(Nk_*\ge D^{2\rho/7}\) over all \(d\). At \(c=0\) these agree with the content-free coupled comparison. At \(c=1/24\) the older one-sided content comparison has the same relative exponent \(7/144\); for larger content use that older result. The statement applies even if the insertion has small rational content.

## Exact content with an opened cutoff

Fix \(b\), write \(x=(b)x^\circ\), and keep the raw row phase of \((b)\). The insertion must avoid \((b)\), a fixed deletion because \((x,I)=1\) on the desired support. All norm and coefficient tests use \(Nx=b^2Nx^\circ\); the inverse \(Nx\) is never replaced by the inverse residual norm. Since \(x\) is squarefree, \(x^\circ\) is squarefree and avoids \((b)\), and exact content means that \(x^\circ\) has content one. The squared \(x^\circ\) coefficient mass after common shortening \(s\) is \(O((DH)^\epsilon/(BD^{2c}Ns))\) and the length is \(O(B/(D^{2c}Ns))\). When the joint powerful tail also uses the \(x^\circ\)-shortening \(h\) against the powerful factor, divide both the mass and the length by \(Nh\). This follows from the original \(1/Nx\) and elementary ideal count on live dyads. There are \(O(D^c)\) choices of \(b\); this cancels the extra inverse \(D^c\) from the norm. The powerful tail uses the exact content as an arbitrary \(x^\circ\)-coefficient test.

For the smoothed dual branch, fix \(P,s,e,r'\) as in the coupled proof; \(P\) is the powerful insertion and \(s\) is the common divisor of \(x^\circ,I_1\). The latter is the squarefree increment-one part of the insertion. Write \(x^\circ=s x'\). The content test requires \(s\) itself to be rationally primitive. Any inert prime or both primes over a split rational prime in \(s\) make the term empty. For each split prime with one factor in \(s\), \(x'\) must avoid both primes over it (one already from squarefreeness). The residual \(x'\) must be rationally primitive. These statements are equivalent to exact content because the ramified prime is excluded by \(S\) and all variable ideals are squarefree. Impose the remaining rational primitivity by
\[
 1_{\operatorname{content}(x')=1}
 =\sum_{z\in\mathbb Z_{\ge1}:\ (z)\mid x'}\mu_{\mathbb Z}(z).
\]
Freeze \(z\) and strip \((z)\) from \(x'\), retaining individual deletion of its support. There is **no** new insertion deletion at \(z\): terms of the earlier common-divisor expansion can have \(z\)-support overlap with the insertion, and raw values remain exact. The norm of the principal ideal \((z)\) is \(z^2\). The extra shortening of the \(x\) count and its original inverse norm give \(z^{-1}\) in the two moment budget; summing \(z\) is harmonic on polynomial support.

Allocate the prime ideals of \((b),s,(z)\) and of the fixed cutoff base to the two actual cutoff factors, at divisor cost. The residue factors exclude all stripped primes and the required conjugate deletions of \(s\). Their remaining coprimality is the same squarefree \(w\) projector as before, keeping the residual factors squarefree and individually avoiding \(w\). No radial cutoff changes. The dyadic log separators operate on the actual norm products with these factors frozen. Thus with shorter and longer log lengths \(u_s,u_l\) in the smoothed dual,
\[
 u_l\le\tfrac12,\quad
 u_s\le\tfrac38-c-\tfrac n2,\quad
 u_s+u_l\le\tfrac34-2c-n
\]
up to fixed length constants, where \(n=\log_D Ns\). In the norm calculation \(X_s X_l\asymp B/(b^2 z^2 Ns(Nw)^2)\); multiplying the dual \(\sqrt L\) by the remaining cutoff inverse factors gives the previous harmonic factors times \(1/(bz)\). Unit and constant-scale live fibres satisfy the same estimates after fixed constants. No derivative of a sharp cutoff or of a rational content coefficient is used.

## Length budgets

Write \(m=\log_D M\) for the powerful dyad \(M\le NP<2M\), \(j=\log_D Ne\) and \(p=\log_D Nr'\). Define
\[
 \sigma_c=\frac14-2\rho-\frac{2c}{3}=\frac9{68}-\frac{3c}{17},\quad
 n_0=\frac3{136}-\frac{9c}{17},\quad
 j_0=\frac1{136}-\frac{3c}{17}.
\]
As in the parent, if \(n\ge n_0\), the original sharp insertion bound and shortened \(x^\circ\)-sieve give excess at most \(\max(0,1/16-c/3-n/6)\le\rho\). If \(j\ge j_0\), the fixed-\(P\) squarefree and deletion expansion with the sharp subinterval moment gives excess at most \(1/16-c/3-j/2\le\rho\). For the large-\(r'\) branch keep the grouping before freezing \(P\). With \(p_0=\max(0,\sigma_c-m/2)\), the sparse gain of the grouped insertion mass is \(D^{-m/4-p_0/2}\). Each raw sieve factor can be bounded by its unshortened dyadic length, except that the \(x^\circ\) length still saves \(D^{2c}\). Thus the relative excess is at most \(1/8-c/3-m/4-p_0/2\le\rho\). The fixed \(h\) and fixed deletion sums are as in the joint powerful proof. If \(p_0=0\) this grouping covers the entire squarefree expansion; no smoothed branch is needed.

Otherwise use the smoothed disk on \(n\le n_0,\ j\le j_0,\ p\le p_0\), with relative width proportional to \(D^{-\beta}\) and
\[
 \beta=\sigma_c-m/3-2n/3-4j/3-2p/3.
\]
The actual insertion residual length \(L\) has exponent \(l=3/4-m-n-j-2p\ge31/68+18c/17\), and \(\beta\ge1/51+9c/17>0\). The shortened \(x^\circ\)-length and \(L\) both lie above the physical-sieve threshold \(D^{3/8}\), up to fixed constants. The thin-shell main term has exponent
\[
 1/8-c/3-m/6-n/3-2j/3-p/3-\beta/2=\rho.
\]
The additive shell term has excess \(-l/6-c/3-n/6-j/2\), as before relative to the shortened mass and the \(O(\sqrt M)\) fixed-\(P\) count. The dual cutoff exponent \(t=m+n+j+2p+2\beta\) is at most \(8\sigma_c/3\). Both grouped lengths are below \(D^{3/4}\) at the cutoff. The excess from their geometric mean is at most
\[
 \tfrac16\max(1/8,t-c)\le \rho.
\]
The inequality follows by substitution since \((8\sigma_c/3-c)/6=\rho\), and \(\rho\ge7/144>1/48\). The original smoothing tail permits geometric summation above the cutoff. The fixed-\(P\) count cancels its shortening factor in this branch.

The separate equality subtraction is counted at physical \(NI\) and \(Nx\), before any sums over \(P\) or the rational-primitivity projector. The same per-\(d\) \(O(R/E)\) bound follows by the original integer norm-fibre count, since the content filter only deletes terms. The remaining radial comparisons and label charges give \(D^{3/4+\rho}/E\), with \((1+Nk_*)^{-7/2}\) available, or \(D^{5/8+\rho}/\sqrt E\). This proves the claimed selections after the harmonic or square-root divisor count. The raw paired phases, \(d\)-sign and both endpoints of the middle test are unchanged. The remaining low-residual small-content pure sector, whole cross, determinant and zero-location bridges are unresolved.
