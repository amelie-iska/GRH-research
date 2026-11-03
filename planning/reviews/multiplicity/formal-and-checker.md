# Theta projective multiplicity and column-functor review

Independent mathematical/formal review, 2026-11-03. Full textual coverage: papers/theta-projective-core.tex lines1–27, papers/theta-projective-details.tex lines1–75, lean-analytic/ThetaProjectiveMultiplicity.lean lines1–112, and the final scripts/check_theta_projective_multiplicity.py lines1–285. The new formal-coverage paragraph in dessin-core.tex/dessin-details.tex was also inspected. Shared sources were read only. The only generated file written by this reviewer in this task is this report.

## Verdict

No unresolved mathematical error was found in the arbitrary-projective ordinary-determinant obstruction, the derived column functor, its exact multiplicities, or the stated symmetry limitations. The generalization genuinely covers arbitrary Lambda-linear endomorphisms of finite projectives, not merely external tensor matrices. The column functor is a valid **change of determinant construction** and does not contradict the ordinary-determinant obstruction. It explicitly continues to use the already computed arithmetic matrix as input.

The five new Lean components compiled independently with warnings treated as errors. They have honest limited types: conditional block determinant statements, scalar-parameter specialization, a polynomial degree obstruction and a three-power-series rank-one obstruction. They do not formalize the entire completed theta order, all projectives, the derived functor or the symmetry interfaces. The new coverage paragraph now states the scalar-versus-polynomial distinction explicitly.

## 1. The actual completed order and its special fiber

With R=Q[[u]] and the two parallel permitted three-cycles, write c_i^+ and c_i^- for the based full turns. The central relation is

    u e_i=c_i^++c_i^-.

For a nonempty path of fixed branch, a full additional turn is multiplication by u: the opposite branch term vanishes. Consequently

    e_i, a_i^+, a_i^-, p_(i,2)^+, p_(i,2)^-, c_i^+

is a genuine six-element R-basis of e_i Lambda. Its spanning proof uses the path identities and completion. Its independence is visible in the branch matrix entries: the four shorter paths occupy distinct off-diagonal entries, and a residual x e_i+y c_i^+ has diagonal pair (x+uy,x). Both zero force x=y=0. This avoids assuming freeness merely from generic rank.

Modulo u, c_i^-=-c_i^+ and all length-four paths vanish. B=Lambda/uLambda is graded, with radical layers (1,2,2,1) in every basic right projective and radical fourth power zero. The relation is homogeneous of degree3 because both theta branches have length3. There are two composition factors at every vertex, giving the all-2 Cartan matrix. This argument is specific to the stated theta order; it is not a claim about the same filtration for every closed dessin.

## 2. Every finite projective and every linear endomorphism

The Nakayama proof is valid. The completed arrow ideal J is two-sided; 1-yx has a formal geometric-series inverse for all x in J and y in Lambda, hence J lies in the Jacobson radical. The quotient Q^3 is semisimple, giving equality. Lifting a basis of the three top spaces into P e_i constructs the stated map Q=sum_i(e_i Lambda)^n_i→P. Its cokernel vanishes by Nakayama. Projectivity of P splits the surjection, so the kernel N is a finite direct summand of the finite module Q. Since the map is an isomorphism on tops, N/NJ=0 and Nakayama gives N=0. No unjustified assertion that every projective is free over Lambda occurs.

The right-module convention is also correct: Hom(e_i Lambda,e_j Lambda) is left multiplication by e_j Lambda e_i. A nonzero constant part is possible only for i=j. Thus the top matrices A_i act on the multiplicity spaces, while every other path entry raises the input path length. On B, each A_i repeats on all six path slots. Writing A=diag(A_i), there are six diagonal copies of A and arbitrary strictly degree-raising terms.

With ordinary column matrices, increasing degree gives a lower triangular matrix. The details correctly reverse the slots to 3+,2+,2-,1+,1-,0 for Lean's upper-block convention. The two same-degree slots are not mixed by the degree-zero part, because constant multiplication preserves their individual paths. This justifies the stronger six-block description rather than only four Loewy blocks with dimensions 1,2,2,1.

It follows that the specialization of det_R(1-Tf) is det_Q(1-TA)^6 for arbitrary f. Coefficientwise specialization follows directly from the finite determinant polynomial. There is no assumption that f is homogeneous, diagonalizable, equivariant or an external tensor action.

For a bounded complex, each term's local determinant has constant coefficient1 in T; its reduction is therefore nonzero. Specializing the displayed alternating rational expression is legitimate, and finite products/quotients retain the sixth-power property. Cancellations cannot change divisor multiplicities modulo6. Adding contractible projective pairs therefore does not remove this obstruction.

## 3. Generic cube and the exact target obstruction

