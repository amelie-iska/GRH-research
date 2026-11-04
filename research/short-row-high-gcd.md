# Original-family Gram kernel and the smooth high-gcd reduction

2026-11-03. Unconditional reduction, not MS_3/4 or GRH. Independent derivations are preserved in planning/reviews/book/short-row-*.md. Work on this branch was interrupted by the expanded book request; its surviving results are recorded here rather than discarded.

Let O=Z[omega]. Columns n are squarefree primary ideals coprime to S (including 2,3), Nn in [D,2D], and χ_n is their primitive sextic residue character extended by zero on nonunits modulo n. For the unit ideal χ_1(u)=1 even at u=0. Fix row-independent coefficients |c_n|≤1, absorbing a fixed bounded annular profile and the actual μ(n)ν(n) coefficient. The original unweighted row energy has the exact identity

E = D^(-1) sum_(n,m) c_n conjugate(c_m) K_H(n,m),
K_H(n,m)=sum_(0<Nu≤H) χ_n(u) conjugate(χ_m(u)).

If n=ha,m=hb with pairwise coprime squarefree h,a,b, then
χ_n(u)conjugateχ_m(u)=1_((u,h)=1) ψ_(a,b)(u), ψ=χ_a conjugateχ_b.
The primitive oscillatory conductor is ab, but the zero-preserving periodic modulus is hab. Thus complete-residue orthogonality is not a theorem about an incomplete short row ball. Möbius inversion preserves the exact mask:
K_H(ha,hb)=sum_(d|h) μ(d) ψ(d) sum_(0<Nv≤H/Nd) ψ(v).
A moving row profile must be evaluated at dv inside this formula, not discarded.

## A genuinely controlled part

Take one fixed nonnegative radial Schwartz function Φ on C, with Φ≥1 on the unit disk, and define the smoothed row energy using Φ(u/sqrt H). The following statement is for this fixed profile; it does not establish the stronger moving-profile/supremum input in the source argument.

For a primitive nonprincipal character ψ modulo a nonunit ideal q, Q=Nq, additive Fourier inversion followed by lattice Poisson summation gives
|sum_(v∈O) ψ(v) Φ(v/sqrt X)| ≪_Φ sqrt Q  (every X>0).
Indeed the Gauss transform has modulus sqrt Q at invertible dual residues and is zero at nonunits; the zero dual frequency vanishes. The resulting bound is (X/sqrt Q) times the sum of the decaying Fourier profile over a nonzero dual lattice at scale sqrt(X/Q). For A>2, the lattice bound sum_(k≠0)(1+sqrt(X/Q)|k|)^(-A) ≪ Q/X holds uniformly: for X≤Q compare annuli with a planar integral, and for X>Q use convergence of sum |k|^(-A) and (X/Q)^(-A/2)≤Q/X. Multiplication by a generator only rotates and scales the planar Eisenstein lattice, and radiality makes every d|h profile the same Φ at X=H/Nd. Primitive Gauss norm follows from finite-field additive orthogonality at each good prime and CRT. No assumed short character-sum cancellation enters.

For n≠m with Nh in [G,2G], this bounds each masked row kernel by τ(h)sqrt(Nab) ≪_ε D^ε D/G. There are O(G) ideals h in that band and O((D/G)^2) residual pairs (a,b), hence O(D²/G) pairs in all. The D^(-1) normalization gives
|E_G^(off)| ≪_(Φ,ε) D^(2+ε)/G².
The diagonal is O_Φ(H) for H≥1: |χ_n|≤1 and the smoothed planar lattice count is O_Φ(H), while the number of columns is O(D). Summing dyadic G≥G0 costs no additional power, so the high-gcd plus diagonal contribution is O_(Φ,ε)(H + D^(2+ε)/G0²). At H=D^(3/4), choosing G0=D^(5/8) controls this part by O_(Φ,ε)(H D^ε).

The small-gcd range, particularly h=1, remains uncontrolled. This is the next load-bearing estimate. Positivity of the full Gram matrix does not prove its required upper operator bound.

## Uniformity barriers

A strengthened source hybrid bound cannot save a fixed power of NB for arbitrary β: at N=L=1 and a fixed nonunit row k0, take β(1,b)=conjugate(χ_k0(b)^3). This is a fixed coefficient sequence, not a row-dependent choice. That row's inner sum counts coprime primary b in an annulus, ≍B, giving energy ≍B². The source factor (K+NB)B has the correct B² size. This does not refute the actual special β.

Similarly an arbitrary completely multiplicative column twist can cancel μν on squarefree columns, producing coherent size D at the unit row. This refutes an arbitrary-full-column-weight strengthening of MS_3/4, not its specified arithmetic μν family, nor the source's finite prime-slot weights. Do not use the counterexample to assert that the actual open input is false.

## Formal scope

ShortRowGram.lean checks finite-field zero masks, complete orthogonality, actual finite Gram expansion, matched-row energy lower bound, Eisenstein norm identities and evaluation omega→2 mod7. It does not formalize planar Poisson summation, the uniform analytic estimates above, the full ideal CRT interface, or MS_3/4. Failed elaboration probes remain locally preserved; only a successful final log is evidence of kernel checking.

## Original-family label correction and next attempted route

The original pinned family is sextic, as specified in October paper2.tex:251–263; its square is cubic. The earlier cubic label is corrected without changing the high-gcd derivation, whose primitive nonprincipal Gauss inputs hold in both cases. The new coprime pair-square attempt is decisively obstructed by the classical frame inequality applied to actual prime columns; see [the derivation and next signed task](short-row-pair-barrier.md). This does not settle the signed low-gcd mean square.
