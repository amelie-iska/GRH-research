# Independent review of the standard-monomial chapters

Reviewed on 13 November 2026. The first two chapters of
`standard-monomials.tex` were read in full, and the specified central
arguments of the third chapter were checked. The final reviewed source
snapshot has SHA-256
`06719f9a8d5a15f5c7acc62c07fe0ce8aa33ee26df9d243d215bcc2fa3d63e7c`.

The review checked the elementary proofs in these chapters. It does not
claim an independent proof of every external general standard-basis,
representation-theoretic, or commutative-algebra theorem they cite, and
these prose proofs are not included in the current selected Lean inventory.

## Main checks

- Exterior bases, Cauchy–Binet, shuffle signs, coproduct composition, and
  the contraction homotopy work without dividing by an integer.
- The elementary one-row, one-column, and `(2,1)` Schur presentations have
  the claimed bases. The characteristic-zero idempotent construction is
  distinguished from the integral construction.
- Segre straightening decreases column inversions; distinct sorted row
  and column multisets give independent monomial images.
- Plücker straightening decreases the lexicographically sorted column
  word at every replacement. The leading monomial of a standard product
  determines both sorted rows, proving independence and the presentation.
- The basic complex quadric has the stated monomial basis, Hilbert series,
  singularity, and bihomogeneous representation. The middle factor
  `(det V)^(-p) Sym^(p+q) V` has highest weight `(q,-p)`.
- The mixed-minor rule (MC) agrees with the visually inspected formula on
  printed page 71 of De Concini–Eisenbud–Procesi, *Hodge Algebras*.
  Replacing its reversed index by an increasing one gives exactly the
  manuscript's complement inequality. The transpose convention is explicit.
- Rank strata, their degenerations, and the dimension formula follow from
  the displayed subspace normal form and flag counts. The statement
  separates admissible rank bounds from maximal component indices.
- The descending-arrow coordinate action gives `V_i tensor V_(i−1)^*`.
  Thus (W)/(SD) has the correct positive outgoing and reversed negative
  incoming blocks at every vertex, including both endpoints. Admissibility
  guarantees enough zero positions; characteristic zero is required for
  the stated splitting into representations. No algebra splitting is inferred.
- In the third chapter, the explicit ASL weights strictly decrease under
  straightening. The homogenized family has the claimed free chain basis.
  The diagonal-semigroup prefix inequalities are necessary and sufficient,
  with correct endpoint conditions; their homogeneity proves saturation.
  The valuation argument proves normality in the common fraction field.

## Precision changes agreed with the chapter author

The positive-degree restriction `d > 0` was placed explicitly in the
Schur-complex theorem: the zeroth tensor power of an acyclic complex is
still the coefficient field. The normality proof explicitly restricts an
integral element to the common fraction field. Its lattice sentence now
distinguishes the total-degree equalities, which hold throughout the
generated lattice, from the inequalities, which select semigroup points.

No remaining mathematical correction was identified within this scope.
