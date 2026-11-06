# Coprime global root numbers with the different and all unitary types retained

New research proof, 6 November 2026. This resolves the explicitly conditional H_ROOT normalization in the earlier C v5 note for the actual Eisenstein family. The root multiplication law itself is classical; the contribution here is a self-contained derivation with this project's different, conductor section and unitary types explicit, followed by its actual all-component application. It gives a fixed-class Schur change of coordinates, not a signed-kernel estimate, a new large sieve, or an improvement of 13/12. No frozen book, public product, canonical source, index or historical experiment is changed.

Governing previous diagnostic: planning/dual-window-20261106/lane-c/ROOT_NUMBER_SCHUR_AND_FINITE_DUAL-v5.md, SHA256 ed8c415b1edac3743393e856f7131caf93b7ec03e576d944a68f92b92813c603. Its conditional status was honest and remains historical. The accepted same-class gauge is inherited input, not a new test or theorem here. Actual v8/scope/unit-k/handoff and primary pins are listed in the accompanying source-pins record.

## 1. Precise conventions, including radial types

Let K=Q(omega), omega^2+omega+1=0 with Im(omega)>0, O=Z[omega], delta=1+2omega=i sqrt(3), and d_K=|disc K|=3. The inverse different is delta^(-1)O. Lebesgue area of O in C is A=sqrt(3)/2. For an integral ideal f=(gamma), Nf=|gamma|^2. We use

    e_gamma(x)=exp(2 pi i Tr_{K/Q}(x/(delta gamma))).             (1)

This is the primitive additive pairing on O/f, even when f contains primes above 2 or 3. The inverse different is not a raw multiplicative character value at delta; it is never deleted or replaced by a unit.

Every unitary Hecke character under consideration has, on principal ideals prime to f, a unique type of the form

    chi((alpha))=theta(alpha) (alpha/|alpha|)^k N(alpha)^(i t),
    k in Z, t in R, theta a primitive finite character mod f,
    theta(u) u^k=1 for u in mu_6.                              (2)

The field has class number one. Finite characters are extended by ZERO at nonunits of their ACTUAL finite conductor. The normalization of k is defined by (2); it need not coincide with a signed infinity-index convention in another reference. We retain arbitrary fixed radial t. In particular a unitary Hecke character is not being declared finite order. Put d=|k|, chi_0=chi N^(-it), and

    Gamma_C(z)=2(2 pi)^(-z) Gamma(z),
    Lambda(s,chi)=(d_K Nf)^(s/2)
                    Gamma_C(s-it+d/2) L(s,chi).                 (3)

Thus Lambda(s,chi)=epsilon(chi)Lambda(1-s,bar chi). The same equality is meromorphic for an unramified norm twist, with its usual poles retained. The primary de Faveri v1, Section 3.2 footnotes 13--14, explicitly permits unitary opposite infinity types and supplies the corrected conjugate functional-equation convention. Its fixed normalized representatives can remove radial twists, but this proof does not require that choice. The cited [22] there is Iwaniec, Topics in classical automorphic forms (1997), not Iwaniec--Kowalski.

## 2. Primitive finite Fourier facts without a physical-modulus lift

Define

    tau_gamma(theta)=sum_{x mod gamma} theta(x)e_gamma(x).

For any beta in O,

    sum_{x mod gamma}theta(x)e_gamma(beta x)
       =bar theta(beta) tau_gamma(theta).                       (4)

For a unit beta, this follows by x -> beta^(-1)x. For a nonunit beta, the additive character factors through f/(beta,f). By primitiveness theta is nontrivial on the kernel of the unit reduction to that proper modulus; multiplying by one such unit leaves the additive factor unchanged and forces the sum to vanish. Surjectivity of unit reduction follows prime by prime and CRT. This proves the ZERO part of (4), rather than assuming a square-root sum at a larger physical modulus. Parseval for the nondegenerate additive pairing gives

    sum_beta |sum_x theta(x)e_gamma(beta x)|^2
        =Nf sum_x |theta(x)|^2=Nf phi(f),
    |tau_gamma(theta)|^2=Nf.                                   (5)

