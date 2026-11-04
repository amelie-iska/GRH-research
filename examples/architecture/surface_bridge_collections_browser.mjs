// Focused optional-collection browser checks; never changes saved records.
import assert from 'node:assert/strict';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
const requested=process.argv.slice(2);assert(requested.length&&requested.every(x=>['rg','qtoken'].includes(x)),'Pass rg and/or qtoken');
let tab;for(let i=0;i<40;i++){try{const tabs=await(await fetch('http://127.0.0.1:9242/json')).json();tab=tabs.find(t=>t.type==='page');if(tab)break;}catch{}await new Promise(r=>setTimeout(r,100));}assert(tab);
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let serial=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timer);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>reject(Error('CDP timeout '+method)),15000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});
const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function until(s){for(let i=0;i<150;i++){if(await evaluate(s))return;await delay(40);}throw Error('Timeout '+s);}
const check='outputs/checks/2026-11-03-actual-rg/architecture',render='outputs/renders/2026-11-03-inspector/actual-rg-surface';mkdirSync(check,{recursive:true});mkdirSync(render,{recursive:true});
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
const report={passed:false,collections:[],checks:[]};
for(const collection of requested){
 const base=collection==='rg'?'/data/rg/':'/data/quantum-tokengt/',manifest=JSON.parse(readFileSync('web'+base+'manifest.json'));
 await send('Page.navigate',{url:'http://127.0.0.1:8765/architecture.html?collection='+collection});await until(`document.body?.dataset.ready==='true'`);
 assert.equal(await evaluate('window.architectureInspector.snapshot().collection'),collection);assert.equal(await evaluate('document.querySelectorAll("#traceSelect option").length'),manifest.traces.length+1);
 for(const entry of manifest.traces){
  await evaluate(`window.architectureInspector.load(${JSON.stringify(entry.id)})`);await until(`document.body?.dataset.ready==='true'&&window.architectureSurface.snapshot().trace===${JSON.stringify(entry.id)}`);
  assert.equal(await evaluate('document.getElementById("recordLink").getAttribute("href")'),base+entry.file);
  const s=await evaluate('window.architectureSurface.snapshot()');assert.equal(s.genus,2);assert.equal(s.edges,5);assert.equal(s.rank,50);assert.equal(s.kind,collection==='rg'?'rg':'rg-token');
  const numerical=JSON.parse(readFileSync('web'+base+entry.file));
  for(const n of numerical.nodes){
   await evaluate(`window.architectureInspector.select(${JSON.stringify(n.id)})`);
   const cells=await evaluate(`[...document.querySelectorAll('#tensorGrid button')].map(b=>({indices:b.dataset.indices?b.dataset.indices.split(',').map(Number):[],real:Number(b.dataset.real),imag:Number(b.dataset.imag)}))`);assert(cells.length);
   for(const c of cells){let real=n.tensor.real??n.tensor.values,imag=n.tensor.imag;for(const i of c.indices){real=real[i];if(imag)imag=imag[i];}assert.equal(c.real,Number(real));assert.equal(c.imag,imag??0);}
   if(n.gate&&collection==='rg'){const roles=await evaluate('window.architectureSurface.snapshot().mapping.roles');assert.deepEqual(roles,n.wires.map(q=>['J+','J−','b'][q]));}
  }
  await evaluate(`document.getElementById('surfaceSteps').children[3].click()`);assert(await evaluate('document.getElementById("surfaceConstruction").textContent.includes("50")'));
 }
 if(collection==='rg'){
  const record=JSON.parse(readFileSync('web'+base+manifest.traces[0].file));await evaluate(`window.architectureInspector.load(${JSON.stringify(record.id)})`);await until(`document.body?.dataset.ready==='true'`);
  const gate=record.nodes.find(n=>n.gate&&n.wires.includes(2));assert(gate,'Fixture must include a b-register gate');await evaluate(`window.architectureInspector.select(${JSON.stringify(gate.id)})`);assert((await evaluate('window.architectureSurface.snapshot().mapping.roles')).includes('b'));assert.deepEqual(await evaluate('window.architectureSurface.snapshot().mapping.edges'),[]);
  await evaluate(`window.architectureInspector.select('couplings')`);assert.deepEqual(await evaluate('window.architectureSurface.snapshot().mapping.roles'),['J+']);
  const output=record.nodes.find(n=>n.tensor.axes.includes('boundary_configuration'));assert(output);await evaluate(`window.architectureInspector.select(${JSON.stringify(output.id)})`);assert.deepEqual(await evaluate('window.architectureSurface.snapshot().mapping.edges'),[0,1,2,3,4]);
  assert(await evaluate('document.getElementById("surfaceBoundary").textContent.includes("7 physical spins")'));
 }
 const clip=await evaluate(`(()=>{const r=document.getElementById('surfacePanel').getBoundingClientRect();return{x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height,scale:1}})()`);const shot=await send('Page.captureScreenshot',{format:'png',clip,captureBeyondViewport:true});writeFileSync(render+'/'+collection+'-collection.png',Buffer.from(shot.data,'base64'));
 report.collections.push({id:collection,cases:manifest.traces.length});
}
await send('Page.navigate',{url:'http://127.0.0.1:8765/architecture.html?collection=https%3A%2F%2Fexample.invalid%2Fmanifest.json'});await until(`document.body?.dataset.ready==='true'`);assert.equal(await evaluate('window.architectureInspector.snapshot().collection'),'architecture');assert.equal(await evaluate('document.querySelectorAll("#traceSelect option").length'),23);assert((await evaluate('document.getElementById("recordLink").getAttribute("href")')).startsWith('/data/architecture/records/'));
assert.equal(exceptions.length,0,JSON.stringify(exceptions));report.passed=true;report.checks=['all selected optional records load and SHA256 verify','selected-base raw links','m5 genus/passport/rank','feature registers not quiver vertices','coupling roles','full boundary support','unknown collection falls back to unchanged original23 options','no browser exceptions'];writeFileSync(check+'/optional-collections-browser-'+requested.join('-')+'.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));ws.close();
