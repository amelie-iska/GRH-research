#!/usr/bin/env python3
"""Guarded local promotion; preserve every existing before byte, no Git/index/publishing."""
from pathlib import Path
import hashlib,json,shutil,subprocess
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
C=R/'outputs/checks/2026-11-06-gauss-book'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=C/'promotion-v1';assert not out.exists()
 required=['root/source-integration-v4.json','review-math-a/acceptance-v1.json','review-integration-a/acceptance-v2.json','review-artifact-c/acceptance-v1.json','builds/run-v3/aggregate.json','native/run-v3/native-build-record.json','pdf-visual/run-v2/review-v1.json','root/native-visual-v1.json','lane-b/native-browser-v2/receipt.json']
 gates={}
 for n in required:
  p=C/n;x=json.loads(p.read_text());assert x.get('passed',x.get('accepted',False)) is True,n;gates[str(p.relative_to(R))]=sha(p)
 before=json.loads((C/'root/integration-before-v1.json').read_text())
 for n,digest in before['old_book_assets_sha256'].items():assert sha(R/n)==digest,('Concurrent live asset edit',n)
 source=json.loads((C/'root/source-integration-v4.json').read_text())
 for e in source['edits']:assert sha(R/e['path'])==e['after'],e['path']
 agg=json.loads((C/'builds/run-v3/aggregate.json').read_text())
 native=C/'native/run-v3';nr=json.loads((native/'native-build-record.json').read_text())
 assert nr['math_nodes']==10299 and nr['canonical_labs']==14 and nr['svg_refs']==31 and nr['old_HTML_restored_exactly']
 for n,d in nr['source_sha256'].items():assert sha(R/n)==d,n
 book=Path(agg['results']['book-pdf']['pdf']).parent
 pairs=[(book/('main.'+e),R/'outputs/book'/('surface-orders-book.'+e)) for e in ['pdf','log','toc']]
 allowed={'main.html','sources/gauss-tail-core.tex','sources/gauss-tail-details.tex','sources/gauss-tail-figure.tex','figures/gauss-tail-partition.pdf','figures/gauss-tail-partition.svg','figures/gauss-tail-partition.tex'}
 for p in (native/'book').rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(native/'book');dest=R/'web/book'/rel
  if not dest.exists() or p.read_bytes()!=dest.read_bytes():
   assert str(rel) in allowed,str(rel);pairs.append((p,dest))
 for ed in ['concise','extended']:
  for group,stem,dest in [('focused','resolutions-'+ed,R/'outputs/papers'),('notes','validated-oracle-'+ed,R/'outputs/papers/validated-oracle-20261104')]:
   br=agg['results'][group+'-'+ed];assert sha(Path(br['pdf']))==br['pdf_sha256']
   b=json.loads(Path(br['record']).read_text());assert b['passed']
   for n,d in b['source_sha256'].items():assert sha(R/n)==d,n
   directory=Path(br['pdf']).parent
   for e in ['pdf','log']:pairs.append((directory/(stem+'.'+e),dest/(stem+'.'+e)))
 assert len(pairs)==18
 gate=json.loads((C/'review-artifact-c/acceptance-v1.json').read_text())
 source_pins=gate['artifact_sha256'];target_pins=gate['target_before_sha256']
 assert set(source_pins)=={str(p.relative_to(R)) for p,t in pairs}
 assert set(target_pins)=={str(t.relative_to(R)) for p,t in pairs}
 for p,t in pairs:
  assert sha(p)==source_pins[str(p.relative_to(R))]
  assert (sha(t) if t.exists() else None)==target_pins[str(t.relative_to(R))]
  assert not t.with_name(t.name+'.gauss-book-pending').exists()
 assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()=='dba37ffaa78c82ade1385f7ee56c907ab0c67d3a'
 ip=Path(subprocess.check_output(['git','rev-parse','--git-path','index'],cwd=R,text=True).strip());ip=ip if ip.is_absolute() else R/ip
 index_before=sha(ip);assert index_before=='0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c'
 pairs.sort(key=lambda pair:pair[1]==R/'web/book/main.html')
 out.mkdir();changes=[]
 for p,t in pairs:
  old=sha(t) if t.exists() else None
  if old==sha(p):continue
  if t.exists():
   backup=out/'before'/t.relative_to(R);backup.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(t,backup)
  t.parent.mkdir(parents=True,exist_ok=True)
  pending=t.with_name(t.name+'.gauss-book-pending');shutil.copyfile(p,pending);assert pending.read_bytes()==p.read_bytes();pending.replace(t)
  changes.append(dict(source=str(p.relative_to(R)),target=str(t.relative_to(R)),before_sha256=old,after_sha256=sha(t)))
 assert sha(ip)==index_before and sha(R/'web/book/main.html')==nr['new_HTML_sha256']
 rec=dict(passed=True,changed_artifacts=changes,acceptance_records_sha256=gates,independently_reviewed_artifact_sha256=source_pins,producer_sha256=sha(Path(__file__)),edition=dict(book_pages=333,chapters=40,MathML=10299,old_literal_MathML_preserved=9810,tables=389,canonical_iframes=14,old_canonical_iframes_preserved=14,SVG_refs=31,old_SVG_refs_preserved=30,focused_pages=[81,228],notes_pages=[39,118]),source_HEAD_preserved=True,source_index_sha256=index_before,index_edited=False,old8765_untouched=True,new_Lean_declarations=0,public_release_performed=False,project_complete=False,research_complete=False,scope='Verified local five-PDF/native source milestone only. Exact-discrete small-cutoff model/full signed/positive determinant/comprehensive Lean/GRH remain open. Historical candidates/evidence preserved.')
 (out/'promotion-v1.json').write_text(json.dumps(rec,indent=2)+'\n')
 print(json.dumps(dict(passed=True,changed=len(changes),sha256=sha(out/'promotion-v1.json'))))
if __name__=='__main__':main()
