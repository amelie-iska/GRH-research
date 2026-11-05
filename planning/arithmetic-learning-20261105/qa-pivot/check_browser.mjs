import {Browser} from '/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
const url=process.env.PIVOT_QA_URL;
assert(url?.startsWith('http://127.0.0.1:'),'Explicit isolated loopback fixture required');
const out=new URL('file://'+process.env.PIVOT_QA_RUN_DIR+'/');
const browser=await new Browser().connect();
const report={passed:false,layouts:[],controls:[],keyboard:[],contrast:[]};
const pause=ms=>new Promise(r=>setTimeout(r,ms));
const pick=async(id,value,event='change')=>browser.evaluate(`(()=>{const e=document.getElementById(${JSON.stringify(id)});e.value=${JSON.stringify(String(value))};e.dispatchEvent(new Event(${JSON.stringify(event)},{bubbles:true}));return true})()`);
const key=async value=>browser.send('input.performActions',{context:browser.context,actions:[{type:'key',id:'pivot-keyboard',actions:[{type:'keyDown',value},{type:'keyUp',value}]}]});
try {
 await browser.viewport(1440,1050);await browser.navigate(url+'/quadratic-pivot.html');
 await browser.until('document.body.dataset.ready==="true"&&document.getElementById("themeToggle")');
 const initial=await browser.evaluate('({theme:document.documentElement.dataset.theme,motion:document.documentElement.dataset.themeMotion})');
 // Persisted settings are restored in finally; this harness owns no browser process.
 report.initialPreferences=initial;
 for(const theme of ['light','biomech']){
  await browser.evaluate(`(()=>{if(document.documentElement.dataset.theme!==${JSON.stringify(theme)})document.getElementById('themeToggle').click();if(document.documentElement.dataset.themeMotion==='live'&&document.documentElement.dataset.theme==='biomech')document.getElementById('motionToggle').click();return true})()`);
  await pause(3100);
  for(const width of [320,390,768,1440]){
   await browser.viewport(width,width<500?844:1050);await pause(130);
   const state=await browser.evaluate(`(()=>{const s=document.getElementById('exponentPlot'),r=s.getBoundingClientRect();return{width:innerWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,plotWidth:r.width,plotHeight:r.height,viewBox:s.getAttribute('viewBox'),fullFace:s.dataset.fullFace,titleCount:s.querySelectorAll('title').length,filter:getComputedStyle(s).filter,capacity:document.getElementById('capacityStatus').dataset.valid}})()`);
   assert(state.scroll<=width+1,`Overflow at ${width}/${theme}: ${state.scroll}`);assert(state.plotWidth>250&&state.plotHeight>=370);assert.equal(state.fullFace,'0,0.25');assert.equal(state.titleCount,1);assert.equal(state.filter,'none');assert.equal(state.capacity,'true');
   report.layouts.push(state);
   await browser.evaluate(`document.getElementById('face-title').scrollIntoView({block:'start'})`);await browser.screenshot(new URL(`plot-${theme}-${width}.png`,out).pathname);
  }
  // Verify the actual theme colors remain readable, including all line labels.
  report.contrast.push(await browser.evaluate(`(()=>{const rgb=s=>s.match(/[0-9.]+/g).slice(0,3).map(Number),lum=c=>rgb(c).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4}).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0),bg=lum(getComputedStyle(document.getElementById('exponentPlot')).backgroundColor);return{theme:document.documentElement.dataset.theme,ratios:[...document.querySelectorAll('.plot-legend li')].map(e=>{const fg=lum(getComputedStyle(e).color);return{label:e.textContent,ratio:(Math.max(fg,bg)+.05)/(Math.min(fg,bg)+.05)}})}})()`));
 }
 for(const group of report.contrast)for(const c of group.ratios)assert(c.ratio>=4.5,`${group.theme}/${c.label} contrast ${c.ratio}`);
 for(const [position,power,historical] of [[0,1,1],[1,1,1.0005],[250,1,1.125],[499,1,1.2495],[500,1,1.25],[501,1,1.25],[1000,1,1.25]]){
  await pick('aValue',position,'input');
  const s=await browser.evaluate(`({power:Number(document.getElementById('exponentPlot').dataset.refinedPower),historical:Number(document.getElementById('exponentPlot').dataset.historicalPower),text:document.getElementById('sectorStatus').textContent,capacity:document.getElementById('capacityStatus').dataset.valid,values:document.getElementById('termRows').rows.length})`);
  assert(Math.abs(s.power-power)<1e-12);assert(Math.abs(s.historical-historical)<1e-12);assert(s.text.includes('entire face'));assert.equal(s.capacity,'true');assert.equal(s.values,7);report.controls.push({position,...s});
 }
 await pick('aValue',250,'input');
 for(const d of [4,8,12,24,48]){await pick('dScale',d);const value=await browser.evaluate(`({sum:document.getElementById('quadSum').textContent,power:document.getElementById('refinedPower').textContent})`);assert.equal(value.power,'1.000');report.controls.push({d,...value});}
 for(const width of [320,390,768,1440]){
  await browser.viewport(width,width<500?844:1050);await pick('plotView','terms');await pause(100);
  const text=await browser.evaluate(`({legendHidden:document.getElementById('termLegend').hidden,labels:[...document.querySelectorAll('#exponentPlot text')].map(x=>x.textContent),scroll:document.documentElement.scrollWidth})`);
  assert.equal(text.legendHidden,false);assert(text.labels.includes('0.25'));assert(text.scroll<=width+1);
  if(width===390||width===1440){await browser.evaluate(`document.getElementById('face-title').scrollIntoView({block:'start'})`);await browser.screenshot(new URL(`terms-biomech-${width}.png`,out).pathname);}
 }
 await pick('plotView','envelopes');await browser.evaluate(`document.getElementById('aValue').focus()`);
 for(const [value,expected] of [['\uE011','0'],['\uE014','1'],['\uE010','1000'],['\uE012','999']]){await key(value);const actual=await browser.evaluate(`document.getElementById('aValue').value`);assert.equal(actual,expected);report.keyboard.push({key:value,actual});}
 // Keyboard scope is the new owned control surface. Shared theme keyboard behavior is unchanged.
 await browser.evaluate(`document.getElementById('dScale').focus()`);await key('\uE011');await key('\uE010');
 assert.equal(await browser.evaluate(`document.getElementById('dScale').value`),'48');report.keyboard.push({scaleHomeEnd:true});
 await browser.evaluate(`document.getElementById('plotView').focus()`);await key('\uE011');await key('\uE015');
 await browser.until(`document.getElementById('plotView').value==='terms'`);assert.equal(await browser.evaluate(`document.getElementById('termLegend').hidden`),false);report.keyboard.push({detailArrowDown:true});
 // New two-dimensional map and exact witness controls.
 for(const name of ['mixed','pure']){await browser.evaluate(`document.querySelector('[data-witness="${name}"]').click()`);const w=await browser.evaluate(`({power:Number(document.getElementById('obstructionPlot').dataset.currentPower),x1:Number(document.getElementById('obstructionPlot').dataset.x1),x2:Number(document.getElementById('obstructionPlot').dataset.x2)})`);assert(Math.abs(w.power-7/6)<1e-12);report.controls.push({witness:name,...w});}
 await browser.evaluate(`document.getElementById('obstructionPlot').focus()`);await key('\uE012');const moved=await browser.evaluate(`Number(document.getElementById('obstructionPlot').dataset.x1)`);assert(moved<.75);report.keyboard.push({triangleArrowLeft:true});
 for(const width of [320,390,768,1440]){await browser.viewport(width,width<500?844:1050);await pause(100);const g=await browser.evaluate(`({scroll:document.documentElement.scrollWidth,filter:getComputedStyle(document.getElementById('obstructionPlot')).filter,cells:document.querySelectorAll('#obstructionPlot polygon').length})`);assert(g.scroll<=width+1);assert.equal(g.filter,'none');assert.equal(g.cells,1024);await browser.evaluate(`document.getElementById('obstruction-title').scrollIntoView({block:'start'})`);await browser.screenshot(new URL(`obstruction-${width}.png`,out).pathname);}
 assert.equal(await browser.evaluate(`new Set([...document.querySelectorAll('[id]')].map(e=>e.id)).size===document.querySelectorAll('[id]').length`),true);
 assert.equal(await browser.evaluate(`document.querySelectorAll('script[src^="http"]').length+document.querySelectorAll('link[href^="http"]').length`),0);
 report.pageErrors=browser.pageErrors().map(e=>e.params.text);assert.deepEqual(report.pageErrors,[]);
 report.fetchErrors=browser.events.filter(e=>e.method==='network.fetchError');assert.deepEqual(report.fetchErrors,[]);
 // A real embedded page shares the parent's theme and suppresses duplicate toggles.
 await browser.viewport(768,1050);await browser.navigate(url+'/__pivot_embed_fixture__');await browser.until(`document.querySelector('iframe')?.contentDocument?.body.dataset.ready==='true'`);
 const embedded=await browser.evaluate(`(()=>{const d=document.querySelector('iframe').contentDocument;return{embedded:d.documentElement.dataset.themeEmbedded,theme:d.documentElement.dataset.theme,toggles:d.querySelectorAll('#themeToggle').length,ready:d.body.dataset.ready}})()`);
 assert.equal(embedded.embedded,'true');assert.equal(embedded.toggles,0);assert.equal(embedded.ready,'true');report.embedded=embedded;
 report.passed=true;report.scope='Real Firefox9335 UI, both palettes, four viewport widths, every control, native keyboard input, independent evaluator separately checked. Includes triangular map, both7/6 witnesses and native map arrow navigation. New book/research hyperlinks are integration targets checked by root.';
 writeFileSync(new URL('browser.json',out),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
} finally {
 try{await browser.navigate(url+'/quadratic-pivot.html');await browser.until('document.getElementById("themeToggle")');if(report.initialPreferences){await browser.evaluate(`(()=>{if(document.documentElement.dataset.theme!==${JSON.stringify(report.initialPreferences.theme)})document.getElementById('themeToggle').click();if(document.documentElement.dataset.themeMotion!==${JSON.stringify(report.initialPreferences.motion)}&&document.documentElement.dataset.theme==='biomech')document.getElementById('motionToggle').click();return true})()`);}}catch{}
 await browser.close();
}
