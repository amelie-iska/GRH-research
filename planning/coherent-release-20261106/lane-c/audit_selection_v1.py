from pathlib import Path
import hashlib,json,ast,subprocess,collections,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
P=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261106-coherent-book/outputs/publication/20261106-coherent-book/release-preparation-v1')
O=R/'outputs/checks/2026-11-06-coherent-release/lane-c'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((O/'selection-inputs-v2.json').read_text())
metadata={p for p,x in m['entries'].items() if 'metadata-baseline-await-root-refresh' in x['groups']}
stable={p:x['sha256'] for p,x in m['entries'].items() if p not in metadata}
assert all(H(R/p)==v for p,v in stable.items())
assert len(m['promoted_aliases'])==18
assert all((R/a).read_bytes()==(R/b).read_bytes() for a,b in m['promoted_aliases'].items())
freeze=json.loads((R/'outputs/checks/2026-11-06-coherent-book/lane-c/frozen-receipt-v1.json').read_text())
frozen=freeze['files']
for p,v in frozen.items():
 sha=v['sha256'] if isinstance(v,dict) else v
 assert H(R/p)==sha and p in m['entries'],p
assert len(frozen)==15
builder=ast.parse((R/'scripts/build_public_site.py').read_text())
tuples=[ast.literal_eval(x) for x in ast.walk(builder) if isinstance(x,ast.Tuple) and len(x.elts)==2 and all(isinstance(v,ast.Constant) and isinstance(v.value,str) for v in x.elts)]
for row in m['public_exports']:assert (row['source'],row['target']) in tuples
helper='scripts/theme_assets.py'
raw=(R/helper).read_bytes();old=subprocess.check_output(['git','-C',str(R),'show',m['base_main']+':'+helper])
assert raw==old
# Current source SHA-only producers; preserved historical failures are separately disclosed.
fields=[]
def walk(v,ctx=''):
 if isinstance(v,dict):
  for k,x in v.items():
   if isinstance(x,str) and len(x)==64 and any(t in k.lower() for t in ['producer','checker','renderer']):fields.append((p,ctx+'/'+k,x))
   walk(x,ctx+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,ctx+'/'+str(i))
for p in m['entries']:
 if p.endswith('.json'):walk(json.loads((R/p).read_text()))
catalog=collections.defaultdict(list)
for p in m['entries']:
 if Path(p).suffix in ['.py','.mjs','.js']:catalog[H(R/p)].append(p)
resolved=[];historical=[]
for p,k,h in fields:
 if 'preserved_prewrite_failures' in k:historical.append({'record':p,'field':k,'sha256':h,'reason':'Preserved failed integration version; not current producer'});continue
 assert h in catalog,(p,k,h)
 resolved.append({'record':p,'field':k,'sha256':h,'selected_sources':catalog[h]})
report={'schema':'coherent-release-independent-named-reproducer-audit-v1','passed':True,'selection_proposal_sha256':H(O/'selection-inputs-v2.json'),'stable_selected_hashes':stable,'metadata_baseline_paths_awaiting_root_refresh':sorted(metadata),'verified_current_UI_files':15,'verified_exact_promoted_aliases':18,'verified_public_PDF_exports':5,'current_SHA_only_producers_resolved':resolved,'historical_producer_references_not_current':historical,'additional_unchanged_BASE_helpers':{helper:{'sha256':H(R/helper),'base_exact':True}},'source_data_immutable':True,'no_scientific_or_numeric_control_build_browser_rerun':True,'not_ROOT_READY_or_publish_authorization':True}
(O/'named-reproducer-audit-v1.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
pins={n:H(P/n) for n in ['release_common_v1.py','propose_allowlist_v1.py','prepare_overlay_v2.py','build_bundle_v1.py']}
review='''# Independent preparation scope review\n\nThe inspected preparation helpers retain exact ROOT_READY/request hashes, the public Main/Pages base commits, twelve prior HEAD/index bindings, canonical relative paths and symlink checks. The common path gate excludes primary/publisher cache directories, build administration and automation metadata. Exact promoted aliases are substituted only after byte equality. Five explicit edition exports include both analytic notes.\n\nThe proposer inspects exact named JSON references and only follows JSON classified current by the approved request. The final request should enumerate current JSON files explicitly and use narrow fresh prefixes. A whole-task fresh prefix would also follow preserved historical draft/snapshot pointers; these are not automatically current proof inputs. Our proposal classifies those edges instead of selecting them.\n\nThe bundle helper checks the exact existing public adapter, raw non-HTML asset equality, intended exported PDFs and the cached verified Pages tree. Planning/raw control records stay Main-only; UB01 has explicit Main-only prefixes. Old unselected Pages leaves remain protected by the later overlay/publication contract.\n\nThis is a static preparation review. The scripts were read, not executed. Root approval of the exact expanded list, current source guards, credential/whitespace gates and staged/live QA remains required. Root is preparing an additive metadata refresh; the initial local milestone receipts retain their historical role.\n'''
q=R/'planning/coherent-release-20261106/lane-c/SCOPE_GUARD_REVIEW-v1.md';q.write_text(review)
scope={'schema':'coherent-release-independent-scope-guard-review-v1','passed':True,'scope':'Read-only static review of preparation helpers; no execution or publication authorization','scripts_sha256':pins,'review':{'path':str(q.relative_to(R)),'sha256':H(q)},'base_main':m['base_main'],'base_Pages':m['base_Pages'],'protected_prior_count':12,'explicit_current_JSON_required_for_bounded_closure':True,'all5_exports_present':True,'UB01_Main_only':True,'no_staging_copy_build_API_auth_or_ref_action':True}
(O/'scope-guard-review-v1.json').write_text(json.dumps(scope,indent=2,sort_keys=True)+'\n')
print(json.dumps({'named_audit_sha256':H(O/'named-reproducer-audit-v1.json'),'scope_review_sha256':H(O/'scope-guard-review-v1.json'),'stable_files':len(stable),'current_producer_fields':len(resolved),'historical_fields':len(historical),'scope_scripts':pins},indent=2))
