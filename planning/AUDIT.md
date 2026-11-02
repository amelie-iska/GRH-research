# Audit synthesis and necessary improvements

Date: 2026-11-02. Research status: no complete proof established. Detailed evidence and exact coverage are in `reviews/` and `COVERAGE.md`. A full textual read is not equivalent to certifying all background theorems or all formal dependencies.

## Decisive findings

| Source | Claim | Finding and required improvement |
|---|---|---|
| Surface TeX 12071–12085 | Congruence geodesics have lengths k log p | False. Integer trace t would give t²=p^k+2+p^(−k), impossible. Replace this arithmetic bridge entirely. |
| Surface TeX 12197–12299 | Determinants converge to completed L | Depends on false geodesic matching, unestimated remainders, and unjustified uniform bounds. Construct an actual identity and prove convergence in a connected domain. |
| GRH PDF printed62–63, Lemma11.3 | Prime tails converge for σ>1/2 | False for σ≤1. Introduce independently proved cancellation or a different regularized operator. |
| Both manuscripts | det(I−T) supplies the Euler product | Diagonal Euler transfer gives the reciprocal product. Fix signs and distinguish transfer, reciprocal, centered and Fredholm determinants. |
| Both manuscripts | Self-adjoint extraction preserves arithmetic zeros | Unsupported and false without additional structure; the exact 2×2 witness changes determinant2→1. Prove an explicit bridge or discard the extraction. |
| Surface TeX 12420–12858 | Python spectral diagnostic | For q1 at real1/2 all phases vanish, H=0 and all centered roots collapse to1/2. The normalized evaluation computes a different Euler product and ignores eigenvalues. Replace rather than tune this diagnostic. |
| Surface TeX4831–4843; GRH PDF25 | Integral induction from cyclic subgroups | False for C2×C2 by degree parity. State Artin rational and Brauer integral induction correctly and preserve base fields. |
| Surface TeX1847–1864 | Displayed shift normalizes upper-Iwahori order | False already in dimension2. Correct orientation and recheck every downstream gluing product. |
| Surface TeX9728–9790 | Formal uniformizer evaluates to unitary phase | Impossible for allowed C[[t]] by unit t−λ. Choose a different algebra or a valid representation. |
| Surface TeX15451–15465 | Three-vertex algebra surjects onto six-vertex cycle | Semisimple quotient dimension/idempotent obstruction. Replace with a cover/unfolded category if justified. |
| Surface TeX13664–13710 | Proposed QPU circuit realizes determinant | Generic complex-s gate is nonunitary; XY terms annihilate vacuum, making overlap independent of s. Separate hardware research and provide a correct observable. |
| GRH PDF printed72–74 | Every finite group is Belyi monodromy and specified π1 map | Monodromy needs two generators; C2³ is a counterexample. The proposed punctured-cover map is ill-defined or has trivial restricted monodromy. Rebuild the topology. |

## Material worth retaining

The finite-dimensional real-spectrum argument and local-uniform-limit/Rouché closure are sound conditional principles. Fredholm determinants are continuous under trace-norm convergence; that topology must be proved, not replaced by weak convergence. Explicit source representations, surface combinatorics, and trace identities can remain useful after their individual assumptions and calculations are corrected. Do not infer that every source statement is false because some are refuted.

The `math` family003 papers make weaker zero-free claims and need their own review. No elementary refutation is currently established for the inspected arguments. The sources explicitly do not prove RH. Its comparator challenge placeholders and actual Lean solutions must not be conflated.

## Prioritized improvements

1. Remove unsupported unconditional labels from new writing; retain all original clones unchanged as evidence.
2. Build a complete dependency ledger with exact theorem statements and proof status. Track Dirichlet, Hecke, Dedekind and Artin scopes separately.
3. Replace the false geodesic/prime identification, DVR phase specialization, and cyclic integral-induction step.
4. Provide an arithmetic determinant identity that survives self-adjoint realization, with correct sign, multiplicities, gamma factors, conductors, bad primes, and character parity.
5. Prove compact-uniform convergence via trace norm or a normal-family bound. No divergent prime-tail bound, implicit functional-equation extension, or disjoint identity-theorem overlap is acceptable.
6. Redesign diagnostics to test the arithmetic bridge and convergence; positivity and critical-line roots built into a matrix are insufficient evidence.
7. Formalize actual analytic definitions and dependencies in mathlib after the prose bridge is proved. Keep current exact obstruction lemmas narrowly described.
8. Have independent specialists review corrected number theory, representation theory, and operator domains before calling the work a full proof.
9. Maintain two synchronized TeX editions, reproducible PDFs, source pins, check logs, and a candid README. Confirm authorship before submission.

## Research performed in this session

Newly written derivations establish the general no-integer-geodesic-norm obstruction, divergence of positive prime tails for σ≤1, the direct failure of q1 diagonal approximants, and determinant loss under symmetrization. The corrected closure theorem is proved by Rouché, and a normal-family continuation interface is proved with a genuine overlap. The extended paper proves a canonical-product converse under RH: abstract existence of the approximants can simply restate the original hypothesis. These are useful checks and obstructions, not a claimed solution to GRH or claims of mathematical novelty.
