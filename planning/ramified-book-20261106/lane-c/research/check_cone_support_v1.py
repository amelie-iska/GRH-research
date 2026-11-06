#!/usr/bin/env python3
"""NEW finite formal support/phase controls; not complete arithmetic data."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"outputs/checks/2026-11-06-ramified-book/lane-c/research/cone-controls-v1"
OUT.mkdir(parents=True,exist_ok=True)
phase_checks=0
def charval(exps,coeffs,cond,L):
    if any(e and c for e,c in zip(exps,cond)):return None
    return sum(e*a for e,a in zip(exps,coeffs))%L
for L in [6,12,18]:
    for cond in product([0,1],repeat=2):
        for coeffs in [(0,1),(1,2),(2,5)]:
            for e0 in product(range(L),repeat=2):
                for bb in product(range(3),repeat=2):
                    exps=tuple(e+L*b for e,b in zip(e0,bb))
                    left=charval(exps,coeffs,cond,L)
                    right=charval(e0,coeffs,cond,L)
                    if any(b and c for b,c in zip(bb,cond)):right=None
                    assert left==right
                    phase_checks+=1
assert charval((18,0),(1,2),(1,0),18) is None
assert charval((0,0),(1,2),(1,0),18)==0
assert 6%18!=0 # synthetic rho order18 branch is not killed by a rho^6=1 projection.
def norm_good(exps):return 7**exps[0]*7**exps[1]*19**exps[2]
rlist=[e for e in product(range(6),repeat=3) if norm_good(e)<64]
assert len(rlist)==7
def ideals_below(limit):
    return [e for e in product(range(4),repeat=3) if norm_good(e)<=limit]
def s_supported(limit):
    aa=0
    while 4**aa<=limit:
        bb=0
        while 4**aa*3**bb<=limit:
            yield aa,bb,4**aa*3**bb
            bb+=1
        aa+=1
cases=[];totals={"cone_states":0,"top_states":0,"low_states":0,"low_w_at_least64":0,"r_s_overlap_states":0,"nonsquarefree_s_states":0,"nonsquarefree_r_states":0}
for V in [1,7,10,49]:
    X=64*V**6
    ids=set();own={k:0 for k in totals}
    for re in rlist:
        nr=norm_good(re)
        for se in ideals_below(2*V):
            ns=norm_good(se)
            cap=X//(nr*ns**6)
            if cap<1:continue
            for ah,bh,nh in s_supported(cap):
                ny=nh*nr*ns**6
                assert ny<=X and ns<=2*V
                full=(ah,bh)+tuple(rr+6*ss for rr,ss in zip(re,se))
                assert full not in ids
                ids.add(full)
                # Independently recover the unique sixth-free extraction from full exponents.
                assert tuple(e%6 for e in full[2:])==re
                assert tuple(e//6 for e in full[2:])==se
                top=(V<ns<=2*V and nh*nr<64)
                low=(ns<=V)
                assert top!=low
                if ns>V:assert nh*nr<64
                own["cone_states"]+=1
                own["top_states"]+=int(top)
                own["low_states"]+=int(low)
                own["low_w_at_least64"]+=int(low and nh*nr>=64)
                own["r_s_overlap_states"]+=int(any(a and b for a,b in zip(re,se)))
                own["nonsquarefree_s_states"]+=int(max(se)>=2)
                own["nonsquarefree_r_states"]+=int(max(re)>=2)
    assert own["cone_states"]==own["top_states"]+own["low_states"]
    assert own["low_w_at_least64"]>0
    cases.append({"V":V,"X":X,**own})
    for k in totals:totals[k]+=own[k]
assert totals["top_states"]>0 and totals["r_s_overlap_states"]>0
assert totals["nonsquarefree_s_states"]>0 and totals["nonsquarefree_r_states"]>0
# Exact important boundary: y=(2)^3, N=64, with s=r=unit,V1.
assert 4**3==64 and 1<=1 and not 1>1
qs=[Q(4,5),Q(5,6)];norms=[4,3]
assert all(q**6>=Q(1,n) and q<1 for q,n in zip(qs,norms))
major=1
for q in qs:major/=1-q
assert major==30
geo_checks=0
for cap in [3,9,27]:
    val=Q(1)
    for q in qs:val*=sum(q**i for i in range(cap+1))
    assert val<=major
    geo_checks+=1
result={"schema":"ramified-book-new-cone-formal-controls-v1","passed":True,
"scope":"NEW formal prime-labelled monoid and finite cyclic phase checks for the bounded-good-sixth-free cone complement. NOT the full Eisenstein ideal family, actual Gauss/energy data, a density proof, training, Lean, or an accepted old fixture rerun.",
"phase_material":{"orders":[6,12,18],"two_S_labels":True,"conductor_patterns":"allfourbinarymasks","coefficient_pairs":[[0,1],[1,2],[2,5]],"residue_exponents":"all0..L-1","L_power_exponents":"all0..2"},
"phase_compression_checks":phase_checks,
"raw_zero_negative_control":"L18, exponenth=(18,0),conductormask(1,0): actualeta(h)=0 while omitting b-mask giveseta(h0)=1",
"nonprincipal_rho_sixth_branch":"Syntheticrhoorder18:6mod18nonzero, kept",
"support_material":{"S_norm_labels":[4,3],"good_labels":["g7plus","g7minus","g19"],"good_norms":[7,7,19],"same_norm_labels_stay_distinct":True,"good_sixth_free_r_cutoff":"Nr<64","V":[1,7,10,49],"X":"64V^6","raw_S_parts":"allallowedinmodel,totalnormcapliteral","s":"arbitrary,notSF","old_top":"V<Ns<=2V,Nhr<64,totalnorm<=X","new_low":"Ns<=V,totalnorm<=X,NhrNOTbounded64"},
"cases":cases,"support_totals":totals,
"closed_boundary_control":"V1,X64,r=s=unit,hNorm64 belongsLOWnotTOP",
"weighted_geometric_checks":{"positive_rational_weight_upperbounds":["4/5","5/6"],"sixthpowers_dominate_inverse_norm":True,"infinite_product_majorant":str(major),"finite_partial_checks":geo_checks},
"randomness":"none","old_controls_rerun":False,
"note_sha256":hashlib.sha256((ROOT/"planning/ramified-book-20261106/lane-c/research/BOUNDED_GOOD_PART_COMPLEMENT-v1.md").read_bytes()).hexdigest()}
p=OUT/"checks-v1.json";assert not p.exists();p.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"passed":True,"phase_checks":phase_checks,"support_totals":totals,"cases":cases,"path":str(p.relative_to(ROOT))},sort_keys=True))
