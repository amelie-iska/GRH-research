# Book-source integration and mathematical-status review

Independent read-only integration review, 2026-11-03. No shared source, planning, manuscript, script, environment, Git state, or generated project output was changed. This /tmp report is the only artifact written in this task. No MCP, installation, authentication, network lookup, TeX rebuild, model execution, or experimental workflow was used.

## 1. Provenance and exact coverage

The supplied files are in `/Users/amelieschreiber/Documents/LaTeX-projects/Hilbert-Polya-GRH/version-1/`.

| Artifact | Source lines | SHA256 | Relation to prior review |
|---|---:|---|---|
| `emergent_cyclic_time_hilbert_polya_GRH_2053.tex` | 15556 | `08708269403c3095381c45eb4c82435a073aaca8819f427a232e8eba368e05dc` | Exactly identical to the pinned `GRH/Surface-Orders-Hilbert-Polya/emergent_cyclic_time_hilbert_polya_GRH_COMPLETED.tex` already audited in full |
| `emergent_cyclic_time_hilbert_polya_GRH_COMPLETED.tex` | 13493 | `7c91fe980d5aed525a94b2c391a512682395edd0c8498fd4c1bd4cba95899379` | A shortened variant of the preceding source, with only52 new/changed lines and two large deleted intervals |

The misleading filename difference matters: the local supplied2053 is the same bytes as the repository's pinned COMPLETED; the supplied local COMPLETED is a different, shorter artifact. Do not use the two names interchangeably in a book manifest. The supplied `00README.XXX` names COMPLETED and reports XeLaTeX/pdfLaTeX page counts; this audit did not independently verify those PDF counts or that either existing PDF corresponds to the exact current TeX bytes.

The established collective full textual coverage of the15556-line source is recorded in `planning/COVERAGE.md`: foundations review1–9999 and15370–15556; completion review10000–15376. The durable detailed audits are `/tmp/grh-surface-foundations-audit.md` and `/tmp/grh-surface-completion-audit.md`. This means full textual reading, not independent certification of every cited theorem, experimental claim, diagram, or proof.

This new pass verified both hashes, compared the entire sources using exact line matching (`difflib.SequenceMatcher`, `autojunk=False`), read ALL52 new/changed COMPLETED lines, and freshly read these COMPLETE source intervals: COMPLETED1310–1341,2410–2447,5635–5810,11526–11625,11960–12412. It also inspected preamble/conditional-compilation and deletion-boundary contexts, all chapter headings, the current wrappers, their input graph, section inventories, `papers/core.tex`1–73, the README, and source/coverage manifests. The rest of the inherited source coverage is explicitly prior collective coverage; this is not a claim of a second independent end-to-end29,049-line rereading.

All52 changed/new COMPLETED lines are410,420,422–424,427–428,489,602,1965,2435,4271,6907,9137,9140,9145,9148–9149,9152,9286,9420,9482,9572,9636,10271–10272,10276,10355–10356,10525,10588,10606,10609–10613,10695,10767,11026,11028,11069–11075,11526,11529,11531,12112. This list includes cosmetic changes and the substantive shifts in claim language. The deleted2053 intervals are12888–14806 (the peptide/hyperbolic-QPU insertion,1919lines) and15237–15371 (its bibliography additions,135lines). The retained source itself contains an intentionally inactive `iffalse` bibliography/prose block:2053:12861–12887 or COMPLETED:12852–12878; source-line coverage includes it but it is not active book content.

Important differences are not mathematical repairs. COMPLETED:9148–9149 and10609–10613 call the spectral program conditional and identify an alleged single remaining obligation, but its unchanged11960–12408 still asserts that the obligation is solved and concludes unconditional GRH. The shorter file therefore remains logically inconsistent about its actual status. It also compresses two long algebraic formulas into malformed mathematical expressions at2435 and4271; those should not be imported as authoritative formulas.

## 2. Whole-source inventory

The following ranges refer to2053/the identical pinned repository source. They provide an inclusion/omission ledger for a future book, not endorsement of all statements.

