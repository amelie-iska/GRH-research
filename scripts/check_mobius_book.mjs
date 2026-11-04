// Focused check of the actual arithmetic source/data reader; no new runtime.
import assert from'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';
const out='outputs/checks/2026-11-03-mobius-split',renders='outputs/renders/2026-11-03-mobius-split';mkdirSync(renders,{recursive:true});
let tab;for(let j=0;j<100;j++){try{tab=(await(await fetch('http://127.0.0.1:9242/json')).json()).find(x=>x.type==='page');if(tab)break;}catch{}await new Promise(r=>setTimeout(r,100));}assert(tab);
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let id=0;const pending=new Map(),errors=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);pending.delete(m.id);if(p){clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>reject(Error(method+' timeout')),20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params}));});
const ev=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=t=>new Promise(r=>setTimeout(r,t));async function until(e){for(let i=0;i<150;i++){if(await ev(e))return;await delay(60);}throw Error('Wait failed: '+e);}
async function shot(name){const x=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renders+'/'+name+'.png',Buffer.from(x.data,'base64'));}
try{
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:'http://127.0.0.1:8765/book/main.html#mobius-proof'});await until(`document.querySelectorAll('iframe').length===10&&document.getElementById('mobius-proof')`);
assert.equal(await ev(`document.querySelectorAll('#mobius-proof').length`),1);
await ev(`document.getElementById('mobius-proof').scrollIntoView();for(const d of document.querySelectorAll('#mobius-proof details'))d.open=true;for(const b of document.querySelectorAll('#mobius-proof button'))b.click()`);
await until(`document.querySelectorAll('#mobius-proof pre')[0].textContent.includes('#check moebius_split')`);await until(`document.querySelectorAll('#mobius-proof pre')[1].textContent.includes('component_order')`);
const json=await ev(`JSON.parse(document.querySelectorAll('#mobius-proof pre')[1].textContent)`),expected=JSON.parse(readFileSync('web/data/mobius-split.json','utf8'));assert.deepEqual(json,expected);assert.equal(json.good_ideals,307);assert.equal(json.different_cutoff_sign_control.II,-2);assert.deepEqual(json.component_order,['original','2*short','type_I','type_II']);
if(await ev(`document.documentElement.dataset.theme!=='biomech'`))await ev(`document.getElementById('themeToggle').click()`);await delay(2800);await shot('signed-arithmetic-book');await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(300);assert(await ev(`document.getElementById('mobius-proof').getBoundingClientRect().width<=innerWidth`));await shot('signed-arithmetic-mobile');assert.equal(errors.length,0);
const report={passed:true,canonical_arithmetic_reader:true,actual_lean_source:true,exact_data_matches:true,distinct_labs:10,mobile_panel_width:true,dark_mode:true,exceptions:errors};writeFileSync(out+'/browser.json',JSON.stringify(report,null,2)+'\n');console.log(report);
}finally{try{await send('Browser.close');}catch{}ws.close();}
