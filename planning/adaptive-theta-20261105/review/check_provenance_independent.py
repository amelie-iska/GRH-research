"""Read-only source-change simulation and immutable output/failure controls."""
from pathlib import Path
from fractions import Fraction as F
from unittest.mock import patch
import sys,time,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import adaptive_theta as a
import precision
OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/review';sources={n:(ROOT/'examples/analytic_oracle'/n).read_bytes() for n in ['precision.py','adaptive_theta.py']};checks=0
stamp=str(time.time_ns());original=Path.read_bytes;counts={}

def simulated_change(path):
 key=str(path);raw=original(path)
 if path.name=='precision.py' and path.parent==ROOT/'examples/analytic_oracle':
  counts[key]=counts.get(key,0)+1
  if counts[key]>1:return raw+b'\n# simulated source change, never written\n'
 return raw

p=OUT/('provenance-rejection-'+stamp)
with patch.object(Path,'read_bytes',simulated_change),patch.object(a,'circle',lambda *args,**kwargs:{'q':3,'radius':F(1,1000000)}):
 try:a.run(p,F(1,1000),(3,),1,1)
 except AssertionError as e:assert 'Source changed during run' in str(e);checks+=1
 else:raise AssertionError('Source-change simulation was accepted')
assert not (p/'sample-certificates.json').exists();checks+=1
failure=json.loads((p/'failure.json').read_text());assert failure['sample_oracle_validated'] is False and failure['error_type']=='AssertionError' and failure['completed_samples']==1;checks+=1
for name,raw in sources.items():assert (p/name).read_bytes()==raw;checks+=1
before={v.name:hashlib.sha256(v.read_bytes()).hexdigest() for v in p.iterdir() if v.is_file()}
try:a.run(p,F(1,1000),(3,),1,1)
except FileExistsError:checks+=1
else:raise AssertionError('Existing failure experiment overwritten')
after={v.name:hashlib.sha256(v.read_bytes()).hexdigest() for v in p.iterdir() if v.is_file()};assert before==after;checks+=1
p2=OUT/('sampler-failure-'+stamp)
with patch.object(a,'circle',side_effect=RuntimeError('controlled review failure')):
 try:a.run(p2,F(1,1000),(3,),1,1)
 except RuntimeError:checks+=1
 else:raise AssertionError('Controlled sampling failure was swallowed')
failure2=json.loads((p2/'failure.json').read_text());assert not (p2/'sample-certificates.json').exists() and failure2['sample_oracle_validated'] is False and failure2['completed_samples']==0 and failure2['error']=='controlled review failure';checks+=1
for module in [a,precision]:
 refused=OUT/('entry-source-rejection-'+module.__name__+'-'+stamp)
 with patch.object(module,'SOURCE_AT_IMPORT',module.SOURCE_AT_IMPORT+b'\n# simulated old imported module\n'):
  try:a.run(refused,F(1,1000),(3,),1,1)
  except ValueError as e:assert 'Loaded modules differ' in str(e);checks+=1
  else:raise AssertionError('Loaded source mismatch accepted')
 assert not refused.exists();checks+=1
assert all((ROOT/'examples/analytic_oracle'/n).read_bytes()==b for n,b in sources.items());checks+=1
report={'passed':True,'checks':checks,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in sources.items()},'source_change_was_read_return_simulation_only':True,'production_files_written':False,'failure_directories':[str(p),str(p2)]}
r=OUT/('provenance-independent-'+stamp+'.json');r.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(r),**report}))