For f=O, the residue ring has one element, tau=1. In the trivial unramified character its theta zero term is treated explicitly below, rather than invoking the nonunit-frequency assertion at Nf>1.

For pairwise coprime f_j=(gamma_j), CRT with
x=gamma_2 gamma_2^(-1)x_1+gamma_1 gamma_1^(-1)x_2 modulo gamma_1 gamma_2 gives

    tau_{gamma_1 gamma_2}(theta_1 theta_2)
       =theta_1(gamma_2)theta_2(gamma_1)
          tau_{gamma_1}(theta_1)tau_{gamma_2}(theta_2).           (6)

Indeed the two additive frequencies are gamma_2^(-1) and gamma_1^(-1); (4) turns their conjugate character values into theta_1(gamma_2) and theta_2(gamma_1). Their product character is primitive at f_1 f_2: each local ramified factor occurs in exactly one input. Formula (6) also holds when one conductor is O.

## 3. The Gaussian calculation which fixes all angular phases

For z in C define P_k(z)=z^k for k>=0 and P_k(z)=bar z^(-k) for k<0. Then P_k(z)=|z|^d phase(z)^k. With Fourier transform

    hat g(w)=integral_C g(z) exp(-2 pi i Re(z bar w)) dx dy,

one has, for b>0,

    hat[P_k(z)exp(-pi b|z|^2)](w)
       =(-i)^d b^(-d-1)P_k(w)exp(-pi|w|^2/b).                 (7)

This follows from the ordinary two-dimensional Gaussian transform and d differentiations. Holomorphic or antiholomorphic harmonicity makes the lower contraction terms zero. Equivalently apply the corresponding complex derivative to the Gaussian d times; the sign is (-i)^d for BOTH k signs. Formula (7) is an exact Fourier identity, not a complex numerical sign test.

Set a=1/(A|gamma|)=2/(sqrt(3)|gamma|) and

    Theta_chi0(t)=sum_{alpha in O}theta(alpha)P_k(alpha)
                                    exp(-pi a t |alpha|^2).

The Euclidean dual of gamma O under Re(z bar w) is

    (gamma O)^*=2/(bar gamma bar delta) O.

This is exactly the trace inverse-different pairing, since Re(2x)=Tr(x). Apply Poisson to each residue class modulo gamma, then reindex the dual lattice point as

    w=2 bar beta/(bar gamma bar delta)=c bar beta.

The finite residue sum is (4), with frequency beta. Moreover

    |c|=a, phase(c)=phase(delta gamma),
    P_k(c bar beta)=a^d phase(delta gamma)^k P_{-k}(beta).

The lattice covolume is A|gamma|^2. Its factor times the Fourier scaling is
(A|gamma|^2)^(-1)a^(-1)=|gamma|^(-1). Therefore Poisson gives the exact identity

    Theta_chi0(t)=i^(-d) phase(delta gamma)^k
                    tau_gamma(theta)/sqrt(Nf)
                    *t^(-d-1)Theta_bar_chi0(1/t).              (8)

All appearances of the different and generator are visible in (8). For Nf>1 primitiveness kills the dual zero frequency; for f=O,k!=0 the harmonic polynomial kills it. Mellin integration with exponent s+d/2 yields (3), up to the SAME s-independent constant on both sides, and proves

    epsilon(chi_0)=i^(-|k|) phase(delta gamma)^k
                                    tau_gamma(theta)/sqrt(Nf). (9)

For f=O,k=0, (8) is the ordinary Gaussian theta inversion including its alpha=0 term. Subtract that term, split the Mellin integral at 1 and retain the two polar terms: the meromorphic functional equation has root 1, as also given by (9). This covers the principal sigma=1 edge. It does not remove a residue from any actual dual formula.

