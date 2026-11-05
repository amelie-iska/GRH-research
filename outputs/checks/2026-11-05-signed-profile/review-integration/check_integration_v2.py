from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json,hashlib,subprocess,csv,datetime,xml.etree.ElementTree as ET
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');O=Path(__file__).resolve().parent
B=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-arithmetic-learning/outputs/publication/20261105-arithmetic-learning/site-bundle-v3')
sha=lambda b:hashlib.sha256(b).hexdigest()
inputs={};checks=[]
def data(p):
 p=Path(p);p=p if p.is_absolute() else R/p;b=p.read_bytes();inputs[str(p)]=sha(b);return b
def text(p):return data(p).decode()
def obj(p):return json.loads(text(p))
def ck(name,ok,**details):checks.append(dict(name=name,passed=bool(ok),**details))
oldp='outputs/checks/2026-11-05-signed-profile/root/before/web/book/main.html';newp='web/book/main.html'
old=text(oldp);new=text(newp);publicold=text(B/'book/main.html')
math=lambda s:re.findall(r'<math\b.*?</math>',s,re.S)
a,b,c=map(math,[old,new,publicold]);matches=[];at=0
for i,v in enumerate(b):
 if at<len(a) and a[at]==v:matches.append(i);at+=1
ck('raw MathML ordered byte preservation',len(a)==7352 and len(b)==7605 and at==len(a),old=len(a),new=len(b),matched=at,old_raw_sequence_sha256=sha('\n'.join(a).encode()),new_raw_sequence_sha256=sha('\n'.join(b).encode()),matched_new_indices=matches)
ck('previous public bundle MathML matches production before',a==c,previous_public_math=len(c))
frames=lambda s:re.findall(r'<iframe\b.*?</iframe>',s,re.S)
f0,f1,f2=map(frames,[old,new,publicold]);ck('13 complete iframe elements unchanged',len(f0)==13 and f0==f1,count=len(f1),sequence_sha256=sha('\n'.join(f1).encode()))
ck('previous public iframe differences are prefix-only',f0==[f.replace('src="/GRH-research/', 'src="/') for f in f2],normalization='Only iframe src /GRH-research/ is mapped back to source-root /. Complete element bytes otherwise match.')
svg=lambda s:re.findall(r'<img\b[^>]*?src="([^"]+\.svg)"',s)
s0,s1,s2=map(svg,[old,new,publicold]);ck('28 SVG references in identical order',len(s0)==28 and s0==s1==s2,count=len(s1),references=s1)
assets=[]
for path in s1:
 oldbytes=data(B/'book'/path);now=data(R/'web/book'/path);candidate=data(R/'outputs/profile-uniformity-book-20261105/v3/native/book'/path)
 assets.append(dict(reference=path,sha256=sha(now),matches_previous_public_bundle=now==oldbytes,matches_accepted_candidate=now==candidate))
ck('SVG assets unchanged from independent previous publication',all(x['matches_previous_public_bundle'] and x['matches_accepted_candidate'] for x in assets),assets=assets)
malformed=[]
for i,m in enumerate(b):
 root=ET.fromstring(m)
 for n in root.iter():
  if n.tag.rsplit('}',1)[-1]=='munder' and len(n)!=2:malformed.append(i)
ck('no new malformed munder nodes',len(malformed)==3 and all(i in matches for i in malformed),inherited_indices=malformed)
accept=obj('outputs/checks/2026-11-05-signed-profile/review-production/acceptance-v1.json')
ck('independent B proof acceptance',accept['passed'] is True and accept['verdict']=='PASS')
parts={}
for part in ['core','details']:
 p=f'papers/profile-uniformity-{part}.tex';v=data(p);parts[part]=v.decode();expected=accept['source_sha256'][p]
 ck('B accepted canonical '+part,sha(v)==expected,sha256=sha(v))
 for prefix in ['book/chapters/','web/book/sources/']:
  q=prefix+f'profile-uniformity-{part}.tex';bv=data(q)
  ck(prefix+part+' exact shared copy',bv==b'% Generated shared reviewed material.\n'+v,sha256=sha(bv))
