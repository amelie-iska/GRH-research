from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import argparse,ast,hashlib,json,re,subprocess,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
B=R/'outputs/checks/2026-11-05-signed-divisor/root/integration-v1/before'
V=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-signed-weights/outputs/publication/20261105-signed-weights/site-bundle-v1/book')
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
for tag,count in [('math',7891),('iframe',13),('table',385)]:
 pat=rf'<{tag}\b.*?</{tag}>';x=re.findall(pat,old,re.S);y=re.findall(pat,new,re.S);assert len(x)==count
 preservation[tag]={'prior_count':len(x),'new_count':len(y),'ordered_literal_matched':subseq(x,y),'old_join_sha256':sha('\n'.join(x).encode())}
assert preservation['math']['new_count']==8176 and preservation['iframe']['new_count']==13 and preservation['table']['new_count']==386
assert re.findall(r'<math\b.*?</math>',prior,re.S)==re.findall(r'<math\b.*?</math>',old,re.S)
x=H();x.feed(old);y=H();y.feed(new);assert len(x.svg)==28 and len(y.svg)==29 and x.svg==y.svg[:28]
assets=[]
for t,k,src,literal in x.svg:
 name=unquote(urlparse(src).path);ps=[R/'web/book'/name,N/'book'/name,V/name];data=[p.read_bytes() for p in ps];assert data[0]==data[1]==data[2]
 assets.append({'reference':src,'sha256':sha(data[0]),'bytes':len(data[0])})
assert len(y.workflow)==1 and y.workflow[0].get('alt') and not y.embeds
sd=[s for s in y.ids if s.startswith('sd:')];assert len(sd)==len(set(sd))==19 and all(k in sd for k in ['sd:core','sd:details','sd:workflow'])
for src in y.links:
 if 'signed-divisor' in src and not urlparse(src).scheme:assert (N/'book'/unquote(urlparse(src).path)).exists(),src
canonical=load(R/'outputs/checks/2026-11-05-signed-divisor/review-design/canonical-acceptance-v1.json');assert canonical['passed']
canonicalcopies=[]
for part,key in [('core','core'),('details','details_v4')]:
 b=Path(canonical['inputs'][key]['path']).read_bytes();paper=R/f'papers/signed-divisor-{part}.tex';book=R/f'book/chapters/signed-divisor-{part}.tex'
 assert paper.read_bytes()==b and book.read_bytes()==b'% Generated shared reviewed material.\n'+b
 assert (N/f'book/sources/signed-divisor-{part}.tex').read_bytes()==book.read_bytes()
 canonicalcopies.extend([pin(paper),pin(book)])
wrappers=[];bs=chr(92)
for n in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
 before=(B/f'papers/{n}.tex').read_text();last='signed-weights-details' if n.endswith('extended') else 'signed-weights-core';needle=bs+'input{'+last+'}';assert before.count(needle)==1
 ins=bs+'input{signed-divisor-core}'+ ('\n'+bs+'input{signed-divisor-details}' if n.endswith('extended') else '')
 expect=before.replace(needle,needle+'\n'+ins);marker='The arithmetic positive determinant comparison remains open;' if n.startswith('resolutions') else 'No proof of GRH or complete Lean formalization is asserted.';assert expect.count(marker)==1
 expect=expect.replace(marker,'A signed common-divisor zeta expansion and a complete-column exact laboratory retain every raw mask; weighted divisor certificates do not close the required asymptotic saving. '+marker);p=R/f'papers/{n}.tex';assert p.read_text()==expect;wrappers.append(pin(p))
p=R/'book/chapters/weighted-cutoff.tex';assert p.read_text()==(B/'book/chapters/weighted-cutoff.tex').read_text()+bs+'input{chapters/signed-divisor-core}\n'+bs+'input{chapters/signed-divisor-figure}\n'+bs+'input{chapters/signed-divisor-details}\n';weighted=pin(p)
p=R/'scripts/assemble_book.py';before=(B/'scripts/assemble_book.py').read_text();needle="'signed-weights-core','signed-weights-details'";assert before.count(needle)==1;assert p.read_text()==before.replace(needle,needle+",'signed-divisor-core','signed-divisor-details'");assembler=pin(p)
ui_path=R/'outputs/checks/2026-11-05-signed-divisor/ui/frozen-receipt-v1.json';checksha(ui_path,'fc01825e94405855319246a18913201f8e026525fa6951f411cd8f2ee201e5a3');ui=load(ui_path);assert ui['passed'] and ui['frozen']
for n,m in ui['files'].items():checksha(R/n,m['sha256']);assert (R/n).stat().st_size==m['bytes']
fig_path=R/'outputs/checks/2026-11-05-signed-divisor/ui/figure-receipt-v1.json';fig=load(fig_path);assert fig['passed'];assert set(fig['files'])=={'book/figures/signed-divisor-workflow.pdf','book/figures/signed-divisor-workflow-.svg','book/figures/signed-divisor-workflow.tex'}
for n,m in fig['files'].items():
 checksha(R/n,m['sha256']);dest=N/'book/figures'/Path(n).name;assert dest.read_bytes()==(R/n).read_bytes()