| Source range | Material | Appropriate disposition |
|---|---|---|
|1–669|Preamble, epigraphs, roadmap and cross-layer dictionary|Rebuild a lean common preamble; replace proof-completion claims with a status ledger|
|670–1307|Introduction and corrected sphere/double-cycle dessin|Use current explicit permutation examples; distinguish the sphere and elliptic theta|
|1308–1478|DG/A-infinity foundations|Expand corrected complexes and derived functors; repair the contractible DG example|
|1479–1739|Multiparameter persistence|Retain as an independent mathematical/data interface after repairing filtrations and topology|
|1740–5104|Orders, normalizers, resolutions, Hilbert/Cartan/Euler matrices, varieties of complexes, Schur/invariant theory, toric and Artin packages|Replace false broad implications by current proved dessin constructions and correctly scoped external results|
|5105–5461|Coverings, Hom-control, AR strings/bands/tubes|Use current explicit quotient meshes; retain covering and category hypotheses|
|5462–5837|Total positivity, wiring, finite Hamiltonians, Wick rotation|Keep a corrected finite-dimensional theorem; treat QFT reconstruction separately|
|5838–6280|Finite/infinite clocks, noncommutative tori, circuits and channels|Develop a self-contained operator/control chapter with explicit domains and logarithm ambiguity|
|6281–6480|Order gluing and time holonomy|Give actual coefficient/category maps and coherence data; remove incompatible compositions|
|6481–6668|Hyperbolic uniformization, dessins and deck shifts|Useful geometry, with orbifold/compactness and quotient hypotheses stated|
|6669–6995|Entanglement metric, modular flow and Einstein-limit modeling|A separate conditional physics program, with proved metric facts and explicit unproved continuum assumptions|
|6996–8109|Graph quanvolution/quantum attention and renormalization|Algorithms and proposed physical interpretation; no automatic geometric/RG theorem|
|8110–8756|Quantum holographic associative memory|Separate computational/modeling development; empirical claims require their own evidence|
|8757–9149|Hardware constraints and experiments|Engineering proposals and validation protocols, not number-theoretic proof steps|
|9150–10618|HP candidates, torus examples, heterogeneous DVRs and arithmetic interfaces|Use as motivation and an obstruction/history chapter; replace unsupported identifications|
|10619–12887|Conditional closure, false final GRH chain, reference code and inactive text|Keep corrected closure and exact counterexamples; discard unconditional claims as theorems|
|12888–14806|Peptide quantum processor, RFdiffusion3 scaffolding, hyperbolic Kagome and error correction|Optional independently researched applications part; absent from suppliedCOMPLETED and not validated by the mathematics|
|14807–15376|Bibliography/back matter, including removed additions|Create a deduplicated, version-pinned bibliography and primary-source scope ledger|
|15377–15556|Mixed torus/AR/circular-complex appendix|Replace unsupported universal AR statements with the current actual module calculations|

This inventory explicitly preserves topics omitted from the shorter source. Deleting the peptide/QPU insertion does not establish that all remaining physics claims have been verified, and including it in a book would require substantial independent technical work.

## 3. The false final GRH chain: exact failures

References in this section are to suppliedCOMPLETED. For11960–12408 the corresponding2053 line is the COMPLETED line plus9.

1. **The modular geodesic/prime assertion is false, not merely unproved.** Proposition12062–12077 asserts at12071 that modular geodesic lengths are log p or k log p. For a hyperbolic gamma in SL2(Z), its positive expanding eigenvalue r>1 is an algebraic unit with conjugate r^(-1), and its geodesic norm is r². If r²=p^k were rational, conjugation would give p^k=p^(−k), impossible. For gamma=[[2,1],[1,1]], the norm is(7+3sqrt5)/2. This exact obstruction applies to every congruence subgroup and every integer prime power. The prime geodesic asymptotic12064–12069 does not identify its indexing objects with rational primes.

2. **The alleged Eichler–Shimura weight theorem12081–12109 has no such input objects.** Its gamma_(p,k) at12084 presupposes the false correspondence. Determinant-p Hecke correspondences are not determinant-one hyperbolic elements, and arithmetic Frobenius in cohomology is not an arbitrary complex-geodesic holonomy. The general Artin statements and higher-rank invocation at12106–12108 overstate the cited correspondences. They must not be restated as established results.

3. **The claimed fixed geometric-to-arithmetic data are not constructed.** At11994–11999 a finite set of complex dessin vertices receives Z_p “for the corresponding prime,” without an arithmetic model or a place-selection map. A complex completed local ring is not thereby a p-adic DVR. The earlier outer-automorphism-valued holonomy cannot simply be composed with an algebra representation: one needs implementing intertwiners and a coherence/cocycle proof.

