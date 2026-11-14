import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const root='http://127.0.0.1:8765',port='http://127.0.0.1:9242',renderDirectory=process.argv[3]??'outputs/renders/2026-11-03-reference-inspector';
const checkDirectory=process.argv[2]??'outputs/checks/2026-11-03-reference-inspector';mkdirSync(checkDirectory,{recursive:true});mkdirSync(renderDirectory,{recursive:true});
let tab;
for(let attempt=0;attempt<40;attempt++){
 try{const tabs=await(await fetch(port+'/json')).json();tab=tabs.find(t=>t.type==='page');if(tab)break;}catch{}
 await new Promise(r=>setTimeout(r,100));
}
assert(tab,'Isolated test browser did not become ready');
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let serial=0,corruptNext=false;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown'&&!m.params.exceptionDetails.url?.startsWith('https://bbycroft.net'))exceptions.push(m.params.exceptionDetails);if(m.method==='Fetch.requestPaused'){
 const requestId=m.params.requestId;
 if(corruptNext){corruptNext=false;send('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'application/json'}],body:Buffer.from('{"corrupted":true}').toString('base64')}).catch(error=>exceptions.push(String(error)));}
 else send('Fetch.continueRequest',{requestId}).catch(error=>exceptions.push(String(error)));
}if(m.id){const item=pending.get(m.id);if(item){pending.delete(m.id);clearTimeout(item.timer);m.error?item.reject(Error(JSON.stringify(m.error))):item.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>{pending.delete(id);reject(Error('CDP timeout '+method));},15000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params}));});
async function evaluate(expression){const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw Error(JSON.stringify(result.exceptionDetails));return result.result.value;}
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function until(expression){for(let i=0;i<150;i++){if(await evaluate(expression))return;await delay(30);}throw Error('Condition timeout: '+expression);}
async function screenshot(name){const s=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renderDirectory+'/'+name+'.png',Buffer.from(s.data,'base64'));}
await send('Runtime.enable');await send('Page.enable');exceptions.length=0;
await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
const report={cases:[],screenshots:[],exceptions};
async function page(query=''){
 await send('Page.navigate',{url:root+'/architecture.html'+query});await until(`document.body?.dataset.ready==='true'`);await delay(80);
}
async function load(id){await evaluate(`window.architectureInspector.load(${JSON.stringify(id)})`);await until(`document.body?.dataset.ready==='true'&&window.architectureInspector.snapshot().trace===${JSON.stringify(id)}`);}
async function select(id){await evaluate(`window.architectureInspector.select(${JSON.stringify(id)})`);assert.equal(await evaluate('window.architectureInspector.snapshot().node'),id);}
async function click(id){await evaluate(`document.getElementById(${JSON.stringify(id)}).click()`);}
async function capture(name){await delay(140);await screenshot(name);report.screenshots.push(name);}
async function numeric(trace){
 const snap=await evaluate('window.architectureInspector.snapshot()'),t=trace.nodes.find(n=>n.id===snap.node).tensor;
 const cells=await evaluate(`[...document.querySelectorAll('#tensorGrid button')].map(b=>({ix:b.dataset.indices?b.dataset.indices.split(',').map(Number):[],r:Number(b.dataset.real),i:Number(b.dataset.imag)}))`);assert(cells.length);
 for(const c of cells){let r=t.real??t.values,i=t.imag;for(const k of c.ix){r=r[k];if(i)i=i[k];}assert.equal(c.r,Number(r));assert.equal(c.i,i??0);}return cells.length;
}
await page('?trace=tokengt-softmax&node=layer0.scores');
const canvas=await evaluate(`document.getElementById('scene').getBoundingClientRect().toJSON()`);
let lens=await evaluate(`window.architectureInspector.snapshot().viewport.cellPlanes.find(p=>p.lens)`);assert(lens);
const center={x:canvas.x+lens.points[0][0]+(lens.points[1][0]-lens.points[0][0])*1.5/lens.columns,y:canvas.y+lens.points[0][1]+(lens.points[3][1]-lens.points[0][1])*1.5/lens.rows};
await send('Input.dispatchMouseEvent',{type:'mouseMoved',...center});await until(`!document.getElementById('cellTooltip').hidden`);assert((await evaluate(`document.getElementById('cellTooltip').textContent`)).includes('[0, 0, 1, 1]'));
await capture('attention-cell-hover');
await send('Input.dispatchMouseEvent',{type:'mousePressed',button:'left',clickCount:1,...center});await send('Input.dispatchMouseEvent',{type:'mouseReleased',button:'left',clickCount:1,...center});
assert.deepEqual(await evaluate('window.architectureInspector.snapshot().selectedIndices'),[0,0,1,1]);assert((await evaluate(`document.getElementById('dependencyCheck').textContent`)).includes('absolute residual'));
await evaluate(`document.getElementById('scene').scrollIntoView({block:'center'})`);await capture('attention-cell-selected');
await click('overview');assert.equal(await evaluate(`document.getElementById('sceneRange').value`),'all');await capture('attention-overview');
await click('focusOperation');
const pan=await evaluate('window.architectureInspector.snapshot().viewport.pan.x');await click('panRight');assert.notEqual(await evaluate('window.architectureInspector.snapshot().viewport.pan.x'),pan);
const yaw=await evaluate('window.architectureInspector.snapshot().yaw');await click('rotateRight');assert.notEqual(await evaluate('window.architectureInspector.snapshot().yaw'),yaw);
const c=await evaluate(`document.getElementById('scene').getBoundingClientRect().toJSON()`);await send('Input.dispatchMouseEvent',{type:'mouseWheel',x:c.x+c.width/2,y:c.y+c.height/2,deltaX:0,deltaY:-100});assert(await evaluate('window.architectureInspector.snapshot().zoom>1'));
await evaluate(`document.getElementById('scene').focus()`);await send('Input.dispatchKeyEvent',{type:'keyDown',key:'f',code:'KeyF'});await send('Input.dispatchKeyEvent',{type:'keyUp',key:'f',code:'KeyF'});assert.equal(await evaluate('window.architectureInspector.snapshot().zoom'),1);
const screenshots=new Set();
for(const [collection,base] of [['architecture','architecture'],['rg','rg'],['qtoken','quantum-tokengt']]){
 await page(collection==='architecture'?'':'?collection='+collection);
 const manifest=JSON.parse(readFileSync('web/data/'+base+'/manifest.json'));
 for(const entry of manifest.traces){
  await load(entry.id);const trace=JSON.parse(readFileSync('web/data/'+base+'/'+entry.file));
  let cells=await numeric(trace);const v=await evaluate('window.architectureInspector.snapshot().viewport');assert(v.visiblePlanes>0);assert(v.cellPlanes.some(p=>p.lens));
  const operation=trace.nodes.find(n=>/(^|\.)scores$/.test(n.id))??trace.nodes.find(n=>n.gate)??trace.nodes.find(n=>n.id==='critic.logits')??trace.nodes.find(n=>n.id==='step2.forward_mean');
  if(operation){await select(operation.id);cells+=await numeric(trace);}
  if(!screenshots.has(v.family)){screenshots.add(v.family);await evaluate('window.scrollTo(0,0)');await capture('family-'+v.family);}
  if(entry.id==='toricgt-soft-moe'){await select('layer0.moe.dispatch');await capture('expert-dispatch');}
  if(entry.id==='tropical-ring'){await select('layer0.context');assert((await evaluate(`document.getElementById('selectedCell').textContent`)).includes('witness keys'));await capture('tropical-context');}
  if(entry.id==='qcnn-9-0'){await select('circuit.layer0.ry0');assert((await evaluate(`document.getElementById('dependencyFormula').textContent`)).includes('RY'));await capture('quantum-gate');}
  if(entry.id==='quantum-tokengt-rg-hybrid'){await select('context');assert((await evaluate(`document.getElementById('dependencyFormula').textContent`)).includes('½'));await capture('quantum-features-classical-attention');}
  const order=await evaluate('window.architectureInspector.snapshot().drawOrder');assert(order.every((h,i)=>!i||order[i-1].depth>=h.depth));
  report.cases.push({collection,id:entry.id,family:v.family,cells});
 }
}
// Retain loading/playback guards, final-choice race handling, checksum rejection.
await page();
await evaluate(`window.architectureInspector.load('qcnn-9-0');document.getElementById('play').click()`);assert.equal(await evaluate('window.architectureInspector.snapshot().playing'),false);await until(`document.body?.dataset.ready==='true'&&window.architectureInspector.snapshot().trace==='qcnn-9-0'`);
await click('resetStep');await click('play');await delay(750);assert.equal(await evaluate('window.architectureInspector.snapshot().playing'),true);await click('play');assert.equal(await evaluate('window.architectureInspector.snapshot().playing'),false);
await evaluate(`for(const id of ['qcnn-9-0','photonic-0','tokengt-softmax'])window.architectureInspector.load(id)`);await until(`document.body?.dataset.ready==='true'&&window.architectureInspector.snapshot().trace==='tokengt-softmax'`);
await send('Fetch.enable',{patterns:[{urlPattern:'*data/architecture/records/*',requestStage:'Request'}]});corruptNext=true;await evaluate(`window.architectureInspector.load('qcnn-4-8')`);await until(`document.body?.dataset.ready==='error'`);assert.equal(await evaluate('window.architectureInspector.snapshot().trace'),'tokengt-softmax');assert((await evaluate(`document.getElementById('loadStatus').textContent`)).includes('checksum mismatch'));await send('Fetch.disable');await load('tokengt-softmax');
await select('layer0.winners');assert((await evaluate(`document.getElementById('walkthroughText').textContent`)).includes('comparison diagnostic'));await load('tropical-ring');await select('layer0.weights');assert((await evaluate(`document.getElementById('walkthroughText').textContent`)).includes('comparison diagnostic'));
await load('clock-carrier');await capture('clock-carrier');
await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});await select('U');await select('V');assert.equal(await evaluate('window.architectureInspector.snapshot().node'),'V');
await click('themeToggle');await delay(120);assert.equal(await evaluate('document.documentElement.dataset.theme'),'biomech');await capture('shared-night');
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
for(const query of ['','?collection=rg','?collection=qtoken']){await page(query);assert(await evaluate('document.documentElement.scrollWidth<=window.innerWidth+1'));}await capture('mobile');
await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});await send('Emulation.setEmulatedMedia',{features:[]});
await page('?collection=untrusted&trace=invalid&node=invalid');assert.equal(await evaluate('window.architectureInspector.snapshot().collection'),'architecture');assert.equal(await evaluate('window.architectureInspector.snapshot().trace'),'qcnn-4-0');
await send('Page.navigate',{url:root+'/book/main.html'});await until(`document.getElementById('lab-architecture')`);assert.equal(await evaluate(`document.querySelectorAll('#lab-architecture iframe').length`),1);assert.equal(await evaluate(`[...document.querySelectorAll('iframe')].filter(f=>f.src.includes('/architecture.html')).length`),1);
assert.equal(exceptions.length,0,JSON.stringify(exceptions));report.passed=true;report.guards={pending_load_pause:true,last_choice_wins:true,checksum_rejected:true,coordinate_picking:true,overview_focus:true,pan_orbit_zoom_fit_keyboard:true,diagnostic_labels:true,reduced_motion:true,shared_theme:true,mobile_all_collections:true,unique_book_frame:true};
writeFileSync(checkDirectory+'/browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,cases:report.cases.length,screenshots:report.screenshots.length}));ws.close();
