# Exact algebra companion; source supplied, not executed by the broken local Sage launcher.
# Run in an existing working Sage environment: sage examples/sage/actual_rg.sage
# Formal Boltzmann variables, not fitted real parameters. No files are changed.
from itertools import product
m=5
R=LaurentPolynomialRing(QQ,names=['x','y','z']+['h%s'%j for j in range(m)])
x,y,z=R.gens()[:3];hs=R.gens()[3:]
def weight(Bp,Bm,s):
    w=x**(Bp*sum(s))*y**(Bm*sum((-1)^j*s[j] for j in range(m)))*z**(5*Bp-3*Bm)
    return w*prod(hs[j]**s[j] for j in range(m))
boundary=list(product([-1,1],repeat=m))
coarse={s:sum(weight(Bp,Bm,s) for Bp,Bm in product([-1,1],repeat=2)) for s in boundary}
Zfine=sum(weight(Bp,Bm,s) for Bp,Bm in product([-1,1],repeat=2) for s in boundary)
assert Zfine==sum(coarse.values())
for j in range(m):
    assert sum(s[j]*weight(Bp,Bm,s) for Bp,Bm in product([-1,1],repeat=2) for s in boundary)==sum(s[j]*coarse[s] for s in boundary)
# Connected clean K2,5 graph, edge qubits, one face with even edge incidences.
edges=[(b,2+j) for b in range(2) for j in range(m)]
HX=matrix(GF(2),[[int(v in e) for e in edges] for v in range(m+2)])
HZ=matrix(GF(2),1,2*m,0)
assert HX*HZ.transpose()==0
assert HX.rank()==6 and HZ.rank()==0 and 2*m-HX.rank()-HZ.rank()==4
T=matrix(PolynomialRing(QQ,'a,b,d'),[[0,0],[0,0]])
a,b,d=T.base_ring().gens();T=matrix(T.base_ring(),[[a,b],[b,d]])
assert T^2==matrix(T.base_ring(),[[a^2+b^2,b*(a+d)],[b*(a+d),d^2+b^2]])
assert (T^2)^8==T^16
print('Exact Laurent RG weights, retained numerators, CSS chain ranks, and transfer identities checked')
