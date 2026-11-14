#!/usr/bin/env python3
"""Exact DG identities and actual dessin forbidden-word endpoints; no training."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'outputs/checks/2026-11-03-dg-foundations';OUT.mkdir(parents=True,exist_ok=True)

def theta(alpha):
    sigma=[1,2,0,4,5,3];tau=[sigma.index(i) for i in range(6)];phi=[alpha[tau[h]] for h in range(6)]
    edges=[];vertex={}
    for h in range(6):
        if h not in vertex:
            i=len(edges);edges.append([h,alpha[h]]);vertex[h]=vertex[alpha[h]]=i
    rows=[]
    for n in range(13):
        matrix=[[int(i==j) for j in range(3)] for i in range(3)] if n==0 else [[0]*3 for _ in range(3)]
        if n:
            for h in range(6):
                last=h
                for _ in range(n-1):last=phi[last]
                matrix[vertex[h]][vertex[tau[last]]]+=1
        rows.append(matrix)
    return dict(sigma=sigma,alpha=alpha,phi=phi,edges=edges,ext_dimensions=rows)

def main():
    a,b,c,d,f,xi,eta,q=s.symbols('a b c d f xi eta q',nonzero=True)
    p=s.Matrix([a,b]);v=s.Matrix([c,d]);D=s.Matrix([[0,f],[0,0]]);H=s.Matrix([[0,0],[1,0]])
    mul=lambda u,v:s.Matrix([u[0]*v[0],u[0]*v[1]+u[1]*v[0]])
    assert D*D==s.zeros(2) and D*H+H*D==f*s.eye(2)
    P0=s.diag(1,0);assert H*P0-P0*H==H  # inverse-arrow homotopy is not graded End(C)-linear
    assert s.simplify(D*mul(p,v)-mul(D*p,v)-mul(s.diag(1,-1)*p,D*v))==s.zeros(2,1)
    assert (xi*eta).subs({xi:q*xi,eta:eta/q},simultaneous=True)==xi*eta
    G=s.groebner([xi*eta],xi,eta)
    for i in range(8):
        for j in range(8):assert G.reduce(xi**i*eta**j)[1]==(xi**i*eta**j if i==0 or j==0 else 0)
    cases={'elliptic':theta([3,4,5,0,1,2]),'spherical':theta([3,5,4,0,2,1])}
    for name,case in cases.items():
        for n,M in enumerate(case['ext_dimensions']):
            for i in range(3):
                for j in range(3):
                    expected=int(i==j) if n==0 else (2*int(j==(i-n)%3) if name=='elliptic' else (2*int(i==j) if n%2==0 else int(i!=j)))
                    assert M[i][j]==expected
    result=dict(passed=True,symbolic_Leibniz_and_homotopy=True,normal_form_monomials=64,theta_cases=cases,scope='Exact symbolic/dart diagnostics; Ext identification uses the existing prose resolution; no categorical DG or arithmetic proof inferred',seed='none; deterministic symbolic and exhaustive finite checks')
    (OUT/'exact-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    web=ROOT/'web/data/dg';web.mkdir(exist_ok=True);(web/'theta.json').write_text(json.dumps(cases,indent=2)+'\n')
    print('DG exact identities,64 normal forms and234 endpoint dimensions passed')
if __name__=='__main__':main()
