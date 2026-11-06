#!/usr/bin/env python3
"""Independent current-source/artifact preservation review. No builds/browser/auth."""
from pathlib import Path
import json,hashlib,re,subprocess,xml.etree.ElementTree as ET,datetime
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlsplit
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
C=R/'outputs/checks/2026-11-05-physical-sieve';BOOK=R/'outputs/physical-sieve-book-20261105/v3'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def pin(p):return {'path':str(Path(p).relative_to(R)),'sha256':sha(p)}
def textsha(s):return hashlib.sha256(s.encode()).hexdigest()
def binding(mapping):
 assert all(sha(R/p)==h for p,h in mapping.items())
 return len(mapping)
def expand(path,base,stack=()):
 path=Path(path).resolve();assert path not in stack
 def replace(m):
  name=m[1] if m[1].endswith('.tex') else m[1]+'.tex'
  return expand(base/name,base,stack+(path,))
 return re.sub(r'\\input\{([^}]+)\}',replace,path.read_text())
def pdfcheck(p,pages,markers):
 info=subprocess.run(['pdfinfo',str(p)],check=True,capture_output=True,text=True).stdout
 got=int(re.search(r'^Pages:\s*(\d+)',info,re.M)[1]);assert got==pages,(p,got,pages)
 t=subprocess.run(['pdftotext',str(p),'-'],check=True,capture_output=True,text=True).stdout
 t=' '.join(t.split());assert all(m in t for m in markers),(p,[m for m in markers if m not in t])
 return got
def logcheck(p):
 s=p.read_text(errors='replace')
 pats=[r'Overfull',r'Undefined control sequence',r'There were undefined references',r'multiply[- ]defined',r'multiply defined',r'Missing character',r'! LaTeX Error',r'Fatal error']
 bad=[x for x in pats if re.search(x,s,re.I)];assert not bad,(p,bad)
 return {'sha256':sha(p),'underfull':s.count('Underfull'),'warnings':[l for l in s.splitlines() if 'Warning:' in l],'bad_diagnostics':[]}
gate=C/'review/canonical-acceptance-v3.json';G=load(gate);assert G['passed'];assert sha(gate)=='f33b0b49137b938f7923fc84ffeea385d90bfbf5959b2a10488ad5920dc61168';binding(G['canonical_sha256'])
source=C/'root/integration-v1/source-integration-v3.json';S=load(source);assert S['passed'] and S['canonical_acceptance_sha256']==sha(gate);assert binding(S['changed_source_sha256'])==14
producer=C/'review-integration-a/producer-source-acceptance-v1.json';assert load(producer)['passed']
four=C/'builds/four-builds-v2.json';F=load(four);assert F['passed'];assert sha(four)=='a67a4fc6264630fa0cd81c6cd2ef002ee3bd80acdc824bf422bdb82f3df4923a';assert F['canonical_layout_acceptance_sha256']==sha(gate);binding(F['final_canonical_guard_sha256'])
names=['coherent-main-core','coherent-main-details','physical-sieve-core','physical-sieve-details'];copies={};canon={}
for n in names:
 q=R/'planning/physical-sieve-20261105/canonical'/(n+'.tex');b=R/'book/chapters'/(n+'.tex');p=R/'papers'/(n+'.tex');a=q.read_bytes();assert p.read_bytes()==a and b.read_bytes()==b'% Generated shared reviewed material.\n'+a;copies[n]={'canonical':sha(q),'paper':sha(p),'book':sha(b)};canon[n]=q.read_text()
