#!/usr/bin/env node
// Focused candidate-only paired cutoff QA. No legacy lab/model/release suite is run.
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {readFileSync, writeFileSync, mkdirSync, existsSync, realpathSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const ROOT='/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104';
const STAGE=realpathSync(process.env.CUTOFF_STAGE_ROOT);assert(STAGE.startsWith(ROOT+'/outputs/checks/2026-11-09-mid-divisor/'));
const HELPER='/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
const require=createRequire(HELPER), WebSocket=require('ws');
const sha=x=>createHash('sha256').update(x).digest('hex');
const delay=ms=>new Promise(r=>setTimeout(r,ms));
const argv=process.argv.slice(2),opts={};
for(let i=0;i<argv.length;i+=2){assert(argv[i].startsWith('--')&&argv[i+1],'Expected --name value');assert(!Object.hasOwn(opts,argv[i]),'Duplicate argument');opts[argv[i]]=argv[i+1];}
const keys=['--base','--out','--native-record','--native-record-sha256','--pdf-record','--pdf-record-sha256','--phase','--hosted-html-sha256'];
assert.deepEqual(Object.keys(opts).sort(),keys.sort(),'Exact required options');
const base=opts['--base'].replace(/\/$/,''),origin=new URL(base);
const phase=opts['--phase'];
assert(['stage','live'].includes(phase));
assert(phase==='stage' ? origin.protocol==='http:'&&origin.hostname==='127.0.0.1'&&origin.port&&origin.pathname==='/GRH-research' : base==='https://amelie-iska.github.io/GRH-research','Only owned staging and the approved public project');
assert(!origin.username&&!origin.password&&!origin.search&&!origin.hash,'No credentials/query/fragment');
const out=path.resolve(opts['--out']),outRoot=ROOT+'/outputs/checks/2026-11-09-mid-divisor/';
assert(out.startsWith(outRoot)&&!existsSync(out),'New owned output directory required');
mkdirSync(path.dirname(out),{recursive:true});const actualParent=realpathSync(path.dirname(out)),ownedRoot=realpathSync(outRoot);assert(actualParent===ownedRoot||actualParent.startsWith(ownedRoot+'/'),'Output parent containment');mkdirSync(out);
const initialFiles=new Map();
function pin(p,expected){const bytes=readFileSync(p);if(expected!==undefined){assert.match(expected,/^[a-f0-9]{64}$/);assert.equal(sha(bytes),expected,p);}initialFiles.set(p,sha(bytes));return bytes;}
const nativeBytes=pin(opts['--native-record'],opts['--native-record-sha256']);
const pdfBytes=pin(opts['--pdf-record'],opts['--pdf-record-sha256']);
const expected=JSON.parse(nativeBytes),pdf=JSON.parse(pdfBytes);
assert(expected.passed&&expected.native_MathML&&pdf.passed);
assert.equal(expected.PDF_build_record_sha256,sha(pdfBytes));
assert.equal(expected.old_literal_math_subtrees,11657);
assert(expected.math_nodes>11657&&expected.math_nodes_added===expected.math_nodes-11657);
assert.deepEqual([expected.tables,expected.canonical_labs,expected.svg_refs],[389,14,33]);
assert(expected.old_math_byte_identical&&expected.old_HTML_restored_exactly&&!expected.production_promoted);
pin(path.join(path.dirname(opts['--pdf-record']),'main.aux'),expected.pdf_aux_sha256);
const sourceNames=['joint-cutoff-core.tex','joint-cutoff-details.tex'];
const sourceText=sourceNames.map(n=>pin(STAGE+'/book/chapters/'+n,expected.source_sha256['book/chapters/'+n]).toString());
const labels=sourceText.flatMap(s=>[...s.matchAll(/\\label\{(pca:[^}]+)\}/g)].map(m=>m[1]));
assert(labels.includes('pca:joint-core')&&labels.includes('pca:joint-details')&&labels.length===new Set(labels).size);
const scriptPath=fileURLToPath(import.meta.url);pin(scriptPath);pin(HELPER);
for(const [p,digest] of Object.entries(expected.source_sha256))pin(STAGE+'/'+p,digest);
const report={schema:'joint-cutoff-focused-native-browser-v1',passed:false,started_at:new Date().toISOString(),base,phase,scope:'New joint cutoff proof appendix, actual source downloads, native layout, and unchanged strict global network-idle protocol.',checks:[],layouts:[],input_files:Object.fromEntries(initialFiles),expected:{labels,math_nodes:expected.math_nodes,math_nodes_added:expected.math_nodes_added,pdf_pages:pdf.pdf_pages}};
const timing=[],idleWaits=[],pendingRequests=new Map(),pageErrors=[],fetchErrors=[],httpErrors=[];
let lastActivity=Date.now(),parentURL=null,b;
const write=(name,data)=>writeFileSync(path.join(out,name),JSON.stringify(data,null,2)+'\n');
const flush=()=>write('network-navigation-timing.json',{events:timing,idleWaits,pending:[...pendingRequests.values()],quiet_ms:750,timeout_ms:30000,scope:'All subscribed network events of the owned context and descendants, without fetch-error or request filters. No headers/cookies captured.'});
function check(ok,name,detail){report.checks.push({name,passed:!!ok,detail});write('checks-so-far.json',report);assert(ok,name+': '+JSON.stringify(detail));}
class ScopedBrowser{
 constructor(){this.pending=new Map();this.id=0;this.context=null;this.userContext=null;this.sessionCreated=false;}
 async connect(){
  this.ws=new WebSocket('ws://127.0.0.1:9337/session');
  await new Promise((resolve,reject)=>{this.ws.once('open',resolve);this.ws.once('error',reject)});
  this.ws.on('message',raw=>{
   const m=JSON.parse(raw);
   if(m.id){const p=this.pending.get(m.id);if(!p)return;this.pending.delete(m.id);clearTimeout(p.timer);m.type==='error'?p.reject(Error(m.error+': '+m.message)):p.resolve(m.result);return;}
   if(m.type!=='event')return;
   const p=m.params??{};
   if(m.method==='log.entryAdded'&&p.level==='error')pageErrors.push(p);
   if(!['network.beforeRequestSent','network.responseCompleted','network.fetchError','browsingContext.navigationStarted','browsingContext.navigationCommitted','browsingContext.load'].includes(m.method))return;
   const r=p.request??{},row={event:m.method,observed_ms:Date.now(),timestamp_ms:p.timestamp??null,context:p.context??null,navigation:p.navigation??null,request:r.request??null,url:r.url??p.url??null,request_method:r.method??null,error:p.errorText??null,status:p.response?.status??null};timing.push(row);
   if(m.method.startsWith('network.')){lastActivity=Date.now();if(m.method==='network.beforeRequestSent')pendingRequests.set(r.request,row);else pendingRequests.delete(r.request);}
   if(m.method==='network.fetchError')fetchErrors.push(row);
   if(m.method==='network.responseCompleted'&&p.response?.status>=400)httpErrors.push(row);
  });
  await this.send('session.new',{capabilities:{alwaysMatch:{acceptInsecureCerts:false}}});this.sessionCreated=true;
  const before=await this.send('browsingContext.getTree',{});this.preexistingContexts=before.contexts.map(x=>x.context);
  this.userContext=(await this.send('browser.createUserContext',{})).userContext;
  this.context=(await this.send('browsingContext.create',{type:'tab',userContext:this.userContext})).context;
  assert(!this.preexistingContexts.includes(this.context),'New owned tab only');
  await this.send('session.subscribe',{events:['log.entryAdded','network.beforeRequestSent','network.responseCompleted','network.fetchError','browsingContext.navigationStarted','browsingContext.navigationCommitted','browsingContext.load'],contexts:[this.context]});
  report.browser_scope={protocol:'WebDriver BiDi',endpoint:'ws://127.0.0.1:9337/session',created_user_context:this.userContext,created_tab:this.context,preexisting_contexts:this.preexistingContexts,scope:'No existing context navigated; no browser.close or process/server termination.'};
 }
 send(method,params={}){return new Promise((resolve,reject)=>{const id=++this.id,timer=setTimeout(()=>{this.pending.delete(id);reject(Error('BiDi timeout '+method));},30000);this.pending.set(id,{resolve,reject,timer});this.ws.send(JSON.stringify({id,method,params}));});}
 async evaluate(expression){const r=await this.send('script.evaluate',{expression:`(async()=>JSON.stringify(await(${expression})))()`,target:{context:this.context},awaitPromise:true,resultOwnership:'none'});if(r.type==='exception')throw Error('Page evaluation: '+JSON.stringify(r.exceptionDetails));return r.result.type==='undefined'?undefined:JSON.parse(r.result.value);}
 eval(fn,arg){return this.evaluate('('+fn.toString()+')('+JSON.stringify(arg)+')');}
 async until(expression,timeout=30000){const start=Date.now();while(Date.now()-start<timeout){if(await this.evaluate(expression))return;await delay(70);}throw Error('Condition timeout: '+expression);}
 viewport(width,height){return this.send('browsingContext.setViewport',{context:this.context,viewport:{width,height},devicePixelRatio:1});}
 async navigate(url){await idle('before-parent-navigation',url);timing.push({event:'harness.parentNavigate',observed_ms:Date.now(),from:parentURL,url,is_initial:parentURL===null,pending:pendingRequests.size});parentURL=url;flush();return this.send('browsingContext.navigate',{context:this.context,url,wait:'complete'});}
 async screenshot(name){const r=await this.send('browsingContext.captureScreenshot',{context:this.context,origin:'viewport',format:{type:'image/png'}});writeFileSync(path.join(out,name),Buffer.from(r.data,'base64'));}
 key(value){return this.send('input.performActions',{context:this.context,actions:[{type:'key',id:'gauss-native-keyboard',actions:[{type:'keyDown',value},{type:'keyUp',value}]}]});}
 async close(){
  const result={owned_tab_closed:false,owned_user_context_removed:false,preexisting_contexts_untouched:false,session_ended:false};
  if(this.context){await this.send('browsingContext.close',{context:this.context});result.owned_tab_closed=true;}
  if(this.userContext){await this.send('browser.removeUserContext',{userContext:this.userContext});result.owned_user_context_removed=true;}
  if(this.sessionCreated){const after=await this.send('browsingContext.getTree',{});const ids=after.contexts.map(x=>x.context);result.preexisting_contexts_untouched=this.preexistingContexts.every(x=>ids.includes(x));assert(result.preexisting_contexts_untouched,'Existing tab disappeared');await this.send('session.end',{});result.session_ended=true;}
  this.ws?.close();return result;
 }
}
async function idle(reason,target){const start=Date.now(),entry=[...pendingRequests.values()];while(Date.now()-start<30000){if(pendingRequests.size===0&&Date.now()-lastActivity>=750){idleWaits.push({reason,from:parentURL,target,start_ms:start,end_ms:Date.now(),duration_ms:Date.now()-start,pending_at_entry:entry,pending_at_exit:[]});flush();return;}await delay(80);}idleWaits.push({reason,from:parentURL,target,start_ms:start,end_ms:Date.now(),timeout:true,pending_at_entry:entry,pending_at_exit:[...pendingRequests.values()]});flush();throw Error('Network-idle timeout: '+JSON.stringify([...pendingRequests.values()]));}
async function jump(id){await b.eval(id=>{document.getElementById(id).scrollIntoView({behavior:'instant',block:'start'});window.scrollBy(0,-110);return true;},id);await delay(150);}
async function fit(){await b.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>{fitReaderMath();fitReviewedReaderMath();r(true)})))');}
async function asset(url,expectedSha){const value=await b.eval(async url=>{const r=await fetch(url);const data=await r.arrayBuffer();return{url:r.url,status:r.status,bytes:data.byteLength,sha256:[...new Uint8Array(await crypto.subtle.digest('SHA-256',data))].map(x=>x.toString(16).padStart(2,'0')).join('')};},url);check(value.status===200&&value.sha256===expectedSha,'source-bound-download-'+new URL(url).pathname,value);return value;}
let failure;
try{
 b=new ScopedBrowser();await b.connect();
 await b.viewport(1440,950);await b.navigate(base+'/');
 const index=await b.evaluate('({reading:document.getElementById("reading").innerText,links:[...document.querySelectorAll("#reading a")].map(a=>a.href)})');
 check(index.reading.includes(String(pdf.pdf_pages)+' pages')&&index.links.includes(base+'/book/main.html#pca:joint-core'),'project link and edition',index.reading.slice(0,240));
 await b.navigate(base+'/book/main.html#pca:joint-core');
 await b.until('document.readyState==="complete"&&!!document.getElementById("joint-cutoff-proof")');
 await b.evaluate('document.fonts.ready.then(()=>true)');await fit();
 const proof=await b.eval(ex=>{
  const root=document.getElementById('joint-cutoff-proof');
  const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);
  const refs=[...root.querySelectorAll('a[href^="#"]')].map(a=>({
    id:decodeURIComponent(a.getAttribute('href').slice(1)),
    number:a.textContent,
    exists:!!document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))}));
  const malformed=[...root.querySelectorAll('msub,msup,munder,mover,mfrac,mroot,msubsup,munderover')]
    .filter(e=>e.children.length!==(['msubsup','munderover'].includes(e.localName)?3:2)).map(e=>e.outerHTML);
  const hidden=[...root.querySelectorAll('math')].filter(e=>{
    const s=getComputedStyle(e),r=e.getBoundingClientRect();
    return s.display==='none'||s.visibility==='hidden'||r.width<=0||r.height<=0;}).length;
  const missing=ex.labels.filter(id=>!root.contains(document.getElementById(id)));
  const numbering=Object.entries(ex.equations).map(([id,number])=>({
    id,number,text:document.getElementById(id)?.closest('.reader-equation')?.querySelector('.reader-equation-number')?.textContent??''}));
  return {math:document.querySelectorAll('math').length,added:root.querySelectorAll('math').length,
    tables:document.querySelectorAll('table').length,frames:document.querySelectorAll('iframe').length,
    svg:document.querySelectorAll('img[src$=".svg"],object[data$=".svg"],embed[src$=".svg"]').length,
    unique:ids.length===new Set(ids).size,missing,refs,malformed,hidden,numbering,
    text:root.textContent.slice(0,17000),pending:document.documentElement.classList.contains('native-math-pending')};
 },{labels,equations:expected.equations});
 check(proof.math===expected.math_nodes&&proof.added===expected.math_nodes_added&&proof.tables===389&&proof.frames===14&&proof.svg===33,'native counts and preserved tools',{math:proof.math,added:proof.added,tables:proof.tables,frames:proof.frames,svg:proof.svg});
 check(proof.unique&&!proof.missing.length&&proof.refs.every(x=>x.exists),'IDs and reference closure',{missing:proof.missing,refs:proof.refs});
 check(!proof.malformed.length&&!proof.hidden&&!proof.pending,'native MathML visibility and fixed arity',{malformed:proof.malformed,hidden:proof.hidden});
 check(proof.numbering.every(x=>x.text.includes('('+x.number+')')),'PDF auxiliary equation numbering',proof.numbering);
 check(['15/32','27/56','111/476','middle equality subtraction'].every(x=>proof.text.includes(x)),'scoped threshold text and compensation');
 for(const theme of ['light','biomech']){
  await b.eval(theme=>{if(document.documentElement.dataset.theme!==theme)document.getElementById('themeToggle').click();if(theme==='biomech'&&document.documentElement.dataset.themeMotion==='live')document.getElementById('motionToggle').click();return true;},theme);
  await b.until('document.documentElement.dataset.theme==='+JSON.stringify(theme));
  await delay(3100);
  for(const [width,height] of [[1440,950],[320,820]]){
   await b.viewport(width,height);await fit();await jump('pca:joint-modes');
   const layout=await b.eval(()=>{
     const root=document.getElementById('joint-cutoff-proof');
     const scrolls=[...root.querySelectorAll('.reader-display-math,.reader-inline-math')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>{
      const prior=e.scrollLeft;e.scrollLeft=e.scrollWidth;const end=e.scrollLeft;e.scrollLeft=prior;const m=e.querySelector('math');
      return {end,tab:e.tabIndex,label:e.getAttribute('aria-label'),font:m?getComputedStyle(m).fontSize:null,
       transform:m?getComputedStyle(m).transform:null};});
     return {width:innerWidth,client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,
       theme:document.documentElement.dataset.theme,scrolls};});
   check(layout.width===width&&layout.scroll<=layout.client+1,'page width '+theme+' '+width,layout);
   check(layout.scrolls.every(x=>x.end>0&&x.tab>=0&&x.label&&(!x.font||parseFloat(x.font)>=18)&&(!x.transform||x.transform==='none')),
     'readable focusable overflow '+theme+' '+width,layout.scrolls);
   report.layouts.push(layout);
   await b.screenshot('selected-'+theme+'-'+width+'.png');
  }
 }
 await b.viewport(320,820);await fit();
 const focus=await b.eval(()=>{
   const root=document.getElementById('joint-cutoff-proof');
   const e=[...root.querySelectorAll('.reader-display-math')].find(e=>e.scrollWidth>e.clientWidth+1);
   if(!e)return {found:false};
   e.scrollIntoView();e.scrollLeft=0;e.focus();return {found:true,focused:document.activeElement===e,client:e.clientWidth,scroll:e.scrollWidth};
 });
 check(focus.found&&focus.focused&&focus.scroll>focus.client,'mobile math horizontal focus',focus);
 await b.key('\uE014');await b.until('document.activeElement.classList.contains("reader-display-math")&&document.activeElement.scrollLeft>0');
 check(true,'mobile math ArrowRight scroll');
 await b.eval(()=>{const link=document.querySelector('#joint-cutoff-proof a[href="#pca:joint-full"]');link.focus();return true;});
 await b.key('\uE007');await b.until('decodeURIComponent(location.hash)==="#pca:joint-full"');check(true,'keyboard theorem link');
 report.downloads=[];
 for(const n of sourceNames)report.downloads.push(await asset(base+'/book/sources/'+n,expected.source_sha256['book/chapters/'+n]));
 report.downloads.push(await asset(base+'/book/sources/weighted-cutoff.tex',expected.source_sha256['book/chapters/weighted-cutoff.tex']));
 report.downloads.push(await asset(base+'/book.pdf',pdf.pdf_sha256));
 report.downloads.push(await asset(base+'/book/main.html',opts['--hosted-html-sha256']));
 await b.navigate(base+'/');
 await idle('final-full-idle',parentURL);
 // Exact inherited predicate from prior native QA; every error is retained in evidence.
 const inherited=pageErrors.filter(x=>JSON.stringify(x).includes('Incorrect number of children for <munder/>'));
 const unexpected=pageErrors.filter(x=>!inherited.includes(x));
 check(unexpected.length===0,'no-new-page-errors',unexpected);report.inheritedMathMLWarnings=inherited;
 check(fetchErrors.length===0,'no-browser-fetch-errors',fetchErrors);
 check(timing.filter(x=>x.event==='network.fetchError').length===0,'global-WS-log-has-no-fetch-errors',timing.filter(x=>x.event==='network.fetchError'));
 check(httpErrors.length===0,'no-HTTP-error-responses',httpErrors);
 check(pendingRequests.size===0&&!idleWaits.some(x=>x.timeout)&&timing.filter(x=>x.event==='harness.parentNavigate').every(x=>x.pending===0),'strict-global-idle-and-departures',{pending:pendingRequests.size,idleWaits:idleWaits.length});
 check([...initialFiles].every(([p,digest])=>sha(readFileSync(p))===digest),'all-source-and-record-inputs-unchanged');
 report.passed=true;
}catch(error){failure=error;report.error=String(error);}
finally{
 try{if(b)report.cleanup=await b.close();}catch(error){report.passed=false;report.cleanup_error=String(error);failure??=error;b?.ws?.close();}
 flush();write('page-errors.json',{all:pageErrors,fetchErrors,httpErrors});
 report.ended_at=new Date().toISOString();report.network={timing_entries:timing.length,protocol_entries:timing.filter(x=>x.event!=='harness.parentNavigate').length,initial_markers:timing.filter(x=>x.event==='harness.parentNavigate'&&x.is_initial).length,actual_departures:timing.filter(x=>x.event==='harness.parentNavigate'&&!x.is_initial).length,fetch_errors:fetchErrors.length,http_errors:httpErrors.length,pending:pendingRequests.size,idle_timeouts:idleWaits.filter(x=>x.timeout).length,quiet_ms:750,timeout_ms:30000};
 write('browser.json',report);write('receipt.json',{schema:report.schema,passed:report.passed,base,out,harness_sha256:initialFiles.get(scriptPath),native_record_sha256:sha(nativeBytes),pdf_record_sha256:sha(pdfBytes),checks:report.checks.length,checks_passed:report.checks.filter(x=>x.passed).length,network:report.network,cleanup:report.cleanup,browser_sha256:sha(readFileSync(path.join(out,'browser.json'))),timing_sha256:sha(readFileSync(path.join(out,'network-navigation-timing.json'))),scope:report.scope});
}
if(failure)throw failure;
console.log(JSON.stringify({passed:report.passed,checks:report.checks.length,out,network:report.network}));
