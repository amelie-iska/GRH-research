// Existing Chrome CDP, no browser dependency. Read-only reference reconnaissance.
import {writeFileSync,mkdirSync} from 'node:fs';
const tabs=await(await fetch('http://127.0.0.1:9242/json')).json(),tab=tabs.find(t=>t.type==='page');
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let serial=0;const pending=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id){const cb=pending.get(m.id);if(cb){pending.delete(m.id);m.error?cb.reject(Error(JSON.stringify(m.error))):cb.resolve(m.result);}}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++serial;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});
const evaluate=async expression=>(await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true})).result.value;
await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1550,height:1000,deviceScaleFactor:1,mobile:false});
if(process.argv[2]==='open'){await send('Page.navigate',{url:'https://bbycroft.net/llm'});await new Promise(r=>setTimeout(r,6000));}
if(process.argv[3])await evaluate(process.argv[3]);
if(process.argv[2]==='hover'){await send('Input.dispatchMouseEvent',{type:'mouseMoved',x:1200,y:480});await new Promise(r=>setTimeout(r,350));}
console.log(await evaluate(`JSON.stringify({title:document.title,text:document.body.innerText.slice(0,14000),buttons:[...document.querySelectorAll('button')].map(b=>({text:b.textContent,title:b.title,rect:b.getBoundingClientRect().toJSON()})),canvas:[...document.querySelectorAll('canvas')].map(c=>c.getBoundingClientRect().toJSON())})`));
const out='outputs/renders/2026-11-03-reference-inspector';mkdirSync(out,{recursive:true});
if(process.argv[2]){const image=await send('Page.captureScreenshot',{format:'png'});writeFileSync(out+'/reference-'+process.argv[2]+'.png',Buffer.from(image.data,'base64'));}
ws.close();
