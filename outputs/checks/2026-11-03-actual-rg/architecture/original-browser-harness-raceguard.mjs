// Existing local Chromium/CDP harness; no runner dependency or external service.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const root='http://127.0.0.1:8765',port='http://127.0.0.1:9242';
const checkDirectory=process.argv[2]??'outputs/checks/2026-11-03-inspector',renderDirectory=process.argv[3]??'outputs/renders/2026-11-03-inspector';
mkdirSync(checkDirectory,{recursive:true});mkdirSync(renderDirectory,{recursive:true});
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
async function screenshot(name){const s=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renderDirectory+'/'+name+'.png',Buffer.from(s.data,'base64'));}
async function change(id,value){await evaluate(`document.getElementById(${JSON.stringify(id)}).value=${JSON.stringify(value)};document.getElementById(${JSON.stringify(id)}).dispatchEvent(new Event('change',{bubbles:true}));`);}
async function select(id){const generation=await evaluate('window.architectureInspector?.snapshot().generation??0');await change('traceSelect',id);await until(`document.body?.dataset.ready==='true'&&window.architectureInspector.snapshot().trace===${JSON.stringify(id)}&&window.architectureInspector.snapshot().generation>${generation}`);}
async function node(id){await evaluate(`document.querySelectorAll('#nodeList button').forEach(b=>{if(b.dataset.node===${JSON.stringify(id)})b.click()})`);assert.equal(await evaluate('window.architectureInspector.snapshot().node'),id);}
function record(id){const m=JSON.parse(readFileSync('web/data/architecture/manifest.json'));const t=m.traces.find(t=>t.id===id);return JSON.parse(readFileSync('web/data/architecture/'+t.file));}
async function assertCells(trace){
 const id=await evaluate('window.architectureInspector.snapshot().node'),t=trace.nodes.find(n=>n.id===id).tensor;
 const cells=await evaluate(`[...document.querySelectorAll('#tensorGrid button')].map(b=>({indices:b.dataset.indices?b.dataset.indices.split(',').map(Number):[],real:Number(b.dataset.real),imag:Number(b.dataset.imag)}))`);
 assert(cells.length>0);
 for(const cell of cells){let r=t.real??t.values,i=t.imag;for(const k of cell.indices){r=r[k];if(i)i=i[k];}assert.equal(cell.real,Number(r));assert.equal(cell.imag,i??0);}
 return cells.length;
}
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:root+'/architecture.html'});await until(`document.body?.dataset.ready==='true'`);
const manifest=JSON.parse(readFileSync('web/data/architecture/manifest.json'));const report={cases:[],screenshots:[]};
const pendingPlay=await evaluate(`(()=>{window.architectureInspector.load('qcnn-9-0');document.getElementById('play').click();return window.architectureInspector.snapshot().playing})()`);assert.equal(pendingPlay,false,'Play must stay paused during a pending record load');await until(`document.body?.dataset.ready==='true'&&window.architectureInspector.snapshot().trace==='qcnn-9-0'`);
assert.equal(await evaluate('document.querySelectorAll("#traceSelect option").length'),23);
for(const entry of manifest.traces){
 await select(entry.id);const cells=await assertCells(record(entry.id));
 const evidence=await evaluate('document.getElementById("evidenceBadge").textContent');assert(evidence.includes(entry.kind==='trained-checkpoint-replay'?'TRAINED':'FIXED'));
 report.cases.push({id:entry.id,cells,evidence});
}
await select('qcnn-9-0');await screenshot('quantum-scene');report.screenshots.push('quantum-scene');
await evaluate(`document.getElementById('resetStep').click();document.getElementById('play').click()`);await delay(850);
assert.equal(await evaluate('window.architectureInspector.snapshot().playing'),true);assert.notEqual(await evaluate('window.architectureInspector.snapshot().node'),'parameters');
await evaluate(`document.getElementById('play').click()`);assert.equal(await evaluate('window.architectureInspector.snapshot().playing'),false);
const yaw=await evaluate('window.architectureInspector.snapshot().yaw');await evaluate(`document.getElementById('rotateRight').click()`);assert.notEqual(await evaluate('window.architectureInspector.snapshot().yaw'),yaw);
for(let k=0;k<10;k++){
 await evaluate(`document.getElementById('rotateRight').click()`);
 const order=await evaluate('window.architectureInspector.snapshot().drawOrder');
 assert(order.every((v,i)=>i===0||order[i-1].depth>=v.depth),'Painter and picking order must be camera depth, far to near');
}
assert(await evaluate(`[...document.querySelectorAll('#nodeList button')].every(b=>!b.hasAttribute('role'))`));
await evaluate(`document.getElementById('resetView').click()`);
const bounds=await evaluate(`(()=>{const r=document.getElementById('scene').getBoundingClientRect();return{x:r.left+r.width/2,y:r.top+r.height/2}})()`);
await send('Input.dispatchMouseEvent',{type:'mouseWheel',x:bounds.x,y:bounds.y,deltaX:0,deltaY:-100});assert(await evaluate('window.architectureInspector.snapshot().zoom>1'));
await node('circuit.layer0.ry0');assert((await evaluate('document.getElementById("formula").textContent')).includes('angle'));
assert.equal(await evaluate('document.getElementById("circuitPanel").hidden'),false);
await evaluate(`document.getElementById('circuitPanel').scrollIntoView({block:'start'})`);await screenshot('quantum-circuit');report.screenshots.push('quantum-circuit');
await select('tropical-ring');await node('layer0.context');await assertCells(record('tropical-ring'));assert((await evaluate('document.getElementById("selectedCell").textContent')).includes('witness keys'));
await evaluate('window.scrollTo(0,0)');await screenshot('tropical');report.screenshots.push('tropical');
await node('layer0.scores');await evaluate(`(()=>{const input=document.querySelector('#sliceAxes input[data-axis="1"]');input.value=1;input.dispatchEvent(new Event('input',{bubbles:true}))})()`);await assertCells(record('tropical-ring'));
await node('layer0.block_contexts');assert(await evaluate(`!![...document.querySelectorAll('#tensorGrid button')].find(b=>b.dataset.indices==='0,0,0,3,0'&&b.classList.contains('masked'))`));
await select('toricgt-soft-moe');await node('layer0.moe.dispatch');await evaluate(`(()=>{const input=document.querySelector('#sliceAxes input[data-axis="1"]');input.value=3;input.dispatchEvent(new Event('input',{bubbles:true}))})()`);
assert(await evaluate(`[...document.querySelectorAll('#tensorGrid button')].every(b=>Number(b.dataset.real)===0)`));assert((await evaluate('document.getElementById("selectedCell").textContent')).includes('TOKENS'));
await node('layer0.moe.combine');await evaluate('window.scrollTo(0,0)');await screenshot('experts');report.screenshots.push('experts');
await select('photonic-0');assert.equal(await evaluate('document.getElementById("photonicPanel").hidden'),false);await change('quadraturePair','0,2');assert((await evaluate('document.getElementById("covarianceCaption").textContent')).includes('Gaussian marginal'));
await screenshot('photonic');report.screenshots.push('photonic');
await select('toricgt-quantum-hybrid-0');assert.equal(await evaluate('document.getElementById("certificatePanel").hidden'),false);assert((await evaluate('document.getElementById("certificateStatus").textContent')).includes('repaired'));
assert.equal((await evaluate('document.getElementById("principalMinors").textContent')).split('\n').length,15);await screenshot('hybrid');report.screenshots.push('hybrid');
await select('clock-carrier');await change('clockDimension','8');await until('window.architectureInspector.snapshot().checks.weyl.error<1e-10&&document.getElementById("shape").textContent.includes("8")');
await change('clockTicks','7');await until('window.architectureInspector.snapshot().nodes===17');assert((await evaluate('document.getElementById("conventions").textContent')).includes('forward'));
await node('U');await evaluate(`document.getElementById('component').value='phase';document.getElementById('component').dispatchEvent(new Event('input'))`);
assert(await evaluate(`!![...document.querySelectorAll('#tensorGrid button')].find(b=>b.dataset.indices==='0,1'&&b.textContent==='—')`));
// Invalid live parameters retain the prior valid record and label the error.
await change('clockDimension','2');await until(`document.body?.dataset.ready==='error'`);assert.equal(await evaluate('document.getElementById("clockDimension").value'),'8');assert((await evaluate('document.getElementById("loadStatus").textContent')).includes('previous valid case'));
await change('clockDimension','8');await until(`document.body?.dataset.ready==='true'`);
// Rapid changes must settle on the final choice, including aborted large records.
await evaluate(`const s=document.getElementById('traceSelect');for(const id of ['qcnn-9-0','photonic-0','tokengt-softmax']){s.value=id;s.dispatchEvent(new Event('change',{bubbles:true}));}`);
await until(`window.architectureInspector.snapshot().trace==='tokengt-softmax'&&document.body?.dataset.ready==='true'`);
await send('Fetch.enable',{patterns:[{urlPattern:'*data/architecture/records/*',requestStage:'Request'}]});corruptNext=true;
await change('traceSelect','qcnn-4-8');await until(`document.body?.dataset.ready==='error'`);
assert.equal(await evaluate('window.architectureInspector.snapshot().trace'),'tokengt-softmax');assert((await evaluate('document.getElementById("loadStatus").textContent')).includes('checksum mismatch'));
await send('Fetch.disable');await select('tokengt-softmax');report.corrupted_record_rejected_without_changing_source_files=true;
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(100);await screenshot('mobile');report.screenshots.push('mobile');
assert(await evaluate('document.documentElement.scrollWidth<=window.innerWidth+1'));
await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1100,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:root+'/architecture.html?trace=not-a-record&node=invalid'});await until(`document.body?.dataset.ready==='true'`);assert.equal(await evaluate('window.architectureInspector.snapshot().trace'),'qcnn-4-0');
await send('Page.navigate',{url:root+'/book/main.html'});await until(`document.querySelectorAll('iframe').length===7`);
const book=await evaluate(`({chapters:document.querySelectorAll('h2.chapterHead').length,sources:[...document.querySelectorAll('iframe')].map(f=>f.getAttribute('src')),canonical:document.querySelectorAll('#lab-architecture').length})`);
const toc=readFileSync('outputs/book/surface-orders-book.toc','utf8'),expectedChapters=(toc.match(/\\contentsline \{chapter\}\{\\numberline/g)||[]).length;
assert.equal(book.chapters,expectedChapters);assert.equal(new Set(book.sources).size,7);assert.equal(book.canonical,1);
await evaluate(`document.getElementById('lab-architecture').scrollIntoView({block:'start'})`);
await until(`document.querySelector('#lab-architecture iframe').contentDocument?.body?.dataset.ready==='true'`);
await evaluate(`(()=>{const d=document.querySelector('#lab-architecture iframe').contentDocument;const s=d.getElementById('traceSelect');s.value='photonic-0';s.dispatchEvent(new Event('change',{bubbles:true}));})()`);
await until(`document.querySelector('#lab-architecture iframe').contentWindow.architectureInspector.snapshot().trace==='photonic-0'`);
await screenshot('book-inspector');report.screenshots.push('book-inspector');report.book=book;
assert.equal(exceptions.length,0);report.passed=true;report.uncaughtExceptions=exceptions;report.data_cases=22;report.computed_clock=true;report.numeric_cells_match_saved_records=true;report.play_pause_orbit_zoom_slices_masks_certificates_mobile=true;
writeFileSync(checkDirectory+'/architecture-browser.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,cases:report.cases.length,screenshots:report.screenshots.length}));
await send('Browser.close');ws.close();
