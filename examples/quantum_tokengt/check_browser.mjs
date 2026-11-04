// Reuse only the coordinated isolated headless browser on localhost:9242.
import assert from 'node:assert/strict';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
const tabs=await(await fetch('http://127.0.0.1:9242/json')).json(),tab=tabs.find(t=>t.type==='page');assert(tab);
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let serial=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timer);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>reject(Error('CDP timeout '+method)),15000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});
const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function until(s){for(let i=0;i<150;i++){if(await evaluate(s))return;await delay(40);}throw Error('Timeout '+s);}
const out='outputs/checks/2026-11-03-actual-rg/quantum-tokengt';mkdirSync(out,{recursive:true});const report={passed:false,panels:[],tensor_tables:[],mobile:false};
const manifest=JSON.parse(readFileSync('web/data/quantum-tokengt/manifest.json')),record=JSON.parse(readFileSync('web/data/quantum-tokengt/'+manifest.file));
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1120,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:'http://127.0.0.1:8765/qtoken.html'});await until(`document.getElementById('status')?.textContent.startsWith('Verified ')`);
assert((await evaluate('document.getElementById("status").textContent')).includes(manifest.sha256.slice(0,16)));
for(const name of ['tokens','concepts','forest','gfn','topology','qec']){
 await evaluate(`document.querySelector('[data-tab="${name}"]').click()`);assert.equal(await evaluate(`document.querySelector('[data-tab="${name}"]').getAttribute('aria-selected')`),'true');
 const title=await evaluate('document.getElementById("title").textContent');assert(title.length>8);
 await evaluate(`(()=>{const s=document.getElementById('step');s.value=s.max;s.dispatchEvent(new Event('input',{bubbles:true}));})()`);
 assert((await evaluate('document.getElementById("facts").children.length'))>=5);
 const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});writeFileSync(out+'/'+name+'.png',Buffer.from(shot.data,'base64'));
 if(name==='qec'){
  assert.equal(await evaluate('document.getElementById("qecLayerPanel").hidden'),false);
  const layer=JSON.parse(readFileSync('web/data/quantum-tokengt/'+manifest.qec_layer.file));
  const rows=await evaluate(`[...document.querySelectorAll('#qecLayerTable tbody tr')].map(r=>[...r.querySelectorAll('td')].map(c=>c.textContent))`);
  assert.equal(rows.length,5);
  for(let i=0;i<5;i++){const c=layer.models['quantum-hybrid'].cases[i],[a,b,d]=c.variants;const values=[c.p,b.effective_logical_X_error,d.effective_logical_X_error,a.metrics.logweight_rmse,b.metrics.logweight_rmse,d.metrics.logweight_rmse,b.metrics.logZ_rmse,b.metrics.retained_magnetization_rmse,b.metrics.mean_TV];assert.deepEqual(rows[i],values.map(v=>v.toFixed(6)));}
  report.qec_layer_table_cases=5;
  const clip=await evaluate(`(()=>{const r=document.getElementById('qecLayerPanel').getBoundingClientRect();return{x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height,scale:1};})()`);
  const layerShot=await send('Page.captureScreenshot',{format:'png',clip,captureBeyondViewport:true});writeFileSync(out+'/qec-memory-layer.png',Buffer.from(layerShot.data,'base64'));

 }
 report.panels.push({name,title,max:await evaluate('Number(document.getElementById("step").max)')});
}
for(const name of ['features','query','key','value','scores','weights','context','basis']){
 await evaluate(`(()=>{const t=document.getElementById('tensor');t.value='${name}';t.dispatchEvent(new Event('change',{bubbles:true}));})()`);
 let matrix=name==='basis'?record.concepts.basis:record.trace[name];if(Array.isArray(matrix[0][0]))matrix=matrix[0];
 const rows=await evaluate(`[...document.querySelectorAll('#tensorValues tbody tr')].map(r=>[...r.querySelectorAll('td')].map(c=>c.textContent))`);assert.equal(rows.length,matrix.length);
 for(let i=0;i<rows.length;i++){assert.equal(rows[i].length,matrix[i].length);for(let j=0;j<rows[i].length;j++)assert.equal(rows[i][j],matrix[i][j].toFixed(6));}
 report.tensor_tables.push({name,rows:matrix.length,columns:matrix[0].length});
}
await evaluate(`document.querySelector('[data-tab="tokens"]').click();document.getElementById('play').click()`);await delay(760);assert.equal(await evaluate('document.getElementById("play").getAttribute("aria-pressed")'),'true');assert(await evaluate('Number(document.getElementById("step").value)>0'));await evaluate('document.getElementById("play").click()');
await evaluate(`(()=>{const t=document.getElementById('model');t.value='classical-hybrid';t.dispatchEvent(new Event('change',{bubbles:true}));})()`);assert.equal(await evaluate('document.querySelector("#metrics strong").textContent'),record.models['classical-hybrid'].heldout.logweight_rmse.toFixed(4));
await evaluate('document.getElementById("themeToggle").click()');assert.equal(await evaluate('document.documentElement.dataset.theme'),'biomech');await delay(250);
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(150);assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'));report.mobile=true;
const mobile=await send('Page.captureScreenshot',{format:'png'});writeFileSync(out+'/mobile-night.png',Buffer.from(mobile.data,'base64'));await evaluate(`document.querySelector('[data-tab="qec"]').click()`);assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'));report.qec_mobile=true;await evaluate('document.getElementById("themeToggle").click()');
// A corrupt optional QEC-layer record must also be rejected before display.
await evaluate(`(()=>{const original=window.fetch;window._qtokenOriginalFetch=original;window.fetch=async(...args)=>{const response=await original(...args);if(String(args[0]).includes('/data/quantum-tokengt/qec-layer-')){const text=await response.text();return new Response(text+' ',{status:200});}return response;};return import('/qtoken.mjs?layer-checksum-test='+Date.now());})()`);await until(`document.getElementById('status').textContent.includes('QEC layer checksum mismatch')`);report.qec_layer_checksum_rejection=true;await evaluate('window.fetch=window._qtokenOriginalFetch');
// Deliberate corruption must be rejected before rendering saved values.
await evaluate(`(()=>{const original=window.fetch;window.fetch=async(...args)=>{const response=await original(...args);if(String(args[0]).includes('/data/quantum-tokengt/record-')){const text=await response.text();return new Response(text+' ',{status:200,headers:{'Content-Type':'application/json'}});}return response;};return import('/qtoken.mjs?checksum-test='+Date.now());})()`);await until(`document.getElementById('status').textContent.includes('checksum mismatch')`);report.checksum_rejection=true;
assert.equal(exceptions.length,0,JSON.stringify(exceptions));report.exceptions=0;report.passed=true;writeFileSync(out+'/browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));ws.close();
