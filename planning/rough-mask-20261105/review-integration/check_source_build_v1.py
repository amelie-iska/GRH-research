from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import argparse,ast,hashlib,json,re,subprocess,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
B=R/'outputs/checks/2026-11-05-rough-mask/root/integration-v1/before'
PUB=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-rough-mask')
BASE='a4de3a29927038bd30ec8b6814985b1e3574731b'
def git(*args):return subprocess.check_output(['git','-C',str(PUB),*args])
V=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-signed-divisor/outputs/publication/20261105-signed-divisor/site-bundle-v1/book')
a=argparse.ArgumentParser();a.add_argument('--native',required=True);a.add_argument('--output',required=True);a.add_argument('--expected-renderer',required=True);a.add_argument('--require-current-renderer',action='store_true');args=a.parse_args()
N=R/args.native;out=R/args.output;assert not out.exists()
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def load(p):return json.loads(Path(p).read_text())
def sourcepins(rec):
 return [pin(R/n) for n,s in rec['source_sha256'].items() if checksha(R/n,s)]
def checksha(p,s):assert sha(Path(p).read_bytes())==s,(str(p),s);return True
def subseq(x,y):
 i=0
 for t in y:
  if i<len(x) and t==x[i]:i+=1
 assert i==len(x),(i,len(x));return i
class H(HTMLParser):
 def __init__(self):super().__init__();self.svg=[];self.links=[];self.ids=[];self.workflow=[];self.embeds=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  for k in ['src','data']:
   if k in d and urlparse(d[k]).path.endswith('.svg'):self.svg.append((t,k,d[k],self.get_starttag_text()))
  if t=='a' and 'href' in d:self.links.append(d['href'])
  if t=='img' and d.get('src')=='figures/signed-divisor-workflow-.svg':self.workflow.append(d)
  if t=='embed':self.embeds.append(d)
old=(B/'web/book/main.html').read_text();new=(N/'book/main.html').read_text();prior=(V/'main.html').read_text();preservation={}
for tag,count in [('math',8176),('iframe',13),('table',386)]:
 pat=rf'<{tag}\b.*?</{tag}>';x=re.findall(pat,old,re.S);y=re.findall(pat,new,re.S);assert len(x)==count
 preservation[tag]={'prior_count':len(x),'new_count':len(y),'ordered_literal_matched':subseq(x,y),'old_join_sha256':sha('\n'.join(x).encode())}
assert preservation['math']['new_count']==8552 and preservation['iframe']['new_count']==13 and preservation['table']['new_count']==388
assert re.findall(r'<math\b.*?</math>',prior,re.S)==re.findall(r'<math\b.*?</math>',old,re.S)
x=H();x.feed(old);y=H();y.feed(new);assert len(x.svg)==len(y.svg)==29 and x.svg==y.svg
assert old.encode()==git('show',BASE+':web/book/main.html'),'Full source baseline differs from published main' 
assets=[]
for t,k,src,literal in x.svg:
 name=unquote(urlparse(src).path);ps=[R/'web/book'/name,N/'book'/name,V/name];data=[p.read_bytes() for p in ps];assert data[0]==data[1]==data[2]
 assets.append({'reference':src,'sha256':sha(data[0]),'bytes':len(data[0])})
assert len(y.workflow)==1 and y.workflow[0].get('alt') and not y.embeds
rma=[v for v in y.ids if v.startswith('rma:')];assert len(rma)==len(set(rma))==40
assert all(k in rma for k in ['rma:core','rma:details','rma:critical-error','rma:Stieltjes','rma:PIT-budget'])
for src in y.links:
 if 'rough-mask' in src and not urlparse(src).scheme:assert (N/'book'/unquote(urlparse(src).path)).exists(),src
canonical_path=R/'outputs/checks/2026-11-05-rough-mask/review/canonical-acceptance-v1.json';canonical=load(canonical_path);assert canonical['passed'] and sha(canonical_path.read_bytes())=='89fa533319df7095e213a87cc9cdf4c5a55d7be756ecf5dc49e25632374cf7e6'
canonicalcopies=[]
for part in ['core','details']:
 proposal=f'planning/rough-mask-20261105/canonical/rough-mask-{part}.tex';b=(R/proposal).read_bytes();assert sha(b)==canonical['canonical_sha256'][proposal]
 paper=R/f'papers/rough-mask-{part}.tex';book=R/f'book/chapters/rough-mask-{part}.tex';assert paper.read_bytes()==b and book.read_bytes()==b'% Generated shared reviewed material.\n'+b
 assert (N/f'book/sources/rough-mask-{part}.tex').read_bytes()==book.read_bytes();canonicalcopies.extend([pin(paper),pin(book)])
