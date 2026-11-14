# Exact Sage counterpart for the nine-dimensional theta-quotient carrier.
# Supplied source only: Sage is not runnable on the current host.
# Columns, covariant quiver representations, vertex labels below.
vertex = [0,1,0,1,2,1,2,0,2]
X = matrix(QQ,9,9)
Y = matrix(QQ,9,9)
xe = [(1,0),(3,2),(4,3),(6,5),(7,6),(0,8)]
ye = [(1,2),(4,5),(7,8)]
for i,j in xe:
    X[i,j] = 1
for i,j in ye:
    Y[i,j] = 1
assert X*Y == Y*X == X^3 == Y^3 == zero_matrix(QQ,9,9)
assert X.rank() == 6 and Y.rank() == 3
# The commutator's displayed entries depend only on these diagonal differences.
defect = vector(ZZ,9)
for sign,edges in [(1,xe),(-1,ye)]:
    for i,j in edges:
        defect[i] += sign
        defect[j] -= sign
assert defect == zero_vector(ZZ,9) and len(xe)-len(ye) == 3
print('Euler obstruction: 0 = 3; valid in characteristic zero.')
