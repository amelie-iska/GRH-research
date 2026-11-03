# Theta Jacobi/cellular final review

Independent review, 2026-11-03. Read all 43 lines of papers/theta-jacobi-core.tex, all 70 lines of papers/theta-jacobi-details.tex, and all 161 lines of the corrected lean-analytic/ThetaJacobi.lean. The final core wording was reread after the coefficient-field and determinant-sign corrections. Extended only scripts/check_theta_jacobi.py and its authorized outputs/checks/2026-11-03-jacobi/exact-checks.json; manuscripts, Lean, planning files and source clones were not edited. This report distinguishes the paper's elementary uniform proofs, universal formal components and finite exact corroboration.

## Verdict

No unresolved mathematical error was found in the uniform local character-sum theorem or the rational cellular construction. The sign of j, positive descent twist, actual cellular basis, Gram matrix, determinant cancellation and rational homotopy all check out. The initial independent Lean compile failed on three elaboration/proof details. The author corrected those; a fresh independent compile of the latest thirteen declarations passed with warnings treated as errors and standard foundational dependencies only.

Two paper corrections requested during this review are now present: the order insertion uses the characteristic-zero order Lambda_Q, distinct from the finite-field curve; and the curve zeta is called the **odd-over-even determinant ratio**, with the conventional even-over-odd alternating determinant its inverse. The global paragraph now fixes a nonzero rational d and states the convergence range proved by the elementary bound. These resolve the category/sign ambiguities in the initial draft.

## 1. Uniform finite-field theorem

The hypotheses exclude characteristics 2 and 3 and d=0. The split case q congruent 1 modulo 3 has nontrivial cubic rho and quadratic eta, zero extended at 0. The cube-fiber formula uses the literal constant 1, rather than mathlib's zero-extended trivial character. This is essential at zero and is stated correctly in both paper editions.

Square-fiber counting gives a_q(d)=-sum_x eta(x^3-d). On grouping by cubes, the literal constant contribution disappears by quadratic-character orthogonality. Substitution t=du gives rho(d)eta(-d)J(rho,eta), including both endpoints because of zero extension. With j=-eta(-1)J and lambda_d=eta(d)rho(d), the result is the trace of lambda_d j. This checks the sign at primes congruent 3 modulo 4 and the positive, rather than inverse, twist orientation.

The Gauss norm argument is independent of the target elliptic factor: for a nontrivial character, x=uy gives q-1 at u=1 and -1 otherwise. In the Gauss–Jacobi product the x+y=0 fiber vanishes because rho eta is nontrivial; its orders 3 and 2 cannot cancel. The three nontrivial Gauss norms give |J|²=q. Consequently j and lambda_d j have norm q, and the local factor is 1-a_q(d)T+qT². The proof works for all prime powers meeting the hypotheses, whereas the checker below is deliberately confined to prime fields.

When q is congruent 2 modulo 3, cubing is bijective, giving trace zero. The details correctly distinguish odd and even extension degrees of a residue characteristic congruent 2 modulo 3. All split values belong to Z[omega] because the summands are signs times cube roots. No finite-field purity or RH conclusion was assumed to establish this particular norm formula.

The exact examples are consistent. At 7, with least primitive generator 3 and rho(3)=omega, j=3+2omega. At d=2, lambda=omega² and alpha=-1-3omega, giving traces 4 and 1 respectively. At 13, with rho(2)=omega, J=1+4omega but j=-1-4omega: this example checks the sign which the first prime alone does not distinguish.

The final identification with an elliptic Tate/etale H1 characteristic polynomial is explicitly a classical external trace/determinant theorem. The manuscript does not claim to derive an arithmetic order functor from the character sum. I checked the elementary proof as written here, not a new full audit of every primary source cited for general cohomology.

## 2. Actual cellular carrier

The given cell structure is the torus theta dessin, with two black vertices, three oriented edges and one face. Its boundary matrix is

    d1=[[-1,-1,-1],[1,1,1]],     d2=0.

Each edge occurs with both orientations in the face, so the zero face boundary is correct. The inclusion columns b0=e0-e1 and b1=e1-e2 give

    inc=[[1,0],[-1,1],[0,-1]],
    P=[[0,0,1],[1,0,0],[0,1,0]],
    C=[[0,-1],[1,-1]],
    G=inc^t inc=[[2,-1],[-1,2]].

Thus d1 inc=0 and P inc=inc C; this is the actual edge rotation, not an abstract representation selected afterward. The involution swaps the two vertices and reverses all three oriented edges, so its C1 action is -I and its H1 action is -I. It preserves the oriented face. G is positive definite, with leading minors 2 and 3, or by the displayed sum-of-squares decomposition.

For alpha_d=A_d+B_d omega, the matrix M_d=A_d I+B_d C is exactly multiplication by this Eisenstein element in the stated basis. Its trace and determinant are 2A_d-B_d and A_d²-A_dB_d+B_d². The universal identity M_d^t G M_d=norm(alpha_d)G therefore gives qG here. This is a fixed positive **scaled isometry**, not a self-adjointness theorem. The matrix normalized by sqrt(q) is unitary in the G metric, proving the local weight-one modulus statement for this carrier.

