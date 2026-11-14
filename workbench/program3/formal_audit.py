"""Strict declaration/type/axiom audit of the new formal modules."""
import argparse,hashlib,importlib.util,json,os,re,subprocess
from pathlib import Path
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[2]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mathlib',type=Path,required=True);p.add_argument('--lean',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
 expected='f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
 if subprocess.check_output(['git','rev-parse','HEAD'],cwd=a.mathlib,text=True).strip()!=expected:raise ValueError('Unpinned mathlib')
 spec=importlib.util.spec_from_file_location('verification',ROOT/'extension/lean/verify_all.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 result={'schema':'grh.program3.formal-audit.v1','utc':datetime.now(timezone.utc).isoformat(),'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'lean_version':subprocess.check_output([str(a.lean),'--version'],text=True).strip(),'lean_sha256':sha(a.lean),'mathlib_commit':expected,'modules':[]}
 env=os.environ.copy();env['PATH']=str(a.lean.parent)+':'+env['PATH']
 for module,count in [('Program3Contracts',11),('CCCGeometry',5),('ECCFiniteGenerated',6)]:
  f=ROOT/'workbench/lean'/(module+'.lean');before=sha(f);code=helper.stripped_code(f.read_text());names=[module+'.'+n for n in re.findall(r'^\s*theorem\s+([A-Za-z0-9_]+)',code,re.M)]
  if len(names)!=count:raise ValueError('Unexpected theorem inventory '+module)
  cmd=[str(a.lean.parent/'lake'),'env',str(a.lean),str(f)]
  proc=subprocess.run(cmd,cwd=a.mathlib,text=True,capture_output=True,timeout=240,env=env);text=proc.stdout+proc.stderr;(a.output/(module+'.log')).write_text(text)
  r=helper.evaluate_lean_output(names,text,proc.returncode,before==sha(f));r.update(module=module,declarations=count,source_sha256=before,log_sha256=sha(a.output/(module+'.log')));result['modules'].append(r)
  (a.output/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
  print(module,r['status'],flush=True)
  if r['status']!='verified':print(text,flush=True);raise SystemExit(1)
 result['new_declarations']=sum(x['declarations']for x in result['modules']);result['status']='verified';(a.output/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
