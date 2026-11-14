"""Read-only public-byte and rendered checks after the Pages deployment."""
import hashlib,json,os,subprocess,urllib.request
from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2]
BASE='https://amelie-iska.github.io/GRH-research/'
OUT=Path(os.environ.get('RUNNER_TEMP','/tmp'))/'program3-publication';OUT.mkdir(exist_ok=True)
def sha(data):return hashlib.sha256(data).hexdigest()
checks=[]
files={f'workbench/{name}':ROOT/'workbench/site'/name for name in ['program3.html','program3-app.js','program3-core.js','program3.css','program3-manifest.json','index.html']}
for f in (ROOT/'workbench/site/program3-assets').iterdir():
 if f.is_file():files['workbench/program3-assets/'+f.name]=f
files['workbench/program3-report.pdf']=ROOT/'releases/program3-20261114/arithmetic-coverings-ccc.pdf'
files['quantum-core.js']=ROOT/'extension/site/quantum-core.js'
for name,path in files.items():
 with urllib.request.urlopen(urllib.request.Request(BASE+name,headers={'User-Agent':'GRH-research publication verification'}),timeout=45)as response:data=response.read(40000001)
 if data!=path.read_bytes():raise ValueError('Public byte mismatch: '+name)
 checks.append({'path':name,'bytes':len(data),'sha256':sha(data)})
report={'schema':'grh.program3.publication.v1','checked_at_utc':datetime.now(timezone.utc).isoformat(),'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'http_exact_bytes':checks,'browser_checks':{},'page_errors':[]}
def check(name,value):
 report['browser_checks'][name]=bool(value)
 if not value:raise AssertionError(name)
try:
 with sync_playwright()as p:
  browser=p.chromium.launch(headless=True);page=browser.new_page(viewport={'width':1365,'height':950},reduced_motion='reduce');page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
  page.goto(BASE+'workbench/program3.html');page.wait_for_function("document.documentElement.dataset.program3Ready==='true'",timeout=60000)
  check('scientific_asset_hashes','passed SHA-256' in page.locator('#loadStatus').inner_text())
  check('emitted_arithmetic','Executed every gate' in page.locator('#arithmeticResult').inner_text())
  page.locator('#algorithm').select_option('endomorphism');page.locator('#point').select_option('0');check('invalid_word_and_cleanup','invalid point word was fixed' in page.locator('#arithmeticResult').inner_text())
  page.locator('#degree').select_option('5');check('covering_selection','15 vertices' in page.locator('#coverResult').inner_text())
  page.locator('#coupling').evaluate("e=>{e.value='31';e.dispatchEvent(new Event('input',{bubbles:true}))}");check('learned_mixed_state','trace=1.0000000000' in page.locator('#mixedResult').inner_text())
  page.locator('#product').select_option('V');page.wait_for_function("document.querySelector('#skyStatus').textContent.startsWith('V:')");check('observed_rank',abs(float(page.locator('#skyMetrics strong').first.inner_text())-.005859375)<1e-6)
  check('final_joint_validation','9 of 256' in page.locator('#jointValidation').inner_text())
  check('correct_evidence_destination','/releases/program3-20261114' in page.locator('#evidenceLink').get_attribute('href'))
  page.locator('#amplitude').select_option('64');page.wait_for_function("document.querySelector('#skyStatus').textContent.includes('Synthetic injection')");check('synthetic_label',True)
  with page.expect_download()as download:page.locator('#export').click()
  f=OUT/'export.json';download.value.save_as(f);record=json.loads(f.read_text());check('export_source_hashes',len(record['asset_sha256'])==4 and record['sky']['injected'])
  page.locator('#resetAll').click();page.wait_for_function("document.querySelector('#skyStatus').textContent.includes('Observed-only replay')");check('reset',page.locator('#product').input_value()=='ILC')
  page.screenshot(path=str(OUT/'desktop.png'),full_page=True)
  page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(500);check('mobile_no_horizontal_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));page.screenshot(path=str(OUT/'mobile.png'),full_page=True)
  check('no_page_exceptions',not report['page_errors']);browser.close()
except Exception as e:report['failure']=type(e).__name__+': '+str(e)
(OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if report.get('failure'):raise SystemExit(1)
