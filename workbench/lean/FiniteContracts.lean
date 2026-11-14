import Std

/-!
Exact rational-pair computations for exported, bounded finite certificates.
Positive denominators are checked before cross multiplication. A certificate
proves these finite checks, not a floating-point implementation, exchangeability,
a continuum limit, a derived equivalence or a physical comparison inequality.
No native_decide, unsafe declarations, axioms or sorry are used.
-/
set_option autoImplicit false
set_option maxRecDepth 4096
set_option maxHeartbeats 2000000
namespace WorkbenchFinite
abbrev Q := Int × Int
def qzero : Q := (0, 1)
def qone : Q := (1, 1)
def qadd (a b : Q) : Q := (a.1*b.2+b.1*a.2, a.2*b.2)
def qmul (a b : Q) : Q := (a.1*b.1, a.2*b.2)
def qdiv (a b : Q) : Q := (a.1*b.2, a.2*b.1)
def qpow (a : Q) : Nat → Q
  | 0 => qone
  | n+1 => qmul (qpow a n) a
def qsum (xs : List Q) : Q := xs.foldl qadd qzero
def qprod (xs : List Q) : Q := xs.foldl qmul qone
def qle (a b : Q) : Bool := decide (0 < a.2 ∧ 0 < b.2 ∧ a.1*b.2 ≤ b.1*a.2)
def qlt (a b : Q) : Bool := decide (0 < a.2 ∧ 0 < b.2 ∧ a.1*b.2 < b.1*a.2)
def qeq (a b : Q) : Bool := decide (0 < a.2 ∧ 0 < b.2 ∧ a.1*b.2 = b.1*a.2)
def probability (a : Q) : Bool := qle qzero a && qle a qone
def heatValid (r : Q) : Bool := qle qzero r && qle (qmul (4,1) r) qone

def gainValid (g : List (List Q)) (w : List Q) (q : Q) : Bool :=
  decide (0 < w.length ∧ w.length ≤ 12 ∧ g.length = w.length) &&
  g.all (fun row => decide (row.length = w.length) && row.all (qle qzero)) &&
  w.all (qlt qzero) && qle qzero q && qlt q qone &&
  (List.range w.length).all (fun i =>
    qle (qsum (((g.getD i []).zip w).map (fun p => qmul p.1 p.2)))
        (qmul q (w.getD i qzero)))

def rankValid (draws exceedances : Nat) (p resolution : Q) : Bool :=
  decide (0 < draws ∧ exceedances ≤ draws) &&
  qeq p (Int.ofNat (exceedances+1), Int.ofNat (draws+1)) &&
  qeq resolution (1, Int.ofNat (draws+1))

def riskValid (tests : Nat) (tail drift alpha total : Q) : Bool :=
  decide (0 < tests) && probability tail && probability drift && probability alpha &&
  qeq total (qadd (qmul (Int.ofNat tests,1) tail) drift) && qle total alpha

def entry (b : List (List Int)) (i j : Nat) : Int := (b.getD i []).getD j 0
def shape (b : List (List Int)) : Bool :=
  decide (0 < b.length ∧ b.length ≤ 12) && b.all (fun row => decide (row.length=b.length))
def skew (b : List (List Int)) : Bool :=
  (List.range b.length).all (fun i => (List.range b.length).all
    (fun j => decide (entry b i j = -entry b j i)))
def mutation (b : List (List Int)) (k : Nat) : List (List Int) :=
  (List.range b.length).map (fun i => (List.range b.length).map (fun j =>
    if i=k ∨ j=k then -entry b i j else entry b i j +
      max (entry b i k) 0 * max (entry b k j) 0 -
      max (-entry b i k) 0 * max (-entry b k j) 0))
def seedMutation (b : List (List Int)) (x : List Q) (k : Nat) : List Q :=
  let a := qprod ((List.range b.length).map (fun i =>
    qpow (x.getD i qzero) (max (entry b i k) 0).toNat))
  let c := qprod ((List.range b.length).map (fun i =>
    qpow (x.getD i qzero) (max (-entry b i k) 0).toNat))
  (List.range b.length).map (fun i => if i=k then qdiv (qadd a c) (x.getD i qzero)
    else x.getD i qzero)
def mutationValid (b : List (List Int)) (x : List Q) (k : Nat)
    (out : List (List Int)) (y : List Q) : Bool :=
  shape b && skew b && decide (k < b.length ∧ x.length=b.length ∧ y.length=b.length) &&
  x.all (qlt qzero) && y.all (qlt qzero) &&
  decide (mutation b k = out) &&
  ((seedMutation b x k).zip y).all (fun p => qeq p.1 p.2)
end WorkbenchFinite
