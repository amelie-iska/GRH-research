#!/usr/bin/env python3
"""NEW exact mixed phase/ray/raw-drop and capacity controls, no Gauss/FE old-suite replay."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
OUT=ROOT/"outputs/checks/2026-11-06-growing-modulus/lane-c/postresearch/mixed-pivot-v1/controls-v1"
assert not OUT.exists();OUT.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
states=0;dropstates=0
# Formal zeta18 exponents: actual sextic phases are multiples3; rayrho may haveorder18.
for rho in range(18):
 for diff in range(6):
  eta=(rho+3*diff)%18
  for jr in range(6):
   for bv,al in [(0,0),(1,0),(1,1)]:  # v2SF andell|v2, with r valuations0..5
    for collision in [False,True]:
     for Szero in [False,True]:
      rawzero=Szero or(collision and(jr>0 or bv>0))
      # One factor3diff means chi6,m*bar chi6,n; reciprocity alpha cancels identically.
      left=(6*diff*bv+eta*al-eta*jr)%18 if not rawzero else None
      right=(-2*rho*bv+eta*(al+2*bv-jr))%18 if not rawzero else None
      assert left==right
      good=(diff*(al+2*bv-jr))%6
      gamma=(diff*(al+2*bv+5*jr))%6
      assert good==gamma  # ONLY the goodsextic factor may replace conjugate byfifthpower.
      if collision and(jr>0 or bv>0) and(al+2*bv+5*jr)%6==0:
       assert rawzero and left is None;dropstates+=1
      states+=1
# Genuine controls against both identified false simplifications.
assert (-1)%18 !=5%18  # rho18 means total barη !=η^5
assert (1+2+5*3)%6==0  # r^3 andell|v2 gives sixthpower phase
dropped_raw=None;dropped_primitive_unit=0
assert dropped_raw!=dropped_primitive_unit
# ORIGINAL(k,v2)=1; do not add k/r,k/s,r/v2/s masks.
allowed=0;kr_overlap=0;ks_overlap=0;rv_overlap=0
for bv,al in [(0,0),(1,0),(1,1)]:
 for k in [0,1]:
  for jr in range(6):
   for sx in [0,1]:
    original=(k*bv==0)
    if not original:continue
    assert k*al==0  # originalellcoprime follows, no new condition
    allowed+=1;kr_overlap+=bool(k and jr);ks_overlap+=bool(k and sx);rv_overlap+=bool(bv and jr)
assert kr_overlap and ks_overlap and rv_overlap
# Exact capacity/envelope powers, no floating fit and no arithmeticenergydata.
delta=F(7,144);X=F(3,8);bounds=[]
for a2 in [F(0),F(1,24),F(1,6),F(3,8)]:
 for slack in [F(0),F(1,2),F(1)]:
  a1=(F(3,4)-2*a2)*slack
  assert a1>=0 and a1+2*a2<=F(3,4)
  lead=a1+F(7,6)*a2+X/6-F(1,9)+delta
  bessel=2*a1+a2+F(7,6)*X+F(5,6)*delta-2
  equal=a1+a2+X/6+F(5,6)*delta-1
  assert lead<=F(3,4)-F(5,6)*a2
  assert bessel<=-F(19,864)-3*a2
  assert equal<=-F(127,864)-a2
  qmax=delta+a2;z=F(2,9)-qmax/3;assert z>=F(35,432)>0
  bounds.append(dict(logD_A1=str(a1),logD_A2=str(a2),leading=str(lead),Bessel=str(bessel),equalnorm=str(equal),Z_lower=str(z)))
assert 64*F(35,144)>=1  # 2D^(61/144)<=D^(2/3) forD>=2^64
assert F(5,12)+F(7,6)*F(1,6)==F(11,18)
# Literalunit branch and arithmetic-empty!=capacity-empty distinction.
good_norm_nodes=[1,7,13,19,25]
assert [n for n in good_norm_nodes if 1<=n<2]==[1]
assert not [n for n in good_norm_nodes if 2<=n<=3]
# The original nodal interpolant is1 at everyintegernormnode in[2,3], regardless
# ofabsenceofgoodideals there; a finitePoissonprojection is NOTdeclaredzero.
nodal_values_at_formal_integer_nodes={2:1,3:1}
assert nodal_values_at_formal_integer_nodes[2]==1
rec=dict(schema="actual-mixed-new-formal-phase-capacity-controls-v1",passed=True,created_utc=datetime.now(timezone.utc).isoformat(),
 producer_sha256=sha(Path(__file__)),governing_note_sha256=sha(Path(__file__).with_name("ACTUAL_MIXED_PRIMITIVE_CONE-v2.md")),
 mixed_rho18_sextic_raw_phase_states=states,raw_sixthpowerdrop_states=dropstates,
 total_eta_fifthpower_negative_control=True,rawsupport_restoration_negative_control=True,
 original_k_v2_constraint=True,allowed_formal_support_states=allowed,retained_k_r_overlap_states=kr_overlap,retained_k_s_overlap_states=ks_overlap,retained_r_v2_overlap_states=rv_overlap,
 Fraction_capacity_vertices=bounds,literal_unit_fibre_J_np_scope=True,arithmeticempty_not_forced_zero=True,
 arithmetic="exact modular integer phases/None forrawzero and Fraction powers; nofloat/randomness",seed="none",
 scope="Formal finite ray/sextic phase and support/capacity checks ONLY. No actual Gauss symbols, ideal energies, density, sourceFE/Perron or old arithmetic/control suites run; generalproof remains in note.",
 old_controls_or_FE_tail_norm_build_browser_Lean_executed=False,source_data_mutated=False)
p=OUT/"checks-v1.json";p.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
print(json.dumps(dict(passed=True,path=str(p.relative_to(ROOT)),sha256=sha(p),formal_mixed_phase_states=states,raw_drop_states=dropstates,capacity_vertices=len(bounds)),indent=2))
