from pathlib import Path
import json,hashlib,shutil
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');C=R/'outputs/checks/2026-11-05-physical-sieve';out=C/'promotion-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
required=['review/canonical-acceptance-v3.json','builds/four-builds-v2.json','builds/build-acceptance-v1.json','review-integration/integration-acceptance-v1.json','review-integration-a/producer-source-acceptance-v1.json','root/native-qa-v1/browser.json','root/visual-v1/root-inspection-v1.json','ui/frozen-receipt-v1.json']
records={}
for name in required:
 p=C/name;d=json.loads(p.read_text());assert d.get('passed') is True,(name,list(d)[:8]);records[str(p.relative_to(R))]=sha(p)
pdf=R/'outputs/physical-sieve-book-20261105/v3/pdf';native=R/'outputs/physical-sieve-book-20261105/v3/native'
builds=[pdf/'build-record.json',native/'native-build-record.json']
pairs=[(pdf/('main.'+ext),R/'outputs/book'/('surface-orders-book.'+ext)) for ext in ['pdf','log','toc']]
allowed_figures={'figures/signed-divisor-workflow.pdf','figures/signed-divisor-workflow.tex','figures/signed-divisor-workflow-.svg'}
for p in (native/'book').rglob('*'):
 if not p.is_file():continue
 relative=p.relative_to(native/'book');target=R/'web/book'/relative
 if not target.exists() or p.read_bytes()!=target.read_bytes():
  assert str(relative)=='main.html' or relative.parts[0]=='sources' or str(relative) in allowed_figures,('Unexpected changed native asset',relative)
  pairs.append((p,target))
for edition in ['concise','extended']:
 b=R/'outputs/physical-sieve-articles-20261105'/(edition+('-v1'if edition=='concise'else'-v2'));builds.append(b/'build-record.json')
 for ext in ['pdf','log']:pairs.append((b/('resolutions-'+edition+'.'+ext),R/'outputs/papers'/('resolutions-'+edition+'.'+ext)))
 b=R/'outputs/physical-sieve-articles-20261105'/('notes-'+edition+('-v1'if edition=='concise'else'-v2'));builds.append(b/'build-record.json')
 for ext in ['pdf','log']:pairs.append((b/('validated-oracle-'+edition+'.'+ext),R/'outputs/papers/validated-oracle-20261104'/('validated-oracle-'+edition+'.'+ext)))
ui=json.loads((C/'ui/frozen-receipt-v1.json').read_text())
assert set(ui['assets'])=={'web/quadratic-pivot.html','web/quadratic-pivot.mjs','web/quadratic-pivot.css','web/physical-sieve-model.mjs'}
for target,pin in ui['assets'].items():
 source=R/pin['candidate'];assert sha(source)==pin['sha256'];pairs.append((source,R/target))
for p in builds:
 d=json.loads(p.read_text());assert d['passed'] is True,p
 for name,h in d.get('source_sha256',{}).items():assert sha(R/name)==h,(p,name)
for p,target in pairs:assert p.is_file(),p
out.mkdir(parents=True,exist_ok=False);changes=[]
for p,target in pairs:
 before=sha(target) if target.exists() else None
 if before==sha(p):continue
 if target.exists():
  back=out/'before'/target.relative_to(R);back.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(target,back)
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target);assert target.read_bytes()==p.read_bytes()
 changes.append({'source':str(p.relative_to(R)),'target':str(target.relative_to(R)),'before_sha256':before,'after_sha256':sha(target)})
record={'passed':True,'all_acceptance_records_sha256':records,'build_records_sha256':{str(p.relative_to(R)):sha(p) for p in builds},'changed_artifacts':changes,'edition':{'book_pages':303,'chapters':40,'MathML':9172,'old_MathML_literal_preserved':8552,'old_tables_literal_preserved':388,'canonical_iframes':13,'old_SVG_refs_preserved':29,'new_source_matched_SVGs':0,'focused_pages':[71,200],'notes_pages':[29,89]},'scope':'Only accepted bookPDF/nativev3 and concisev1/extendedv2 article+note artifacts and source-bound inspectorv3 promoted. Every changed production byte backed up. External-preprint application gives unsigned9/8 and scopedA6=1signed13/12; target signed estimate, complete Lean and GRH remain open.'}
(out/'promotion-v1.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'changed_artifacts':len(changes),'record':str(out/'promotion-v1.json')}))
