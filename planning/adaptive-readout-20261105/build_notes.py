"""Source-preserving standalone note build; candidates only, never promote."""
from pathlib import Path
import re,subprocess,hashlib,json,argparse,os
ROOT=Path(__file__).resolve().parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--edition',choices=['concise','extended'],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
sources={}
def read(path):
 path=path.resolve();data=path.read_bytes();sources[str(path.relative_to(ROOT))]=sha(data);return data.decode()
def expand(text):return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(read(ROOT/'papers'/(m[1]+'.tex'))),text)
name='validated-oracle-'+a.edition;text=expand(read(ROOT/'papers'/(name+'.tex')))
assert all('papers/'+n+'-core.tex' in sources for n in ['adaptive-readout','covariance-budget'])
if a.edition=='extended':assert all('papers/'+n+'-details.tex' in sources for n in ['adaptive-readout','covariance-budget'])
source=out/(name+'.expanded.tex');source.write_text(text)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for i in range(3):
 with (out/f'build-pass{i+1}.txt').open('w') as log:subprocess.run(['nice','-n','15','pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname='+name,'-output-directory='+str(out),str(source)],cwd=out,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
log=(out/(name+'.log')).read_text();bad=[x for x in log.splitlines() if re.search(r'Overfull|undefined references|Reference .* undefined|multiply defined',x)]
assert not bad,bad
assert all(sha((ROOT/n).read_bytes())==h for n,h in sources.items()),'Source changed during build'
pdf=out/(name+'.pdf');info=subprocess.check_output(['pdfinfo',str(pdf)],text=True);pages=int(re.search(r'Pages:\s+(\d+)',info)[1])
text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True);(out/'extracted-text.txt').write_text(text)
assert 'Requested-error readouts' in text and 'quantitative covariance budget' in text
record={'passed':True,'source_sha256':sources,'pdf_sha256':sha(pdf.read_bytes()),'pdf_pages':pages,'production_promoted':False,'new_Lean_declarations':0}
(out/'build-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
