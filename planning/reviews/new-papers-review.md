# Read-only review of the new paper sources

Reviewed completely:

- `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/papers/core.tex`, lines1–182, 9,096 bytes;
- `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/papers/details.tex`, lines1–189, initially10,545 bytes. After the parent applied the phase/mask wording correction below, I reread lines36–45; the current file is10,602 bytes and still189 lines.

This review did not edit either source. It checks the mathematical assertions and scope of the supplied drafts; it does not claim to have run or audited their Lean/Python companion files or externally verified every citation. Those claims must be matched to the parent's actual validation evidence.

## Conclusion

I found **no substantive mathematical error** in the core theorems or worked counterexamples as stated in these files. The drafts correctly separate conditional Hilbert–Polya closure from a construction, explicitly deny that the supplied obstructions refute GRH, and do not promote a7/8 zero-free region into a critical-line theorem. The canonical-product converse is explicitly conditional on RH and marked as classical, so it avoids importing the unknown zero locations as if they had been proved.

The one small precision correction below concerned character phases versus ramification masks and has now been applied and verified. The remaining comments are scope/citation/verification checks, not mathematical refutations.

## Core statements checked

1. **Spectral approximation criterion**, core lines24–44: valid. Connectedness plus a nonzero holomorphic target makes zeros isolated; a small disk off the critical line and Rouche's theorem transfer a positive zero count, contradicting the approximants' line zeros. The exponential never vanishes. This corrects the omitted nonzero-limit condition in the original manuscript.
2. **Normal-family continuation interface**, core55–68: valid under its explicit local uniform boundedness and common connected domain assumptions. Montel plus the identity theorem identifies every convergent subsequence, which gives convergence of the whole sequence. Entire approximants are stronger than needed, but harmless.
3. **No integral prime-power geodesic norms**, core74–95: valid for hyperbolic matrices in SL2(Z), with length equal to log(u²). If u²=n>1 is an integer then t²=n+2+1/n contradicts t being integral. Every p^k is excluded, not just prime p. This does not prohibit other arithmetic dynamical models or determinant-p Hecke correspondences; the following paragraph correctly distinguishes those.
4. **Failure of integral cyclic induction**, core97–110: valid. At the identity every induced character from a cyclic subgroup of C2×C2 has even degree, whereas the trivial character has degree1. The draft correctly distinguishes this from valid Brauer/Artin induction statements.
5. **Prime-tail obstruction**, core112–130: valid and self-contained. A convergent reciprocal-prime series would bound all finite Euler products, but each dominates the initial harmonic sum. Comparison then gives divergence for every real sigma<=1. This refutes absolute-tail arguments in the critical strip, without asserting that cancellation or regularization is impossible.
6. **Reciprocal determinant and Hermitian-part example**, core133–148: correct. The diagonal Euler transfer computes the reciprocal finite Euler product. The displayed skew-Hermitian2×2 matrix has det(I−T)=2 while its Hermitian part is0 and has determinant1.
7. **Diagonal diagnostic obstruction**, core150–165: correct for the algorithm explicitly specified there. For q=1 at s=1/2, all phase arguments are0 and every centered polynomial vanishes there; Lambda and xi do not. Positivity of the alternating eta series gives zeta(1/2)<0. A nonvanishing exponential normalization would not remove the approximants' forced zero, although the proposition only needs the displayed unnormalized model.

## Details checked

- **Trace3 worked norm**, details3–13: `(3+sqrt5)²/4=(7+3sqrt5)/2` and the length formula are correct. The integer obstruction2t²=9 is indeed impossible modulo2.
- **Odd scalar nebentypus**, details24–34: correct for scalar weight-zero functions on Gamma0(3). Since −I fixes the upper-half-plane point and contributes−1, equivariance forces every such function to vanish. A different weight or ambient group requires rebuilding the construction.
- **Negative1×1 minor**, details36–42: correct for the quadratic character modulo5 evaluated at p=2; total nonnegativity fails immediately.
- **Induction/base field**, details44–52: correct. Degree-one over an inducing subgroup's fixed number field does not make the corresponding function a product of Dirichlet functions over Q.
- **Iwahori shift orientation**, details55–64: correct for the displayed upper-Iwahori order and S=[[0,pi],[1,0]]. Direct multiplication gives `S E12 S^{-1}=pi^{-1}E21`, which is outside the order. The statement is appropriately limited to the displayed orientation; the opposite shift can repair this particular normalizer calculation.
- **No evaluation of the formal uniformizer at a nonzero scalar**, details66–72: correct. In C[[t]], t−lambda is a unit for nonzero lambda, so a unital C-algebra map cannot send it to zero in a nonzero matrix algebra. Laurent polynomial phase evaluation is a different algebraic setup, as the draft says.
- **Sphere Euler characteristic and idempotent obstruction**, details74–84: correct for a cellular connected two-vertex, three-edge graph on the sphere and a claimed k-algebra surjection from the stated three-vertex path algebra. In the target semisimple quotient k^6, arrows between distinct vertices vanish by orthogonal idempotents; at most three source idempotents cannot generate all six independent coordinates.
- **Strong convergence versus Fredholm determinants**, details87–94: correct. Rank-one basis projections tend strongly to0, have trace norm1, and det(I−P_n)=0. This does not contradict trace-norm continuity, which requires a stronger hypothesis.
- **Phragmen–Lindelof cautions**, details96–111: correct. Individual polynomial growth is not a uniform family bound;1+|s|² is not holomorphic;1+s² has zeros at±i. Cusped finite-area surfaces have global injectivity-radius infimum0.
- **Canonical-product converse**, details114–134: valid. The order-one entire xi function has no zero at0 and has the standard genus-one Hadamard product. Assuming RH makes every finite zero product a characteristic polynomial of a diagonal self-adjoint matrix after the critical shift, with its canonical exponential factors absorbed into an affine exponential. Local uniform convergence follows from the canonical product. The draft expressly avoids claiming this is a new proof.

## Suggested precision and evidence improvements

1. **Character phases versus zeros (details40–42), resolved.** The initial sentence “the twist values disappear from TT* at real s” has been corrected to distinguish disappearance of the nonzero character phases from persistence of the ramification zero mask. I verified the changed passage. Indeed diagonal entries of TT* are `|chi(p)|² p^{-2sigma}`, and chi(p)=0 at conductor primes persists.
2. **Pin the cited source statements.** Attach exact manuscript chapter/page/theorem references to the original false cyclic induction, absolute prime-tail, normalizer, dessin quotient and injectivity-radius claims. The proofs are correct independent counterexamples, but a reader should be able to verify each describes what the cited source actually asserts, and in which version.
3. **Separate manuscript-source and executable evidence.** Details166–182 correctly limits Lean/Python scope. Retain those statements only to the extent the parent's actual tool outputs establish the pinned toolchain, successful kernel checking, actual theorem axioms and exact finite examples. Reading these two sources alone does not validate those external artifacts.
4. **Preserve theorem status.** The drafts' explicit conditional language is appropriate. Do not describe the family of approximants or the normal-family hypothesis as constructed unless a separate proved arithmetic construction is supplied. Their current conclusion respects this.
5. **Publication status.** The new result of this work is an audit/reformulation and concrete counterexamples to specified proposed bridges. The drafts correctly make no novelty claim for the classical complex-analysis closure or canonical-product converse. Independent mathematical review is still appropriate before publication.

No source was changed by this review.
