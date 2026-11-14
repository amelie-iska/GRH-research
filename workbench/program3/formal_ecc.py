"""Generate finite Lean certificates with an independent modular addition formula.

The generated tables are witnesses. Lean checks every listed valid point,
addition-table entry, group law and decomposition. This is a bounded field/curve
certificate, not a formal complexity theorem or an elliptic-curve theorem for
arbitrary parameters. Generated source is committed before release verification.
"""
import argparse
from pathlib import Path
from .ecc import Curve,decomposition


def generate():
 c=Curve();pts=c.points();words=[c.encode(p)for p in pts];index={p:i for i,p in enumerate(pts)};table=[[index[c.add(p,q)]for q in pts]for p in pts];G=pts[1];d=decomposition(c,G);phi=[index[c.phi(p,d['beta'])]for p in pts];pairs=[[a%13,b%13]for a,b in d['pairs']]
 source='''import Std
set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000
namespace ECCFiniteGenerated
'''
 source+=f'def encodings : List Nat := {words}\n'
 source+=f'def table : List (List Nat) := {table}\n'
 source+=f'def phi : List Nat := {phi}\n'
 source+=f'def decomposition : List (List Nat) := {pairs}\n'
 source+='''
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
'''
 for name in ['valid_points','exact_affine_table','group_associativity','identity_and_inverse','endomorphism_homomorphism','decomposition_exact']:
  source+=f'#check ECCFiniteGenerated.{name}\n#print axioms ECCFiniteGenerated.{name}\n'
 return source

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(generate());print(a.output)
