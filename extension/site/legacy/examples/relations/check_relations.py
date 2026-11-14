#!/usr/bin/env python3
"""Exact rational checks on modules of actual infinite dessin algebras.

No random data or dependencies are installed. Outputs are finite diagnostics,
separate from the general proofs and kernel-checked relation statements.
"""
from pathlib import Path
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'outputs/checks/2026-11-03-linear-relations'

def jordan(lam,n):
    return s.Matrix(
        n,n,lambda i,j:lam if i==j else int(i==j+1))

def module(m,T):
    d=T.rows
    return [T if i==0 else s.eye(d) for i in range(m)], [s.zeros(d) for _ in range(m)]

def transport(m,T):
    d=T.rows;L=s.zeros(m*d);a,_=module(m,T)
    for i in range(m):
        L[((i-1)%m)*d:((i-1)%m+1)*d,i*d:(i+1)*d]=a[i]
    return L

def hom_dimension(T,U,m=None):
    r,q=T.rows,U.rows
    count=1 if m is None else m
    variables=s.symbols('h:'+str(count*r*q))
    hs=[s.Matrix(q,r,variables[i*q*r:(i+1)*q*r]) for i in range(count)]
    if m is None: eq=list(hs[0]*T-U*hs[0])
    else:
        aa,_=module(m,T);bb,_=module(m,U);eq=[]
        for i in range(m):eq+=list(hs[(i-1)%m]*aa[i]-bb[i]*hs[i])
    mat,_=s.linear_eq_to_matrix(eq,variables)
    return len(variables)-mat.rank()

def filtration(T):
    n=T.rows;ks=[n-(T**r).rank() for r in range(n+2)]
    return dict(kernel_dimensions=ks,image_dimensions=[n-k for k in ks],
        nilpotent_blocks={str(r):2*ks[r]-ks[r-1]-ks[r+1] for r in range(1,n+1)
                          if 2*ks[r]-ks[r-1]-ks[r+1]})

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    f=jordan(0,3);g=f.T
    assert s.Matrix.vstack(s.eye(3),f).rank()==3
    assert s.Matrix.vstack(s.eye(3),f*f).rank()==3
    assert s.Matrix.vstack(s.eye(3),g*f*f).rank()==3
    assert (g*f).nullspace()==[s.eye(3)[:,2]]
    assert (f*g).nullspace()==[s.eye(3)[:,0]]
    cases=[];z=s.Symbol('z')
    for m in [5,9]:
        sigma=list(range(1,m))+[0]+list(range(m+1,2*m))+[m]
        alpha=[(i+m)%(2*m) for i in range(2*m)]
        inv=[sigma.index(i) for i in range(2*m)]
        phi=[alpha[inv[i]] for i in range(2*m)]
        def cycles(p):
            seen=set();out=[]
            for i in range(len(p)):
                if i in seen:continue
                c=[];j=i
                while j not in seen:seen.add(j);c.append(j);j=p[j]
                out.append(c)
            return out
        assert len(cycles(phi))==1
        genus=(m-1)//2
        assert 2-len(cycles(sigma))-len(cycles(alpha))-len(cycles(phi))+2*m==2*genus
        for lam,n in [(0,1),(0,3),(1,2),(2,2)]:
            T=jordan(lam,n);a,b=module(m,T);L=transport(m,T)
            for i in range(m):
                assert b[(i-1)%m]*a[i]==s.zeros(n)
                assert a[(i-1)%m]*b[i]==s.zeros(n)
            assert L**m==s.diag(*([T]*m))
            for zz in [-2,-1,0,1,2]:
                assert (s.eye(m*n)-zz*L).det()==(s.eye(n)-zz**m*T).det()
            if m==5 and n<=2:
                assert s.expand((s.eye(m*n)-z*L).det()-(s.eye(n)-z**m*T).det())==0
            # Every letter has precisely two legal next letters, with formal
            # inverses, cancellation and inverse forbidden pairs all retained.
            letters=[(branch,i,sign) for branch in [0,1] for i in range(m) for sign in [-1,1]]
            def endpoints(letter):
                _,i,sign=letter;return (i,(i-1)%m) if sign==1 else ((i-1)%m,i)
            for x in letters:
                legal=[]
                for y in letters:
                    if endpoints(x)[1]!=endpoints(y)[0]:continue
                    if x[:2]==y[:2] and x[2]==-y[2]:continue
                    if x[2]==y[2] and x[0]!=y[0]:continue
                    legal.append(y)
                assert len(legal)==2
            cases.append(dict(m=m,genus=genus,lam=lam,size=n,filtration=filtration(T)))
    hom=[]
    for m in [5,9]:
        for lam,mu,r,q in [(0,0,1,2),(0,0,2,3),(1,1,2,3),(0,1,2,2),(1,2,1,2)]:
            T,U=jordan(lam,r),jordan(mu,q)
            expected=min(r,q) if lam==mu else 0
            assert hom_dimension(T,U)==expected
            assert hom_dimension(T,U,m)==expected
            hom.append(dict(m=m,lam=lam,mu=mu,r=r,s=q,dimension=expected))
    # A mixed finite endomorphism and the full stable direct sum.
    mixed=s.diag(jordan(0,3),jordan(0,1),jordan(1,2))
    N=mixed.rows;K=s.Matrix.hstack(*(mixed**N).nullspace())
    I=s.Matrix.hstack(*(mixed**N).columnspace())
    assert K.cols==4 and I.cols==2 and K.row_join(I).det()!=0
    assert filtration(mixed)['nilpotent_blocks']=={'1':1,'3':1}
    # The nonsplit ambient-A extension of the length-(m-1) string.
    T=jordan(0,2);inc=s.Matrix([0,1]);proj=s.Matrix([[1,0]])
    assert T*inc==s.zeros(2,1) and proj*T==s.zeros(1,2)
    x,y=s.symbols('x y');lift=s.Matrix([x,y])
    assert s.solve(list(T*lift)+[*(proj*lift-s.ones(1))],[x,y])==[]
    report=dict(passed=True,arithmetic='exact rational/integer SymPy',cases=cases,
        hom=hom,mixed_fitting=filtration(mixed),source_graph_ranks=[3,3,3],
        source_kernel_gf=[0,0,1],source_kernel_fg=[1,0,0],
        nonsplit_string_extension=True,two_successors_per_letter=True,
        limitations='Finite diagnostics; general relation/category/determinant proofs are in the article. No GRH or full formal category result.')
    (OUT/'exact.json').write_text(json.dumps(report,indent=2)+'\n')
    target=ROOT/'web/data/relations.json';target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(passed=True,module_cases=len(cases),hom_cases=len(hom),
        source_corrections=True,dessin_genera=[2,4],nonsplit_string_extension=True),indent=2))

if __name__=='__main__':main()
