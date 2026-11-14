import assert from 'node:assert/strict';import {writeFileSync,mkdirSync} from 'node:fs';
const out='outputs/checks/2026-11-04-synthetic-training',renders='outputs/renders/2026-11-04-synthetic-training';mkdirSync(renders,{recursive:true});let tab;
for(let i=0;i<300;i++){try{tab=(await(await fetch('http://127.0.0.1:9242/json')).json()).find(t=>t.type==='page');if(tab)break;}catch{}await new Promise(r=>setTimeout(r,100));}assert(tab);
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let id=0;const pending=new Map(),errors=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);pending.delete(m.id);if(p){clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>reject(Error(method)),20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params}));});
const ev=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=t=>new Promise(r=>setTimeout(r,t));async function until(s){for(let i=0;i<180;i++){if(await ev(s))return;await delay(50);}throw Error('wait:'+s);}async function shot(name){const r=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renders+'/'+name+'.png',Buffer.from(r.data,'base64'));}

async function canvasShot(id,name){const b=await ev(`(()=>{const r=document.getElementById('${id}').getBoundingClientRect();return {x:r.left+scrollX,y:r.top+scrollY,width:r.width,height:r.height,scale:1};})()`);const r=await send('Page.captureScreenshot',{format:'png',clip:b,captureBeyondViewport:true});writeFileSync(renders+'/'+name+'.png',Buffer.from(r.data,'base64'));}

try{
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:'http://127.0.0.1:8765/datasets.html'});await until('!!window.datasetExplorer');
await ev("document.documentElement.style.scrollBehavior='auto'");
const change=async(id,v)=>ev(`(()=>{const e=document.getElementById(${JSON.stringify(id)});e.value=${JSON.stringify(String(v))};e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
const result=[];
for(const id of ['1L2Y','1HRW','1AZU']){
 const index=await ev(`[...document.getElementById('datasetCase').options].findIndex(o=>o.textContent.includes('PDB residue transfer / ${id}'))`);assert(index>=0);await change('datasetCase',index);await until('window.datasetExplorer.snapshot().structureReady');
 for(const mode of ['balls','sticks']){await change('datasetRepresentation',mode);const s=await ev('window.datasetExplorer.snapshot().scene');assert(s.sourceGeometry&&s.atoms>50&&s.bonds>50&&s.bondSegments>=s.bonds*8);result.push({id,mode,...s});await ev("document.getElementById('datasetScene').scrollIntoView({block:'center'})");await shot('peptide-'+id+'-'+mode);}
 await change('datasetRepresentation','cartoon');const s=await ev('window.datasetExplorer.snapshot().scene');assert(s.ribbonPatches>80);if(id==='1L2Y')assert(s.secondary.alpha>=8);if(id==='1HRW')assert(s.secondary.strand>=6);await shot('peptide-'+id+'-cartoon');if(id==='1L2Y')await canvasShot('datasetScene','atlas-protein-ribbon');result.push({id,mode:'cartoon',...s});
 await change('datasetRepresentation','cartoon-sticks');assert((await ev('window.datasetExplorer.snapshot().scene')).bondSegments>100);
}
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});const mobile=await ev('({inner:innerWidth,scroll:document.documentElement.scrollWidth})');assert(mobile.scroll<=mobile.inner+1);assert.equal(errors.length,0);writeFileSync(out+'/molecular-browser.json',JSON.stringify({passed:true,views:result,mobile,errors},null,2)+'\n');console.log({passed:true,views:result.length,mobile});
}finally{ws.close();}
