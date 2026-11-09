"""Exact arithmetic controls for the isolated good-sixth-free smooth candidate."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from json import dump
from math import prod
from pathlib import Path

pins={
    "planning/mid-divisor-20261109/lane-b/SMOOTH_GOOD_SIXTH_FREE-v1.md":"bb9940b105af9a9c49d56d736f7a0ad7525304853337b8e742f8d3f4b2301d7d",
    "planning/mid-divisor-20261109/lane-b/SMOOTH_RADIAL_PARTNER-v1.md":"7e71ef83c62acd3f7fdbc4906e69ee88e9afa300ba2015012271359cb2555145",
    "planning/joint-unit-pair-20261109/FREQUENCY_RATIONAL_CONTENT-v2.md":"e22b7235595e07ecc71d24a0f71242193b4d779559f8f33c70df8a53361c162a",
}
for path,want in pins.items():
    assert sha256(Path(path).read_bytes()).hexdigest()==want,path

def norm(values):
    return prod(p**e for p,e in zip((7,7,13),values))

cutoffs=(1,7,13,48,49,91,637)
projector_count=0
nonzero_large_remainders=0
for good in product(range(16),repeat=3):
    base=tuple(exponent//6 for exponent in good)
    factors=list(product(*(range(min(1,exponent)+1) for exponent in base)))
    signs={q:(-1)**sum(q) for q in factors}
    d=prod(e+1 for e in base)
    target=int(not any(base))
    assert sum(signs.values())==target
    for bad_exponent,cut in product((0,1,6,7),cutoffs):
        # A fixed S valuation has no role in the good sixth-power base.
        k=(*good,bad_exponent)
        small=sum(sign for q,sign in signs.items() if norm(q)<=cut)
        remainder=sum(sign for q,sign in signs.items() if norm(q)>cut)
        assert target==small+remainder and abs(small)<=d and abs(remainder)<=d
        assert not remainder or norm(tuple(exponent//6 for exponent in k[:3]))>cut
        projector_count+=1
        nonzero_large_remainders+=int(bool(remainder))
assert nonzero_large_remainders

# Sixth roots in the exact basis (1, epsilon) with epsilon^2=epsilon-1.
roots=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def mu6(label,point):
    phase=0
    for (p,w),power in zip(((7,2),(7,4),(13,3)),label):
        if not power:
            continue
        v=(point[0]+point[1]*w)%p
        if not v:
            return None
        powers={pow(1+w,j,p):j for j in range(6)}
        phase+=power*powers[pow(v,(p-1)//6,p)]
    return phase%6
def times(a,b): return None if a is None or b is None else (a+b)%6
def vector(phase): return (0,0) if phase is None else roots[phase]
def dot_add(values):
    a=b=F(0)
    for coef,phase in values:
        x,y=vector(phase)
        a+=coef*x
        b+=coef*y
    return a,b

long=[(label,F((-1)**sum(label),norm(label))) for label in product(range(2),repeat=3) if label not in ((0,0,0),(1,1,1))]
inverse=[(label,F((sum(label)%5)-2,norm(label))) for label in product(range(4),repeat=3)]
grouped={}
for (left,a),(right,b) in product(long,inverse):
    pair=tuple(x+y for x,y in zip(left,right))
    grouped[pair]=grouped.get(pair,F(0))+a*b
pair_checks=0
raw_zeros=0
for point in product(range(9),repeat=2):
    for (left,a),(right,b) in product(long,inverse):
        pair=tuple(x+y for x,y in zip(left,right))
        original=times(mu6(left,point),mu6(right,point))
        assert original==mu6(pair,point)
        pair_checks+=1
        raw_zeros+=int(original is None)
    direct=dot_add((a*b,times(mu6(left,point),mu6(right,point))) for (left,a),(right,b) in product(long,inverse))
    rewritten=dot_add((weight,mu6(label,point)) for label,weight in grouped.items())
    assert direct==rewritten
assert raw_zeros

def d6(x):
    return max(F(0),x-F(3,4),x/3-F(1,8),5*x/6-F(1,2))
scale_count=0
for i,j,g in product(range(65),range(49),range(13)):
    l=F(i,128)
    v=F(j,128)
    radial=F(g,16)
    gain=d6(l+v)-d6(l)
    max_gain=d6(F(1,2)+v)-d6(F(1,2))
    assert gain<=max_gain<=v/2
    relative=(d6(l+v+radial)-d6(l)-v-radial)/2
    assert relative<=-v/4
    scale_count+=1

out=Path("outputs/checks/2026-11-09-mid-divisor/lane-b/smooth-good-sixth-free-controls-v1.json")
receipt={
    "status":"pass_author_controls_candidate_pending_review",
    "source_hashes":pins,
    "exact_projector_cells":projector_count,
    "nonzero_large_remainders":nonzero_large_remainders,
    "exact_raw_product_pairs":pair_checks,
    "raw_zero_pairs":raw_zeros,
    "grouped_row_checks":81,
    "exact_scale_checks":scale_count,
    "scope":"Exact controls with distinct conjugate-prime labels over 7, S valuations frozen in the sixth-free selector, nonunique raw inverse-cutoff products, and Fraction exponent checks. The finite values corroborate the candidate and are not a run of the actual full row family."
}
with out.open("x") as handle:
    dump(receipt,handle,indent=2,sort_keys=True)
    handle.write("\n")
print({k:v for k,v in receipt.items() if k not in ("source_hashes","scope")})
print(sha256(out.read_bytes()).hexdigest(),out)

