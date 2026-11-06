import assert from'node:assert/strict';import{writeFileSync,mkdirSync}from'node:fs';import path from'node:path';
export async function runGaussTail(browser,base,out,expected,pdfMap,controls){
 mkdirSync(out,{recursive:true});
 const b={navigate:url=>browser.navigate(url),evaluate:x=>browser.evaluate(x),eval:(fn,arg)=>browser.evaluate('('+fn.toString()+')('+JSON.stringify(arg)+')'),until:(x,t)=>browser.until(x,t),viewport:(w,h)=>browser.viewport(w,h),screenshot:name=>browser.screenshot(path.join(out,name)),key:value=>browser.send('input.performActions',{context:browser.context,actions:[{type:'key',id:'gauss-release-keyboard',actions:[{type:'keyDown',value},{type:'keyUp',value}]}]})};
 const delay=ms=>new Promise(r=>setTimeout(r,ms)),labels=expected.labels,sourceNames=['gauss-tail-core.tex','gauss-tail-figure.tex','gauss-tail-details.tex'],pdf={pdf_sha256:pdfMap.public_files['book.pdf']},timing=controls.timing,idleWaits=controls.idleWaits,pendingRequests=controls.pendingRequests,idle=controls.idle;
 const report={schema:'gauss-tail-public-bundle-focused-browser-v1',passed:false,scope:'40 focused checks in SAME full-release owned context/global timing; public-prefix bundle bytes only, no candidate HTTP fallback.',checks:[],layouts:[],expected:{labels,math_nodes:10299,math_nodes_added:489,tables:389,frames:14,svg_refs:31,pdf_pages:333}};
 const write=(name,value)=>writeFileSync(path.join(out,name),JSON.stringify(value,null,2)+'\n');
 function check(ok,name,detail){report.checks.push({name,passed:!!ok,detail});write('checks-so-far.json',report);assert(ok,name+': '+JSON.stringify(detail));}
 async function jump(id){await b.eval(id=>{document.getElementById(id).scrollIntoView({behavior:'instant',block:'start'});window.scrollBy(0,-110);return true;},id);await delay(150);}
 async function fit(){await b.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>{fitReaderMath();fitReviewedReaderMath();r(true)})))');}
 async function asset(url,expectedSha){const value=await b.eval(async url=>{const r=await fetch(url);const data=await r.arrayBuffer();return{url:r.url,status:r.status,bytes:data.byteLength,sha256:[...new Uint8Array(await crypto.subtle.digest('SHA-256',data))].map(x=>x.toString(16).padStart(2,'0')).join('')};},url);check(value.status===200&&value.sha256===expectedSha,'source-bound-download-'+new URL(url).pathname.replace(/^\/GRH-research/,''),value);return value;}
