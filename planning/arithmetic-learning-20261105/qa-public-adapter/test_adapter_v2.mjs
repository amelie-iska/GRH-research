import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync,writeFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
const ROOT=new URL('../../../',import.meta.url),sourceURL=new URL('scripts/build_public_site.py',ROOT),beforeURL=new URL('outputs/checks/2026-11-05-arithmetic-learning/adapter/build_public_site.before.py',ROOT);
const source=readFileSync(sourceURL,'utf8'),before=readFileSync(beforeURL,'utf8'),origin='https://example.test',current=origin+'/GRH-research/current.html';
const extract=s=>{const quotes=String.fromCharCode(39).repeat(3),prefix='runtime=r'+quotes,start=s.indexOf(prefix),end=s.indexOf('\n'+quotes,start);assert(start>=0&&end>start);return s.slice(start+prefix.length,end);};
const checks=[];
function environment(code){
 const calls=[];
 class BrowserRequest extends Request{constructor(input,init){super(typeof input==='string'?new URL(input,current):input,init);}}
 class Element{setAttribute(){}querySelectorAll(){return[];}}
 const globals={URL,Request:BrowserRequest,Element,location:{origin},document:{documentElement:{}},MutationObserver:class{observe(){}},window:{fetch:(input,init)=>{calls.push({input,init});return Promise.resolve({stub:true});}}};
 for(const[name,key]of[['HTMLAnchorElement','href'],['HTMLImageElement','src'],['HTMLIFrameElement','src'],['HTMLMediaElement','src'],['HTMLSourceElement','src']]){const Type=class extends Element{};Object.defineProperty(Type.prototype,key,{configurable:true,get(){return this.value;},set(v){this.value=v;}});globals[name]=Type;}
 vm.runInNewContext(code,globals,{timeout:1000});return{...globals,calls};
}
const env=environment(extract(source));
const absolute=input=>new URL(input instanceof Request?input.url:input instanceof URL?input.href:input,current).href;
const routes=[
 ['root','/data/a.json',origin+'/GRH-research/data/a.json'],
 ['prefixed','/GRH-research/data/a.json',origin+'/GRH-research/data/a.json'],
 ['relative','./data/a.json',origin+'/GRH-research/data/a.json'],
 ['same-origin-absolute',origin+'/data/a.json',origin+'/GRH-research/data/a.json'],
 ['same-origin-prefixed',origin+'/GRH-research/data/a.json',origin+'/GRH-research/data/a.json'],
 ['external','https://outside.test/data/a.json','https://outside.test/data/a.json'],
 ['legacy8765','http://127.0.0.1:8765/data/a.json',origin+'/GRH-research/data/a.json']
];
for(const type of['string','URL','Request'])for(const[name,input,expected]of routes){
 const value=type==='string'?input:type==='URL'?new URL(input,current):new env.Request(input,{headers:{'X-Input':'preserved'},credentials:'include',cache:'no-store',redirect:'manual'}),init={headers:{'X-Override':'same-object'},credentials:'omit'};
 await env.window.fetch(value,init);const call=env.calls.at(-1);assert.equal(absolute(call.input),expected,`${type}/${name}`);assert.strictEqual(call.init,init,'Fetch init object forwarded unchanged');assert(!absolute(call.input).includes('/GRH-research/GRH-research/'));
 if(type==='URL')assert(call.input instanceof URL);
 if(type==='Request'){assert(call.input instanceof env.Request);assert.equal(call.input.headers.get('X-Input'),'preserved');assert.equal(call.input.credentials,'include');assert.equal(call.input.cache,'no-store');assert.equal(call.input.redirect,'manual');}
 checks.push(`${type}/${name}`);
}
const controller=new AbortController();
const original=new env.Request('/api/submit',{method:'POST',body:'original body',headers:{'Content-Type':'text/plain','X-Original':'yes'},credentials:'include',mode:'cors',cache:'no-cache',redirect:'manual',referrer:origin+'/source',referrerPolicy:'same-origin',integrity:'sha256-test',keepalive:false,signal:controller.signal});
const override={method:'PUT',body:'override body',headers:{'X-Override':'yes'},credentials:'omit',redirect:'follow'};
await env.window.fetch(original,override);const captured=env.calls.at(-1);assert.equal(captured.input.url,origin+'/GRH-research/api/submit');
for(const property of['method','credentials','mode','cache','redirect','referrer','referrerPolicy','integrity','keepalive'])assert.equal(captured.input[property],original[property],`Request ${property}`);
assert.deepEqual([...captured.input.headers],[...original.headers]);assert.equal(await captured.input.clone().text(),'original body');assert.strictEqual(captured.init,override);
const effective=new env.Request(captured.input,captured.init);assert.equal(effective.method,'PUT');assert.equal(effective.credentials,'omit');assert.equal(effective.redirect,'follow');assert.equal(effective.headers.get('X-Override'),'yes');assert.equal(effective.headers.get('X-Original'),null);assert.equal(await effective.text(),'override body');controller.abort();assert(captured.input.signal.aborted,'Abort propagation preserved');checks.push('Request body/headers/method/credentials/mode/cache/redirect/referrer/integrity/keepalive/signal and explicit init overrides');
const keepaliveRequest=new env.Request('/data/keepalive.json',{keepalive:true});await env.window.fetch(keepaliveRequest);assert.equal(env.calls.at(-1).input.keepalive,true);checks.push('body-free Request keepalive preserved');
const old=environment(extract(before));assert.throws(()=>old.window.fetch(new URL('./data/a.json',current)),TypeError);assert.equal(old.calls.length,0);checks.push('negative control: previous runtime rejects same-origin URL input before native fetch');
let expected=before.replace('input instanceof URL?new URL(map(input.href)):input instanceof Request?new Request(map(input.url),input)','input instanceof URL?new URL(map(input.href),location.origin):input instanceof Request?new Request(new URL(map(input.url),location.origin),input)');expected=expected.replace("    for source,name in [('outputs/book/surface-orders-book.pdf','book.pdf'),('outputs/papers/resolutions-concise.pdf','concise.pdf'),('outputs/papers/resolutions-extended.pdf','extended.pdf')]:shutil.copyfile(ROOT/source,output/name)","    for source,name in [('outputs/book/surface-orders-book.pdf','book.pdf'),('outputs/papers/resolutions-concise.pdf','concise.pdf'),('outputs/papers/resolutions-extended.pdf','extended.pdf'),('papers/dessin-core.tex','papers/dessin-core.tex')]:\n        (output/name).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/source,output/name)");assert.equal(source,expected,'Only authorized constructor-base corrections plus exact public-paper copy block');
const digest=s=>createHash('sha256').update(s).digest('hex');
assert.equal(digest(extract(source)),'f8671345461a67648dd313817cf13209810f24314e343ece5a73862597feb94b','Runtime bytes unchanged by documentation-asset copy addition');
assert.equal(digest(source),'6f59dd43b53a61fb3c4c7ad626d3377507911379545544ceed693e50676dfa8a','Root-authorized exact source revision');
const report={passed:true,checks,checksCount:checks.length,networkRequests:0,sourceSha256:digest(source),beforeSha256:digest(before),runtimeSha256:digest(extract(source)),testSha256:digest(readFileSync(new URL(import.meta.url))),scope:'Full generated runtime executed in Node VM; native fetch stub only, browser-relative Request shim. No dependency, real network, bundle, UI, scientific-source or frozen-run change.'};
if(process.argv.length!==2&&!(process.argv.length===4&&process.argv[2]==='--output'))throw Error('Use optional --output FRESH_PATH only');
const output=process.argv.length===4?process.argv[3]:new URL('outputs/checks/2026-11-05-arithmetic-learning/adapter/node-vm-v2.json',ROOT);assert(!existsSync(output),'Preserve prior receipt; choose a fresh output path');
writeFileSync(output,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