4. **Conditions(a) and(b),12123–12156, are not supplied by valences or Fricke.** A dessin with local valences dividing2 and3 does not construct the required positive planar network on the chosen state space. A complex arithmetic twist can have negative or nonreal weights. A holomorphic matrix family that is pointwise real/Hermitian throughout a complex domain is too rigid to carry the proposed nonconstant parameter dependence. Fricke z↦−1/(qz) is holomorphic and orientation preserving; it is not the asserted orientation-reversing planar reflection. Doubling a complex twist produces a realification, not automatic entrywise/total positivity or the same determinant. For odd chi, chi(−1)=−1 also obstructs the stated weight-zero scalar quotient by the trivially acting−I.

5. **Condition(c)'s norm claim is explicitly false.** At12171, A=I−(sI−(I/2+iH))/C cannot have norm<1 throughout compact subsets of the strip merely by choosing C>0. At real s<1/2 each eigenvalue has real part1+(1/2−s)/C>1. The finite Fredholm determinant identity itself is an elementary valid rewriting; it does not connect A to the geometric transfer or give the log-trace convergence subsequently used.

6. **The determinant/Euler orientation disagrees.** At12210 logdet(I−T)=−sum Tr(T^k)/k. At12226 log L_N=+sum chi(p)^k p^(−ks)/k. Equal prime-cycle traces therefore give L_N^(-1), not L_N. The identity12233–12235 silently changes T into A without a determinant-preserving comparison. This cannot be repaired by a vanishing remainder.

7. **The purported convergence proof12248–12273 is invalid.** Exterior Euler convergence and a functional equation do not provide compact-uniform convergence in the strip. The approximants' claimed approximate functional equations and uniform-in-N growth are not established; the polynomial degree is growing. The displayed divisor(1+|s|²)^M is not holomorphic, so its maximum-modulus argument is not applicable. An affine exponential prefactor does not by itself approximate a nontrivial gamma factor on an open domain. The current normal-family interface in papers/core.tex55–71 supplies the correct kind of missing hypotheses.

8. **The remainder bound12275–12288 has no valid proof.** None of the claimed exact integer prime norms exists, so the mismatch is not a sparse exceptional set. Increasing closed-walk length on a fixed dessin is not a mesh-refinement theorem. A finite-area cusp surface has injectivity radius tending to0 near its cusps, contrary to the asserted global positive lower bound. Mixing does not manufacture the absent correspondence or the asserted N^(−eta) discretization estimate.

9. **The final statements consequently do not follow.** Theorem12298–12315 is not a proof of Dirichlet GRH;12317–12328 does not obtain Hecke GRH over arbitrary number fields from the preceding Q-Dirichlet assertion. The Dedekind formula12336 writes induction in the wrong direction and is not meaningful for a general non-Galois K. Correctly use a Galois closure L/Q, G=Gal(L/Q), H=Gal(L/K), and Ind_H^G1; that formal identity supplies no GRH proof. The repeated summary12353–12408 inherits the failures.

10. **Even one stated conditional holomorphy theorem needs correction.** At11575–11591 the limit F is defined only in0<Re(s)<1 but its “overlap” is U inRe(s)>1. These sets are disjoint. The identity theorem cannot connect them without a common connected domain or an actual analytic-continuation construction. The ordinary zero-location/Hurwitz criterion itself survives.

The book should retain exact counterexamples in a documented audit chapter or appendix. They explain why the new work changes the construction. They are not counterexamples to RH or GRH.

## 4. A clean conditional criterion for the book

The existing `papers/core.tex`24–45 is a correct minimal theorem: on a connected open domain U, if nonzero holomorphic f is a locally uniform limit of

    exp(a_N+b_N s) det(sI−(I/2+iH_N)),  H_N=H_N*,

then every zero of f in U lies onRe(s)=1/2. The disk/Rouche proof is explicit and sufficient. Zero-free holomorphic factors can be incorporated if their role in the actual convergence statement is specified. Total positivity, toric geometry and wiring are possible constructions of H_N, not necessary assumptions of the closure theorem.

For an Artin holomorphy variant, specify a CONNECTED common domain U containing the target strip and a nonempty matching open set V inRe(s)>1. Let the meromorphic continued target, with explicitly specified pole-clearing factor, be g. If holomorphic approximants converge locally uniformly throughout U to F and F=g on V, meromorphic identity on U proves g=F and removes any interior poles. Then the zero-location theorem applies, provided the pole-clearing factor has no zeros in the target strip. A limit defined only on the strip plus equality asserted outside its domain is not this theorem.

