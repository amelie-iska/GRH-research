# ToricGT quantum/hybrid interface: exact scope and corrections

2026-11-03. Subtask of the explicitly requested book expansion. Only this record and the two ToricGT chapter chunks were authored here. External clones remain immutable; no dependencies, training campaign, source upload or push was performed by this subtask.

## Source pins and read scope

- ToricGT a5199bc989a6fb170e21220e5e87bf95bc2fc0b4: README orientation, pyproject dependency and test declarations, graph token data schemas, toric_algebra.py finite rotation/cocycle code, cas_certificates.py schema/provenance, and tropical_toric_certificates.py input conversion, wall intervals, hull balancing and output scope flags.
- ToricGT-Program f91ba1811b5a4f70d53c7120acf8ca2a0049f85b: README five-paper architecture and evaluation contract.
- No AGENTS.md was found inside either clone. Repository prose was treated as source data, not new instructions.
- Primary literature: Kontsevich–Soibelman math/0011041v2 §§6–8 and Theorem4 scope; Abouzaid math/0610004v4 introduction/Theorem1.2/Cor1.4. Lekili–Polishchuk uses the project's existing pinned v5 Definition3.1.1/Lemma3.1.3/Theorem3.2.2 citation. This is a targeted source-scope review, not full rereading or independent verification of all cited papers.

## New exact derivations

1. Actual infinite elliptic-square algebra representation stratum: kill all but one framed 2×2 forward arrow and impose rank≤1. Its coordinate ring is the Segre semigroup ring with exponent columns (1,0,0),(1,1,0),(1,0,1),(1,1,1). Kernel exactly (z00z11−z10z01), proved by monomial normal form. Full one-step polynomial-ring resolution and Hilbert series (1+t)/(1−t)^3, degree-n dimension (n+1)^2. This is a framed rank stratum, not the full order or its semi-invariant ring.
2. Square support tropical function max(0,u,v,u+v) has exactly four ray facets weight1 and local balance0. Pairwise opposite-corner ties are zero-dimensional and must not be counted as facets. Tropicalization of the Segre ideal instead lives in R4 and gives w00+w11=w10+w01. Those two tropical objects are different.
3. ToricGT shift V sends e_j→e_(j−1), unlike some chapter conventions. VU=ωUV, ordered W(a,b)=U^aV^b has multiplier ω^(bc). Symmetric gauge D(a,b)=exp(πiθab)W gives exp(πiθ(bc−ad)). projective_phase exp(2πixΘy) with skewΘ has doubled commutator; the matching Θ has offdiagonal −θ/2,+θ/2. Real-lift convention avoids illegal modular halves when q even. Finite carrier, not faithful representation of the full rational rotation algebra; irrational approximants are not an automatic inclusion tower.
4. Physical Gram Kij=Trρ Di*Dj is PSD by a trace-square proof; explicitly no arithmetic Jensen/explicit-formula identification follows.
5. Toric mirror-potential computation for P1×P1: W=z+z^-1+w+w^-1 gives four nondegenerate critical points and values4,0,0,−4. Qubit Harper2Z+2X gives eigenvalues±2sqrt2. The mismatch demonstrates that a quantization/functor comparison is required, not that mirror geometry is unavailable.

## Code-level corrections retained without upstream mutation

The tropical certificate helper int-casts float coordinates/biases, so its exact arithmetic claims apply here only after integral-input validation. Pairwise-wall feasibility does not distinguish zero-dimensional ties automatically. Polygon edge balance alone does not establish a global complete-fan Chow/Minkowski certificate; the source's stronger flag names are not inherited as mathematical premises. Existing full graph transformer and language-model score claims were not reproduced.

## Hybrid design and proof boundary

Typed dessin/module records → graph attention + measured/simulated finite Weyl features → candidate maps/metrics/parameters → exact presentation/PSD/algebra and Lean checking → proved output or exact failure record. Learned outputs remain proposals until checked. Classical baselines, matched parameter/data budgets and held-out tests are required before claiming utility or quantum advantage. The chapter does not assert any new upstream benchmark, circuit execution, full-book Lean formalization, categorical equivalence for completed singular orders, Frobenius identification, or GRH proof.

A useful future task is an actual adapter exporting the pinned ToricGT finite feature/certificate records into the book's circuit and checker schemas, with exact convention tests. A subsequent spectral proposal experiment can search over arithmetic candidates only after the independent arithmetic action and determinant target are specified. Failed finite fits/positive tests do not settle a universal claim.

## Focused validation

The standalone book11pt one-inch wrapper compiles twice with the project TeX installation; 11 pages including the entire inherited bibliography (the ToricGT chapter itself occupies the first six pages). Final log contains no undefined control sequences, unresolved citations/references or overfull boxes. The tropical diagram and the final widened hybrid-architecture diagram were rendered at scale1300 and visually inspected. Temporary wrapper/log/render products live under /tmp/grh-toricgt-*; no shared build products were overwritten.

A separate finite NumPy diagnostic checked the symmetric-gauge multiplier on all pairs with entries−1,0,1 for each q=2,…,8; maximum matrix residual was1.06e−15. This corroborates the algebraic proof and is not its justification. No complete upstream campaign, quantum speedup or arithmetic comparison was tested. The parent remains responsible for the integrated book build and independent review.
