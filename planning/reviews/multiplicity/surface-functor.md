# Theta special fiber, projective determinants and a qualified multiplicity-one repair

Independent read-only audit, 2026-11-03. Coefficients are R=Q[[u]], K=Q((u)). Lambda is the actual completed elliptic-theta order of rank18, with generic algebra M3(K) times M3(K). No shared files were modified.

## 1. Compute the special fiber before computing determinants

Index vertices by i modulo3. Write x_i and y_i for the two branch arrows i->i-1. Products stay on a single branch; every mixed adjacent branch product is zero. Let X_i=x_i x_(i-1) x_(i-2), and define Y_i similarly. The common central parameter is

u=sum_i(X_i+Y_i).

It is important that this is the sum of the two branch full turns at a paired vertex, not a relation independently setting each branch turn to u e_i inside Lambda. In the hereditary normalization its coordinates are (u I3,u I3).

In B=Lambda/uLambda one has X_i+Y_i=0. Multiplying u e_i by an outgoing arrow shows every length-four surviving branch path is zero; the other branch term vanishes by a mixed zero relation. Thus e_i B has the six-element basis

e_i; x_i,y_i; x_i x_(i-1), y_i y_(i-1); X_i,

with Y_i=-X_i. Independence follows from the formal branch normal forms: only the displayed full-turn sum is identified at degree3, and no lower-degree path is identified. Globally B has dimension18 and radical layers dimensions

(dim B/J_B, dim J_B/J_B^2, dim J_B^2/J_B^3, dim J_B^3)=(3,6,6,3).

Here J_B^4=0 and J_B^3 is nonzero. Each basic projective has layer dimensions(1,2,2,1). The endpoint counts give its three composition multiplicities as(2,2,2): one top plus one socle at i, two arrows at i-1, and two length-two paths at i-2. Therefore the special-fiber Cartan matrix is the 3-by-3 matrix all of whose entries are2. These statements are compatible: total dimension of each e_iB is6.

Upstairs the arrow ideal J is the Jacobson radical. Indeed uLambda is contained in J, J^4 is contained in uLambda, and u-adic completeness makes geometric inverses of1-z converge for z in J. The quotient Lambda/J=Q^3 is semisimple. The usual lifted-top/Nakayama argument then shows every finitely generated projective right module is a finite direct sum of the e_iLambda: lift bases of its three top spaces, map the corresponding sum of basic projectives onto it, split by projectivity, and apply Nakayama to the complementary kernel whose top is zero. This proves the quantifier 'any finite projective', rather than only the displayed free modules.

## 2. Sixth-power specialization for every Lambda-linear projective endomorphism

Let P=direct_sum_i (e_iLambda)^(m_i), and let f be any Lambda-linear endomorphism. Let f_i be its induced Q-linear m_i-by-m_i matrix on the i-th top space. Put H_f(T)=product_i det(I-T f_i).

The reduction Pbar=P/uP is a projective B-module and fbar preserves its radical filtration Pbar J_B^r. Off-diagonal vertex maps and positive-radical entries raise that filtration. The degree-zero associated-graded action is therefore f_i tensored with the identity on each length-r path space starting at i. These path dimensions are1,2,2,1. Determinants on a filtered finite-dimensional vector space multiply over associated-graded pieces, so

det_R(I-Tf) modulo u
 = product_i det_Q(I-T f_i)^(1+2+2+1)
 = H_f(T)^6.

No scalar-tensor assumption, diagonalizability, uniform eigenvalue assumption or grading-preserving assumption on f is used. Lambda-linearity and projectivity are essential. The differential of a bounded projective complex does not change this termwise statement.

For a bounded perfect complex P^bullet with a Lambda-linear chain endomorphism f, take the rational alternating characteristic determinant D(T)=product_n det_R(I-T f_n)^((-1)^n), or its reciprocal if using the zeta convention. Specialization is always defined in Q(T): each denominator polynomial has constant term1 in T, so is not the zero polynomial after reduction. Consequently

D(T) modulo u = [product_n H_(f_n)(T)^((-1)^n)]^6.

Every zero and pole of this rational function over an algebraic closure has order divisible by6. An elliptic local polynomial1-aT+qT^2 is not a sixth power: its pole at infinity has order2. The full good curve zeta P(T)/[(1-T)(1-qT)] and its reciprocal are not sixth powers either: q>1 and P(1)=#E(F_q)>0, P(1/q)=P(1)/q>0 give simple poles or zeros at1 and1/q. Thus no such ordinary underlying-R perfect determinant can equal these u-independent targets. Equality over R or K with a u-independent rational target would specialize and contradict the theorem.

This is a genuine strengthening of the prior uniform-tensor multiplicity calculation. It does not concern every possible categorical determinant functor or semilinear operator.

## 3. Generic Morita theory gives a cube, not yet multiplicity one

