import {Browser} from '/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import {writeFileSync} from 'node:fs';
const base=process.env.READOUT_QA_URL,out=process.env.READOUT_QA_OUTPUT;
if(!base||!out)throw Error('Explicit QA URL/output required');
const b=await new Browser().connect(),checks=[];
function check(ok,name,detail){if(!ok)throw Error(name+': '+JSON.stringify(detail));checks.push({name,detail});}
try{
 await b.viewport(1440,1000);await b.navigate(base+'/readout.html');await b.until('document.getElementById("status").textContent.includes("final certified")');
 for(const tolerance of ['1e-12','1e-15'])for(const q of [3,4,5]){
  await b.evaluate(`(()=>{document.getElementById('family').value='${q}';document.getElementById('tolerance').value='${tolerance}';document.getElementById('tolerance').dispatchEvent(new Event('change'));return true})()`);
  const state=await b.evaluate(`(()=>({status:document.getElementById('status').textContent,values:document.getElementById('values').textContent,max:Number(document.getElementById('iteration').max),step:Number(document.getElementById('iteration').value),options:document.getElementById('coefficient').options.length,link:document.getElementById('certificate').href}))()`);
  check(state.status.includes(`Conductor ${q}`)&&state.status.includes(tolerance)&&state.step===state.max&&state.options>20&&!state.values.includes('NaN')&&state.link.includes('-v3/'),'all-six-replays',state);
  await b.evaluate(`(()=>{let el=document.getElementById('iteration');el.value=0;el.dispatchEvent(new Event('input'));return true})()`);
  check((await b.evaluate('document.getElementById("values").textContent')).includes('Step = 0;'),'zero-initialization');
 }
 await b.evaluate(`(()=>{document.getElementById('play').click();return true})()`);
 await b.until('Number(document.getElementById("iteration").value)>1');
 await b.evaluate(`(()=>{document.getElementById('play').click();document.getElementById('iteration').value=document.getElementById('iteration').max;document.getElementById('iteration').dispatchEvent(new Event('input'));return true})()`);
 check(await b.evaluate('document.getElementById("play").textContent==="Play updates"'),'animation-pauses');
 await b.screenshot(out+'/readout-desktop.png');
 await b.evaluate(`(()=>{scrollTo({top:document.getElementById('convergence').getBoundingClientRect().top+scrollY-150,behavior:'instant'});return true})()`);
 await b.screenshot(out+'/readout-plots.png');
 await b.evaluate(`(()=>{document.getElementById('themeToggle').click();return true})()`);
 await b.until('document.documentElement.dataset.theme==="biomech"');
 await new Promise(r=>setTimeout(r,3500));
 await b.screenshot(out+'/readout-night.png');
 check(await b.evaluate('document.documentElement.dataset.theme==="biomech"'),'night-mode');
 await b.evaluate(`(()=>{document.getElementById('themeToggle').click();return true})()`);
 await new Promise(r=>setTimeout(r,2500));

 for(const width of [320,390,768,1440]){
  await b.viewport(width,900);
  const geo=await b.evaluate('({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,width:innerWidth,canvases:[...document.querySelectorAll("canvas")].map(x=>({width:x.clientWidth,height:x.clientHeight}))})');
  check(geo.scroll<=geo.client+1&&geo.canvases.every(x=>x.width>0&&x.height>0),'responsive-'+width,geo);
  if(width===390){await b.evaluate(`(()=>{scrollTo({top:document.getElementById('convergence').getBoundingClientRect().top+scrollY-120,behavior:'instant'});return true})()`);await b.screenshot(out+'/readout-mobile.png');}
 }
 await b.evaluate(`(()=>{document.getElementById('tolerance').value='1e-18';document.getElementById('tolerance').dispatchEvent(new Event('change'));return true})()`);
 const refusal=await b.evaluate('({message:document.getElementById("refusal").textContent,visible:!document.getElementById("refusal").hidden,chartsHidden:document.querySelector(".readout-grid").hidden,disabled:document.getElementById("play").disabled})');
 check(refusal.visible&&refusal.chartsHidden&&refusal.disabled&&refusal.message.includes('not an approximation impossibility'),'precision-refusal',refusal);
 await b.screenshot(out+'/readout-refusal.png');
 const resources=await b.evaluate(`Promise.all(['/examples/analytic_oracle/adaptive_readout.py','/data/adaptive-readout/summary-v3.json','/book/main.html'].map(async url=>{const r=await fetch(url);const text=await r.text();return {url,status:r.status,anchor:url.endsWith('main.html')?text.includes('id="ar:requested"'):true}}))`);
 check(resources.every(x=>x.status===200&&x.anchor),'source-data-proof-links',resources);
 check(b.pageErrors().length===0,'no-browser-errors',b.pageErrors());
 writeFileSync(out+'/browser-checks.json',JSON.stringify({passed:true,checks,builds_and_browser_location:'iska-linux-vscode',scope:'Six source-backed displays, exact trace endpoints, controls/refusal, four widths and live sources; not a proof of analytic inclusion.'},null,2));
 console.log(JSON.stringify({passed:true,checks:checks.length}));
}finally{await b.close();}
