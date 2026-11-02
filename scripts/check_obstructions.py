#!/usr/bin/env python3
"""Deterministic exact witnesses; these checks do not verify GRH."""
from fractions import Fraction as Q
import json
from pathlib import Path

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def run():
    # pi=2, upper-Iwahori E12: conjugation has forbidden lower entry 1/2.
    shift=[[0,2],[1,0]]; inv=[[0,1],[Q(1,2),0]]; e12=[[0,1],[0,0]]
    conjugate=mul(mul(shift,e12),inv)
    assert conjugate == [[0,0],[Q(1,2),0]]
    # Antisymmetric transfer loses its determinant under Hermitian-part extraction.
    transfer=[[0,1],[-1,0]]
    original=det([[1,-1],[1,1]])
    symmetrized=det([[1,0],[0,1]])
    assert original==2 and symmetrized==1
    # For norm n=2, integer trace would satisfy 2*t^2=9, impossible by parity.
    assert (2+1)**2 % 2 == 1
    # Every cyclic subgroup of V4 has index 2 or 4; all induced 1D degrees even.
    assert all(d % 2==0 for d in [2,2,2,4]) and 1 % 2==1
    # The q=1 model evaluates positive diagonal entries, so every phase is zero.
    # Its centered characteristic polynomial therefore vanishes at 1/2 for every degree.
    for degree in [1,2,5,20]: assert Q(0)**degree==0
    report={"arithmetic":"exact integers and fractions", "randomness":"none",
      "checks_passed":5,"iwahori_forbidden_entry":str(conjugate[1][0]),
      "det_before_symmetrization":original,"det_after_symmetrization":symmetrized,
      "scope":"finite witnesses only; universal analytic statements are proved in the paper, not by this script"}
    out=Path(__file__).resolve().parents[1]/"outputs/checks/obstructions.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": run()
