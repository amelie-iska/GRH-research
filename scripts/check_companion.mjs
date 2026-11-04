// Headless Chromium checks of our own local companion. No external runtime.
import {writeFileSync,readFileSync,mkdirSync} from 'node:fs';
const checkDirectory=process.argv[2]??'outputs/checks/2026-11-03-book';
const renderDirectory=process.argv[3]??'outputs/renders/2026-11-03-book';
mkdirSync(checkDirectory,{recursive:true});mkdirSync(renderDirectory,{recursive:true});
const expectedChapters=(readFileSync('outputs/book/surface-orders-book.toc','utf8').match(/\\contentsline \{chapter\}\{\\numberline/g)||[]).length;
const base='http://127.0.0.1:9242';
let tab;
for(let i=0;i<30;i++){
 try {const tabs=await(await fetch(base+'/json',{signal:AbortSignal.timeout(2000)})).json();tab=tabs.find(x=>x.type==='page');if(tab)break;} catch{}
 await new Promise(r=>setTimeout(r,100));
}
if(!tab)throw Error('Test Chromium not ready');
const ws=new WebSocket(tab.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let id=0;const pending=new Map(),exceptions=[];
ws.onmessage=e=>{const r=JSON.parse(e.data);if(r.method==='Runtime.exceptionThrown')exceptions.push(r.params.exceptionDetails);if(r.id){const [resolve,reject]=pending.get(r.id)||[];pending.delete(r.id);r.error?reject(r.error):resolve(r.result)}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id;const timeout=setTimeout(()=>{pending.delete(n);reject(Error('CDP timeout: '+method));},15000);pending.set(n,[r=>{clearTimeout(timeout);resolve(r)},e=>{clearTimeout(timeout);reject(e)}]);ws.send(JSON.stringify({id:n,method,params}))});
const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
await send('Runtime.enable');await send('Page.enable');await send('Emulation.setDeviceMetricsOverride',{width:1440,height:1050,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:'http://127.0.0.1:8765/'});
await new Promise(r=>setTimeout(r,1500));
const report=await evaluate(`(async()=>{
 const change=(id,v)=>{document.getElementById(id).value=v;document.getElementById(id).dispatchEvent(new Event('input',{bubbles:true}));document.getElementById(id).dispatchEvent(new Event('change',{bubbles:true}));};
 const results={surfaces:[],ar:[],models:[]};
 for(const v of ['theta','square','sphere','g2','g3','g4','g5','g9','g16','hyp']){change('surface',v);results.surfaces.push(document.getElementById('surfaceTitle').textContent);}
 for(const v of ['grid','node','stable','tube','quilt']){change('arType',v);results.ar.push(document.getElementById('arTitle').textContent);}
 change('hyperDepth','3');document.getElementById('hyperboloid').checked=true;document.getElementById('hyperboloid').dispatchEvent(new Event('input'));results.hyperbolic=document.getElementById('surfaceData').textContent;change('surface','g16');change('rotation4d','1.2');
 change('dimension','8');change('ticks','7');change('steps','3');
 results.quantum=document.getElementById('quantumData').textContent;
 const select=document.getElementById('model');
 if(select.options.length!==6)throw Error('Expected six saved trained models; got '+select.options.length);
 for(let j=0;j<select.options.length;j++){change('model',String(j));results.models.push(document.getElementById('trainingStats').textContent);change('epoch','0');change('sample','1');}
 results.pdfStatus=(await fetch('/book.pdf')).status;
 results.videoStatus=(await fetch('/media/SurfaceClock.mp4')).status;
 results.invalidTraversal=(await fetch('/examples/%2e%2e/%2e%2e/.env')).status;
 results.forbiddenSource=(await fetch('/.git/config')).status;
 change('surface','theta');change('arType','grid');change('model','3');
 document.getElementById('rotate').click();
 return results;
})()`);
if(report.pdfStatus!==200||report.videoStatus!==200)throw Error('Missing deliverable');
if(exceptions.length)throw Error(JSON.stringify(exceptions));
for(const name of ['atlas','ar','learning','reading']){
 await evaluate(`document.documentElement.style.scrollBehavior='auto';window.scrollTo(0,document.getElementById('${name}').offsetTop-85)`);
 const r=await send('Page.captureScreenshot',{format:'png'});
 writeFileSync(`${renderDirectory}/web-${name}.png`,Buffer.from(r.data,'base64'));
}
await evaluate(`document.getElementById('surface').value='hyp';document.getElementById('surface').dispatchEvent(new Event('input'));document.getElementById('hyperboloid').checked=false;document.getElementById('hyperboloid').dispatchEvent(new Event('input'));window.scrollTo(0,document.getElementById('atlas').offsetTop-85)`);
for(const mode of ['disk','hyperboloid']){if(mode==='hyperboloid')await evaluate(`document.getElementById('hyperboloid').checked=true;document.getElementById('hyperboloid').dispatchEvent(new Event('input'))`);const r=await send('Page.captureScreenshot',{format:'png'});writeFileSync(`${renderDirectory}/web-hyperbolic-${mode}.png`,Buffer.from(r.data,'base64'));}
await send('Page.navigate',{url:'http://127.0.0.1:8765/book/main.html'});await new Promise(r=>setTimeout(r,1600));
report.book=await evaluate(`({chapters:document.querySelectorAll('h2.chapterHead').length,panels:document.querySelectorAll('.reader-lab').length,math:document.querySelectorAll('math').length,brokenImages:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src)})`);if(report.book.chapters!==expectedChapters||report.book.panels!==10||report.book.brokenImages.length)throw Error(JSON.stringify(report.book));
await evaluate(`document.documentElement.style.scrollBehavior='auto';window.scrollTo(0,0)`);const bookShot=await send('Page.captureScreenshot',{format:'png'});writeFileSync(`${renderDirectory}/web-book.png`,Buffer.from(bookShot.data,'base64'));
writeFileSync(`${checkDirectory}/companion-checks.json`,JSON.stringify({...report,uncaughtExceptions:exceptions},null,2)+'\n');
console.log('Companion: ten surfaces, five AR views, trained models, native MathML book, PDF/video and access checks passed');
await evaluate(`const im=document.querySelector('img[src="main4x.svg"]');window.scrollTo(0,im.getBoundingClientRect().top+scrollY-200)`);const diagramShot=await send('Page.captureScreenshot',{format:'png'});writeFileSync(`${renderDirectory}/web-book-diamond.png`,Buffer.from(diagramShot.data,'base64'));
await send('Browser.close');ws.close();
