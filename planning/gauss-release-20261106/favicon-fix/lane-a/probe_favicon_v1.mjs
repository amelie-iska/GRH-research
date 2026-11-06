import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {Browser} from '/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104/planning/gauss-release-20261106/qa/owned_browser_v2.mjs';
const cfg=JSON.parse(process.env.FAVICON_PROBE_CONFIG);
const out=cfg.output;
const hash=x=>createHash('sha256').update(x).digest('hex');
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function closeOwned(b){
 const c={owned_tab_closed:false,owned_user_context_removed:false,preexisting_contexts_untouched:false,session_ended:false,errors:[]};
 try{
  if(b.context)try{await b.send('browsingContext.close',{context:b.context});c.owned_tab_closed=true;}catch(e){c.errors.push('owned tab: '+String(e));}
  if(b.userContext)try{await b.send('browser.removeUserContext',{userContext:b.userContext});c.owned_user_context_removed=true;}catch(e){c.errors.push('owned user context: '+String(e));}
  if(b.sessionCreated){
   try{const ids=(await b.send('browsingContext.getTree',{})).contexts.map(x=>x.context);c.preexisting_contexts_untouched=b.preexistingContexts.every(id=>ids.includes(id));}catch(e){c.errors.push('context preservation: '+String(e));}
   try{await b.send('session.end',{});c.session_ended=true;}catch(e){c.errors.push('owned session: '+String(e));}
  }
 }finally{try{b.ws?.close();}catch(e){c.errors.push('websocket: '+String(e));}}
 return c;
}
const results=[];
for(const name of ['control','treatment']){
 const b=new Browser(),result={case:name,passed:false,URL:cfg.origins[name]+'/GRH-research/',runtime_sha256:cfg.runtime_sha256[name],no_error_filter:true,requests_blocked_or_intercepted:false,prefs_changed:false};
 const pending=new Set(),idleWaits=[];let last=Date.now();
 try{
  await b.connect();
  await b.send('session.subscribe',{events:['network.beforeRequestSent','network.responseCompleted','network.fetchError'],contexts:[b.context]});
  b.ws.on('message',raw=>{
   const m=JSON.parse(raw);
   if(m.type!=='event'||!m.method.startsWith('network.'))return;
   const id=m.params.request?.request;
   if(m.method==='network.beforeRequestSent')pending.add(id);
   if(m.method==='network.responseCompleted'||m.method==='network.fetchError')pending.delete(id);
   last=Date.now();
  });
  await b.viewport(900,600);
  await b.navigate(result.URL);
  await b.until('window.__probeDOMContentLoaded!==undefined',10000);
  const start=Date.now();
  while(pending.size||Date.now()-last<750){
   if(Date.now()-start>30000)throw Error('Strict probe idle timeout');
   await sleep(50);
  }
  idleWaits.push({quiet_ms:750,timeout_ms:30000,start_ms:start,end_ms:Date.now(),pending_at_exit:[...pending]});
  result.DOM=await b.evaluate('(()=>{const link=document.querySelector(\'link[rel~="icon"]\');let svg=null;if(link?.href.startsWith("data:image/svg+xml,")){const source=decodeURIComponent(link.href.slice("data:image/svg+xml,".length));const doc=new DOMParser().parseFromString(source,"image/svg+xml");svg={source,namespace:doc.documentElement.namespaceURI,root:doc.documentElement.localName,parserError:!!doc.querySelector("parsererror")};}return{readyState:document.readyState,DOMContentLoaded:window.__probeDOMContentLoaded,iconCount:document.querySelectorAll(\'link[rel~="icon"]\').length,icon:link?{rel:link.rel,type:link.type,href:link.href,connected:link.isConnected}:null,svg};})()');
  result.imageDecode=await b.evaluate('(async()=>{const link=document.querySelector(\'link[rel~="icon"]\');if(!link)return null;const im=new Image();im.src=link.href;await im.decode();return{width:im.naturalWidth,height:im.naturalHeight,complete:im.complete};})()');
  await b.evaluate('(()=>{const box=document.getElementById("state"),link=document.querySelector(\'link[rel~="icon"]\');box.textContent=JSON.stringify({DOMContentLoaded:window.__probeDOMContentLoaded,currentIcon:link?{href:link.href,type:link.type}:null},null,2);if(link){const im=document.getElementById("icon-preview");im.src=link.href;im.hidden=false;}return true;})()');
  await b.screenshot(out+'/'+name+'.png');
  result.events=b.allEvents.filter(e=>e.method.startsWith('network.')||e.method==='log.entryAdded').map(e=>({event:e.method,context:e.params.context??e.params.source?.context??null,navigation:e.params.navigation??null,request:e.params.request?.request??null,url:e.params.request?.url??null,method:e.params.request?.method??null,status:e.params.response?.status??null,error:e.params.errorText??null,level:e.params.level??null,text:e.params.text??null}));
  result.HTTP_errors=result.events.filter(e=>e.event==='network.responseCompleted'&&e.status>=400);
  result.fetch_errors=result.events.filter(e=>e.event==='network.fetchError');
  result.page_errors=b.pageErrors().map(e=>({level:e.params.level,text:e.params.text}));
  result.origin_favicon_requests=result.events.filter(e=>e.event==='network.beforeRequestSent'&&e.url===cfg.origins[name]+'/favicon.ico');
  result.idleWaits=idleWaits;result.pending_final=[...pending];
  assert.equal(result.fetch_errors.length,0);
  assert.equal(result.page_errors.length,0);
  if(name==='control'){
   assert.equal(result.DOM.iconCount,0);
   assert(result.origin_favicon_requests.length>=1,'Control must reproduce automatic root favicon request');
   assert(result.HTTP_errors.length>=1&&result.HTTP_errors.every(e=>e.status===404&&e.url===cfg.origins[name]+'/favicon.ico'));
  }else{
   assert.equal(result.DOM.iconCount,1);
   assert.equal(result.DOM.DOMContentLoaded.icons.length,1,'Icon must exist by DOMContentLoaded');
   assert.equal(result.DOM.DOMContentLoaded.icons[0].href,cfg.icon_uri);
   assert.equal(result.DOM.icon.href,cfg.icon_uri);
   assert.equal(result.DOM.icon.type,'image/svg+xml');
   assert.equal(result.DOM.svg.root,'svg');assert.equal(result.DOM.svg.namespace,'http://www.w3.org/2000/svg');assert.equal(result.DOM.svg.parserError,false);
   assert.deepEqual(result.imageDecode,{width:32,height:32,complete:true});
   assert.equal(result.origin_favicon_requests.length,0);
   assert.equal(result.HTTP_errors.length,0);
  }
  result.passed=true;
 }catch(error){result.error=String(error);result.stack=error.stack;}
 finally{
  result.cleanup=await closeOwned(b);
  if(result.cleanup.errors.length||!result.cleanup.owned_tab_closed||!result.cleanup.owned_user_context_removed||!result.cleanup.preexisting_contexts_untouched||!result.cleanup.session_ended)result.passed=false;
  writeFileSync(out+'/'+name+'.json',JSON.stringify(result,null,2)+'\n');
  results.push(result);
 }
}
const summary={passed:results.every(x=>x.passed),scope:'Two isolated loopback404 origins, exact old runtime versus one icon insertion; no HTTP request interception/filtering, prefs, publication or frozen-source changes.',results:results.map(r=>({case:r.case,passed:r.passed,HTTP_errors:r.HTTP_errors,origin_favicon_requests:r.origin_favicon_requests?.length,cleanup:r.cleanup})),files_sha256:Object.fromEntries(['control.json','treatment.json','control.png','treatment.png'].map(n=>[n,hash(readFileSync(out+'/'+n))]))};
writeFileSync(out+'/browser-probe.json',JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify(summary));if(!summary.passed)process.exitCode=1;
