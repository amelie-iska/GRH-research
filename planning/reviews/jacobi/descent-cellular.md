# Elliptic theta descent, deck automorphisms and local arithmetic acceptance test

Read-only independent mathematical review, 2026-11-03. No shared source, manuscript, script, environment or existing output was changed. The formulas below are derived from the displayed cover and finite-field sums; no Frobenius matrix is fitted from a desired answer.

## 1. The actual deck group and labelled order action

Work in characteristic different from2,3, with d nonzero. Let E_d be the smooth projective curve y^2=x^3-d and beta_d=x^3/d. Over an algebraic closure, x can be multiplied by any cube root c of1 and y by either square root e of1. These six automorphisms preserve beta. The generic fiber has six points and the extension of function fields has degree six, so these already form the full deck group mu3 times mu2, isomorphic to C6.

For E1 over C choose a base value t in(0,1), and label its fiber by x=zeta^j t^(1/3), y=+i sqrt(1-t), j=0,1,2, as darts0,1,2; use the negative y sign as darts3,4,5. Analytic continuation round0 is sigma=(012)(345); round1 is alpha=(03)(14)(25). Under this explicit labelling the deck maps x->zeta x and y->-y act by sigma and alpha themselves. They commute. Their product is

r=sigma alpha=(0 4 2 3 1 5).

It has order six, with sigma=r^4 and alpha=r^3. A permutation commuting with sigma and alpha is determined by the image of one dart, because their action is transitive; therefore the centralizer has at most six elements. This C6 supplies six, proving the full centralizer assertion. An exhaustive independent check of all720 permutations agreed.

Let tau=sigma^-1 and phi=alpha tau, as in the project. For every g in this centralizer define theta_g(e_[h])=e_[gh] and theta_g(a_h)=a_gh. Commutation with alpha makes the vertex formula well-defined; commutation with tau preserves sources and targets. Commutation with phi sends each forbidden pair a_h a_(phi h) to another forbidden pair. Hence theta_g is an actual graded polynomial algebra automorphism, preserves J, and extends continuously and uniquely to the J-adic order Lambda. Its inverse is theta_(g^-1), and theta_g^6=1.

The global central parameter u is the sum of full permitted turns based at all dart occurrences. The automorphism permutes those turns, hence fixes u. It is consequently R=k[[u]]-linear. In the normalization it permutes branches and rotates their state coordinates. When a chosen cycle cut moves, matrix coordinates can acquire u factors; an arbitrary constant permutation conjugacy need not preserve the chosen hereditary matrix order. The path description above avoids that coordinate error. The normalization radical is the conductor here: its diagonal residues all vanish, and multiplication by separate normalized diagonal idempotents forces that vanishing for any two-sided normalized ideal inside Lambda. Theta preserves it, in particular uB. This is compatibility with the **order conductor ideal**, not a computation of the elliptic curve's arithmetic conductor at bad primes.

Restriction along theta_g is an exact autoequivalence of the module category and preserves finite projectives and R-free lattices. It acts on determinant lines only with the correct coefficient/automorphism conventions. On an equivariant finite R-free module a strict C6-linearization has sixth power1; its generic eigenvalues are roots of unity. This gives useful categorical symmetry, not weight-one Frobenius.

## 2. Descent cocycle, Frobenius direction and differential character

Choose a^3=d and b^2=d and set phi_d:E1->E_d by (x0,y0)->(a x0,b y0). It preserves beta because a^3=d. For an absolute Galois element s, the descent cocycle in these coordinates is

h_s=phi_d^-1 s(phi_d)=(s(a)/a, s(b)/b) in mu3 times mu2.

It satisfies h_(st)=h_s s(h_t); it is not an ordinary constant-group character if the Galois action on mu3 is nontrivial.

Now let q be an odd prime power with characteristic not3 and q congruent1 modulo6, and let d lie in F_q^*. Use the **q-power Frobenius morphisms** F_d and F_1 on the respective curves. Direct substitution, not a convention guess, gives

phi_d^-1 F_d phi_d = h_d F_1,

