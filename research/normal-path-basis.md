# Unbounded normal-image faithfulness

Task P4-source-expansion; slice toward P6 actual algebra/category comparison.
The aim of this run was to formalize a load-bearing part of the genus-two
dessin normal-form comparison, without substituting finite matrices for the
infinite polynomial algebra. The existing BranchExtension module sequence
and the signed arithmetic frontier are preserved.

## Definitions and proof

Use vertices Fin5 and all slots (i,j,q), q natural, with i<j or q>0. A
branch slot is the actual polynomial matrix pair (t^qEij,0) or (0,t^qEij);
stationary images are (Eii,Eii). Positive length is 5q+j−i. Prove positivity
before converting Nat subtraction to length+i=5q+j. The endpoint is the
unique residue in0..4, so start and length determine both endpoint and q.

The stationary selector reads the first constant diagonal coefficient; a
positive selector reads its specified factor/entry/degree. A positive
constant diagonal is excluded by construction. This gives delta_xy for
every pair of indices, including all zero-degree and characteristic2
cases. Linear maps then recover each coefficient of an arbitrary Finsupp
linear combination. Zero expansion forces every coefficient zero, proving
actual LinearIndependent and injective normal expansion. No cutoff enters
any theorem. The slot proof witness contributes no additional algebra data.

## Scope

These are ambient polynomial matrix-pair theorems. The formal proof does
not yet construct the path quotient, establish generated-subalgebra
membership/spanning, or package the existing prose algebra isomorphism.
Products in exact tests validate conventions but are not an implicit
formal path-algebra construction. The full module category, Ext objects
and universal almost-split property remain later tasks. No formal-series
completion, lattice equivalence, spectral positivity or GRH is inferred.

## Verification

Eight new public declarations and their literal types/axioms are printed.
The new slot_ext is axiom-free; three length results use propext/Quot.sound;
the remaining four use only the standard propext/Classical.choice/Quot.sound.
Production checks475keys/225625selectorpairs/1030arrowsteps/15625products/
200finitecombination cases overQ,F2,F3,F5, including degree1000003 and
length5000019, with17invalidkeys rejected. No randomness. Independent
stdlib oracle uses seed20261103,525keys/275625pairs/200combinations/1015
reconstructions. Independent fresh final Lean compile and prose review
accepted. Exact numerical diagnostics are finite; the universal assertion
is supported by the compiled Lean proof.

## Next concrete step

Define the normal-path concatenation/mixed-zero algebra and generator
normalization, prove permitted images belong and span, then turn the
faithful expansion into an algebra equivalence with the generated object.
Avoid assuming the desired equivalence to prove membership. Continue the
separate arithmetic lane with the full moving-weight original signed
second moment recorded in the preceding Hecke-type-I handoff; pointwise
convexity alone is already known insufficient.
