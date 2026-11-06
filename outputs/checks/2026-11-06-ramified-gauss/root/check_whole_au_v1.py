#!/usr/bin/env python3
"""Fresh formal whole-factor classification and exact budget controls.
No original Gauss/energy/annular data, training, numerical fit, or Lean."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
R=Path(__file__).resolve().parents[4]
OUT=Path(__file__).parent/"whole-au-controls-v1"
OUT.mkdir(exist_ok=True)
def compositions(total,n):
    if n==1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a,n-1):yield (a,)+tail
def classify(a):
    total=sum(a); lo=(total+2)//3;hi=2*total//3
    reachable=1
    for v in a:reachable|=reachable<<v
    balanced=any((reachable>>v)&1 for v in range(lo,hi+1))
    long=[i for i,v in enumerate(a) if 3*v>2*total]
    assert balanced != bool(long)
    if long:
        assert len(long)==1 and sum(a)-a[long[0]]<F(total,3)
        return "I",long[0]
    middle=[i for i,v in enumerate(a) if total<=3*v<=2*total]
    if middle:return "II",middle[0]
    s=0
    for v in a:
        s+=v
        if 3*s>=total:
            assert 3*s<=2*total
            return "II",s
    raise AssertionError("Missing partition")
rows=[];counts={"all_compositions":0,"admitted_typed":0,"I":0,"II":0,"j1":0,"unit_factors":0}
for j in range(1,6):
    own={"j":j,"factors":2*j+1,"all":0,"admitted":0,"I":0,"II":0}
    for a in compositions(12,2*j+1):
        own["all"]+=1;counts["all_compositions"]+=1
        kind,index=classify(a)
        # Original a,b and the j short-mu factors are all <=sqrtD.
        # This is weaker than the actual short-mu cutoff, so includes it.
        if any(v>6 for v in a[:2+j]):continue
        own["admitted"]+=1;counts["admitted_typed"]+=1
        own[kind]+=1;counts[kind]+=1
        counts["unit_factors"]+=a.count(0)
        if kind=="I":assert index>=2+j
        if j==1:
            assert kind=="II";counts["j1"]+=1
    rows.append(own)
z=F(2,9)
exponents={
 "z":z,"large_column":F(1,2)-z/2,
 "small_column":F(1,4)+F(5,8)*z,
 "balanced_column":F(1,3),
 "deletion_prefix":-F(1,2)-F(1,4)+F(3,8),
 "deletion_h":-F(1,2)-F(1,4)+F(3,8),
 "wrong_prefix_without_original_weight":-F(1,4)+F(3,8),
 "k_majorant":-2+F(3,8),
 "A1V":F(3,4)+F(1,16),
 "normalized":F(13,16)-F(1,9),
 "margin":F(3,4)-(F(13,16)-F(1,9)),
 "balanced_normalized":F(13,16)-F(1,6),
 "Lambda":F(3,4)+F(3,8)-2,
 "Bessel_normalized":F(13,16)+F(3,4)+F(3,8)-2,
 "equal_norm":F(13,16)-1,
}
assert exponents["large_column"]==exponents["small_column"]==F(7,18)
assert exponents["deletion_prefix"]==exponents["deletion_h"]==-F(3,8)
assert exponents["wrong_prefix_without_original_weight"]==F(1,8)
assert exponents["normalized"]==F(101,144) and exponents["margin"]==F(7,144)
assert exponents["k_majorant"]==-F(13,8)
# Exact powered dyadic-constant controls, no floating logs:
# Pbox^(2/3)>sqrtD follows D>2^44. D>=2^64 is safe.
assert 2**64>2**44
# D^(2/3)/2^(22/3) > (2D)^(1/5) follows D^7>2^113.
assert (2**64)**7>2**113
result={"schema":"ramified-whole-au-fresh-controls-v1","passed":True,
 "material":{"grid_total":12,"j":list(range(1,6)),"factor_count":"2j+1","norm_constants_threshold":"D>=2^64",
 "enumeration":"all labelled nonnegative integer compositions; zero is a literal unit-scale factor",
 "typed_cut":"a,b and every short-mu scale <=1/2 of total; includes the actual stronger short-mu bound",
 "randomness":False,"actual_arithmetic_energy_data":False,"old_controls_rerun":False},
 "counts":counts,"per_j":rows,"exact_fraction_budgets":{k:str(v) for k,v in exponents.items()},
 "negative_controls":["omitting the original prefix1/sqrtNp changes -3/8 to+1/8",
 "arbitrary finite-valued/growing-conductor phase is NOT the fixed finite-kappa theorem",
 "101/144 is only the declared pure finite primitive-dual top prefix"],
 "producer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "proof":{"path":"planning/ramified-gauss-20261106/root/FULL_AU_PURE_PREFIX-v1.md",
 "sha256":hashlib.sha256((R/"planning/ramified-gauss-20261106/root/FULL_AU_PURE_PREFIX-v1.md").read_bytes()).hexdigest()}}
p=OUT/"checks-v1.json";assert not p.exists();p.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"path":str(p.relative_to(R)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"counts":counts,"exponents":result["exact_fraction_budgets"]}))
