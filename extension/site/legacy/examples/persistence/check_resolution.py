#!/usr/bin/env python3
"""Exact symbolic diagnostics for the worked persistence chapter.

The ring k[x,y] is the auxiliary filtration parameter ring, not a replacement
for a primary infinite dessin algebra. Matrix identities with u² apply to
central coefficients; exactness over the actual order is proved in the book.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
def main():
 x,y,u,s,t=sp.symbols('x y u s t')
 d1=sp.Matrix([[x*x,x*y,y*y]])
 d2=sp.Matrix([[-y,0],[x,-y],[0,x]])
 assert d1*d2==sp.zeros(1,2)
 minors=[sp.expand(d2[list(ix),:].det()) for ix in combinations(range(3),2)]
 assert minors==[y*y,-x*y,x*x]
 D1=sp.Matrix.hstack(d1,sp.Matrix([[u*u]]))
 D2=sp.Matrix.vstack(sp.Matrix.hstack(d2,u*u*sp.eye(3)),sp.Matrix.hstack(sp.zeros(1,2),-d1))
 D3=sp.Matrix.vstack(u*u*sp.eye(2),-d2)
 assert D1.shape==(1,4) and D2.shape==(4,5) and D3.shape==(5,2)
 assert D1*D2==sp.zeros(1,5) and D2*D3==sp.zeros(4,2)
 numerator=1-s*s-s*t-t*t+s*s*t+s*t*t
 assert sp.expand((1+s+t)*(1-s)*(1-t)-numerator)==0
 table=[]
 for a in range(5):
  for b in range(5):
   disks=sum(a>=i and b>=j for i,j in [(2,0),(1,1),(0,2)])
   h1=int(disks==0);h2=max(disks-1,0)
   assert h1==int(a+b<2)
   assert h2==int(a>=2 and b>=1)+int(a>=1 and b>=2)
   table.append(dict(grade=[a,b],H1=h1,H2=h2,disks=disks))
 report=dict(d1d2_zero=True,maximal_minors=list(map(str,minors)),total_ranks=[1,4,5,2],total_complex_products_zero=True,hilbert_numerator=str(numerator),graded_CW_checks=table,scope='Exact symbolic/cell-count diagnostics; universal exactness and order regularity require the chapter proofs, not numerical ranks')
 (ROOT/'outputs/checks/2026-11-03-architecture/persistence-checks.json').write_text(json.dumps(report,indent=2)+'\n')
 print('Persistence: exact syzygies, minors, total complex, Hilbert numerator and25CWgrades passed')
if __name__=='__main__':main()
