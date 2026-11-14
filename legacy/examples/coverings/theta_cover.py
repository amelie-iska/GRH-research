#!/usr/bin/env python3
"""Exact finite-support calculations for a cover of an actual theta quotient.

Column matrices/covariant representations; opposite convention to the lecture's
right modules. No finite window is asserted to be the whole infinite cover.
"""
from pathlib import Path
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]


def band(m=3):
    x=S.zeros(3*m);y=S.zeros(3*m)
    xe=[edge for i in range(m) for edge in [(3*i+1,3*i),((3*i+3)%(3*m),3*i+2)]]
    ye=[(3*i+1,3*i+2) for i in range(m)]
    for i,j in xe:x[i,j]=1
    for i,j in ye:y[i,j]=1
    return x,y,[v for i in range(m) for v in [i,(i+1)%m,i]],xe,ye


def hom_basis(x,y,vertex,xx,yy,vvertex,source_grades=None,target_grades=None,degree=None):
    m,n=xx.rows,x.rows
    positions=[(i,j) for i in range(m) for j in range(n) if vvertex[i]==vertex[j]
               and (degree is None or target_grades[i]-source_grades[j]==degree)]
    if not positions:return []
    variables=S.symbols('f:'+str(len(positions)))
    f=S.zeros(m,n)
    for (i,j),v in zip(positions,variables):f[i,j]=v
    a,_=S.linear_eq_to_matrix(list(f*x-xx*f)+list(f*y-yy*f),variables)
    result=[]
    for v in a.nullspace():
        h=S.zeros(m,n)
        for (i,j),c in zip(positions,v):h[i,j]=c
        result.append(h)
    return result


def interval(start,length,simple_sum=False):
    x=S.zeros(length);y=S.zeros(length)
    if not simple_sum:
        for j in range(length-1):x[j+1,j]=1
    grades=list(range(start,start+length))
    return x,y,[g%3 for g in grades],grades


def matrix_unit(i,j):
    e=S.zeros(9);e[i,j]=1;return e


def main():
    x,y,vertex,xe,ye=band()
    assert x*y==y*x==S.zeros(9) and x**3==y**3==S.zeros(9)
    # All length-three words vanish, not only pure powers.
    for a in [x,y]:
        for b in [x,y]:
            for c in [x,y]:assert a*b*c==S.zeros(9)
    ends=hom_basis(x,y,vertex,x,y,vertex)
    rad=[matrix_unit(0,2)+matrix_unit(1,3),matrix_unit(1,5),
         matrix_unit(3,5)+matrix_unit(4,6),matrix_unit(4,8),
         matrix_unit(6,8)+matrix_unit(7,0),matrix_unit(7,2)]
    basis=[S.eye(9)]+rad
    assert len(ends)==7 and S.Matrix.hstack(*(m.reshape(81,1) for m in basis)).rank()==7
    for f in basis:assert f*x==x*f and f*y==y*f
    products={}
    for i,a in enumerate(rad):
        for j,b in enumerate(rad):
            p=a*b
            if p!=S.zeros(9):
                k=next(k for k,r in enumerate(rad) if p==r)
                products[f'r{i}r{j}']=f'r{k}'
            for c in rad:assert p*c==S.zeros(9)
    assert products=={'r0r2':'r1','r2r4':'r3','r4r0':'r5'}
    # Euler contradiction tested on completely arbitrary D, not just diagonal D.
    variables=S.symbols('d:81');d=S.Matrix(9,9,variables)
    constraints=list(d*x-x*d-x)+list(d*y-y*d-y)
    a,b=S.linear_eq_to_matrix(constraints,variables)
    assert a.rank()<a.row_join(b).rank()
    # The exact linear certificate telescopes for a symbolic arbitrary D.
    defect=sum((d*x-x*d)[i,j] for i,j in xe)-sum((d*y-y*d)[i,j] for i,j in ye)
    assert S.expand(defect)==0 and len(xe)-len(ye)==3
    checks=[]
    fixtures=[interval(-3,2),interval(0,3),interval(1,4),interval(0,5),interval(2,5),interval(0,5,True)]
    for source in fixtures:
        for target in fixtures:
            sx,sy,sv,sg=source;tx,ty,tv,tg=target
            maps=hom_basis(sx,sy,sv,tx,ty,tv)
            degrees=sorted({i-j for i in tg for j in sg if (i-j)%3==0})
            counts={}
            for degree in degrees:
                hs=hom_basis(sx,sy,sv,tx,ty,tv,sg,tg,degree)
                if hs:counts[str(degree//3)]=len(hs)
            assert sum(counts.values())==len(maps)
            for f in maps:
                reconstructed=S.zeros(f.rows,f.cols)
                for degree in degrees:
                    h=S.Matrix(f.rows,f.cols,lambda i,j:f[i,j] if tg[i]-sg[j]==degree else 0)
                    assert h*sx==tx*h and h*sy==ty*h
                    reconstructed+=h
                assert reconstructed==f
            checks.append(dict(source_grades=sg,target_grades=tg,hom_dimension=len(maps),
                               homogeneous_dimensions=counts))
    defects=[]
    for name,module in [('five_simples',interval(0,5,True)),('five_chain',interval(0,5))]:
        xx,yy,vv,gg=module
        down=len(hom_basis(xx,yy,vv,xx,yy,vv))
        up=len(hom_basis(xx,yy,vv,xx,yy,vv,gg,gg,0))
        defects.append(dict(module=name,cover_end=up,pushdown_end=down,defect=down-up))
    assert [d['defect'] for d in defects]==[4,1]
    higher=[]
    for m in [3,5,9,19]:
        xx,yy,vv,xe,ye=band(m)
        zero=S.zeros(3*m)
        assert xx*yy==yy*xx==xx**3==yy**3==zero
        # The Euler certificate cancels each individual diagonal coefficient.
        coefficients=[0]*(3*m)
        for sign,edges in [(1,xe),(-1,ye)]:
            for i,j in edges:coefficients[i]+=sign;coefficients[j]-=sign
        assert coefficients==[0]*(3*m) and len(xe)-len(ye)==m
        higher.append(dict(m=m,genus=(m-1)//2,dimension=3*m,euler_rhs=m,
                           mixed_and_cubic_zero=True,diagonal_coefficients=coefficients))
    out=dict(passed=True,conventions='columns; vertex residues mod3; deck shift +3; homogeneous degree=target_grade-source_grade',
        quotient='B_L=A/J^L of actual infinite elliptic theta algebra; examples use L=3 or5',
        source_dessin=dict(sigma=[[0,1,2],[3,4,5]],alpha=[[0,3],[1,4],[2,5]],genus=1),
        band=dict(X=[list(map(int,x.row(i))) for i in range(9)],Y=[list(map(int,y.row(i))) for i in range(9)],
                  vertex=vertex,end_dimension=7,radical_dimension=6,radical_cube_zero=True,
                  nonzero_radical_products=products,euler_obstruction='0=6-3=3; characteristic zero',
                  arbitrary_euler_system_ranks=[a.rank(),a.row_join(b).rank()]),
        hom_cases=checks,hom_control_counterexample=defects,higher_genus=higher,
        scope='Exact checks supplement general prose proofs; neither full AR classification, completed-order equivalence nor GRH')
    target=ROOT/'outputs/checks/2026-11-03-coverings/theta-cover.json'
    target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,indent=2)+'\n')
    web=ROOT/'web/data/theta-cover.json';web.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(passed=True,hom_pairs=len(checks),band_end_dimension=7,hom_control_defects=[4,1]),indent=2))


if __name__=='__main__':main()
