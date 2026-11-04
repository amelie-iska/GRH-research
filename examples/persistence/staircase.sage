# Exact Sage companion. Supplied source; not executed on this machine because
# its existing Sage launcher has no target application. Do not install/upgrade.
R.<x,y> = PolynomialRing(QQ, 2)
for G in [[(2,0),(1,1),(0,2)], [(3,0),(2,1),(1,2),(0,3)],
          [(5,0),(3,1),(1,3),(0,5)], [(4,0),(3,2),(1,4),(0,6)]]:
    m = len(G)
    d1 = matrix(R, 1, m, [x^a*y^b for a,b in G])
    d2 = matrix(R, m, m-1)
    for i in range(m-1):
        d2[i,i] = -y^(G[i+1][1]-G[i][1])
        d2[i+1,i] = x^(G[i][0]-G[i+1][0])
    assert d1*d2 == zero_matrix(R, 1, m-1)
    for i in range(m):
        rows = [j for j in range(m) if j != i]
        assert d2.matrix_from_rows(rows).det() == (-1)^i*d1[0,i]
    basis = [(a,b) for a in range(G[0][0]) for b in range(G[-1][1])
             if not any(a>=c and b>=d for c,d in G)]
    print({'generators': G, 'length': len(basis), 'free_ranks_R': (1,m,m-1),
           'free_ranks_Lambda_xy_cone': (1,m+1,2*m-1,m-1)})
# Universal exactness is the induction in the book, not a matrix-product test.
