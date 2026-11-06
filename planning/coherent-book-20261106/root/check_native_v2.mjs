import{Browser}from'/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import assert from'node:assert/strict';
import{writeFileSync,readFileSync}from'node:fs';
const base=process.env.CBK_QA_URL,out=process.env.CBK_QA_OUTPUT,expected=JSON.parse(readFileSync(process.env.CBK_QA_EXPECTATIONS,'utf8'));assert(base&&out&&expected.math_nodes>9172);const b=await new Browser().connect(),report={passed:false,integration:[]};const delay=ms=>new Promise(r=>setTimeout(r,ms));
const collectedErrors=[],collectedFetch=[],timingEvents=[],idleWaits=[],pendingRequests=new Map();let lastNetworkActivity=Date.now(),parentURL=null;
const timingMethods=new Set(['network.beforeRequestSent','network.responseCompleted','network.fetchError','browsingContext.navigationStarted','browsingContext.navigationCommitted','browsingContext.load']);
b.ws.on('message',raw=>{const m=JSON.parse(raw);if(m.type!=='event'||!timingMethods.has(m.method))return;const p=m.params,r=p.request??{},row={event:m.method,observed_ms:Date.now(),timestamp_ms:p.timestamp??null,context:p.context??null,navigation:p.navigation??null,request:r.request??null,url:r.url??p.url??null,request_method:r.method??null,error:p.errorText??null};timingEvents.push(row);if(m.method.startsWith('network.')){lastNetworkActivity=Date.now();if(m.method==='network.beforeRequestSent')pendingRequests.set(r.request,row);else pendingRequests.delete(r.request);}});
await b.send('session.subscribe',{events:['network.beforeRequestSent','network.responseCompleted','browsingContext.navigationStarted','browsingContext.navigationCommitted','browsingContext.load'],contexts:[b.context]});
const flushTiming=()=>writeFileSync(out+'/network-navigation-timing.json',JSON.stringify({events:timingEvents,idleWaits,pending:[...pendingRequests.values()],timeout_ms:30000,quiet_ms:750,scope:'Protocol event order; no request headers/cookies recorded and no network errors filtered.'},null,2)+'\n');
async function waitForNetworkIdle(reason,target){const start=Date.now(),atEntry=[...pendingRequests.values()];while(Date.now()-start<30000){if(pendingRequests.size===0&&Date.now()-lastNetworkActivity>=750){idleWaits.push({reason,from:parentURL,target,start_ms:start,end_ms:Date.now(),duration_ms:Date.now()-start,pending_at_entry:atEntry,pending_at_exit:[]});flushTiming();return;}await delay(80);}idleWaits.push({reason,from:parentURL,target,start_ms:start,end_ms:Date.now(),timeout:true,pending_at_entry:atEntry,pending_at_exit:[...pendingRequests.values()]});flushTiming();throw Error('Network-idle timeout before '+target+': '+JSON.stringify([...pendingRequests.values()]));}
const navigate=b.navigate.bind(b);b.navigate=async url=>{await waitForNetworkIdle('before-parent-navigation',url);collectedErrors.push(...b.pageErrors());collectedFetch.push(...b.events.filter(e=>e.method==='network.fetchError'));timingEvents.push({event:'harness.parentNavigate',observed_ms:Date.now(),from:parentURL,url,is_initial:parentURL===null,pending:pendingRequests.size});parentURL=url;flushTiming();return navigate(url);};