h_d(x,y)=(c x,e y), c=a^(q-1)=d^((q-1)/3), e=b^(q-1)=d^((q-1)/2).

The two root-of-unity factors lie in F_q and commute with F_1. This identity fixes the positive twist orientation. It must not be replaced by h_d^-1 F_1 while retaining the same phi direction.

For omega_d=dx/y, phi_d^*omega_d=(a/b)omega_1. On E1 the deck pullback is h_d^*omega_1=(c/e)omega_1=ce omega_1. Choose an embedding of the finite-field mu3 into C and define rho(d) to be the image of d^((q-1)/3); let eta be the quadratic character. The deck character is therefore

lambda_d=rho(d) eta(d).

Replacing rho by its inverse exchanges the two conjugate character lines; it does not change the final unordered Frobenius polynomial. The ratio a/b itself is not the finite-order Frobenius character; its Galois ratio is c/e.

There are two important inverse issues. Arithmetic Galois acts on the Tate module by the positive h_d factor under the transported point representation. On its contragredient cohomology representation that factor is inverse; geometric Galois Frobenius reverses it again. Pullback by the displayed q-power morphism has the same characteristic roots as its Tate-module endomorphism, and its pullback composition has the positive h_d character. Keep these functors explicit rather than using an unqualified 'Frobenius'. Also, q-power pullback on regular differentials in characteristic p is zero: the deck differential character does **not** itself supply Frobenius eigenvalues of size sqrt(q).

## 3. Elementary local Jacobi calculation with all signs

Extend the nontrivial characters rho,bar(rho),eta by zero at0, and define

J(rho,eta)=sum_(t in F_q) rho(t) eta(1-t),
pi_q=-eta(-1) J(rho,eta).

The cube map has fiber size1+rho(z)+bar(rho)(z), including z=0. Consequently, with a_q(d)=q+1-#E_d(F_q),

a_q(d)=-sum_x eta(x^3-d)
       =-sum_z [rho(z)+bar(rho)(z)] eta(z-d)
       =-eta(-d)[rho(d)J(rho,eta)+bar(rho)(d)J(bar(rho),eta)]
       =eta(d)[rho(d)pi_q+bar(rho)(d)bar(pi_q)].

The constant1 term disappears because the sum of a translated nontrivial quadratic character is zero. The sign eta(-1) comes specifically from eta(t-1)=eta(-1)eta(1-t). Omitting it changes the answer at q congruent3 modulo4.

For completeness the size is independently justified. For a nontrivial multiplicative character chi and a nontrivial additive character psi, its Gauss sum G(chi) has |G(chi)|^2=q: substitute x=ty in the squared norm, with the inner sum over y nonzero equal q-1 for t=1 and -1 otherwise. Because rho,eta,rho eta are all nontrivial, grouping G(rho)G(eta) by x+y=z gives

G(rho)G(eta)=J(rho,eta)G(rho eta).

The z=0 term is zero since rho eta is nontrivial. Taking absolute values proves pi_q bar(pi_q)=q. Thus the local polynomial obtained from this curve count is

P_d(T)=(1-lambda_d pi_q T)(1-bar(lambda_d)bar(pi_q)T)
      =1-a_q(d)T+qT^2.

This genuinely recovers the finite-field local factor, rather than postulating its roots. Its identification with the elliptic curve's Tate/etale H1 characteristic polynomial uses the classical cohomological/isogeny theorem, external to the order construction. A primary reference checked here is [Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf), II Proposition6.4 and Corollary6.5 (printed p71, PDF p76), IV Proposition9.1/Theorem9.4 (printed pp148–150, PDF pp153–155), and Theorem9.10/Remark9.11 (printed pp156–157, PDF pp161–162). They identify the Tate characteristic polynomial, degree/determinant and finite-field zeta numerator. This is a focused theorem/proof reading, not a fresh full241-page audit.

For q=7 choose primitive root3 and rho(3)=omega, omega^2+omega+1=0. Exact summation gives J=pi=3+2omega=2+sqrt(-3). For d=1, lambda=1, a7=4 and P=1-4T+7T^2. For d=2, rho(2)=omega^2, eta(2)=1; lambda pi=-1-3omega, giving a7=1 and P=1-T+7T^2. Thus the displayed nonisomorphic arithmetic models are distinguished by the descent character **together with the untwisted arithmetic pi**.

