import assert from 'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';
const out='outputs/checks/2026-11-03-actual-rg',renders='outputs/renders/2026-11-03-actual-rg';mkdirSync(renders,{recursive:true});
const tabs=await(await fetch('http://127.0.0.1:9242/json')).json(),tab=tabs.find(x=>x.type==='page');assert(tab);const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let id=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails);if(m.id){const p=pending.get(m.id);pending.delete(m.id);if(p){clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>reject(Error(method+' timeout')),20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params}));});
const ev=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
const delay=t=>new Promise(r=>setTimeout(r,t));async function until(expression){for(let i=0;i<180;i++){if(await ev(expression))return;await delay(40);}throw Error('Wait failed:'+expression);}
const set=async(id,value)=>ev(`(()=>{const x=document.getElementById(${JSON.stringify(id)});x.value=${JSON.stringify(String(value))};x.dispatchEvent(new Event('input',{bubbles:true}));})()`);
async function screenshot(name){const r=await send('Page.captureScreenshot',{format:'png'});writeFileSync(renders+'/'+name+'.png',Buffer.from(r.data,'base64'));}
try{
await send('Page.enable');await send('Runtime.enable');await send('Emulation.setDeviceMetricsOverride',{width:1450,height:1100,deviceScaleFactor:1,mobile:false});await send('Page.navigate',{url:'http://127.0.0.1:8765/rg.html'});await until(`document.body?.dataset.ready==='true'`);
const lab=JSON.parse(readFileSync('web/data/rg/lab.json','utf8'));
let s=await ev('rgLab.snapshot()');assert.equal(s.mode,'classical');assert(Math.abs(s.logZ-lab.classical[0].flow[1].logZ)<1e-10);assert.equal(s.sites.length,5);
await set('rgBody','higher');assert(await ev(`document.querySelectorAll('#rgTerms tr').length>0`));await ev(`document.querySelector('#rgTerms tr').click()`);await screenshot('rg-classical');
for(const m of[5,9]){await set('rgM',m);const n=await ev(`Number(document.getElementById('rgStep').max)`),z=(await ev('rgLab.snapshot()')).logZ;for(let j=0;j<=n;j++){await set('rgStep',j);s=await ev('rgLab.snapshot()');assert(Math.abs(s.logZ-z)<1e-10);}}
await set('rgMode','quantum');for(let i=0;i<3;i++){await set('rgQuantumCase',i);const n=await ev(`Number(document.getElementById('rgStep').max)`);for(let j=0;j<=n;j++){await set('rgStep',j);assert(Math.abs((await ev('rgLab.snapshot()')).logZ-lab.quantum[i].logZ)<1e-10);}}await screenshot('rg-quantum');
await set('rgMode','chain');await set('rgStep',0);assert((await ev(`document.getElementById('rgGeometry').textContent`)).includes('periodic Ising chain'));await set('rgStep',6);assert.equal((await ev('rgLab.snapshot()')).step,6);await screenshot('rg-chain');
await set('rgMode','learned');await set('rgStep',0);await ev(`document.getElementById('rgLearnedCase').value='2';document.getElementById('rgLearnedCase').dispatchEvent(new Event('change'))`);s=await ev('rgLab.snapshot()');assert(s.params.every((x,j)=>Math.abs(x-lab.training.examples[2].parameters[j])<1e-13));assert((await ev(`document.getElementById('rgInspector').href`)).includes('actual-rg-2'));await screenshot('rg-learned');
const before=s.draws;await ev(`document.getElementById('rgOrbit').click()`);assert((await ev('rgLab.snapshot()')).draws>before);
if(await ev(`document.documentElement.dataset.theme!=='biomech'`))await ev(`document.getElementById('themeToggle').click()`);await delay(2800);await screenshot('rg-dark');
await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});await delay(250);assert(await ev('document.documentElement.scrollWidth<=innerWidth+1'));await screenshot('rg-mobile');
assert.equal(exceptions.length,0);const report={passed:true,classical_generations:[5,9],quantum_cases:3,all_scale_partitions:true,learned_saved_inputs_exact:true,orbit:true,mobile_dark:true,exceptions};writeFileSync(out+'/browser.json',JSON.stringify(report,null,2)+'\n');console.log(report);
}finally{try{await send('Browser.close');}catch{}ws.close();}