const check=(ok,name,detail)=>{report.integration.push({name,passed:!!ok,detail});writeFileSync(out+'/checks-so-far.json',JSON.stringify(report,null,2)+'\n');assert(ok,name+': '+JSON.stringify(detail));};
const jump=async id=>{await b.evaluate('(()=>{document.getElementById('+JSON.stringify(id)+').scrollIntoView({block:"start"});window.scrollBy(0,-110);return true})()');await delay(150);};
const geometry=String.raw`({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,inner:innerWidth,math:document.querySelectorAll('math').length})`;
try{
 if(process.env.CBK_LAB_MODULE){const mod=await import(process.env.CBK_LAB_MODULE);report.lab=await mod.runLab(b,base,out);}
 await b.viewport(1440,1050);await b.navigate(base+'/baseline/book/main.html');await b.evaluate('document.fonts.ready.then(()=>true)');
 const oldHashes=await b.evaluate(String.raw`(async()=>{const result={};for(const tag of ['math','table','iframe']){const values=[...document.querySelectorAll(tag)].map(x=>x.outerHTML);result[tag]={count:values.length,sha:[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(values.join('\n'))))].map(x=>x.toString(16).padStart(2,'0')).join('')};}return result})()`);
 const malformedBefore=await b.evaluate('[...document.querySelectorAll("munder")].filter(e=>e.children.length!==2).map(e=>e.outerHTML)');check(malformedBefore.length===3,'exact-three-inherited-munder-nodes',malformedBefore);
 check(oldHashes.math.count===9172&&oldHashes.table.count===389&&oldHashes.iframe.count===13,'old-baseline-counts',oldHashes);
 await b.navigate(base+'/book/main.html');await b.until('document.querySelectorAll("math").length==='+expected.math_nodes+' && !!document.getElementById("cbk:details")',30000);await b.evaluate('document.fonts.ready.then(()=>true)');
 await b.evaluate('(()=>{fitReaderMath();fitReviewedReaderMath();return true})()');
 const state=await b.evaluate(String.raw`(()=>{const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);const cbk=[...document.querySelectorAll('[id^="cbk:"]')];const refs=[...document.querySelectorAll('#coherent-band-section a[href^="#"]')];return{math:document.querySelectorAll('math').length,iframes:document.querySelectorAll('iframe').length,frames:[...document.querySelectorAll('iframe')].map(e=>e.getAttribute('src')),tables:document.querySelectorAll('table').length,uniqueIds:ids.length===new Set(ids).size,cbk:cbk.map(e=>e.id),allRefs:refs.every(e=>!!document.getElementById(decodeURIComponent(e.getAttribute('href').slice(1))))};})()`);
 check(state.math===expected.math_nodes&&state.iframes===14&&state.tables===expected.tables&&state.uniqueIds&&state.cbk.length===expected.explicit_labels&&state.allRefs,'new-native-integrity',state);
 const newHashes=await b.evaluate(String.raw`(async()=>{const result={};for(const tag of ['math','table','iframe']){const values=[...document.querySelectorAll(tag)].filter(e=>!e.closest('#coherent-band-section')).map(x=>x.outerHTML);result[tag]={count:values.length,sha:[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(values.join('\n'))))].map(x=>x.toString(16).padStart(2,'0')).join('')};}return result})()`);
 check(JSON.stringify(newHashes)===JSON.stringify(oldHashes),'browser-old-subtree-preservation',{oldHashes,newHashes});
 const malformedAfter=await b.evaluate('[...document.querySelectorAll("munder")].filter(e=>e.children.length!==2).map(e=>e.outerHTML)');check(JSON.stringify(malformedAfter)===JSON.stringify(malformedBefore),'exact-inherited-malformed-node-preservation');
 const nums=await b.evaluate('Object.fromEntries([...document.querySelectorAll("#coherent-band-section .reader-equation[id]")].map(e=>[e.id,e.querySelector(".reader-equation-number").textContent]))');
 check(Object.entries(expected.equations).every(([id,n])=>nums[id]?.includes('('+n+')')),'PDF-aux-equation-numbers',nums);
 check(await b.evaluate('document.querySelector("#cbk\\\\:workflow figcaption").textContent.startsWith("Figure '+expected.figure_number+'.")'),'PDF-aux-figure-number');
 for(const id of ['cbk:core','cbk:workflow','cbk:equal','cbk:ray','cbk:schur-proof']){await jump(id);await b.screenshot(out+'/'+id.replace(':','-')+'-desktop.png');}
 const results=[];
 for(const [width,height] of [[320,844],[390,844],[768,1024],[1440,1050]]){
  await b.viewport(width,height);await b.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>{fitReaderMath();fitReviewedReaderMath();r(true)})))');
  const g=await b.evaluate(geometry);check(g.inner===width&&g.scroll<=g.client+1,'native-layout-'+width,g);
  const overflow=await b.evaluate(String.raw`[...document.querySelectorAll('#coherent-band-section .reader-display-math,#coherent-band-section .reader-inline-math,#coherent-band-section .reader-table-scroll,#coherent-band-section .reader-figure-scroll')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>{const old=e.scrollLeft;e.scrollLeft=e.scrollWidth;const end=e.scrollLeft;e.scrollLeft=old;const m=e.querySelector('math');return{end,tabIndex:e.tabIndex,label:e.getAttribute('aria-label'),font:m?getComputedStyle(m).fontSize:null,transform:m?getComputedStyle(m).transform:null}})`);
  check(overflow.every(e=>e.end>0&&e.tabIndex>=0&&e.label&&(!e.font||parseFloat(e.font)>=18)&&(!e.transform||e.transform==='none')),'new-overflow-accessible-'+width,overflow);results.push({g,overflow});
  if(width===320||width===1440){await jump('cbk:equal');await b.screenshot(out+'/equal-'+width+'.png');await jump('cbk:workflow');await b.screenshot(out+'/workflow-'+width+'.png');}
 }
 report.layouts=results;
 await b.viewport(390,844);await b.evaluate('(()=>{if(document.documentElement.dataset.theme!=="biomech")document.getElementById("themeToggle").click();if(document.documentElement.dataset.themeMotion==="live")document.getElementById("motionToggle").click();return true})()');await delay(3100);await jump('cbk:core');await b.screenshot(out+'/core-mobile-night.png');
 check(await b.evaluate('document.documentElement.dataset.theme==="biomech"'),'native-night-theme');
 await b.evaluate('(()=>{document.querySelector("#coherent-band-section a[href=\\"#cbk:details\\"]").click();return true})()');await b.until('decodeURIComponent(location.hash)==="#cbk:details"');check(true,'native-reference-click');
 const downloads=[];
 for(const name of ['coherent-band-core.tex','coherent-band-details.tex','coherent-band-figure.tex']){
  const v=await b.evaluate('(async()=>{const r=await fetch("/book/sources/'+name+'");const b=await r.arrayBuffer();return{status:r.status,bytes:b.byteLength,sha:[...new Uint8Array(await crypto.subtle.digest("SHA-256",b))].map(x=>x.toString(16).padStart(2,"0")).join("")}})()');
  check(v.status===200&&v.sha===expected.sources['book/chapters/'+name],'new-source-download-'+name,v);downloads.push(v);
 }
 const pdf=await b.evaluate('(async()=>{const r=await fetch("/book.pdf");const b=await r.arrayBuffer();return{status:r.status,bytes:b.byteLength,sha:[...new Uint8Array(await crypto.subtle.digest("SHA-256",b))].map(x=>x.toString(16).padStart(2,"0")).join("")}})()');
 check(pdf.status===200&&pdf.sha===expected.pdf_sha256,'candidate-book-PDF-download',pdf);
 await waitForNetworkIdle('final-full-idle',parentURL);
 collectedErrors.push(...b.pageErrors());collectedFetch.push(...b.events.filter(e=>e.method==='network.fetchError'));
 const errors=collectedErrors,inherited=errors.filter(x=>JSON.stringify(x).includes('Incorrect number of children for <munder/>'));const unexpected=errors.filter(x=>!inherited.includes(x));check(unexpected.length===0,'no-new-page-errors',unexpected);report.inheritedMathMLWarnings=inherited;
 check(collectedFetch.length===0,'no-browser-fetch-errors',collectedFetch);
 check(timingEvents.filter(x=>x.event==='network.fetchError').length===0,'global-WS-log-has-no-fetch-errors',timingEvents.filter(x=>x.event==='network.fetchError'));
 check(pendingRequests.size===0&&!idleWaits.some(e=>e.timeout)&&timingEvents.filter(e=>e.event==='harness.parentNavigate').every(e=>e.pending===0),'strict-global-idle-and-departures',{pending:pendingRequests.size,idleWaits:idleWaits.length});
 report.passed=true;report.network={events:timingEvents.length,fetchErrors:collectedFetch.length,newPageErrors:unexpected.length,inheritedMathMLWarnings:inherited.length,pending:pendingRequests.size,idleWaits:idleWaits.length,quiet_ms:750,timeout_ms:30000,departures:timingEvents.filter(e=>e.event==='harness.parentNavigate'&&!e.is_initial).length};report.new_sources=downloads;
}catch(error){report.error=String(error);throw error;}
finally{flushTiming();writeFileSync(out+'/browser.json',JSON.stringify(report,null,2)+'\n');await b.close();}
