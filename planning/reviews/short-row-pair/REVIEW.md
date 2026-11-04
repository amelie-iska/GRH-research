# Independent coprime pair-square review — 2026-11-03

Reviewer: `/root/persistence_tool_review`. Reviewed the research note,
`ShortRowPairBarrier.lean`, exact checker/results and both new paper sections
against the original October sextic-family definition and the preceding
high-gcd/frontier notes. Only this report and the explicitly authorized
`outputs/checks/2026-11-03-low-gcd-pair/review/` artifacts were written.

## Result and arithmetic scope

Accepted: the finite duality and diagonal argument prove the stated sharp
bound NR(N−R). The weighted version N²Q−NS² has the correct normalization.
Ordered column pairs are counted throughout. No independence, full rank,
positive definiteness or desired cancellation is assumed; when N<R the
unweighted right side can be negative and is correctly labelled vacuous.

The original character is sextic, χ_n=(u/n)_6, as the new files now state;
its square is the cubic symbol. For H<D and prime-ideal columns with norms
in [D,2D], nonzero row divisibility would force Nu≥D. Consequently every
original zero mask is genuinely one on this specific row ball. Distinct
prime ideals give coprime pairs. CRT and the nonprincipal local sextic
characters force the primitive finite residue conductor to be exactly pq,
with norm in [D²,4D²], including conjugate split prime ideals. No claim about
an unspecified global Hecke conductor is needed.

The full all-element Eisenstein row count, including associates, is
R=(2π/√3)H+O(√H+1). The unconditional fixed-field prime-ideal theorem
(equivalently the fixed progression1 mod3 prime theorem for the split
subfamily) supplies N asymptotic to D/logD after excluding fixed S. This
classical analytic theorem remains an explicit external input. At H=D^3/4,
R=o(N), and the lower bound is of order D^11/4/(logD)². Comparison with
H²D^ε=D^(3/2+ε) rules out the proposed pair-square target for every fixed
ε<5/4. The quoted Cauchy-envelope loss D^5/8/logD is also correct.

The final text fixes W supported in [1,2], so the Cauchy expression and B1
use the same containing column annulus. The finite examples explicitly
specialize ν=1 and exclude only primes above2,3. These two scope clarifications
raised during review are resolved. A nonzero W admits a closed subannulus
where its modulus is bounded below; this also obstructs the corresponding
weighted absolute pair-square attempt.

Crucially, B1 is a nonnegative sum of kernel squares and therefore contains
the prime-pair subsum. The prime-only signed energy is not thereby a
positive summand of the full μν energy: prime/composite cross terms remain.
The new files preserve this distinction. The result refutes a new proposed
sufficient input, not an assertion made by the supplied source, the signed
short-row mean square, or GRH. It is a new route obstruction within the
inspected project notes; the underlying frame inequality is classical.

## Formal and exact checks

Independently verified the unchanged mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` and pinned manifest. The focused
Lean4.24.0 compile exited0 with warnings treated as errors. All four literal
theorem types concern actual finite complex matrices; their only printed
axioms are propext, Classical.choice and Quot.sound. The weighted theorem's
sole structural premise is the specified common squared norm per row; the
unit-modulus theorem specializes it. No project-specific axiom, admission,
arithmetic premise or spectral conclusion is hidden in these types.

Final formal source SHA-256:
`88e2f6458416b15313631f694e5e921f049adeb79f3f5fc88041a28c8ce80e7d`.
The ideal/character identification, prime counting, lattice asymptotics
and exponent application are not claimed as part of this Lean formalization.

The exact checker was independently rerun to reviewer-owned paths, including
after its final metadata clarification. All four numerical cases agree with
the recorded outputs, including the correctly negative endpoint example.
Its sextic lift uses the actual root ζ6=1+ω and tests zero before assigning
a unit value. Its integer Gram encoding, weighted identity and256 scalar
pair checks have the correct conjugation and norm conventions.

An additional independent unbounded-integer implementation used trial
primality, both directly enumerated roots of X²+X+1 modulo each split prime,
all row elements and every ordered distinct pair in the D128/H4 case.
Its462 pair sums reproduce unweighted6840 and weighted52680. The explicit
norm7 collision control is valid and explains the H<D restriction.
Final checker SHA-256:
`fd4a3a8403c7496e23677972415c2233a27462bc2617002cbe07bc58914d12ed`.
Evidence: `review/lean-focused.log`, `review/exact-final-checks.json`,
`review/exact-final.log` and `review/scalar-oracle.json` under the authorized
check directory. Historical reviewer outputs were preserved.

The next truncated Möbius convolution identity is algebraically correct:
expanding (μ−a)*(μ−a)*1 and using μ*1=δ gives μ−2a+a*a*1.
On squarefree total ideals the factors are pairwise coprime and the genuine
row-character zeros multiply correctly. Future type-I/type-II estimates
must retain that total-squarefree restriction, cross-factor coprimality,
ν,W and the actual conductors; the identity supplies no bound by itself.

No remaining blocker was found in this milestone's stated scope. The signed
arithmetic estimate and independent positive determinant bridge remain open.
