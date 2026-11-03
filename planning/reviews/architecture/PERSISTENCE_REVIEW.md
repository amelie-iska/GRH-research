# Independent adversarial review: persistence and surface-order coefficient resolution

2026-11-03. Reviewed the complete current `book/chapters/persistence.tex` and `research/persistence-interfaces.md`. This report is the only file authored or changed by this task. No source chapter, cache, environment, data, checkpoint or build artifact was modified. This is an independent review of the explicit mathematical arguments, not a fresh complete audit of all cited external papers and not full Lean formalization.

**Result: no blocking mathematical defect found in the specified constructions.** In particular, the new total resolution over the actual nodal surface order is valid under its stated field/central-variable hypotheses. The following checks explain this conclusion and its boundaries.

## 1. The R/(x,y)^2 resolution

For R=k[x,y], the displayed `d1=[x²,xy,y²]`, `d2=[[-y,0],[x,-y],[0,x]]` are homogeneous for the listed bigraded shifts. Both columns compose to zero. The direct kernel proof is correct: reduce `x²f+xyg+y²h=0` modulo x, write h=xb; divide by x; reduce modulo y, write f=−ya; then cancellation of y gives g=xa−yb. Injectivity of d2 follows from its outer entries, since x,y are nonzerodivisors. The same argument works over Z[x,y], as the chapter says, without proving a length-two bound for arbitrary integral modules.

Every differential entry has positive total/bigraded degree, so this particular field-polynomial resolution is minimal. The Betti grades and Hilbert numerator `(1−s²−st−t²+s²t+st²)` are correct. The rank-invariant formula is correct **with its explicit comparable-grade precondition**: incomparable grades (1,0),(0,1) have no transition map. It is not asserted as a complete classification invariant.

The dual calculation is also correct. From −yA+xB=−yB+xC=0, coprimality forces (A,B,C)=(x²q,xyq,y²q), so Ext0 and Ext1 against R vanish. The Ext2 presentation has relations ye1=0, xe1=ye2, xe2=0 and basis e1,e2,xe1 (ungraded); suppression of internal shifts is explicitly stated. No contradiction with the persistence support arises: Ext/Tor are different invariants.

## 2. The bifiltered CW construction

One circle present at (0,0), with three degree-one filling disks appearing at (2,0),(1,1),(0,2), gives the asserted cellular differential with monomial birth factors. The cellular chain functor has genuine inclusions: every boundary cell is present by each disk's birth. Thus H1 is precisely R/(x,y)^2.

H2 is ker(d1), not the cokernel of a guessed extra differential. The already proved injective d2 identifies it with the free module on the two syzygies born at (2,1),(1,2). At grade (2,2), three common-boundary disks have two independent sphere classes. There are no three-cells, so these classes persist; no missing killing map was assumed. The CW space is not a two-manifold/dessin surface when all three disks are present, and the chapter states this essential limitation.

## 3. Schur and grading distinctions

The GL(V)-equivariant map `(v∧w)⊗z ↦ v⊗wz − w⊗vz` lands in the multiplication kernel `V⊗Sym²V→Sym³V`. Its two basis images agree with the syzygy columns. Their independence, together with dimension6−4=2, proves the identification with `det(V)⊗V=S_(2,1)V`. In characteristic zero the stated LR splitting is valid.

A general GL2 substitution preserves total degree, not the two fixed filtration coordinates. Only the diagonal torus preserves each individual bigraded weight space in this setup. The chapter explicitly retains this distinction and does not promote a termwise Schur operation to an exact functor on arbitrary complexes. The positive-characteristic scope is appropriately restricted to the displayed maps/resolution rather than semisimple representation decomposition.

## 4. Fitting, grade and base change

The Fitting conventions give Fitt0(M)=(x,y)^2 and Fitt_j=R for j≥1. The maximal minors of d2 are y²,−xy,x²; the ideal has grade2, with regular sequence x²,y². This is compatible with the finite-free Buchsbaum–Eisenbud conditions, while the direct kernel proof remains sufficient. The chapter correctly avoids replacing grade by height over an arbitrary coefficient ring or applying the commutative criterion indiscriminately to path-algebra complexes.

At x=y=0 both maps vanish and the positive Tor dimensions are3,2. At y=0, d1=(x²,0,0), d2 has columns (0,x,0),(0,0,x), so H0=k[x]/x², H1=k², H2=0. Formation of Fitting ideals commutes with arbitrary base change; exactness of this resolution does not. These distinctions are correctly made. The directed-limit generic-resolution description is not used as a finite-termination or specialization theorem.

## 5. Finite rank/incidence geometry

