# Final literal dessin/Fock/Schur review

Independent review, 2026-11-03. This report records full textual reading of papers/dessin-core.tex lines 1–251 and papers/dessin-details.tex lines 1–258, full reading of lean-analytic/DessinNodeOrder.lean lines 1–359 and lean-analytic/DessinInvariantComponents.lean lines 1–110, and a fresh compile of the latter two files. It concentrates mathematical verification on the Fock extension, incidence Smith form, degree spectral triple, Schur statements and exact-checker consistency. The AR/string/pure-injective literature claims were read but not all independently re-proved; the separate specialist reviews remain necessary. PDF layout/build checks belong to the root agent.

## Verdict

No new blocking mathematical error was found in the targeted Fock/SNF/spectral or Schur claims. The exact checker initially used the **dual** Chebyshev dessin. That was a genuine test-model mismatch, not an error in the paper's rank formula. It has now been corrected under explicit authorization, and the complete integrated checker passes with the intended ranks 36, 64, 100. Neither the thirty new Lean declarations nor these diagnostics constitute a formal proof of the infinite C* extension, global arithmetic comparison, or RH/GRH; the paper says so explicitly.

## 1. Corrected Chebyshev test contract

The paper's map at core154–161/details107–112 is beta_n=1/(1-T_n(z)^2). It has one black2n-cycle, n white2-cycles, and face lengths2 repeated n−1 times plus1,1. Its gentle quiver is the doubled n-vertex line with square-zero endpoint loops, and has one permitted cycle of length2n. Therefore the common-DVR rank is(2n)^2, not4n−2.

The earlier checker instead used beta=1-T_n^2, whose contracted graph is a path with rotation rho consisting of two fixed points and n−1transpositions. That has rank4n−2=10,14,18. The replacement keeps alpha=(01)(23)... and sets sigma=(alpha rho^-1)^-1. Its allowed successor is the old face permutation; its forbidden successor is rho^-1. The script now asserts the precise endpoint/arrow presentation:

* l=a_0 is the left endpoint loop, r=a_(2n−1) the right endpoint loop;
* forward a_i=a_(2i−1):i−1→i and reverse b_i=a_(2i):i→i−1;
* the forbidden pairs are l²,r²,a_i b_i,b_i a_i;
* there is one permitted2n-cycle and the expected forbidden cycle lengths.

Its Cartan test now uses

    det C(q)=(1+q)^2(1-q^2)^(n-1)/(1-q^(2n)).

The saved JSON has ranks36,64,100. The Fock incidence columns for these bouquet dessins are all2, so the resulting recorded groups are K0=Z^n plus Z/2 and K1=0. This is consistent with the core's general nonbipartite formula. The independently imported HLS quotient checker has the desired forward-chain arrows and square-zero endpoint loops. This corrects the source algebra to which its nine objects are inflated.

## 2. Fock extension and boundary index

Core170–200 and details161–172 retain the correct conventions. Prefix creation preserves terminal sectors. The initial projection is P_t(a)−Q_f(a), not the ordinary CK1 projection; this is the necessary reason forbidden pairs do not force the constrained Fock algebra to vanish. The vacuum relation yields all terminal-sector rank-one operators through L_p v_v L_q*. The direct sum of their compact algebras is an ideal and is exactly the vacuum ideal. Cross-terminal matrix units are correctly excluded.

In the quotient the range projections Q_a and partial isometries L_a form the allowed-arrow-state cycle graph family. Each Q_a has infinite rank and hence a nonzero quotient image. The length gauge action descends. These supply the vertex nonvanishing and equivariance required for gauge-invariant uniqueness; no unwarranted ordinary graph-Toeplitz identification is used.

The corrected lift W=L_c Q_a+(1−Q_a) is essential. L_c alone has initial projection Q_a plus the source vacuum. The tempting uncorrected lift would send that vacuum to the orthogonal sum of the vacuum and the cycle path, of squared norm2. Restricting first to Q_a makes W an isometry. Its range defect consists exactly of the first|c|positive paths beginning with a. Their terminal vertices run through the dart incidences of that sigma-cycle, with a loop counted twice. The stated sign delta=[initial defect]−[range defect] therefore gives minus the unsigned incidence column. No extra cycle-length multiplier or missing compact-sector multiplicity appears.

The checker evaluates creation and deletion rules without truncating outputs, on all input paths of length≤8. It also explicitly evaluates each cycle's full defect list, even for the Chebyshev length10cycle beyond that input bound, and checks actual L_p v L_q* actions with word/input lengths≤3. These are bounded diagnostics of the universal prose argument, not a finite truncation used as its proof.

## 3. Incidence Smith form

Core185–200/details170 correctly treat the underlying connected cellular graph, including loops and repeated edges. A signed spanning-tree elimination gives V−1unit pivots. The remaining root column evaluates on a nontree edge as0 for an even fundamental cycle and ±2for an odd one. Thus the bipartite case has rankV−1and no torsion; the nonbipartite case has rankV and one2pivot. The six-term exact sequence gives K1=ker B and an extension of coker B by Z^V. The free quotient splits abstractly, not canonically. Substituting the ranks yields precisely Z^(E+1),Z in the bipartite case and Z^E plus Z/2,0otherwise.

The script computes the determinantal divisors of actual integer incidence matrices, not merely rational ranks. The interval, loop, both theta examples and elliptic square give the expected groups; the square gives K0=Z² plus Z/2,K1=0. The common theta groups do not distinguish their genus, as the paper correctly notes.

## 4. Spectral and arithmetic scope

