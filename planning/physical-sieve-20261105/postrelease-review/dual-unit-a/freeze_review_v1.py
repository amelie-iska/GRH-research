#!/usr/bin/env python3
"""Freeze the new component proof review and narrow prior-scope addendum only."""
from pathlib import Path
import datetime,hashlib,json,subprocess
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
A=R/'planning/physical-sieve-20261105/postrelease-review/dual-kernel-a'
O=R/'planning/physical-sieve-20261105/postrelease-review/dual-unit-a'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p,s):
 p=Path(p); a=sha(p); assert a==s,(str(p),a,s); return a
pin(A/'acceptance-v1.json','a5b972340f4117c813ee64b9da8c8adc6c4f8cc2f138d78393574a65956f0a3b')
pin(A/'source-pins-v1.json','44e9d507fff04f1e3474f92ca091ec373ca7940d932eb565c98450338c9486c6')
old=json.loads((A/'source-pins-v1.json').read_text()); expected=old['protected_states_before']
def states():
 out=[]
 for x in expected:
  p=Path(x['path']); h=subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip(); ip=Path(subprocess.check_output(['git','-C',str(p),'rev-parse','--git-path','index'],text=True).strip())
  if not ip.is_absolute():ip=p/ip
  a={'path':str(p),'HEAD':h,'index_sha256':sha(ip)};assert a==x,(a,x);out.append(a)
 return out
