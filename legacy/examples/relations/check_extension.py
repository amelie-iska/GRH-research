#!/usr/bin/env python3
"""Exact whole-polynomial path actions for the genuine genus-two algebra.

Paths and polynomial degrees are unbounded definitions; finite diagnostics
corroborate the general Lean module identities and independent prose proof.
No installation, random input or source-data mutation is performed.
"""
from pathlib import Path
from collections import defaultdict
import argparse,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
M=5

def path(branch,length,start):
    assert length>=0 and 0<=start<M
    return (0 if length==0 else branch,length,start)

def compose(left,right):
    b,l,j=left;c,r,k=right
    if (k-r)%M!=j:return None
    if l and r and b!=c:return None
    return path(b if l else c,l+r,k)

def add(A,B):
    C=defaultdict(int,A)
    for key,v in B.items():C[key]+=v
    return {k:v for k,v in C.items() if v}

def mul(A,B):
    C=defaultdict(int)
    for x,a in A.items():
        for y,b in B.items():
            if (z:=compose(x,y)) is not None:C[z]+=a*b
    return {k:v for k,v in C.items() if v}

def image(A):
    C=defaultdict(int)
    for (branch,length,start),v in A.items():
        if length==0:
            for b in (1,2):C[b,start,start,0]+=v
        else:
            end=(start-length)%M;degree=(length-start+end)//M
            assert degree>=0 and length==start-end+M*degree
            C[branch,end,start,degree]+=v
    return {k:v for k,v in C.items() if v}

def polynomial_mul(A,B):
    C=defaultdict(int)
    for (branch,i,j,d),a in A.items():
        for (other,k,l,e),b in B.items():
            if branch==other and j==k:C[branch,i,l,d+e]+=a*b
    return {k:v for k,v in C.items() if v}

def matrices(A):
    C0=s.zeros(M);C1=s.zeros(M)
    for (branch,i,j,d),a in image(A).items():
        if branch==1 and d==0:C0[i,j]+=a
        if branch==1 and d==1:C1[i,j]+=a
    return C0,s.BlockMatrix([[C0,s.zeros(M)],[C1,C0]]).as_explicit()

def rank_mod(A,p):
    B=[[int(v)%p for v in row] for row in A.tolist()];r=0
    for j in range(A.cols):
        pivot=next((i for i in range(r,len(B)) if B[i][j]),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r];inv=pow(B[r][j],-1,p)
        B[r]=[(v*inv)%p for v in B[r]]
        for i in range(r+1,len(B)):
            v=B[i][j]
            if v:B[i]=[(a-v*b)%p for a,b in zip(B[i],B[r])]
        r+=1
        if r==len(B):break
    return r

def check():
    unit={path(0,0,i):1 for i in range(M)}
    gens=[{path(0,0,i):1} for i in range(M)]+[
        {path(b,1,i):1} for b in [1,2] for i in range(M)]
    basis=[path(0,0,i) for i in range(M)]+[
        path(b,l,i) for b in [1,2] for l in range(1,41) for i in range(M)]
    assert len({tuple(sorted(image({p:1}).items())) for p in basis})==len(basis)
    small=[p for p in basis if p[1]<=8];pairs=0
    for x in small:
        for y in small:
            assert image(mul({x:1},{y:1}))==polynomial_mul(image({x:1}),image({y:1}))
            pairs+=1
    loop=gens[6]
    for i in [7,8,9,5]:loop=mul(loop,gens[i])
    assert image(loop)=={(1,0,0,1):1}
    for i in range(1,31):
        assert image({path(1,5*i,0):1})=={(1,0,0,i):1}
    inc=s.zeros(2*M,M);proj=s.zeros(M,2*M)
    for i in range(M):inc[M+i,i]=1;proj[i,i]=1
    assert inc.rank()==M and proj.rank()==M and proj*inc==s.zeros(M)
    assert s.Matrix.hstack(*proj.nullspace()).columnspace()==inc.columnspace()
    elements=[]
    for r in range(80):
        A=unit.copy()
        for j in range(7):
            p=basis[(17*r+53*j)%len(basis)];A=add(A,{p:(r+2*j)%7-3})
        elements.append(A)
    max_degree=0
    for r,A in enumerate(elements):
        B=elements[(r*7+11)%len(elements)]
        assert image(mul(A,B))==polynomial_mul(image(A),image(B))
        C0,C2=matrices(A);D0,D2=matrices(B);E0,E2=matrices(mul(A,B))
        assert E0==C0*D0 and E2==C2*D2
        assert C2*inc==inc*C0 and proj*C2==C0*proj
        max_degree=max(max_degree,max(d for _,_,_,d in image(A)))
    assert max_degree>=8
    # All generator equations for a genuine module section, not just one
    # eigenvalue equation. Coordinate order is all re entries, then all im.
    unknowns=s.symbols('z:50');S=s.Matrix(2*M,M,unknowns);eq=[]
    for g in gens:
        C0,C2=matrices(g);eq+=list(C2*S-S*C0)
    eq+=list(proj*S-s.eye(M));C,y=s.linear_eq_to_matrix(eq,unknowns)
    aug=C.row_join(y);fields=[]
    for label,p in [('Q',None),('F2',2),('F3',3),('F5',5)]:
        r=C.rank() if p is None else rank_mod(C,p)
        q=aug.rank() if p is None else rank_mod(aug,p)
        assert r==49 and q==50
        fields.append(dict(field=label,coefficient_rank=r,augmented_rank=q,no_section=True))
    return dict(passed=True,algebra='Actual unbounded polynomial two-branch path algebra realization for m5/genus2',
        normal_paths_checked=len(basis),path_product_pairs=pairs,
        whole_polynomial_elements=len(elements),maximum_sampled_degree=max_degree,
        all_element_module_maps=True,exact_dimensions=[5,10,5],
        fields=fields,coordinate_order='re0..re4,im0..im4',
        loop_image='(t E00,0); all positive powers remain nonzero',
        scope='Finite exact diagnostics, not an infinite classification or GRH certificate. General A-module exactness and no-section are separately Lean checked.')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,
        default=ROOT/'outputs/checks/2026-11-03-branch-extension/exact.json');args=parser.parse_args()
    result=check();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