Changing gamma to u gamma changes tau by theta(u), and phase(delta gamma)^k by u^k. Their product is one by (2); hence (9) is independent of conductor generator. The same calculation handles a unit change of delta in a consistently changed additive convention. No choice of primary generator or a prime splitting/inert/conjugate orientation can leave an additional variable phase. A primary generator section is allowed, but unnecessary for the invariance proof.

## 4. Radial twists and conjugation

From (3), without a new analytic theorem,

    Lambda(s,chi_0 N^(it))=(d_K Nf)^(it/2)Lambda(s-it,chi_0),
    epsilon(chi)=(d_K Nf)^(it)epsilon(chi_0).                  (10)

These are unit-modulus positive-real powers. In particular omitting a fixed radial twist from an individual root would generally be wrong.

Complex conjugation of the finite sum gives

    tau_gamma(bar theta)=theta(-1)bar tau_gamma(theta),
    theta(-1)=(-1)^k.

Conjugate chi_0 has angular type -k; (9) gives epsilon(bar chi_0)=bar epsilon(chi_0), since i^(-2|k|)(-1)^k=1. Equation (10), with t -> -t, then proves the exact global relation

    epsilon(bar chi)=bar epsilon(chi).                        (11)

This is proved with the different and infinity factor, not imposed on a raw Gauss sum. If a chosen source decomposition is changed by xi_m -> xi_m N^(it_C), psi_C -> psi_C N^(-it_C), its beta_m=epsilon(xi_m)psi_C(m) changes by the fixed class scalar d_K^(it_C). Thus such source freedom does not generate a remaining Nm-dependent beta correction.

## 5. Coprime products: conversion from residue values to ideal values

First take t_1=t_2=0. Insert (6) into (9). The angular ratio in the numerator is exactly

    phase(delta gamma_1 gamma_2)^(k_1+k_2) /
       [phase(delta gamma_1)^k_1 phase(delta gamma_2)^k_2]
       =phase(gamma_2)^k_1 phase(gamma_1)^k_2.

These factors convert theta_1(gamma_2)theta_2(gamma_1) into
chi_1(f_2)chi_2(f_1). The delta phase cancels; it was not silently set to one. Thus for arbitrary normalized angular types,

    epsilon(chi_1 chi_2)
       =i^(|k_1|+|k_2|-|k_1+k_2|)
          epsilon(chi_1)epsilon(chi_2)chi_1(f_2)chi_2(f_1).     (12)

It is essential that the cross terms are IDEAL values, not just the finite residue theta values. For arbitrary radial t_1,t_2, the extra factors on the right are

    product_j(d_K Nf_j)^(it_j)
       *product_{i!=j}Nf_j^(it_i)
       =(d_K N(f_1 f_2))^(i(t_1+t_2)).

This is precisely the factor (10) on the left. Consequently (12) holds for the full unitary characters (2), with no zero-radial representative assumption. Iterating gives, for pairwise coprime ACTUAL primitive conductors,

    epsilon(product_{j=1}^r chi_j)
       =i^(sum_j|k_j|-|sum_j k_j|)
           product_j epsilon(chi_j)
           product_{i!=j}chi_i(f_j).                          (13)

This proof is global theta/Fourier plus finite CRT. It handles conductor primes in the different, arbitrary fixed infinity types, inert primes and repeated rational norms. Coprimality of IDEAL conductors is its precise hypothesis; no claim is made for a noncoprime product or for a lifted raw modulus.

## 6. Application: H_ROOT and its exact fixed correction

Retain the full original two-pivot scope and all coefficients/masks from the earlier C v5. Good squarefree original columns m,n remain DISTINCT ideal indices, (m,n)=1. No rational-norm-squarefree condition is imposed. The source decomposition and fixed class representatives are

    tilde_chi_m=xi_m psi_A, cond(xi_m)=m,
    beta_m=epsilon(xi_m)psi_A(m).

Let xi_m have angular/radial types (k_A,t_A), xi_n types (k_B,t_B). Every actual S-supported finite ray character rho is retained; it need not factor through the source R_c. Define

    sigma=primitive character inducing rho psi_A bar psi_B,
    f=cond(sigma) supported in S.