builds={};allrecords={};actual_count=0
for name,x in F['builds'].items():
 rp=R/x['build_record'];rec=load(rp);assert rec['passed'] and sha(rp)==x['build_record_sha256'];actual=F['actual_compiled_inputs_by_build'][name];assert rec['source_sha256']==actual;actual_count+=binding(actual)
 pdf=R/x['pdf'];assert sha(pdf)==x['pdf_sha256']==rec['pdf_sha256'];pages=pdfcheck(pdf,x['pages'],x['PDF_markers']);log=pdf.with_suffix('.log');assert sha(log)==x['log_sha256'];checks=logcheck(log);assert checks['underfull']==x['underfull_count'];assert not x['new_warning_lines'] and not x['bad_log_lines']
 ex=pdf.with_suffix('.expanded.tex');assert sha(ex)==x['expanded_source_sha256'];wrapper=R/'papers'/(pdf.stem+'.tex');original=expand(wrapper,R/'papers');assert textsha(original)==x['current_original_expanded_source_sha256']
 originalfile=ex if name.startswith('notes-') else pdf.parent/'expanded-original.tex';assert originalfile.read_text()==original
 included=[n for n in names if n.endswith('core') or name.startswith('extended') or name.startswith('notes-extended')]
 compiled=ex.read_text();assert all(canon[n] in compiled for n in included)
 builds[name]={'record':pin(rp),'PDF':pin(pdf),'pages':pages,'log':checks,'expanded_source_sha256':sha(ex),'independent_current_original_expansion_sha256':textsha(original),'actual_input_count':len(actual),'actual_input_pins_current':True,'current_included_new_fragments':included};allrecords[str(rp.relative_to(R))]=sha(rp)
assert sorted(x['pages'] for x in builds.values())==[29,71,89,200]
# The only stale guard is explicitly unused by the concise compiled input.
unused=F['unused_historical_guard_metadata'];assert len(unused)==1
for x in unused:
 assert not x['actually_compiled'] and x['path'] not in F['actual_compiled_inputs_by_build'][x['build']];assert sha(R/x['path'])==x['current_sha256'];assert x['historical_guard_sha256']!=x['current_sha256']
bookrecord=BOOK/'pdf/build-record.json';BR=load(bookrecord);assert BR['passed'];bookbindings=binding(BR['source_sha256']);pdf=BOOK/'pdf/main.pdf';assert sha(pdf)==BR['pdf_sha256'];assert pdfcheck(pdf,303,['The coherent signed main and its remaining inputs','A sieve comparison indexed by the physical radicand','Proofs for the coherent main reductions'])==303
booklog=logcheck(BOOK/'pdf/main.log');oldbook=R/'outputs/rough-mask-book-20261105/v1/pdf/build-record.json';OB=load(oldbook);oldlog=logcheck(oldbook.parent/'main.log');assert booklog['underfull']==oldlog['underfull']==8;assert Counter(booklog['warnings'])==Counter(oldlog['warnings'])
original=expand(R/'book/main.tex',R/'book');assert textsha(original)==BR['original_expanded_source_sha256'];assert (BOOK/'pdf/source-expansion-before-diagram-replacement.tex').read_text()==original
assert all(canon[n] in (BOOK/'pdf/main.tex').read_text() for n in names)
allrecords[str(bookrecord.relative_to(R))]=sha(bookrecord)
nativerecord=BOOK/'native/native-build-record.json';NR=load(nativerecord);assert NR['passed'];nativebindings=binding(NR['source_sha256']);assert NR['raw_TeX_nodes']==NR['conversion_warnings']==0;assert (BOOK/'native/conversion.log').stat().st_size==0
oldhtml=C/'root/integration-v1/before/web/book/main.html';newhtml=BOOK/'native/book/main.html';a=oldhtml.read_text();b=newhtml.read_text();assert sha(newhtml)==NR['new_HTML_sha256']
def raw(s,tag):return re.findall(r'<'+tag+r'\b[^>]*>[\s\S]*?</'+tag+r'>',s)
preservation={}
for tag,oldn,newn in [('math',8552,9172),('table',388,389),('iframe',13,13)]:
 x=raw(a,tag);y=raw(b,tag);assert len(x)==oldn and len(y)==newn;at=0;positions=[]
 for z in x:
  while at<len(y) and y[at]!=z:at+=1
  assert at<len(y),(tag,len(positions));positions.append(at);at+=1
 preservation[tag]={'old_count':len(x),'new_count':len(y),'old_literal_subtrees_byte_identical_in_order':True,'old_concatenated_sha256':textsha(''.join(x)),'matched_positions_sha256':textsha(json.dumps(positions))}
