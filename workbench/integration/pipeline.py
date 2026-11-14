"""Executed integration pipeline, with source and artifact integrity gates."""
import argparse,hashlib,importlib.util,json,os,re,shutil,subprocess,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def run(command,log,cwd=ROOT,timeout=300):
 p=subprocess.run(command,cwd=cwd,text=True,capture_output=True,timeout=timeout);log.parent.mkdir(parents=True,exist_ok=True);log.write_text(p.stdout+p.stderr);print(log.name,'exit',p.returncode,flush=True)
 if p.returncode:print((p.stdout+p.stderr)[-8000:],flush=True);raise SystemExit(p.returncode)
 return p.stdout+p.stderr
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def studies(out,data):
 out.mkdir(parents=True,exist_ok=True)
 for name,args in [('arithmetic',['--output',str(out/'arithmetic')]),('neural_operator',['--output',str(out/'neural-operator.json')])]:run([sys.executable,'-m','workbench.integration.'+name,*args],out/(name+'.log'))
 run([sys.executable,'-c',"from pathlib import Path;from workbench.program3.cmb import acquire;acquire(Path("+repr(str(data))+"))"],out/'acquisition.log')
 run([sys.executable,'-m','workbench.integration.calibration','--data',str(data),'--original','releases/program3-20261114/evidence/cmb/results.json','--output',str(out/'calibration.json')],out/'calibration.log',timeout=600);shutil.copy2(data/'acquisition.json',out/'acquisition.json');run([sys.executable,'-m','workbench.integration.unify','--evidence',str(out)],out/'integration.log')
def manuscript_inputs():
 directories=['extension/manuscript','extension/lean','workbench/research','workbench/integration','releases/program3-20261114/evidence/paper'];result={}
 for directory in directories:
  for p in(ROOT/directory).rglob('*'):
   if p.is_file()and p.suffix in('.tex','.bib','.sty','.lean','.png')and '.texbuild'not in p.parts:result[str(p.relative_to(ROOT))]=sha(p)
 return result
def verify(out):
 source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip();(out/'source.json').write_text(json.dumps({'source_commit':source,'remote_machine_access':False,'scope':'Unified native manuscript and main-page integration; independent CPU verification.'},indent=2)+'\n')
 for opt,name in [([],'tests-normal.log'),(['-O'],'tests-optimized.log')]:run([sys.executable,*opt,'-m','unittest','discover','-s','workbench/tests','-v'],out/name)
 for script in ['verify-math.cjs','verify-quantum.cjs','verify-quantum-worker.cjs','verify-algebra.cjs','verify-cosmology.cjs']:run(['node','extension/site/'+script],out/(script+'.log'))
 run(['node','--check','extension/site/integrated-app.js'],out/'integrated-javascript-syntax.log');before=manuscript_inputs();run([sys.executable,'build_pdf.py'],out/'manuscript-build.log',cwd=ROOT/'extension/manuscript',timeout=600)
 if manuscript_inputs()!=before:raise AssertionError('Native manuscript inputs changed during build')
 (out/'all-manuscript-inputs.json').write_text(json.dumps(before,indent=2)+'\n');pdf=ROOT/'extension/manuscript/main.pdf';downloads=ROOT/'extension/site/downloads';downloads.mkdir(exist_ok=True);shutil.copy2(pdf,downloads/'paper.pdf');shutil.copy2(pdf,ROOT/'extension/site/workbench/program3-report.pdf');run([sys.executable,'-m','workbench.integration.browser_check','--output',str(out/'browser')],out/'browser.log',timeout=180)
