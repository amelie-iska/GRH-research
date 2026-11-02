# Research results and attempted repairs

See the full proofs in `papers/core.tex` and `papers/details.tex`; exact checks are in `scripts/check_obstructions.py` and `lean/GRHResearch.lean`.

1. The geodesic norm obstruction holds for every integer norm n>1, not just prime norms. Thus extending truncation or improving numerical resolution cannot repair the source's termwise geodesic/primes identity.
2. Replacing the transfer by its Hermitian part fails to preserve det(I−T) already for a real2×2 matrix. The positive state TT* similarly loses nonzero character phases. An alternative must establish an actual relation to the arithmetic determinant.
3. The diagonal q1 phase algorithm gives identically zero eigenvalues. Its centered approximants vanish at1/2, while the target does not. Increasing dimension cannot fix this convergence failure.
4. Positive prime-tail control cannot extend Euler products below Re(s)=1. Cancellation or a regularization is necessary and remains to be proved.
5. Normal-family continuation supplies a valid interface with a connected overlap. The source's functional-equation analogy supplies no uniform bounds for the approximating family.
6. Under RH, Hadamard factorization constructs centered self-adjoint diagonal approximants directly from the zeros. This proves abstract existence can merely restate RH; it does not supply an independent arithmetic construction.

These deductions narrow the remaining research problem but do not solve it. All are elementary/classical deductions; no priority or novelty claim is made. The research objective remains a rigorous GRH proof with every analytic and arithmetic bridge discharged.
