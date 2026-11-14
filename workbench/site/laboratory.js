/* Same-origin opt-in wrapper. Original published laboratory files stay unchanged. */
'use strict';
const choice=new URLSearchParams(location.search).get('lab');
const name=choice==='cosmology'?'cosmology':'fluids',frame=document.getElementById('lab'),status=document.getElementById('state');
frame.addEventListener('load',()=>{
 try{
  const doc=frame.contentDocument;
  if(doc.querySelector('section[aria-label="Live exact verification bridge"]')){status.textContent='Live finite-contract adapter attached.';return;}
  function load(file,next){const s=doc.createElement('script');s.src=new URL(file,location.href).href;s.onload=next;s.onerror=()=>{status.textContent='Adapter failed to load; no proof is claimed.';};doc.body.appendChild(s);}
  load('core.js',()=>load('bridge.js',()=>{status.textContent='Live finite-contract adapter attached. Kernel replay requires the local server.';}));
 }catch(e){status.textContent='Same-origin adapter unavailable: '+e.message;}
});
frame.src='../'+name+'.html';