A genuine sufficient analytic interface is uniform trace-norm convergence on compacta of specified holomorphic trace-class A_N(s) to A(s), together with exact identifications of the APPROXIMANTS and target Fredholm determinants, on one common Hilbert space/domain. N-dependent scalar normalizations must be controlled in that identity; they are not invisible to convergence. Alternatively, the local uniform boundedness plus actual overlap in `papers/core.tex`55–71 gives a normal-family continuation route. Neither condition has been constructed for the claimed surface-order arithmetic HP sequence.

The unresolved task is simultaneous: the SAME target must have an arithmetic determinant identity, correct completion/ramification/multiplicities, independently proved positive/self-adjoint zero-location mechanism, and locally uniform limiting control. The new Abel family solves an arithmetic convergence problem but not positivity; the finite positive-pencil theorem solves zero location but not arithmetic matching. Their properties cannot be transferred by juxtaposition.

## 5. Physics interfaces to preserve, repair and expand

The finite-dimensional statement at COMPLETED5643–5666 is useful: a real symmetric positive-definite T has self-adjoint H=−a^(−1)log T; scaling T by its top eigenvalue makes H nonnegative. Total positivity is a sufficient stronger hypothesis and gives simple positive eigenvalues. Two literal corrections are necessary:5664 has the wrong shift sign (the correct normalized H is H+(log lambda_max)/a timesI), and5761 falsely calls i logT equivalent to−a^(−1)logT. For positive T, i logT is skew-adjoint. The theorem's main spectral conclusion survives after correcting those lines.

The book needs explicit interfaces rather than a single “time” identification:

* A discrete unitary tick admits nonunique logarithms; a principal Borel logarithm is bounded and aliases frequencies modulo2pi/tau. A specified strongly continuous unitary group with a Stone generator is the correct setting for a canonical unbounded time generator. No one-tick logarithm identifies high zeta zeros.
* K=−log rho of a faithful trace-one state is nonnegative. It cannot, after a finite affine shift, be a two-sided unbounded signed HP spectrum. Modular Liouville operators on doubled spaces have a different construction and spectrum; they require their own arithmetic comparison.
* Finite SPD transfer matrices do not establish an infinite-volume QFT. Reflection positivity, Euclidean covariance/regularity, domains, reconstruction, and continuum/tightness limits must be supplied for the stated QFT. Concatenation does not preserve symmetry merely because it preserves total positivity.
* A CPTP map is not automatically a continuous-time Lindblad evolution, and taking a formal logarithm is not a proof of semigroup embeddability. Detailed balance and positive spectra must be stated where used.
* The actual Fock/graph extension, its compact ideal and graph K-theory are proved operator constructions with exact scopes. The diagonal-fiber C* completion is a different model, and its polynomial embedding does not extend to the formal order. None by itself identifies arithmetic Frobenius or a completed L-function's spectral zeros.
* Entanglement-derived lengths need nonnegativity/strict positivity and a subcomplex-respecting monotone filtration. The unique torus2-cell attaches by a commutator and does NOT reduce H1 fromZ² toZ; the source persistence toy must be rebuilt. Stability of a specified invariant does not imply Einstein equations or arithmetic convergence.
* Quanvolution, attention, memory and molecular hardware require specified inputs, noise models, complexity/resource definitions and independent benchmark/experimental validation. No new biological or hardware empirical claim was checked in this task. The prior completion audit contains exact gate, CSS/counting and fidelity-model counterexamples that must be resolved before copying those chapters.

For example, the source's Heisenberg sqrt(SWAP)/iSWAP confusion and central-transition/ground-state confusion are not repaired by renaming them “proposals.” A rigorous applications chapter should distinguish an actual proven finite control identity, an engineering specification, and an empirically validated device. The peptide/Kagome material is an optional research program, not evidence for the arithmetic theorem.

## 6. Current wrapper/input graph and a coherent book organization

`papers/concise.tex` and `extended.tex` share `core.tex`; extended adds `details.tex`. They are the analytic/audit editions. `resolutions-concise.tex` and `resolutions-extended.tex` NOW share `dessin-core.tex`, not the older `resolutions-core.tex`; extended adds `dessin-details.tex`. The current dessin core includes `dessin-string-scope`, `dessin-gluing-core`, `theta-jacobi-core`, `theta-projective-core`, `theta-tame-core`. Its details includes the matching four detailed fragments. Thus importing both wrapper pairs wholesale would duplicate preambles, document environments, bibliography and core/detail material. The older resolutions bodies remain protected sources and contain useful Hodge, boundary, base-change and purity discussions that need an explicit selective inclusion ledger.

