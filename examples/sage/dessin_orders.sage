# SageMath source. Exact, reproducible characteristic-zero calculations.
# Run: sage examples/sage/dessin_orders.sage
# No environment install, download or file mutation occurs here.
def odd_hyperelliptic_dessin(m):
    assert m >= 3 and m % 2 == 1
    H = list(range(2*m))
    sigma = [(i+1)%m if i<m else m+(i-m+1)%m for i in H]
    alpha = [(i+m)%(2*m) for i in H]
    inv = [sigma.index(i) for i in H]
    phi = [alpha[inv[i]] for i in H]
    def cycles(p):
        left=set(H); out=[]
        while left:
            a=min(left);c=[]
            while a in left:
                left.remove(a);c.append(a);a=p[a]
            out.append(c)
        return out
    faces=cycles(phi);g=(2-len(cycles(sigma))+m-len(faces))//2
    assert len(faces)==1 and g==(m-1)//2
    # Quiver: paired darts are vertices; every arrow advances sigma^-1.
    arrows=[(i%m,inv[i]%m) for i in H]
    for i in H: assert arrows[i][1]==arrows[phi[i]][0]
    return dict(m=m,genus=g,rank=2*m*m,sigma=cycles(sigma),alpha=cycles(alpha),faces=faces,arrows=arrows,relations=[(i,phi[i]) for i in H])

for m in [3,5,7,9,11,19,33]:print(odd_hyperelliptic_dessin(m))
R.<a,b,u,T> = PolynomialRing(QQ)
F=matrix(R,[[a,-b],[0,a+u*b]])
assert (identity_matrix(R,2)-T*F).det()==(1-T*a)*(1-T*(a+u*b))
P=PolynomialRing(QQ,8,'z');z=P.gens()
minor=lambda i,j:z[i]*z[4+j]-z[j]*z[4+i]
assert minor(0,1)*minor(2,3)-minor(0,2)*minor(1,3)+minor(0,3)*minor(1,2)==0
K.<w> = CyclotomicField(3)
U=diagonal_matrix(K,[1,w,w^2]);V=matrix(K,[[0,0,1],[1,0,0],[0,1,0]])
assert U*V==w*V*U
assert V^3==identity_matrix(K,3)
print('Sage exact determinant, Pluecker and qutrit identities passed')
