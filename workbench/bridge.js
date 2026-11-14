/* Live laboratory -> finite contract -> kernel receipt, with stale-response rejection.
   The receipt certifies a scalar contract, not the simulation or physical theory. */
(async function(){
 'use strict';
 const W=globalThis.GRHWorkbench;if(!W)return;
 const fluid=document.getElementById('fluid-main'),cosmic=document.getElementById('cosmology-main');
 const host=fluid||cosmic;if(!host)return;
 let dataset=null,epoch=0,current=null;
 const panel=document.createElement('section');panel.className='f-panel';panel.setAttribute('aria-label','Live exact verification bridge');
 const title=document.createElement('h2');title.textContent='Live verification bridge';
 const note=document.createElement('p');note.textContent='Changing laboratory inputs invalidates the previous receipt. The exact certificate covers the finite coefficient or rank calculation, not floating-point evolution, noise calibration or a continuum claim.';
 const status=document.createElement('p');status.setAttribute('role','status');status.setAttribute('aria-live','polite');
 const detail=document.createElement('pre');detail.style.whiteSpace='pre-wrap';detail.style.overflowWrap='anywhere';
 const open=document.createElement('a');open.textContent='Inspect or export this exact witness';open.style.marginRight='20px';
 const verify=document.createElement('button');verify.textContent='Replay in local Lean';verify.className='button secondary';
 const receipt=document.createElement('pre');receipt.style.whiteSpace='pre-wrap';receipt.style.overflowWrap='anywhere';
 panel.append(title,note,status,detail,open,verify,receipt);host.appendChild(panel);
 async function refresh(){
  const mine=++epoch;current=null;receipt.textContent='No current kernel receipt.';
  try{
   let c;
   if(fluid){const angles=[0,1,2,3].map(i=>Number(document.getElementById('fluidTheta'+i).value));const r=globalThis.FluidMath.circuit(angles).r;c=W.certificate('heat',{r:W.binary64(r)});}
   else{
    if(!dataset||document.documentElement.dataset.cosmologyReady!=='true'){status.textContent='Waiting for the synthetic laboratory fixture.';return;}
    const result=globalThis.CCCMath.evaluate(dataset,{center:Number(document.getElementById('injectionCenter').value),width:Number(document.getElementById('injectionWidth').value),snr:Number(document.getElementById('injectionSNR').value)});
    c=W.certificate('rank',{draws:dataset.calibration_maxima_sorted.length,exceedances:result.exceedances});
   }
   const hash=await W.digest(c);if(mine!==epoch)return;
   current={certificate:c,hash};status.textContent='Exact arithmetic accepted; Lean replay is separate.';detail.textContent=JSON.stringify({inputs:c.inputs,claim:c.claim,scope:c.scope,sha256:hash},null,2);
   open.href=new URL('workbench/index.html',location.href).href+'#certificate='+encodeURIComponent(W.canonical(c));
  }catch(e){if(mine===epoch){status.textContent='No valid certificate: '+e.message;detail.textContent='';open.removeAttribute('href');}}
 }
 verify.addEventListener('click',async()=>{
  const c=current,mine=epoch;if(!c)return;
  if(!['127.0.0.1','localhost'].includes(location.hostname)){receipt.textContent='Static hosting cannot run Lean. Use the loopback workbench server for kernel replay.';return;}
  receipt.textContent='Checking the current finite predicate...';
  try{
   const response=await fetch('/api/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:W.canonical(c.certificate)});const r=await response.json();
   if(mine!==epoch||!current||current.hash!==c.hash)return;
   if(!response.ok||r.certificate_sha256!==c.hash)throw new Error(r.error||'Receipt does not match current inputs');
   receipt.textContent=JSON.stringify(r,null,2);
  }catch(e){if(mine===epoch)receipt.textContent='No kernel verification: '+e.message;}
 });
 document.addEventListener('input',()=>{epoch++;current=null;receipt.textContent='Inputs changed; prior receipt invalid.';requestAnimationFrame(refresh);});
 document.addEventListener('click',e=>{if(!panel.contains(e.target)){epoch++;current=null;receipt.textContent='Laboratory state changed; prior receipt invalid.';requestAnimationFrame(refresh);}});
 if(cosmic){
  try{const r=await fetch('data/cosmology-synthetic.json');if(!r.ok)throw new Error('Fixture fetch failed');dataset=await r.json();globalThis.CCCMath.validateDataset(dataset);}catch(e){status.textContent=e.message;return;}
  const observer=new MutationObserver(()=>{if(document.documentElement.dataset.cosmologyReady==='true'){refresh();observer.disconnect();}});observer.observe(document.documentElement,{attributes:true,attributeFilter:['data-cosmology-ready']});
 }
 refresh();
})();
