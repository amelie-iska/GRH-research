"""Independent exact oracle for the actual polynomial dessin branch extension.

No production imports, random samples, new packages or outside writes.
Polynomial matrices are sparse dictionaries; module arithmetic is exact.
"""
from fractions import Fraction
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
M=5

def add(A,B):
    out=A.copy()
    for k,v in B.items():
        out[k]=out.get(k,0)+v
        if not out[k]:del out[k]
    return out

def scale(c,A):return {k:c*v for k,v in A.items() if c*v}

def mul(A,B):
    out={}
    for (branch,i,j,n),x in A.items():
        for (branch2,j2,k,q),y in B.items():
            if branch==branch2 and j==j2:
                key=(branch,i,k,n+q);out[key]=out.get(key,0)+x*y
                if not out[key]:del out[key]
    return out

def arrow(branch,i):return {(branch,(i-1)%M,i,int(i==0)):1}
def idem(i):return {(b,i,i,0):1 for b in [0,1]}
I={k:v for i in range(M) for k,v in idem(i).items()}
ZERO={}

def path(branch,start,length):
    # Rightmost arrow acts first: path starts at start and travels down.
    value=idem(start)
    for j in range(length):value=mul(arrow(branch,(start-j)%M),value)
    return value

def scalar(c,p=0):return Fraction(c) if p==0 else c%p
def inv(c,p=0):return 1/c if p==0 else pow(c,-1,p)
def rref_rank(rows,p=0):
    if not rows:return 0
    A=[[scalar(c,p) for c in row] for row in rows]
    r=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        u=inv(A[r][j],p);A[r]=[scalar(u*x,p) for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                q=A[i][j];A[i]=[scalar(x-q*y,p) for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r

def evaluate(A,dual=False):
    n=M*(2 if dual else 1);B=[[0]*n for _ in range(n)]
    for (branch,i,j,q),c in A.items():
        if branch:continue
        if dual:
            if q==0:B[2*i][2*j]+=c;B[2*i+1][2*j+1]+=c
            elif q==1:B[2*i+1][2*j]+=c
        elif q==0:B[i][j]+=c
    return B

def mv(A,v):return [sum(a*x for a,x in zip(row,v)) for row in A]
def incl(v):return [z for x in v for z in [0,x]]
def proj(v):return v[::2]

def hom_rows(source,target):
    ns,nt=len(source[0]),len(target[0]);equations=[]
    for S,T in zip(source,target):
        for i in range(nt):
            for j in range(ns):
                row=[0]*(nt*ns)
                for k in range(nt):row[k*ns+j]+=T[i][k]
                for k in range(ns):row[i*ns+k]-=S[k][j]
                equations.append(row)
    return equations

def main():
    gens=[idem(i) for i in range(M)]+[arrow(b,i) for b in [0,1] for i in range(M)]
    generator_checks=0
    for i in range(M):
        assert mul(idem(i),idem(i))==idem(i)
        for j in range(M):
            if i!=j:assert mul(idem(i),idem(j))==ZERO
        for b in [0,1]:
            a=arrow(b,i)
            assert mul(idem((i-1)%M),a)==a==mul(a,idem(i))
            assert mul(arrow(1-b,(i-1)%M),a)==ZERO
            generator_checks+=3
    assert add(add(add(add(idem(0),idem(1)),idem(2)),idem(3)),idem(4))==I
    # Normal paths independently recover every permitted monomial entry and
    # cannot identify distinct branches or powers of t.
    signatures=set();normal=[]
    for b in [0,1]:
        for start in range(M):
            for length in range(1,41):
                P=path(b,start,length);end=(start-length)%M
                q=(length+end-start)//M
                assert P=={(b,end,start,q):1}
                assert (b,end,start,q) not in signatures
                signatures.add((b,end,start,q));normal.append(P)
    for A in normal:
        for (b,i,j,q),c in A.items():assert i<j or q>=1
    cycle=mul(mul(mul(mul(arrow(0,1),arrow(0,2)),arrow(0,3)),arrow(0,4)),arrow(0,0))
    assert cycle=={(0,0,0,1):1}
    # The sum of the actual full turns is t times the shared identity.
    u={}
    for b in [0,1]:
        for start in range(M):u=add(u,path(b,start,M))
    assert u=={(b,i,i,1):1 for b in [0,1] for i in range(M)}
    for a in gens:assert mul(u,a)==mul(a,u)
    # Whole polynomial elements, not just arrows: test module maps under
    # combinations containing both branches and powers up to t^8.
    polynomials=[]
    for r in range(20):
        A=scale(r-7,I)
        for j,P in enumerate(normal):
            c=((r+2)*(j+3))%7-3
            if c:A=add(A,scale(c,P))
        polynomials.append(A)
    module_checks=0
    for A in polynomials:
        C,D=evaluate(A),evaluate(A,True)
        for j in range(M):
            v=[int(i==j) for i in range(M)]
            assert mv(D,incl(v))==incl(mv(C,v))
            module_checks+=1
        for j in range(2*M):
            v=[int(i==j) for i in range(2*M)]
            assert proj(mv(D,v))==mv(C,proj(v))
            module_checks+=1
    G1=[evaluate(g) for g in gens];G2=[evaluate(g,True) for g in gens]
    h12=hom_rows(G1,G2);h11=hom_rows(G1,G1);h22=hom_rows(G2,G2)
    # Every putative section has pS=identity. These exact linear equations
    # contradict arrow compatibility over Q and in characteristics2,3,5.
    A=h12.copy();rhs=[0]*len(A)
    for i in range(M):
        for j in range(M):
            row=[0]*(2*M*M);row[(2*i)*M+j]=1
            A.append(row);rhs.append(int(i==j))
    ranks=[]
    for p in [0,2,3,5]:
        rank=rref_rank(A,p);aug=rref_rank([row+[b] for row,b in zip(A,rhs)],p)
        assert (rank,aug)==(49,50)
        assert M*M-rref_rank(h11,p)==1
        assert (2*M)**2-rref_rank(h22,p)==2
        assert 2*M*M-rref_rank(h12,p)==1
        ranks.append(dict(field='Q' if not p else f'F{p}',section_coefficient_rank=rank,augmented_rank=aug,
                          end_M1_dimension=1,end_M2_dimension=2,hom_M1_M2_dimension=1))
    report=dict(passed=True,generator_relation_checks=generator_checks,distinct_normal_paths=len(normal),
        max_path_length=40,whole_polynomial_module_map_checks=module_checks,fields=ranks,
        actual_cycle_image='(t E00,0)',central_parameter='(t I,t I)',
        scope='Independent finite exact oracle; infinite path-basis identification and nonsplitting proof reviewed in prose, not inferred solely from samples')
    (OUT/'oracle.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