Over K=Q((u)), Lambda_K=M3(K) times M3(K). Every e_i Lambda_K is one three-dimensional row simple in each branch. If N=sum_i n_i, an arbitrary commuting endomorphism has multiplicity matrices F_+,F_- of size N, and its ordinary underlying-K characteristic determinant is

    [det(1-TF_+) det(1-TF_-)]^3.

This remains true when the n_i are unequal. Taking the finite alternating product gives a cube in K(T). The reduced/Morita determinant in the brackets is a different construction; the manuscript explicitly distinguishes it and makes no claim that all alternative determinant theories are excluded.

A nonzero quadratic cannot be a rational-function sixth power: cross multiplication gives 2+6 deg B=6 deg A. The full local curve zeta is also excluded: q>1 and |a_q|≤2sqrt(q)<q+1 imply P(1)>0 and P(1/q)=P(1)/q>0. Its denominator roots1 and1/q are distinct, uncancelled simple poles. Neither can be a pole of a sixth power. This handles repeated numerator roots at square prime powers as well. The corrected phrase “full local curve zeta” avoids calling that rational function entire.

The target is required to be constant in the independent central parameter u. Singular rescalings or different determinant/coefficient categories would require new hypotheses and are not covered by this argument. No zero-location conjecture is used.

## 4. The column functor is an actual integral construction

Projecting to the plus hereditary order and its standard column gives a left Lambda/right-R bimodule W_+=R^3. Here “integral” means over the stated formal DVR R, not an already constructed arithmetic Tate lattice. The plus arrow acts by u^w_i E_(i,i-1), with one cut weight1 and the others0; the minus arrows act by zero. Matrix multiplication agrees with travel-order path multiplication. On a **left** module, these matrices act from the target coordinate toward the source coordinate, consistently with e_i a=a=a e_(i-1); they should not simultaneously be read as forward right-module arrow maps.

Each plus full cycle maps to u E_ii and the central sum acts by uI. Longer paths tend to zero u-adically, so the action extends to the full completed order. This differs from the earlier bounded circle/Fock representation, which could not evaluate arbitrary formal series. No forbidden pair survives.

Derived tensor with W_+ maps bounded finite projectives to bounded finite free R modules. Every acyclic bounded projective complex is contractible, and tensor preserves its contraction. Thus the construction descends to a triangulated functor Perf(Lambda)→Perf(R). No flatness assertion on all Lambda modules is needed. The explicit multiplication isomorphism e_i Lambda tensor_Lambda W_+→e_i W_+, with its balanced inverse, proves that each basic projective maps to a single R-line.

Consequently the supplied external action1 tensor M_d on e_i Lambda tensor_Q V maps to M_d once, giving P_d. The regular module maps to three lines and gives P_d^3. Pairing both branch functors gives P_d^2 on the basic-projective input. None of these claims independently recovers M_d from the order. The paper states that surviving arithmetic obligation plainly.

## 5. Cuts, rotation and branch swap

Different cuts give generically isomorphic column representations, so their characteristic determinants agree by generic conjugacy and injection R→K. This does not itself give an integral equivariant lattice isomorphism or a natural identification of determinant functors.

The branch-swap counterexample uses an actual **corner unit** f=e_i+c_i^+ acting as an automorphism of e_i Lambda. It is not being called a unit of the entire ring. The plus output line sees scalar1+u, while alpha(f)=e_i+c_i^- sees scalar1. Any natural determinant-line isomorphism compatible with alpha would have to intertwine those scalar automorphisms by an invertible scalar, impossible over R. The characteristic factors1-(1+u)T and1-T are also distinguished. The proof correctly uses an automorphism, making naturality in the determinant-line category meaningful.

For a central-fixed branch lattice of rank one at each vertex, the three nonzero arrow scalars multiply to u. Their nonnegative valuations sum to1. An invertible R-linear rotation intertwiner permutes vertex lines by units, forcing equal valuations; hence3m=1, impossible. The power-series residue proof is an equivalent, weaker-input formulation. It does not exclude noninvertible intertwiners, other ranks, changed central action, semilinear comparisons or every determinant-level transformation.

After u=v^3, a newly chosen lattice with all three arrow scalars v has the claimed strict order-three cyclic permutation. Merely base-changing the old cut column gives valuations(3,0,0), not(1,1,1), and does not repair it. The paper explicitly changes both the base and the lattice, retains the branch-swap issue, and does not claim an arithmetic descent result.

## 6. Five independently compiled formal components

Fresh command used the pinned existing Lean4.24.0/mathlib4.24.0 environment, lake env lean -DwarningAsError=true on ThetaProjectiveMultiplicity.lean. It completed with exit0. All five printed types and axiom reports were inspected; only standard Lean foundations occur, with no admissions or new axioms.

