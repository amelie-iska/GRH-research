#!/usr/bin/env python3
"""Exact stdlib genus/ramification and polynomial identity diagnostics."""
from pathlib import Path
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parents[1]
def cycles(p):
    left=set(range(len(p)));out=[]
    while left:
        a=min(left);c=[]
        while a in left:left.remove(a);c.append(a);a=p[a]
        out.append(c)
    return out

def hyper(m):
    sigma=[(i+1)%m if i<m else m+(i-m+1)%m for i in range(2*m)]
    alpha=[(i+m)%(2*m) for i in range(2*m)]
    tau=[sigma.index(i) for i in range(2*m)];phi=[alpha[tau[i]] for i in range(2*m)]
    g=(2-len(cycles(sigma))+m-len(cycles(phi)))//2
    assert len(cycles(phi))==1 and g==(m-1)//2
    # Exact Riemann--Hurwitz: degree2m beta, ramification at0,1,infinity.
    assert 2*g-2 == -4*m+2*(m-1)+m+(2*m-1)
    arrows=[(i%m,tau[i]%m) for i in range(2*m)]
    assert all(arrows[i][1]==arrows[phi[i]][0] for i in range(2*m))
    return dict(m=m,genus=g,rank=2*m*m,sigma=cycles(sigma),alpha=cycles(alpha),faces=cycles(phi))
rows=[hyper(m) for m in [3,5,7,9,11,19,33]]
# Integer Pluecker check supplements (does not replace) the Lean polynomial proof.
from itertools import product
count=0
for a,b,c,d in product(range(-2,3),repeat=4):
    z=[[1,0,a,b],[0,1,c,d]]
    p=lambda i,j:z[0][i]*z[1][j]-z[0][j]*z[1][i]
    assert p(0,1)*p(2,3)-p(0,2)*p(1,3)+p(0,3)*p(1,2)==0
    count+=1
out=dict(higher_genus_dessins=rows,integer_pluecker_examples=count,scope='bounded exact diagnostics; universal proofs in book and selected Lean statements')
path=ROOT/'outputs/checks/2026-11-03-book/exact-examples.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':pass