wrappers=[];bs=chr(92)
for n in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
 before=(B/f'papers/{n}.tex').read_text();last='signed-divisor-details' if n.endswith('extended') else 'signed-divisor-core';needle=bs+'input{'+last+'}';assert before.count(needle)==1
 ins=bs+'input{rough-mask-core}'+ ('\n'+bs+'input{rough-mask-details}' if n.endswith('extended') else '')
 expect=before.replace(needle,needle+'\n'+ins);marker='The arithmetic positive determinant comparison remains open;' if n.startswith('resolutions') else 'No proof of GRH or complete Lean formalization is asserted.';assert expect.count(marker)==1
 expect=expect.replace(marker,'An exact rough-prime support identity gives an explicit target-budget mask correction; the remaining coherent signed main term is still unestimated. '+marker);p=R/f'papers/{n}.tex';assert p.read_text()==expect;wrappers.append(pin(p))
p=R/'book/chapters/weighted-cutoff.tex';before=(B/'book/chapters/weighted-cutoff.tex').read_text();needle=bs+'input{chapters/signed-divisor-details}';assert before.count(needle)==1
assert p.read_text()==before.replace(needle,needle+'\n'+bs+'input{chapters/rough-mask-core}\n'+bs+'input{chapters/rough-mask-details}');weighted=pin(p)
p=R/'scripts/assemble_book.py';before=(B/'scripts/assemble_book.py').read_text();needle="'signed-divisor-core','signed-divisor-details']";assert before.count(needle)==1;assert p.read_text()==before.replace(needle,"'signed-divisor-core','signed-divisor-details','rough-mask-core','rough-mask-details']");assembler=pin(p)
ui_path=R/'outputs/checks/2026-11-05-signed-divisor/ui/frozen-receipt-v1.json';checksha(ui_path,'fc01825e94405855319246a18913201f8e026525fa6951f411cd8f2ee201e5a3');ui=load(ui_path);assert ui['passed'] and ui['frozen']
for n,m in ui['files'].items():checksha(R/n,m['sha256']);assert (R/n).stat().st_size==m['bytes']
fig_path=R/'outputs/checks/2026-11-05-signed-divisor/ui/figure-receipt-v1.json';fig=load(fig_path);assert fig['passed'];assert set(fig['files'])=={'book/figures/signed-divisor-workflow.pdf','book/figures/signed-divisor-workflow-.svg','book/figures/signed-divisor-workflow.tex'}
for n,m in fig['files'].items():
 checksha(R/n,m['sha256']);dest=N/'book/figures'/Path(n).name;assert dest.read_bytes()==(R/n).read_bytes()
figure_wrapper=R/'book/chapters/signed-divisor-figure.tex';assert bs+'label{sd:workflow}' in figure_wrapper.read_text();assert (N/'book/sources/signed-divisor-figure.tex').read_bytes()==figure_wrapper.read_bytes()
native_path=N/'native-build-record.json';native=load(native_path);assert native['passed'] and native['renderer_sha256']==args.expected_renderer;assert native['new_HTML_sha256']==sha(new.encode()) and native['math_nodes']==3196 and native['explicit_labels']==156 and native['raw_TeX_nodes']==native['conversion_warnings']==0
renderer=N/'render_native.py';checksha(renderer,args.expected_renderer);current=R/'planning/book-integration-20261104/render_native.py';currentmatch=sha(current.read_bytes())==args.expected_renderer
if args.require_current_renderer:assert currentmatch
assert renderer.read_bytes()==git('show',BASE+':planning/book-integration-20261104/render_native.py'), 'Unexpected new renderer/runtime change'
assert (N/'book/reviewed-math-scroll.js').read_bytes()==git('show',BASE+':web/book/reviewed-math-scroll.js')
# Every old book leaf stays exact except the rebuilt main and explicitly integrated weighted wrapper.
baseleaves={}
for row in git('ls-tree','-rz',BASE,'--','web/book').split(b'\0'):
 if not row:continue
 meta,name=row.split(b'\t',1);mode,typ,oid=meta.decode().split();assert typ=='blob';name=name.decode();assert name.startswith('web/book/');baseleaves[name[9:]]=(mode,oid)
