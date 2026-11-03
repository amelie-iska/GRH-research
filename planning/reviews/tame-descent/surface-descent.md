# Tame cubic descent of the balanced theta column

Independent read-only derivation, 2026-11-03. Let k=Q(omega), omega^2+omega+1=0, R=k[[u]], S=k[[v]], u=v^3. The actual theta order is base changed to k. All statements below retain the specified branch representation and distinguish a semilinear group action from an fpqc descent datum. No shared sources were changed.

## 1. Exact action and commutator signs

On W=S^3 write epsilon_0,epsilon_1,epsilon_2 for the vertex basis. The plus arrows act as v E_(i,i-1), with indices modulo3; minus arrows act by zero. Their full-cycle products are v^3 E_ii=u E_ii. Thus this is a module for the full completed order: long paths converge v-adically. With the stipulated travel multiplication these are left-module matrices, sending epsilon_(i-1) to v epsilon_i.

Let g fix k and send v to omega v. Put D=diag(1,omega^-1,omega^-2), T=Dg, and C epsilon_i=epsilon_(i+1). Since g fixes D, T^3=1. On the plus arrow A_i=vE_(i,i-1),

T A_i = omega v omega^-i E_(i,i-1) g
      = v omega^(-(i-1)) E_(i,i-1) g = A_i T.

The wrap index satisfies the same identity modulo3. Hence T is a genuine g-semilinear **Lambda-linear** action, not just a coefficient action on an unrelated carrier. C is S-linear and intertwines the theta rotation of the order. Directly on every basis vector,

T C=omega^-1 C T.

Both T^3 and C^3 are1. The commutator is central and nontrivial. Their action is a representation of the cubic central extension (the finite Heisenberg relation), not a commuting C3-by-C3 action on the vector bundle. Projectivization removes this scalar commutator; it does not automatically identify the projective object with the projectivization of a descended R-column lattice.

## 2. The invariant lattice restores the original cut

T(sum_i f_i epsilon_i)=sum_i f_i epsilon_i means g(f_i)=omega^i f_i. The coefficient of v^n can therefore be nonzero only when n=i modulo3. Consequently

L=W^T=R epsilon_0 + R v epsilon_1 + R v^2 epsilon_2.

In its basis l_i=v^i epsilon_i the three plus arrow coefficients are(u,1,1), respectively for i=0,1,2. Thus invariants recover the unbalanced hereditary cut column already studied; they do not descend the balanced arrows to another symmetric rank-one-per-vertex lattice over R.

C sends the T-invariant space to the T-eigenspace of weight omega^-1, rather than preserving it. The corrected operator vC does preserve L. Its matrix is

A=(vC)|L=[[0,0,u],[1,0,0],[0,1,0]],
A^3=uI, det A=u.

It is an R-linear map but not an R-module automorphism. After inverting u it is invertible and gives a projective order-three action, since its cube is central. It does not yield an ordinary K-linear C3-linearization: rescaling A by h in K would require h^3 u=1, impossible by the integral valuation of K.

More generally a scalar correction fC commutes with T precisely when g(f)=omega f. Every such nonzero f in S is v h(u), h in R; none is a unit. Over the fraction fields it has this same form with h in K and still has cube u h^3. Scalar correction therefore records the central obstruction rather than removing it.

The full underlying R-module W is free of rank9, with each vertex rank3. Its three T-eigenspaces are free rank3 and C cyclically permutes them. Keeping all these weights retains rotation at the expense of tripling the column size. The rank-one-per-vertex obstruction was never an obstruction to this larger carrier.

## 3. Flat base change, ramification and failure of naive Galois descent

R->S is finite **free of rank3**, with basis1,v,v^2, hence faithfully flat. It is incorrect to call this ring extension nonflat. It is ramified and is not a mu3 torsor at v=0. For example S tensor_R S=S[w]/(w^3-v^3); its three linear factors are not comaximal at v=0, so it is not the product of three copies of S there. After inverting v it is a genuine etale cubic Galois cover.

