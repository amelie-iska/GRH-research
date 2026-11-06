from pathlib import Path
import json,hashlib,subprocess,collections,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
P=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261106-coherent-book/outputs/publication/20261106-coherent-book/release-preparation-v1')
O=R/'outputs/checks/2026-11-06-coherent-release/review-c';O.mkdir(parents=True,exist_ok=True)
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert H(P/'selection-request-v1.json')=='bb0565104b91e1098645bc2e5ef8dffd93ddfd833e4bcd768afad9a38ad60acc'
req=json.loads((P/'selection-request-v1.json').read_text())
old=json.loads((R/'outputs/checks/2026-11-06-coherent-release/lane-c/selection-inputs-v3.json').read_text())
assert len(req['paths'])==216
original={}
for row in req['paths']:
 assert H(R/row['path'])==row['sha256'],row['path']
 original[row['path']]=row['sha256']
additions={
'planning/dual-window-20261106/lane-a/EULER_SCHUR_AND_BESSEL_HIERARCHY-v1.md':'48de3f906d16dbbc60cfd1cef174b0e05b3020279ee8e5f1dacaa408465b24db',
'planning/dual-window-20261106/lane-b/NEW_LOW_MODEL_BOUND-v4.md':'de79e9639fee4b463ae16901459c3f5552434130b88daa9a8b7cfd7b61d97c5d',
'planning/dual-window-20261106/root/SHARP_ROW_DUAL_TAIL-v2.md':'bb2c8277cdcd7673bbca87470bd0d7047cc9eb6bdeace9a1d8423fa9acf31ae1',
'planning/dual-window-20261106/lane-b/WINDOW_AND_COMPLEMENT-v2.md':'a4df542c9a0874fc2ca5b0dabcb39e51a59b3d1a4243f9133e50431439a37890',
'outputs/checks/2026-11-06-dual-window/lane-b/review-a-new/acceptance-v1.json':'8d9a81e4f3f9ce2c556365d2c3883fe362acf96918358ccc3282851a6afb3d86',
'planning/dual-window-20261106/lane-b/review-a-new/REVIEW-v1.md':'e86c0666da42a2d69ea11604f636387cf5f853695c5bae6a9fb1a70b79939e7e',
'outputs/checks/2026-11-06-dual-window/lane-a/review-b-low/acceptance-v1.json':'058a81cbfd74ae645ca1869138209a4b60f2111591cccd00f19023be427cd169',
'planning/dual-window-20261106/lane-a/review-b-low/REVIEW-v1.md':'3d7bd986b6cedb8a79f884cf308ebbd23dfffaa5ae87f80cca39eccc8f4cf5a8',
'outputs/checks/2026-11-06-dual-window/lane-a/review-root-tail/acceptance-v1.json':'f6e710b9eb97694f649eb7bb0d626e4bb8bd6dc8ff06d4107784e734eeb8c917',
'planning/dual-window-20261106/lane-a/review-root-tail/REVIEW-v1.md':'c799587e0bc9816642f543157cca2b781055bb84643bbe8c359c989abb23d4b2',
'outputs/checks/2026-11-06-dual-window/root/review-b/acceptance-v1.json':'490b60fa286067ea79c8d6d51594de5ff9eb130c120eebcc8f06068823309b4d',
'planning/dual-window-20261106/root/review-b/REVIEW-v1.md':'842964cb134cc973b23598e3deba8ac88c4df3308ed83a50fdf431b1a243d212',
'outputs/checks/2026-11-06-dual-window/lane-b/source-pins-v1.json':'e821774ffa74e97d2334b2f89c886e5912d4476877ffb57d70748688c39a8327',
'outputs/checks/2026-11-06-dual-window/lane-a/review-b-low/source-pins-v1.json':'71c048a9ba75952cc9701d5c08114357008d0be325c24fce253000ab1600859d',
'outputs/checks/2026-11-06-dual-window/lane-a/review-root-tail/source-pins-v1.json':'070480d19eeb6f60d1ab671e7b406fe6da6119ead4e73a1829106698db1a2db4',
}
for n,h in additions.items():assert H(R/n)==h and n not in original,n
base={}
for line in subprocess.check_output(['git','-C',str(R),'ls-tree','-rz',req['base_commit']]).split(b'\0'):
 if line:
  h,n=line.split(b'\t',1);base[n.decode()]=h.decode().split()[2]
