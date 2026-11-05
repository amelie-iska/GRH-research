// Saved-state display only. No optimizer, training update or scientific source mutation.
export const PAYLOAD_SHA256='0a33dfeae6a854c80cc7e6c21a4d1bd2bb66338223674432f396a253d94508ff';
export const PHASES=[[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]];
export function complexProjection([a,b]){return[a+b/2,Math.sqrt(3)*b/2];}
export function complexNorm([a,b]){return Math.sqrt(Math.max(0,a*a+a*b+b*b));}
export function featureValue(block,coordinates,phase){
 if(phase.length!==block.q.length)throw new RangeError('Phase dimension mismatch');
 let a=0,b=0;
 for(const o of block.orientations){const exponent=(( -o.signs.reduce((n,s,i)=>n+s*phase[i],0))%6+6)%6,[c,d]=PHASES[exponent],[x,y]=coordinates[o.pair];a+=x*c-y*d;b+=x*d+y*c+y*d;}
 return[a,b];
}
export async function sha256(bytes){return [...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(n=>n.toString(16).padStart(2,'0')).join('');}
export async function unpackDisplay(data){
 if(data.schema!=='arithmetic-learning-display-v1'||data.cases.length!==4||data.pairs.length!==210)throw Error('Unexpected display schema');
 for(const c of data.cases)for(const [method,t]of Object.entries(c.trajectories)){
  const bytes=Uint8Array.from(atob(t.states_gzip_base64),x=>x.charCodeAt(0));
  const decoded=await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
  if(await sha256(decoded)!==t.states_sha256)throw Error('Saved trajectory hash mismatch');
  t.states=JSON.parse(new TextDecoder().decode(decoded));
  if(t.states.length!==t.state_count||t.states.length!==t.updates+1||t.states.some((s,i)=>s.step!==i||s.coordinates.length!==210||s.residuals.length!==210))throw Error('Incomplete saved trajectory');
  if(method==='ordinary'&&(!t.budget_limited||t.requested_tau_certified))throw Error('Ordinary scope mismatch');
 }
 return data;
}
const NS='http://www.w3.org/2000/svg';
const svgEl=(name,attrs={},text)=>{const e=document.createElementNS(NS,name);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=text;return e;};
const line=(p,color,width=2,dash='')=>svgEl('polyline',{points:p.map(v=>v.join(',')).join(' '),fill:'none',stroke:color,'stroke-width':width,'stroke-dasharray':dash,'stroke-linejoin':'round'});
const fmt=x=>Number(x).toExponential(4).replace('e+','e');
const basis=v=>`(${v[0]}, ${v[1]})`;
const displayComplex=v=>{const[x,y]=complexProjection(v);return`${fmt(x)} ${y<0?'−':'+'} ${fmt(Math.abs(y))} i`;};
function init(data){
 const $=id=>document.getElementById(id);let caseData,trajectory,state,index=0,coordinate=34,phaseIndex=0,timer,frame;
 const matrixButtons=new Map(),pairIndex=new Map(data.pairs.map(p=>[`${p.m},${p.n}`,p.id]));
 const dl=(el,rows)=>el.replaceChildren(...rows.map(([k,v])=>{const div=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=k;dd.textContent=v;div.append(dt,dd);return div;}));
 const setStatus=text=>$('loadStatus').textContent=text;
 const css=n=>getComputedStyle(document.documentElement).getPropertyValue('--al-'+n).trim();
 const sourceBase='https://github.com/amelie-iska/GRH-research/blob/main/';
 function stop(){clearInterval(timer);timer=undefined;$('playSteps').textContent='Play saved states';$('playSteps').setAttribute('aria-pressed','false');}
 function drawLoss(){
  const svg=$('lossPlot'),w=Math.max(250,Math.round(svg.getBoundingClientRect().width)),h=w<560?310:330;svg.setAttribute('viewBox',`0 0 ${w} ${h}`);
  const left=52,right=w-14,top=25,bottom=h-40,low=-30,high=Math.max(8,4*Math.ceil(Math.max(...trajectory.states.map(s=>s.log_loss))/4));
  const X=k=>left+k/trajectory.updates*(right-left),Y=v=>bottom-(v-low)/(high-low)*(bottom-top);
  const nodes=[svgEl('title',{id:'loss-title'},'Saved full loss and squared signed-readout certificates'),svgEl('desc',{id:'loss-desc'},`${caseData.id}, ${$('methodSelect').value}, selected state ${index} of ${trajectory.updates}. Curves are saved weighted loss and squared CC/CM transfer bounds. Requested amplitude tolerance 1e-12 corresponds to squared tolerance 1e-24.`)];
  for(let e=-24;e<=high;e+=8){nodes.push(line([[left,Y(e)],[right,Y(e)]],'var(--line)',1));nodes.push(svgEl('text',{x:left-7,y:Y(e)+4,'text-anchor':'end'},`10^${e}`));}
  nodes.push(line([[left,top],[left,bottom],[right,bottom]],'var(--muted)',1));
  nodes.push(line([[left,Y(-24)],[right,Y(-24)]],css('pink'),1.5,'5 4'));
  for(const [key,color]of[['loss','violet'],['CC','teal'],['CM','rust']])nodes.push(line(trajectory.states.map(s=>[X(s.step),Y(key==='loss'?s.log_loss:s.log_bounds_squared[key])]),css(color),2.3));
  nodes.push(line([[X(index),top],[X(index),bottom]],'var(--ink)',1,'2 3'));
  for(const k of[0,Math.round(trajectory.updates/2),trajectory.updates])nodes.push(svgEl('text',{x:X(k),y:bottom+20,'text-anchor':'middle'},String(k)));
  nodes.push(svgEl('text',{x:(left+right)/2,y:h-7,'text-anchor':'middle',class:'axis-text'},'executed saved update'));
  nodes.push(svgEl('text',{x:12,y:15,class:'axis-text'},'squared values'));
  svg.replaceChildren(...nodes);svg.dataset.step=String(index);svg.dataset.method=$('methodSelect').value;
 }
 function drawError(){
  const svg=$('errorPlot'),w=Math.max(250,Math.round(svg.getBoundingClientRect().width)),h=w<560?310:330;svg.setAttribute('viewBox',`0 0 ${w} ${h}`);
  const left=40,right=w-16,top=27,bottom=h-40,cx=(left+right)/2,cy=(top+bottom)/2,[re,im]=complexProjection(state.residuals[coordinate]),span=Math.max(Math.abs(re),Math.abs(im),1e-16)*1.35,scale=Math.min(right-left,bottom-top)/2/span;
  const X=x=>cx+x*scale,Y=y=>cy-y*scale;
  const nodes=[svgEl('title',{id:'error-title'},'Complex residual of the selected saved coefficient'),svgEl('desc',{id:'error-desc'},`Coordinate ${coordinate}; real residual${re}, imaginary residual${im}. Linear scale half-span${span}. The target residual is the origin.`)];
  const defs=svgEl('defs'),clip=svgEl('clipPath',{id:'error-clip'});clip.append(svgEl('rect',{x:left,y:top,width:right-left,height:bottom-top}));defs.append(clip);nodes.push(defs);
  nodes.push(line([[left,cy],[right,cy]],'var(--line)',1));nodes.push(line([[cx,top],[cx,bottom]],'var(--line)',1));
  const path=line(trajectory.states.slice(0,index+1).map(s=>{const[x,y]=complexProjection(s.residuals[coordinate]);return[X(x),Y(y)];}),css('violet'),1.5);path.setAttribute('clip-path','url(#error-clip)');nodes.push(path);
  nodes.push(line([[cx,cy],[X(re),Y(im)]],css('teal'),2.5));nodes.push(svgEl('circle',{cx,cy,r:4,fill:'var(--al-panel)',stroke:'var(--ink)','stroke-width':1.4}));nodes.push(svgEl('circle',{cx:X(re),cy:Y(im),r:5,fill:css('rust'),stroke:'var(--paper)','stroke-width':1.5}));
  nodes.push(svgEl('text',{x:right,y:bottom+22,'text-anchor':'end',class:'axis-text'},'Re(g − Γ)'));
  nodes.push(svgEl('text',{x:left,y:16,class:'axis-text'},'Im(g − Γ)'));
  nodes.push(svgEl('text',{x:left,y:h-7,class:'axis-text'},`half-span ±${fmt(span)} · linear zoom`));
  svg.replaceChildren(...nodes);svg.dataset.coordinate=String(coordinate);svg.dataset.residualNorm=String(complexNorm(state.residuals[coordinate]));
 }
 function buildMatrix(){const nodes=[document.createElement('span')];for(let n=0;n<15;n++){const e=document.createElement('span');e.className='matrix-label';e.textContent=n;nodes.push(e);}for(let m=0;m<15;m++){const label=document.createElement('span');label.className='matrix-label';label.textContent=m;nodes.push(label);for(let n=0;n<15;n++){if(m===n){const e=document.createElement('span');e.className='matrix-diagonal';e.textContent='×';e.title='Diagonal is exact, outside learned210-vector';nodes.push(e);continue;}const id=pairIndex.get(`${m},${n}`),button=document.createElement('button');button.type='button';button.dataset.coordinate=String(id);button.setAttribute('aria-label',`Correlation ${id}, column ${m} to${n}`);button.addEventListener('click',()=>selectCoordinate(id));button.addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(event.key))return;event.preventDefault();let mm=m,nn=n;const dm=event.key==='ArrowDown'?1:event.key==='ArrowUp'?-1:0,dn=event.key==='ArrowRight'?1:event.key==='ArrowLeft'?-1:0;mm=(mm+dm+15)%15;nn=(nn+dn+15)%15;if(mm===nn){mm=(mm+dm+15)%15;nn=(nn+dn+15)%15;}const next=pairIndex.get(`${mm},${nn}`);selectCoordinate(next);matrixButtons.get(next).focus();});matrixButtons.set(id,button);nodes.push(button);}}$('correlationMatrix').replaceChildren(...nodes);}
 function drawMatrix(){const mode=$('heatmapMode').value,dark=document.documentElement.dataset.theme==='biomech',mix=(a,b,t)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*t)).join(',')})`,max=Math.max(...caseData.target.map(v=>Math.abs(complexProjection(v)[0])),1);
  for(const p of data.pairs){const b=matrixButtons.get(p.id),v=mode==='error'?complexNorm(state.residuals[p.id]):complexProjection((mode==='target'?caseData.target:state.coordinates)[p.id])[0];let color;if(mode==='error'){const t=Math.max(0,Math.min(1,(Math.log10(Math.max(v,1e-15))+15)/18));color=mix(dark?[16,68,77]:[211,232,221],dark?[204,150,62]:[153,89,33],t);}else color=v>=0?mix(dark?[20,45,55]:[229,234,223],dark?[223,162,91]:[158,77,39],Math.min(1,v/max)):mix(dark?[20,45,55]:[229,234,223],dark?[153,158,235]:[85,99,155],Math.min(1,-v/max));b.style.backgroundColor=color;b.title=`${p.id}: ${p.m}→${p.n}; μ(q)=${p.mu_q}; ${mode==='error'?'residual norm':'real value'}≈${fmt(v)}`;b.setAttribute('aria-pressed',String(p.id===coordinate));b.tabIndex=p.id===coordinate?0:-1;}
  $('matrixScale').replaceChildren();for(const text of mode==='error'?['|g−Γ| ≤10⁻¹⁵','10³ · fixed log scale']:[`−${fmt(max)}`,`+${fmt(max)} · signed real part`]){const e=document.createElement('span');e.textContent=text;$('matrixScale').append(e);}
 }
 function phaseSetup(){const block=data.pairs[coordinate].block,feature=caseData.features.find(f=>f.block===block);phaseIndex=Math.min(phaseIndex,feature.values.length-1);$('phaseSample').replaceChildren(...feature.values.map((v,i)=>new Option(`e = (${v.phase.join(', ')})`,String(i))));$('phaseSample').value=String(phaseIndex);}
 function showFeature(){const pair=data.pairs[coordinate],block=data.blocks[pair.block],sample=caseData.features.find(f=>f.block===pair.block).values[phaseIndex],value=featureValue(block,state.coordinates,sample.phase),error=featureValue(block,state.residuals,sample.phase);$('featureValues').textContent=`Block ${block.id}: ${block.orientations.length} active orientations
