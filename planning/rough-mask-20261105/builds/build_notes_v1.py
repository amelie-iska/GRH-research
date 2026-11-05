"""Preserved version of the existing inline three-pass notes build workflow."""
from pathlib import Path
import argparse,hashlib,json,os,re,subprocess,sys,unicodedata
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--edition',choices=['concise','extended'],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--core-sha',required=True);p.add_argument('--details-sha',required=True);a=p.parse_args()
 os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
 out=a.output.resolve();assert not out.exists(),'Preserve all prior build attempts';out.mkdir(parents=True)
 snapshot=Path(__file__).read_bytes();(out/'builder.py').write_bytes(snapshot);sources={}
 def unchanged():return all(sha(ROOT/n)==h for n,h in sources.items())
 try:
  for name,h in [('rough-mask-core.tex',a.core_sha),('rough-mask-details.tex',a.details_sha)]:assert sha(ROOT/'papers'/name)==h,'Canonical source changed: '+name
  base=ROOT/'papers';wrapper=base/('validated-oracle-'+a.edition+'.tex')
  def expand(path,stack=()):
   path=path.resolve();assert path not in stack,'Recursive input cycle';name=str(path.relative_to(ROOT));h=sha(path)
   if name in sources:assert sources[name]==h
   sources[name]=h;raw=path.read_text()
   return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(base/(m[1]if m[1].endswith('.tex')else m[1]+'.tex'),stack+(path,)),raw)
  text=expand(wrapper);assert sources['papers/rough-mask-core.tex']==a.core_sha
  if a.edition=='extended':assert sources['papers/rough-mask-details.tex']==a.details_sha
  labels=re.findall(r'\\label\{([^}]+)\}',text);assert len(labels)==len(set(labels)),'Duplicate source labels'
  target=out/('validated-oracle-'+a.edition+'.expanded.tex');target.write_text(text)
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
  for turn in(1,2,3):
   with(out/f'build-pass{turn}.txt').open('x')as f:subprocess.run(['nice','-n','15','pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname=validated-oracle-'+a.edition,'-output-directory='+str(out),str(target)],cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
  stem='validated-oracle-'+a.edition;log=out/(stem+'.log');raw=log.read_text();bad=[v for v in raw.splitlines()if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|^!',v)]
  assert not bad,bad
  pdf=out/(stem+'.pdf');assert pdf.read_bytes().startswith(b'%PDF');info=subprocess.check_output(['pdfinfo',str(pdf)],text=True);pages=int(re.search(r'Pages:\s+(\d+)',info)[1]);extract=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True);(out/'extracted-text.txt').write_text(extract)
  normalize=lambda s:''.join(c.lower()for c in unicodedata.normalize('NFKD',s)if c.isascii()and c.isalnum())
  marker='A target-sized budget for rough-prime masks';assert normalize(marker)in normalize(extract)
  if a.edition=='extended':assert normalize('Proof of the rough-prime mask budget')in normalize(extract)
  assert unchanged()and Path(__file__).read_bytes()==snapshot
  record=dict(passed=True,builder_sha256=hashlib.sha256(snapshot).hexdigest(),source_sha256=sources,pdf_sha256=sha(pdf),pdf_pages=pages,log_sha256=sha(log),expanded_source_sha256=sha(target),source_unchanged=True,new_proof_marker=marker,CPU_affinity_count=len(os.sched_getaffinity(0)),pdflatex_nice_increment=15,production_edited=False,production_promoted=False,new_Lean_declarations=0)
  (out/'build-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'edition':a.edition,'output':str(out),'pages':pages}))
 except Exception as e:
  (out/'failure-record.json').write_text(json.dumps(dict(passed=False,error_type=type(e).__name__,error=str(e),source_sha256=sources,source_unchanged=unchanged(),builder_sha256=hashlib.sha256(snapshot).hexdigest(),production_edited=False,production_promoted=False),indent=2)+'\n');raise
if __name__=='__main__':main()
