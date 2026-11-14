/* Display-only replay of hash-bound saved auxiliary matrices. No training/SVD/Perron evaluation. */
export const DATA_SHA = 'e540ac344bbf3d4d07d1ac9fcb8c5cd336a6195c7130a602567242c33bc73171';
export const STAGES = Object.freeze([{key:'raw',label:'K',norm:'K_norm'},{key:'au',label:'A_U ◦ K',norm:'AU_K_norm'},{key:'profile',label:'W ◦ A_U ◦ K',norm:'W_AU_K_norm'}]);
export function complexPhase(phase6){const k=((phase6%6)+6)%6;return [[1,0],[.5,Math.sqrt(3)/2],[-.5,Math.sqrt(3)/2],[-1,0],[-.5,-Math.sqrt(3)/2],[.5,-Math.sqrt(3)/2]][k];}
export function multiply(x,y){return [x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];}
export function entryValue(e,stage){if(!e.support)return [0,0];const k=complexPhase(e.phase6);if(stage==='raw')return k;const a=k.map(x=>x*e.A_U);return stage==='au'?a:multiply(a,e.W.map(Number));}
export function omegaText(p){const [a,b]=p;if(!b)return String(a);let tail=b===1?'ω':b===-1?'−ω':`${b}ω`;if(!a)return tail;return `${a}${b>0?'+':''}${tail}`.replace(/-/g,'−');}
export function generatorText(p){return omegaText(p);}
export function fractionText(p){return p[1]===1?String(p[0]):`${p[0]}/${p[1]}`;}
export function zeroReason(e,stage){if(!e.support)return 'source-masked zero';if(stage!=='raw'&&e.A_U===0)return 'coefficient zero';if(stage==='profile'&&e.W.every(x=>Number(x)===0))return 'profile zero';return null;}
export function magnitude(z){return Math.hypot(...z);}
export function complexText(z,digits=7){const f=x=>Math.abs(x)<1e-16?'0':Number(x.toPrecision(digits)).toString();return `${f(z[0])}${z[1]<0?'−':'+'}${f(Math.abs(z[1]))}i`;}
export function getCaseEntry(c,i,j){return c.entries[i*c.shape[1]+j];}
export function phaseColor(z,dark=false){return `hsl(${(190+Math.atan2(z[1],z[0])*180/Math.PI+360)%360} 53% ${dark?65:43}%)`;}
const NS='http://www.w3.org/2000/svg';let data,state={caseIndex:0,stage:'profile',i:0,j:0};
function el(id){return document.getElementById(id);}function text(id,value){el(id).textContent=value;}
function fmt(v,n=8){return Number(Number(v).toPrecision(n)).toString();}
function current(){return data.cases[state.caseIndex];}function selected(){return getCaseEntry(current(),state.i,state.j);}
function stageMax(c,stage){return Math.max(1e-12,...c.entries.map(e=>magnitude(entryValue(e,stage))));}
function escaped(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
function matrix(focus=false){
 const c=current(),max=stageMax(c,state.stage),dark=document.documentElement.dataset.theme==='biomech';const cw=18,x0=68,y0=42;
 let s='<title id="cbMatrixTitle">Every saved matrix position</title><desc id="cbMatrixDesc">Fourteen d ideals by twenty-nine a ideals. Arrow keys select adjacent entries; native row and column selectors are equivalent. Dashed frontier is the auxiliary product cutoff.</desc>';
 s+=`<text class="cb-axis" x="68" y="12">a index → / distinct ideal columns</text><text class="cb-axis" x="8" y="31">d / norm</text>`;
 for(let j=0;j<c.shape[1];j++)s+=`<text class="cb-axis ${j===state.j?'selected':''}" text-anchor="middle" x="${x0+j*cw+8}" y="31">${j}</text>`;
 for(let i=0;i<c.shape[0];i++){
  s+=`<text class="cb-axis ${i===state.i?'selected':''}" text-anchor="end" x="61" y="${y0+i*cw+12}">${i} / ${data.row_ideals[i].norm}</text>`;
  for(let j=0;j<c.shape[1];j++){
   const e=getCaseEntry(c,i,j),z=entryValue(e,state.stage),m=magnitude(z),why=zeroReason(e,state.stage),x=x0+j*cw,y=y0+i*cw,sel=i===state.i&&j===state.j;
   const fill=why?'var(--cb-mask)':phaseColor(z,dark),opacity=why?'.35':String(.25+.75*Math.sqrt(m/max));
   const label=`d ${i}, norm ${data.row_ideals[i].norm}; a ${j}, norm ${data.column_ideals[j].norm}; ${why||complexText(z)}${sel?'; selected':''}`;
   s+=`<g class="cb-cell" role="gridcell" data-cell="${i*c.shape[1]+j}" data-support="${e.support}" data-phase6="${e.phase6===null?'masked':e.phase6}" data-value-real="${z[0]}" data-value-imag="${z[1]}" data-zero-reason="${why||'nonzero'}" aria-rowindex="${i+1}" aria-colindex="${j+1}" aria-selected="${sel}" aria-label="${escaped(label)}" tabindex="${sel?0:-1}"><title>${escaped(label)}</title><rect x="${x}" y="${y}" width="16" height="16" rx="1" fill="${fill}" fill-opacity="${opacity}"/>`;
   if(!e.support){if(e.mask_causes.includes('product_cutoff'))s+=`<path d="M${x+4} ${y+12}l8 -8" stroke="var(--cb-grid)" stroke-width=".8"/>`;if(e.mask_causes.includes('shared_ideal_prime'))s+=`<circle cx="${x+8}" cy="${y+8}" r="2" fill="var(--muted)"/>`;}
   else if(why)s+=`<circle cx="${x+8}" cy="${y+8}" r="${why==='profile zero'?3:1.8}" fill="${why==='profile zero'?'none':'var(--muted)'}" stroke="var(--muted)" stroke-width=".8"/>`;
   s+='</g>';
  }
 }
 let path='';for(let i=0;i<c.shape[0];i++){const n=data.column_ideals.filter(a=>a.norm*data.row_ideals[i].norm<=c.X).length;const x=x0+n*cw-1,y=y0+i*cw;path+=`${i?'L':'M'}${x} ${y}L${x} ${y+cw}`;}
 s+=`<path class="cb-frontier" d="${path}"/><text class="cb-axis" x="68" y="${y0+14*cw+23}">phase color + relative entry magnitude / exact labels in selection</text>`;
 el('cbMatrix').innerHTML=s;text('cbScale',`Cell opacity is relative to this stage’s maximum entry magnitude ${fmt(max,6)}. It is not an operator-norm scale.`);
 if(focus){const g=el('cbMatrix').querySelector(`[data-cell="${state.i*29+state.j}"]`);g.focus({preventScroll:true});const host=el('cbMatrixHost'),b=g.getBoundingClientRect(),h=host.getBoundingClientRect();if(b.left<h.left+12)host.scrollLeft-=h.left+12-b.left;else if(b.right>h.right-12)host.scrollLeft+=b.right-h.right+12;}
}
function idealHTML(a,label){const fs=a.factors.length?a.factors.map(f=>`<span class="cb-tag ${f.kind}">(${escaped(generatorText(f.generator))}) · N=${f.norm}<br>${f.kind==='inert'?`inert p=${f.rational_prime}, norm p²`:`split p=${f.rational_prime}`} · exponent ${f.exponent}</span>`).join(''):'<span class="cb-tag">Unit ideal / no prime factors</span>';return `<div class="cb-ideal"><span class="cb-label">${label} ${a.id} / N=${a.norm}</span><strong>${escaped(generatorText(a.generator))}</strong><p>source canonical generator<br>good and ideal-squarefree</p>${fs}</div>`;}
function plane(e){const z=entryValue(e,state.stage),max=stageMax(current(),state.stage),scale=74/max,x=110+z[0]*scale,y=110-z[1]*scale,dark=document.documentElement.dataset.theme==='biomech';let s='<title>Selected complex entry, numerical display projection</title><path class="axes" d="M22 110H204M110 22V204"/><circle class="axes" cx="110" cy="110" r="74" fill="none" stroke-dasharray="2 3"/>';
 s+=`<text x="194" y="123">Re</text><text x="117" y="25">Im</text><text x="149" y="201">scale ${escaped(fmt(max,4))}</text>`;
 if(e.support&&state.stage==='au'&&e.A_T){const a=multiply(complexPhase(e.phase6),e.A_T.map(Number));s+=`<circle cx="${110+a[0]*scale}" cy="${110-a[1]*scale}" r="6" fill="none" stroke="var(--orange)" stroke-width="1.4"><title>Saved finite-Perron entry; it may visually coincide with the integer coefficient.</title></circle>`;}
 s+=`<path d="M110 110L${x} ${y}" stroke="${phaseColor(z,dark)}" stroke-width="2"/><circle cx="${x}" cy="${y}" r="4" fill="${phaseColor(z,dark)}"/>`;el('cbPlane').innerHTML=s;
}
function detail(){
 const c=current(),e=selected(),row=data.row_ideals[e.i],col=data.column_ideals[e.j],z=entryValue(e,state.stage),why=zeroReason(e,state.stage);
 text('cbEntryTitle',`Entry d${e.i} / a${e.j}`);text('cbEntryValue',`${STAGES.find(s=>s.key===state.stage).label} = ${why?`0 · ${why}`:state.stage==='raw'?omegaText(e.K_omega):state.stage==='au'?omegaText(e.AU_K_omega):complexText(z,10)}`);
 el('cbFactors').innerHTML=idealHTML(row,'ROW d')+idealHTML(col,'COLUMN a');
 let reason=e.support?`Both source predicates pass: no shared prime IDEAL and ${e.product_norm} ≤ X=${c.X}.`:`Source-masked entry: ${e.mask_causes.map(x=>x==='shared_ideal_prime'?`shared prime ideal ${e.common_factors.map(g=>'('+generatorText(g)+')').join(', ')}`:`Nd·Na=${e.product_norm} exceeds X=${c.X}`).join('; ')}. AU, A_T and W were not evaluated for this entry in the saved controls; all pipeline matrices retain zero.`;
 text('cbMaskNote',reason);el('cbMaskNote').dataset.blocked=String(!e.support);
 const fields=[['Nd · Na',`${row.norm} · ${col.norm} = ${e.product_norm}`],['profile x',fractionText(e.x_fraction)],['raw phase',e.support?`phase6=${e.phase6}; ${omegaText(e.K_omega)} ≠ 0`:'not evaluated / support=0'],['integer A_U',e.support?String(e.A_U):'not evaluated'],['saved A_T',e.support?`${fmt(Number(e.A_T[0]),12)} ${Number(e.A_T[1])<0?'−':'+'} ${fmt(Math.abs(Number(e.A_T[1])),6)}i`:'not evaluated'],['|A_T − A_U|',e.support?fmt(Number(e.A_T_error),8):'not evaluated'],['W amplitude',e.support?fractionText(e.profile_amplitude_fraction):'not evaluated'],['W phase x/7',e.support&&e.profile_angle_fraction?`${fractionText(e.profile_angle_fraction)} radians`:'zero / not evaluated']];
 el('cbValues').innerHTML=fields.map(([a,b])=>`<dt>${escaped(a)}</dt><dd>${escaped(b)}</dd>`).join('');
 text('cbSavedEntry',e.support?`SOURCE SAVED NUMERICAL COORDINATES (55 digits)\nA_T real = ${e.A_T[0]}\nA_T imaginary = ${e.A_T[1]}\n|A_T-A_U| = ${e.A_T_error}\nentry comparison expression = ${e.A_T_control_bound}\nW real = ${e.W[0]}\nW imaginary = ${e.W[1]}\n\nInteger A_U = ${e.A_U}; exact cubic K = ${omegaText(e.K_omega)}.\nThe coordinates are numerical consistency outputs, not interval enclosures.`:'The source stores only i, j and mask=0 here. No unsaved coefficient evaluation is presented as source data.');
 plane(e);text('cbSelectionLive',`D${c.D}: selected row d${e.i}, column a${e.j}; ${why||'nonzero selected-stage entry'}.`);
}
function render(focus=false){const c=current();el('cbRow').value=String(state.i);el('cbCol').value=String(state.j);el('cbCase').value=String(c.D);
 text('cbCounts',`${c.shape[0]} × ${c.shape[1]} · ${c.supported} supported · ${c.masked} masked · ${c.inert_factor_entries} supported inert-factor positions`);
 for(const st of STAGES){const b=document.querySelector(`[data-stage="${st.key}"]`);b.setAttribute('aria-pressed',String(st.key===state.stage));const out=b.querySelector('output');out.textContent=`‖·‖₂ ≈ ${fmt(Number(c.norms[st.norm]),9)}`;out.dataset.savedNorm=c.norms[st.norm];out.title=c.norms[st.norm];}
 text('cbParameters',`D=${c.D}; U=${c.U}; X=2D=${c.X}; T=8X=${c.T}; c=1/log(4X); U#=${2*c.U+1}/2. All source support predicates remain.`);
 text('cbPerronNorms',`Saved numerical ‖A_T ◦ K‖₂ = ${c.norms.AU_T_K_norm}\nSaved numerical ‖(A_U−A_T) ◦ K‖₂ = ${c.norms.residual_norm}`);
 text('cbComparison',Object.entries(c.comparisons).map(([k,v])=>`${k}\n  saved numerical norm ${v.norm}\n  saved comparison expression ${v.bound}${v.J_bound?'\n  J(W) comparison '+v.J_bound:''}`).join('\n\n'));
 matrix(focus);detail();
}
function choose(i,j,focus=false){state.i=Math.max(0,Math.min(13,i));state.j=Math.max(0,Math.min(28,j));render(focus);}
function preset(which){let e;
 if(which==='conjugate')e=current().entries.find(e=>e.support&&data.row_ideals[e.i].norm===7&&data.column_ideals[e.j].norm===7);
 if(which==='collision')e=current().entries.find(e=>!e.support&&e.mask_causes.includes('shared_ideal_prime')&&data.row_ideals[e.i].norm===7&&data.column_ideals[e.j].norm===7);
 if(which==='inert')e=current().entries.find(e=>e.support&&Number(e.W[0])!==0&&e.A_U!==0&&[...data.row_ideals[e.i].factors,...data.column_ideals[e.j].factors].some(f=>f.kind==='inert'));
 if(!e)return;state.stage=which==='inert'?'profile':'raw';choose(e.i,e.j);
}
async function boot(){
 const req=new Request(new URL('data/coherent-band-schur-v1.json',document.baseURI),{cache:'no-store'});const res=await fetch(req);if(!res.ok)throw new Error(`Data HTTP ${res.status}`);const bytes=await res.arrayBuffer();const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),x=>x.toString(16).padStart(2,'0')).join('');if(digest!==DATA_SHA)throw new Error('Display payload SHA256 mismatch');
 data=JSON.parse(new TextDecoder().decode(bytes));if(data.schema!=='coherent-band-schur-display-v1'||data.totals.states!==1218)throw new Error('Unexpected display schema');
 el('cbCase').innerHTML=data.cases.map(c=>`<option value="${c.D}">D${c.D} / U${c.U} / 14 × 29</option>`).join('');
 for(const [id,items,kind] of [['cbRow',data.row_ideals,'d'],['cbCol',data.column_ideals,'a']])el(id).innerHTML=items.map(a=>`<option value="${a.id}">${kind}${a.id} · N${a.norm} · ${escaped(generatorText(a.generator))}</option>`).join('');
 const initial=current().entries.find(e=>e.support&&e.A_U!==0&&Number(e.W[0])!==0);state.i=initial.i;state.j=initial.j;
 el('cbCase').addEventListener('change',()=>{state.caseIndex=data.cases.findIndex(c=>c.D===Number(el('cbCase').value));render();});el('cbRow').addEventListener('change',()=>choose(Number(el('cbRow').value),state.j));el('cbCol').addEventListener('change',()=>choose(state.i,Number(el('cbCol').value)));
 for(const b of document.querySelectorAll('[data-stage]'))b.addEventListener('click',()=>{state.stage=b.dataset.stage;render();});for(const b of document.querySelectorAll('[data-preset]'))b.addEventListener('click',()=>preset(b.dataset.preset));
 el('cbZoom').addEventListener('input',()=>{el('cbMatrixHost').style.setProperty('--zoom',el('cbZoom').value);text('cbZoomValue',`${Number(el('cbZoom').value).toFixed(2)}×`);});
 el('cbMatrix').addEventListener('click',e=>{const g=e.target.closest('[data-cell]');if(g){const id=Number(g.dataset.cell);choose(Math.floor(id/29),id%29,true);}});
 el('cbMatrix').addEventListener('keydown',e=>{let i=state.i,j=state.j;switch(e.key){case'ArrowLeft':j--;break;case'ArrowRight':j++;break;case'ArrowUp':i--;break;case'ArrowDown':i++;break;case'Home':j=0;if(e.ctrlKey)i=0;break;case'End':j=28;if(e.ctrlKey)i=13;break;default:return;}e.preventDefault();choose(i,j,true);});
 const watch=new MutationObserver(()=>{if(data){matrix(false);plane(selected());}});watch.observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
 text('cbSourceHash',data.source.sha256);text('cbPayloadHash',digest);text('cbStatus',`SHA256 verified · 3 cases / 1218 positions · source 1511 numerical consistency assertions at 55 digits`);el('cbStatus').dataset.verified='true';el('cbBody').hidden=false;el('coherentBandLab').dataset.ready='true';render();
 window.coherentBandLab=Object.freeze({getState:()=>{const e=selected(),c=current();return {D:c.D,stage:state.stage,i:state.i,j:state.j,support:e.support,phase6:e.phase6,A_U:e.A_U,value:entryValue(e,state.stage),A_T:e.A_T?[...e.A_T]:null,W:e.W?[...e.W]:null,sourceSHA:data.source.sha256,payloadSHA:DATA_SHA,auxiliary:true};},inspectCase:(D,stage='raw')=>{const c=data.cases.find(c=>c.D===Number(D));if(!c||!STAGES.some(s=>s.key===stage))throw new Error('Unknown display case/stage');return {D:c.D,norms:{...c.norms},entries:c.entries.map(e=>({...e,value:entryValue(e,stage)}))};},getSummary:()=>({...data.totals})});
}
if(typeof document!=='undefined')boot().catch(error=>{const p=document.getElementById('cbStatus');p.textContent=`Data verification failed: ${error.message}`;p.setAttribute('role','alert');p.dataset.error='true';console.error(error);});
