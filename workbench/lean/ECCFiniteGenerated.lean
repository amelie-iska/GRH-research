import Std
set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000
namespace ECCFiniteGenerated
def encodings : List Nat := [64, 17, 41, 18, 42, 27, 35, 20, 44, 29, 37, 30, 38]
def table : List (List Nat) := [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 11, 0, 8, 12, 9, 7, 4, 5, 10, 6, 3, 2], [2, 0, 12, 11, 7, 8, 10, 6, 3, 5, 9, 1, 4], [3, 8, 11, 9, 0, 6, 12, 2, 10, 7, 4, 5, 1], [4, 12, 7, 0, 10, 11, 5, 9, 1, 3, 8, 2, 6], [5, 9, 8, 6, 11, 4, 0, 1, 7, 12, 2, 10, 3], [6, 7, 10, 12, 5, 0, 3, 8, 2, 1, 11, 4, 9], [7, 4, 6, 2, 9, 1, 8, 5, 0, 11, 3, 12, 10], [8, 5, 3, 10, 1, 7, 2, 0, 6, 4, 12, 9, 11], [9, 10, 5, 7, 3, 12, 1, 11, 4, 2, 0, 6, 8], [10, 6, 9, 4, 8, 2, 11, 3, 12, 0, 1, 7, 5], [11, 3, 1, 5, 2, 10, 4, 12, 9, 6, 7, 8, 0], [12, 2, 4, 1, 6, 3, 9, 10, 11, 8, 5, 0, 7]]
def phi : List Nat := [0, 3, 4, 7, 8, 11, 12, 1, 2, 5, 6, 9, 10]
def decomposition : List (List Nat) := [[0, 0], [1, 0], [12, 1], [0, 1], [1, 1], [12, 2], [0, 2], [0, 11], [11, 12], [12, 12], [0, 12], [1, 12], [12, 0]]

def enc (i : Nat) : Nat := encodings.getD i 0
def add (i j : Nat) : Nat := (table.getD i []).getD j 0
def mul (k i : Nat) : Nat := (List.range k).foldl (fun a _ => add a i) 0
def onCurve (P : Nat) : Bool :=
 P == 64 || decide (P < 64 ∧ P % 8 < 7 ∧ P / 8 < 7 ∧
   (P/8)^2 % 7 = ((P%8)^3+3)%7)
def affineAdd (P Q : Nat) : Nat :=
 if P=64 then Q else if Q=64 then P else
 let x := P%8; let y := P/8; let u := Q%8; let v := Q/8
 if x=u ∧ (y+v)%7=0 then 64 else
 let numerator := if P=Q then 3*x*x else v+7-y
 let denominator := if P=Q then 2*y else u+7-x
 let slope := (numerator*(denominator%7)^5)%7
 let z := (slope*slope+14-x-u)%7
 let t := (slope*(x+7-z)+7-y)%7
 z+8*t

theorem valid_points : encodings.all onCurve = true := by decide

theorem exact_affine_table : (List.range 13).all (fun i =>
 (List.range 13).all (fun j => enc (add i j) == affineAdd (enc i) (enc j))) = true := by decide

theorem group_associativity : (List.range 13).all (fun i =>
 (List.range 13).all (fun j => (List.range 13).all (fun k =>
 add (add i j) k == add i (add j k)))) = true := by decide

theorem identity_and_inverse : (List.range 13).all (fun i =>
 (add 0 i == i) && (add i 0 == i) &&
 (List.range 13).any (fun j => (add i j == 0) && (add j i == 0))) = true := by decide

theorem endomorphism_homomorphism : (List.range 13).all (fun i =>
 (List.range 13).all (fun j =>
 phi.getD (add i j) 99 == add (phi.getD i 99) (phi.getD j 99))) = true := by decide

theorem decomposition_exact : (List.range 13).all (fun k =>
 let pair := decomposition.getD k []
 mul k 1 == add (mul (pair.getD 0 99) 1) (mul (pair.getD 1 99) (phi.getD 1 99))) = true := by decide

end ECCFiniteGenerated
#check ECCFiniteGenerated.valid_points
#print axioms ECCFiniteGenerated.valid_points
#check ECCFiniteGenerated.exact_affine_table
#print axioms ECCFiniteGenerated.exact_affine_table
#check ECCFiniteGenerated.group_associativity
#print axioms ECCFiniteGenerated.group_associativity
#check ECCFiniteGenerated.identity_and_inverse
#print axioms ECCFiniteGenerated.identity_and_inverse
#check ECCFiniteGenerated.endomorphism_homomorphism
#print axioms ECCFiniteGenerated.endomorphism_homomorphism
#check ECCFiniteGenerated.decomposition_exact
#print axioms ECCFiniteGenerated.decomposition_exact
