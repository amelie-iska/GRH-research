#!/usr/bin/env node
// Focused candidate-only ramified-cusp QA. No legacy lab/model/release suite is run.
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {readFileSync, writeFileSync, mkdirSync, existsSync, realpathSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const ROOT='/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104';
const HELPER='/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
const require=createRequire(HELPER), WebSocket=require('ws');
const sha=x=>createHash('sha256').update(x).digest('hex');
const delay=ms=>new Promise(r=>setTimeout(r,ms));
const argv=process.argv.slice(2),opts={};
for(let i=0;i<argv.length;i+=2){assert(argv[i].startsWith('--')&&argv[i+1],'Expected --name value');assert(!Object.hasOwn(opts,argv[i]),'Duplicate argument');opts[argv[i]]=argv[i+1];}
const keys=['--base','--out','--native-record','--native-record-sha256','--pdf-record','--pdf-record-sha256'];
assert.deepEqual(Object.keys(opts).sort(),keys.sort(),'Exact required options');
const base=opts['--base'].replace(/\/$/,''),origin=new URL(base);
assert(origin.protocol==='http:'&&['127.0.0.1','localhost','[::1]'].includes(origin.hostname)&&origin.port,'Only a fresh explicit loopback server');
assert(!origin.username&&!origin.password&&!origin.search&&!origin.hash,'No credentials/query/fragment');
const out=path.resolve(opts['--out']),outRoot=ROOT+'/outputs/checks/2026-11-06-ramified-book/lane-a/';
assert(out.startsWith(outRoot)&&!existsSync(out),'New owned output directory required');
mkdirSync(path.dirname(out),{recursive:true});const actualParent=realpathSync(path.dirname(out)),ownedRoot=realpathSync(outRoot);assert(actualParent===ownedRoot||actualParent.startsWith(ownedRoot+'/'),'Output parent containment');mkdirSync(out);
const initialFiles=new Map();
function pin(p,expected){const bytes=readFileSync(p);if(expected!==undefined){assert.match(expected,/^[a-f0-9]{64}$/);assert.equal(sha(bytes),expected,p);}initialFiles.set(p,sha(bytes));return bytes;}
const nativeBytes=pin(opts['--native-record'],opts['--native-record-sha256']);
const pdfBytes=pin(opts['--pdf-record'],opts['--pdf-record-sha256']);
const expected=JSON.parse(nativeBytes),pdf=JSON.parse(pdfBytes);
assert(expected.passed&&expected.native_MathML&&pdf.passed,'Passed candidate records');
assert.equal(expected.PDF_build_record_sha256,sha(pdfBytes));
assert(expected.math_nodes>10299&&expected.math_nodes_added===expected.math_nodes-10299);
assert.deepEqual([expected.old_literal_math_subtrees,expected.old_tables,expected.old_canonical_labs,expected.old_svg_refs],[10299,389,14,31]);
assert.deepEqual([expected.tables,expected.canonical_labs,expected.svg_refs,pdf.pdf_pages],[389,14,32,348]);
assert.equal(expected.production_promoted,false,'Candidate record required');
assert.equal(expected.old_math_byte_identical,true,'10299 literal old math subtrees preserved');
assert.equal(expected.old_HTML_restored_exactly,true,'Old HTML exact restoration');
pin(path.join(path.dirname(opts['--pdf-record']),'main.aux'),expected.pdf_aux_sha256);
const sourceNames=['ramified-gauss-core.tex','ramified-gauss-figure.tex','ramified-gauss-details.tex'];
const sourceText=sourceNames.map(n=>pin(ROOT+'/book/chapters/'+n,expected.source_sha256['book/chapters/'+n]).toString());
const labels=sourceText.flatMap(s=>[...s.matchAll(/\\label\{(rg:[^}]+)\}/g)].map(m=>m[1]));
assert.equal(labels.length,75,'Exactly75 new source labels');assert.equal(labels.length,new Set(labels).size);assert(labels.includes('rg:core')&&labels.includes('rg:details')&&labels.includes('rg:workflow'));
assert.equal(expected.proof_environments,sourceText.join('\n').match(/\\begin\{proof\}/g)?.length??0);
const scriptPath=fileURLToPath(import.meta.url);pin(scriptPath);pin(HELPER);for(const [p,digest] of Object.entries(expected.source_sha256))pin(ROOT+'/'+p,digest);
const report={schema:'ramified-gauss-focused-native-browser-v1',passed:false,started_at:new Date().toISOString(),base,scope:'Only new ramified-cusp native sections/assets/layout and exact source downloads. No old release/model/training/lab controls. Strict global WS log/error/idle protocol retained.',checks:[],layouts:[],input_files:Object.fromEntries(initialFiles),expected:{labels,math_nodes:expected.math_nodes,math_nodes_added:expected.math_nodes_added,tables:389,frames:14,svg_refs:32,pdf_pages:348}};
const timing=[],idleWaits=[],pendingRequests=new Map(),pageErrors=[],fetchErrors=[],httpErrors=[];
let lastActivity=Date.now(),parentURL=null,b;
const write=(name,data)=>writeFileSync(path.join(out,name),JSON.stringify(data,null,2)+'\n');
const flush=()=>write('network-navigation-timing.json',{events:timing,idleWaits,pending:[...pendingRequests.values()],quiet_ms:750,timeout_ms:30000,scope:'All subscribed network events of the owned context and descendants, without fetch-error or request filters. No headers/cookies captured.'});
function check(ok,name,detail){report.checks.push({name,passed:!!ok,detail});write('checks-so-far.json',report);assert(ok,name+': '+JSON.stringify(detail));}
class ScopedBrowser{
 constructor(){this.pending=new Map();this.id=0;this.context=null;this.userContext=null;this.sessionCreated=false;}
 async connect(){
  this.ws=new WebSocket('ws://127.0.0.1:9335/session');
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
  report.browser_scope={protocol:'WebDriver BiDi',endpoint:'ws://127.0.0.1:9335/session',created_user_context:this.userContext,created_tab:this.context,preexisting_contexts:this.preexistingContexts,scope:'No existing context navigated; no browser.close or process/server termination.'};
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
 b=new ScopedBrowser();await b.connect();await b.viewport(1440,1050);await b.navigate(base+'/book/main.html#rg:core');
 await b.until('document.readyState==="complete"&&!!document.getElementById("ramified-gauss-section")');await b.evaluate('document.fonts.ready.then(()=>true)');await fit();
 check(await b.eval(n=>document.querySelectorAll('math').length===n,expected.math_nodes),'candidate-record-math-count',expected.math_nodes);
 const state=await b.eval(labels=>{
  const root=document.getElementById('ramified-gauss-section'),allIds=[...document.querySelectorAll('[id]')].map(e=>e.id),newLabels=[...root.querySelectorAll('[id^="rg:"]')].map(e=>e.id);
  const refs=[...root.querySelectorAll('a[href^="#"]')].map(a=>({id:decodeURIComponent(a.getAttribute('href').slice(1)),text:a.textContent,exists:!!document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))}));
  const malformed=[...root.querySelectorAll('msub,msup,munder,mover,mfrac,mroot,msubsup,munderover')].filter(e=>e.children.length!==(['msubsup','munderover'].includes(e.localName)?3:2)).map(e=>({tag:e.localName,children:e.children.length,html:e.outerHTML}));
  const hidden=[...root.querySelectorAll('math')].filter(e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display==='none'||s.visibility==='hidden'||r.width<=0||r.height<=0;}).length;
  return{math:document.querySelectorAll('math').length,newMath:root.querySelectorAll('math').length,tables:document.querySelectorAll('table').length,newTables:root.querySelectorAll('table').length,frames:document.querySelectorAll('iframe').length,newFrames:root.querySelectorAll('iframe').length,svgRefs:document.querySelectorAll('img[src$=".svg"],object[data$=".svg"],embed[src$=".svg"]').length,newSVG:root.querySelectorAll('img[src$=".svg"]').length,uniqueIds:allIds.length===new Set(allIds).size,labels:newLabels,missingLabels:labels.filter(id=>!document.getElementById(id)),extraLabels:newLabels.filter(id=>!labels.includes(id)),refs,malformed,hidden,pendingMath:document.documentElement.classList.contains('native-math-pending'),proofs:[...root.querySelectorAll('em')].filter(e=>e.textContent.startsWith('Proof')).length};
 },labels);
 check(state.newMath===expected.math_nodes_added&&state.tables===389&&state.frames===14&&state.svgRefs===32&&state.newFrames===0&&state.newSVG===1,'scoped-counts-no-new-lab',state);
 check(state.uniqueIds&&!state.missingLabels.length&&!state.extraLabels.length,'all-source-gtl-labels-exact',state.labels);
 check(state.refs.every(x=>x.exists),'new-local-reference-closure',state.refs);
 check(!state.malformed.length&&!state.hidden&&!state.pendingMath,'all-new-MathML-visible-and-valid-fixed-arity',{malformed:state.malformed,hidden:state.hidden,pending:state.pendingMath});
 check(state.proofs===expected.proof_environments,'all-new-proof-environments',state.proofs);
 const numbering=await b.eval(ex=>{
  const root=document.getElementById('ramified-gauss-section');
  return{equations:Object.entries(ex.equations).map(([id,number])=>({id,number,text:document.getElementById(id)?.closest('.reader-equation')?.querySelector('.reader-equation-number')?.textContent??''})),headings:ex.headings.map(x=>({id:x.id,number:x.number,text:document.getElementById(x.id)?.textContent??'',paragraph:document.getElementById(x.id)?.classList.contains('paragraphHead')})),theorems:ex.theorems.map(x=>({id:x.id,number:x.number,text:document.getElementById(x.id)?.querySelector('strong')?.textContent??''})),references:[...root.querySelectorAll('a[data-reference]')].map(a=>({id:a.dataset.reference,kind:a.dataset.referenceType,text:a.textContent})),caption:document.getElementById('rg:workflow').querySelector('figcaption').textContent};
 },{equations:expected.equations,headings:expected.headings,theorems:expected.theorems});
 check(numbering.equations.every(x=>x.text.includes('('+x.number+')'))&&numbering.headings.every(x=>x.paragraph||x.text.includes(x.number))&&numbering.theorems.every(x=>x.text.includes(x.number)),'PDF-aux-equation-heading-theorem-numbers',numbering);
 check(numbering.references.length===expected.references.length&&numbering.references.every((x,i)=>{const e=expected.references[i];return x.id===e.id&&x.kind===e.kind&&x.text===(e.kind==='eqref'?'('+e.number+')':e.number);})&&numbering.caption.startsWith('Figure '+expected.figure_number+'.'),'PDF-aux-reference-and-figure-numbers',numbering.references);
 check(state.newTables===expected.tables-389,'new-table-count-explicit-zero',state.newTables);
 for(const id of ['rg:core','rg:sharp-row','rg:prefix-theorem','rg:details','rg:workflow']){await jump(id);await b.screenshot(id.replace(':','-')+'-desktop.png');}
 for(const theme of ['light','biomech']){
  await b.eval(theme=>{if(document.documentElement.dataset.theme!==theme)document.getElementById('themeToggle').click();if(theme==='biomech'&&document.documentElement.dataset.themeMotion==='live')document.getElementById('motionToggle').click();return true;},theme);
  await b.until('document.documentElement.dataset.theme==='+JSON.stringify(theme));await delay(3100);
  for(const [width,height] of [[1440,1050],[320,844]]){
   await b.viewport(width,height);await fit();
   const layout=await b.eval(()=>{
    const root=document.getElementById('ramified-gauss-section'),fig=document.getElementById('rg:workflow'),img=fig.querySelector('img'),wrap=img.closest('.reader-figure-scroll'),is=getComputedStyle(img);
    const scrolls=[...root.querySelectorAll('.reader-display-math,.reader-inline-math,.reader-table-scroll,.reader-figure-scroll')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>{const prior=e.scrollLeft;e.scrollLeft=e.scrollWidth;const end=e.scrollLeft;e.scrollLeft=prior;const m=e.querySelector('math');return{className:e.className,end,tabIndex:e.tabIndex,label:e.getAttribute('aria-label'),font:m?getComputedStyle(m).fontSize:null,transform:m?getComputedStyle(m).transform:null};});
    return{width:innerWidth,client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,figure:{complete:img.complete,naturalWidth:img.naturalWidth,width:img.getBoundingClientRect().width,height:img.getBoundingClientRect().height,filter:is.filter,transform:is.transform,alt:img.alt,wrapperWidth:wrap.clientWidth,wrapperScroll:wrap.scrollWidth,tabIndex:wrap.tabIndex,label:wrap.getAttribute('aria-label'),role:wrap.getAttribute('role'),overflow:getComputedStyle(wrap).overflowX},scrolls,tables:[...root.querySelectorAll('table')].map(e=>({wrapped:!!e.closest('.reader-table-scroll'),tabIndex:e.closest('.reader-table-scroll')?.tabIndex}))};
   });
   check(layout.width===width&&layout.scroll<=layout.client+1,'new-layout-no-page-overflow-'+theme+'-'+width,layout);
   check(layout.figure.complete&&layout.figure.naturalWidth>0&&layout.figure.width>=650&&layout.figure.height>0&&layout.figure.filter==='none'&&layout.figure.transform==='none'&&layout.figure.alt&&layout.figure.tabIndex===0&&layout.figure.role==='region'&&layout.figure.label&&layout.figure.overflow==='auto','readable-source-figure-'+theme+'-'+width,layout.figure);
   check(layout.scrolls.every(x=>x.end>0&&x.tabIndex>=0&&x.label&&(!x.font||parseFloat(x.font)>=18)&&(!x.transform||x.transform==='none'))&&layout.tables.every(x=>x.wrapped&&x.tabIndex===0),'new-overflow-focusable-and-unscaled-'+theme+'-'+width,layout.scrolls);
   report.layouts.push(layout);await jump('rg:workflow');await b.screenshot('figure-'+theme+'-'+width+'.png');await jump('rg:sharp-proof');await b.screenshot('direct-proof-'+theme+'-'+width+'.png');
  }
 }
 await b.viewport(320,844);await fit();await jump('rg:workflow');
 const focus=await b.eval(()=>{const e=document.getElementById('rg:workflow').querySelector('.reader-figure-scroll');e.scrollLeft=0;e.focus();return{focused:document.activeElement===e,width:e.clientWidth,scroll:e.scrollWidth};});
 check(focus.focused&&focus.scroll>focus.width+1,'figure-genuine-mobile-horizontal-scroll',focus);
 await b.key('\uE014');await b.until('document.activeElement.classList.contains("reader-figure-scroll")&&document.activeElement.scrollLeft>0');
 check(true,'figure-native-ArrowRight-scroll');await b.key('\uE004');
 check(await b.evaluate('document.activeElement.tagName==="A"&&document.activeElement.getAttribute("href").endsWith("figures/ramified-cusp-prefix.tex")'),'figure-Tab-to-original-TeX-link');
 await b.eval(()=>{document.querySelector('#ramified-gauss-section nav a[href="#rg:details"]').focus();return true;});await b.key('\uE007');await b.until('decodeURIComponent(location.hash)==="#rg:details"');check(true,'proof-reference-native-Enter-navigation');
 const linkState=await b.eval(names=>{
  const root=document.getElementById('ramified-gauss-section');return{sources:names.map(n=>({name:n,present:!![...root.querySelectorAll('a[href]')].find(a=>a.getAttribute('href').endsWith('sources/'+n))})),figure:['svg','tex','pdf'].map(ext=>({ext,present:ext==='svg'?!!root.querySelector('img[src$="figures/ramified-cusp-prefix.svg"]'):!!root.querySelector('a[href$="figures/ramified-cusp-prefix.'+ext+'"]')})),pdf:!!root.querySelector('a[href$="book.pdf"]')};
 },sourceNames);
 check(linkState.sources.every(x=>x.present)&&linkState.figure.every(x=>x.present)&&linkState.pdf,'actual-new-source-figure-and-book-PDF-links',linkState);
 report.downloads=[];
 for(const n of sourceNames)report.downloads.push(await asset(base+'/book/sources/'+n,expected.source_sha256['book/chapters/'+n]));
 for(const ext of ['svg','tex','pdf'])report.downloads.push(await asset(base+'/book/figures/ramified-cusp-prefix.'+ext,expected.source_sha256['book/figures/ramified-cusp-prefix.'+ext]));
 report.downloads.push(await asset(base+'/book.pdf',pdf.pdf_sha256));
 report.downloads.push(await asset(base+'/book/main.html',expected.new_HTML_sha256));
 // Standalone original SVG and return exercise real parent departures with the same strict idle guard.
 await b.viewport(1440,1050);await b.navigate(base+'/book/figures/ramified-cusp-prefix.svg');
 await b.until('document.documentElement.localName==="svg"');
 const svgState=await b.evaluate('({tag:document.documentElement.localName,tabindex:document.documentElement.getAttribute("tabindex"),focusable:document.documentElement.getAttribute("focusable"),title:document.querySelector("title")?.textContent,desc:document.querySelector("desc")?.textContent,cusps:document.querySelectorAll("circle").length,slots:document.querySelectorAll("rect[id^=factor-]").length,external:[...document.querySelectorAll("*")].some(e=>[...e.attributes].some(a=>a.localName==="href"||a.name.toLowerCase().startsWith("on")))})');
 check(svgState.tag==='svg'&&svgState.tabindex==='0'&&svgState.focusable==='true'&&svgState.title&&svgState.desc&&svgState.cusps===27&&svgState.slots===11&&!svgState.external,'standalone-original-SVG-accessible-and-source-specific',svgState);
 await b.screenshot('standalone-original-svg-desktop.png');
 await b.viewport(320,844);await b.screenshot('standalone-original-svg-mobile.png');
 await b.navigate(base+'/book/main.html#rg:prefix-theorem');
 await b.until('document.readyState==="complete"&&!!document.getElementById("ramified-gauss-section")');await b.evaluate('document.fonts.ready.then(()=>true)');await fit();await jump('rg:prefix-theorem');await b.screenshot('final-prefix-theorem-mobile.png');
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