newleaves={p.relative_to(N/'book').as_posix()for p in (N/'book').rglob('*')if p.is_file()}
assert newleaves-set(baseleaves)=={'sources/rough-mask-core.tex','sources/rough-mask-details.tex'} and set(baseleaves)<=newleaves
for rel,(mode,oid)in baseleaves.items():
 assert mode=='100644'
 if rel in ['main.html','sources/weighted-cutoff.tex']:continue
 b=(N/'book'/rel).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==oid,rel
nativepins=sourcepins(native)
pdf_path=R/'outputs/rough-mask-book-20261105/v1/pdf/build-record.json';pdf=load(pdf_path);assert pdf['passed'] and pdf['pdf_pages']==288;bookpdf=pdf_path.parent/'main.pdf';checksha(bookpdf,pdf['pdf_sha256']);pdfpins=sourcepins(pdf)
def pages(p):return int(re.search(r'^Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',str(p)],text=True),re.M)[1])
assert pages(bookpdf)==288
article_path=R/'outputs/checks/2026-11-05-rough-mask/builds/build-acceptance-v1.json';article=load(article_path);checksha(article_path,'052e9e424c3cf9c763643a9470e58e33163ed665c7d8a2902610f52661311acf');assert article['passed'];articles=[]
for ed,pg in [('concise-v1',67),('extended-v1',183),('notes-concise-v1',25),('notes-extended-v1',74)]:
 p=R/f'outputs/rough-mask-articles-20261105/{ed}/build-record.json';j=load(p);assert j['passed'];checksha(p,article['build_records'][ed]['sha256']);ps=[x for x in p.parent.glob('*.pdf') if sha(x.read_bytes())==j['pdf_sha256']];assert len(ps)==1 and pages(ps[0])==pg==j.get('pages',j.get('pdf_pages'));sp=sourcepins(j);articles.append({'edition':ed,'record':pin(p),'pdf':pin(ps[0]),'pages':pg,'recursive_source_pins':sp})
record={'schema':'rough-mask-independent-source-build-preservation-v1','passed':True,'accepted_scope':'Source/build/preservation checks only; responsive/native QA and final administrative metadata are separate gates','promotion_authorized_by_this_receipt':False,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_record':pin(native_path),'native_HTML':pin(N/'book/main.html'),'renderer':pin(renderer),'renderer_current_matches':currentmatch,'baseline_HTML':pin(B/'web/book/main.html'),'prior_published_HTML':pin(V/'main.html'),'preservation':preservation,'old_svg_reference_order_literal_exact':True,'no_new_diagram_or_runtime':True,'all_old_book_leaves_preserved_except_explicit_main_and_weighted_wrapper':True,'old_svg_assets':assets,'existing_accessible_source_bound_figure_unchanged':True,'new_rma_labels':rma,'canonical_acceptance':pin(canonical_path),'canonical_copies':canonicalcopies,'four_wrapper_exact_bounded_diffs':wrappers,'weighted_wrapper':weighted,'assembler':assembler,'figure_wrapper':pin(figure_wrapper),'figure_receipt':pin(fig_path),'UI_receipt':pin(ui_path),'book_PDF_record':pin(pdf_path),'book_PDF':pin(bookpdf),'book_PDF_source_pins':pdfpins,'native_source_pins':nativepins,'article_acceptance':pin(article_path),'articles':articles,'checker':pin(Path(__file__)),'reviewer_harness_diagnostic':pin(R/'outputs/checks/2026-11-05-rough-mask/main-attempt/finite-reviewer-schema-diagnostic-v1.json'),'metadata_ready_claimed':False,'browser_or_scientific_runs':False,'source_or_existing_artifacts_edited':False}
record['new_proof_data_pins']={k:pin(R/v)for k,v in {'finite':'outputs/checks/2026-11-05-rough-mask/main-attempt/finite-data-acceptance-v1.json','projection':'web/data/rough-mask-controls.json','PIT':'outputs/checks/2026-11-05-rough-mask/root/pit-review-v1.json','primary_public_citation':'outputs/checks/2026-11-05-rough-mask/main-attempt/PUBLIC-CITATION-v1.json'}.items()}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');print(json.dumps({'passed':True,'output':str(out),'sha256':sha(out.read_bytes()),'preservation':preservation,'renderer_current_matches':currentmatch,'metadata_ready':False},indent=2))
