# Persistence, Schur syzygies and genuine surface-order coefficients

2026-11-03. Implemented only `book/chapters/persistence.tex`, its bibliography fragment `book/chapters/persistence-references.tex`, and this research record. Original source clones, cached papers, environments, toolchains, data and Git history remain unchanged. This is a new worked construction and scoped source review, not an assertion that the entire book or the imported literature is Lean verified.

## Primary sources and honest review coverage

- 1810.06750v5: `research/literature/projective/surface-I-v5-independent-audit-20261103/arxiv-1810.06750v5.pdf`, SHA256 `6fa9663600cc670e36b2504642989fe8a83420f9cc11cb2a3aadee3d72e7d43a`.
- 1812.00621v1: `research/literature/projective/surface-II-1812.00621v1-20261103-9af2d671.pdf`, SHA256 `5f2e498421e3121b6b18ba68d6309a1f6a6e3545b1bc451856b34d5a2555e7aa`.
- 2210.11433v1: `research/literature/projective/arxiv-2210.11433v1-review-20261103-01/paper.pdf`, SHA256 `931fbfaf973d1e827621b8c989289c4800e9334c3f2c7c564721d7668dbc01d3`.

The public arXiv records were checked for these exact requested versions. The Surface II cache has an internal date of 27 November 2024 despite its v1 identifier and 2018 record; the chapter's bibliography retains that discrepancy rather than inventing another numbered revision.

Fresh targeted reading: Surface I v5 definitions of the locally gentle surface algebra, completed/pullback order and its source §10 projective-resolution theorem/proof (source lines621–676,776–822,1361–1474); Surface II local algebra/order definitions and hereditary columns in §§5–6, plus the proposed global gluing in §9; 2210.11433v1 §§3–7 and §10 were consulted in the cached original TeX for the graded persistence dictionary, finite presentations, Fitting invariants, generic exactification, varieties of complexes and time-varying Ising proposals. The exact Fitting/generic construction text and the complex-space rank discussion were read directly. The new chapter does not rely on §8's disputed straightening claims or the global representation-correspondence assertions. Existing full reviews `planning/reviews/projective/{surface-I,surface-II,persistence-resolutions}.md` supply prior coverage and counterexamples; this run is not another full end-to-end reading of all three articles.

Independently reread the primary Buchsbaum–Eisenbud criterion and Corollaries1–2 on printed pp260–261 in the cached1973 paper. Rendered/read Bruns' actual Theorem1 and directed-limit proof on printed pp35–36 using the existing source images. The source supports a direct-limit construction killing positive homology, not automatic finite termination or exactness after every specialization. No protected cache was changed and no new server, dependency, GPU or paid computation was used.

## Exact worked result

For R=k[x,y], M=R/(x²,xy,y²), the minimal bigraded free resolution is

0 -> R(-2,-1) + R(-1,-2) --d2-> R(-2,0)+R(-1,-1)+R(0,-2) --d1-> R -> M -> 0,

d1=[x²,xy,y²], d2=[[-y,0],[x,-y],[0,x]].

The chapter proves kernel=image directly by reducing first modulo x and then y; injectivity of d2 follows from the first and last coordinates. It computes the three-point rank diagram, all multigraded Betti numbers, H_M(s,t)=1+s+t and its resolution numerator, Fitt0(M)=(x,y)² and the dual Ext calculation. The three maximal minors of d2 are y²,-xy,x². Over the field polynomial ring their grade is2, agreeing with the classical finite-free acyclicity criterion.

A concrete CW bifiltration starts with one loop at (0,0) and three degree-one filling disks born at (2,0),(1,1),(0,2). Its H1 is exactly M. Its H2 is free with the two displayed syzygies born at (2,1),(1,2). The auxiliary three-disk CW complex is explicitly not claimed to be a Riemann surface. This realizes the persistence module without replacing any primary infinite dessin algebra by a finite-dimensional example.

For char k=0, generators transform as Sym²V and the first linear syzygies as S_(2,1)V = det(V) tensor V. The chapter constructs the natural delta map, proves its kernel-image description by a basis/dimension calculation, and records the Littlewood–Richardson decomposition. GL2 preserves the total grading, while the diagonal torus preserves the separate filtration weights. Positive-characteristic semisimplicity and termwise Schur exactness are not assumed.

The three-term complex variety has a corrected incidence resolution over Flag(b,n1-a;V1), not a false universal exactness assertion. The full-rank locus is exact in positive degrees for format(1,3,2), but the zero matrices remain a nonexact boundary. Base change at the origin gives Tor dimensions1,3,2; setting only y=0 gives H0=k[x]/x², H1=k², H2=0. Fitting base change therefore remains distinct from resolution exactness.

## Genuine infinite surface-order application

The primary algebra remains the actual nodal interval dessin A=k[xi,eta]/(xi eta) and its completed order Lambda=k[[xi,eta]]/(xi eta), u=xi+eta. Set E=Lambda/u². It has nontrivial arrow actions and k-basis1,xi,u,u xi; multiplication by u² is a regular map Lambda→Lambda, so E has the stated length-one free resolution. E is finite length, not a coefficient lattice.

For B=Lambda tensor_k k[x,y], the tensor total complex resolves E tensor_k M with free ranks(1,4,5,2). The actual block matrices are

D1=[d1,u²], D2=[[d2,u²I3],[0,-d1]], D3=[[u²I2],[-d2]].

Their consecutive products vanish. The chapter gives a direct lifting proof of exactness: reduce a cycle modulo u², use exactness of E tensor_k P in positive degrees, lift a boundary, and cancel u² in the remaining free term. This is compatible with the fixed central action. It neither shortens the infinite residue-simple resolution nor constructs Frobenius or a GRH determinant comparison. Restriction to k[[u]][x,y] doubles the free ranks.

## Focused checks and layout

- Exact symbolic in-memory checks using the already approved isolated CPU environment passed d1*d2=0, all three maximal minors, the Hilbert numerator, the total ranks and both total differential products. No numerical test is used as the proof of kernel=image.
- Standalone one-inch book11pt wrapper compiles to8pages including bibliography, with no errors, unresolved references/citations or overfull boxes. The parent integrates the fragments into the main book separately.
- Rendered all8pages at maximum dimension1600px to `/tmp/grh-persistence-visual`, inspected two contact sheets and the full-size rank-diagram page. A legend initially intruded into the rightmost zero-column; it was moved to an explicitly west-anchored position outside the lattice and the latest page was re-rendered. No other clipping, broken formula or overlap was found.
- No full Lean run, Sage execution or all-source external theorem verification was performed by this subtask. The general UFD exactness proof, CW realization, Schur/category interfaces and full surface-coefficient total complex remain prose unless separately formalized by the parent. The chapter does not claim GRH completion.

## Integration handoff

Insert the persistence chapter after the computational/learned chapters or alongside the representation-theory development; append its five Pers-prefixed bibitems to the shared bibliography generator. The rank diagram is one new TikZ picture. Existing diagram-generation automation should discover it when regenerated. The total matrices and graded births supply exact deterministic Sage/Lean targets; preserve the distinction between a complex equation and exactness, and between snapshot graph data and a genuine monotone bifiltration. Future learned proposals can target these finite identities, not certify an arithmetic theorem through a small loss.
