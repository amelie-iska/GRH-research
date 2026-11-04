// Existing local Chromium/CDP harness; no runner dependency or external service.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const root='http://127.0.0.1:8765',port='http://127.0.0.1:9242';
const checkDirectory=process.argv[2]??'outputs/checks/2026-11-03-dg-foundations',renderDirectory=process.argv[3]??'outputs/renders/2026-11-03-dg-foundations';
mkdirSync(checkDirectory,{recursive:true});mkdirSync(renderDirectory,{recursive:true});
let tab;
for(const deadline=Date.now()+20000;Date.now()<deadline;){
 try{const tabs=await(await fetch(port+'/json',{signal:AbortSignal.timeout(1000)})).json();tab=tabs.find(t=>t.type==='page');if(tab)break;}catch{}
 await new Promise(r=>setTimeout(r,100));
}
assert(tab,'Isolated test browser did not become ready');
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let serial=0,corruptNext=false;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.method==='Fetch.requestPaused'){
 const requestId=m.params.requestId;
 if(corruptNext){corruptNext=false;send('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'application/json'}],body:Buffer.from('{"corrupted":true}').toString('base64')}).catch(error=>exceptions.push(String(error)));}
 else send('Fetch.continueRequest',{requestId}).catch(error=>exceptions.push(String(error)));
}if(m.id){const item=pending.get(m.id);if(item){pending.delete(m.id);clearTimeout(item.timer);m.error?item.reject(Error(JSON.stringify(m.error))):item.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>{pending.delete(id);reject(Error('CDP timeout '+method));},15000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});
async function evaluate(expression){const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw Error(JSON.stringify(result.exceptionDetails));return result.result.value;}
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function until(expression){for(let i=0;i<150;i++){if(await evaluate(expression))return;await delay(30);}throw Error('Condition timeout: '+expression);}
async function screenshot(name){const s=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renderDirectory+'/'+name+'.png',Buffer.from(s.data,'base64'));}
async function change(id,value,event='input'){await evaluate(`document.getElementById(${JSON.stringify(id)}).value=${JSON.stringify(value)};document.getElementById(${JSON.stringify(id)}).dispatchEvent(new Event(${JSON.stringify(event)},{bubbles:true}));`);}
const snap=()=>evaluate('window.dgLab.snapshot()'),report={};
try{
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:root+'/dg.html'});await until(`document.body?.dataset.ready==='true'`);
for(const mode of ['node','unit','zero'])for(const N of [0,1,3,6]){
 await change('mode',mode,'change');await change('size',N);const a=await snap();assert.equal(a.rank,mode==='node'?N*N:mode==='unit'?(N+1)**2:0);assert.deepEqual(a.homology,mode==='node'?[0,2*N+1]:mode==='unit'?[0,0]:[(N+1)**2,(N+1)**2]);
}
await change('mode','node','change');await change('size',3);await evaluate(`document.getElementById('dgCanvas').scrollIntoView({block:'center'})`);await screenshot('nodal-window');
for(const [phase,phrase] of [[0,'pointwise'],[180,'not linear'],[90,'does not preserve']]){await change('phase',phase);assert((await evaluate(`document.getElementById('DVR').textContent`)).includes(phrase));}
await change('phase',270);const complexText=await evaluate(`document.getElementById('clock').textContent`);assert(complexText.includes('(0.000−1.000i)ξ')&&complexText.includes('(0.000+1.000i)η'));report.negative_phase_sign=true;
const yaw=(await snap()).yaw;const rect=await evaluate(`(()=>{const r=document.getElementById('dgCanvas').getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2}})()`);
await send('Input.dispatchMouseEvent',{type:'mousePressed',x:rect.x,y:rect.y,button:'left',clickCount:1});await send('Input.dispatchMouseEvent',{type:'mouseMoved',x:rect.x+35,y:rect.y+20,button:'left',buttons:1});await send('Input.dispatchMouseEvent',{type:'mouseReleased',x:rect.x+35,y:rect.y+20,button:'left',clickCount:1});assert.notEqual((await snap()).yaw,yaw);
for(const [kind,n,row] of [['elliptic',1,[0,0,2]],['elliptic',3,[2,0,0]],['spherical',1,[0,1,1]],['spherical',2,[2,0,0]]]){await change('surface',kind,'change');await change('degree',n);assert.deepEqual((await snap()).theta.matrix[0],row);}
await evaluate(`document.getElementById('thetaCanvas').scrollIntoView({block:'center'})`);await screenshot('spherical-ext');
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(100);assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'));await screenshot('mobile');
await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:root+'/book/main.html'});await until(`document.querySelectorAll('iframe').length===7`);
assert.equal(await evaluate(`document.querySelectorAll('#lab-dg').length`),1);assert.equal(await evaluate(`new Set([...document.querySelectorAll('iframe')].map(f=>f.src)).size`),7);
await evaluate(`document.getElementById('lab-dg').scrollIntoView({block:'start'})`);await until(`document.querySelector('#lab-dg iframe').contentDocument?.body?.dataset.ready==='true'`);
const selector='#lab-dg button[data-source="/lean/NodalDG.lean"]';await evaluate(`(()=>{const b=document.querySelector('${selector}');b.closest('details').open=true;b.click();})()`);await until(`document.querySelector('${selector}').parentElement.querySelector('pre').textContent.includes('end GRHResearch.NodalDG')`);
assert.equal(await evaluate(`document.querySelector('${selector}').parentElement.querySelector('pre').textContent`),readFileSync('lean-analytic/NodalDG.lean','utf8'));
await screenshot('book-dg');assert.equal(exceptions.length,0);Object.assign(report,{passed:true,finite_windows:12,actual_theta_endpoint_cases:4,clock_DVR_conventions:true,orbit:true,mobile:true,unique_book_tools:7,literal_Lean_source:true,uncaughtExceptions:exceptions});writeFileSync(checkDirectory+'/dg-browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}finally{try{await send('Browser.close');}catch{}ws.close();}
