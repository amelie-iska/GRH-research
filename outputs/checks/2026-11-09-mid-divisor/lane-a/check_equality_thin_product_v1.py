from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import prod
from pathlib import Path
import sys

NORMS=(7,7,13,13,19,31)
LABELS=frozenset(range(len(NORMS)))
COUNTS=Counter()


def norm(label):
    return prod(NORMS[i] for i in label)


def subsets(label):
    order=sorted(label)
    return (frozenset(i for i,flag in zip(order,bits) if flag)
            for bits in product((0,1),repeat=len(order)))


def actual_strip_checks():
    for U,m,n,ell in product((37,61,83,91,97,127),
                             (frozenset({0}),frozenset({2})),
                             (frozenset({1}),frozenset({4})),
                             (frozenset(),frozenset({3}),frozenset({5}))):
        if m&n or (m|n)&ell:
            continue
        E=norm(m)*norm(n)
        eligible=LABELS-m-n-ell
        labels=tuple(subsets(eligible))
        for ell1 in subsets(ell):
            ell2=ell-ell1
            G1,G2=F(U,norm(m)*norm(ell1)),F(U,norm(n)*norm(ell2))
            pairs=[(a,b) for a,b in product(labels,repeat=2)
                   if not a&b and norm(a)*norm(ell1)<=U and norm(b)*norm(ell2)<=U]
            widths={F(1,7),F(1,3),F(1,2),F(1)}
            widths.update(F(E*norm(ell)*norm(a)*norm(b),U**2)-1 for a,b in pairs
                          if U**2<E*norm(ell)*norm(a)*norm(b)<=2*U**2)
            for eta in widths:
                direct=[]
                for a,b in pairs:
                    x,y=norm(a),norm(b)
                    omega=F(E*norm(ell)*x*y,U**2)
                    if omega==1:
                        COUNTS["strict_wide_lower_endpoint_controls"]+=1
                    if G1<x and G2<y and 1<omega<=1+eta:
                        assert G1<x<=(1+eta)*G1 and G2<y<=(1+eta)*G2
                        assert omega<7
                        direct.append((a,b))
                        if omega==1+eta:
                            COUNTS["weak_wide_upper_endpoint_controls"]+=1
                        if a!=b and x==y and a and b:
                            COUNTS["equal_norm_distinct_g_factors"]+=1
                for G in (G1,G2):
                    fibres=Counter(norm(a) for a in labels if G<norm(a)<=(1+eta)*G)
                    if fibres:
                        upper=((1+eta)*G).numerator//((1+eta)*G).denominator
                        lower=G.numerator//G.denominator
                        assert len(fibres)<=upper-lower<=1+eta*G
                        assert sum(F(c,n) for n,c in fibres.items())<=max(fibres.values())*(eta+1/G)
                        COUNTS["exact_weighted_norm_fibre_bounds"]+=1
                if direct:
                    COUNTS["live_ordered_equality_strip_cells"]+=1


def threshold(e):
    partner=max(F(3,4)-e,1-2*e,F(23,24)-4*e/3,F(13,12)-11*e/6)
    return max(F(0),partner-F(1,2)-8*max(F(0),F(1,4)-e))


def exponent_checks():
    for i,j in product(range(257),range(65)):
        e=F(17,74)+F(i,256)*(F(11,32)-F(17,74))
        t=F(j,64)*F(1,8)
        lower=F(1,2)-e-t
        theta=threshold(e)
        assert lower>=F(1,32)>=theta/4
        for width_exponent in (F(1,32),theta/4):
            individual=min(width_exponent,lower)
            assert 4*individual>=theta
            COUNTS["two_factor_squared_gain_controls"]+=1


def main():
    actual_strip_checks()
    exponent_checks()
    for witness in ("strict_wide_lower_endpoint_controls","weak_wide_upper_endpoint_controls",
                    "live_ordered_equality_strip_cells","equal_norm_distinct_g_factors"):
        assert COUNTS[witness]>0,witness
    note=Path(sys.argv[2])
    receipt={"status":"pass","scope":"Fresh exact equality-side thin support, distinct norm fibres, endpoints and paired exponent controls",
             "counts":dict(sorted(COUNTS.items())),
             "source_sha256":{str(path):sha256(path.read_bytes()).hexdigest()
                              for path in (Path(__file__),note)}}
    with Path(sys.argv[1]).open("x") as stream:
        stream.write(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(json.dumps(receipt["counts"],sort_keys=True))


if __name__=="__main__":
    main()

