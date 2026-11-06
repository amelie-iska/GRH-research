#!/usr/bin/env python3
"""Fresh exact exponent/control checks only; not actual Gauss/character data."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"outputs/checks/2026-11-06-twisted-gauss/lane-c/convexity-controls-v1"
OUT.mkdir(parents=True,exist_ok=True)
counts={"balanced_height_cases":0,"horizontal_strip_cases":0,"trivial_fallback_cases":0}
for a in [Q(1,2),Q(3,2)]:
    for it in range(17):
        tau=Q(it,8)
        for ir in range(17):
            rho=Q(ir,8)
            target=(tau+a*rho)/4
            if tau>=a*rho:
                h=(tau-a*rho)/4
                assert h>=0
                assert a*rho/2+h==target
                assert tau/2-h==target
                assert a*rho+2*h-tau<=0
                counts["balanced_height_cases"]+=1
                for js in range(9):
                    sigma=Q(1,2)+Q(js,16)
                    horizontal=sigma*tau+a*(1-sigma)*rho+2*(1-sigma)*h-h-tau/2
                    assert horizontal<=target
                    counts["horizontal_strip_cases"]+=1
            else:
                assert tau/2<=target
                counts["trivial_fallback_cases"]+=1
cases={}
alpha=Q(3,4)
for name,beta in [("coarse",Q(3,8)),("refined",Q(1,8))]:
    deletion=beta-alpha
    dsum=beta-alpha-1
    ksum=beta-2
    assert deletion<0 and dsum<-1 and ksum<-1
    prefix=1+beta-alpha
    assert prefix>0
    normalized=Q(13,16)+alpha-1+prefix/8
    assert normalized== -Q(1,16)+7*alpha/8+beta/8
    assert normalized==Q(19,32)+beta/8
    assert normalized<Q(3,4)
    cases[name]={"alpha":str(alpha),"beta":str(beta),"deletion_power":str(deletion),
                 "d_series_power":str(dsum),"k_series_power":str(ksum),
                 "prefix_sum_power":str(prefix),"normalized_D_power":str(normalized),
                 "target_margin":str(Q(3,4)-normalized)}
assert cases["coarse"]["normalized_D_power"]=="41/64"
assert cases["refined"]["normalized_D_power"]=="39/64"
# Actual localized material parameters are separate, not a new count of ideals.
pmax=rmax=Q(1,8); dmax=kmax=Q(1,32); smax=Q(1,16)
hmax=rmax+smax
level=pmax+dmax+kmax+hmax
length=1-pmax-dmax-hmax
assert hmax==Q(3,16) and level==Q(3,8) and length==Q(21,32)
height_margins={}
for a in [Q(1,2),Q(3,2)]:
    assert length-a*level>0
    height_margins[str(a)]=str((length-a*level)/4)
result={"schema":"twisted-gauss-new-convexity-exponents-v1","passed":True,
"scope":"Fresh deterministic synthetic Fraction checks of the NEW contour-height, deletion and localized exponent assembly. NOT proof of FE, actual ideal/character/Gauss data, training, numerical energy or Lean.",
"randomness":"none","grid_material_parameters":{"length_log_scale":"0..2 step1/8","level_log_scale":"0..2 step1/8","horizontal_sigma":"1/2..1 step1/16","left_level_costs":["1/2","3/2"]},
"counts":counts,"localized_cases":cases,
"localized_parameters":{"hmax":"3/16","levelmax":"3/8","lengthmin":"21/32","optimized_height_lower_powers":height_margins},
"old_controls_rerun":False,"full_actual_ramified3_FE_supplied":False,
"note_sha256":hashlib.sha256((ROOT/"planning/twisted-gauss-20261106/lane-c/FE_CONVEXITY_SHARP_ONE_ROW-v1.md").read_bytes()).hexdigest()}
dest=OUT/"checks-v1.json"
assert not dest.exists()
dest.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"passed":True,"counts":counts,"cases":cases,"result":str(dest.relative_to(ROOT))},sort_keys=True))