A feasible book spine, organized by dependencies rather than heartbeat history, is:

1. **Definitions, claim status and arithmetic targets.** Dirichlet/Hecke/Artin distinctions, local/global centers, source provenance, conditional closure, an honest theorem/contract/proposal legend.
2. **Cellular dessins and infinite locally gentle orders.** The explicit interval/loop/theta/square/Chebyshev examples, normalization, centers, completion versus polynomial and special-fiber categories.
3. **Projective resolutions, Koszul interfaces and determinant lines.** Correct signed Euler/Cartan identities; labeled versus intrinsic period; flat base change; perfectness; Hodge cancellation and boundary obstructions.
4. **Modules and geometric representation theory.** Actual node almost-split sequences, quotient diamond meshes, strings/bands/pure-injectives with category restrictions, curve/Fukaya/Koszul results under their exact hypotheses.
5. **Schur and cyclic invariant theory.** Young operators, LR intertwiners, monodromy invariants, semi-invariants/flags, local Cauchy positivity, and exact failures of Schur exactness/fixed-R lattice preservation.
6. **Operator completions and spectral constructions.** CK1 collapse, constrained Fock graph model, incidence K-theory, diagonal gluing, domains/spectral triples, relative boundary and actual arithmetic Abel operators.
7. **Arithmetic theta benchmark and descent.** Finite-field Jacobi sums, actual cellular H1, split/inert distinctions, projective multiplicity, derived branch functor, tame descent and full-deck kernel obstruction.
8. **Analytic approximants and positivity.** Finite Euler no-go, convergent arithmetic approximants, off-line finite-approximant certificate, Hermitian rigidity, positive pencils, Jensen metrics and unresolved positivity.
9. **Character-sum analytic route.** Actual7/8 and11/12 targets, Euler/principal/central interfaces, reflection/Gram/reciprocity components, remaining deep hypotheses, and the new short-row/high-gcd reduction when its own article is reviewed. No unconditional improved endpoint should be inferred from conditional exponent algebra.
10. **Clocks, modular states and quantum field interfaces.** Correct finite logarithms and detailed balance; infinite domains and semigroup/reconstruction hypotheses; geometry and holonomy with actual coefficient maps.
11. **Persistence, emergent geometry and computational models.** Rebuilt filtrations, rank/Betti calculations, metrics and stability; clearly separated continuum/emergent-gravity hypotheses; reproducible algorithm specifications.
12. **Hardware/application research program and open arithmetic comparison.** Optional peptide/hyperbolic-code material after independent repair and source verification; explicit milestones; no claim that hardware realizes an unknown arithmetic spectral operator.

Proofs should be integrated next to the statements instead of placing all “details” after unrelated results. Keep exact-code/Lean theorem-scope inventories, source diff manifest, selected failed-proof counterexamples and reproducibility data in appendices. Retain corrected subject-specific references rather than mechanically merging bibliography keys. The prospective book class/preamble must be designed once; article theorem counters and nested section commands need remapping during integration.

## 7. Expansion and verification obligations before calling the book complete

The current focused mathematical papers supply a strong spine but do not cover every topic in the15556-line source. Expansion is still needed for DG/A-infinity constructions with actual complexes; nontrivial persistence examples satisfying topology/filtration axioms; precise covering/Hom-control hypotheses; global arithmetic descent and Frobenius functoriality; unbounded spectral domains and genuine QFT reconstruction; physically justified metric/RG limits; quantum-channel/circuit implementations and error models; and independently sourced hardware/biomolecular claims if included. “All recent papers included” is not a substitute for these missing chapters.

Formal declarations verify their literal component types, not whole chapters. Universal prose proofs, external theorems, finite exact diagnostics and Lean declarations should have separate coverage entries. The README's current220 total predates the developing ShortRowGram file; do not count an unfinished or failing snapshot. No new Lean or code checks were run during this integration task. Current wrappers were inventoried, not rebuilt or visually certified here.

The strongest defensible book conclusion is a collection of proved constructions and obstructions, explicit conditional spectral/analytic criteria, a finite-field arithmetic benchmark, and a research program whose central global arithmetic-positive determinant comparison remains open. The supplied sources do not establish RH, Dirichlet GRH, general Artin holomorphy or general GRH.
