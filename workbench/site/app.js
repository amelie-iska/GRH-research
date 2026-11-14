/* Same-payload receipts only. Static hosting never masquerades as a proof server. */
'use strict';
const defaults={heat:{r:'1/4'},gain:{matrix:[['1/4','3/2'],['3/32','1/4']],weights:['4','1'],rate:'5/8'},rank:{draws:4095,exceedances:0},risk:{tests:288,per_test:'1/10000',drift:'1/100',alpha:'1/20'},mutation:{matrix:[[0,1],[-1,0]],seed:['2','5'],vertex:0}};
const $=id=>document.getElementById(id),W=globalThis.GRHWorkbench;
let generation=0,current=null;
function invalidate(){generation++;current=null;$('receipt').textContent='No current kernel receipt. Inputs changed.';$('digest').textContent='';$('claim').textContent='';$('scope').textContent='';}
async function evaluate(){
 const epoch=++generation;current=null;$('receipt').textContent='No current kernel receipt.';
 try{
  const c=W.certificate($('kind').value,JSON.parse($('inputs').value));const hash=await W.digest(c);
  if(epoch!==generation)return null;
  current={certificate:c,hash,epoch};$('status').textContent='Exact arithmetic accepted. Not yet kernel checked.';$('status').className='good';$('scope').textContent=c.scope;$('claim').textContent=JSON.stringify(c.claim,null,2);$('digest').textContent='Certificate SHA-256: '+hash;return current;
 }catch(e){if(epoch!==generation)return null;$('status').textContent=e.message;$('status').className='bad';$('claim').textContent='';$('digest').textContent='';return null;}
}
function download(name,content,type){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function choose(){invalidate();$('inputs').value=JSON.stringify(defaults[$('kind').value],null,2);evaluate();}
$('kind').addEventListener('change',choose);$('inputs').addEventListener('input',()=>{invalidate();$('status').textContent='Inputs changed; recheck before using a witness.';});$('check').addEventListener('click',evaluate);
$('export').addEventListener('click',async()=>{const c=current||await evaluate();if(c)download('grh-'+c.certificate.kind+'.json',JSON.stringify(c.certificate,null,2),'application/json');});
async function service(endpoint){
 const c=current||await evaluate();if(!c)return;const epoch=generation;
 $('receipt').textContent='Local service request in progress; no proof is claimed yet.';
 try{
  if(!['localhost','127.0.0.1'].includes(location.hostname))throw new Error('Kernel service is unavailable on static hosting. Run the loopback server locally.');
  const response=await fetch('/api/'+endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:W.canonical(c.certificate)});const data=await response.json();
  if(epoch!==generation||!current||current.hash!==c.hash)return;
  if(!response.ok)throw new Error(data.error||'Local service failed');
  if(endpoint==='source'){download('Certificate.lean',data.source,'text/plain');$('receipt').textContent='Lean source exported. Export is not proof execution.';return;}
  if(data.certificate_sha256!==c.hash)throw new Error('Receipt digest does not match the current inputs');
  $('receipt').textContent=JSON.stringify(data,null,2);$('status').textContent=data.status==='kernel_checked'?'Lean kernel accepted this finite predicate.':'Kernel check did not succeed: '+data.status;
 }catch(e){if(epoch===generation){$('receipt').textContent=e.message;$('status').textContent='No kernel verification receipt.';}}
}
$('verify').addEventListener('click',()=>service('verify'));$('source').addEventListener('click',()=>service('source'));choose();
