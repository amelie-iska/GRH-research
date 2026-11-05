// Read-only lifecycle regression harness. No browser or external dependency.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const rendererPath='planning/book-integration-20261104/render_native.py';
const runtimePath='planning/book-integration-20261104/reviewed-math-scroll.js';
const renderer=readFileSync(rendererPath,'utf8');
const runtime=readFileSync(runtimePath,'utf8');
const guard=renderer.match(/parse_guard='(<script>.*?<\/script><style>.*?<\/style>)'/)?.[1];
assert.ok(guard,'Extract the literal emitted head guard');
const inline=guard.match(/<script>(.*?)<\/script>/)?.[1];
assert.ok(inline);
assert.ok(guard.includes('html.native-math-pending math{display:none!important}'));
assert.ok(renderer.includes('<script defer="defer" src="reviewed-math-scroll.js"></script>'));
const names=[];
function environment({throwOnQuery=false}={}) {
  const classes=new Set();
  const listeners=new Map();
  const trace=[];
  const context={};
  const classList={
    add(name){classes.add(name);trace.push('add:'+name);},
    remove(name){classes.delete(name);trace.push('remove:'+name);},
    contains(name){return classes.has(name);}
  };
  const document={
    readyState:'loading',documentElement:{classList},fonts:null,
    addEventListener(type,callback,options){
      const records=listeners.get(type)??[];records.push({callback,once:options?.once===true});listeners.set(type,records);
    },
    querySelectorAll(selector){
      assert.equal(classList.contains('native-math-pending'),false,'Unhide before measuring math');
      trace.push('query:'+selector);
      if(throwOnQuery)throw Error('synthetic fitting failure');
      return [];
    }
  };
  Object.assign(context,{document,window:context,
    addEventListener(){},requestAnimationFrame(callback){callback();}});
  const realm=vm.createContext(context);
  const execute=(script)=>vm.runInContext(script,realm);
  const fire=(type)=>{
    document.readyState='interactive';trace.push('event:'+type);
    const records=[...(listeners.get(type)??[])];
    listeners.set(type,(listeners.get(type)??[]).filter(x=>!x.once));
    for(const record of records)record.callback();
  };
  return {classes,listeners,trace,context,execute,fire};
}
{
  const e=environment(); // Scripts disabled: neither guard nor runtime executes.
  e.fire('DOMContentLoaded');assert.equal(e.classes.size,0);names.push('no-JS content remains visible');
}
{
  const e=environment();e.execute(inline);
  assert.ok(e.classes.has('native-math-pending'));
  assert.equal(e.listeners.get('DOMContentLoaded').length,1);
  assert.equal(e.listeners.get('DOMContentLoaded')[0].once,true);
  e.fire('DOMContentLoaded');assert.equal(e.classes.has('native-math-pending'),false);
  const removals=e.trace.filter(x=>x.startsWith('remove:')).length;
  e.fire('DOMContentLoaded');assert.equal(e.trace.filter(x=>x.startsWith('remove:')).length,removals);
  names.push('blocked external helper releases once at DOMContentLoaded');
}
{
  const e=environment();e.execute(inline);e.context.document.readyState='interactive';
  e.execute(runtime);
  assert.equal(e.classes.has('native-math-pending'),false);
  assert.equal(typeof e.context.fitReviewedReaderMath,'function');
  assert.ok(e.trace.indexOf('remove:native-math-pending')<e.trace.indexOf('query:math'));
  e.fire('DOMContentLoaded');assert.equal(e.classes.has('native-math-pending'),false);
  names.push('deferred helper releases before math measurement; fallback is idempotent');
}
{
  const e=environment();e.execute(inline);e.fire('DOMContentLoaded');e.execute(runtime);
  assert.equal(e.classes.has('native-math-pending'),false);
  names.push('late helper after fallback remains visible');
}
{
  const e=environment({throwOnQuery:true});e.execute(inline);
  assert.throws(()=>e.execute(runtime),/synthetic fitting failure/);
  assert.equal(e.classes.has('native-math-pending'),false);
  e.fire('DOMContentLoaded');assert.equal(e.classes.has('native-math-pending'),false);
  names.push('helper fitting exception cannot leave parse guard active');
}
{
  const e=environment();e.execute(runtime);
  assert.equal(e.classes.has('native-math-pending'),false);
  names.push('external helper also works when inline script is blocked');
}
const hash=s=>createHash('sha256').update(s).digest('hex');
console.log(JSON.stringify({passed:true,cases:names,renderer_sha256:hash(renderer),runtime_sha256:hash(runtime),scope:'Synthetic lifecycle regression controls only; no Firefox9335 access or browser-layout claim.'},null,2));
