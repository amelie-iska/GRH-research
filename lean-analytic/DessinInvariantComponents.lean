import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace GRHResearch.DessinInvariants
open Matrix

/-- The CK1 initial-projection relation kills a forbidden successor. -/
theorem ck1_forbidden_successor {R : Type*} [Ring R] (a b ghost : R)
    (hsource : (ghost*a)*b=b) (hforbid : a*b=0) : b=0 := by
  calc
    b=(ghost*a)*b := hsource.symm
    _=ghost*(a*b) := mul_assoc _ _ _
    _=0 := by rw [hforbid,mul_zero]

/-- Closed dessin forbidden-successor permutations kill all arrows under CK1. -/
theorem closed_ck1_arrows_zero {R H : Type*} [Ring R] (f : H ≃ H)
    (a ghost : H → R)
    (hsource : ∀h,(ghost h*a h)*a (f h)=a (f h))
    (hforbid : ∀h,a h*a (f h)=0) : ∀h,a h=0 := by
  intro h
  have hz:=ck1_forbidden_successor (a (f.symm h)) (a (f (f.symm h)))
    (ghost (f.symm h)) (hsource (f.symm h)) (hforbid (f.symm h))
  simpa using hz

/-- Incoming edges cover every dessin vertex, so CK1 also kills every vertex. -/
theorem closed_ck1_vertices_zero {R H V : Type*} [Ring R] (t : H → V)
    (ht : Function.Surjective t) (a ghost : H → R) (p : V → R)
    (ha : ∀h,a h=0) (hCK1 : ∀h,ghost h*a h=p (t h)) : ∀v,p v=0 := by
  intro v
  obtain ⟨h,rfl⟩:=ht v
  rw [← hCK1 h,ha h,mul_zero]

/-- Determinantal semi-invariant change of bases, in cleared form. -/
theorem determinant_change_of_bases {R ι : Type*} [CommRing R]
    [Fintype ι] [DecidableEq ι] (D G₀ G₁ W₀ : Matrix ι ι R)
    (h : G₀*W₀=1) :
    (G₁*D*W₀).det*G₀.det=G₁.det*D.det := by
  have hd : G₀.det*W₀.det=1 := by rw [← Matrix.det_mul,h,Matrix.det_one]
  rw [Matrix.det_mul,Matrix.det_mul]
  calc
    G₁.det*D.det*W₀.det*G₀.det = G₁.det*D.det*(G₀.det*W₀.det) := by ring
    _=G₁.det*D.det := by rw [hd,mul_one]

variable {R : Type*} [CommRing R]

/-- The actual symmetric-square matrix in basis e1²,e1e2,e2². -/
def symSquare (M : Matrix (Fin 2) (Fin 2) R) : Matrix (Fin 3) (Fin 3) R :=
  !![M 0 0^2, M 0 0*M 0 1, M 0 1^2;
     2*M 0 0*M 1 0, M 0 0*M 1 1+M 0 1*M 1 0, 2*M 0 1*M 1 1;
     M 1 0^2, M 1 0*M 1 1, M 1 1^2]

theorem sym_square_zero : symSquare (0 : Matrix (Fin 2) (Fin 2) R)=0 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [symSquare]

theorem sym_square_one : symSquare (1 : Matrix (Fin 2) (Fin 2) R)=1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [symSquare]

theorem sym_square_composition (M N : Matrix (Fin 2) (Fin 2) R) :
    symSquare (M*N)=symSquare M*symSquare N := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [symSquare,Matrix.mul_apply,Fin.sum_univ_two,Fin.sum_univ_three] <;> ring

/-- Positive-degree Schur functors preserve the actual monomial zero relation. -/
theorem sym_square_preserves_relation (M N : Matrix (Fin 2) (Fin 2) R)
    (h : M*N=0) : symSquare M*symSquare N=0 := by
  rw [← sym_square_composition,h,sym_square_zero]

/-- The character identity V tensor V=Sym²(V) plus exterior²(V). -/
theorem schur_two_character (M : Matrix (Fin 2) (Fin 2) R) :
    M.trace^2=(symSquare M).trace+M.det := by
  simp [Matrix.trace,Fin.sum_univ_two,Fin.sum_univ_three,symSquare,Matrix.det_fin_two]
  ring

/-- The same Schur operation does not preserve the fixed central DVR action on a node lattice. -/
theorem schur_node_parameter_failure (u : R) (hu : u≠0) :
    symSquare (!![u,0;0,0] : Matrix (Fin 2) (Fin 2) R)+
      symSquare (!![0,0;0,u] : Matrix (Fin 2) (Fin 2) R) ≠
        u • (1 : Matrix (Fin 3) (Fin 3) R) := by
  intro h
  have he:=congrArg (fun M : Matrix (Fin 3) (Fin 3) R => M 1 1) h
  simp [symSquare] at he
  exact hu he.symm

#check ck1_forbidden_successor
#check closed_ck1_arrows_zero
#check closed_ck1_vertices_zero
#check determinant_change_of_bases
#check sym_square_zero
#check sym_square_one
#check sym_square_composition
#check sym_square_preserves_relation
#check schur_two_character
#check schur_node_parameter_failure
#print axioms ck1_forbidden_successor
#print axioms closed_ck1_arrows_zero
#print axioms closed_ck1_vertices_zero
#print axioms determinant_change_of_bases
#print axioms sym_square_zero
#print axioms sym_square_one
#print axioms sym_square_composition
#print axioms sym_square_preserves_relation
#print axioms schur_two_character
#print axioms schur_node_parameter_failure
end GRHResearch.DessinInvariants
