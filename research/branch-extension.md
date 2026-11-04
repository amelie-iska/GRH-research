# Actual genus-two branch extension

Attempted claim: replace the earlier Jordan-matrix component check by an exact
nonsplit sequence of modules over the actual infinite polynomial dessin
algebra. Result: proved, with its module maps and nonsplitting kernel checked.
It is not the independent arithmetic determinant/zero-location bridge.

The complex clean dessin is y²=x⁵−1, beta=x⁵. For any coefficient field k,
the two branch cycles generate B inside Mat5(k[t])² with shared stationary
idempotents and mixed products zero. A positive length-l path from j to i
has one-branch image t^q Eij, l=j−i+5q. These monomials and shared constant
diagonal units give a normal basis. They identify B with the infinite
locally gentle path quotient, and with H×_(k⁵)H where H is upper triangular
mod t. The identification is proved in the shared article, not yet Lean.
The unital map k[t]→B sending t to the a-turn has a left inverse obtained
by taking first-factor entry00. It is injective; B is not finite dimensional.
This is proved in Lean for actual polynomial matrices of unrestricted degree.

For D=k[epsilon]/epsilon², first-factor evaluation at0/epsilon gives actual
B-module structures on M1=k⁵, M2=D⁵. For every polynomial matrix C(t),
the latter action is [[C0,0],[C1,C0]], with coordinates all constant then
all epsilon coefficients. The injection x→(0,x) and projection (x,y)→x
are B-linear. Coordinatewise kernel/image equality proves exactness.
Any B-linear section must take e0 to a vector with constant coordinate0=1.
The arrow a0 kills M1 but sends that coordinate to epsilon coordinate4
in M2, contradicting linearity of the section. No eigenvalue, algebraic
closure, characteristic restriction or desired positivity is assumed.

This refutes the source's unqualified rigidity suggestion on a genuine
infinite surface algebra: N5(J1(0)) has a nonsplit self-extension through
N5(J2(0)). The extension is an ambient finite-module extension, not a
lattice sequence. The central u acts nilpotently, allowing completed action.
The general branch-category equivalence, ambient almost-split universality,
Yoneda/derived categorical packaging and arithmetic comparison remain
separate. A Jordan-tube AR statement cannot be exported to all B-modules
without its factorization proof.

Evidence: lean-analytic/BranchExtension.lean (21 printed theorem reports),
examples/relations/check_extension.py (405 paths,7225 products,80 whole
polynomial samples and Q/F2/F3/F5 section equations), independent review at
planning/reviews/branch-extension/REVIEW.md. The independent no-production-
import oracle additionally checks400 positive paths and300 module-map cases.

Next mathematical interface: formalize the normal-form path-quotient map
and its isomorphism, then package the exact sequence in the actual module
category before attempting a universal almost-split factorization theorem.
The P7 signed low-gcd and positive determinant obligations remain open.