The finite deck action fixes the common path parameter and relabels the projective resolution correctly. Its finite-order eigenvalues alone cannot create the independently computed norm-q Jacobi coefficient. The draft keeps these two inputs separate.

## 3. Chain lift, exact cancellation and descent homotopy

For gamma=A_d+B_d, the prescribed matrices are

    F1=A_d I+B_d P,
    F0=1/2 [[1+gamma,1-gamma],[1-gamma,1+gamma]],
    F2=q.

F0 acts by 1 on the vertex-sum line and by gamma on delta=v_minus-v_plus. F1 acts by gamma on the edge sum and by M_d on the sum-zero plane. Thus d1 F1=F0 d1, and the d2 equation is zero. The reduced lift is strictly compatible with P and the vertex-swap involution. Coefficientwise determinant identities are

    det(I-TF0)=(1-T)(1-gamma T),
    det(I-TF1)=(1-gamma T)P_d(T),
    det(I-TF2)=1-qT.

The odd-over-even ratio is P_d(T)/((1-T)(1-qT)), the finite-field curve zeta function. This is a rational identity; cancellation does not require dividing by a numerically nonzero value of 1-gamma T at each T. The conventional alternating determinant with exponent (-1)^i is its inverse, as the corrected core and details now consistently state.

Writing the base j=A_1+B_1 omega and lambda=kappa omega^r, the unreduced edge map kappa P^r(A_1 I+B_1 P) differs from the reduced F1 by kS, S=I+P+P², with

    k=0 for r=0;
    k=kappa B_1 for r=1;
    k=kappa A_1 for r=2.

The unreduced boundary scalar differs by 3k. The rational homotopy matrix H:C0→C1 has every row (-k/2,k/2), giving H(delta)=k edge_sum and H(vertex_sum)=0. Direct multiplication yields H d1=kS and d1 H=T0-F0. F2 is unchanged, so the homotopy identities hold in every degree. This proves equality in the rational chain-homotopy category, not equality of the literal chain maps.

Rational coefficients are genuinely needed for the displayed strict deck-equivariant normalization. For p=7,d=2, gamma=-4 and F0=[[-3/2,5/2],[5/2,-3/2]]. Any two-vertex matrix commuting with the swap is [[a,b],[b,a]]; requiring eigenvalues 1 on the sum and gamma on delta forces a=(1+gamma)/2,b=(1-gamma)/2. If gamma is even it cannot be integral in this cell basis. This is a precise limitation of this particular equivariant cellular normalization, not an obstruction to a different integral complex or Tate-lattice comparison.

## 4. Exact checker extension and fresh run

The checker now records the actual chain matrices for **all 516 split twists**, rather than merely their 2-by-2 characteristic matrices. It verifies d1 inc=0, induced Gram data, the C and P actions, both chain equations, F1 inc=inc M_d, H0/edge-sum eigenvalues, strict reduced deck equivariance and M_d^t G M_d=pG. It computes det(I-TF_i) by independent coefficientwise Leibniz expansion, then checks the three factor identities and their cross-multiplied rational cancellation. No floating-point T sampling is used.

For every twist it computes the unreduced map from the original j and actual eta/rho exponent, verifies kS and the 3k boundary difference, constructs H over exact fractions, and checks H d1 and d1 H. There are 172 twists for each cubic exponent, 172 zero homotopy scalars and 344 nonzero ones. The output contains every F0,F1,F2, both unreduced maps and unchanged F2, H, determinant coefficients and the exact k distribution.

Fresh command python3 -B scripts/check_theta_jacobi.py completed with exit 0. The saved JSON was reloaded and validated. Totals:

* 11 split primes, every nonzero d: 516 curves;
* 8 inert primes, every nonzero d: 218 curves;
* 734 curves and 2,813,918 exhaustive affine-pair tests;
* 67,894 rho/eta multiplicativity equalities and 32,904 lambda equalities;
* 516 cellular Gram scaled-isometries;
* 2,064 coefficientwise cellular determinant identities;
* 516 exact rational cellular homotopies;
* exhaustive 720-candidate dart centralizer check and 864 permitted/forbidden word checks through length 12.

All earlier p=7 values and local factor checks remain passing. The prime lists, character normalization, finite bounds and scope are stored in the JSON. This is finite corroboration; it does not replace the paper's uniform prime-power proof.

## 5. Thirteen Lean declarations: corrected independent pass

The first supplied file did not compile independently: conjugation left a commuted product unresolved under the sum, a doc-comment/omit placement failed parsing, and the cellular inclusion theorem needed an explicit coefficient type. The author corrected all three. A fresh run in the existing pinned Lean4.24.0/mathlib4.24.0 environment with lake env lean -DwarningAsError=true on the latest ThetaJacobi.lean completed with exit 0. All thirteen printed types and dependencies were inspected; the final output has no sorryAx or new axioms, only standard Lean foundations.