def malformed(s):
 bad=Counter();errors=[]
 for no,x in enumerate(raw(s,'math')):
  try:e=ET.fromstring(x)
  except ET.ParseError as ex:errors.append((no,str(ex)));continue
  for z in e.iter():
   t=z.tag.rsplit('}',1)[-1];n={'munder':2,'mover':2,'munderover':3,'msub':2,'msup':2,'msubsup':3,'mfrac':2,'mroot':2}.get(t)
   if n and len(z)!=n:bad[(t,len(z),hashlib.sha256(ET.tostring(z)).hexdigest())]+=1
 return bad,errors
bad0,err0=malformed(a);bad1,err1=malformed(b);assert not err0 and not err1 and bad1==bad0 and sum(bad1.values())==3
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.frames=[];self.svg=[];self.ids=Counter()
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids[d['id']]+=1
  if t=='iframe':self.frames.append(d.get('src'))
  if t in ('img','object','embed','image'):
   for k in ('src','data','href','xlink:href'):
    if d.get(k) and urlsplit(d[k]).path.endswith('.svg'):self.svg.append((t,k,d[k]))
pa=HTML();pa.feed(a);pb=HTML();pb.feed(b);assert pa.frames==pb.frames and len(pb.frames)==len(set(pb.frames))==13;assert pa.svg==pb.svg and len(pb.svg)==29;assert not [(k,v) for k,v in pb.ids.items() if v>max(pa.ids.get(k,0),1)]
labels=[l for n in names for l in re.findall(r'\\label\{([^}]+)\}',canon[n])];assert len(labels)==51 and all(pb.ids[x]==1 for x in labels)
for n in names:assert (BOOK/'native/book/sources'/(n+'.tex')).read_bytes()==(R/'book/chapters'/(n+'.tex')).read_bytes()
allrecords[str(nativerecord.relative_to(R))]=sha(nativerecord);assert len(allrecords)==6
# Actual old/new cache methods; one SVG fallback has regenerated PDF bytes.
assert OB['diagram_cache_reads']==BR['diagram_cache_reads']==18;assert OB['diagram_asset_mode']==BR['diagram_asset_mode']=='preserved-PDF-cache-with-accepted-SVG-fallback';assert len(OB['diagram_records'])==len(BR['diagram_records'])==19
for x,y in zip(OB['diagram_records'],BR['diagram_records']):assert {k:v for k,v in x.items() if k!='pdf_sha256'}=={k:v for k,v in y.items() if k!='pdf_sha256'}
different=[i for i,(x,y) in enumerate(zip(OB['diagram_records'],BR['diagram_records'])) if x!=y];assert different==[15]
cache=C/'review-integration/cache-comparison-v1/comparison-v1.json';CR=load(cache);assert CR['passed'] and CR['rendered_PNG_bytes_identical']
auxpaths=[C/'root/native-qa-v1/browser.json',C/'root/visual-v1/root-inspection-v1.json',C/'ui/frozen-receipt-v1.json'];aux={}
for p in auxpaths:
 j=load(p);assert j['passed'];aux[str(p.relative_to(R))]=sha(p)
QA=load(auxpaths[0]);assert QA['state']['math']==9172 and QA['state']['iframes']==13 and not QA['pageErrors'];assert QA['inheritedMathMLDiagnostics']['newMalformedMunderNodes']==0
UI=load(auxpaths[2]);binding(UI['candidate_source_sha256'])
for k in ('numeric_model_acceptance','static_caption_addendum','browser'):
 x=UI[k];assert sha(R/x['path'])==x['sha256'] and load(R/x['path'])['passed']
