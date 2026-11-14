import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const out=process.argv[2]??'outputs/checks/2026-11-03-convextok',renders=process.argv[3]??'outputs/renders/2026-11-03-convextok';mkdirSync(out,{recursive:true});mkdirSync(renders,{recursive:true});
let tabs;for(let i=0;i<100;i++){try{tabs=await(await fetch('http://127.0.0.1:9242/json')).json();if(tabs.some(t=>t.type==='page'))break;}catch{}await new Promise(r=>setTimeout(r,100));}
const tab=tabs.find(t=>t.type==='page'),ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let id=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);pending.delete(m.id);if(p){clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>reject(Error(method+' timeout')),20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params}));});
const ev=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=t=>new Promise(r=>setTimeout(r,t));async function until(expression){for(let i=0;i<200;i++){if(await ev(expression))return;await delay(40);}throw Error('Wait failed:'+expression);}
const set=(id,value)=>ev(`(()=>{const x=document.getElementById(${JSON.stringify(id)});x.value=${JSON.stringify(String(value))};x.dispatchEvent(new Event('change',{bubbles:true}));})()`);
async function screenshot(name){const r=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renders+'/'+name+'.png',Buffer.from(r.data,'base64'));}
try{
 await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});
 await send('Page.navigate',{url:'http://127.0.0.1:8765/convextok.html'});await until('window.convexTokReady===true');
 const data=JSON.parse(readFileSync('web/data/convextok.json'));let cases=0,discreteModes=0;
 for(const c of data.cases){await set('ctCase',c.id);for(const r of c.results){await set('ctBudget',r.budget);for(const mode of ['Det','Bias','Int','integer']){await set('ctScheme',mode);assert((await ev("document.getElementById('ctMetrics').textContent")).includes(String(r.integer.value)));assert(await ev("document.querySelectorAll('#ctDag path').length>0"));assert.equal(await ev("document.querySelectorAll('#ctColours input:checked').length"),mode==='integer'?r.integer.vocabulary.length:r.lp.rounded[mode].vocabulary.length);discreteModes++;}cases++;}}
 await set('ctCase','gap');await set('ctBudget',2);await set('ctScheme','Int');await screenshot('integrality-gap');
 await set('ctOverlay','lp');assert(await ev("[...document.querySelectorAll('#ctDag path title')].some(t=>t.textContent.includes('1/2'))"));await screenshot('fractional-flow');
 await ev("document.querySelector('#ctColours input:checked').click()");assert(await ev("document.getElementById('ctManual').textContent.length>0"));await ev("document.getElementById('ctReset').click()");assert.equal(await ev("document.getElementById('ctManual').textContent"),'');
 await set('ctCase','surface-g4');await set('ctScheme','integer');await screenshot('genus-four-paths');
 if(await ev("document.documentElement.dataset.theme!=='biomech'"))await ev("document.getElementById('themeToggle').click()");await delay(2800);await screenshot('night');
 await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(200);assert(await ev('document.documentElement.scrollWidth<=innerWidth+1'));await screenshot('mobile');
 await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:'http://127.0.0.1:8765/book/main.html#lab-convextok'});await until("document.querySelectorAll('iframe').length===11");await ev("document.getElementById('lab-convextok').scrollIntoView()");await until("document.querySelector('#lab-convextok iframe')?.contentWindow?.convexTokReady===true");assert.equal(await ev("document.querySelectorAll('iframe[src=\"/convextok.html?embed=book\"]').length"),1);await screenshot('book');
 await ev("document.querySelector('#lab-convextok .load-code').click()");await until("document.querySelector('#lab-convextok pre').textContent.includes('def certify')");
 await ev("document.querySelector('#lab-relations button[data-source=\"/lean/BranchExtension.lean\"]').click()");await until("document.querySelector('#lab-relations button[data-source=\"/lean/BranchExtension.lean\"]').parentElement.querySelector('pre').textContent.includes('no_module_section')");
 assert.equal(exceptions.length,0);const report={passed:true,budget_cases:cases,discrete_modes:discreteModes,manual_reset:true,fractional_flow:true,genus_four:true,night_mobile:true,unique_canonical_book:true,actual_code_and_lean_sources:true,exceptions};writeFileSync(out+'/browser.json',JSON.stringify(report,null,2)+'\n');console.log(report);
}finally{try{await send('Browser.close');}catch{}ws.close();}
