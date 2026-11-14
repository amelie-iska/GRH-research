/** Use the existing loopback CDP browser only after its current owner releases it. */
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../../',import.meta.url));
const evidence=root+'outputs/checks/2026-11-03-convextok/browser-'+Date.now();
mkdirSync(evidence,{recursive:true});
const data=JSON.parse(readFileSync(root+'web/data/convextok.json','utf8'));
const tabs=await(await fetch('http://127.0.0.1:9242/json')).json();
const tab=tabs.find(t=>t.type==='page');assert(tab,'No CDP page available');
const ws=new WebSocket(tab.webSocketDebuggerUrl);
await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let id=0;const pending=new Map(),exceptions=[],badResponses=[];
ws.onmessage=e=>{
  const m=JSON.parse(e.data);
  if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);
  if(m.method==='Network.responseReceived'&&m.params.response.status>=400)badResponses.push({url:m.params.response.url,status:m.params.response.status});
  if(m.id){const p=pending.get(m.id);pending.delete(m.id);if(p){clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}
};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>reject(Error(method+' timeout')),20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params}));});
const ev=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=t=>new Promise(r=>setTimeout(r,t));
async function until(expression){for(let i=0;i<200;i++){if(await ev(expression))return;await delay(40);}throw Error('Wait failed: '+expression);}
const set=(target,value)=>ev(`(()=>{const s=document.getElementById(${JSON.stringify(target)});s.value=${JSON.stringify(String(value))};s.dispatchEvent(new Event('change',{bubbles:true}));})()`);
async function shot(name){const r=await send('Page.captureScreenshot',{format:'png'});writeFileSync(evidence+'/'+name+'.png',Buffer.from(r.data,'base64'),{flag:'wx'});}
try{
  await send('Page.enable');await send('Runtime.enable');await send('Network.enable');
  await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});
  await send('Page.navigate',{url:'http://127.0.0.1:8765/convextok.html'});
  await until('window.convexTokReady===true');
  let controls=0;
  for(const c of data.cases){
    await set('ctCase',c.id);
    for(const r of c.results){
      await set('ctBudget',r.budget);
      for(const scheme of ['Det','Bias','Int','integer']){
        await set('ctScheme',scheme);
        const expected=scheme==='integer'?r.integer.value:r.lp.rounded[scheme].dp_count;
        const actual=await ev(`({metrics:[...document.querySelectorAll('#ctMetrics strong')].map(e=>e.textContent),rows:document.querySelectorAll('#ctSegments .ct-row').length,chosen:document.querySelectorAll('#ctColours input:checked').length,status:document.getElementById('ctStatus').textContent})`);
        assert.equal(actual.metrics[0],r.lp.value);assert.equal(Number(actual.metrics[1]),r.integer.value);assert.equal(Number(actual.metrics[2]),expected);assert.equal(actual.rows,c.words.length);assert(actual.chosen<=r.budget);controls++;
      }
    }
  }
  await set('ctCase','gap');await set('ctScheme','Det');await set('ctOverlay','lp');
  assert(await ev(`document.querySelectorAll('#ctDag .flow').length>0`));
  assert(await ev(`[...document.querySelectorAll('#ctDag title')].some(e=>e.textContent.includes('1/2'))`));
  const initial=await ev(`document.querySelectorAll('#ctColours input:checked').length`);
  await ev(`document.querySelector('#ctColours input:not(:checked)').click()`);
  assert.equal(await ev(`document.querySelectorAll('#ctColours input:checked').length`),initial);
  assert(await ev(`document.getElementById('ctManual').textContent.includes('full')`));
  await ev(`document.querySelector('#ctColours input:checked').click()`);
  assert.equal(await ev(`document.querySelectorAll('#ctColours input:checked').length`),initial-1);
  assert(await ev(`document.getElementById('ctStatus').textContent.startsWith('Manual')`));
  await ev(`document.getElementById('ctReset').click()`);
  assert.equal(await ev(`document.querySelectorAll('#ctColours input:checked').length`),initial);
  await shot('desktop');
  if(await ev(`document.documentElement.dataset.theme!=='biomech'`))await ev(`document.getElementById('themeToggle').click()`);
  await until(`document.documentElement.dataset.theme==='biomech'`);
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(250);
  assert(await ev('document.documentElement.scrollWidth<=innerWidth+1'));
  await shot('mobile-dark');
  const links=await ev(`Promise.all([...document.querySelectorAll('a[href^="/"]')].map(a=>fetch(a.pathname).then(r=>({url:a.pathname,status:r.status}))))`);
  assert(links.every(l=>l.status===200),JSON.stringify(links));
  assert.equal(exceptions.length,0,JSON.stringify(exceptions));assert.equal(badResponses.length,0,JSON.stringify(badResponses));
  const report={passed:true,controls,corpora:data.cases.length,exact_displayed_bounds:true,fractional_flow:true,manual_budget_guard:true,reset:true,mobile_dark:true,local_links:links,exceptions,badResponses,evidence};
  writeFileSync(evidence+'/report.json',JSON.stringify(report,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(report));
}finally{ws.close();}