Let m=sum_i m_i. On the generic fiber P_K is m copies of the simple row module for each of the two M3(K) branches. A Lambda_K-linear f has multiplicity matrices f_+,f_- of size m. Hence

det_K(I-T f on P_K)
 = [det_K(I-T f_+) det_K(I-T f_-)]^3.

This also proves a generic cube obstruction for the **ordinary K-vector-space determinant**. The product inside brackets is the product reduced characteristic norm, not an unexplained root. In this split setting the branch matrices can be taken over R using the hereditary matrix coordinates and their chosen cuts. At u=0 each is block triangular, with diagonal blocks the same top matrices f_i. Thus

N_+(0,T)=N_-(0,T)=H_f(T),
N_+(0,T)N_-(0,T)=H_f(T)^2.

So the product reduced norm is a genuine lower-multiplicity invariant, but its integral specialization remains a square. In particular it cannot equal a nonsquare elliptic local polynomial, and cannot equal the full curve zeta with simple poles. A single selected branch has H_f, without that square. The changes in multiplicity are precisely3 from the matrix row dimension and2 from retaining both glued branches.

One must distinguish a well-defined reduced norm or a specified Morita determinant functor from arbitrarily taking a sixth root of a scalar formula. The former can be constructed; the latter alone supplies neither an integral line nor functorial exact-triangle compatibility.

## 4. A genuine integral branch determinant functor repairs multiplicity one

There is a positive construction, beyond just taking a root. Choose one hereditary branch and its cycle cut. The actual algebra maps

Lambda -> B_+ subset M3(R)

give W_+=R^3 the structure of a left Lambda/right R bimodule. Every e_i W_+ is free of rank one over R. On bounded complexes of finitely generated projective right Lambda-modules define

F_+(P^bullet)=P^bullet tensor_Lambda W_+.

This is a genuine triangulated functor Perf(Lambda)->Perf(R): each projective term is a summand of a finite free Lambda-module, so its tensor is a summand of a finite free R-module. Working on projective complexes computes derived tensor and respects homotopies. No flatness assertion for W_+ as a Lambda-module or exactness on the entire module category is needed.

Composing with the standard determinant functor over R gives an actual new determinant-line construction. For the externally supplied arithmetic operator F_V on a two-dimensional V, choose P=e_iLambda tensor_Q V and f=id tensor F_V. Then F_+(P)=R tensor_Q V and its characteristic determinant is exactly P_d(T), with multiplicity one. This is a mathematically valid repair for a chosen-branch determinant. The Jacobi arithmetic matrix remains external input; this functor by itself does not reconstruct it.

This does not contradict Section2: its determinant is that of P tensor W_+, not the original underlying R-module P. Likewise selecting one branch changes the symmetry and coefficient data of the problem. It should be described as a new functor with explicit choices, not a normalization of the old determinant silently assumed equivalent.

## 5. Exact loss of integral deck symmetry for the branch column

The C3 deck rotation sigma cycles the three vertices and the three plus arrows, while alpha swaps the two branches. Consider any R-free column lattice supported generically on the plus branch, with each vertex space free of rank one and u acting by its fixed scalar. In vertex bases its three nonzero arrow maps are scalars a_i in R. The full-cycle relation on this branch gives product_i a_i=u, so their valuations m_i are nonnegative integers with sum1.

An R-linear sigma-linearization is an isomorphism between the column and its sigma twist. Its maps between the rank-one vertex spaces are units. The arrow intertwining equations then force all three valuations m_i equal. This would give3m=1, impossible. Thus there is no such unramified integral sigma-equivariant one-column lattice, regardless of where the cut was chosen. The proof is about this actual lattice representation, not all imaginable equivariant categorical constructions.

The fixed-base hypothesis matters. After ramification R'=Q[[v]], u=v^3, set all three plus-arrow maps to v times the corresponding matrix units and all minus arrows to zero. Their cyclic product is u. The cyclic permutation of the three basis vectors now gives an honest R'-linear order-three sigma-linearization. This is a valid different coefficient category. The other branch is still exchanged by alpha. Taking both ramified columns gives a full branch-swap model with rank two at each vertex over R', and a uniform arithmetic tensor then has determinant P_d^2 over R'. Restricting scalars back to R multiplies those ranks by3, restoring exponent6 for the paired construction. Ramification has not preserved the original determinant while removing its multiplicity.

Even determinant-level full C6 equivariance fails for the particular unramified chosen-branch functor. Alpha fixes the quiver vertex e_i but swaps the branches. The corner unit f on e_iLambda having normalized branch values((1+u)E_ii,E_ii) is an actual automorphism, with inverse((1+u)^(-1)E_ii,E_ii). Its F_+ determinant is1+u; the F_+ determinant of its alpha twist is1. A natural isomorphism of the two R-line functors would have to intertwine these unequal scalar automorphisms, impossible for an invertible line map. Thus F_+ does not admit the demanded alpha-equivariant determinant-functor structure on all Perf(Lambda).

