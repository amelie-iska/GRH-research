import{Browser}from'/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';
import{writeFileSync}from'node:fs';
const out=process.env.UI_QA_OUTPUT;if(!out)throw Error('Output required');
const b=await new Browser().connect(),checks=[];const ok=(v,n,d)=>{checks.push({name:n,passed:!!v,detail:d});if(!v)throw Error(n+' '+JSON.stringify(d));};
const key=async value=>b.send('input.performActions',{context:b.context,actions:[{type:'key',id:'keyboard',actions:[{type:'keyDown',value},{type:'keyUp',value}]}]});
const jump=async id=>{await b.evaluate('(()=>{document.getElementById('+JSON.stringify(id)+').scrollIntoView({block:"start"});return true})()');let last=null,stable=0;for(let i=0;i<80;i++){const v=await b.evaluate('({y:scrollY,top:document.getElementById('+JSON.stringify(id)+').getBoundingClientRect().top})');stable=last!==null&&Math.abs(v.y-last)<.5?stable+1:0;last=v.y;if(stable>=3&&v.top>=-1&&v.top<160)return;await new Promise(r=>setTimeout(r,80));}throw Error('Target scroll failed to settle '+id);};
try{
 await b.viewport(1440,1000);await b.navigate('http://127.0.0.1:8878/quadratic-pivot.html');await b.until('document.body.dataset.ready==="true"');
 const initial=await b.evaluate('({g:Number(document.getElementById("globalPlot").dataset.globalPower),s:Number(document.getElementById("globalPlot").dataset.sixthFreePower),face:Number(document.getElementById("refinedPower").textContent),w:Number(document.getElementById("obstructionPlot").dataset.currentPower)})');
 ok(initial.g===9/8&&Math.abs(initial.s-13/12)<1e-12&&initial.face===1&&Math.abs(initial.w-13/12)<1e-12,'critical-four-distinct-comparisons',initial);
 await jump('global-title');await b.screenshot(out+'/global-desktop.png');
 for(const name of['mixed','pure']){await b.evaluate('document.querySelector("[data-witness='+name+']").click()');const v=await b.evaluate('Number(document.getElementById("obstructionPlot").dataset.currentPower)');ok(Math.abs(v-13/12)<1e-12,'current-sixth-free-'+name,v);}
 await b.evaluate('document.getElementById("thetaValue").focus()');await key('\uE014');ok(await b.evaluate('document.getElementById("thetaValue").value==="751"'),'real-range-arrow');
 await key('\uE011');ok(await b.evaluate('document.getElementById("thetaValue").value==="0"&&Number(document.getElementById("globalPlot").dataset.globalPower)===1'),'real-range-home');
 await key('\uE010');ok(await b.evaluate('document.getElementById("thetaValue").value==="1000"&&Math.abs(Number(document.getElementById("globalPlot").dataset.globalPower)-7/6)<1e-12'),'real-range-end');
 await b.evaluate('(()=>{const e=document.getElementById("thetaValue");e.value=750;e.dispatchEvent(new Event("input"));return true})()');
 for(const[width,height]of[[320,844],[390,844],[1440,1000]]){
  await b.viewport(width,height);await b.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>r(true))))');
  const g=await b.evaluate('({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,ready:document.body.dataset.ready,labels:[...document.querySelectorAll("#globalPlot text")].map(e=>e.textContent)})');
  ok(g.scroll<=g.client+1&&g.labels.length>5&&g.ready==="true",'layout-'+width,g);await jump('global-title');await b.screenshot(out+'/global-'+width+'.png');await jump('obstruction-title');await b.screenshot(out+'/triangle-'+width+'.png');
 }
 await b.viewport(390,844);await b.evaluate('document.getElementById("themeToggle").click()');await b.evaluate('(()=>{if(document.documentElement.dataset.themeMotion==="live")document.getElementById("motionToggle").click();return true})()');await b.until('document.documentElement.dataset.theme==="biomech"&&getComputedStyle(document.body).backgroundColor==="rgb(7, 13, 20)"&&getComputedStyle(document.body).color==="rgb(210, 225, 230)"');await jump('global-title');await b.screenshot(out+'/global-mobile-night.png');
 ok(await b.evaluate('getComputedStyle(document.getElementById("globalPlot")).backgroundColor==="rgb(10, 23, 33)"'),'night-plot-palette');
 await b.evaluate('document.getElementById("themeToggle").click()');
 const errs=b.pageErrors(),fetch=b.events.filter(e=>e.method==='network.fetchError');ok(errs.length===0&&fetch.length===0,'zero-page-and-fetch-errors',{errs,fetch});
 writeFileSync(out+'/browser.json',JSON.stringify({passed:true,checks,scope:'Focused current physical-sieve inspector: live keyboard/range/witnesses/mobile/night and source-matched screenshot candidate; no browser training.'},null,2)+'\n');console.log(JSON.stringify({passed:true,checks:checks.length}));
}finally{await b.close();}