1. six_path_blocks_det: arbitrary upper-block matrix indexed by Fin6 times an arbitrary finite coefficient index, with six literally identical diagonal blocks, has determinant det(A)^6. The finite-fiber equivalence is real, not a cardinality hypothesis standing in for a missing matrix identification.
2. six_path_blocks_local_det: the same hypotheses imply det(1-tM)=det(1-tA)^6 for a scalar t in a commutative ring.
3. power_series_det_specialization: a genuine power-series constant-coefficient ring map commutes with the local determinant for each scalar parameter. Its type does not itself package a coefficientwise polynomial-in-T theorem for the completed order.
4. quadratic_not_ratio_sixth: for P,A,B in Q[T], degree(P)=2 and B nonzero imply P B^6 differs from A^6. Nonzeroness and degree behavior are proved, so cancellation is not ignored.
5. no_cyclic_rank_one_arrows: three actual formal power series with product X cannot have cyclically equivalent vanishing constant coefficients. The unit-intertwiner/category-to-residue implications remain a prose interface.

The new manuscript coverage paragraph explicitly retains the scalar-parameter limit, and leaves the completed-order path-block derivation, projective decomposition, derived tensor functor and deck interfaces as prose. The file proves conditional block components, not the entire order theorem by assuming away its central argument. Generic Morita/reduced determinant theory, the complex ratio and the actual arithmetic action are not formalized by these five declarations. The root's full208-declaration suite is separate; this reviewer independently compiled only this new module.

## 7. Final exact checker: full review and pure run

The checker is a deterministic stdlib implementation of the actual18-dimensional special fiber. Its multiplication handles the minus length-three sign, idempotents, branch switches and vanishing length-four products. Its right-projective Hom matrices prepend e_j B e_i paths; its right-action matrices append paths. The commutation tests therefore check actual right linearity rather than matching endpoints alone.

The final added column section was also read and run via checks(), without invoking its report writer. For each of the two selected branches it checks all18² basis multiplication pairs, giving648 exact representation identities. For each branch/vertex, it constructs the actual18-dimensional unbalanced tensor space e_i B tensor_Q W, then every balancing relation p b tensor w minus p tensor b w. The relation matrix has rank17 in all six cases. The multiplication functional is nonzero and annihilates all relations, so it induces an actual one-dimensional quotient isomorphism. This is substantially stronger than a dimension label supplied as input.

Fresh pure API output passed:

* 5,832 associativity triples;
* 96 elementary module homomorphisms and1,728 right-linearity identities;
* 15 all-coefficient determinant tests on dimensions6,12,18 and30, including unequal projective multiplicities and repeated copies;
* 648 column multiplicativity pairs;
* six tensor quotient presentations, each relation rank17 and quotient dimension1;
* the three possible nonnegative arrow valuation patterns summing to1, none cyclically equal.

The large and top determinant polynomials use exact rational Newton traces, not numerical interpolation. The finite tests supplement the independently proved/formal block determinant identity. The branch representation is evaluated only at u=0; its docstring correctly denies that a nonzero integer substitution evaluates the whole formal completion. The full-R corner-unit counterexample1+u versus1 and categorical claims rest on their explicit prose proofs, not these fiber samples. No source PDFs, dependencies, randomness, MCP activation or Git mutation were needed.

No remaining blocking correction was found in the final literal statements. The actual arithmetic endomorphism, descent-compatible symmetry and global determinant-preserving positive realization remain open, exactly as the final paragraph states.

## 8. Two final refinements checked

Reread the additions at details lines53 and60 after the preceding pass. Both are correct; the five-statement formal file and final285-line checker are unchanged from the verified versions.

First, left multiplication by c_i^+ on e_i Lambda has ordinary **characteristic** determinant det_R(1-Tf)=(1-uT)^3. Generically it acts as u times the identity on the plus three-dimensional row and as zero on the minus row. Equivalently, in the explicit R basis it sends e_i to c_i^+, acts by u on the two shorter plus paths and c_i^+, and kills the two shorter minus paths. Its remaining two-by-two block has eigenvalues0,u. Thus the full characteristic factor has exactly three copies of1-uT. It is not a sixth power in K(T), since its nonzero root has multiplicity3. This correctly shows that the sixth-power conclusion belongs to specialization; the generic universal conclusion is only a cube. The ordinary determinant of f itself would be zero, so the characteristic-determinant notation is the intended one here.

Second, W_+ has infinite projective dimension as a left Lambda module. Central R-finiteness over a noetherian DVR makes Lambda left noetherian, and W_+ is finitely generated. If its projective dimension were finite, the resolution could be chosen with finite projective terms. The same top/Nakayama argument on the left expresses each such term as a sum of Lambda e_i; each has R rank6. Exactness after passing to K would then express rank_R(W_+)=3 as a finite alternating sum of multiples of6, impossible. This is a real nonperfectness statement about the left kernel, not a counterexample to the constructed functor. Bounded right-projective inputs still tensor to bounded R-perfect outputs; neither left flatness nor finite left projective dimension of W_+ was required.