await b.viewport(1440,1050);await b.navigate(base+'/book/main.html#gtl:core');
 await b.until('document.readyState==="complete"&&!!document.getElementById("gauss-tail-section")');await b.evaluate('document.fonts.ready.then(()=>true)');await fit();
 check(await b.eval(n=>document.querySelectorAll('math').length===n,expected.math_nodes),'candidate-record-math-count',expected.math_nodes);
 const state=await b.eval(labels=>{
  const root=document.getElementById('gauss-tail-section'),allIds=[...document.querySelectorAll('[id]')].map(e=>e.id),newLabels=[...root.querySelectorAll('[id^="gtl:"]')].map(e=>e.id);
  const refs=[...root.querySelectorAll('a[href^="#"]')].map(a=>({id:decodeURIComponent(a.getAttribute('href').slice(1)),text:a.textContent,exists:!!document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))}));
  const malformed=[...root.querySelectorAll('msub,msup,munder,mover,mfrac,mroot,msubsup,munderover')].filter(e=>e.children.length!==(['msubsup','munderover'].includes(e.localName)?3:2)).map(e=>({tag:e.localName,children:e.children.length,html:e.outerHTML}));
  const hidden=[...root.querySelectorAll('math')].filter(e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display==='none'||s.visibility==='hidden'||r.width<=0||r.height<=0;}).length;
  return{math:document.querySelectorAll('math').length,newMath:root.querySelectorAll('math').length,tables:document.querySelectorAll('table').length,newTables:root.querySelectorAll('table').length,frames:document.querySelectorAll('iframe').length,newFrames:root.querySelectorAll('iframe').length,svgRefs:document.querySelectorAll('img[src$=".svg"],object[data$=".svg"],embed[src$=".svg"]').length,newSVG:root.querySelectorAll('img[src$=".svg"]').length,uniqueIds:allIds.length===new Set(allIds).size,labels:newLabels,missingLabels:labels.filter(id=>!document.getElementById(id)),extraLabels:newLabels.filter(id=>!labels.includes(id)),refs,malformed,hidden,pendingMath:document.documentElement.classList.contains('native-math-pending'),proofs:[...root.querySelectorAll('em')].filter(e=>e.textContent.startsWith('Proof')).length};
 },labels);
 check(state.newMath===expected.math_nodes_added&&state.tables===389&&state.frames===14&&state.svgRefs===31&&state.newFrames===0&&state.newSVG===1,'scoped-counts-no-new-lab',state);
 check(state.uniqueIds&&!state.missingLabels.length&&!state.extraLabels.length,'all-source-gtl-labels-exact',state.labels);
 check(state.refs.every(x=>x.exists),'new-local-reference-closure',state.refs);
 check(!state.malformed.length&&!state.hidden&&!state.pendingMath,'all-new-MathML-visible-and-valid-fixed-arity',{malformed:state.malformed,hidden:state.hidden,pending:state.pendingMath});
 check(state.proofs===expected.proof_environments,'all-new-proof-environments',state.proofs);
 const numbering=await b.eval(ex=>{
  const root=document.getElementById('gauss-tail-section');
  return{equations:Object.entries(ex.equations).map(([id,number])=>({id,number,text:document.getElementById(id)?.closest('.reader-equation')?.querySelector('.reader-equation-number')?.textContent??''})),headings:ex.headings.map(x=>({id:x.id,number:x.number,text:document.getElementById(x.id)?.textContent??'',paragraph:document.getElementById(x.id)?.classList.contains('paragraphHead')})),theorems:ex.theorems.map(x=>({id:x.id,number:x.number,text:document.getElementById(x.id)?.querySelector('strong')?.textContent??''})),references:[...root.querySelectorAll('a[data-reference]')].map(a=>({id:a.dataset.reference,kind:a.dataset.referenceType,text:a.textContent})),caption:document.getElementById('gtl:partition').querySelector('figcaption').textContent};
 },{equations:expected.equations,headings:expected.headings,theorems:expected.theorems});
 check(numbering.equations.every(x=>x.text.includes('('+x.number+')'))&&numbering.headings.every(x=>x.paragraph||x.text.includes(x.number))&&numbering.theorems.every(x=>x.text.includes(x.number)),'PDF-aux-equation-heading-theorem-numbers',numbering);
 check(numbering.references.length===expected.references.length&&numbering.references.every((x,i)=>{const e=expected.references[i];return x.id===e.id&&x.kind===e.kind&&x.text===(e.kind==='eqref'?'('+e.number+')':e.number);})&&numbering.caption.startsWith('Figure '+expected.figure_number+'.'),'PDF-aux-reference-and-figure-numbers',numbering.references);
 check(state.newTables===expected.tables-389,'new-table-count-explicit-zero',state.newTables);
 for(const id of ['gtl:core','gtl:tail-theorem','gtl:discrete','gtl:direct-proof','gtl:partition']){await jump(id);await b.screenshot(id.replace(':','-')+'-desktop.png');}
 for(const theme of ['light','biomech']){
  await b.eval(theme=>{if(document.documentElement.dataset.theme!==theme)document.getElementById('themeToggle').click();if(theme==='biomech'&&document.documentElement.dataset.themeMotion==='live')document.getElementById('motionToggle').click();return true;},theme);
  await b.until('document.documentElement.dataset.theme==='+JSON.stringify(theme));await delay(3100);
  for(const [width,height] of [[1440,1050],[320,844]]){
   await b.viewport(width,height);await fit();
   const layout=await b.eval(()=>{
    const root=document.getElementById('gauss-tail-section'),fig=document.getElementById('gtl:partition'),img=fig.querySelector('img'),wrap=img.closest('.reader-figure-scroll'),is=getComputedStyle(img);
    const scrolls=[...root.querySelectorAll('.reader-display-math,.reader-inline-math,.reader-table-scroll,.reader-figure-scroll')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>{const prior=e.scrollLeft;e.scrollLeft=e.scrollWidth;const end=e.scrollLeft;e.scrollLeft=prior;const m=e.querySelector('math');return{className:e.className,end,tabIndex:e.tabIndex,label:e.getAttribute('aria-label'),font:m?getComputedStyle(m).fontSize:null,transform:m?getComputedStyle(m).transform:null};});
    return{width:innerWidth,client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,figure:{complete:img.complete,naturalWidth:img.naturalWidth,width:img.getBoundingClientRect().width,height:img.getBoundingClientRect().height,filter:is.filter,transform:is.transform,alt:img.alt,wrapperWidth:wrap.clientWidth,wrapperScroll:wrap.scrollWidth,tabIndex:wrap.tabIndex,label:wrap.getAttribute('aria-label'),role:wrap.getAttribute('role'),overflow:getComputedStyle(wrap).overflowX},scrolls,tables:[...root.querySelectorAll('table')].map(e=>({wrapped:!!e.closest('.reader-table-scroll'),tabIndex:e.closest('.reader-table-scroll')?.tabIndex}))};
   });
   check(layout.width===width&&layout.scroll<=layout.client+1,'new-layout-no-page-overflow-'+theme+'-'+width,layout);
   check(layout.figure.complete&&layout.figure.naturalWidth>0&&layout.figure.width>=650&&layout.figure.height>0&&layout.figure.filter==='none'&&layout.figure.transform==='none'&&layout.figure.alt&&layout.figure.tabIndex===0&&layout.figure.role==='region'&&layout.figure.label&&layout.figure.overflow==='auto','readable-source-figure-'+theme+'-'+width,layout.figure);
   check(layout.scrolls.every(x=>x.end>0&&x.tabIndex>=0&&x.label&&(!x.font||parseFloat(x.font)>=18)&&(!x.transform||x.transform==='none'))&&layout.tables.every(x=>x.wrapped&&x.tabIndex===0),'new-overflow-focusable-and-unscaled-'+theme+'-'+width,layout.scrolls);
   report.layouts.push(layout);await jump('gtl:partition');await b.screenshot('figure-'+theme+'-'+width+'.png');await jump('gtl:direct-proof');await b.screenshot('direct-proof-'+theme+'-'+width+'.png');
  }
 }
 await b.viewport(320,844);await fit();await jump('gtl:partition');
 const focus=await b.eval(()=>{const e=document.getElementById('gtl:partition').querySelector('.reader-figure-scroll');e.scrollLeft=0;e.focus();return{focused:document.activeElement===e,width:e.clientWidth,scroll:e.scrollWidth};});
 check(focus.focused&&focus.scroll>focus.width+1,'figure-genuine-mobile-horizontal-scroll',focus);
 await b.key('\uE014');await b.until('document.activeElement.classList.contains("reader-figure-scroll")&&document.activeElement.scrollLeft>0');
 check(true,'figure-native-ArrowRight-scroll');await b.key('\uE004');
 check(await b.evaluate('document.activeElement.tagName==="A"&&document.activeElement.getAttribute("href").endsWith("figures/gauss-tail-partition.tex")'),'figure-Tab-to-original-TeX-link');
 await b.eval(()=>{document.querySelector('#gauss-tail-section nav a[href="#gtl:details"]').focus();return true;});await b.key('\uE007');await b.until('decodeURIComponent(location.hash)==="#gtl:details"');check(true,'proof-reference-native-Enter-navigation');
 const linkState=await b.eval(names=>{
  const root=document.getElementById('gauss-tail-section');return{sources:names.map(n=>({name:n,present:!![...root.querySelectorAll('a[href]')].find(a=>a.getAttribute('href').endsWith('sources/'+n))})),figure:['svg','tex','pdf'].map(ext=>({ext,present:ext==='svg'?!!root.querySelector('img[src$="figures/gauss-tail-partition.svg"]'):!!root.querySelector('a[href$="figures/gauss-tail-partition.'+ext+'"]')})),pdf:!!root.querySelector('a[href$="book.pdf"]')};
 },sourceNames);
 check(linkState.sources.every(x=>x.present)&&linkState.figure.every(x=>x.present)&&linkState.pdf,'actual-new-source-figure-and-book-PDF-links',linkState);
 report.downloads=[];
 for(const n of sourceNames)report.downloads.push(await asset(base+'/book/sources/'+n,expected.source_sha256['book/chapters/'+n]));
 for(const ext of ['svg','tex','pdf'])report.downloads.push(await asset(base+'/book/figures/gauss-tail-partition.'+ext,expected.source_sha256['book/figures/gauss-tail-partition.'+ext]));
 report.downloads.push(await asset(base+'/book.pdf',pdf.pdf_sha256));
 report.downloads.push(await asset(base+'/book/main.html',expected.new_HTML_sha256));
 await idle('final-full-idle',controls.parentURL());
 const pageErrors=controls.pageErrors(),fetchErrors=controls.fetchErrors(),httpErrors=controls.httpErrors();
 // Exact inherited predicate from prior native QA; every error is retained in evidence.
 const inherited=pageErrors.filter(x=>JSON.stringify(x).includes('Incorrect number of children for <munder/>'));
 const unexpected=pageErrors.filter(x=>!inherited.includes(x));
 check(unexpected.length===0,'no-new-page-errors',unexpected);report.inheritedMathMLWarnings=inherited;
 check(fetchErrors.length===0,'no-browser-fetch-errors',fetchErrors);
 check(timing.filter(x=>x.event==='network.fetchError').length===0,'global-WS-log-has-no-fetch-errors',timing.filter(x=>x.event==='network.fetchError'));
 check(httpErrors.length===0,'no-HTTP-error-responses',httpErrors);
 check(pendingRequests.size===0&&!idleWaits.some(x=>x.timeout)&&timing.filter(x=>x.event==='harness.parentNavigate').every(x=>x.pending===0),'strict-global-idle-and-departures',{pending:pendingRequests.size,idleWaits:idleWaits.length});
 check(controls.inputsUnchanged(),'all-source-and-record-inputs-unchanged');
 report.passed=true;
 assert(report.checks.length===40&&controls.requiredNames.length===40&&controls.requiredNames.every(name=>report.checks.some(x=>x.name===name&&x.passed)),'Exact inherited focused40 names');
 return report;
}
