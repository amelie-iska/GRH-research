/* New lab-only checks. Call with the existing globally guarded BiDi Browser.
   This module does not connect/close a session, replace navigate, or filter errors. */
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const ROOT=new URL('../../../',import.meta.url);
const DATA=new URL('web/data/coherent-band-schur-v1.json',ROOT);
const DATA_SHA='e540ac344bbf3d4d07d1ac9fcb8c5cd336a6195c7130a602567242c33bc73171';
const SOURCE_SHA='fd5b33de0c54632b46d0515f5a3f67c7b91ceb896d09bd5f0303256f9fe91a04';
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const phase=e=>[Math.cos(e.phase6*Math.PI/3),Math.sin(e.phase6*Math.PI/3)];
function projected(e,stage){if(!e.support)return[0,0];let z=phase(e);if(stage!=='raw')z=z.map(x=>x*e.A_U);if(stage==='profile'){const[a,b]=e.W.map(Number);z=[z[0]*a-z[1]*b,z[0]*b+z[1]*a];}return z;}
function close(a,b){return Math.hypot(a[0]-b[0],a[1]-b[1])<4e-14;}
export async function runLab(b,base,out){
 const bytes=readFileSync(DATA);assert.equal(createHash('sha256').update(bytes).digest('hex'),DATA_SHA);const data=JSON.parse(bytes);const report={passed:false,checks:[],layouts:[],sourceSHA:SOURCE_SHA,payloadSHA:DATA_SHA,caseStageMatrices:0,renderedCellsChecked:0,savedStringPositionsChecked:0};
 const save=()=>writeFileSync(out+'/coherent-band-lab-so-far.json',JSON.stringify(report,null,2)+'\n');
 const check=(ok,name,detail=null)=>{report.checks.push({name,passed:!!ok,detail});save();assert(ok,name+': '+JSON.stringify(detail));};
 const ev=s=>b.evaluate(s);
 const pick=(id,v,event='change')=>ev(`(()=>{const e=document.getElementById(${JSON.stringify(id)});e.value=${JSON.stringify(String(v))};e.dispatchEvent(new Event(${JSON.stringify(event)},{bubbles:true}));return true})()`);
 const click=s=>ev(`document.querySelector(${JSON.stringify(s)}).click()`);
 const key=async(value,ctrl=false)=>{const actions=[];if(ctrl)actions.push({type:'keyDown',value:'\uE009'});actions.push({type:'keyDown',value},{type:'keyUp',value});if(ctrl)actions.push({type:'keyUp',value:'\uE009'});await b.send('input.performActions',{context:b.context,actions:[{type:'key',id:'coherent-band-keyboard',actions}]});};
 const select=async(i,j)=>{await pick('cbRow',i);await pick('cbCol',j);};
 const state=()=>ev('window.coherentBandLab.getState()');
 const expectEntry=async(c,e,stage,name)=>{await click(`[data-stage="${stage}"]`);await select(e.i,e.j);const got=await state();check(got.D===c.D&&got.i===e.i&&got.j===e.j&&got.support===e.support&&got.phase6===e.phase6&&got.A_U===e.A_U&&JSON.stringify(got.A_T)===JSON.stringify(e.A_T)&&JSON.stringify(got.W)===JSON.stringify(e.W)&&close(got.value,projected(e,stage)),name,got);};
 await b.viewport(1440,1050);await b.navigate(new URL('coherent-band.html',base.replace(/\/$/,'')+'/').href);
 await b.until(`document.getElementById('coherentBandLab')?.dataset.ready==='true'||document.getElementById('cbStatus')?.dataset.error==='true'`,30000);
 check(await ev(`document.getElementById('coherentBandLab').dataset.ready==='true'&&document.getElementById('cbStatus').dataset.verified==='true'`),'coherent-band-source-ready',await ev(`document.getElementById('cbStatus').textContent`));
 report.initial=await ev(`({theme:document.documentElement.dataset.theme,motion:document.documentElement.dataset.themeMotion})`);
 check(await ev(`window.coherentBandLab.getState().payloadSHA===${JSON.stringify(DATA_SHA)}&&window.coherentBandLab.getState().sourceSHA===${JSON.stringify(SOURCE_SHA)}&&document.querySelector('meta[name="coherent-band-data-sha256"]').content===${JSON.stringify(DATA_SHA)}`),'coherent-band-runtime-payload-source-hashes');
 check(JSON.stringify(await ev('window.coherentBandLab.getSummary()'))===JSON.stringify(data.totals),'coherent-band-1218-786-42-shape',await ev('window.coherentBandLab.getSummary()'));
 for(const c of data.cases){
  await pick('cbCase',c.D);await b.until(`window.coherentBandLab.getState().D===${c.D}`);
  const snap=await ev(`window.coherentBandLab.inspectCase(${c.D},'raw')`);assert.deepEqual(snap.norms,c.norms);for(let n=0;n<c.entries.length;n++){const{value,...entry}=snap.entries[n];assert.deepEqual(entry,c.entries[n]);assert(close(value,projected(entry,'raw')));report.savedStringPositionsChecked++;}
  check(true,'coherent-band-every-saved-string-'+c.D,{positions:c.entries.length,allNormStringsExact:true});
  for(const stage of ['raw','au','profile']){
   await click(`[data-stage="${stage}"]`);
   const cells=await ev(`Array.from(document.querySelectorAll('#cbMatrix [data-cell]'),e=>({index:Number(e.dataset.cell),support:Number(e.dataset.support),phase:e.dataset.phase6,z:[Number(e.dataset.valueReal),Number(e.dataset.valueImag)]}))`);
   assert.equal(cells.length,406);for(const got of cells){const e=c.entries[got.index];assert.equal(got.support,e.support);assert.equal(got.phase,e.phase6===null?'masked':String(e.phase6));assert(close(got.z,projected(e,stage)));}
   const norms=await ev(`Array.from(document.querySelectorAll('.cb-pipeline output'),e=>e.dataset.savedNorm)`);assert.deepEqual(norms,[c.norms.K_norm,c.norms.AU_K_norm,c.norms.W_AU_K_norm]);
   report.caseStageMatrices++;report.renderedCellsChecked+=cells.length;check(true,`coherent-band-all-406-rendered-${c.D}-${stage}`,{cells:406,normStringsExact:true});
  }
  await expectEntry(c,c.entries.find(e=>e.support&&e.phase6===0),'raw','coherent-band-phase0-is-one-'+c.D);
  await click('[data-preset="conjugate"]');const pair=await state();const pe=c.entries[pair.i*29+pair.j];check(pair.support===1&&data.row_ideals[pair.i].norm===7&&data.column_ideals[pair.j].norm===7&&pe.common_factors.length===0,'coherent-band-distinct-ideal-norm7-'+c.D,pair);
  await click('[data-preset="collision"]');check(await ev(`window.coherentBandLab.getState().support===0&&document.getElementById('cbMaskNote').textContent.includes('shared prime ideal')&&document.getElementById('cbSavedEntry').textContent.includes('only i, j and mask=0')`),'coherent-band-shared-prime-rawzero-'+c.D);
  const cap=c.entries.find(e=>!e.support&&e.mask_causes.includes('product_cutoff')&&!e.mask_causes.includes('shared_ideal_prime'));await expectEntry(c,cap,'raw','coherent-band-product-only-zero-'+c.D);
  const ann=c.entries.find(e=>e.support&&e.A_U!==0&&e.W.every(x=>Number(x)===0));await expectEntry(c,ann,'profile','coherent-band-annulus-zero-is-not-mask-'+c.D);check(await ev(`document.getElementById('cbEntryValue').textContent.includes('profile zero')`),'coherent-band-profile-zero-label-'+c.D);
  await click('[data-preset="inert"]');check(await ev(`window.coherentBandLab.getState().support===1&&document.querySelectorAll('#cbFactors .inert').length>0&&document.getElementById('cbFactors').textContent.includes('norm p²')`),'coherent-band-inert-prime-factor-'+c.D);
  const here=await state();check(await ev(`document.getElementById('cbSavedEntry').textContent.includes(${JSON.stringify(here.A_T[0])})&&document.getElementById('cbSavedEntry').textContent.includes(${JSON.stringify(here.W[0])})&&document.getElementById('cbPerronNorms').textContent.includes(${JSON.stringify(c.norms.residual_norm)})`),'coherent-band-selected-55digit-Perron-profile-'+c.D);
  await select(13,28);check(await ev(`window.coherentBandLab.getState().i===13&&window.coherentBandLab.getState().j===28&&document.getElementById('cbRow').options.length===14&&document.getElementById('cbCol').options.length===29`),'coherent-band-full-selector-ranges-'+c.D);
 }
 await pick('cbCase',121);await click('[data-stage="raw"]');await select(0,0);await ev(`document.querySelector('#cbMatrix [data-cell="0"]').focus()`);await key('\uE014');check((await state()).j===1,'coherent-band-keyboard-right');await key('\uE015');check((await state()).i===1,'coherent-band-keyboard-down');await key('\uE010');check((await state()).j===28,'coherent-band-keyboard-end');await key('\uE011');check((await state()).j===0,'coherent-band-keyboard-home');await key('\uE010',true);const last=await state();check(last.i===13&&last.j===28,'coherent-band-keyboard-control-end');await key('\uE011',true);const first=await state();check(first.i===0&&first.j===0,'coherent-band-keyboard-control-home');
 await pick('cbZoom',1.75,'input');check(await ev(`document.getElementById('cbZoomValue').textContent==='1.75×'&&document.getElementById('cbMatrixHost').style.getPropertyValue('--zoom')==='1.75'`),'coherent-band-zoom-range');await pick('cbZoom',1,'input');
 for(const theme of ['light','biomech']){
  await ev(`(()=>{if(document.documentElement.dataset.theme!==${JSON.stringify(theme)})document.getElementById('themeToggle').click();if(document.documentElement.dataset.theme==='biomech'&&document.documentElement.dataset.themeMotion==='live')document.getElementById('motionToggle').click();document.documentElement.style.scrollBehavior='auto';return true})()`);await sleep(3100);
  for(const width of [320,390,1440]){
   await b.viewport(width,width<500?844:1050);
   for(const c of data.cases){await pick('cbCase',c.D);for(const stage of ['raw','au','profile']){await click(`[data-stage="${stage}"]`);const v=await ev(`({width:innerWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,stage:window.coherentBandLab.getState().stage,D:window.coherentBandLab.getState().D,matrixFilter:getComputedStyle(document.getElementById('cbMatrix')).filter,planeFilter:getComputedStyle(document.getElementById('cbPlane')).filter,hostWidth:document.getElementById('cbMatrixHost').clientWidth,hostScroll:document.getElementById('cbMatrixHost').scrollWidth,cellCount:document.querySelectorAll('#cbMatrix [data-cell]').length,bodyBackground:getComputedStyle(document.body).backgroundColor})`);assert(v.scroll<=width+1,`Overflow ${theme}/${width}/${c.D}/${stage}: ${v.scroll}`);assert.equal(v.matrixFilter,'none');assert.equal(v.planeFilter,'none');assert.equal(v.cellCount,406);report.layouts.push(v);}}
   check(true,`coherent-band-nine-layouts-${theme}-${width}`,{layouts:9});
   await pick('cbCase',121);await click('[data-preset="inert"]');await ev(`document.getElementById('cbMatrixHeading').scrollIntoView({block:'start',behavior:'auto'})`);await sleep(300);await b.screenshot(out+`/coherent-band-${theme}-${width}.png`);
  }
 }
 check(report.layouts.length===54&&report.caseStageMatrices===9&&report.renderedCellsChecked===3654&&report.savedStringPositionsChecked===1218,'coherent-band-complete-lab-coverage',{layouts:report.layouts.length,caseStages:report.caseStageMatrices,cells:report.renderedCellsChecked,savedPositions:report.savedStringPositionsChecked});
 const nativeHead=await ev(`(async()=>{const r=await fetch(new Request(new URL('data/coherent-band-schur-v1.json',document.baseURI),{method:'HEAD'}));return{status:r.status,url:r.url}})()`);check(nativeHead.status===200,'coherent-band-native-URL-Request-HEAD',nativeHead);
 check(await ev(`document.body.textContent.includes('not full physical-row-family data')&&document.body.textContent.includes('interval enclosures')&&document.body.textContent.includes('C²')&&document.getElementById('cbFactors').textContent.includes('source canonical generator')`),'coherent-band-auxiliary-precision-profile-generator-scope');
 await ev(`(()=>{if(document.documentElement.dataset.theme!==${JSON.stringify(report.initial.theme)})document.getElementById('themeToggle').click();if(document.documentElement.dataset.theme==='biomech'&&document.documentElement.dataset.themeMotion!==${JSON.stringify(report.initial.motion)})document.getElementById('motionToggle').click();return true})()`);
 report.passed=true;report.scope='Only the new source-bound auxiliary-matrix lab. No legacy release/old arithmetic control replay. Root caller retains exact global WS,750ms quiet,30s idle and unfiltered fetch/page-error guards.';writeFileSync(out+'/coherent-band-lab.json',JSON.stringify(report,null,2)+'\n');return report;
}
