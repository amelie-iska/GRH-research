"""Rendered interaction, independent mixed-state and failure-state checks."""
import argparse,json,re,sys,threading
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'workbench'))
import server
from program3.quantum_reference import hierarchy_kraus,channel

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();out=a.evidence/'browser';out.mkdir(parents=True,exist_ok=True)
 service=server.make_server(0);thread=threading.Thread(target=service.serve_forever,daemon=True);thread.start();base=f'http://127.0.0.1:{service.server_port}'
 report={'schema':'grh.program3.browser.v1','utc':datetime.now(timezone.utc).isoformat(),'url':base+'/workbench/program3.html','checks':{},'page_errors':[],'engine':'Playwright installed Chromium on isolated CPU runner'}
 def check(name,value):
  report['checks'][name]=bool(value)
  if not value:raise AssertionError(name)
 def ready(page):
  page.wait_for_function("document.documentElement.dataset.program3Ready==='true' || document.querySelector('#loadStatus').classList.contains('error') || document.querySelector('#skyStatus').classList.contains('error')",timeout=60000)
  if page.locator('#loadStatus').get_attribute('class')=='error':raise RuntimeError(page.locator('#loadStatus').inner_text())
  if page.locator('#skyStatus').get_attribute('class')=='error':raise RuntimeError(page.locator('#skyStatus').inner_text())
 try:
  with sync_playwright()as p:
   browser=p.chromium.launch(headless=True);page=browser.new_page(viewport={'width':1365,'height':950},reduced_motion='reduce');page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
   page.goto(report['url']);ready(page)
   check('hash_checked_assets','passed SHA-256' in page.locator('#loadStatus').inner_text())
   check('page_identity','Arithmetic, coverings' in page.title())
   check('actual_gate_execution','Executed every gate' in page.locator('#arithmeticResult').inner_text())
   check('clean_work_default','registers clean' in page.locator('#arithmeticResult').inner_text())
   default=page.locator('#resourceMetrics').inner_text();page.locator('#algorithm').select_option('endomorphism');check('cost_changes',page.locator('#resourceMetrics').inner_text()!=default)
   check('complete_cost_comparison','more CCX' in page.locator('#comparison').inner_text())
   page.locator('#point').select_option('0');check('invalid_word_fixed','invalid point word was fixed' in page.locator('#arithmeticResult').inner_text())
   page.locator('#curve').select_option('13');check('larger_curve_replay',page.locator('#resourceMetrics strong').nth(1).inner_text()=='27')
   page.locator('#gateNext').click();check('gate_pagination','Gates 19' in page.locator('#gateRange').inner_text());page.locator('#gatePrevious').click()
   page.locator('#degree').select_option('5');check('cover_degree','15 vertices' in page.locator('#coverResult').inner_text())
   check('integral_obstruction','no' in page.locator('#orderTable').inner_text())
   page.locator('#seed').select_option('29');check('trained_hierarchy','Actual four-qubit replay' in page.locator('#hierarchyResult').inner_text())
   old=page.locator('#hierarchyResult').inner_text();page.locator('#angle').evaluate("e=>{e.value='-1.2';e.dispatchEvent(new Event('input',{bubbles:true}))}");check('gate_parameter_response',old!=page.locator('#hierarchyResult').inner_text())
   page.locator('#coupling').evaluate("e=>{e.value='31';e.dispatchEvent(new Event('input',{bubbles:true}))}");check('heldout_mixed_state','test' in page.locator('#couplingValue').inner_text());check('mixed_density_replay','trace=1.0000000000' in page.locator('#mixedResult').inner_text())
   data=json.loads((ROOT/'workbench/site/program3-assets/hierarchy.json').read_text());r=next(x for x in data['thermal_runs']if x['seed']==29);rho=np.array(data['thermal'][31]['rho']);outstate=channel(rho,hierarchy_kraus(r['weights']['theta'])[2]);expected=float(r['weights']['slope']*(outstate[0,0]-outstate[1,1]).real+r['weights']['bias']);shown=float(re.search(r'predicted mean ZZ=([-+0-9.eE]+)',page.locator('#mixedResult').inner_text())[1]);check('mixed_state_independent_numeric_parity',abs(shown-expected)<5.1e-7)
   check('frozen_channel_baseline_visible','Frozen initial channel' in page.locator('#trainingResult').inner_text())
   page.locator('#product').select_option('V');page.wait_for_function("document.querySelector('#skyStatus').textContent.startsWith('V:')")
   expected=json.loads((ROOT/'workbench/site/program3-assets/cmb.json').read_text())['sources']['V']['record']['joint_rank_p']
   check('observed_rank_replayed',abs(float(page.locator('#skyMetrics strong').first.inner_text())-expected)<1e-6)
   page.locator('#template').select_option('5');page.locator('#amplitude').select_option('64');page.wait_for_function("document.querySelector('#skyStatus').textContent.includes('Synthetic injection')")
   check('injection_labeled','Synthetic injection' in page.locator('#skyStatus').inner_text())
   check('exploratory_followup_label','Exploratory' in page.locator('#followupResult').inner_text())
   check('dependent_product_control_visible','shared-phase family control' in page.locator('#jointResult').inner_text())
   before=page.locator('#skyMetrics').inner_text();page.reload();ready(page)
   check('url_restore',page.locator('#product').input_value()=='V' and page.locator('#amplitude').input_value()=='64' and page.locator('#degree').input_value()=='5')
   check('restored_score',before==page.locator('#skyMetrics').inner_text())
   with page.expect_download()as dl:page.locator('#export').click()
   path=out/'replay.json';dl.value.save_as(path);export=json.loads(path.read_text());check('export_hashes',len(export['asset_sha256'])==4 and all(len(x)==64 for x in export['asset_sha256'].values()))
   check('export_observation_vs_injection',export['sky']['injected'] and export['state']['amplitude']==64)
   page.locator('#resetAll').click();page.wait_for_function("document.querySelector('#skyStatus').textContent.includes('Observed-only replay')")
   check('reset',page.locator('#curve').input_value()=='7'and page.locator('#product').input_value()=='ILC'and page.locator('#algorithm').input_value()=='binary')
   page.screenshot(path=str(out/'desktop.png'),full_page=True)
   for id in ['arithmetic','coverings','sky']:page.locator('#'+id).screenshot(path=str(out/(id+'.png')))
   page.locator('#degree').focus();page.keyboard.press('ArrowDown');page.keyboard.press('Enter');check('keyboard_native_control',page.locator('#degree').input_value()=='3')
   page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(500);check('mobile_no_page_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));page.screenshot(path=str(out/'mobile.png'),full_page=True)
   page.set_viewport_size({'width':844,'height':390});page.wait_for_timeout(500);check('landscape_no_page_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
   check('nonblank_observed_canvas',page.locator('#skyCanvas').evaluate("c=>{const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let i=0;i<d.length;i+=400)n+=d[i]!==d[i+1];return n>50;}"))
   bad=browser.new_page();bad.route('**/program3-assets/arithmetic.json',lambda route:route.fulfill(status=200,content_type='application/json',body='{"wrong":true}'));bad.goto(report['url']);bad.wait_for_function("document.querySelector('#loadStatus').textContent.includes('hash mismatch')",timeout=30000);check('corrupt_evidence_rejected','hash mismatch' in bad.locator('#loadStatus').inner_text());bad.close()
   check('no_page_errors',not report['page_errors']);browser.close()
 except Exception as error:
  report['failure']=type(error).__name__+': '+str(error)
  try:report['failure_status']={'load':page.locator('#loadStatus').text_content(),'sky':page.locator('#skyStatus').text_content()};page.screenshot(path=str(out/'failure.png'),full_page=True)
  except Exception:pass
 finally:
  service.shutdown();service.server_close();thread.join();(out/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
 if report.get('failure'):raise SystemExit(1)