def row(n,h,group):
 b=(R/n).read_bytes();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 return dict(bytes=len(b),sha256=h,git_blob_sha1=blob,groups=[group],base_relation='unchanged' if base.get(n)==blob else 'modified' if n in base else 'new')
entries={n:row(n,h,'original216-current-pin-unchanged') for n,h in original.items()}
entries.update({n:row(n,h,'explicit-required-mathematical-input-or-governing-review') for n,h in additions.items()})
assert all(n not in base for n in additions),'Additions are new Main science provenance, not existing BASE aliases'
rationale=[
dict(selected_user='planning/intermediate-kernel-20261106/lane-b/EXACT_FINITE_K_ALL_J_BOUND-v1.md',required='planning/dual-window-20261106/lane-a/EULER_SCHUR_AND_BESSEL_HIERARCHY-v1.md',reason='Explicit accepted finite-K Bessel hierarchy Eq9 input, not merely an old source-pin pointer.'),
dict(selected_user='planning/intermediate-kernel-20261106/lane-a/HONEST_BV_MELLIN_INTERMEDIATE-v1.md',required='planning/dual-window-20261106/lane-b/NEW_LOW_MODEL_BOUND-v4.md',reason='Explicit arbitrary-coefficient all-good-ideal Phi norm (4.2), derived from external Theorem1.1 in the actual family.'),
dict(selected_user='planning/intermediate-kernel-20261106/root/CRITICAL_MELLIN_DYADIC-v1.md',required='planning/dual-window-20261106/root/SHARP_ROW_DUAL_TAIL-v2.md',reason='Explicit sharp-row Bessel/derivative summability input.'),
dict(selected_user='planning/dual-window-20261106/lane-b/NEW_LOW_MODEL_BOUND-v4.md',required='planning/dual-window-20261106/lane-b/WINDOW_AND_COMPLEMENT-v2.md',reason='Governing low-model definition (3.2) and its separate exact-window/complement construction; closes the added standalone theorem.'),
]
for a,b in old['promoted_aliases'].items():assert (R/a).read_bytes()==(R/b).read_bytes()
manifest=dict(schema='coherent-release-independent-selection-proposal-v4',proposal_only_not_ROOT_READY=True,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),base_main=req['base_commit'],base_Pages=req['pages_base_commit'],parent_request_sha256=H(P/'selection-request-v1.json'),parent_request_count=216,original216_verified_unchanged=True,entries=dict(sorted(entries.items())),narrow_additions=additions,mathematical_dependency_edges=rationale,promoted_aliases=old['promoted_aliases'],public_exports=req['public_exports'],required_public_paths=req['required_public_paths'],fresh_json_prefixes=[],current_json_files=[],Main_only_UB01=True,coupled_sixth_research_excluded=True,excluded_not_current_inputs=['Old conditional ROOT_NUMBER_SCHUR_AND_FINITE_DUAL-v5: historical diagnostic superseded by proved GLOBAL_ROOT_MULTIPLICATION-v2.','No whole dual-window folder, historical draft versions, controls/tables, automation, primary/publisher cache or build administration.'],no_source_overlay_stage_API_auth_or_scientific_rerun=True)
q=O/'selection-inputs-v4.json'
with q.open('x')as f:json.dump(manifest,f,indent=2,sort_keys=True);f.write('\n')
out=dict(schema='coherent-release-independent-amended-closure-acceptance-v1',passed=True,selection=dict(path=str(q.relative_to(R)),sha256=H(q)),original_request_sha256=H(P/'selection-request-v1.json'),original216_source_pins_unchanged=True,explicit_added_files=len(additions),added_sha256=additions,mathematical_dependency_edges=rationale,all5PDF_18promotion_aliases_UI_native_math_metadata_unchanged=True,whole_folders_or_historical_JSON_not_followed=True,UB01_Main_only_new_coupled_sixth_excluded=True,scope='Narrow mathematical provenance amendment before overlay; current cbk proofs remain complete, while selected standalone intermediate notes now have their explicit governing inputs.',producer=dict(path=str(Path(__file__).relative_to(R)),sha256=H(Path(__file__))),no_helper_execution_staging_auth_API_or_publication=True)
p=O/'amended-closure-acceptance-v1.json'
with p.open('x')as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(dict(selection_sha256=H(q),acceptance_sha256=H(p),files=len(entries),bytes=sum(x['bytes']for x in entries.values()),added=len(additions),base_counts=dict(collections.Counter(x['base_relation']for x in entries.values()))),indent=2))