Caution: failure of a sigma-linearization of W_+ does **not** by itself prove that every determinant-level sigma-equivariance fails. The branch reduced characteristic polynomial is invariant under generic inner conjugation by sigma, even though the integral column lattices are not isomorphic. Coherent natural line isomorphisms are a weaker and different question. No universal theorem excluding alternative determinant functors, complexes, twisted target Picard categories or other natural-isomorphism constructions is asserted here.

## 6. Semilinear maps and remaining scope

An operator satisfying f(a m)=theta_g(a)f(m), with g nontrivial, is not Lambda-linear and is not covered by Section2. If it fixes R it can still have an ordinary R-characteristic determinant, but radical layers now carry permutation/intertwiner actions rather than repeated top matrices. Their determinants need their own proof. A base-semilinear map moving u is not even an R-endomorphism; one must specify the invariant base, an iterate, or a skew determinant before applying these formulas.

Generic branch selection, ramified lattices, reduced norms and semilinear maps are therefore real possible changes to the framework, with changed hypotheses. None automatically proves an arithmetic comparison or yields a canonical root line. Full C6 compatibility is stronger than preserving the conductor, and the one-column valuation proof makes that difference explicit. A successful next construction must state its coefficient ring, source/target perfect categories, chosen branch or symmetry, its endomorphism linearity, and the determinant functor actually used.

No GRH consequence is claimed. The result established here is: the ordinary underlying-R determinant of every Lambda-linear bounded perfect complex has sixth-power special fiber; a valid chosen-branch determinant functor can remove multiplicity, but it does not retain the full specified unramified deck symmetry.


## Final artifact review and independent diagnostics

Read every line of `papers/theta-projective-core.tex` and `papers/theta-projective-details.tex` after their creation. No literal mathematical correction was required. The statements retain the original completed infinite theta order, explicitly identify all determinants in the obstruction as ordinary underlying-R determinants, and correctly change the determinant functor for the positive repair. The proof of arbitrary projective decomposition uses the actual radical, top lifting, split kernel and Nakayama. The endomorphism proof uses its full path filtration, rather than the Cartan matrix alone. Denominators have nonzero reduction and the divisor argument covers repeated numerator roots as well as the simple poles of the full curve zeta.

The explicit branch bimodule matrices u^(w_i)E_(i,i-1), with one cut weight1 and the others0, respect the stipulated travel multiplication. As a **left** module the matrix sends the column at i-1 to the column at i; this is consistent with the path convention and tensoring right projectives, not an accidental orientation reversal in the bimodule. The module extends to the formal order because arbitrarily long nonzero branch paths acquire arbitrarily high u-powers. Its tensor functor is defined on perfect complexes and does not incorrectly assume un-derived flatness.

The actual corner unit e_i+c_i^+ is invertible in e_iLambda e_i by its geometric series; hence it is a valid automorphism on which the determinant functor acts. It witnesses failure of alpha-invariance even at the line-functor level. The paper correctly does not infer a universal determinant-level rotation obstruction from failure of a column-lattice linearization. The scalar valuation and coefficient proofs are valid, and the distinction between merely base-changing the old lattice and choosing the new ramified lattice is explicit. The closing arithmetic construction, bad-prime/Tate comparison and positive global limit are expressly unresolved.

An independent exact18-dimensional model of B verified the normal-form multiplication, all5832 associativity triples, radical layer dimensions(3,6,6,3), the all2 Cartan matrix and the top-scalar diagonal of multiplication by an arbitrary element with nontrivial positive-length coefficients. This finite diagnostic corroborates the supplied universal normal-form proof; it is not used in place of it. There were no random seeds or installations and no shared output writes.

The graded special-fiber Cartan matrix provides an additional independent check:

C_B(t)=[[1+t^3,2t^2,2t],[2t,1+t^3,2t^2],[2t^2,2t,1+t^3]],
det C_B(t)=(1-t^3)(1-t^6).

Indeed C_B(t)=(1-t^3) C_A(t), because central u has path degree3 and acts injectively. Taking determinants agrees with the elliptic-theta infinite Cartan factor (1-t^6)/(1-t^3)^2. Setting t=1 gives precisely the rank-one all2 matrix, without implying finite global dimension or loss of the actual infinite order.

This review did not independently rerun the newly reported five Lean files or parent checker. Its verification consists of full assigned prose reads, the independent universal proofs above and the exact special-fiber diagnostic. Earlier theta Jacobi/positive-chain checks are in the separate theta descent and inert reports. No global arithmetic or GRH claim is inferred.

Final source snapshots:
- `papers/theta-projective-core.tex`: 4893 bytes, 27 lines, SHA-256 `95b3a886583a8a8e94e7ffccd4bd1a061ba7ae37d71afbd79289a23316aa7c73`.
- `papers/theta-projective-details.tex`: 10485 bytes, 75 lines, SHA-256 `b901010fe9525b7fd33b6b7965c55bcc791eaafdaa145476c23539df6264cbe2`.
