"""Build only four new staging candidates from root-frozen canonical source."""
from pathlib import Path
import sys,os,subprocess,hashlib,json,re,time,argparse
sys.dont_write_bytecode=True
os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
OUT=ROOT/'outputs/rough-mask-articles-20261105';CHECK=ROOT/'outputs/checks/2026-11-05-rough-mask/builds'
parser=argparse.ArgumentParser();parser.add_argument('--core-sha',required=True);parser.add_argument('--details-sha',required=True);parser.add_argument('--root-go',action='store_true');args=parser.parse_args();assert args.root_go,'Await explicit root source-integration GO';CORE=args.core_sha;DETAILS=args.details_sha

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def protected_states():
 states=json.loads((HERE.parent/'analytic/source-pins-v1.json').read_text())['protected_source_and_all_nine_release_worktrees']
 for x in states:
  b=Path(x['path']);env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
  def git(*args):return subprocess.check_output(['git','-C',str(b),*args],env=env,text=True).strip()
  ip=Path(git('rev-parse','--git-path','index'));ip=ip if ip.is_absolute()else b/ip
  assert dict(path=str(b),HEAD=git('rev-parse','HEAD'),index_sha256=sha(ip),index_bytes=ip.stat().st_size)==x
 return states
START=time.monotonic()
try:
 before=protected_states();assert sha(ROOT/'papers/rough-mask-core.tex')==CORE and sha(ROOT/'papers/rough-mask-details.tex')==DETAILS
 assert sha(ROOT/'scripts/build_remote_articles.py')=='ee282c130136a5e720a237787d32184a7a62ac5e9687d655d0bc357e9cce0152'
 # Preflight all four planned recursive source expansions before any output write.
 def preflight(wrapper):
  seen={}
  def expand(path,stack=()):
   path=path.resolve();assert path not in stack;raw=path.read_text();seen[str(path.relative_to(ROOT))]=sha(path)
   return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(ROOT/'papers'/(m[1]if m[1].endswith('.tex')else m[1]+'.tex'),stack+(path,)),raw)
  text=expand(ROOT/'papers'/wrapper);labels=re.findall(r'\\label\{([^}]+)\}',text);assert len(labels)==len(set(labels)),wrapper
  assert seen['papers/rough-mask-core.tex']==CORE
  if 'extended'in wrapper:assert seen['papers/rough-mask-details.tex']==DETAILS
  assert r'\label{rma:core}'in text
  return seen
 planned={n:preflight(n)for n in ['resolutions-concise.tex','resolutions-extended.tex','validated-oracle-concise.tex','validated-oracle-extended.tex']}
 assert not CHECK.exists();CHECK.mkdir(parents=True)
 records={};env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
 jobs=[('concise-v1','concise',False),('extended-v1','extended',False),('notes-concise-v1','concise',True),('notes-extended-v1','extended',True)]
 for name,edition,notes in jobs:
  dest=OUT/name;assert not dest.exists()
  if notes:cmd=[sys.executable,'-B',str(HERE/'build_notes_v1.py'),'--edition',edition,'--output',str(dest),'--core-sha',CORE,'--details-sha',DETAILS]
  else:cmd=[sys.executable,'-B',str(ROOT/'scripts/build_remote_articles.py'),'--edition',edition,'--output',str(dest)]
  with(CHECK/(name+'-command.log')).open('x')as f:subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
  r=json.loads((dest/'build-record.json').read_text());assert r['passed'] and r['source_sha256']['papers/rough-mask-core.tex']==CORE
  if edition=='extended':assert r['source_sha256']['papers/rough-mask-details.tex']==DETAILS
  for n,h in r['source_sha256'].items():assert sha(ROOT/n)==h,n
  stem=('validated-oracle-'if notes else'resolutions-')+edition;log=dest/(stem+'.log');text=log.read_text();bad=[v for v in text.splitlines()if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!',v)]
  assert not bad,bad
  old=ROOT/'outputs/signed-divisor-articles-20261105'/name/(stem+'.log');oldtext=old.read_text()
  warnings=[v for v in text.splitlines()if 'Warning:'in v];oldwarnings=[v for v in oldtext.splitlines()if 'Warning:'in v]
  added=[v for v in warnings if v not in oldwarnings]
  marker='atargetsizedbudgetforroughprimemasks';norm=lambda s:''.join(c.lower()for c in s if c.isascii()and c.isalnum());assert marker in norm((dest/'extracted-text.txt').read_text())
  records[name]={'build_record':str((dest/'build-record.json').relative_to(ROOT)),'build_record_sha256':sha(dest/'build-record.json'),'pdf':str((dest/(stem+'.pdf')).relative_to(ROOT)),'pdf_sha256':sha(dest/(stem+'.pdf')),'pages':r.get('pages',r.get('pdf_pages')),'log':str(log.relative_to(ROOT)),'log_sha256':sha(log),'expanded_source_sha256':sha(dest/(stem+'.expanded.tex')),'warning_lines':warnings,'previous_warning_lines':oldwarnings,'new_warning_lines':added,'underfull_count':text.count('Underfull'),'previous_underfull_count':oldtext.count('Underfull'),'bad_log_lines':bad,'all_sources_current':True}
  print(json.dumps({'stage':'BUILD_PASS','name':name,'pages':records[name]['pages'],'new_warning_lines':added,'underfull':records[name]['underfull_count'],'elapsed':round(time.monotonic()-START,3)}),flush=True)
 for name,r in records.items():
  for n,h in json.loads((ROOT/r['build_record']).read_text())['source_sha256'].items():assert sha(ROOT/n)==h,n
 assert protected_states()==before
 result=dict(passed=True,runner_sha256=sha(Path(__file__)),notes_builder_sha256=sha(HERE/'build_notes_v1.py'),planned_recursive_source_preflight=planned,canonical_core_sha256=CORE,canonical_details_sha256=DETAILS,builds=records,CPU_affinity_count=len(os.sched_getaffinity(0)),pdflatex_nice_increment=15,production_edited=False,production_promoted=False,protected_source_and_all_nine_release_states=before,all_source_bindings_current=True,elapsed_seconds=round(time.monotonic()-START,3))
 with(CHECK/'four-builds-v1.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'stage':'ALL_FOUR_PASS','receipt':str(CHECK/'four-builds-v1.json'),'sha256':sha(CHECK/'four-builds-v1.json')}),flush=True)
except Exception as e:
 CHECK.mkdir(parents=True,exist_ok=True)
 with(CHECK/'failure-v1.json').open('x')as f:json.dump(dict(passed=False,error_type=type(e).__name__,error=str(e),runner_sha256=sha(Path(__file__)),elapsed_seconds=round(time.monotonic()-START,3)),f,indent=2);f.write('\n')
 raise