The semilinear action T is not by itself the full ordinary fpqc descent datum across that branchpoint. The natural comparison

S tensor_R W^T -> W

has matrix diag(1,v,v^2). It is injective, has determinant v^3=u, and has cokernel

(S/(v)) epsilon_1 + (S/(v^2)) epsilon_2.

It is not an isomorphism, although W^T is R-free. The **comparison cokernel** is nonflat torsion; the base extension is flat. Over the punctured spectrum the comparison is an isomorphism. At v=0 the stabilizer acts on the fiber by D with three distinct weights; a vector bundle pulled back from the coarse R-base would have trivial stabilizer action. This supplies another direct view of the failure.

Since3 is invertible, averaging makes T-invariants exact as an R-linear functor on equivariant short exact sequences. Exactness of invariants is not monoidality, and does not repair this vector-bundle comparison.

## 4. A real projective/algebra-level escape

The scalar commutator cancels on the S-linear matrix algebra End_S(W), with induced descent H -> D g(H) D^-1. Its invariant entries satisfy

H_ij in v^([i-j]_3) R.

Conjugating to the invariant-column basis l_i=v^i epsilon_i changes their exponents to[i-j]_3+j-i: zero for i>=j, and3 for i<j. Thus the invariant algebra is exactly the hereditary cycle order with entries R on and below the diagonal and uR above it. This is the plus hereditary branch order for the chosen cut.

Conjugation by C commutes with this matrix descent, because the original commutator is scalar. On the invariant order it is conjugation by A=vC in generic coordinates. Although A is not an integral unit, it normalizes this hereditary order and Ad_A has order three because A^3=uI. This is an actual descended **algebra automorphism** and a useful positive explanation for determinant-level rotation invariance.

This matrix algebra is End_S(W), not the much smaller commutant End_Lambda(W). Its invariants recover the existing branch order; they do not supply a new arithmetic action or a vector-lattice linearization. Keeping both branches and the paired residues leads back to the actual glued theta order rather than a multiplicity-one arithmetic reconstruction.

## 5. Tensor/Schur selection rule: what is proved

For the induced global tensor operators on W tensor_S ... tensor_S W of degree m,

T_m C_m=omega^-m C_m T_m.

The same holds on any nonzero homogeneous Schur summand S_lambda(W) of degree m in characteristic zero. Indeed Schur maps preserve composition, scalars act by their m-th power, and the Young projector commutes with the induced operators. The operators are invertible on the nonzero summand. Therefore **these particular induced operators commute if and only if3 divides m**. Equivalently C_m preserves their invariant lattice exactly in this case. Constant character twists or scalar unit rescalings do not change this condition: evaluating g(f)=omega^m f at v=0 excludes a unit unless omega^m=1. For mixed covariant/contravariant constructions the relevant number is net central degree, not necessarily the number of tensor factors; End(W)=W tensor W^vee has net degree zero.

This is a precise central-commutator selection rule, not a theorem about every possible modified lift, determinant category or nonlinear operation. It also does **not** say that3|m suffices for ordinary vector-bundle descent through the branchpoint. For Sym^3 W the induced operators commute, but the fiber stabilizer weights have multiplicities(4,3,3). For example epsilon_0^2 epsilon_1 has nontrivial weight omega^-1. The natural pullback from invariants still has diagonal v-powers and determinant v^9=u^3, so is not an isomorphism. One gets a new invariant R-lattice with rotation; one has not descended the original balanced S-bundle unchanged.

There is a further categorical limit. The global tensor W^tensor m or Schur module S_lambda(S^3) is a construction on the carrier and its C,T operators; Lambda has no specified Hopf algebra structure, so these are **not automatically Lambda-module tensor functors**. The actual vertexwise Sym^m of the one-dimensional vertex spaces has arrows v^m, whose full-cycle scalar is u^m. It changes the original fixed central R-action for m>1. Vertexwise exterior^3 of those rank-one vertex spaces is zero. Neither operation can silently be used as a nonzero central-u-fixed projective functor. Any genuine derived Schur or twisted-base replacement needs separate definitions and exactness/comparison theorems.

