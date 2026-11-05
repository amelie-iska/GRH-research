from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
out=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/promotion'
assert not out.exists(), 'Do not overwrite prior promotion evidence'
assert (ROOT/'web/arithmetic-learning.mjs').is_file(), 'Replay must exist before book promotion'
records=['outputs/arithmetic-learning-book-20261105/v5/pdf/build-record.json','outputs/arithmetic-learning-book-20261105/v6-native/native-build-record.json','outputs/arithmetic-learning-articles-20261105/concise-v2/build-record.json','outputs/arithmetic-learning-articles-20261105/extended-v4/build-record.json','outputs/arithmetic-learning-articles-20261105/notes-concise-v2/build-record.json','outputs/arithmetic-learning-articles-20261105/notes-extended-v3/build-record.json']
for n in records:
 d=json.loads((ROOT/n).read_text());assert d['passed']
 for name,h in d.get('source_sha256',{}).items():assert sha((ROOT/name).read_bytes())==h,(n,name)
for n in ['outputs/checks/2026-11-05-arithmetic-learning/review-mixed/acceptance-v1.json','outputs/checks/2026-11-05-arithmetic-learning/review-learning/acceptance-v2.json']:
 assert (ROOT/n).is_file()
book=ROOT/'outputs/arithmetic-learning-book-20261105/v5/pdf'
native=ROOT/'outputs/arithmetic-learning-book-20261105/v6-native/book'
maps={str(book/'main.pdf'):'outputs/book/surface-orders-book.pdf',str(book/'main.log'):'outputs/book/surface-orders-book.log',str(book/'main.toc'):'outputs/book/surface-orders-book.toc',str(native/'main.html'):'web/book/main.html'}
for p in (native/'sources').glob('*.tex'):
 target=ROOT/'web/book/sources'/p.name
 if not target.exists() or p.read_bytes()!=target.read_bytes():maps[str(p)]=str(target.relative_to(ROOT))
for edition,v in [('concise','concise-v2'),('extended','extended-v4')]:
 for ext in ['pdf','log']:
  maps[str(ROOT/f'outputs/arithmetic-learning-articles-20261105/{v}/resolutions-{edition}.{ext}')]=f'outputs/papers/resolutions-{edition}.{ext}'
for edition,v in [('concise','notes-concise-v2'),('extended','notes-extended-v3')]:
 for ext in ['pdf','log']:
  maps[str(ROOT/f'outputs/arithmetic-learning-articles-20261105/{v}/validated-oracle-{edition}.{ext}')]=f'outputs/papers/validated-oracle-20261104/validated-oracle-{edition}.{ext}'
for source,target in maps.items():
 assert Path(source).is_file(),source
 if target.endswith('.log'):assert not re.search(r'undefined references|Citation .* undefined|Reference .* undefined|Overfull',Path(source).read_text())
out.mkdir();(out/'previous').mkdir()
entries=[]
for source,target in maps.items():
 s=Path(source);t=ROOT/target;old=sha(t.read_bytes()) if t.exists() else None
 if t.exists():
  p=out/'previous'/target;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.read_bytes())
 # Main HTML last so all companion artifacts already exist.
 entries.append(dict(source=str(s.relative_to(ROOT)),target=target,previous_sha256=old,new_sha256=sha(s.read_bytes())))
for x in sorted(entries,key=lambda x:x['target']=='web/book/main.html'):
 t=ROOT/x['target'];t.parent.mkdir(parents=True,exist_ok=True);t.write_bytes((ROOT/x['source']).read_bytes());assert sha(t.read_bytes())==x['new_sha256']
report=dict(passed=True,production_promoted=True,records=records,files=entries,pages=[261,59,157,17,48],MathML=7352,new_Lean_declarations=0,research_complete=False,implementation_complete=False,failed_candidates_preserved=True,scope='Only source-bound, independently reviewed, build/browser-checked PDF/native artifacts promoted; source HEAD/index and unrelated progress preserved.')
(out/'promotion.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'promoted_files':len(entries),'pages':report['pages'],'MathML':7352}))