Its types are (k_B-k_A,t_B-t_A), possibly nonzero. The actual primitive

    eta=xi_m bar xi_n sigma,  cond(eta)=m n f,

has total angular/radial type (0,0). The three conductor factors are pairwise coprime. At a good prime of m or n the unique ramified local factor cannot cancel against an unramified factor; at S its conductor is precisely f, including genuine drops. Apply (13) and the PROVED (11):

    epsilon(eta)=gamma_ABrho epsilon(xi_m)bar epsilon(xi_n)
        xi_m(n f)bar xi_n(m f)sigma(mn),
    gamma_ABrho=i^(|k_A|+|k_B|+|k_B-k_A|)epsilon(sigma).         (14)

This proves H_ROOT in exactly its original actual normalization. gamma is fixed by A,B,rho/family; there is NO remaining m/n angular phase. Radial factors have cancelled by (10)--(13), not been discarded. Primary generators cause no extra correction by the generator-invariance proof after (9). If a component has no actual coprime pair its form is zero; no reference-pair calibration is needed.

Source reciprocity gives

    tilde_chi_m(n)bar tilde_chi_n(m)=alpha(A,B).

Substitute xi_m=tilde_chi_m/psi_A and xi_n=tilde_chi_n/psi_B in (14). All psi factors cancel as IDEAL values. The result is

    epsilon(eta)=kappa_ABrho beta_m bar beta_n
                      xi_m(f)bar xi_n(f)rho(m)rho(n),
    kappa_ABrho=alpha(A,B)
       i^(|k_A|+|k_B|+|k_B-k_A|)epsilon(sigma).               (15)

The requested xi_m(f), bar xi_n(f), rho(m)rho(n) factors are explicit. There is no assertion that rho is constant on R_c classes. Legitimate primitive xi_m(f) values do not restore the original raw S-deleted symbol values. All actual raw zeros, original column-pair coprime restriction, row capacity/ray/literal constraints, nu, one common W, ell/e dual weights and exact nonseparable conductor profile remain in the other matrix entries. Formula (15) does not extend the actual character root to common-prime pairs. In same-class/rho=1 it reduces to the inherited (-1)^|k_A| alpha(A,A) beta_m bar beta_n, consistent with primary Lemma 3.3; that inherited case is not counted as a new result.

## 7. What is now proved, and what remains open

The all-component finite-class Schur map from previous v5 is now an ACTUAL root-phase map on the coprime-supported matrix space, not conditional on H_ROOT. For each fixed A,B,rho put

    U_AB=diag_m[beta_m xi_m(f_ABrho)rho(m)],
    V_AB=diag_n[beta_n xi_n(f_ABrho)bar rho(n)].

They are diagonal unitaries, and each block obeys

    (M_R X)_AB=kappa_ABrho U_AB X_AB V_AB^*.

For J=max(1,number of represented source classes), the same finite-block proof and entrywise-conjugate inverse give

    J^(-1)||X||op <= ||M_R X||op <= J||X||op.                 (16)

Empty original annuli give the zero form. Off-coprime entries of the phase extension are auxiliary only; X retains literal zeros there. This is not a PSD claim for the coprime slice and not a single common global unitary when f_ABrho changes with the opposite class. Finite rho/class coefficients remain in their original signed sum; (16) does not make them positive row weights.

Thus the ROOT normalization technical gate is closed for the actual family, including unequal source classes and fixed nontrivial infinity types. What is still absent is a new bound for the Euler/profile/dual signed matrix X or for its pairing with the actual A_U/nu/W columns. The nonseparable product-conductor profile cannot be pulled into one coefficient or discarded. The finite-block map has a bounded inverse and therefore supplies no negative norm power by itself. No new exponent, fixed-W error lower bound, GRH statement or determinant estimate follows. The actual signed intermediate-window problem and the accepted 13/12 bound are unchanged.

No numerical Gauss-phase table, historical orientation run, browser, build, dependency install or publication was used. This proof requires independent analytic review before being treated as a newly accepted input.
