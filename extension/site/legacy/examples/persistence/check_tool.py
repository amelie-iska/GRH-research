#!/usr/bin/env python3
"""Independent symbolic and row-elimination checks of the discrete tool.

Uses the approved CPU environment. Does not re-train or modify source data.
Exactness for the entire polynomial module is the book's proof; these are
independent symbolic/finite diagnostics, not a replacement proof or Lean.
"""
from pathlib import Path
from itertools import combinations
import hashlib,json,subprocess
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'outputs/checks/2026-11-03-persistence-tools';OUT.mkdir(parents=True,exist_ok=True)

def reduce_rows(matrix,ncols):
    a=[list(r) for r in matrix];piv=[];i=0
    for j in range(ncols):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        for k in range(len(a)):
            if k!=i and a[k][j]:a[k]=[v^w for v,w in zip(a[k],a[i])]
        piv.append(j);i+=1
    return a,piv

def rank(a,n):return len(reduce_rows(a,n)[1])
def nullspace(a,n):
    rows,piv=reduce_rows(a,n);out=[]
    for j in range(n):
        if j in piv:continue
        v=[0]*n;v[j]=1
        for i,p in enumerate(piv):v[p]=rows[i][j]
        out.append(v)
    return out

def complex_at(d,channel,r,e):
    verts=[p['id'] for p in d['points'] if p['birth']<=e]
    edges=[v for v in combinations(verts,2) if d[channel+'_labels'][v[0]][v[1]]<=r]
    triangles=[v for v in combinations(verts,3) if all(edge in edges for edge in combinations(v,2))]
    d1=[[int(v in edge) for edge in edges] for v in verts]
    d2=[[int(set(edge)<=set(face)) for face in triangles] for edge in edges]
    assert all(sum(d1[i][k]*d2[k][j] for k in range(len(edges)))%2==0 for i in range(len(verts)) for j in range(len(triangles)))
    return dict(v=verts,e=edges,t=triangles,d1=d1,d2=d2,betti=[len(verts)-rank(d1,len(edges)),len(edges)-rank(d1,len(edges))-rank(d2,len(triangles))])

def inclusion(a,b):
    assert set(a['v'])<=set(b['v']) and set(a['e'])<=set(b['e']) and set(a['t'])<=set(b['t'])
    z=nullspace(a['d1'],len(a['e']))
    embedded=[[v[a['e'].index(edge)] if edge in a['e'] else 0 for edge in b['e']] for v in z]
    aug=[row+[v[i] for v in embedded] for i,row in enumerate(b['d2'])]
    h1=rank(aug,len(b['t'])+len(z))-rank(b['d2'],len(b['t']))
    h0=rank([row+[int(v==sv) for sv in a['v']] for v,row in zip(b['v'],b['d1'])],len(b['e'])+len(a['v']))-rank(b['d1'],len(b['e']))
    return dict(h0=h0,h1=h1)

def main():
    x,y,u,s,t=sp.symbols('x y u s t');algebra=[]
    for gens in [[(1,0),(0,1)],[(2,0),(1,1),(0,2)],[(3,0),(2,1),(1,2),(0,3)],[(5,0),(3,1),(1,3),(0,5)],[(4,0),(3,2),(1,4),(0,6)]]:
        m=len(gens);d1=sp.Matrix([[x**a*y**b for a,b in gens]]);d2=sp.zeros(m,m-1)
        for i in range(m-1):d2[i,i]=-y**(gens[i+1][1]-gens[i][1]);d2[i+1,i]=x**(gens[i][0]-gens[i+1][0])
        assert d1*d2==sp.zeros(1,m-1)
        for i in range(m):assert sp.expand(d2[[j for j in range(m) if j!=i],:].det()-(-1)**i*d1[i])==0
        basis=[(a,b) for a in range(gens[0][0]) for b in range(gens[-1][1]) if not any(a>=i and b>=j for i,j in gens)]
        num=1-sum(s**a*t**b for a,b in gens)+sum(s**gens[i][0]*t**gens[i+1][1] for i in range(m-1))
        assert sp.expand(sum(s**a*t**b for a,b in basis)*(1-s)*(1-t)-num)==0
        D1=d1.row_join(sp.Matrix([[u**2]]));D2=d2.row_join(u**2*sp.eye(m)).col_join(sp.zeros(1,m-1).row_join(-d1));D3=(u**2*sp.eye(m-1)).col_join(-d2)
        assert D1*D2==sp.zeros(1,2*m-1) and D2*D3==sp.zeros(m+1,m-1)
        algebra.append(dict(gens=gens,length=len(basis),cone_ranks=[1,m+1,2*m-1,m-1]))
    X=sp.Matrix([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,1,1,0]])
    U=sp.Matrix([[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]]);Y=U-X
    assert X*Y==Y*X==U*U==sp.zeros(4) and X*X==U*X
    folder=ROOT/'web/data/persistence';manifest=json.loads((folder/'manifest.json').read_text());body=(folder/manifest['file']).read_bytes();assert hashlib.sha256(body).hexdigest()==manifest['sha256'];d=json.loads(body)
    p=d['provenance'];assert hashlib.sha256((ROOT/p['checkpoint']).read_bytes()).hexdigest()==p['checkpoint_sha256'];assert hashlib.sha256((ROOT/'examples/persistence/export_quantum_bifiltration.py').read_bytes()).hexdigest()==p['generator_sha256']
    assert hashlib.sha256((ROOT/p['channel_implementation']).read_bytes()).hexdigest()==p['channel_implementation_sha256']
    states=[np.array([complex(*v) for v in state]) for state in d['input_amplitudes']]
    for i,a in enumerate(states):
        for j,b in enumerate(states):
            exact=np.sqrt(max(0,1-abs(np.vdot(a,b))**2)) if i!=j else 0
            assert abs(exact-d['numerical_input_distances'][i][j])<3e-8
            assert d['output_labels'][i][j]<=d['input_labels'][i][j]
    # Independent row-matrix implementation vs browser's BigInt columns.
    js="""import {readFileSync} from 'node:fs';import{flagComplex,inclusionRanks}from './web/persistence-model.mjs';const m=JSON.parse(readFileSync('web/data/persistence/manifest.json')),d=JSON.parse(readFileSync('web/data/persistence/'+m.file)),out=[];for(const c of ['input','output'])for(const r of [0,383,400,600,800,1000])for(const e of [0,500,1000]){const a=flagComplex(d,c,r,e),b=flagComplex(d,c,1000,1000);out.push({c,r,e,betti:a.betti,ranks:inclusionRanks(a,b),channel:inclusionRanks(flagComplex(d,'input',r,e),flagComplex(d,'output',r,e))});}console.log(JSON.stringify(out));"""
    cases=json.loads(subprocess.check_output(['node','--input-type=module','-e',js],cwd=ROOT))
    for case in cases:
        c,r,e=case['c'],case['r'],case['e'];a=complex_at(d,c,r,e);b=complex_at(d,c,1000,1000)
        assert a['betti']==case['betti'] and inclusion(a,b)==case['ranks']
        assert inclusion(complex_at(d,'input',r,e),complex_at(d,'output',r,e))==case['channel']
    result=dict(passed=True,symbolic_staircases=algebra,independent_GF2_cases=len(cases),frozen_record_sha256=manifest['sha256'],checkpoint_unchanged=True,actual_node_actions=True,scope='Symbolic identities and finite checks, not universal Lean exactness or GRH')
    (OUT/'independent.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