records=[('concise-v1','resolutions-concise','outputs/papers',61,False),('extended-v2','resolutions-extended','outputs/papers',162,True),('notes-concise-v1','validated-oracle-concise','outputs/papers/validated-oracle-20261104',19,False),('notes-extended-v2','validated-oracle-extended','outputs/papers/validated-oracle-20261104',53,True)]
for edition,stem,target,pages,extended in records:
 base=Path('outputs/profile-uniformity-articles-20261105')/edition;rec=obj(base/'build-record.json');wrapper=f'papers/{stem}.tex';w=text(wrapper)
 mismatches=[p for p,h in rec['source_sha256'].items() if sha(data(p))!=h]
 exp=text(base/(stem+'.expanded.tex'));pdf=Path(target)/(stem+'.pdf');pb=data(pdf)
 actualpages=int(re.search(r'^Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',str(R/pdf)],text=True),re.M).group(1))
 ck(edition+' all recorded sources bound',rec['passed'] and not mismatches and wrapper in rec['source_sha256'],source_count=len(rec['source_sha256']),mismatches=mismatches)
 ck(edition+' correct canonical expansion',parts['core'] in exp and (parts['details'] in exp)==extended and '\\input{profile-uniformity-core}' in w and ('\\input{profile-uniformity-details}' in w)==extended)
 ck(edition+' promoted PDF exact and page count',sha(pb)==rec['pdf_sha256'] and pb==data(base/(stem+'.pdf')) and actualpages==pages,pages=actualpages,pdf_sha256=sha(pb))