At q congruent5 modulo6, cubing is bijective and the same direct quadratic-character count gives a_q(d)=0. There is no nontrivial cubic character on F_q^* for the preceding split formula; Frobenius exchanges the two CM lines. Bad reduction primes dividing6d are excluded from all these formulas. No arithmetic conductor, bad local factor or global functional equation is recovered here.

## 4. An actual two-dimensional carrier in the dessin itself

The theta embedding has two graph vertices, three oriented edges and one face on the torus. Orient the edges from the first black vertex to the second. Its rational cellular chain complex is

C2=Q -> C1=Q^3 -> C0=Q^2,

d2=0, d1(each edge)=v_minus-v_plus. The face boundary is zero in cellular chains because each edge occurs once in each orientation. Thus H1 is the sum-zero plane in Q^3. With b1=e0-e1 and b2=e1-e2,

sigma|H1 = [[0,-1],[1,-1]],
alpha|H1 = -I,
r|H1 = [[0,1],[-1,1]].

This is a concrete rational C6 representation extracted from the labelled dessin. The characteristic polynomial of r is X^2-X+1, and on complex H1 its two characters are -omega and -bar(omega), agreeing with the holomorphic/antiholomorphic deck characters. No arbitrary two-dimensional representation was substituted for this carrier.

Write pi_q=A+B omega and rho(d)=omega^j. Define on this H1

F_(q,d)=eta(d) sigma^j (A I+B sigma).

Its eigenvalues are exactly lambda_d pi_q and their conjugates, by the preceding direct sum computation. Its rational matrix is therefore obtained from a finite-field Jacobi sum and the actual deck matrix. Its trace and determinant are a_q(d) and q. This is a genuine positive local arithmetic encoding; the coefficients A,B remain additional arithmetic input and do not follow from the finite permutation.

One can also give an honest finite cellular chain lift. On C1 use the same polynomial in its three-cycle permutation. Put gamma=eta(d)(A+B). Its invariant edge line has eigenvalue gamma. On C0 choose eigenvalue1 on Q(v_plus+v_minus) and gamma on the boundary line Q(v_minus-v_plus); on C2 choose multiplication by q. These maps commute with d1,d2. Thus

det(1-T F0) det(1-T F2)/det(1-T F1)
    =(1-T)(1-qT)/P_d(T)=Z(E_d/F_q,T)^(-1).

The usual zeta sign convention takes the reciprocal. This complex is perfect over Q and built from the actual cell structure. It is not a complex of projective Lambda-modules, not a proved functor from order modules to arithmetic cohomology, and not a proof that its constructed chain map is induced by the inseparable geometric Frobenius on this topological cellulation. Identifying its determinant with the classical local factor uses exactly the curve-count input proved above. The separately chosen H0/H2 eigenvalues1,q should remain explicit; a uniform polynomial in the finite deck operator would not give both.

## 5. Precise finite-deck obstruction and the positive relative statement

Any finite-dimensional complex representation obtained solely by applying a C6 deck permutation has operator sixth power1; all eigenvalues have absolute value1. A weight-one elliptic Frobenius has eigenvalues of absolute value sqrt(q)>1 and determinant q. These cannot be the same operator. The same conclusion holds for strict finite-order actions on the generic fiber of finite R-free lattices or finite equivariant complexes. Finite-order deck action and Frobenius action are different pieces of data.

Even d=1 has h_d=1 at every split prime. Its base pi_7=3+2omega, pi_13=-1-4omega and pi_19=-5-2omega already differ. The identity permutation alone cannot select those arithmetic values. Merely multiplying a chosen permutation by sqrt(q) does not generally recover the correct phase either: at7 the normalized trace4/sqrt(7) is not the trace of a determinant-one two-dimensional C6 representation.