figure_wrapper=R/'book/chapters/signed-divisor-figure.tex';assert bs+'label{sd:workflow}' in figure_wrapper.read_text();assert (N/'book/sources/signed-divisor-figure.tex').read_bytes()==figure_wrapper.read_bytes()
native_path=N/'native-build-record.json';native=load(native_path);assert native['passed'] and native['renderer_sha256']==args.expected_renderer;assert native['new_HTML_sha256']==sha(new.encode()) and native['math_nodes']==2820 and native['explicit_labels']==116 and native['raw_TeX_nodes']==native['conversion_warnings']==0
renderer=N/'render_native.py';checksha(renderer,args.expected_renderer);current=R/'planning/book-integration-20261104/render_native.py';currentmatch=sha(current.read_bytes())==args.expected_renderer
if args.require_current_renderer:assert currentmatch
oldrenderer=B/'planning/book-integration-20261104/render_native.py'
def assertions(p):return [ast.dump(n,include_attributes=False) for n in sorted([n for n in ast.walk(ast.parse(p.read_text())) if isinstance(n,ast.Assert)],key=lambda n:n.lineno)]
aa=assertions(oldrenderer);bb=assertions(renderer);assert subseq(aa,bb)==35
nativepins=sourcepins(native)
pdf_path=R/'outputs/signed-divisor-book-20261105/v1/pdf/build-record.json';pdf=load(pdf_path);assert pdf['passed'] and pdf['pdf_pages']==279;bookpdf=pdf_path.parent/'main.pdf';checksha(bookpdf,pdf['pdf_sha256']);pdfpins=sourcepins(pdf)
def pages(p):return int(re.search(r'^Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',str(p)],text=True),re.M)[1])
assert pages(bookpdf)==279
article_path=R/'outputs/checks/2026-11-05-signed-divisor/analytic/article-builds-v1/build-acceptance-v1.json';article=load(article_path);checksha(article_path,'5af508bc883701a0b96b7ad690e9a1ad680a180e34f6b10ed58a44fa259d77e3');assert article['passed'];articles=[]
for ed,pg in [('concise-v1',64),('extended-v1',175),('notes-concise-v1',23),('notes-extended-v1',66)]:
 p=R/f'outputs/signed-divisor-articles-20261105/{ed}/build-record.json';j=load(p);assert j['passed'];checksha(p,article['build_records'][ed]['sha256']);ps=[x for x in p.parent.glob('*.pdf') if sha(x.read_bytes())==j['pdf_sha256']];assert len(ps)==1 and pages(ps[0])==pg==j.get('pages',j.get('pdf_pages'));sp=sourcepins(j);articles.append({'edition':ed,'record':pin(p),'pdf':pin(ps[0]),'pages':pg,'recursive_source_pins':sp})
record={'schema':'signed-divisor-independent-source-build-preservation-v1','passed':True,'accepted_scope':'Source/build/preservation checks only; responsive/native QA and final administrative metadata are separate gates','promotion_authorized_by_this_receipt':False,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_record':pin(native_path),'native_HTML':pin(N/'book/main.html'),'renderer':pin(renderer),'renderer_current_matches':currentmatch,'baseline_HTML':pin(B/'web/book/main.html'),'prior_published_HTML':pin(V/'main.html'),'preservation':preservation,'old_svg_reference_order_literal_exact':True,'old_svg_assets':assets,'one_new_accessible_source_bound_figure':True,'old_renderer_assertions_retained':35,'new_renderer_assertions':len(bb),'new_sd_labels':sd,'canonical_acceptance':pin(R/'outputs/checks/2026-11-05-signed-divisor/review-design/canonical-acceptance-v1.json'),'canonical_copies':canonicalcopies,'four_wrapper_exact_bounded_diffs':wrappers,'weighted_wrapper':weighted,'assembler':assembler,'figure_wrapper':pin(figure_wrapper),'figure_receipt':pin(fig_path),'UI_receipt':pin(ui_path),'book_PDF_record':pin(pdf_path),'book_PDF':pin(bookpdf),'book_PDF_source_pins':pdfpins,'native_source_pins':nativepins,'article_acceptance':pin(article_path),'articles':articles,'checker':pin(Path(__file__)),'reviewer_harness_diagnostic':pin(R/'outputs/checks/2026-11-05-signed-divisor/review-integration/harness-diagnostic-v1.json'),'metadata_ready_claimed':False,'browser_or_scientific_runs':False,'source_or_existing_artifacts_edited':False}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');print(json.dumps({'passed':True,'output':str(out),'sha256':sha(out.read_bytes()),'preservation':preservation,'renderer_current_matches':currentmatch,'metadata_ready':False},indent=2))
