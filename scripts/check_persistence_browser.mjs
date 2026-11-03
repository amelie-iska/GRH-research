// Existing local Chromium/CDP harness; no runner dependency or external service.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const root='http://127.0.0.1:8765',port='http://127.0.0.1:9242';
mkdirSync('outputs/checks/2026-11-03-persistence-tools',{recursive:true});mkdirSync('outputs/renders/2026-11-03-persistence-tools',{recursive:true});
let tab;
for(let attempt=0;attempt<40;attempt++){
 try{const tabs=await(await fetch(port+'/json')).json();tab=tabs.find(t=>t.type==='page');if(tab)break;}catch{}
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
async function screenshot(name){const s=await send('Page.captureScreenshot',{format:'png'});writeFileSync('outputs/renders/2026-11-03-persistence-tools/'+name+'.png',Buffer.from(s.data,'base64'));}
async function change(id,value,event='input'){await evaluate(`document.getElementById(${JSON.stringify(id)}).value=${JSON.stringify(value)};document.getElementById(${JSON.stringify(id)}).dispatchEvent(new Event(${JSON.stringify(event)},{bubbles:true}));`);}
async function snap(){return evaluate('window.persistenceTool.snapshot()');}
const report={};
try{
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:root+'/persistence.html'});await until(`document.body.dataset.ready==='true'`);
assert.equal((await snap()).length,3);
for(const [value,length] of [['3,0;2,1;1,2;0,3',6],['5,0;3,1;1,3;0,5',13],['4,0;3,2;1,4;0,6',16]]){
 await change('idealPreset',value,'change');assert.equal((await snap()).length,length);
}
await change('customIdeal','2,;0,2');await evaluate(`document.getElementById('applyIdeal').click()`);assert.equal((await snap()).length,16);assert(await evaluate(`document.getElementById('idealStatus').classList.contains('error')`));
await change('idealPreset','2,0;1,1;0,2','change');
await evaluate(`document.getElementById('coefficientE').click()`);assert((await evaluate(`document.getElementById('bettiRanks').textContent`)).includes('(1, 4, 5, 2)'));
await change('sourceA',1);await change('sourceB',1);await change('targetA',0);
const a=await snap();assert(a.to[0]>=a.from[0]);assert((await evaluate(`document.getElementById('moduleRank').textContent`)).includes('rank = 0'));
for(const point of ['0,0','1,0','0,1','1,1']){await change('fiberPoint',point,'change');assert((await evaluate(`document.getElementById('fiberResult').textContent`)).includes(point==='0,0'?'(1,3,2)':'(0,0,0)'));}
await evaluate(`document.getElementById('fiberResult').scrollIntoView({block:'center'})`);await screenshot('staircase-resolution');
await evaluate(`document.getElementById('quantumTab').click();document.getElementById('quantum').scrollIntoView({block:'start'})`);
assert.deepEqual((await snap()).quantum.bettiA,[2,1]);assert.equal((await snap()).quantum.ranks.h1,0);
await change('radiusB',600);await change('energyB',500);assert.equal((await snap()).quantum.ranks.h1,1);
await screenshot('quantum-persistent-cycle');
await change('channel','output','change');assert.deepEqual((await snap()).quantum.bettiA,[2,1]);assert.equal((await snap()).quantum.ranks.h1,1);
await change('radiusB',800);await change('energyB',1000);assert.equal((await snap()).quantum.ranks.h1,0);
const yaw=(await snap()).yaw;const rect=await evaluate(`(()=>{const r=document.getElementById('sourceComplex').getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2}})()`);
await send('Input.dispatchMouseEvent',{type:'mousePressed',x:rect.x,y:rect.y,button:'left',clickCount:1});await send('Input.dispatchMouseEvent',{type:'mouseMoved',x:rect.x+25,y:rect.y+25,button:'left',buttons:1});await send('Input.dispatchMouseEvent',{type:'mouseReleased',x:rect.x+25,y:rect.y+25,button:'left',clickCount:1});
assert.notEqual((await snap()).yaw,yaw);
await evaluate(`document.getElementById('rankCanvas').scrollIntoView({block:'center'})`);await screenshot('rank-map');
await evaluate(`(()=>{const c=document.getElementById('rankCanvas'),r=c.getBoundingClientRect();c.dispatchEvent(new MouseEvent('click',{clientX:r.left+65,clientY:r.top+30}));})()`);
assert.equal((await snap()).quantum.from[0],0);
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(100);assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'));await screenshot('mobile-quantum');
// A rejected numerical record must leave the exact algebra tool usable.
await send('Fetch.enable',{patterns:[{urlPattern:'*data/persistence/quantum-*',requestStage:'Request'}]});corruptNext=true;
await send('Page.navigate',{url:root+'/persistence.html'});await until(`document.body.dataset.ready==='error'`);assert(await evaluate(`document.getElementById('quantumTab').disabled`));assert.equal((await snap()).length,3);assert((await evaluate(`document.getElementById('quantumStatus').textContent`)).includes('checksum mismatch'));await send('Fetch.disable');
await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
console.log('Standalone checks passed; checking book.');await send('Page.navigate',{url:root+'/book/main.html'});await until(`document.querySelectorAll('iframe').length===6`);
console.log('Book frame count passed.');assert.equal(await evaluate(`document.querySelectorAll('#lab-persistence').length`),1);
assert.equal(await evaluate(`new Set([...document.querySelectorAll('iframe')].map(f=>f.src)).size`),6);
await evaluate(`document.getElementById('lab-persistence').scrollIntoView({block:'start'})`);await until(`document.querySelector('#lab-persistence iframe').contentDocument?.body?.dataset.ready==='true'`);
await evaluate(`document.querySelector('#lab-persistence iframe').contentDocument.getElementById('quantumTab').click()`);await screenshot('book-canonical');
assert.equal(exceptions.length,0);
Object.assign(report,{passed:true,staircase_presets:4,invalid_input_preserves_model:true,coefficient_rings_and_fibers:true,monotone_grade_controls:true,nontrivial_cycle_persists_then_dies:true,same_channel_inclusion:true,orbit_and_heatmap:true,mobile:true,checksum_failure_preserves_algebra:true,canonical_embeds:6,uncaughtExceptions:exceptions});
writeFileSync('outputs/checks/2026-11-03-persistence-tools/browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}catch(error){console.error('Original failure:',error);throw error;}finally{try{await send('Browser.close');}catch(error){console.error('Test browser close failed:',error.message);}ws.close();}