The positive result is exact: once the base arithmetic H1/Frobenius has been supplied independently, the finite descent cocycle twists it correctly and recovers every sextic twist at that good split prime. For this CM example the base arithmetic endomorphism can be constructed from the Jacobi sum rather than specified as a desired 2-by-2 characteristic matrix. A putative semilinear order lift still has to explain how that coefficient is produced and how its determinant is compared with the cohomological one. This argument does not rule out richer pencils, nonfinite-order lifts or a future arithmetic functor.

## 6. Naive tensor insertion: exact multiplicities and categorical limits

Let V carry the preceding two-dimensional arithmetic operator F_V with characteristic polynomial P_d. Picking a vertex simple S_e and forming S_e tensor_k V, with all arrows zero and operator id tensor F_V, gives an actual finite-dimensional Lambda-module and its ordinary k-determinant is P_d. This is a legitimate finite-dimensional scalar encoding. However S_e has an infinite forbidden-word minimal projective resolution, so this object is not perfect over Lambda. Being nonperfect over Lambda does not invalidate its k-determinant; it prevents claiming this construction lands in Perf(Lambda). The selected vertex is moreover not stable under the full C6: sigma cyclically permutes the three quiver vertices. A single-vertex choice therefore breaks that full deck-equivariance.

On the free order module Lambda tensor_k V, using the Lambda-linear operator id_Lambda tensor F_V, the underlying R-module determinant is P_d(T)^18 because rank_R Lambda=18. On eLambda tensor_k V it is P_d(T)^6: each vertex has one row in each of two 3-by-3 hereditary branches. The full three-simple orbit, with the same uniform operator on each summand, gives the ordinary k-polynomial P_d^3.

More generally, every finite sum of the three basic projectives has R-rank divisible by6. A bounded complex of these projectives with a uniform external tensor factor V and identity action on its order terms therefore has alternating determinant P_d^(6m), with m an integer. Alternating terms can cancel multiplicities but do not produce exponent1 in this restricted construction. Taking a sixth or eighteenth root of the resulting scalar rational function is not automatically a determinant-line functor or a canonical categorical root. It simply reuses the externally known factor unless a separate construction proves it.

These powers apply to id tensor F_V. A genuine deck-semilinear operator theta_h tensor F_V instead satisfies F(a m)=theta_h(a)F(m); it is generally not Lambda-linear. Its R-characteristic determinant involves the deck eigenvalues as well and need not be P_d to the same rank. Likewise adding a vertex permutation to the three-simple orbit changes the factor to products with those permutation eigenvalues. One must not combine the Lambda-linearity and multiplicity claims from the first construction with the deck-equivariance of the second.

As an R-perfect torsion complex, a vertex simple has zero generic rank; resolving its u-torsion over the DVR makes identical lifted arithmetic factors cancel in the generic alternating R-determinant. This is another reason to specify whether a determinant is over k, over R, on a generic fiber, or on a derived special fiber. No one of these choices automatically yields all the others.

## 7. Checks and remaining acceptance conditions

Independent exact diagnostics used no random seeds, numerical complex arithmetic or software installation. Exhausted720 dart permutations to check the centralizer, derived all six powers of r, and computed character sums using pairs of integers for Z[omega]. For each nonzero d at split primes7,13,19,31,37,43,61,67,73,79,97, the Jacobi-sum trace matched the direct quadratic-character point count and the norm was q:516 twist instances. At7 the traces for d=1,...,6 are4,1,5,-5,-1,-4. These corroborate the universal elementary derivation; they do not replace its proof or prove a cohomological order functor.

The accepted next local arithmetic test can therefore demand: (1) the actual theta order automorphism above; (2) its correct cocycle and Frobenius convention; (3) independent construction of the arithmetic pi or the genuine curve H1; (4) a functor or comparison from a specified order/projective category respecting that action; (5) a determinant identity with the exact multiplicity and coefficient category; (6) separate ramification and bad-prime data. This review supplies1–3 locally and a concrete Q-perfect cellular carrier, while4–6 remain new work. Finite-field elliptic purity is classical and is neither Dirichlet GRH nor global Hasse–Weil GRH.

## 8. Reduced CM chain lift, exact homotopy and positive Gram form

