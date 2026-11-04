// Existing local Chromium/CDP harness; no runner dependency or external service.
import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
const root='http://127.0.0.1:8765',port='http://127.0.0.1:9242';
const checkDirectory=process.argv[2]??'outputs/checks/2026-11-03-living-theme',renderDirectory=process.argv[3]??'outputs/renders/2026-11-03-living-theme';
mkdirSync(checkDirectory,{recursive:true});mkdirSync(renderDirectory,{recursive:true});
let tab;
for(const deadline=Date.now()+20000;Date.now()<deadline;){
 try{const tabs=await(await fetch(port+'/json',{signal:AbortSignal.timeout(1000)})).json();tab=tabs.find(t=>t.type==='page');if(tab)break;}catch{}
 await new Promise(r=>setTimeout(r,100));
}
assert(tab,'Isolated test browser did not become ready');
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let serial=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.id){const item=pending.get(m.id);if(item){pending.delete(m.id);clearTimeout(item.timer);m.error?item.reject(Error(JSON.stringify(m.error))):item.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>{pending.delete(id);reject(Error('CDP timeout '+method));},15000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});
async function evaluate(expression){const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw Error(JSON.stringify(result.exceptionDetails));return result.result.value;}
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function until(expression){for(let i=0;i<150;i++){if(await evaluate(expression))return;await delay(30);}throw Error('Condition timeout: '+expression);}
async function screenshot(name){const s=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renderDirectory+'/'+name+'.png',Buffer.from(s.data,'base64'));}
const report={};
async function navigate(path){await send('Page.navigate',{url:root+path});await until(`document.getElementById('themeToggle')`);}
try{
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
await navigate('/#learning');await until(`document.getElementById('model')?.options.length===6`);
assert.equal(await evaluate('document.documentElement.dataset.theme'),'light');
const position=await evaluate(`(()=>{const r=document.getElementById('themeToggle').getBoundingClientRect();return{x:r.x,y:r.y}})()`);assert(position.x<25&&position.y<25);
const values=await evaluate(`document.getElementById('trainingStats').textContent`);
await evaluate(`document.getElementById('themeToggle').click()`);assert.equal(await evaluate('document.documentElement.dataset.theme'),'biomech');assert.equal(await evaluate(`document.getElementById('themeToggle').getAttribute('aria-pressed')`),'true');
assert(await evaluate(`new Set([...document.querySelectorAll('[data-theme-material]')].map(e=>e.style.getPropertyValue('--theme-duration'))).size>=4`));
await delay(2800);assert.equal(await evaluate(`document.getElementById('trainingStats').textContent`),values);
assert(await evaluate(`document.getAnimations().some(a=>a.animationName?.startsWith('theme-')&&a.playState==='running')`));
const signalColor=await evaluate(`getComputedStyle(document.querySelector('#learning .eyebrow')).color`);await delay(900);assert.notEqual(await evaluate(`getComputedStyle(document.querySelector('#learning .eyebrow')).color`),signalColor);
await screenshot('living-learning');
await evaluate(`document.getElementById('motionToggle').click()`);assert.equal(await evaluate('document.documentElement.dataset.themeMotion'),'paused');
assert(await evaluate(`document.getAnimations().filter(a=>a.animationName?.startsWith('theme-')).every(a=>a.playState==='paused')`));
await navigate('/#learning');assert.equal(await evaluate('document.documentElement.dataset.theme'),'biomech');assert.equal(await evaluate('document.documentElement.dataset.themeMotion'),'paused');
await evaluate(`document.getElementById('motionToggle').click()`);
await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});await until(`document.documentElement.dataset.themeMotion==='paused'`);assert(await evaluate(`document.getElementById('motionToggle').disabled`));
assert(await evaluate(`document.getAnimations().filter(a=>a.animationName?.startsWith('theme-')).length===0`));
await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});await until(`document.documentElement.dataset.themeMotion==='live'`);
for(const path of ['/architecture.html','/persistence.html','/dg.html','/verification.html','/implementation-plan.html','/sources/2053.html']){await navigate(path);assert.equal(await evaluate('document.documentElement.dataset.theme'),'biomech');assert.equal(await evaluate(`document.querySelectorAll('#themeToggle').length`),1);}
await navigate('/architecture.html');await until(`document.body.dataset.ready==='true'`);assert.equal(await evaluate(`getComputedStyle(document.getElementById('selectedCell')).backgroundColor`),'rgb(16, 35, 46)');const numeric=await evaluate(`document.querySelector('#tensorGrid button')?.dataset.real`);assert(Number.isFinite(Number(numeric)));await screenshot('architecture-dark');
await navigate('/book/main.html');await until(`document.querySelectorAll('iframe').length===9`);
await evaluate(`document.getElementById('lab-dg').scrollIntoView({block:'start'})`);await until(`document.querySelector('#lab-dg iframe')?.contentDocument?.documentElement?.dataset.theme==='biomech'`);
assert.equal(await evaluate(`document.querySelector('#lab-dg iframe').contentDocument.querySelectorAll('#themeToggle').length`),0);await screenshot('book-dark');
await evaluate(`document.getElementById('themeToggle').click()`);await until(`document.querySelector('#lab-dg iframe')?.contentDocument?.documentElement?.dataset.theme==='light'`);
await evaluate(`for(let i=0;i<5;i++)document.getElementById('themeToggle').click()`);await until(`document.querySelector('#lab-dg iframe')?.contentDocument?.documentElement?.dataset.theme==='biomech'`);
await navigate('/#learning');await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(2800);assert(await evaluate('document.documentElement.scrollWidth<=innerWidth+1'));await screenshot('mobile-dark');
await evaluate(`document.getElementById('themeToggle').focus()`);await send('Input.dispatchKeyEvent',{type:'keyDown',key:' ',code:'Space',windowsVirtualKeyCode:32});await send('Input.dispatchKeyEvent',{type:'keyUp',key:' ',code:'Space',windowsVirtualKeyCode:32});assert.equal(await evaluate('document.documentElement.dataset.theme'),'light');
assert.equal(exceptions.length,0);Object.assign(report,{passed:true,staggered_transitions:true,ambient_motion_pause:true,reduced_motion:true,persistent_settings:true,all_HTML_routes:true,iframe_sync:true,numeric_values_unchanged:true,mobile_and_keyboard:true,uncaughtExceptions:exceptions});writeFileSync(checkDirectory+'/theme-browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}finally{try{await send('Browser.close');}catch{}ws.close();}
