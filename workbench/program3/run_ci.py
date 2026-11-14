"""Run the independent CPU portion and preserve every command's complete log."""
import argparse,hashlib,importlib.metadata,json,os,platform,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[2]

def run(args,cwd,log,timeout=900):
 p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,timeout=timeout)
 log.parent.mkdir(parents=True,exist_ok=True);log.write_text(p.stdout+p.stderr)
 print(log.name,'exit',p.returncode,flush=True)
 if p.returncode:print((p.stdout+p.stderr)[-8000:],flush=True);raise SystemExit(p.returncode)
 return p.stdout+p.stderr

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();a.evidence.mkdir(parents=True,exist_ok=True);a.data.mkdir(parents=True,exist_ok=True)
 meta={'schema':'grh.program3.ci-source.v1','utc':datetime.now(timezone.utc).isoformat(),'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'python':platform.python_version(),'packages':{x:importlib.metadata.version(x)for x in ['numpy','scipy','torch','healpy','astropy','pyerfa','playwright']},'runner':'Standard public ubuntu-latest GitHub Actions CPU runner','remote_desktop_used':False,'gpu_reexecuted':False}
 (a.evidence/'source.json').write_text(json.dumps(meta,indent=2)+'\n')
 for optimized in (False,True):run([sys.executable]+(['-O']if optimized else[])+['-m','unittest','discover','-s','workbench/tests','-v'],ROOT,a.evidence/('tests-optimized.log'if optimized else'tests-normal.log'))
 commands=[('ecc',['--output',str(a.evidence/'ecc')]),('ecc_oracles',['--output',str(a.evidence/'ecc')]),('covers',['--output',str(a.evidence/'covers.json')]),('qrg',['--output',str(a.evidence/'qrg')]),('cmb',['--data',str(a.data),'--output',str(a.evidence/'cmb'),'--acquire']),('cmb_followup',['--data',str(a.data),'--original',str(a.evidence/'cmb/results.json'),'--output',str(a.evidence/'cmb/followup.json')]),('visual_data',['--evidence',str(a.evidence),'--output',str(ROOT/'workbench/site/program3-assets')])]
 for name,args in commands:run([sys.executable,'-m','workbench.program3.'+name,*args],ROOT,a.evidence/(name+'.log'),timeout=1200)
 asset=ROOT/'workbench/site/program3-assets';(ROOT/'workbench/site/program3-manifest.json').write_bytes((asset/'program3-manifest.json').read_bytes())
 run(['node','workbench/program3/browser_replay.cjs',str(asset)],ROOT,a.evidence/'javascript-replay.json')
 for f in ['acquisition.json']:(a.evidence/f).write_bytes((a.data/f).read_bytes())
 print('CPU, observations, frozen search and independent JavaScript replay completed.',flush=True)
