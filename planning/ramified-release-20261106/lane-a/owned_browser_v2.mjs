import assert from'node:assert/strict';
import{createRequire}from'node:module';import{writeFileSync}from'node:fs';
const require=createRequire('/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs'),WebSocket=require('ws');
export class Browser{
 constructor(){this.pending=new Map();this.id=0;this.events=[];this.allEvents=[];this.context=null;this.userContext=null;this.sessionCreated=false;this.preexistingContexts=[];}
 async connect(){try{
  this.ws=new WebSocket('ws://127.0.0.1:9335/session');await new Promise((resolve,reject)=>{this.ws.once('open',resolve);this.ws.once('error',reject)});
  this.ws.on('message',raw=>{const m=JSON.parse(raw);if(m.id){const p=this.pending.get(m.id);if(!p)return;this.pending.delete(m.id);clearTimeout(p.timeout);m.type==='error'?p.reject(Error(m.error+': '+m.message)):p.resolve(m.result);}else if(m.type==='event'){this.events.push(m);this.allEvents.push(m);}});
  await this.send('session.new',{capabilities:{alwaysMatch:{acceptInsecureCerts:false}}});this.sessionCreated=true;
  this.preexistingContexts=(await this.send('browsingContext.getTree',{})).contexts.map(x=>x.context);
  this.userContext=(await this.send('browser.createUserContext',{})).userContext;
  this.context=(await this.send('browsingContext.create',{type:'tab',userContext:this.userContext})).context;assert(!this.preexistingContexts.includes(this.context));
  await this.send('session.subscribe',{events:['log.entryAdded','network.fetchError'],contexts:[this.context]});return this;
 }catch(error){try{await this.close();}catch{this.ws?.close();}throw error;}
 }
 send(method,params={}){return new Promise((resolve,reject)=>{const id=++this.id;this.pending.set(id,{resolve,reject,timeout:setTimeout(()=>{this.pending.delete(id);reject(Error('BiDi timeout '+method));},30000)});this.ws.send(JSON.stringify({id,method,params}));});}
 async navigate(url){this.events=[];return this.send('browsingContext.navigate',{context:this.context,url,wait:'complete'});}
 async viewport(width,height){await this.send('browsingContext.setViewport',{context:this.context,viewport:{width,height},devicePixelRatio:1});}
 async evaluate(expression){const r=await this.send('script.evaluate',{expression:'(async()=>JSON.stringify(await('+expression+')))()',target:{context:this.context},awaitPromise:true,resultOwnership:'none'});if(r.type==='exception')throw Error('Page evaluation: '+JSON.stringify(r.exceptionDetails));return r.result.type==='undefined'?undefined:JSON.parse(r.result.value);}
 async until(expression,timeout=15000){const start=Date.now();while(Date.now()-start<timeout){if(await this.evaluate(expression))return;await new Promise(r=>setTimeout(r,70));}throw Error('Condition not met: '+expression);}
 async screenshot(path,origin='viewport'){const x=await this.send('browsingContext.captureScreenshot',{context:this.context,origin,format:{type:'image/png'}});writeFileSync(path,Buffer.from(x.data,'base64'));}
 pageErrors(){return this.events.filter(x=>x.method==='log.entryAdded'&&x.params.level==='error'&&x.params.source?.context===this.context);}
 async close(){const x={owned_tab_closed:false,owned_user_context_removed:false,preexisting_contexts_untouched:false,session_ended:false};if(this.context){await this.send('browsingContext.close',{context:this.context});x.owned_tab_closed=true;}if(this.userContext){await this.send('browser.removeUserContext',{userContext:this.userContext});x.owned_user_context_removed=true;}if(this.sessionCreated){const ids=(await this.send('browsingContext.getTree',{})).contexts.map(x=>x.context);x.preexisting_contexts_untouched=this.preexistingContexts.every(id=>ids.includes(id));assert(x.preexisting_contexts_untouched);await this.send('session.end',{});x.session_ended=true;}this.ws?.close();return x;}
}
