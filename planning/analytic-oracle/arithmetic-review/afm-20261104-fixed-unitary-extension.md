# Separate fixed-unitary Hecke AFM extension

2026-11-04. Status: independent analytic review accepted this explicit
extension; not Lean verification. Companion finite-order proof:
afm-20261104-fixed-twist-final.md. Preserve all external dependencies and
remaining cutoff/covariance/determinant obligations from that note.

The recorded original-family statements above fix finite-order nu. Here is a
separate extension for the possible fixed angular/norm twist; it does not
assert membership in BGL's finite ray-class set.

Fix one unitary Hecke character nu of K. Choose the norm-twist convention
 nu(a)=nu_0(a)*(Na)^(-i*tau),
where tau is real, and nu_0 has angular infinity parameter m in Z and no
continuous norm parameter. We specify m by the completed primitive Hecke
factor
 gamma_nu(s)=2*(2pi)^(-(s+abs(m)/2+i*tau))
                 *Gamma(s+abs(m)/2+i*tau).
With Q_rho=abs(d_K)*N(f_rho), the external functional equation used is
 Lambda(s,rho)=Q_rho^(s/2)*gamma_nu(s)*L(s,rho)
             =epsilon_rho*Lambda(1-s,conjugate(rho)),
with the conjugate-character infinity factor on the right. A constant
Q_rho^(i*tau/2), if included in another norm-twist convention, cancels
from its gamma ratio and has modulus one. These are explicit standard
primitive Hecke functional-equation inputs, not additional zero assumptions.
The pure norm row is rho(a)=(Na)^(-i*tau), so its L-function is
zeta_K(s+i*tau) and its possible pole is at 1-i*tau. This fixes all signs.

Every finite Kummer twist of nu has this same infinity parameter; its dual
has the conjugate parameter. Put T_nu=1+abs(t+tau)+abs(m). For fixed nu,
T_nu and T=1+abs(t) are comparable, with constants depending on nu. On
Re z=eta>0 the normalized gamma ratio is
 Gamma(1/2+abs(m)/2+eta+i*(t+tau+y))
 /[Gamma(1/2+abs(m)/2+i*(t+tau))*T_nu^(eta+i*y)].
For each fixed shifted line it has a polynomial-in-y times exp(C*abs(y))
majorant, with constants allowed to depend on m,tau and that line.
The same holds for the dual kernel, since its vertical argument at 1-s
is -(t+tau). Thus exactly the Mellin/AFE reduction of section3 uses common
length sqrt(X)*T_nu*(H*T_nu)^eta and the same integrable e^(-y^2) envelope.
Column twisting still has modulus one for ideals prime to S, conductors
outside S are unchanged, and S-conductor choices remain a finite set.
All squarefree and squarefull sums are unchanged. No assertion of a
uniform constant as m or tau varies is made.

Rows that are pure norm characters are separated before this pole-free
AFE. Their count is O(H), and the scalar bound
 abs(zeta_K(1/2+i*(t+tau)))^2 <<_(nu,epsilon) T^(1+epsilon)
handles their moment. Other rows are entire. This proves the same central
fixed-twist and literal-element moment for fixed unitary nu, with a
nu-dependent constant.

For the off-central transfer multiply F_rho(s) by
 h_tau(s)=(s-1+i*tau)/(s+1+i*tau)
only on pure norm rows. This cancels their actual pole; h_tau is analytic
on Re s>=1/2, has boundary modulus at most1, and at Re s=1/2+delta,
 abs(h_tau(s)^(-1)) <= (3/2+delta)/(1/2-delta).
The denominator (s+1)^(5/4) and Poisson convolution proof of section5
therefore work without any change to the height exponent, and the same
numerical transfer factor200 multiplies the now nu-dependent central
moment constant. If an alternate convention uses nu(a)=nu_0(a)*(Na)^(i*tau),
replace tau by -tau everywhere, including the pole. The separate theorem
is AFM for any fixed unitary nu; it supplies no uniformity in nu, no
positive determinant, and no GRH consequence without the remaining steps.
