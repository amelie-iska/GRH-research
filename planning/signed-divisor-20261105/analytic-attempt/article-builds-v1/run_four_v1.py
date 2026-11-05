"""Build only four new staging candidates from root-frozen canonical source."""
from pathlib import Path
import sys,os,subprocess,hashlib,json,re,time
sys.dont_write_bytecode=True
os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OUT=ROOT/'outputs/signed-divisor-articles-20261105';CHECK=ROOT/'outputs/checks/2026-11-05-signed-divisor/analytic/article-builds-v1'
CORE='bce916fab66aab19718a127b26b3ac581e48f49e0dd0317a64cf1648a4e5b7cb';DETAILS='504318141e100fd43f1021492c349a655953909b3213a083452d1230fa35cbc9'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def protected_states():
 states=json.loads((HERE.parent/'source-pins-v1.json').read_text())['protected_source_and_eight_release_worktrees']
 for x in states:
  b=Path(x['path']);env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
  def git(*args):return subprocess.check_output(['git','-C',str(b),*args],env=env,text=True).strip()
  ip=Path(git('rev-parse','--git-path','index'));ip=ip if ip.is_absolute()else b/ip
  assert dict(path=str(b),HEAD=git('rev-parse','HEAD'),index_sha256=sha(ip),index_bytes=ip.stat().st_size)==x
 return states
START=time.monotonic();assert not CHECK.exists();CHECK.mkdir(parents=True)
try:
 before=protected_states();assert sha(ROOT/'papers/signed-divisor-core.tex')==CORE and sha(ROOT/'papers/signed-divisor-details.tex')==DETAILS
 assert sha(ROOT/'scripts/build_remote_articles.py')=='ee282c130136a5e720a237787d32184a7a62ac5e9687d655d0bc357e9cce0152'
 records={};env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
 jobs=[('concise-v1','concise',False),('extended-v1','extended',False),('notes-concise-v1','concise',True),('notes-extended-v1','extended',True)]
 for name,edition,notes in jobs:
  dest=OUT/name;assert not dest.exists()
  if notes:cmd=[sys.executable,'-B',str(HERE/'build_notes_v1.py'),'--edition',edition,'--output',str(dest),'--core-sha',CORE,'--details-sha',DETAILS]
  else:cmd=[sys.executable,'-B',str(ROOT/'scripts/build_remote_articles.py'),'--edition',edition,'--output',str(dest)]
  with(CHECK/(name+'-command.log')).open('x')as f:subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
  r=json.loads((dest/'build-record.json').read_text());assert r['passed'] and r['source_sha256']['papers/signed-divisor-core.tex']==CORE
  if edition=='extended':assert r['source_sha256']['papers/signed-divisor-details.tex']==DETAILS
  for n,h in r['source_sha256'].items():assert sha(ROOT/n)==h,n
  stem=('validated-oracle-'if notes else'resolutions-')+edition;log=dest/(stem+'.log');text=log.read_text();bad=[v for v in text.splitlines()if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!',v)]
  assert not bad,bad
  old=ROOT/'outputs/signed-weights-articles-20261105'/name/(stem+'.log');oldtext=old.read_text()
  warnings=[v for v in text.splitlines()if 'Warning:'in v];oldwarnings=[v for v in oldtext.splitlines()if 'Warning:'in v]
  added=[v for v in warnings if v not in oldwarnings]
  marker='thesigneddivisormeanandacompletecolumnlaboratory';norm=lambda s:''.join(c.lower()for c in s if c.isascii()and c.isalnum());assert marker in norm((dest/'extracted-text.txt').read_text())
  records[name]={'build_record':str((dest/'build-record.json').relative_to(ROOT)),'build_record_sha256':sha(dest/'build-record.json'),'pdf':str((dest/(stem+'.pdf')).relative_to(ROOT)),'pdf_sha256':sha(dest/(stem+'.pdf')),'pages':r.get('pages',r.get('pdf_pages')),'log':str(log.relative_to(ROOT)),'log_sha256':sha(log),'expanded_source_sha256':sha(dest/(stem+'.expanded.tex')),'warning_lines':warnings,'previous_warning_lines':oldwarnings,'new_warning_lines':added,'underfull_count':text.count('Underfull'),'previous_underfull_count':oldtext.count('Underfull'),'bad_log_lines':bad,'all_sources_current':True}
  print(json.dumps({'stage':'BUILD_PASS','name':name,'pages':records[name]['pages'],'new_warning_lines':added,'underfull':records[name]['underfull_count'],'elapsed':round(time.monotonic()-START,3)}),flush=True)
 for name,r in records.items():
  for n,h in json.loads((ROOT/r['build_record']).read_text())['source_sha256'].items():assert sha(ROOT/n)==h,n
 assert protected_states()==before
 result=dict(passed=True,runner_sha256=sha(Path(__file__)),notes_builder_sha256=sha(HERE/'build_notes_v1.py'),canonical_core_sha256=CORE,canonical_details_sha256=DETAILS,builds=records,CPU_affinity_count=len(os.sched_getaffinity(0)),pdflatex_nice_increment=15,production_edited=False,production_promoted=False,protected_source_and_eight_release_states=before,all_source_bindings_current=True,elapsed_seconds=round(time.monotonic()-START,3))
 with(CHECK/'four-builds-v1.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'stage':'ALL_FOUR_PASS','receipt':str(CHECK/'four-builds-v1.json'),'sha256':sha(CHECK/'four-builds-v1.json')}),flush=True)
except Exception as e:
 with(CHECK/'failure-v1.json').open('x')as f:json.dump(dict(passed=False,error_type=type(e).__name__,error=str(e),runner_sha256=sha(Path(__file__)),elapsed_seconds=round(time.monotonic()-START,3)),f,indent=2);f.write('\n')
 raise