For feasible ranks a,b, the proposed flags have dimensions `dim L=b`, `dim K=n1−a` and `L⊂K`. The fiber really is `Hom(V1/K,V0)⊕Hom(V2,L)`. The full space is a vector bundle over a smooth irreducible flag variety. The map to the affine pair-of-matrices space is proper because the incidence conditions are closed and the flag factor is projective.

Surjectivity onto the **reduced rank-bound variety** follows by extending im B inside ker A first to a b-plane and then to an (n1−a)-plane. This uses both `rank B≤b` and `a+b≤n1`, and both are stated. On the nonempty full-rank locus the flags are uniquely im B and ker A; these vary algebraically in the standard nonzero-minor charts. Thus the projection is birational. No unsupported normality, scheme-theoretic reducedness or universal acyclicity claim is needed.

For dimensions(1,3,2), ranks(1,2), the flag is a two-plane, base dimension2 and vector-bundle fiber dimension5, total7. Full-rank complexes are exact in positive degrees, but the zero pair is not. The punctured-plane polynomial-matrix example and its nonexact origin are consistent with the earlier specialization calculation.

## 6. New actual nodal-order coefficient result

The primary algebra is genuinely infinite: `A=k[xi,eta]/(xi eta)`, `Lambda=k[[xi,eta]]/(xi eta)`, center parameter u=xi+eta. The order's rank-two k[[u]] description on1,xi with xi²=u xi proves u² is a nonzerodivisor. Thus `0→Lambda --u²→ Lambda→E→0` is a genuine free resolution for E=Lambda/u². The four-element basis1,xi,u,u xi is correct. E is finite-length, not a lattice; its arrow actions are nontrivial and J³ kills it, hence it is continuous. No infinite simple-module resolution is shortened by this construction.

For `B=Lambda⊗_k k[x,y]=Lambda[x,y]`, the displayed block matrices have dimensions D1:1×4, D2:4×5, D3:5×2, as required by ranks(1,4,5,2). The signs make cross terms cancel because u² is central. They are the mapping-cone/total complex of multiplication by u² on the scalar-extended persistence resolution.

The direct exactness proof is sound, including the low/top degrees. In degree n>0 write a cycle as `(a,b)∈P_n⊕P_(n−1)` with `da+u²b=0`, `db=0`. Reducing a modulo u² makes it a positive-degree cycle in E⊗_kP, which is exact since k is a field. Lift a preimage c, write a−dc=u²e, and cancel u² from `u²(de+b)=0` in the free term. Then b=−de and `(a,b)=D(c,e)`. For n=1, the next differential out of P0 is zero and the same argument still applies; in top degree the missing P terms are zero and u² injectivity forces the remaining component to vanish. Degree-zero cokernel is B/(u²,x²,xy,y²)=E⊗_kM.

This proof establishes exactness; it is stronger than merely observing D²=0. Over the commutative ring k[[u]][x,y], restriction doubles ranks because Lambda is finite free of rank2. Virtual B-rank0 is correct but does not imply an arithmetic determinant identity or triviality of a determinant functor. The chapter explicitly leaves these additional comparisons open. It also does not claim this total complex is a minimal resolution in an unspecified local/Jacobson sense.

## 7. Monotonicity and scope

The chapter correctly distinguishes monotone birth/threshold constructions from arbitrary dynamic snapshots. For a cumulative union, use compatible simplex-set unions or explicitly declare flag completion; these can differ by mixed-time cliques. The chapter's requirement that vertices/higher cells have compatible births is sufficient for its abstract inclusion claim. Unrelated quantum channels need not commute, so assigning them to two axes does not automatically define a persistence functor. This is separate from the useful same-channel trace-distance contractivity construction in TORICGT_ARCHITECTURES.md.

No assertion here constructs Frobenius, a completed arithmetic L-function, a positive global spectral limit or GRH. General category and analytic interfaces remain prose/open, and the source explicitly says the entire book is not Lean verified.

## Focused independent checks

Using the already approved isolated CPU environment, a fresh in-memory SymPy run checked d1d2=0, all three maximal minors with signs, D1/D2/D3 shapes, D1D2=D2D3=0, the Hilbert numerator identity, and y=0 specialization matrices. The run passed. These finite symbolic identities corroborate the direct proofs; they do not replace the exactness argument, CW realization, or algebraic-geometric proof.

No new TeX build, visual review, full Lean run, Sage execution, or complete external-source audit was performed by this independent task. The earlier author's build/layout evidence remains separate. Parent integration should keep the coefficient/persistence variables distinct and preserve the stated theorem/formalization boundary.
