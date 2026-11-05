"""Independent accepted-source/build/raw-subtree integration check; no source edits."""
from pathlib import Path
from copy import deepcopy
from urllib.parse import urlsplit
import re,json,hashlib,subprocess,argparse,os,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3];BASE='63edb8a38c026e918077d9864a896cb37badf9da';OUT=ROOT/'outputs/checks/2026-11-05-signed-weights/review-integration'
sha=lambda b:hashlib.sha256(b).hexdigest()
def filehash(p):return sha(p.read_bytes())
def git(*a):return subprocess.check_output(['git','-C',str(ROOT),*a],env=dict(os.environ,GIT_OPTIONAL_LOCKS='0'))
def load(n):return json.loads((ROOT/n).read_text())
def loc(n):return n.tag.rsplit('}',1)[-1]
def serial(n):
 n=deepcopy(n);n.tail=None;return ET.tostring(n,encoding='utf8')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
 acceptance=load('outputs/checks/2026-11-05-signed-weights/review-production/acceptance-v1.json');assert acceptance['passed'];bindings={}
 prefix=b'% Generated shared reviewed material.\n';book=ROOT/'outputs/signed-weights-book-20261105/v1/native/book'
 for kind in ['core','details']:
  n='planning/signed-weights-20261105/root/signed-weights-'+kind+'.tex';data=(ROOT/n).read_bytes();assert sha(data)==acceptance['source_sha256'][n]
  for q in ['papers/signed-weights-'+kind+'.tex','book/chapters/signed-weights-'+kind+'.tex']:
   expected=prefix+data if q.startswith('book/') else data;assert (ROOT/q).read_bytes()==expected,q;bindings[q]=filehash(ROOT/q)
  q=book/'sources'/('signed-weights-'+kind+'.tex');assert q.read_bytes()==prefix+data;bindings[str(q.relative_to(ROOT))]=filehash(q)
 wrappers={}
 for stem in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
  p=ROOT/'papers'/(stem+'.tex');inc=re.findall(r'\\input\{([^}]+)\}',p.read_text());assert inc.count('signed-weights-core')==1;assert inc.count('signed-weights-details')==(1 if 'extended'in stem else 0);assert all(x in inc for x in ['mixed-conductor-core','joint-gauss-core','signed-bilinear-core']);wrappers[str(p.relative_to(ROOT))]=filehash(p)
 w=ROOT/'book/chapters/weighted-cutoff.tex';assert all(w.read_text().count(r'\input{chapters/signed-weights-'+k+'}')==1 for k in ['core','details'])
 records=[('outputs/signed-weights-book-20261105/v1/pdf/build-record.json','outputs/signed-weights-book-20261105/v1/pdf/main.pdf',272),('outputs/signed-weights-book-20261105/v1/native/native-build-record.json',None,None),('outputs/signed-weights-articles-20261105/concise-v1/build-record.json','outputs/signed-weights-articles-20261105/concise-v1/resolutions-concise.pdf',62),('outputs/signed-weights-articles-20261105/extended-v1/build-record.json','outputs/signed-weights-articles-20261105/extended-v1/resolutions-extended.pdf',168),('outputs/signed-weights-articles-20261105/notes-concise-v1/build-record.json','outputs/signed-weights-articles-20261105/notes-concise-v1/validated-oracle-concise.pdf',20),('outputs/signed-weights-articles-20261105/notes-extended-v1/build-record.json','outputs/signed-weights-articles-20261105/notes-extended-v1/validated-oracle-extended.pdf',59)]
 buildbind={};pdfs=[]
 for n,pdf,pages in records:
  d=load(n);assert d['passed'];buildbind[n]=filehash(ROOT/n)
  for rel,h in d.get('source_sha256',{}).items():assert filehash(ROOT/rel)==h,(n,rel);bindings[rel]=h
  if pdf:
   p=ROOT/pdf;assert filehash(p)==d['pdf_sha256'];info=subprocess.check_output(['pdfinfo',str(p)],text=True);assert int(re.search(r'Pages:\s+(\d+)',info)[1])==pages==d.get('pdf_pages',d.get('pages'))
   log=p.with_suffix('.log');lines=log.read_text().splitlines();assert not any(re.search(r'Overfull|undefined references|Reference .* undefined|Citation .* undefined|multiply[- ]defined|^!',s)for s in lines),str(log)
   pdfs.append(dict(path=pdf,pages=pages,sha256=filehash(p),log_sha256=filehash(log)))
 b=git('show',BASE+':web/book/main.html');assert sha(b)=='92e69d423af82e5443a9d2bf3e5527790fd222ad332760a7463046ec98e92369';nb=(book/'main.html').read_bytes();nr=load(records[1][0]);assert sha(nb)==nr['new_HTML_sha256']
 old=re.findall(rb'<math\b[^>]*>.*?</math\s*>',b,re.S);new=re.findall(rb'<math\b[^>]*>.*?</math\s*>',nb,re.S);assert len(old)==7605 and len(new)==7891;cursor=0
 for s in new:
  if cursor<len(old) and s==old[cursor]:cursor+=1
 assert cursor==len(old)
 ot=ET.fromstring(b);nt=ET.fromstring(nb);nodes=lambda t,k:[n for n in t.iter()if loc(n)==k]
 assert [serial(n)for n in nodes(ot,'iframe')]==[serial(n)for n in nodes(nt,'iframe')];assert len(nodes(nt,'iframe'))==13
 tables=[serial(n)for n in nodes(ot,'table')];newtables=[serial(n)for n in nodes(nt,'table')];c=0
 for n in newtables:
  if c<len(tables) and n==tables[c]:c+=1
 assert c==len(tables)
 svg=lambda t:[n.attrib.get('data'if loc(n)=='object'else'src','')for n in t.iter()if loc(n)in ['object','img']and n.attrib.get('data'if loc(n)=='object'else'src','').endswith('.svg')]
 refs=svg(ot);assert refs==svg(nt) and len(refs)==28
 for ref in refs:
  u=urlsplit(ref);assert not u.scheme and not u.netloc
  rel=os.path.normpath('web/book/'+u.path);assert git('show',BASE+':'+rel)==(ROOT/rel).read_bytes();assert (book/u.path).read_bytes()==(ROOT/rel).read_bytes()
 arity={'mfrac':2,'msub':2,'msup':2,'msubsup':3,'munder':2,'mover':2,'munderover':3,'mroot':2};bad=lambda t:[(loc(n),len(list(n)))for n in t.iter()if loc(n)in arity and len(list(n))!=arity[loc(n)]];assert bad(ot)==bad(nt)==[('munder',3)]*3
 ids=[n.attrib['id']for n in nt.iter()if 'id'in n.attrib];assert len(ids)==len(set(ids));labels=re.findall(r'\\label\{([^}]+)\}',(ROOT/'papers/signed-weights-core.tex').read_text()+(ROOT/'papers/signed-weights-details.tex').read_text());assert all(k in ids for k in labels)
 qa='outputs/checks/2026-11-05-signed-weights/native-qa-v1/browser.json';qd=load(qa);assert qd['passed']
 doc='outputs/checks/2026-11-05-signed-weights/root/documentation-v1/record.json';docs=load(doc)
 for n,h in docs['sha256'].items():assert filehash(ROOT/n)==h,n
 # Only the latest append is claimed current; archival prose remains untouched.
 report=ROOT/'research/signed-coprime-weights.md';assert '5/12'in report.read_text() and 'No new power saving'in report.read_text()
 latest='planning/signed-weights-20261105/joint-budget/ACTUAL_SIGNED_BUDGET-v4.md';assert filehash(ROOT/latest)=='07ec61960f77e7e02116bf7ad0f5108954e615558000ddaba0afbb789bb508ff'
 v3=(ROOT/'planning/signed-weights-20261105/joint-budget/ACTUAL_SIGNED_BUDGET-v3.md').read_text();v4=(ROOT/latest).read_text();oldwords='The two Gauss magnitudes and the Jacobi magnitude give exactly1/Q.';newwords='The two Gauss magnitudes, equivalently the central Gauss and Jacobi magnitudes, give exactly1/Q.';assert v3.count(oldwords)==1 and v4==v3.replace(oldwords,newwords)
 head=git('rev-parse','HEAD').decode().strip();ip=Path(git('rev-parse','--git-path','index').decode().strip());ip=ip if ip.is_absolute()else ROOT/ip;assert head=='dba37ffaa78c82ade1385f7ee56c907ab0c67d3a'and filehash(ip)=='0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c'
 r=dict(passed=True,scope='Candidate integration/source bindings and current scientific prose; production promotion/checkpoint separate',accepted_source_sha256=acceptance['source_sha256'],shared_and_build_source_bindings=bindings,wrapper_sha256=wrappers,build_records_sha256=buildbind,PDFs=pdfs,baseline_commit=BASE,baseline_HTML_sha256=sha(b),candidate_HTML_sha256=sha(nb),old_literal_raw_MathML=7605,new_MathML=7891,all_old_raw_subtrees_preserved_ordered=True,old_tables_preserved=len(tables),iframe_subtrees_preserved=13,SVG_references_and_asset_bytes_preserved=28,inherited_arity_errors=bad(ot),new_malformed_nodes=0,new_labels_resolve=labels,unique_HTML_ids=len(ids),root_browser_receipt=qa,root_browser_sha256=filehash(ROOT/qa),documentation_record_sha256=filehash(ROOT/doc),documentation_source_sha256=docs['sha256'],B_v4_wording_only_delta_sha256=filehash(ROOT/latest),source_HEAD=head,source_index_sha256=filehash(ip),accepted_scientific_or_data_controls_rerun=False,production_edited=False,checker_sha256=filehash(Path(__file__)))
 with a.output.open('x')as f:json.dump(r,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in r.items()if k in ['passed','scope','old_literal_raw_MathML','new_MathML','old_tables_preserved','iframe_subtrees_preserved','SVG_references_and_asset_bytes_preserved','new_malformed_nodes','root_browser_sha256','checker_sha256']}))
if __name__=='__main__':main()