Core202–214/details174–177 give the actual maximal domain of the real diagonal degree operator, finite supports as core, compact resolvent, bounded polynomial commutators and summability exactly for p>1. The multiplicities E at0and2Eat every positive integer follow from the unique permitted continuation/predecessor property, including coincident endpoints. The semigroup trace of N is correctly distinguished from the heat trace of N². The character trace identity is restricted to Re(s)>1; analytic continuation is not asserted to make the same operator product trace class on a larger half-plane.

Length parity is explicitly not an even-spectral-triple grading, and the ordinary odd Fredholm class is correctly identified as trivial because the bounded transform differs from the identity by a compact operator. The scalar zeros of the zeta trace are not identified with degree eigenvalues.

The Abel attachment at core216–232/details179–224 retains the required fixed terminal sector, radial isometry, complex-linear coefficient pairing and rank-one determinant formula. The dyadic norm and tail estimates have the correct factors; the Galerkin estimate uses ||u−P_Nu||≤B0/sqrt(J), the bounded functional norm and the v-tail. Completion scales J(v), not the entire old perturbation, leaving the subtraction of e1* unscaled. The common-metric obstruction uses the correct conjugation in its inner-product identity and genuinely distinct subsequential coefficient ratios.

The E_d descent counterexample at core234–240 is supported by the exhaustive F7counts4and7and local factors1−4T+7T²and1−T+7T². The complex Belyi-pair equivalence does not erase a chosen rational model. The paper explicitly restricts its obstruction to undecorated complex/combinatorial data, distinguishes elliptic weight one from Dirichlet weight zero, and does not call this a GRH counterexample.

The final Hurwitz criterion at core246 is a valid **conditional** criterion for primitive nonprincipal completed Dirichlet functions. Self-adjoint finite matrices and entire nowhere-zero scalar factors have no zeros off the real axis; locally uniform convergence to a nonzero entire target preserves this zero-free property on each off-axis disk. Constructing those arithmetic approximants remains explicitly open.

## 5. Schur and invariant consistency

Core104–135/details37–89 agree with the prior Schur review. Positive-degree Schur functors preserve zero path relations; the empty partition is kept only as a scalar feature. The LR tensor operation is specified vertexwise and is not confused with tensor over A. The coordinate dual is V_source tensor V_target*, with the contragredient character convention stated. The invariant ring of the actual retained three-cycle stratum, its total degree3jHilbert series, singular-arrow scope and Schur basis are correct.

The nonnormal matrix norm bound uses the inherited norm on the Schur subspace inside the tensor power. This is valid even though a chosen Young projector need not be orthogonal. The Cauchy kernel requires nonnegative r and rR0²<1; it is explicitly local rather than a global arithmetic positivity theorem. The empty partition, continuous nilpotent monodromy collapse, fixed central-R lattice failure and split-sequence exactness counterexample all remain visible.

## 6. Thirty independently compiled Lean statements

Fresh commands used the pinned existing Lean4.24.0/mathlib4.24.0 environment and lake env lean -DwarningAsError=true, separately for DessinNodeOrder.lean and DessinInvariantComponents.lean. Both completed with exit0. I inspected all twenty plus ten printed theorem types and their printed dependency lists. There are no sorry/admit declarations or new axioms in either source; dependencies are standard Lean foundations, with some elementary CK components using fewer or none.

The node is genuinely the subring of two power-series rings with equal constants. Its x,y are nonzero branch elements, u is diagonal X and regular. The factorization and annihilator results are actual existential equalities inside this order. The boundaries are genuine linear maps; augmentation surjectivity/exactness, three alternating kernel=range statements, square-zero compositions and projectivity give the stated completed-node resolution components. The coordinate theorem is a bijection of power-series pairs, not yet a packaged R-linear equivalence; the manuscript correctly states this limitation. Since the ring is commutative, the left-module encoding suffices for the intended right-module node statement.

The invariant file proves three CK collapse components with explicit permutation/coverage hypotheses, a cleared determinant change-of-bases identity with a supplied inverse, actual symmetric-square zero/identity/composition/relation identities, its degree-two character formula, and the nodal fixed-parameter obstruction under u≠0. It does not formalize general Schur/LR theory, the C*extension/SNF, spectral traces, arithmetic descent or GRH. Its displayed symmetric-square matrix agrees with the Python monomial convention; there is no discrepancy from a missing factor2in the formal composition proof.

## 7. Fresh exact evidence and remaining coverage limits

After the Chebyshev correction, python3 -B scripts/check_dessin_extension.py completed with exit 0 and regenerated only the two authorized diagnostic outputs. Saved JSON was reloaded and validated. Totals are 8 dessins, 24 rational Cartan samples, 2516 initial-projection identities, 2516 forbidden products, 493 cycle-lift/defect input cases, 25382 terminal matrix-unit basis actions, 1628 signed EC/CE scalar coefficients through degree 10, 81 Cauchy coefficients through degree 8 and 5 actual LR matrix intertwiners. The Schur portion also enumerates 12 semistandard two-row shapes through size 5 and checks the actual theta zero relations and Sym² images.

The imported pure HLS checker reports 9 modules, 54 dessin relations, 12 signed maps, 72 arrow commutations, 4 exact meshes/12 vertex exactness checks, 1 negative-sign control, 5 node jet levels, 10 exact rows, 4 literal three-by-three jet diagrams, 12 exact columns and 32 commuting squares. Importing its checks() did not invoke its report writer. These checks verify matrices/exactness, not the abstract almost-split property or all pure-injective classifications.

No fresh PDF rendering/build or full 177-statement suite was run by this reviewer. The independent formal rerun here consists precisely of the new 20+10 statements. No shared manuscript, Lean, planning or README was edited. Authorized modifications were limited to the dessin checker and its exact-checks.json/exact-check.log; this separate report is in /tmp. No MCP, package installation, source-clone edit or Git mutation was used.
