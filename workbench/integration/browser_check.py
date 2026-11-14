"""Verify old and newly embedded experiments on the same canonical page."""
import argparse,functools,http.server,json,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2]

def run(output,base=None):
 output.mkdir(parents=True,exist_ok=True);server=None;thread=None
 if base is None:
  class Quiet(http.server.SimpleHTTPRequestHandler):
   def log_message(self,*args):pass
  server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT/'extension/site')));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base=f'http://127.0.0.1:{server.server_port}/'
 report={'schema':'grh.integrated-browser.v1','base':base,'checks':{},'errors':[]}
 def check(name,value):
  report['checks'][name]=bool(value)
  if not value:raise AssertionError(name)
 def ready(page):
  page.wait_for_function("(()=>{const h=document.getElementById('integratedMount');return h&&(h.dataset.nextStepsError||h.shadowRoot?.getElementById('loadStatus')?.classList.contains('error')||(h.dataset.program3Ready==='true'&&h.dataset.nextStepsReady==='true'));})()",timeout=60000)
  error=page.evaluate("(()=>{const h=document.getElementById('integratedMount');return h.dataset.nextStepsError||(h.shadowRoot.getElementById('loadStatus').classList.contains('error')?h.shadowRoot.getElementById('loadStatus').textContent:null);})()")
  if error:raise RuntimeError(error)
 try:
  with sync_playwright()as p:
   browser=p.chromium.launch(headless=True);page=browser.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce');page.on('pageerror',lambda e:report['errors'].append(str(e)));page.goto(base,wait_until='domcontentloaded');ready(page)
   check('original_six_laboratories_present',all(page.locator('#'+x).count()==1 for x in('torus','cone','elliptic','fourier','hodge','gauge')))
   check('one_main_document_link',page.locator('.header-download').get_attribute('href')=='downloads/paper.pdf')
   check('new_controls_embedded_not_iframe',page.locator('#integratedMount iframe').count()==0 and page.locator('#integratedMount #curve').count()==1)
   page.locator('#integratedMount #algorithm').select_option('endomorphism');page.locator('#integratedMount #point').select_option('0');check('embedded_ecc_invalid_word','invalid point word was fixed' in page.locator('#integratedMount #arithmeticResult').inner_text())
   page.locator('#integratedMount #degree').select_option('5');check('cover_control','15 vertices' in page.locator('#integratedMount #coverResult').inner_text())
   page.locator('#integratedMount #product').select_option('V');page.wait_for_function("document.getElementById('integratedMount').shadowRoot.getElementById('skyStatus').textContent.startsWith('V:')");check('observed_map_result_preserved',abs(float(page.locator('#integratedMount #skyMetrics strong').first.inner_text())-.005859375)<1e-6)
   page.locator('#integratedMount #uniformP').select_option('13');page.locator('#integratedMount #uniformOp').select_option('multiply')
   for key,value in [('uniformX','12'),('uniformY','11'),('uniformZ','7')]:page.locator('#integratedMount #'+key).fill(value);page.locator('#integratedMount #'+key).dispatch_event('change')
   r=page.evaluate('window.GRHExtensionReplay()');check('uniform_multiplier_correct',r['arithmetic']['final_output']==(7^(2+16))and r['arithmetic']['clean'])
   page.locator('#integratedMount #uniformOp').select_option('inverse');page.locator('#integratedMount #uniformX').fill('0');page.locator('#integratedMount #uniformX').dispatch_event('change');r=page.evaluate('window.GRHExtensionReplay()');check('inverse_zero_validity',not r['arithmetic']['valid']and r['arithmetic']['final_output']==7)
   page.locator('#integratedMount #operatorN').select_option('15');page.locator('#integratedMount #operatorSeed').select_option('29');r=page.evaluate('window.GRHExtensionReplay()');check('operator_mass',abs(r['heat']['mass']-1)<1e-12)
   evidence=json.loads((ROOT/'extension/site/verification/integration/next-steps.json').read_text());expected=next(x for x in evidence['operator']['results']if x['nodes']==15 and x['seed']==29 and x['time']==1.13);check('independent_python_operator_parity',abs(r['heat']['operator_norm_error']-expected['operator_norm_error'])<1e-12)
   check('calibration_precision_shown','4,095'in page.locator('#integratedMount #precisionResult').inner_text())
   page.locator('#tauReal').evaluate("e=>{e.value='0.5';e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));}");check('original_parameter_works','0.5'in page.locator('#tauRealOut').inner_text());check('old_state_preserves_new_state','p3_product=V'in page.url and 'next_seed=29'in page.url)
   page.reload();ready(page);check('reload_shared_state',page.locator('#integratedMount #product').input_value()=='V'and page.locator('#integratedMount #operatorSeed').input_value()=='29'and page.locator('#tauReal').input_value()=='0.5')
   with page.expect_download()as d:page.locator('#integratedMount #export').click()
   d.value.save_as(output/'replay.json');ex=json.loads((output/'replay.json').read_text());check('single_export_includes_completed_steps',ex['completedNextSteps']['arithmetic']['clean']and len(ex['asset_sha256'])==4)
   page.locator('#laboratories #resetAll').click();check('old_reset_does_not_reset_embedded',page.locator('#integratedMount #product').input_value()=='V');page.locator('#integratedMount #resetAll').click();page.wait_for_function("document.getElementById('integratedMount').shadowRoot.getElementById('skyStatus').textContent.startsWith('ILC:')")
   for name in('arithmetic','coverings','sky','completed-steps'):page.locator('#integratedMount #'+name).screenshot(path=str(output/(name+'.png')))
   page.screenshot(path=str(output/'desktop.png'),full_page=True);page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(500);check('mobile_no_horizontal_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));page.locator('#integratedMount #completed-steps').screenshot(path=str(output/'mobile-completed.png'))
   page.locator('#integratedMount #operatorN').focus();page.keyboard.press('ArrowDown');page.keyboard.press('Enter');check('keyboard_controls',page.locator('#integratedMount #operatorN').input_value()=='24')
   page.goto(base+'workbench/program3.html?curve=13&product=W');ready(page);check('old_deep_link_redirects_to_main','/workbench/program3.html'not in page.url and page.locator('#integratedMount #curve').input_value()=='13'and page.locator('#integratedMount #product').input_value()=='W');check('no_page_errors',not report['errors']);browser.close()
 except Exception as e:report['failure']=type(e).__name__+': '+str(e)
 finally:
  if server:server.shutdown();server.server_close();thread.join()
  (output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
 if report.get('failure'):raise SystemExit(1)
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--base');a=p.parse_args();run(a.output,a.base)
