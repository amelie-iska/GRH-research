from pathlib import Path
import json,hashlib,subprocess,collections,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-06-coherent-release/lane-c'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=O/'selection-inputs-v2.json';j=json.loads(old.read_text())
receipt='outputs/checks/2026-11-06-coherent-release/root/release-metadata-v2/receipt.json'
assert H(R/receipt)=='3075ba0b128c4cce933bd227e219b17d495b0061bec262050c921bbb1588a795'
meta=json.loads((R/receipt).read_text());assert meta['passed'] and meta['public_release_performed'] is False
rows=j['entries'];stable={p:x['sha256'] for p,x in rows.items() if 'metadata-baseline-await-root-refresh' not in x['groups']}
assert all(H(R/p)==s for p,s in stable.items())
changed=[]
for p,x in list(rows.items()):
 if 'metadata-baseline-await-root-refresh' not in x['groups']:continue
 cur=H(R/p)
 if cur!=x['sha256']:changed.append(p)
 if p in meta['files']:assert cur==meta['files'][p]['sha256']
 else:assert cur==x['sha256']
for p,x in meta['files'].items():
 assert p in rows and H(R/p)==x['sha256']
 if x.get('append_only'):
  before=R/'outputs/checks/2026-11-06-coherent-release/root/release-metadata-v1/before'/p
  assert H(before)==x['before_sha256']==rows[p]['sha256']
  assert (R/p).read_bytes().startswith(before.read_bytes())
assert len(changed)==10
oldindex=(R/'outputs/checks/2026-11-06-coherent-release/root/release-metadata-v2/before/web/index.html').read_bytes()
assert hashlib.sha256(oldindex).hexdigest()==rows['web/index.html']['sha256']
a='303 pages · 40 chapters · 9,172 MathML expressions</strong>; focused articles71/200pages and notes29/89pages.'.encode()
b='319 pages · 40 chapters · 9,810 MathML expressions</strong>; focused articles 76/215 pages and notes 34/105 pages.'.encode()
assert oldindex.count(a)==1 and oldindex.replace(a,b,1)==(R/'web/index.html').read_bytes()
additional=[
'scripts/theme_assets.py','scripts/build_implementation_page.py','scripts/build_verification_page.py','planning/IMPLEMENTATION_QUEUE.json',
receipt,'outputs/checks/2026-11-06-coherent-release/root/release-metadata-v1/receipt.json','planning/coherent-release-20261106/root/prepare_release_metadata_v1.py',
'outputs/checks/2026-11-06-coherent-release/lane-c/named-reproducer-audit-v1.json',
'outputs/checks/2026-11-06-coherent-release/lane-c/scope-guard-review-v1.json',
'planning/coherent-release-20261106/lane-c/SCOPE_GUARD_REVIEW-v1.md',
'planning/coherent-release-20261106/lane-c/audit_selection_v1.py',
'outputs/checks/2026-11-06-coherent-release/lane-c/selection-inputs-v2.json'
]
base={}
for line in subprocess.check_output(['git','-C',str(R),'ls-tree','-rz',j['base_main']]).split(b'\0'):
 if line:
  h,p=line.split(b'\t',1);base[p.decode()]=h.decode().split()[2]
def pin(p,groups):
 b=(R/p).read_bytes();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_sha1=blob,groups=groups,base_relation='unchanged' if base.get(p)==blob else 'modified' if p in base else 'new')
for p in list(rows):
 if 'metadata-baseline-await-root-refresh' in rows[p]['groups']:rows[p]=pin(p,['current-root-reviewed-release-metadata'])
for p in additional:rows[p]=pin(p,['named-metadata-or-scope-reproducer'])
parent=json.loads((R/'outputs/checks/2026-11-06-coherent-release/root/release-metadata-v1/receipt.json').read_text())
assert H(R/'planning/coherent-release-20261106/root/prepare_release_metadata_v1.py')==parent['producer_sha256']
assert meta['producer_sha256'] is None and meta['parent_receipt_sha256']==H(R/'outputs/checks/2026-11-06-coherent-release/root/release-metadata-v1/receipt.json')
queue=json.loads((R/'planning/IMPLEMENTATION_QUEUE.json').read_text())
assert queue['project_complete'] is False and queue['research_complete'] is False
assert next(t for t in queue['tasks'] if t['id']=='P4-source-expansion')['status']=='in_progress'
j.update(schema='coherent-release-independent-selection-proposal-v3',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),metadata_baseline_requires_root_refresh=False,release_metadata_receipt=dict(path=receipt,sha256=H(R/receipt)),parent_proposal=dict(path=str(old.relative_to(R)),sha256=H(old)),metadata_changed_paths=changed,metadata_unchanged_extra_paths=sorted(p for p in rows if 'current-root-reviewed-release-metadata' in rows[p]['groups'] and p not in changed),explicit_additional_paths=additional,not_a_stage_or_publish_authorization=True)
j['entries']=dict(sorted(rows.items()))
j['required_bundle_paths']=j.pop('required_public_paths',[])
j['required_public_paths']=['web/'+p for p in j['required_bundle_paths']]
for e in j['public_exports']:e['bundle_path']=e.pop('target')
j['closure_follow_policy']='All selected paths explicitly pinned. No broad fresh JSON prefixes; named historical edges remain provenance, not current inputs. Exclude ongoing coupled-sixth drafts.'
out=O/'selection-inputs-v3.json';assert not out.exists();out.write_text(json.dumps(j,indent=2,sort_keys=True)+'\n')
report=dict(schema='coherent-release-independent-final-metadata-refresh-v1',passed=True,parent_baseline_sha256=H(old),selection_sha256=H(out),release_metadata_receipt_sha256=H(R/receipt),stable_science_evidence_UI_reproducer_hashes_verified=len(stable),changed_metadata_paths=changed,unchanged_extra_metadata_paths=j['metadata_unchanged_extra_paths'],all7_append_prefixes_exact=True,all10_current_metadata_hashes_exact=True,landing_counter_exact_single_field_replacement=True,parent_v1_producer_retained=True,all5PDFs_and18aliases_preserved=True,UB01_Main_only=True,ongoing_coupled_sixth_drafts_excluded=True,P4_in_progress_both_completion_gates_false=True,scientific_build_browser_control_reruns=0,producer_path=str(Path(__file__).relative_to(R)),producer_sha256=H(Path(__file__)))
p=O/'metadata-refresh-acceptance-v2.json';assert not p.exists();p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'selection_sha256':H(out),'metadata_acceptance_sha256':H(p),'files':len(rows),'bytes':sum(x['bytes'] for x in rows.values()),'base_counts':dict(collections.Counter(x['base_relation'] for x in rows.values())),'changed_metadata':len(changed),'unchanged_extra_metadata':len(j['metadata_unchanged_extra_paths'])},indent=2))