bookrec=obj('outputs/profile-uniformity-book-20261105/v3/pdf/build-record.json');mismatch=[p for p,h in bookrec['source_sha256'].items() if sha(data(p))!=h]
pdf=Path('outputs/book/surface-orders-book.pdf');pb=data(pdf);actualpages=int(re.search(r'^Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',str(R/pdf)],text=True),re.M).group(1))
ck('book promoted PDF exact and 266 pages',bookrec['passed'] and actualpages==266 and sha(pb)==bookrec['pdf_sha256'] and not mismatch,pages=actualpages,source_count=len(bookrec['source_sha256']),mismatches=mismatch)
ck('promoted native equals final candidate',data(newp)==data('outputs/profile-uniformity-book-20261105/v3/native/book/main.html'))
class H(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  for k in ['id','name']:
   if k in d:self.ids.add(d[k])
  for k in ['href','src','data-source']:
   if k in d:self.refs.append((t,k,d[k]))
def html(s):p=H();p.feed(s);return p
nh=html(new);oh=html(old)
def missing_refs(source,parsed):
 missing=[];checked=0
 for tag,attr,ref in parsed.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  if not path:
   if u.fragment and unquote(u.fragment) not in parsed.ids:missing.append((ref,'fragment'))
   checked+=1;continue
  if path.startswith('/GRH-research/'):path=path[len('/GRH-research'):]
  if path.startswith('/'):
   q=R/'web'/path.lstrip('/')
   if not q.exists():q=R/path.lstrip('/')
  else:q=(R/source).parent/path
  if q.is_dir():q=q/'index.html'
  if not q.exists():missing.append((ref,'file'))
  elif u.fragment and q.suffix=='.html':
   qh=html(text(q))
   if unquote(u.fragment) not in qh.ids:missing.append((ref,'fragment'))
  checked+=1
 return checked,missing
ncount,nmissing=missing_refs('web/book/main.html',nh);ocount,omissing=missing_refs('web/book/main.html',oh)
ck('book local reference closure no regressions',not (set(nmissing)-set(omissing)),checked=ncount,missing=nmissing,inherited_missing=omissing)
lab=html(text('web/profile-uniformity.html'));lcount,lmissing=missing_refs('web/profile-uniformity.html',lab)
ck('standalone lab local resource and proof closure',not lmissing,checked=lcount,missing=lmissing)
repo_refs=[]
for tag,attr,ref in lab.refs:
 prefix='https://github.com/amelie-iska/GRH-research/blob/main/'
 if ref.startswith(prefix):
  q=ref[len(prefix):].split('#')[0];repo_refs.append(q)
ck('all new GitHub source links resolve within source project',all((R/p).is_file() for p in repo_refs),paths=repo_refs)
ck('book proof anchors and lab navigation',all(i in nh.ids for i in ['prf:core','prf:details','prf:lower','jdq:details']) and any('../profile-uniformity.html'==r[2] for r in nh.refs) and all(any('sources/profile-uniformity-'+part+'.tex'==r[2] for r in nh.refs) for part in ['core','details']))
landing=text('web/index.html');readme=text('README.md');claims=list(csv.DictReader(text('planning/CLAIMS.csv').splitlines()));claimkeys=[row[next(iter(row))] for row in claims]
ck('claims246 unique including new claims',len(claims)==246 and len(set(claimkeys))==246 and all(x in claimkeys for x in ['PRF01','JPM01']),rows=len(claims))
ck('current README and landing counts',all(s in readme for s in ['266 pages,40 chapters,7,605 MathML','thirteen unique in-book']) and all(s in landing for s in ['266 pages','40 chapters','7,605 MathML','articles61/162pages','notes19/53pages']))
ck('README and landing scope',all(s in readme for s in ['varies with scale','not a counterexample for fixed W','A complete proof of GRH has not been established']) and all(s in landing for s in ['moving-profile lower bound','fixed-profile quantifiers matter','signed asymptotic estimate and GRH bridge remain open']))
metadata=['book/VERIFICATION.md','book/SOURCE_COVERAGE.md','planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md'];sections=[]
for p in metadata:
 s=text(p);marker='## Moving-profile and coherent-mean boundary — 5 November 2026';section=s[s.index(marker):];section=section[:section.index('Next:')];sections.append(section)
ck('six synchronized scope sections',len(set(sections))==1,files=metadata,common_scope_sha256=sha(sections[0].encode()))
ck('six docs retain precise theorem and experiment boundaries',all(x in sections[0] for x in ['principal nu=1','varies with D','derivatives O_k(D^k)','SELECTED literal class','unselected rows','lower power9/8','current upper7/6','fixed-W counterexample','theta<2/3','k*alpha>=1−5theta/6','A6=1','Finite ratios do not prove','No new Lean declaration']))
research=text('research/profile-uniformity-and-coherent-means.md')
ck('research note fixed-profile and conductor-mask scope',all(s in research for s in ['not a new signed upper bound','It varies with D','S containing the primes above2,3','v is not squarefree','q=mn~D²','not estimates for the infinite dual tail','fixed-X64 is a separate range','Fixed-W bounds','no new upper saving','GRH proof is claimed']))
receipt=obj('outputs/checks/2026-11-05-signed-profile/promotion-final-v2/promotion-v1.json');changed=receipt['changed_artifacts'];promotion_mismatches=[x['target'] for x in changed if sha(data(x['target']))!=x['after_sha256'] or data(x['source'])!=data(x['target'])]
ck('successful promotion binds15 current artifacts',receipt['passed'] and len(changed)==15 and not promotion_mismatches,mismatches=promotion_mismatches)
frozen=obj('outputs/checks/2026-11-05-signed-profile/lab/frozen-receipt.json');labm=[p for p,m in frozen['files'].items() if sha(data(p))!=m['sha256']]
ck('frozen standalone lab unmodified',not labm,mismatches=labm)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();indexsha=sha(data('.git/index'))
ck('source HEAD and index preserved',head=='dba37ffaa78c82ade1385f7ee56c907ab0c67d3a' and indexsha=='0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c',HEAD=head,index_sha256=indexsha)
changed_inputs=[p for p,h in inputs.items() if sha(Path(p).read_bytes())!=h]
ck('all review inputs remained unchanged',not changed_inputs,changed=changed_inputs)
result={'passed':all(x['passed'] for x in checks),'reviewer':'quadratic_pivot_lab independent read-only integration review','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'input_sha256':inputs,'checker_sha256':sha(Path(__file__).read_bytes()),'limitations':['No compilation, experiment rerun or browser use; source/PDF/native outputs were read and compared.','Publication and final P7 checkpoint/generated governance pages are outside this review; root said they follow this receipt.','Three inherited munder diagnostics retained; no new malformed munder found.','Historical README edition paragraphs are retained; top-level current edition and current landing agree with the promoted artifacts.']}
(O/'integration-v2.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'checks':len(checks),'failed':[{k:v for k,v in x.items() if k!='matched_new_indices'} for x in checks if not x['passed']],'receipt':str(O/'integration-v2.json'),'sha256':sha((O/'integration-v2.json').read_bytes())},indent=2))
