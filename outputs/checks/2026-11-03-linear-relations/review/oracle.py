"""Independent exact reviewer oracle. No project code or mutable outputs imported."""
from pathlib import Path
import json,hashlib
import sympy as s
OUT=Path(__file__).resolve().parent

def jordan(r,lam):
    return s.diag(*([lam]*r))+s.Matrix(r,r,lambda i,j:int(i==j+1))

f=jordan(3,0);g=f.T
source=[]
for name,T in [('f',f),('g',g),('f2',f*f),('gf2',g*f*f),('gf',g*f),('fg',f*g)]:
    n=T.rows
    graph=s.eye(n).col_join(T)
    source.append(dict(name=name,graph_dimension=graph.rank(),operator_rank=T.rank(),stable_kernel_basis=[list(v) for v in (T**n).nullspace()],stable_image_basis=[list(v) for v in (T**n).columnspace()]))
    assert graph.rank()==3
assert (g*f).nullspace()==[s.Matrix([0,0,1])]
assert (f*g).nullspace()==[s.Matrix([1,0,0])]

checks=[];z=s.Symbol('z')
for m in [5,9]:
    for r in range(1,5):
        for lam in [0,1,2]:
            T=jordan(r,lam)
            arrows=[T]+[s.eye(r)]*(m-1)
            L=s.zeros(m*r)
            for i,A in enumerate(arrows):
                j=(i-1)%m;L[j*r:(j+1)*r,i*r:(i+1)*r]=A
            assert L**m==s.diag(*([T]*m))
            # charpoly avoids an expensive symbolic rational Schur complement.
            cp=L.charpoly(z).as_expr()
            expected=(z**m-lam)**r
            assert s.expand(cp-expected)==0
            checks.append(dict(m=m,r=r,lam=lam,charpoly=str(expected),central_turn_exact=True))

hom=[]
for r in range(1,6):
 for q in range(1,6):
  for lam,mu in [(0,0),(1,1),(2,2),(0,1),(1,2)]:
   T=jordan(r,lam);S=jordan(q,mu)
   # vec(H) uses column-major ordering.
   equations=s.kronecker_product(s.eye(r),S)-s.kronecker_product(T.T,s.eye(q))
   dimension=r*q-equations.rank()
   assert dimension==(min(r,q) if lam==mu else 0)
   hom.append(dict(r=r,q=q,lam=lam,mu=mu,dimension=dimension))

T=s.diag(jordan(3,0),jordan(2,2));N=T.rows
K=(T**N).nullspace();I=(T**N).columnspace()
assert len(K)==3 and len(I)==2 and s.Matrix.hstack(*(K+I)).rank()==N
filtration=[len((T**r).nullspace()) for r in range(N+2)]
block_counts=[2*filtration[r]-filtration[r-1]-filtration[r+1] for r in range(1,N+1)]
assert block_counts==[0,0,1,0,0]
J=jordan(2,0);Q=s.Matrix([[1,0]])
equations=J.col_join(Q);rhs=s.Matrix([0,0,1])
assert equations.rank()<equations.row_join(rhs).rank()

report=dict(passed=True,source_examples=source,transport_cases=checks,hom_cases=hom,
 fitting=dict(stable_kernel_dimension=len(K),stable_image_dimension=len(I),nilpotent_block_counts=block_counts),
 nonrigid_string_extension_has_no_section=True,
 source_pdf_sha256=hashlib.sha256(Path('research/literature/pullback-extension-20261103/1308.6410v2.pdf').read_bytes()).hexdigest(),
 scope='Exact finite algebra oracle; no general classification, topology formalization or GRH conclusion')
(OUT/'oracle.json').write_text(json.dumps(report,indent=2,default=lambda x:int(x))+'\n')
print('PASS:',len(checks),'exact transport/characteristic cases;',len(hom),'Hom cases; full source graphs; Fitting; nonsplit string extension')
