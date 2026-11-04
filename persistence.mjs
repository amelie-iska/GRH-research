import {staircase,standard,rankMap,cwAt,specialized,monomial,validateQuantum,flagComplex,inclusionRanks,comparable} from './persistence-model.mjs';
const $=id=>document.getElementById(id),state={model:staircase([[2,0],[1,1],[0,2]]),data:null,from:[0,0],to:[1,0],yaw:.35,pitch:.35,complexCache:new Map(),rankHits:[]};
const text=(id,value)=>$(id).textContent=value;
function canvas(id){const element=$(id),r=element.getBoundingClientRect(),ratio=Math.min(devicePixelRatio||1,2);if(!r.width||!r.height)return null;if(element.width!==Math.round(r.width*ratio)||element.height!==Math.round(r.height*ratio)){element.width=Math.round(r.width*ratio);element.height=Math.round(r.height*ratio);}const ctx=element.getContext('2d');ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,r.width,r.height);return {ctx,w:r.width,h:r.height};}
function updateAlgebra(){
 const m=state.model,factor=$('coefficientE').checked?4:1;
 for(const [name,point] of [['source',state.from],['target',state.to]])for(let axis=0;axis<2;axis++){const input=$(name+(axis?'B':'A'));input.max=m.bounds[axis]+1;point[axis]=Math.min(point[axis],Number(input.max));}
 for(let axis=0;axis<2;axis++)state.to[axis]=Math.max(state.to[axis],state.from[axis]);
 for(const [name,point] of [['source',state.from],['target',state.to]])for(let axis=0;axis<2;axis++)$(name+(axis?'B':'A')).value=point[axis];
 text('idealDescription','R = k[x,y]\nI = ('+m.gens.map(monomial).join(', ')+')\nFitting₀(R/I) = I; support = origin with its stated thickening.\nHilbert length = '+m.basis.length);
 text('syzygies',m.syzygies.map((s,i)=>`s${i} = -y^${s.negativeY} e${i} + x^${s.positiveX} e${i+1}  @ (${s.degree})`).join('\n'));
 text('bettiShifts',m.betti.map((g,i)=>`F${i}: `+g.map(p=>'('+p+')').join(', ')).join('\n'));
 const n=m.gens.length;
 text('bettiRanks',`Over R: (1, ${n}, ${n-1})`+(factor===4?`\nE⊗ₖM as an R-module: (4, ${4*n}, ${4*(n-1)})\nOver B=Λ[x,y], the u² cone: (1, ${n+1}, ${2*n-1}, ${n-1})`:'\nEnable E to compare the different coefficient rings.'));
 text('standardBasis',m.basis.map(monomial).join(' + '));
 text('moduleRank',`ν=(${state.from}) → μ=(${state.to})\nField-fiber dimensions: ${factor*Number(standard(m,state.from))} → ${factor*Number(standard(m,state.to))}; map rank = ${factor*rankMap(m,state.from,state.to)}`);
 const cw=cwAt(m,state.to);text('cwDescription',`CW incidence at μ: one vertex, one loop, ${cw.disks.length} disk(s) attached once to that same loop. H₁ field dimension ${factor*cw.h1}; H₂ field dimension ${factor*cw.h2}. Active generator disks: ${cw.disks.join(', ')||'none'}. The CW space is an auxiliary filtered model, not the compact dessin surface.`);
 const fiber=specialized(m,...$('fiberPoint').value.split(',').map(Number));text('fiberResult',`R-resolution fiber at (${$('fiberPoint').value}) over F₂:\n(H₀,H₁,H₂) = (${fiber.homology})`);
 drawStaircase();
}
function drawStaircase(){
 const c=canvas('staircaseCanvas');if(!c)return;const {ctx,w,h}=c,m=state.model,maxx=m.bounds[0]+1,maxy=m.bounds[1]+1,step=Math.min((w-100)/(maxx+1),(h-70)/(maxy+1)),x0=55,y0=h-38;
 const p=([a,b])=>[x0+a*step,y0-b*step];ctx.font='11px ui-monospace,monospace';ctx.textAlign='center';
 for(let a=0;a<=maxx;a++)for(let b=0;b<=maxy;b++){const [x,y]=p([a,b]);ctx.beginPath();ctx.arc(x,y,Math.max(2,Math.min(6,step*.13)),0,2*Math.PI);ctx.fillStyle=standard(m,[a,b])?'#145e4d':'#cbd6c6';ctx.fill();}
 m.gens.forEach(g=>{const [x,y]=p(g);ctx.fillStyle='#c16b37';ctx.fillRect(x-5,y-5,10,10);});
 m.betti[2].forEach(g=>{const [x,y]=p(g);ctx.fillStyle='#487ca8';ctx.beginPath();ctx.moveTo(x,y-7);ctx.lineTo(x+7,y);ctx.lineTo(x,y+7);ctx.lineTo(x-7,y);ctx.closePath();ctx.fill();});
 const a=p(state.from),b=p(state.to);ctx.strokeStyle=rankMap(m,state.from,state.to)?'#145e4d':'#ae6245';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(...a);ctx.lineTo(b[0],a[1]);ctx.lineTo(...b);ctx.stroke();
 for(const [g,label] of [[state.from,'ν'],[state.to,'μ']]){const [x,y]=p(g);ctx.strokeStyle='#182c2b';ctx.lineWidth=2;ctx.strokeRect(x-10,y-10,20,20);ctx.fillStyle='#182c2b';ctx.fillText(label,x+15,y-10);}
 ctx.fillStyle='#58716c';for(let a=0;a<=maxx;a++)ctx.fillText(a,...[p([a,0])[0],y0+20]);for(let b=0;b<=maxy;b++)ctx.fillText(b,x0-20,p([0,b])[1]+3);ctx.fillText('a',w-20,h-15);ctx.fillText('b',20,20);
}
function complex(channel,r,e){const key=channel+':'+r+':'+e;if(!state.complexCache.has(key)){if(state.complexCache.size>=512)state.complexCache.delete(state.complexCache.keys().next().value);state.complexCache.set(key,flagComplex(state.data,channel,r,e));}return state.complexCache.get(key);}
function updateQuantum(){
 if(!state.data)return;const channel=$('channel').value;
 const from=[Number($('radiusA').value),Number($('energyA').value)],to=[Math.max(from[0],Number($('radiusB').value)),Math.max(from[1],Number($('energyB').value))];$('radiusB').value=to[0];$('energyB').value=to[1];
 const a=complex(channel,...from),b=complex(channel,...to),ranks=inclusionRanks(a,b);state.quantum={from,to,a,b,ranks,channel};
 text('sourceTitle',`ν = (${from})`);text('targetTitle',`μ = (${to})`);
 for(const [id,c] of [['sourceHomology',a],['targetHomology',b]])text(id,`(vertices, edges, triangles) = (${c.vertices.length}, ${c.edges.length}, ${c.triangles.length})\n(β₀, β₁) over F₂ = (${c.betti})`);
 text('quantumRank',`Induced ν→μ ranks over F₂: ρ₀=${ranks.h0}, ρ₁=${ranks.h1}`);
 const input=complex('input',...from),output=complex('output',...from),contracted=inclusionRanks(input,output);
 text('channelInclusion',`At ν, frozen labels give K_input ⊆ K_output; identity-on-labels induced H₁ rank = ${contracted.h1}. Birth grades stay fixed. This compares one common channel, not successive unrelated training epochs.`);
 drawComplex('sourceComplex',a);drawComplex('targetComplex',b);drawRank();
}
function project(p,w,h){const [x,y,z]=p,rx=x*Math.cos(state.yaw)-y*Math.sin(state.yaw),ry=x*Math.sin(state.yaw)+y*Math.cos(state.yaw),depth=ry*Math.cos(state.pitch)-z*Math.sin(state.pitch),scale=Math.min(w,h)*.34/(1+depth*.14);return {x:w/2+rx*scale,y:h/2-(ry*Math.sin(state.pitch)+z*Math.cos(state.pitch))*scale,depth};}
function drawComplex(id,c){
 const result=canvas(id);if(!result)return;const {ctx,w,h}=result,points=state.data.points.map(p=>project(p.position,w,h));
 ctx.lineWidth=1;ctx.strokeStyle='#c3cebc';for(const axis of [0,1,2]){ctx.beginPath();for(let j=0;j<=60;j++){const a=j*Math.PI/30,p=[Math.cos(a),Math.sin(a),0];if(axis===1)[p[1],p[2]]=[p[2],p[1]];if(axis===2)[p[0],p[2]]=[p[2],p[0]];const q=project(p,w,h);j?ctx.lineTo(q.x,q.y):ctx.moveTo(q.x,q.y);}ctx.stroke();}
 ctx.fillStyle='#90b88c22';for(const face of c.triangles){ctx.beginPath();face.forEach((v,i)=>i?ctx.lineTo(points[v].x,points[v].y):ctx.moveTo(points[v].x,points[v].y));ctx.closePath();ctx.fill();}
 ctx.strokeStyle='#145e4d99';ctx.lineWidth=1.5;for(const [i,j] of c.edges){ctx.beginPath();ctx.moveTo(points[i].x,points[i].y);ctx.lineTo(points[j].x,points[j].y);ctx.stroke();}
 const active=new Set(c.vertices);points.map((p,i)=>({...p,i})).sort((a,b)=>b.depth-a.depth).forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,active.has(p.i)?6:3,0,2*Math.PI);ctx.fillStyle=active.has(p.i)?'#145e4d':'#b9c7b2';ctx.fill();ctx.fillStyle='#345149';ctx.font='11px system-ui';ctx.fillText(state.data.points[p.i].label,p.x+8,p.y-5);});
}
function drawRank(){
 const result=canvas('rankCanvas');if(!result)return;const {ctx,w,h}=result,rs=[0,200,400,600,800,1000],es=[1000,500,0],dx=(w-80)/6,dy=(h-50)/3,{to,channel}=state.quantum;
 state.rankHits=[];ctx.font='12px ui-monospace,monospace';ctx.textAlign='center';
 es.forEach((e,row)=>rs.forEach((r,col)=>{const x=50+col*dx,y=10+row*dy,valid=r<=to[0]&&e<=to[1],rank=valid?inclusionRanks(complex(channel,r,e),complex(channel,...to)).h1:null;ctx.fillStyle=rank===null?'#e5e6de':rank?'#a2c79a':'#d1ddc8';ctx.fillRect(x,y,dx-4,dy-4);ctx.fillStyle='#264734';ctx.fillText(rank===null?'—':rank,x+dx/2,y+dy/2);if(valid)state.rankHits.push({x0:x,x1:x+dx,y0:y,y1:y+dy,r,e});}));
 ctx.fillStyle='#58716c';rs.forEach((r,i)=>ctx.fillText(r,50+(i+.5)*dx,h-10));es.forEach((e,i)=>ctx.fillText(e,23,10+(i+.5)*dy));
}
function tab(name){for(const id of ['algebra','quantum']){$(id).hidden=id!==name;$(id+'Tab').setAttribute('aria-selected',String(id===name));}name==='algebra'?updateAlgebra():updateQuantum();}
$('algebraTab').onclick=()=>tab('algebra');$('quantumTab').onclick=()=>tab('quantum');
function applyIdeal(){try{const gens=$('customIdeal').value.split(';').map(g=>{const pair=g.trim().split(',');if(pair.length!==2||pair.some(n=>!/^\d+$/.test(n.trim())))throw Error('Enter two natural exponents per generator');return pair.map(Number);});state.model=staircase(gens);text('idealStatus','Minimal staircase accepted. Parameters x,y are the two filtration directions.');$('idealStatus').classList.remove('error');state.from=[0,0];state.to=[1,0];updateAlgebra();}catch(error){text('idealStatus',error.message+' · Keeping the previous valid ideal.');$('idealStatus').classList.add('error');}}
$('applyIdeal').onclick=applyIdeal;$('idealPreset').onchange=()=>{$('customIdeal').value=$('idealPreset').value;applyIdeal();};
for(const name of ['source','target'])for(const [axis,suffix] of [[0,'A'],[1,'B']])$(name+suffix).oninput=()=>{state[name==='source'?'from':'to'][axis]=Number($(name+suffix).value);updateAlgebra();};
$('coefficientE').onchange=updateAlgebra;$('fiberPoint').onchange=updateAlgebra;
for(const id of ['radiusA','radiusB','energyA','energyB'])$(id).oninput=updateQuantum;$('channel').onchange=updateQuantum;
$('rankCanvas').onclick=e=>{const b=$('rankCanvas').getBoundingClientRect(),x=e.clientX-b.left,y=e.clientY-b.top,hit=state.rankHits.find(v=>x>=v.x0&&x<v.x1&&y>=v.y0&&y<v.y1);if(hit){$('radiusA').value=hit.r;$('energyA').value=hit.e;updateQuantum();}};
for(const id of ['sourceComplex','targetComplex']){let drag;$(id).onpointerdown=e=>{drag=[e.clientX,e.clientY,state.yaw,state.pitch];$(id).setPointerCapture(e.pointerId);};$(id).onpointermove=e=>{if(!drag)return;state.yaw=drag[2]+(e.clientX-drag[0])*.01;state.pitch=Math.max(-1.2,Math.min(1.2,drag[3]+(e.clientY-drag[1])*.007));updateQuantum();};$(id).onpointerup=()=>drag=null;$(id).onpointercancel=()=>drag=null;}
const resize=new ResizeObserver(()=>{$('algebra').hidden?updateQuantum():drawStaircase();});for(const id of ['staircaseCanvas','sourceComplex','targetComplex','rankCanvas'])resize.observe($(id));
window.persistenceTool={snapshot:()=>({ideal:state.model.gens,length:state.model.basis.length,from:state.from,to:state.to,quantum:state.quantum?{from:state.quantum.from,to:state.quantum.to,bettiA:state.quantum.a.betti,bettiB:state.quantum.b.betti,ranks:state.quantum.ranks,channel:state.quantum.channel}:null,yaw:state.yaw})};
if(new URLSearchParams(location.search).has('embed'))document.body.classList.add('embed');updateAlgebra();
try{const response=await fetch('/data/persistence/manifest.json');if(!response.ok)throw Error('Numerical manifest unavailable');const manifest=await response.json();if(!/^quantum-[a-f0-9]{16}\.json$/.test(manifest.file))throw Error('Invalid numerical record path');const r=await fetch('/data/persistence/'+manifest.file);if(!r.ok)throw Error('Numerical record unavailable');const bytes=await r.arrayBuffer(),hash=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),v=>v.toString(16).padStart(2,'0')).join('');if(hash!==manifest.sha256)throw Error('Numerical record checksum mismatch');state.data=validateQuantum(JSON.parse(new TextDecoder().decode(bytes)));text('quantumProvenance',JSON.stringify({provenance:state.data.provenance,checks:state.data.checks},null,2));text('quantumStatus','SHA-256 verified. Frozen integer labels; homology/inclusion ranks exact over F₂. Numerical distance estimates are not interval-certified.');updateQuantum();document.body.dataset.ready='true';}catch(error){text('quantumStatus',error.message);$('quantumStatus').classList.add('error');$('quantumTab').disabled=true;document.body.dataset.ready='error';}