For implementation it is cleaner to multiply the twist first in Z[omega]: let alpha_d=lambda_d pi_q=A_d+B_d omega, and set

F1=A_d I+B_d P on C1,
gamma=A_d+B_d,
F0=1/2 [[1+gamma,1-gamma],[1-gamma,1+gamma]] on (v_plus,v_minus),
F2=q on C2.

Then d1 F1=F0 d1 because d1 P=d1 and F0 sends delta=v_minus-v_plus to gamma delta. The zero d2 gives the other chain equation. The edge sum is a P-invariant line with F1 eigenvalue gamma; the complementary sum-zero plane has matrix M(A_d,B_d)=[[A_d,-B_d],[B_d,A_d-B_d]]. Consequently

det(I-TF1)=(1-gamma T)P_d(T),
det(I-TF0)=(1-T)(1-gamma T),
det(I-TF2)=1-qT.

The local zeta is **odd determinant divided by even determinants**:

Z=det(I-TF1)/(det(I-TF0)det(I-TF2))
 =P_d(T)/[(1-T)(1-qT)].

This identity is a rational function identity, so cancellation remains legitimate even at a zero of1-gamma T. The inverse ratio is the usual positive-even alternating determinant. Neither sign convention should be silently swapped.

This reduced chain lift is strictly C6-equivariant: P acts as the edge cycle and the identity on C0,C2; alpha acts as -I on C1, swaps the two vertices on C0, and preserves the oriented face on C2. The polynomial F1 and symmetric F0 commute with those actions.

It also agrees with the earlier full Kummer-twisted lift in the homotopy category, even when their literal chain maps differ. Let pi=A+B omega, lambda=kappa omega^j, kappa=eta(d), j=0,1,2, and set S=I+P+P^2. If T1=kappa P^j(AI+BP) and R1=A_d I+B_d P, then

T1-R1=kS,

where k=0 for j0, k=kappa B for j1, and k=kappa A for j2. This follows by reducing omega^2=-1-omega and P^3=I. Their invariant-edge eigenvalues differ by3k, so T0-R0 acts by3k on the boundary line and by zero on the H0 line; their F2 are identical.

Define H:C0->C1 by H(delta)=k(e0+e1+e2) and H(v_plus+v_minus)=0, with all other homotopy degrees zero. Then d1 H(delta)=3k delta, while H d1(ei)=k(e0+e1+e2)=kS(ei). Thus T-R=dH+Hd exactly in every degree. This construction is rational, as expected from the half-sum splitting of C0; no integral cellular or Tate-lattice claim follows. It proves **homotopy-class compatibility**, not equality of both literal chain maps.

There is also a fixed explicit positive form on this cellular H1. In the basis(e0-e1,e1-e2), the ordinary Euclidean edge metric restricts to G=[[2,-1],[-1,2]], which is positive definite. Direct multiplication gives C^t G C=G for C=M(0,1). Since C^2+C+I=0, the G-adjoint of C is C^-1=-I-C. Hence

M(A_d,B_d)^t G M(A_d,B_d)
 =(A_d^2-A_d B_d+B_d^2)G=qG.

Thus the independently computed Jacobi operator is sqrt(q) times a G-unitary on the actual two-dimensional dessin carrier. The form does not depend on q or d. Its scale identity uses the external arithmetic norm alpha_d bar(alpha_d)=q. It supplies genuine finite-field positive weight-one data; it does not construct a global arithmetic complex or prove any number-field GRH. The full chain operator need not satisfy q-unitarity on all three chain degrees: their other prescribed homological eigenvalues are1 andq, and a contractible piece has gamma.

The reduced lift was additionally checked over exact Fractions for all516 twists above: P restricted to the displayed basis equals C; dF1=F0d; F1 restricted to H1 equals M(A_d,B_d); F^tGF=qG; and both degree components of the explicit Kummer-reduction homotopy are exact matrix equalities. All passed. These checks wrote no shared output. Two simple sign diagnostics are worth retaining: omitting -eta(-1) changes the base trace at7 from4 to-4, and using lambda_d^-1 with the fixed rho/phi convention changes d=2's trace at7 from1 to-5.