## 6. Determinant line: genuine escape, nonunit comparison

The top exterior line det_S W has D-determinant omega^-3=1 and C-determinant1. Its induced action is just g on coefficients, so its invariant line is R times vol, vol=epsilon_0 wedge epsilon_1 wedge epsilon_2. Its pullback to S really is det_S W. Thus the degree-three determinant line removes both the central commutator and the fiber stabilizer obstruction in this particular case.

However determinant and coarse invariants do not commute via an isomorphism here. The natural map

det_R(W^T) -> (det_S W)^T

sends l_0 wedge l_1 wedge l_2 to v^3 vol=u vol. Its image is uR vol and its cokernel is R/(u). This factor is a divisor at the branchpoint; it is not a unit that can be dropped from an integral determinant-line comparison. Abstractly both modules are free rank-one R-lines, but their given rational trivializations and natural comparison differ by u. Correspondingly det(A)=u for the invariant-lattice rotation A=vC, whereas the descended det(C) is1 on the other line. A claimed determinant-functor escape must say which line and which trivialization it uses.

The degree-three determinant operator records only a top product. It is not the full characteristic polynomial det(I-tF), whose exterior-degree-one and exterior-degree-two terms retain trace information and are not homogeneous of degree three. In particular the two elliptic arithmetic operators at7 have the same determinant7 but distinct polynomials1-4t+7t^2 and1-t+7t^2. A determinant line alone cannot reconstruct that distinction. No assertion is made that every more elaborate degree-three Schur construction, additional projector or Tate twist is impossible; such a construction must establish its own central action, spectrum and determinant comparison.

A concrete warning is the CM expression A I+B C on the balanced column, with A,B fixed by g. Unless B=0, it does not commute with T. Replacing C by vC makes it preserve the invariant lattice, but changes its characteristic polynomial to

det(I-t(AI+B vC))=(1-A t)^3-B^3 u t^3.

Its special fiber is(1-A t)^3. Thus this elementary scalar compensation reintroduces a cut/nilpotent degeneration and does not retain an arbitrary constant quadratic arithmetic factor.

## 7. Verification and scope

Independent exact phase calculations checked all arrow/semilinear identities on v^n epsilon_i for n<18; all global tensor central weights through degree six; the ten degree-three symmetric monomials and their(4,3,3) fiber weights; and every invariant matrix-entry carry exponent. There were1200 phase/arrow/tensor assertions, plus the symmetric and matrix-order checks. No random seeds, numerical complex approximations, installations or shared output writes were used. The coefficient-by-coefficient arguments above are the full proofs, not inferences from truncation.

The established positive statements are the explicit invariant lattice, the projective/hereditary-order rotation, and a genuine descended top determinant line with its nonunit comparison recorded. The failures concern the original balanced column's coarse-base vector-bundle descent, its strict rank-one-per-vertex rotation, and the automatic use of global Schur operations as order-module functors. There is no universal no-go for alternative determinant categories, root-stack/parabolic replacements, larger or ramified carriers, arithmetic semilinear actions or Hilbert–Polya models. No conductor, Tate-lattice, global determinant or GRH claim follows from this calculation.

## 8. Full unramified deck-equivariant lattice kernels force vertex rank divisible by six

There is a further elementary theorem that allows branch intersections and does not assume an integral direct sum of the two branches.

Let W0 be a nonzero finite R-free **left** Lambda-module with invertible R-linear maps S0,A0 implementing sigma and alpha, respectively. In particular, a strict full C6-linearization, with S0^3=A0^2=1 and commuting generators, satisfies these hypotheses. Let V=W0 tensor_R K. The generic central idempotents split V=V_+ plus V_-, since Lambda_K=M3(K) times M3(K). Define L_+=W0 intersect V_+ and L_-=W0 intersect V_- inside V.

