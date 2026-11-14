"""Package completed evidence, build the research PDF, and seal all members."""
import argparse,hashlib,json,os,re,shutil,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def table(path,columns,heading,rows):
 path.write_text('\\begin{tabular}{'+columns+'}\\toprule '+heading+'\\\\\\midrule\n'+'\n'.join(' & '.join(map(str,r))+'\\\\'for r in rows)+'\n\\bottomrule\\end{tabular}\n')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);p.add_argument('--destination',type=Path,required=True);a=p.parse_args();dest=a.destination.resolve();a.evidence=a.evidence.resolve()
 if dest.exists():raise ValueError('Refuse to overwrite a prior release directory')
 formal=json.loads((a.evidence/'formal/audit.json').read_text());browser=json.loads((a.evidence/'browser/report.json').read_text());js=json.loads((a.evidence/'javascript-replay.json').read_text())
 if formal.get('status')!='verified'or browser.get('failure')or not all(browser['checks'].values())or not js.get('passed'):raise ValueError('Publication gate failed')
 counts={}
 for name in ['tests-normal.log','tests-optimized.log']:
  text=(a.evidence/name).read_text();counts[name]=int(re.search(r'Ran (\d+) tests',text)[1])
  if '\nOK\n'not in text:raise ValueError('Regression suite did not pass')
 source=json.loads((a.evidence/'source.json').read_text());current=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
 if current!=source['commit'] or formal['source_commit']!=current:raise ValueError('Source changed during verification')
 ecc=json.loads((a.evidence/'ecc/results.json').read_text());qrg=json.loads((a.evidence/'qrg/results.json').read_text());cmb=json.loads((a.evidence/'cmb/results.json').read_text());joint=json.loads((a.evidence/'cmb/joint-followup.json').read_text());extended=json.loads((a.evidence/'extended-controls.json').read_text())
 paper=a.evidence/'paper';paper.mkdir();rows=[]
 for c in ecc['curves']:
  for r in c['algorithms']:
   x=r['resources'];rows.append([c['curve']['p'],r['variant'],x['logical_qubits'],x['gates'].get('X',0),x['gates'].get('CCX',0),x['depth_all_to_all']])
 table(paper/'ecc-table.tex','llrrrr','Field & Path & Qubits & X & CCX & Depth',rows)
 table(paper/'cmb-table.tex','lrrr','Product & Full-search rank & Three-product bound & Null rejections',[[r['product'],f"{r['joint_rank_p']:.6f}",f"{r['bonferroni_three_product_p']:.6f}",str(r['null_validation']['rejections'])+'/256']for r in cmb['records']])
 table(paper/'qrg-table.tex','lrrr','Seed & Selected step & Test MSE & Constant baseline',[[r['seed'],r['selected_step'],f"{r['test_mse']:.7f}",f"{r['constant_test_mse']:.7f}"]for r in qrg['thermal_runs']])
 table(paper/'gate-controls-table.tex','lrrr','Seed & Learned gates MSE & Frozen gates + readout & Constant MSE',[[r['seed'],f"{r['learned_channel_test_mse']:.7f}",f"{r['initial_channel_train_only_linear_readout_test_mse']:.7f}",f"{r['constant_test_mse']:.7f}"]for r in extended['gate_learning_baselines']['rows']])
 table(paper/'joint-table.tex','lrr','Shared-phase family & Joint rank & Null rejections',[[joint['selected_product']+' selected',f"{joint['joint_rank']:.6f}",str(joint['null_validation']['rejections'])+'/256']])
 text='The independent runner accepted '+str(formal['new_declarations'])+' new formal declarations, '+str(counts['tests-normal.log'])+' regression methods under each Python mode, '+str(len(browser['checks']))+' browser checks, and '+str(js['full_sky_replays'])+' complete JavaScript/Python sky-score replays. The maximum score discrepancy was '+format(js['max_sky_score_error'],'.3g')+'.\n'
 (paper/'verification-summary.tex').write_text(text)
 for f in (ROOT/'workbench/research').glob('program3-*.tex'):shutil.copy2(f,paper/f.name)
 for name in ['arithmetic','coverings','sky']:shutil.copy2(a.evidence/'browser'/(name+'.png'),paper/(name+'.png'))
 for iteration in range(3):
  r=subprocess.run(['pdflatex','-halt-on-error','-interaction=nonstopmode','program3-main.tex'],cwd=paper,text=True,capture_output=True,timeout=90);(paper/f'pass-{iteration+1}.log').write_text(r.stdout+r.stderr)
  if r.returncode:print(r.stdout[-9000:]);raise SystemExit(r.returncode)
 pdf=paper/'program3-main.pdf';info=subprocess.check_output(['pdfinfo',str(pdf)],text=True);pages=int(re.search(r'Pages:\s*(\d+)',info)[1]);(paper/'pdfinfo.txt').write_text(info)
 final_log=(paper/'pass-3.log').read_text()
 if 'undefined references'in final_log or 'Overfull \\hbox'in final_log:raise ValueError('PDF unresolved references or overfull content')
 subprocess.run(['pdftoppm','-scale-to','600','-png',str(pdf),str(paper/'page')],check=True,timeout=60,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 dest.mkdir(parents=True);shutil.copytree(a.evidence,dest/'evidence');shutil.copy2(pdf,dest/'arithmetic-coverings-ccc.pdf');shutil.copytree(ROOT/'workbench/site/program3-assets',dest/'visual-data')
 (dest/'README.md').write_text('# Arithmetic, coverings, learned renormalization and CCC controls\n\nScientific source: `'+current+'`.\n\nThe PDF, emitted circuits, exact resource counts, source acquisition records, learned weights, full-search calibration, held-out diagnostics, explicitly exploratory followups and browser/formal logs are included. Raw NASA FITS remain linked by official URL and hash rather than duplicated. Initial product-specific scans remain separate from post-inspection common-reference and shared-phase family controls.\n\nThe CPU runner has no GPU. Earlier cuStateVec observations from the authorized workstation are described with their observed scope, not represented as independently reexecuted by this workflow. Desktop Commander reached its monthly quota; no remote retry or reconnection was attempted. Remote clones are not asserted synchronized after the pause.\n\nThe learned finite CPTP channel is not an infinite-system phase-transition proof. Independent-feature width, parameter sharing and covering degree have separate results and counterexamples. WMAP ranks are conditional phase-surrogate controls, not probabilities that CCC is true.\n')
 manifest={'schema':'grh.program3.release.v1','created_at_utc':datetime.now(timezone.utc).isoformat(),'scientific_source_commit':current,'run_id':os.environ.get('GITHUB_RUN_ID'),'cpu_runner_reexecution':True,'gpu_runner_reexecution':False,'new_formal_declarations':formal['new_declarations'],'regression_methods':counts,'browser_checks':len(browser['checks']),'javascript_replay':js,'pdf_pages':pages,'pdf_sha256':sha(dest/'arithmetic-coverings-ccc.pdf'),'main_machines_synchronized':False,'remote_scope':'Desktop Commander quota paused; independent public CPU runner, no paused-device access.','files':{str(f.relative_to(dest)):{'bytes':f.stat().st_size,'sha256':sha(f)}for f in sorted(dest.rglob('*'))if f.is_file()}}
 dump(dest/'manifest.json',manifest)
 if {str(f.relative_to(dest))for f in dest.rglob('*')if f.is_file()}!=set(manifest['files'])|{'manifest.json'}:raise ValueError('Manifest membership mismatch')
 print('PACKAGE_READY',dest,'pages',pages,'source',current,flush=True)
