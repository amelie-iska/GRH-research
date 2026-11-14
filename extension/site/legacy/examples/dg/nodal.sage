# Sage source companion; supplied unexecuted. Existing launcher target is absent.
# Actual infinite nodal quotient; R is its ambient polynomial ring.
R.<xi,eta> = PolynomialRing(QQ, 2)
f = xi*eta
D = matrix(R, [[0,f],[0,0]])
H = matrix(R, [[0,0],[1,0]])
assert D*D == zero_matrix(R,2)
assert D*H+H*D == f*identity_matrix(R,2)
A = R.quotient(R.ideal(f), names=('xibar','etabar'))
assert A(xi)*A(eta) == 0
assert A(xi^7) != 0 and A(eta^7) != 0
print(A)
print('Koszul homotopy verified; quotient remains infinite dimensional')
# Full graded/category/continuous/A-infinity interfaces are separate tasks.
