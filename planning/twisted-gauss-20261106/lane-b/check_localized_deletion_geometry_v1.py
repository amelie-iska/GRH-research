from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,datetime

ROOT=Path(__file__).resolve().parents[3]
NOTE=ROOT/"planning/twisted-gauss-20261106/lane-b/LOCALIZED_FULL_DELETION_SHARP_TRANSFER-v1.md"
OUT=ROOT/"outputs/checks/2026-11-06-twisted-gauss/lane-b/geometry-v1"
OUT.mkdir(parents=True,exist_ok=True)
RESULT=OUT/"checks-v1.json"
assert not RESULT.exists(), "Immutable result exists: do not rerun."
rows=[]
for p,r,d,k,s,h_end in product((F(0),F(1,8)),(F(0),F(1,8)),(F(0),F(1,32)),(F(0),F(1,32)),(F(0),F(1,16)),(0,1)):
    h=F(0) if not h_end else r+s
    level=p+d+k+h
    inner=F(1)-p-d-h
    product_power=F(1)+k
    margin=level-product_power/2
    # These affine checks imply all intervening real exponent boxes too.
    assert h<=r+s
    assert inner>=F(21,32)
    assert level<=F(3,8)
    assert margin<=-F(9,64)
    assert level+inner==product_power
    # Original left 1/sqrt(p h u), with u at its actual radial scale.
    assert -(p+h+inner)/2==(d-F(1))/2
    # The right trivial sqrt(D/d) cancels that left square-root scaling.
    assert (d-F(1))/2+(F(1)-d)/2==0
    rows.append({z:str(v) for z,v in {
       "p":p,"r":r,"d":d,"k":k,"s":s,"h":h,
       "physical_level":level,"inner_length":inner,
       "product":product_power,"level_minus_half_product":margin}.items()})
out={
"schema":"twisted-gauss-localized-full-deletion-geometry-v1",
"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"passed":True,
"new_exact_Fraction_affine_vertex_cases":len(rows),
"maximum_physical_level_power":str(max(F(z["physical_level"]) for z in rows)),
"minimum_inner_length_power":str(min(F(z["inner_length"]) for z in rows)),
"maximum_level_minus_half_product":str(max(F(z["level_minus_half_product"]) for z in rows)),
"material_parameters":{"p_and_r_max":"1/8","common_d_max":"1/32","original_k_max":"1/32","s_max":"1/16","h_max":"r+s","constants":"Fixed factors 128 and V's 1/2 handled in note, not asymptotic exponents.","randomness":"none"},
"rows":rows,
"note":{"path":str(NOTE.relative_to(ROOT)),"sha256":hashlib.sha256(NOTE.read_bytes()).hexdigest()},
"producer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
"scope":"NEW synthetic exact affine parameter and normalization controls for whole-prefix-localized full deletion only. Not actual Eisenstein ideal/character/Gauss samples or proof of missing finite-twist input. No accepted old Laurent/Mobius/exponent fixture rerun.",
"conditional_input_proved":False,
"whole_signed_or_GRH_gain":False}
RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({"result":str(RESULT.relative_to(ROOT)),"sha256":hashlib.sha256(RESULT.read_bytes()).hexdigest(),"cases":len(rows),"passed":True}))