The exact scope is four character statements (actual Jacobi conjugation, norm with all three nontrivialities explicit, shifted Jacobi rescaling and nontriviality of the cubic-quadratic product), five CM matrix/positivity statements (determinant, local polynomial, Gram identity, positive quadratic form and the two p=7 polynomials), and four cellular components (inclusion into cycles, homology restriction identity, 3-by-3 edge determinant and rational vertex/edge chain equation).

The Jacobi norm uses mathlib's finite-field Jacobi theorem with characteristic inequality justified by finite F versus characteristic-zero C; it does not assume the target norm as a hypothesis. The positive Gram theorem is a real quadratic inequality, not a packaged Matrix.PosDef declaration. The p=7 formal statement checks the two integral matrices after the character sum, rather than formally computing those finite-field characters. The file does not formalize the entire point-count proof, prime-power character existence, all chain-homotopy formulas, a Tate comparison, order Frobenius functor, global analytic continuation or GRH. Those limits match the actual types.

## 6. Remaining category and arithmetic scope

The revised paper explicitly takes the order-insertion examples over Lambda_Q and R_Q=Q[[u]]. This is essential: reducing M_d in characteristic p makes its determinant p vanish and is a different construction. The finite-Q determinant on a selected simple is P_d, but the simple has infinite projective dimension and is not fully deck-stable. On the regular order module the R determinant of the uniform external tensor operator is P_d^18, and on a basic projective it is P_d^6, because their R ranks are 18 and 6. The three-simple orbit gives P_d^3 for that same untwisted tensor action. These multiplicities are not automatically those of a genuinely semilinear deck operator.

The current paragraph does not claim that a scalar root supplies a determinant-line functor, that the rational chain lift is induced by geometric Frobenius on a complex cellulation, or that the finite-field positive form gives a global number-field spectrum. Those qualifications are mathematically necessary and correctly retained. The final global paragraph now fixes a rational model and asserts only the absolute convergence range Re(s)>3/2 supplied by the local bound, with distinct finite-field, elliptic global and Dirichlet centers. Bad primes, conductor/gamma data, order-derived compatibility and a determinant-preserving global positive realization remain outside the established result.

No full 200-declaration suite or PDF build was independently run here. The independent formal verification was exactly the corrected thirteen-statement module, and the focused exact checker was rerun after its authorized extension. No remaining blocking correction was found in the final literal formulas.

## 7. Final inert-prime extension: sixteen-statement independent pass

Follow-up, 2026-11-03. Read the added inert subsection in theta-jacobi-details.tex lines64–78, the new core line41 and explicit split-case qualifications at core23/details31. Read the three added Lean declarations and their proofs at ThetaJacobi.lean lines137–165. The latest file has 199 lines, the core 45 and details 87. A fresh independent compile of the updated module with -DwarningAsError=true completed with exit0 and all sixteen printed declarations using standard foundational dependencies. No older Python test suite was rerun in this follow-up, and no checker or shared source was changed.

The split scope is now explicit: the real rational CM/cellular construction above assumes q congruent 1 modulo 3. At q congruent 2 modulo 3, the q-power action conjugates the cubic deck transformation. With the fixed real matrix C, the required relation MC=C²M forces

    M=[[a,b],[a+b,-a]],
    det(M)=-a²-ab-b²
          =-(a²+b²+(a+b)²)/2 ≤ 0.

This is an exact obstruction to determinant q>0 on this **fixed real two-dimensional carrier**. It does not prohibit a two-dimensional representation over a different coefficient field, a complex realization, a larger real carrier or an infinite-dimensional height operator. In particular there is no contradiction with the ordinary two-dimensional ell-adic Frobenius representation: that coefficient field and its positivity properties differ from R. The core and details retain the appropriate limited conclusion.

For K=[[1,-1],[0,-1]], direct multiplication gives K²=I, KC=C²K and K^t G K=G. Thus on the complexification F=i sqrt(q) K indeed has trace0, determinant q, square -qI and Hermitian scaled-isometry identity F*GF=qG. Its complex characteristic factor is 1+qT², as required for that individual trace-zero local factor. On the underlying four-dimensional **real** space, its characteristic factor is the square (1+qT²)²; the paper correctly calls it a two-dimensional complex, four-dimensional real model and does not identify it with the excluded real two-plane.

The one-q qualification is essential and is now stated literally. Independently choosing i sqrt(q) K for each field does not define a Frobenius-power-compatible family. For example a choice at p has square -pI at p², not i p K. Even on odd-degree extensions, independently resetting the positive square root can lose the sign of the required power. A compatible family would start with one F_p and prove the comparison for its powers, with descent data for the actual base curve. The paper does not claim to have supplied that comparison or an integral/Tate/global positive determinant realization.

The three new formal statements have precisely these types: the three K matrix identities over a commutative ring; nonpositivity of the determinant of a real matrix satisfying MC=C²M; and impossibility of additionally having determinant q for q>0. They do **not** formalize the i sqrt(q) complex replacement, field-extension compatibility, the arithmetic reason for the conjugation relation, or a global cohomology theory. The preceding arithmetic/prose hypotheses remain load bearing. No new mathematical correction was found in this final subsection.