Finite phase-group size: ${block.phase_group_size}
Selected saved phase: (${sample.phase.join(', ')})

Exact target F basis (a,b):
${basis(sample.target)}

Saved-state F, display evaluation ≈
${displayComplex(value)}

Feature residual from exact-coordinate differences ≈
${displayComplex(error)}
|residual| ≈ ${fmt(complexNorm(error))}`;}
 function showCoordinate(){const pair=data.pairs[coordinate],block=data.blocks[pair.block],m=data.columns[pair.m],n=data.columns[pair.n],hist=caseData.histogram_summary.find(h=>h.block===block.id),audit=state.audit_exact[String(coordinate)];$('coordinateName').textContent=`COORDINATE ${coordinate} · COLUMN ${pair.m} → ${pair.n}`;
  dl($('pairMetadata'),[['Column norms Nm, Nn',`${m.norm}, ${n.norm}`],['Actual long-factor counts r_U',`${m.r_U}, ${n.r_U}`],['Common h · norm',`${JSON.stringify(block.h)} · ${block.Nh}`],['q · norm',`${JSON.stringify(block.q)} · ${block.Nq}`],['μ(q) inside signed sum',String(pair.mu_q)],['Orientation mask',String(pair.orientation_mask)],['Deleted rows for this (h,q)',`${hist.invalid_rows} / ${caseData.row_count}`],['Occupied phase tuples',String(hist.occupied_phases)]]);
  $('coordinateExact').textContent=`Exact target Γ (a,b):