before=states(); assert len(before)==12
inputs={
'planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v1.md':'bb49f6aeeca666d047bade9e226010493ede10e682e6e1fdb5eb65aff62a7ef8',
'planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v3.md':'abeee9010e2b500565ce857f930650c277999fecc2d6cc64b59e9b0ab1973744',
'outputs/checks/2026-11-05-physical-sieve/postrelease-research/dual-unit-k-v1/source-freeze-v1.json':'313678e0e769174e0fd81545a2a0f0a698b16cefe840e0b7af9e28554459b1a6',
'outputs/checks/2026-11-05-physical-sieve/postrelease-research/dual-unit-k-v1/source-freeze-v3.json':'9ad3e10ff1b5d713f73cc8fa07f68eea481ac1431ff5658724a30989d422c06e',
'planning/physical-sieve-20261105/postrelease-research/dual-kernel-v1/DRAFT-v8.md':'cba96d347cd880cdead3a330ce5e39969b1950c049df1750f6444ce68a0d4ff7',
'planning/prime-fibre-20261105/lane-b/primary/defaveri-optimal-v1.pdf':'97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726',
'planning/prime-fibre-20261105/lane-b/primary/defaveri-optimal-v1.txt':'ef550aa4bca1659c6d98ebf69e2cbd42a2793b707f6171f53d1b2baeb8654a57',
'papers/weighted-cutoff-core.tex':'e358e0a3686caaa1f3d676f360a99b9969ef2d66ed666163e9f8057c58d3f1f2'}
# The original weighted-cutoff pin is authoritative; retain its complete digest.
inputs['papers/weighted-cutoff-core.tex']='e358e0a3686caaa1f3d676f360a99b9969ef2d66ed666163e9f8057c58d3f1f2'
# Correct the literal above from the accepted immutable input snapshot, not a new source assumption.
inputs['papers/weighted-cutoff-core.tex']=old['source_sha256']['papers/weighted-cutoff-core.tex']
actual={n:pin(R/n,s) for n,s in inputs.items()}
for n,s in old['frozen_canonical_sha256'].items():pin(R/n,s)
signal=old['release_signal'];pin(signal['path'],signal['sha256'])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for n in ['source-pins-v1.json','acceptance-v1.json']:assert not (O/n).exists(),n
assert not (A/'scope-addendum-v1.json').exists()
source={'schema':'dual-unit-independent-inputs-v1','checked_utc':now,'source_sha256':actual,'protected_states_before':before,'frozen_canonical_sha256':old['frozen_canonical_sha256'],'release_signal':signal,'full_primary_cache_local_only':True,'mathematical_or_arithmetic_controls_rerun':False}
(O/'source-pins-v1.json').write_text(json.dumps(source,indent=2,sort_keys=True)+'\n')
add={'schema':'dual-kernel-two-pivot-scope-addendum-v1','passed':True,'created_utc':now,'preserved_acceptance_path':str((A/'acceptance-v1.json').relative_to(R)),'preserved_acceptance_sha256':sha(A/'acceptance-v1.json'),'scope_note_path':str((A/'SCOPE-ADDENDUM-v1.md').relative_to(R)),'scope_note_sha256':sha(A/'SCOPE-ADDENDUM-v1.md'),'clarifying_author_note_path':'planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v3.md','clarifying_author_note_sha256':inputs['planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v3.md'],'actual_scope':'v3=v4=v5=v6=O; u0 unit/S-supported, no good-prime support','extension_requires_primal_z_masks_and_rescalings':True,'prior_identity_and_powers_unchanged':True,'no_rerun_or_release_change':True}
(A/'scope-addendum-v1.json').write_text(json.dumps(add,indent=2,sort_keys=True)+'\n')
after=states();assert after==before
receipt={'schema':'dual-unit-independent-acceptance-v1','passed':True,'verdict':'PASS_UNIFORM_COMPONENT_APPROXIMATION_WITH_EXPLICIT_ERRORS','frozen_utc':now,'governing_note':'planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v3.md','governing_note_sha256':inputs['planning/physical-sieve-20261105/postrelease-research/dual-unit-k-v1/DUAL_UNIT_K_LEMMA-v3.md'],'review_path':str((O/'REVIEW-v1.md').relative_to(R)),'review_sha256':sha(O/'REVIEW-v1.md'),'source_pins_path':str((O/'source-pins-v1.json').relative_to(R)),'source_pins_sha256':sha(O/'source-pins-v1.json'),'freezer_path':str(Path(__file__).relative_to(R)),'freezer_sha256':sha(Path(__file__)),'v8_scope_addendum_path':str((A/'scope-addendum-v1.json').relative_to(R)),'v8_scope_addendum_sha256':sha(A/'scope-addendum-v1.json'),'release_signal':signal,'protected_states_count':12,'protected_states_unchanged':True,'frozen_canonical_sources_unchanged':True,'checked':['Actual component prefactor with primitive F/root and cubic eta^2','Exact pre-S finite Kcut, empty fibres and representation dependence','Full actual deletion union and distinction from abstract arbitrary T','Bessel/Mellin/Fourier normalization and complex signed mean','Uniform moment bounds without derivative seminorms','Ideal count2X, strict tail4/K, zeta3<=3 and zeta4<=8/3','Absolute Euler recombination with both explicit error terms'],'limitations':['Only specified good dual-unit component, not whole kernel','No nonvanishing, lower bound or target-power gain','Euler factor stays orientation/deletion dependent','All nonunit and S-supported dual modes remain','No extension to extra frozen good factors without primal inclusion-exclusion'],'arithmetic_controls_builds_browser_auth_publication_rerun':False,'excluded_from_current_frozen_release':True,'no_source_or_index_mutation':True}
(O/'acceptance-v1.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':True,'receipt_path':str((O/'acceptance-v1.json').relative_to(R)),'receipt_sha256':sha(O/'acceptance-v1.json'),'review_sha256':sha(O/'REVIEW-v1.md'),'source_pins_sha256':sha(O/'source-pins-v1.json'),'scope_addendum_path':str((A/'scope-addendum-v1.json').relative_to(R)),'scope_addendum_sha256':sha(A/'scope-addendum-v1.json'),'scope_note_sha256':sha(A/'SCOPE-ADDENDUM-v1.md'),'freezer_sha256':sha(Path(__file__)),'protected_states':len(before)},sort_keys=True))