pins=load(R/'planning/prime-fibre-20261105/lane-a/source-pins-v1.json');binding(pins['source_sha256']);now={}
for chunk in subprocess.check_output(['git','worktree','list','--porcelain'],text=True).strip().split('\n\n'):
 z=dict(l.split(' ',1) for l in chunk.splitlines() if ' ' in l);p=Path(z['worktree']);i=Path(subprocess.check_output(['git','-C',str(p),'rev-parse','--git-path','index'],text=True).strip());i=i if i.is_absolute() else p/i;now[str(p)]={'path':str(p),'HEAD':z['HEAD'],'index_sha256':sha(i)}
assert all(now.get(x['path'])==x for x in pins['protected_states'])
result={'passed':True,'schema':'physical-sieve-independent-integration-acceptance-v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':pin(__file__),'source_proof_gate':pin(gate),'source_integration':pin(source),'producer_document_source_acceptance':pin(producer),'governing_four_PDFs':pin(four),'six_build_records_sha256':allrecords,'four_current_canonical_paper_book_copies':copies,'four_article_note_build_checks':builds,'actual_article_note_source_binding_entries_verified':actual_count,'unused_historical_guard_disclosure':unused,'book':{'PDF':pin(pdf),'pages':303,'PDF_record_source_bindings':bookbindings,'native_record_source_bindings':nativebindings,'current_original_expanded_source_sha256':textsha(original),'final_log':booklog,'old_log_diagnostics_unchanged':True,'native':pin(newhtml),'full_current_math_count':9172,'renderer_supplement_math_count':NR['math_nodes'],'renderer_internal_baseline_math_count':NR['preservation']['math']['old_count'],'acceptance_baseline_is_current_8552_not_renderer_ancient_5356':True},'current_delivery_preservation':{'baseline':pin(oldhtml),'candidate':pin(newhtml),'subtrees':preservation,'canonical_iframes':13,'SVG_refs':29,'iframe_and_SVG_sequences_unchanged':True,'new_labels_present_once':51,'no_new_duplicate_ids':True,'XML_parse_errors':0,'old_malformed_munder_nodes':3,'new_malformed_fixedarity_nodes':0,'malformed_signatures_unchanged':[{'tag':k[0],'children':k[1],'serialized_sha256':k[2],'count':v} for k,v in bad1.items()],'four_new_native_downloads_match_accepted_book_prefix_copies':True,'conversion_warnings':0,'raw_TeX_nodes':0},'diagram_cache':{'prior_record':pin(oldbook),'current_record':pin(bookrecord),'old_and_new_preserved_PDF_reads':18,'old_and_new_diagram_records':19,'all19_source_SVG_method_trim_records_unchanged':True,'fallback_index':15,'fallback_PDF_bytes_regenerated':True,'fallback_same_render_comparison':pin(cache),'same_render_at_DPI':72,'no_new_cache_loss_claim':True,'inherited_PDF_searchability_and_public_SVG_reproduction_limits_retained':True},'bound_root_browser_visual_UI_records_sha256':aux,'all_old11_HEAD_index_states_and_old_scientific_sources_unchanged':True,'scientific_scope':'External de Faveri v1 theorem application gives current unsigned9/8 and scoped A6=1 signed/combined13/12 upper bounds. Full coherent means/masks/endpoints and hypothetical scalar-input qualifications retained; no target/GRH/Lean/new-sieve conclusion.','limitations':['No compilation, browser, author numeric control, old scientific table or publication/auth action was rerun by this checker.','Independent current input expansion/PDF metadata/text/log/source hashes and literal HTML preservation were checked; visual/browser gates are the separately source-bound root records.','This is pre-promotion acceptance; production artifact promotion and public publication are separate root actions.']}
p=C/'review-integration/integration-acceptance-v1.json'
with p.open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'passed':True,'receipt':str(p.relative_to(R)),'sha256':sha(p),'full_MathML':9172,'old_math_preserved':8552,'old_tables_preserved':388,'new_tables':389,'PDF_pages':[303,71,200,29,89],'cache_reads':18,'diagrams':19,'all_old11_states_unchanged':True},sort_keys=True))