${basis(caseData.target_exact[coordinate])}

${audit?'Exact saved g (a,b):\n'+basis(audit):'Saved g display projection (a,b):\n'+basis(state.coordinates[coordinate].map(fmt))}

Residual display projection (a,b):
${basis(state.residuals[coordinate].map(fmt))}
Complex residual norm ≈ ${fmt(complexNorm(state.residuals[coordinate]))}`;
  $('coordinatePrecision').textContent=audit?'This audit coordinate includes its exact rational saved state at every update. The residual plot uses the separately extracted exact difference.':'The target above is exact. This coordinate’s current state is a double display projection; its full exact fractions remain in the linked source case. Seven labelled audit coordinates bundle exact states at every update.';
  drawError();showFeature();
 }
 function selectCoordinate(id){coordinate=id;$('coordinateSelect').value=String(id);phaseIndex=0;phaseSetup();drawMatrix();showCoordinate();document.body.dataset.coordinate=String(coordinate);}
 function render(){state=trajectory.states[index];$('savedStep').value=String(index);$('stepLabel').value=`${index} / ${trajectory.updates}`;$('previousStep').disabled=index===0;$('firstStep').disabled=index===0;$('nextStep').disabled=index===trajectory.updates;
  const metric=$('methodSelect').value==='metric';$('methodStatus').dataset.certified=String(metric&&state.accepted);$('methodStatus').textContent=metric?`Metric GD in λᵢM: ${trajectory.updates} actual updates. ${state.accepted?'This saved state meets all three exact squared tolerance tests.':'The requested certificate has not yet been accepted at this saved state.'}`:'Ordinary real-coordinate GD: 50 actual updates, fixed budget. This run does not claim requested-error certification.';
  dl($('stateValues'),[['Saved update',`${index} / ${trajectory.updates}`],['Weighted full loss L ≈',fmt(state.loss)],['CC error bound ≈',fmt(Math.sqrt(state.bounds_squared.CC))],['CM error bound ≈',fmt(Math.sqrt(state.bounds_squared.CM))],['Full-coordinate bound ≈',fmt(Math.sqrt(state.bounds_squared.uniform))],['Exact request accepted',metric?(state.accepted?'yes':'not at this state'):'not claimed'],['Rows / raw column zeros',`${caseData.row_count} / ${caseData.raw_zero_entries}`],['Nonzero negative-μ(q) CC',String(caseData.negative_q_nonzero_CC_pair_ids.length)]]);$('exactLoss').textContent=state.loss_exact;
  $('signedReadouts').replaceChildren(...['CC','CM'].map(k=>{const article=document.createElement('article'),title=document.createElement('h4'),values=document.createElement('dl');title.textContent=k==='CC'?'C–C energy':'C–μ mixed readout';dl(values,[['Exact target basis (a,b)',basis(caseData.exact[k])],['Saved prediction, double ≈',displayComplex(state.predicted[k])],['Signed residual, double ≈',displayComplex(state.errors[k])],['Actual residual norm ≈',fmt(Math.sqrt(state.actual_errors_squared[k]))]]);article.append(title,values);return article;}));
  drawLoss();drawMatrix();showCoordinate();document.body.dataset.step=String(index);document.body.dataset.method=$('methodSelect').value;document.body.dataset.case=caseData.id;
 }
 function setup(){stop();caseData=data.cases[Number($('caseSelect').value)];trajectory=caseData.trajectories[$('methodSelect').value];index=trajectory.updates;$('savedStep').max=String(trajectory.updates);phaseSetup();$('caseSource').href=sourceBase+caseData.source_file;setStatus(`${caseData.row_count} rows · ${caseData.profile} common smooth profile · principal ν · saved ${caseData.source_file.split('/').at(-1)}`);render();}
 $('caseSelect').replaceChildren(...data.cases.map((c,i)=>new Option(`${c.row_set==='all_literal'?'All 2262 literal rows':'2148 guaranteed nonprincipal'} · ${c.profile} profile`,String(i))));
 $('coordinateSelect').replaceChildren(...data.pairs.map(p=>new Option(`${data.audit_coordinates.includes(p.id)?'★ exact · ':''}${p.id}: ${p.m}→${p.n} · μ(q)=${p.mu_q}`,String(p.id))));$('coordinateSelect').value=String(coordinate);
 buildMatrix();$('caseSelect').addEventListener('change',setup);$('methodSelect').addEventListener('change',setup);$('coordinateSelect').addEventListener('change',()=>selectCoordinate(Number($('coordinateSelect').value)));$('heatmapMode').addEventListener('change',drawMatrix);$('phaseSample').addEventListener('change',()=>{phaseIndex=Number($('phaseSample').value);showFeature();});$('savedStep').addEventListener('input',()=>{stop();index=Number($('savedStep').value);render();});
 const move=n=>{stop();index=Math.max(0,Math.min(trajectory.updates,index+n));render();};$('previousStep').addEventListener('click',()=>move(-1));$('nextStep').addEventListener('click',()=>move(1));$('firstStep').addEventListener('click',()=>{stop();index=0;render();});$('playSteps').setAttribute('aria-pressed','false');$('playSteps').addEventListener('click',()=>{if(timer){stop();return;}if(index===trajectory.updates)index=0;render();$('playSteps').textContent='Pause replay';$('playSteps').setAttribute('aria-pressed','true');timer=setInterval(()=>{if(index>=trajectory.updates){stop();return;}index++;render();},150);});
 const redraw=()=>{cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>{drawLoss();drawMatrix();drawError();});};new MutationObserver(redraw).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});const observer=new ResizeObserver(redraw);observer.observe($('lossPlot'));observer.observe($('errorPlot'));document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
 $('replayBody').hidden=false;$('coordinateSection').hidden=false;$('payloadProvenance').textContent=`Display payload SHA256: ${PAYLOAD_SHA256}. Frozen v2 manifest SHA256: ${data.manifest_sha256}. Seed ${data.seed}; exact source and artifact hashes are embedded in the payload. All 8 trajectory blocks are verified after native gzip decoding.`;setup();document.body.dataset.ready='true';
}
async function boot(){try{const response=await fetch(new URL('./data/arithmetic-learning.json',import.meta.url));if(!response.ok)throw Error(`Display response${response.status}`);const bytes=await response.arrayBuffer();if(await sha256(bytes)!==PAYLOAD_SHA256)throw Error('Display payload hash mismatch');const data=await unpackDisplay(JSON.parse(new TextDecoder().decode(bytes)));init(data);}catch(e){document.getElementById('loadStatus').textContent=`Saved replay unavailable: ${e.message}. Exact source links remain available below.`;document.body.dataset.ready='error';}}
if(typeof document!=='undefined')boot();
