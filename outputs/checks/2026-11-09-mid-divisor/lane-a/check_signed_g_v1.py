from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import isqrt, prod
from pathlib import Path
import sys

NORMS=(7,7,13,13,19,31,37,43)
CONJUGATE={0:1,1:0,2:3,3:2}
LABELS=frozenset(range(len(NORMS)))
COUNTS=Counter()


def norm(label):
    return prod(NORMS[i] for i in label)


def mu(label):
    return (-1)**len(label)


def subsets(label):
    order=sorted(label)
    return (frozenset(p for p,flag in zip(order,bits) if flag)
            for bits in product((0,1),repeat=len(order)))


def direct_tests(U,D,E,R,J,nl,ns,Nl1,Nl2,Nm,Nn,index,p):
    z1,z2=(nl*Nl1,ns*Nl2) if index==0 else (ns*Nl1,nl*Nl2)
    z=z1*z2
    first_floor=F(U*p,Nm)
    second_floor=F(U,Nn)
    M=F(R*E*J,D)
    return (z1>first_floor and z2>second_floor and max(z1,z2)<=U
            and J<=z<2*J and F(D,E*J)>F(1,2) and F(D,E)>1
            and 1<z<=4*M and (nl>=ns if index==0 else nl>ns))


def shortened_tests(U,D,E,R,J,Nq,Nb,ns,Nl1,Nl2,Nm,Nn,index,p):
    if index==0:
        fixed_z=ns*Nl2
        factor=Nq*Nl1
        lower=F(U*p,Nm*factor)
        fixed_floor=F(U,Nn)
    else:
        fixed_z=ns*Nl1
        factor=Nq*Nl2
        lower=F(U,Nn*factor)
        fixed_floor=F(U*p,Nm)
    factor_product=fixed_z*factor
    M=F(R*E*J,D)
    return (fixed_floor<fixed_z<=U and lower<Nb<=F(U,factor)
            and F(J,factor_product)<=Nb<F(2*J,factor_product)
            and F(D,E*J)>F(1,2) and F(D,E)>1
            and F(1,factor_product)<Nb<=4*M/factor_product
            and (Nb>=F(ns,Nq) if index==0 else Nb>F(ns,Nq)))


def projector_checks():
    rows=(frozenset(),frozenset({1}),frozenset({2,4}),
          frozenset({0,5,6}),frozenset({1,3,7}))
    for U,(m,n),ell in product(
        (31,43,67,97,151),
        ((frozenset({2}),frozenset({4})),(frozenset({0}),frozenset({5})),
         (frozenset({4}),frozenset({7}))),
        (frozenset(),frozenset({0}),frozenset({1}),frozenset({3}),frozenset({6})),
    ):
        d=m|n
        if d&ell:
            continue
        E=norm(d)
        D=7*U**2//2
        R=U*isqrt(U)
        eligible=LABELS-d-ell
        for ell1 in subsets(ell):
            ell2=ell-ell1
            for gs in subsets(eligible):
                ns=norm(gs)
                if ns>U:
                    continue
                for gl in subsets(eligible-gs):
                    nl=norm(gl)
                    if nl>U:
                        continue
                    z=nl*ns*norm(ell)
                    J=2**(z.bit_length()-1)
                    for index,p in product(range(2),(1,*[NORMS[i] for i in m if NORMS[i] in (7,13)])):
                        actual=direct_tests(U,D,E,R,J,nl,ns,norm(ell1),norm(ell2),norm(m),norm(n),index,p)
                        for q in subsets(gl):
                            b=gl-q
                            assert not (q&b or q&(d|gs|ell) or b&(d|gs|ell))
                            assert mu(q)*mu(gl)==mu(b)
                            assert actual==shortened_tests(U,D,E,R,J,norm(q),norm(b),ns,norm(ell1),norm(ell2),norm(m),norm(n),index,p)
                            COUNTS["exact_longer_factor_interval_checks"]+=1
                        if not actual:
                            continue
                        COUNTS["actual_live_masked_coefficients"]+=1
                        if any(CONJUGATE.get(j) in gl for j in ell):
                            COUNTS["allowed_conjugate_overlap_witnesses"]+=1
                        for row in rows:
                            before=F(mu(gl),nl) if not gl&row else F(0)
                            after=sum((F(mu(gl-q),norm(q)*norm(gl-q))
                                       for q in subsets(gl&row)),F(0))
                            assert before==after
                            COUNTS["raw_row_projector_weighted_checks"]+=1
                            if gl&row:
                                COUNTS["nontrivial_zero_projector_checks"]+=1


def power_checks():
    for i,j in product(range(257),range(65)):
        e=F(17,74)+F(i,256)*(F(11,32)-F(17,74))
        t=F(j,64)*F(1,8)
        assert (1-e-t)/2>=F(17,64)
        assert (1-e-t)/2-F(3,16)>=F(5,64)
        assert F(3,32)-t/2>=F(1,32)
        assert F(3,8)+2*t<=F(3,4)
        COUNTS["signed_split_exponent_checks"]+=1
    assert F(3,4)+F(1,8)/2==F(13,16)
    for A in (18,145,1177):
        for n in range(1,2*A+1):
            exact=sum(n%r==0 for r in range(1,n+1))
            hyperbola=2*sum(n%r==0 for r in range(1,isqrt(2*A)+1))
            assert exact<=hyperbola
            COUNTS["integer_norm_fibre_hyperbola_checks"]+=1


def main():
    projector_checks()
    power_checks()
    for witness in ("allowed_conjugate_overlap_witnesses","nontrivial_zero_projector_checks"):
        assert COUNTS[witness]>0,witness
    note=Path(sys.argv[2])
    receipt={"status":"pass","scope":"Fresh exact signed longer-factor projector and Fraction arithmetic controls",
             "counts":dict(sorted(COUNTS.items())),
             "source_sha256":{str(path):sha256(path.read_bytes()).hexdigest()
                              for path in (Path(__file__),note)}}
    with Path(sys.argv[1]).open("x") as stream:
        stream.write(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(json.dumps(receipt["counts"],sort_keys=True))


if __name__=="__main__":
    main()