These intersections are finite R-free Lambda-stable lattices. They span the two generic branch modules, although their sum need only have finite index in W0 rather than equal it integrally. Sigma preserves the generic branches and alpha exchanges them, so S0 preserves L_+,L_- and A0 exchanges them. The rank argument therefore applies to these actual branch intersections.

Write n_+ for the multiplicity of the standard three-dimensional simple in V_+. Every e_i L_+ has R-rank n_+. The minus arrows vanish on this lattice, while the product of the three plus arrows in cyclic order equals uI on each vertex space, by ue_i=c_i^++c_i^- and vanishing of the minus branch. Choose R-bases of the three e_i L_+. The plus arrows are square n_+-by-n_+ matrices B_i with nonzero determinant and nonnegative valuations m_i=val_u det B_i. Taking determinant valuations of their cyclic product yields

m_0+m_1+m_2=n_+.

The invertible rotation intertwiner gives unit change-of-basis matrices at the vertex lattices. Its arrow identities identify the three determinant valuations. Hence m_0=m_1=m_2 and n_+=3m for a nonnegative integer m. The same applies to the minus branch, and the branch-swap intertwiner gives n_-=n_+. Generic rank additivity now gives, without any integral splitting assumption,

rank_R(e_i W0)=n_++n_-=6m for every i,
rank_R W0=18m.

Because W0 is nonzero and torsion free, its generic fiber is nonzero. Branch swap then makes m positive. The regular left module Lambda with its actual order automorphisms realizes the minimum m=1. Thus the divisibility is sharp. The strict finite-order group identities were not needed for the divisibility; invertible central-fixed rotation and branch-swap intertwiners already suffice.

The hypothesis boundary is exact. On one ramified branch over S with u=v^3, the same arrow determinant equation has right-hand valuation3n_+, so equality of the three valuations need not force3|n_+. Both branches can then have vertex rank2 over S. Restriction of scalars to R multiplies that rank by3, restoring6. Allowing a noninvertible intertwiner, a changed action on the central base, derived/projective symmetry data or a different determinant target is outside the theorem.

### Consequence for ordinary coefficient-kernel determinant functors

This closes more than the uniform scalar-tensor test. Use W0 as a bimodule kernel and define Phi_W0(P)=P tensor_Lambda W0 on Perf(Lambda). Since W0 is finite R-free, this again maps perfect Lambda-complexes to perfect R-complexes. Let f be any Lambda-linear endomorphism of P=direct_sum_i(e_iLambda)^(a_i), with top matrices f_i. Filter W0/uW0 by the left radical of B=Lambda/uLambda. A positive-length entry of f raises this filtration; a top scalar block acts as f_i on each copy of the i-th vertex space in every layer. Summing those layer dimensions gives dim_k e_i(W0/uW0)=rank_R e_iW0=6m. Therefore

det_R(I-T Phi_W0(f)) modulo u
 = product_i det_k(I-T f_i)^(6m).

Bounded perfect-complex alternating ratios have the same divisibility. Thus an ordinary determinant produced by a **finite R-free coefficient lattice kernel with these invertible full deck intertwiners** still cannot specialize to a multiplicity-one quadratic local factor or the complete curve zeta with its simple poles. This proof allows arbitrary f and allows the direct sum of the two disjoint branch intersections to have finite index in W0 rather than equal W0.

It does not classify all triangulated functors or all determinant-line natural transformations. In particular it says nothing universal about a kernel complex with only derived equivariance, torsion/perfect replacements outside these lattice hypotheses, twisted Picard targets, noncommutative/reduced determinants or infinite analytic constructions. Such constructions need their own precise hypotheses. The earlier chosen branch functor violates the full deck-kernel hypothesis and is therefore a valid, explicitly different multiplicity-one example rather than a counterexample to this theorem.
