from pathlib import Path
import json,hashlib,shutil
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');C=R/'outputs/checks/2026-11-05-rough-mask';out=C/'promotion-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
required=['review/canonical-acceptance-v1.json','main-attempt/finite-data-acceptance-v1.json','root/pit-review-v1.json','builds/build-acceptance-v1.json','review-integration/integration-acceptance-v1.json','root/native-qa-v1/browser.json','root/visual-v1/root-inspection-v1.json']
records={}
for name in required:
 p=C/name;d=json.loads(p.read_text());assert d.get('passed') is True,(name,list(d)[:8]);records[str(p.relative_to(R))]=sha(p)
pdf=R/'outputs/rough-mask-book-20261105/v1/pdf';native=R/'outputs/rough-mask-book-20261105/v1/native'
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
 b=R/'outputs/rough-mask-articles-20261105'/(edition+'-v1');builds.append(b/'build-record.json')
 for ext in ['pdf','log']:pairs.append((b/('resolutions-'+edition+'.'+ext),R/'outputs/papers'/('resolutions-'+edition+'.'+ext)))
 b=R/'outputs/rough-mask-articles-20261105'/('notes-'+edition+'-v1');builds.append(b/'build-record.json')
 for ext in ['pdf','log']:pairs.append((b/('validated-oracle-'+edition+'.'+ext),R/'outputs/papers/validated-oracle-20261104'/('validated-oracle-'+edition+'.'+ext)))
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
record={'passed':True,'all_acceptance_records_sha256':records,'build_records_sha256':{str(p.relative_to(R)):sha(p) for p in builds},'changed_artifacts':changes,'edition':{'book_pages':288,'chapters':40,'MathML':8552,'old_MathML_literal_preserved':8176,'old_tables_literal_preserved':386,'canonical_iframes':13,'old_SVG_refs_preserved':29,'new_source_matched_SVGs':0,'focused_pages':[67,183],'notes_pages':[25,74]},'scope':'Only accepted PDF/nativev1 and four articlev1 artifacts promoted. All old diagram assets retained; every changed production byte backed up. Explicit rough-prime correction bound and fresh exact controls; no new global power, Lean or GRH.'}
(out/'promotion-v1.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'changed_artifacts':len(changes),'record':str(out/'promotion-v1.json')}))
