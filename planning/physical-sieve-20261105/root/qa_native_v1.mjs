import {Browser} from '/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import {writeFileSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const expectedMath=Number(process.env.BOOK_QA_EXPECTED_MATH??6216);
const base=process.env.BOOK_QA_URL,out=process.env.BOOK_QA_OUTPUT,candidate=process.env.BOOK_QA_CANDIDATE;
if(!base||!out||!candidate)throw Error('Explicit QA URL/output/candidate required');
const sha=data=>createHash('sha256').update(data).digest('hex');
const browser=await new Browser().connect();
const check=(condition,message,detail)=>{if(!condition)throw Error(message+' '+JSON.stringify(detail??''));};
const geometry='({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,inner:innerWidth,math:document.querySelectorAll("math").length})';
const subtreeHashes=`(async()=>{const result={};for(const tag of ['math','table','iframe']){const values=[...document.querySelectorAll(tag)].filter(x=>!x.closest('.new-reviewed-chapters')).map(x=>x.outerHTML);const bytes=new TextEncoder().encode(values.join('\\n'));result[tag]={count:values.length,sha256:[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('')};}return result})()`;
const jump=async id=>browser.evaluate(`(()=>{document.getElementById(${JSON.stringify(id)}).scrollIntoView({block:'start'});window.scrollBy(0,-110);return true})()`);
try{
 await browser.viewport(390,844);await browser.navigate(base+'/baseline/book/main.html');
 await browser.evaluate('document.fonts.ready.then(()=>true)');
 await browser.evaluate('(()=>{fitReaderMath();return true})()');
 const baseline=await browser.evaluate(geometry),baselineSubtrees=await browser.evaluate(subtreeHashes);
 const baselineDiagnostics=browser.pageErrors();
 const malformedBaseline=await browser.evaluate(`([...document.querySelectorAll('munder')].filter(x=>x.children.length!==2).map(x=>x.outerHTML))`);
 check(baseline.math===5356,'Baseline math count',baseline);
 writeFileSync(out+'/baseline-dom.json',JSON.stringify({geometry:baseline,subtrees:baselineSubtrees},null,2));
 await browser.viewport(1440,1000);await browser.navigate(base+'/book/main.html');
 await browser.until('document.querySelectorAll("math").length==='+expectedMath+' && typeof fitReviewedReaderMath==="function"');
 await browser.evaluate('document.fonts.ready.then(()=>true)');
 const state=await browser.evaluate(`(()=>{
 const ids=[...document.querySelectorAll('[id]')].map(x=>x.id);
 const anchors=['cmr:core','cmr:joint','cmr:conditional-strip','phy:core','phy:global','phy:signed','phy:short','mm:afm','rc:recombination','rc:boundary','wc:uniform','wc:powered-input','wc:literal-reciprocity','sb:window','sb:covariance-example','sb:perron-factor','sb:perron-error'];
 const refs=[...document.querySelectorAll('a[href^="#mm:"],a[href^="#rc:"],a[href^="#wc:"],a[href^="#sb:"]')];
 return {math:document.querySelectorAll('math').length,iframes:document.querySelectorAll('iframe').length,uniqueFrames:new Set([...document.querySelectorAll('iframe')].map(x=>x.getAttribute('src'))).size,anchors:anchors.map(id=>({id,present:!!document.getElementById(id)})),allNewRefsResolve:refs.every(x=>!!document.getElementById(x.getAttribute('href').slice(1))),uniqueIds:new Set(ids).size===ids.length,chapters:[...document.querySelectorAll('h2.chapterHead')].map(x=>x.textContent.trim()).slice(-4),bodyWidth:document.body.scrollWidth,clientWidth:document.documentElement.clientWidth};})()`);
 check(state.math===expectedMath&&state.iframes===13&&state.uniqueFrames===13&&state.anchors.every(x=>x.present)&&state.allNewRefsResolve&&state.uniqueIds,'DOM integrity',state);
 const candidateSubtrees=await browser.evaluate(subtreeHashes);
 check(JSON.stringify(candidateSubtrees)===JSON.stringify(baselineSubtrees),'Browser old subtree fidelity',{baselineSubtrees,candidateSubtrees});
 writeFileSync(out+'/initial-dom.json',JSON.stringify(state,null,2));
 await jump('wc:uniform');await browser.screenshot(out+'/weighted-envelope-desktop.png');
 await jump('rc:recombination');await browser.screenshot(out+'/cutoff-convergence-desktop.png');
 await jump('sb:window');await browser.screenshot(out+'/high-window-desktop.png');
 await jump('sb:covariance-example');await browser.screenshot(out+'/signed-covariance-desktop.png');
 await jump('sb:perron-error');await browser.screenshot(out+'/double-perron-desktop.png');
 for(const id of ['cmr:core','cmr:joint','cmr:conditional-strip','phy:core','phy:global','phy:signed','phy:short']){await jump(id);await browser.screenshot(out+'/'+id.replace(':','-')+'-desktop.png');}
 const downloads=[];
 for(const name of ['validated-oracle-details.tex','masked-moment-details.tex','weighted-cutoff-details.tex','signed-bilinear-core.tex','signed-bilinear-details.tex','coherent-main-core.tex','coherent-main-details.tex','physical-sieve-core.tex','physical-sieve-details.tex']){
  const downloaded=await browser.evaluate(`fetch('/book/sources/${name}').then(async r=>({status:r.status,text:await r.text()}))`);
  const expected=readFileSync(candidate+'/book/sources/'+name);
  check(downloaded.status===200&&sha(downloaded.text)===sha(expected),'Source download mismatch',name);
  downloads.push({path:'/book/sources/'+name,status:downloaded.status,bytes:expected.length,sha256:sha(expected)});
 }
 const pdf=await browser.evaluate(`fetch('/book.pdf').then(async r=>({status:r.status,bytes:(await r.arrayBuffer()).byteLength,contentType:r.headers.get('content-type')}))`);
 check(pdf.status===200&&pdf.bytes>100000&&pdf.contentType==='application/pdf','PDF download',pdf);
 const viewports=[];
 for(const [width,height] of [[390,844],[320,740],[768,1024],[1440,1000],[390,844]]){
  await browser.viewport(width,height);
  await browser.evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(()=>{fitReaderMath();fitReviewedReaderMath();resolve(true)})))');
  const sizes=await browser.evaluate(geometry);
  check(sizes.inner===width&&sizes.client<=width&&width-sizes.client<=20&&sizes.scroll<=sizes.client+1,'Viewport overflow',{width,...sizes});
  const equations=await browser.evaluate(`(()=>{
   const boxes=[...document.querySelectorAll('.reader-display-math,.reader-inline-math,.reader-table-scroll')].filter(x=>x.scrollWidth>x.clientWidth+1);
   return boxes.map(box=>{const old=box.scrollLeft;box.scrollLeft=box.scrollWidth;const end=box.scrollLeft;box.scrollLeft=old;const math=box.querySelector('math');return{class:box.className,client:box.clientWidth,scroll:box.scrollWidth,end,tabIndex:box.tabIndex,label:box.getAttribute('aria-label'),mathFont:math?getComputedStyle(math).fontSize:null,transform:math?getComputedStyle(math).transform:null};});})()`);
  check(equations.every(x=>x.end>0&&x.tabIndex>=0&&x.label&&(!x.mathFont||parseFloat(x.mathFont)>=18)&&(!x.transform||x.transform==='none')),'Equation accessibility/readability',equations.filter(x=>x.end<=0||x.tabIndex<0||!x.label||x.mathFont&&parseFloat(x.mathFont)<18||x.transform&&x.transform!=='none'));
  viewports.push({requested:{width,height},geometry:sizes,scrollableExpressions:equations.length,equations});
 }
 await jump('wc:uniform');
 const uniform=await browser.evaluate(`(()=>{const e=document.getElementById('wc:minimum'),box=e.querySelector('.reader-display-math');return{number:e.querySelector('.reader-equation-number').textContent,mathFont:getComputedStyle(e.querySelector('math')).fontSize,box:box?{client:box.clientWidth,scroll:box.scrollWidth}:null};})()`);
 check(uniform.box&&uniform.box.scroll>uniform.box.client&&uniform.number==='(40.4)'&&uniform.mathFont==='18px','Uniform envelope layout',uniform);
 await jump('wc:minimum');await browser.screenshot(out+'/weighted-envelope-mobile.png');
 await browser.evaluate('(()=>{document.getElementById("wc:minimum").querySelector(".reader-display-math").scrollLeft=99999;return true})()');
 await browser.evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(()=>resolve(true))))');
 await browser.screenshot(out+'/weighted-envelope-mobile-scrolled.png');
 check(sha(readFileSync(out+'/weighted-envelope-mobile.png'))!==sha(readFileSync(out+'/weighted-envelope-mobile-scrolled.png')),'Scroll screenshot did not change');
 await jump('rc:recombination');await browser.screenshot(out+'/cutoff-convergence-mobile.png');
 await browser.evaluate(`(()=>{document.querySelector('.new-reviewed-chapters a[href="#wc:uniform"]').click();return true})()`);
 await browser.until('decodeURIComponent(location.hash)==="#wc:uniform"');
 const link=await browser.evaluate(`({hash:decodeURIComponent(location.hash),targetPresent:!!document.getElementById('wc:uniform')})`);
 check(link.hash==='#wc:uniform'&&link.targetPresent,'Reference click',link);
 await browser.evaluate('(()=>{document.getElementById("themeToggle").click();if(document.documentElement.dataset.themeMotion==="live")document.getElementById("motionToggle").click();return true})()');
 await browser.until(`getComputedStyle(document.body).backgroundColor==='rgb(7, 13, 20)'&&getComputedStyle(document.body).color==='rgb(210, 225, 230)'&&getComputedStyle(document.querySelector('.new-reviewed-chapters')).color==='rgb(210, 225, 230)'&&getComputedStyle(document.getElementById('wc:minimum').querySelector('math')).color==='rgb(210, 225, 230)'`);
 await jump('phy:short');await browser.screenshot(out+'/physical-short-mobile-night.png');
 await jump('cmr:conditional-strip');await browser.screenshot(out+'/coherent-input-mobile-night.png');
 await jump('wc:minimum');await browser.screenshot(out+'/weighted-envelope-mobile-night.png');
 const night=await browser.evaluate(`(()=>{const body=getComputedStyle(document.body),math=getComputedStyle(document.getElementById('wc:minimum').querySelector('math'));const luminance=color=>{const rgb=color.match(/[0-9.]+/g).slice(0,3).map(x=>Number(x)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return .2126*rgb[0]+.7152*rgb[1]+.0722*rgb[2]};const bg=luminance(body.backgroundColor),fg=luminance(math.color);return{client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,motion:document.documentElement.dataset.themeMotion,background:body.backgroundColor,bodyInk:body.color,mathInk:math.color,mathFont:math.fontSize,baseColorContrast:(Math.max(bg,fg)+.05)/(Math.min(bg,fg)+.05)};})()`);
 check(night.scroll<=night.client+1&&night.baseColorContrast>=7,'Stable night layout/contrast',night);
 await browser.evaluate('(()=>{document.getElementById("themeToggle").click();return true})()');
 const diagnostics=browser.pageErrors();
 const inheritedMessages=new Set(baselineDiagnostics.map(x=>x.params.text));
 const errors=diagnostics.filter(x=>!inheritedMessages.has(x.params.text));
 const malformedCandidate=await browser.evaluate(`([...document.querySelectorAll('munder')].filter(x=>x.children.length!==2&&!x.closest('.new-reviewed-chapters')).map(x=>x.outerHTML))`);
 const malformedNew=await browser.evaluate(`document.querySelectorAll('.new-reviewed-chapters munder').length===0||[...document.querySelectorAll('.new-reviewed-chapters munder')].every(x=>x.children.length===2)`);
 check(JSON.stringify(malformedCandidate)===JSON.stringify(malformedBaseline)&&malformedNew,'Malformed MathML regression',{old:malformedBaseline.length,candidate:malformedCandidate.length,malformedNew});
 check(errors.length===0,'New browser errors',errors);
 const inheritedMathMLDiagnostics={baselineEvents:baselineDiagnostics.length,candidateEvents:diagnostics.length,messages:[...inheritedMessages],oldMalformedMunderNodes:malformedBaseline.length,newMalformedMunderNodes:0,scope:'Three old TeX4ht lim-leftarrow munder nodes have three children. Preserved by the required unchanged-old-MathML policy. Reflow repeats Firefox diagnostics; no new distinct diagnostic or new malformed node.'};
 const record={passed:true,browser:'Isolated Firefox BiDi9335',baseline,state,baselineSubtrees,candidateSubtrees,downloads,pdf,viewports,uniform,link,night,inheritedMathMLDiagnostics,pageErrors:errors,scope:'New chapters, all old DOM math/table/iframe hashes, exact source downloads, PDF, real reference click, 320/390/768/1440px layouts and full-size keyboard-focusable scrollable equations. New physical/coherent proof anchors and9exactsource downloads; current8552 subtree preservation independently checked. No production promotion.'};
 writeFileSync(out+'/browser.json',JSON.stringify(record,null,2)+'\n');
 console.log(JSON.stringify({passed:true,baseline,viewports:viewports.map(x=>({requested:x.requested,...x.geometry,scrollableExpressions:x.scrollableExpressions})),uniform,oldSubtrees:baselineSubtrees,sourceDownloads:downloads.length,newPageErrors:errors.length,inheritedMathMLDiagnostics},null,2));
}finally{await browser.close();}