def formal(out,mathlib,lean):
 expected='f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
 if subprocess.check_output(['git','rev-parse','HEAD'],cwd=mathlib,text=True).strip()!=expected:raise ValueError('Unpinned mathlib')
 spec=importlib.util.spec_from_file_location('audit',ROOT/'extension/lean/verify_all.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);report={'schema':'grh.integrated-formal.v1','mathlib_commit':expected,'lean_version':subprocess.check_output([str(lean),'--version'],text=True).strip(),'modules':[],'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()};env=os.environ.copy();env['PATH']=str(lean.parent)+':'+env['PATH']
 for name in('Program3Contracts','CCCGeometry','ECCFiniteGenerated','IntegratedOperatorContracts'):
  path=ROOT/'workbench/lean'/(name+'.lean');text=path.read_text();names=[name+'.'+n for n in re.findall(r'^\s*theorem\s+(\w+)',helper.stripped_code(text),re.M)];before=sha(path);p=subprocess.run([str(lean.parent/'lake'),'env',str(lean),str(path)],cwd=mathlib,text=True,capture_output=True,env=env,timeout=180);log=p.stdout+p.stderr;(out/(name+'.log')).write_text(log);r=helper.evaluate_lean_output(names,log,p.returncode,before==sha(path));r.update(module=name,source_sha256=before,count=len(names));report['modules'].append(r)
  if r['status']!='verified':print(log,flush=True)
 report['status']='verified'if all(x['status']=='verified'for x in report['modules'])else'failed';report['declarations']=sum(x['count']for x in report['modules']);(out/'formal.json').write_text(json.dumps(report,indent=2)+'\n')
 if report['status']!='verified':raise SystemExit(1)
def package(out):
 pdf=ROOT/'extension/manuscript/main.pdf';record=json.loads((ROOT/'extension/manuscript/build-verification.json').read_text());browser=json.loads((out/'browser/report.json').read_text());proof=json.loads((out/'formal.json').read_text())
 if browser.get('failure')or not all(browser['checks'].values())or proof['status']!='verified':raise AssertionError('Evidence gate failed')
 if record['pages']<=355:raise AssertionError('New edition omits original/full added source')
 destination=ROOT/'releases/integrated-20261114';destination.mkdir(parents=True,exist_ok=True);shutil.copytree(out,destination/'evidence',dirs_exist_ok=True);shutil.copy2(pdf,destination/'monograph.pdf');shutil.copy2(ROOT/'extension/manuscript/build-verification.json',destination/'manuscript-build.json');archive=ROOT/'extension/site/downloads/source.zip'
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED)as z:
  for parent in('extension/manuscript','extension/lean','workbench/research','workbench/integration','workbench/lean','workbench/program3','workbench/tests'):
   for f in(ROOT/parent).rglob('*'):
    if f.is_file()and f.suffix.lower()in('.tex','.bib','.sty','.py','.lean','.js','.cjs','.md','.svg','.png','.pdf')and f.name not in('main.pdf','fluid-extension.pdf')and '.texbuild'not in f.parts:z.write(f,str(f.relative_to(ROOT)))
  for f in(ROOT/'releases/program3-20261114/evidence/paper').iterdir():
   if f.suffix in('.tex','.png'):z.write(f,str(f.relative_to(ROOT)))
 manifest={'schema':'grh.integrated-release.v1','scientific_source':json.loads((out/'source.json').read_text())['source_commit'],'pdf_pages':record['pages'],'pdf_sha256':sha(pdf),'native_source_integration':True,'same_main_page':True,'new_uniform_arithmetic_cases':len(json.loads((out/'arithmetic/results.json').read_text())['records']),'learned_operator_heldout_cases':len(json.loads((out/'neural-operator.json').read_text())['results']),'fresh_formal_declarations':proof['declarations'],'browser_checks':len(browser['checks']),'regression_tests':int(re.search(r'Ran (\d+) tests',(out/'tests-normal.log').read_text())[1]),'calibration_draws':4095,'validation_draws':1024,'historical_releases_preserved':True,'remote_clone_synchronization':'not performed; Desktop Commander remained paused','files':{str(f.relative_to(destination)):{'bytes':f.stat().st_size,'sha256':sha(f)}for f in sorted(destination.rglob('*'))if f.is_file()}};(destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');shutil.copy2(destination/'manifest.json',ROOT/'extension/site/verification/integration/manifest.json');print(json.dumps({k:v for k,v in manifest.items()if k!='files'},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('phase',choices=['studies','verify','formal','package']);p.add_argument('--out',type=Path,required=True);p.add_argument('--data',type=Path);p.add_argument('--mathlib',type=Path);p.add_argument('--lean',type=Path);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 if a.phase=='studies':studies(a.out,a.data)
 elif a.phase=='verify':verify(a.out)
 elif a.phase=='formal':formal(a.out,a.mathlib,a.lean)
 else:package(a.out)
