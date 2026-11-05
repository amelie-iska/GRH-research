from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[3];sha=lambda b:hashlib.sha256(b).hexdigest()
old=json.loads((R/'outputs/checks/2026-11-05-arithmetic-learning/promotion/promotion.json').read_text())
out=R/'outputs/checks/2026-11-05-arithmetic-learning/final-diff-fixes/promotion';assert not out.exists();out.mkdir()
records=[old['records'][0],old['records'][1]]+[f'outputs/arithmetic-learning-articles-20261105/{v}/build-record.json' for v in ['concise-v3','extended-v5','notes-concise-v3','notes-extended-v4']]
for n in records:
 d=json.loads((R/n).read_text());assert d['passed']
 for p,h in d['source_sha256'].items():assert sha((R/p).read_bytes())==h,(n,p)
entries=old['files'];replacements={}
for edition,v in [('concise','concise-v3'),('extended','extended-v5')]:
 for ext in ['pdf','log']:replacements[f'outputs/papers/resolutions-{edition}.{ext}']=f'outputs/arithmetic-learning-articles-20261105/{v}/resolutions-{edition}.{ext}'
for edition,v in [('concise','notes-concise-v3'),('extended','notes-extended-v4')]:
 for ext in ['pdf','log']:replacements[f'outputs/papers/validated-oracle-20261104/validated-oracle-{edition}.{ext}']=f'outputs/arithmetic-learning-articles-20261105/{v}/validated-oracle-{edition}.{ext}'
for x in entries:
 assert sha((R/x['target']).read_bytes())==x['new_sha256']
 if x['target'] not in replacements:continue
 t=R/x['target'];p=out/'previous'/x['target'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.read_bytes())
 source=replacements[x['target']];s=R/source
 if s.suffix=='.log':assert not re.search(r'undefined references|Citation .* undefined|Reference .* undefined|Overfull',s.read_text())
 x.update(source=source,previous_first_promotion_sha256=x['new_sha256'],new_sha256=sha(s.read_bytes()));t.write_bytes(s.read_bytes())
report=dict(old,records=records,files=entries,scope='Final exposition-only wrapper fixes:4PDFs/logs rebuilt and source-bound; bookPDFv5/nativev6 and all exact mathematical/learner bytes remain unchanged. First promotion and prior bytes preserved.',supersedes_for_current_artifacts='outputs/checks/2026-11-05-arithmetic-learning/promotion/promotion.json',new_promoter='planning/arithmetic-learning-20261105/integration/promote-v2.py')
(out/'promotion-v2.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'rebuilt_PDFs':4,'updated_artifacts':8,'current_complete_target_map':len(entries),'pages':report['pages']}))
