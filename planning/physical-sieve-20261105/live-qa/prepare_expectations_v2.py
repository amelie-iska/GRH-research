"""Prepare immutable release expectations from explicitly pinned accepted artifacts. No browser/build/auth."""
from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction as F
import argparse,hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
class Inventory(HTMLParser):
 def __init__(self):super().__init__();self.counts={};self.ids=set();self.svgs=[];self.frames=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs);self.counts[t]=self.counts.get(t,0)+1
  if 'id'in a:self.ids.add(a['id'])
  if t=='img'and a.get('src','').endswith('.svg'):self.svgs.append(a['src'])
  if t=='iframe':self.frames.append(a['src'])
def inv(b):
 x=Inventory();x.feed(b.decode());return x
p=argparse.ArgumentParser();p.add_argument('--contract',type=Path,required=True);p.add_argument('--contract-sha',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
cb=a.contract.read_bytes();assert sha(cb)==a.contract_sha;c=json.loads(cb);assert c['schema']=='physical-sieve-expectations-input-v1'
bindings={}
def readpin(key,pin):
 f=Path(pin['path']);f=f if f.is_absolute()else R/f;f=f.resolve();assert f.is_relative_to(R)
 b=f.read_bytes();assert sha(b)==pin['sha256'],('pin mismatch',key);bindings[key]={'path':str(f.relative_to(R)),'sha256':sha(b)};return b
def record(key,pin):
 d=json.loads(readpin(key,pin));assert d['passed']is True,(key,'not passed')
 for rel,h in d.get('source_sha256',{}).items():assert sha((R/rel).read_bytes())==h,('source pin',key,rel)
 return d
gate=record('canonical_acceptance',c['canonical_acceptance']);assert len(gate['canonical_sha256'])==4
for rel,h in gate['canonical_sha256'].items():assert sha((R/rel).read_bytes())==h
bookrec=record('book_pdf_record',c['book']['record']);book=readpin('book_pdf',c['book']['pdf']);assert sha(book)==bookrec['pdf_sha256']
nrec=record('native_record',c['native']['record']);html=readpin('native_HTML',c['native']['html']);assert sha(html)==nrec['new_HTML_sha256'];current=inv(html)
assert nrec['raw_TeX_nodes']==0 and nrec['conversion_warnings']==0
assert current.counts['math']>8552 and current.counts['iframe']==13 and len(current.svgs)==29
pages={}
for name,item in {'book':c['book'],**c['articles']}.items():
 rec=bookrec if name=='book'else record(name+'_record',item['record']);pdf=book if name=='book'else readpin(name+'_pdf',item['pdf']);assert sha(pdf)==rec['pdf_sha256']
 f=Path(item['pdf']['path']);f=f if f.is_absolute()else R/f
 info=subprocess.check_output(['pdfinfo',str(f)],text=True);n=int(re.search(r'Pages:\s+(\d+)',info)[1]);assert n==rec.get('pdf_pages',rec.get('pages'));pages[name]=n
assert set(pages)=={'book','concise','extended','notes_concise','notes_extended'}
ui=record('UI_acceptance',c['UI_acceptance'])
for rel,h in ui['candidate_source_sha256'].items():assert sha((R/rel).read_bytes())==h
fa=record('four_build_acceptance',c['four_build_acceptance']);assert fa['all_ACTUAL_compiled_source_bindings_current'] and fa['canonical_layout_acceptance_sha256']==bindings['canonical_acceptance']['sha256']
for pins in fa['actual_compiled_inputs_by_build'].values():
 for rel,h in pins.items():assert sha((R/rel).read_bytes())==h
for name,item in c['articles'].items():
 key={'concise':'concise-v1','extended':'extended-v2','notes_concise':'notes-concise-v1','notes_extended':'notes-extended-v2'}[name];bound=fa['builds'][key];assert item['record']['sha256']==bound['build_record_sha256'] and item['pdf']['sha256']==bound['pdf_sha256']
if c.get('native_QA'):record('native_QA',c['native_QA'])
old=inv(subprocess.check_output(['git','show','90e62069cd81de4314b2e9ae3f17a7e12b7c46c9:web/book/main.html'],cwd=R));assert old.counts['math']==8552 and old.counts['table']==388 and old.counts['iframe']==13 and len(old.svgs)==29
prior=R/'planning/rough-mask-20261105/live-qa/expectations-v1.json';pb=prior.read_bytes();e=json.loads(pb);assert e['math_nodes']==8552 and e['tables']==388
priorbrowser=R/'outputs/checks/2026-11-05-rough-mask/live-qa/live-browser-20261105T223727258144Z/browser.json';bb=priorbrowser.read_bytes();assert sha(bb)=='8b72fe616d2b11af3adf0788fadc0f38d6919788950ba5f623149cf71ca6b509';bd=json.loads(bb);assert bd['passed']and bd['strict_integration_groups']==161
legacy=[x['name']for x in bd['integration']];assert len(legacy)==len(set(legacy))==161 and all(x['passed']for x in bd['integration'])
anchors=[]
for rel in gate['canonical_sha256']:anchors+=re.findall(r'\\label\{((?:cmr|phy):[^}]+)\}',(R/rel).read_text())
assert len(anchors)==len(set(anchors))==51 and all(x in current.ids for x in anchors)
theta=[]
for h in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
 powers=[h,1+h/6,5*h/6+F(1,3),h/3+F(5,6)];oldpowers=[h,1+h/6,2*(1+h)/3];sf=[h,F(1),5*h/6+F(1,3),h/3+F(5,6)]
 theta.append(dict(value=int(1000*h),theta=float(h),power=float(max(powers)),previousPower=float(max(oldpowers)),sixthFreePower=float(max(sf)),targetGap=float(max(powers)-h)))
e.update(schema='physical-sieve-release-expectations-v1',source='Explicit accepted artifact pins; counts parsed from bound HTML/PDF records. Browser execution still requires frozen bundle/root GO.',old_math_nodes=8552,old_tables=388,math_nodes=current.counts['math'],tables=current.counts['table'],book_pages=pages['book'],focused_pages=[pages['concise'],pages['extended']],notes_pages=[pages['notes_concise'],pages['notes_extended']],prior_harness_sha256='57640381b26548582c0012ca6577fcce82af68500d34497686700e698fae4e98',legacy_group_names=legacy,new_anchors=anchors,theta_states=theta,input_contract_sha256=sha(cb),input_bindings=bindings,ui_source_hashes={rel:row['sha256']for rel,row in ui['assets'].items()},prior_expectations_sha256=sha(pb),prior_browser_sha256=sha(bb),canonical_sha256=gate['canonical_sha256'],primary_pdf_sha256='97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726')
with a.output.open('x')as w:json.dump(e,w,sort_keys=True,indent=2);w.write('\n')
print(json.dumps({'passed':True,'path':str(a.output),'sha256':sha(a.output.read_bytes()),'counts':{'math':e['math_nodes'],'tables':e['tables'],'pages':pages},'legacy_groups':len(legacy),'new_anchors':len(anchors)}))
