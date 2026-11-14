import {surfaceProfile,selectionMapping,cycleText,relationAudit} from './surface-bridge-model.mjs';
const $=id=>document.getElementById(id),palette=['#a14a28','#276b9d','#16745d','#854bb0','#a6660a','#b44575','#2b7580','#666ca0','#7e681b'];
const torus=(u,v)=>[(1.55+.5*Math.cos(2*Math.PI*v))*Math.cos(2*Math.PI*u),(1.55+.5*Math.cos(2*Math.PI*v))*Math.sin(2*Math.PI*u),.5*Math.sin(2*Math.PI*v)];
const sample=f=>Array.from({length:81},(_,i)=>f(i/80));
export function mountSurfaceBridge(){
 let trace,node,profile,mapping={edges:[],arrows:[],sites:[],labels:[]},selected=0,stage=0,yaw=-.5,pitch=.65,zoom=1,hits=[],drag=null,lastIndices=[];
 const canvas=$('surfaceScene'),ctx=canvas.getContext('2d'),steps=['Surface / passport','Quiver from paired darts','Forbidden products','Completed order','Finite carrier / actual module'];
 function facts(){
  const d=profile.d,h=d.edges[selected][0],a=d.arrows[h],audit=relationAudit(d,h);
  $('surfaceTitle').textContent=profile.title;$('surfaceCurve').textContent=profile.curve;
  $('surfaceBoundary').textContent=profile.limit;
  $('surfacePassport').textContent=`σ=${cycleText(d.sigma)}\nα=${cycleText(d.alpha)}\nτ=σ⁻¹=${cycleText(d.tau)}\nφ=α∘σ⁻¹=${cycleText(d.phi)}\nPassport (black; clean white; faces): (${d.passport.map(a=>a.join(',')).join('; ')})\nV=${d.passport[0].length}, E=${d.edges.length}, F=${d.faces.length}; 2−2g=V−E+F=${2-2*d.genus}; g=${d.genus}`;
  const explanations=[`${profile.curve}. Black vertices are σ-orbits, clean white vertices pair darts by α, and faces are φ-orbits. ${profile.geometry==='sheet'?`Shown: the two sheets y=±√(x^${d.edges.length}−1), projected from ℂ² to ℝ³; sheets may overlap. Infinity and chart gluing are not rendered. The compactification has genus ${d.genus}.`:profile.geometry==='interval'?'Shown: the interval dessin on a spherical schematic.':`Shown: a topological torus embedding of the ${profile.geometry==='square'?'two fundamental loops':'three theta edges'}, not a metric uniformization of the algebraic curve.`}`,
   `Q₀=H/α, a_h:[h]→[τh]. Travel order ab traverses a then b. Selected edge [${selected}]={${d.edges[selected].join(',')}}. Its dart a${h} goes [${a.source}]→[${a.target}]. These are quiver vertices, whereas the black/white points belong to the dessin.`,
   `I=(a_h a_{φh}:h∈H). For a${h}, successor a${a.permitted} is permitted and a${a.forbidden} is forbidden. Both start at [${a.target}], but use opposite branches. Each arrow has one permitted and one forbidden successor; ${d.arrows.length} composability/distinctness checks pass. Permitted cycles survive to all lengths, so A=kQ/I is infinite-dimensional.`,
   `J=A₊, Λ=limₙ A/Jⁿ. R=k[[u]] embeds centrally by one full turn u_c on each permitted σ-cycle. Λ lies in ∏c B_c ⊂ ∏c M_ℓ(c)(k[[u_c]]), with the two diagonal constant terms paired by α equal. Rank_R Λ=Σc ℓ(c)²=${d.rank}. The conductor contains u∏c B_c. Path degree is not u-degree; order rank and finite spin/token dimension measure different objects, even when numerically equal.`,
   `${audit.checked} forbidden products checked exactly on a two-dimensional diagnostic module: ${audit.failures} failures. ${audit.description}`];
  $('surfaceConstruction').textContent=explanations[stage];
  $('surfaceRelations').textContent=d.arrows.map(a=>`a${a.dart}: [${a.source}]→[${a.target}]   allowed a${a.permitted}   a${a.dart}a${a.forbidden}=0`).join('\n');
  $('surfaceModule').textContent=`Actual diagnostic A/J² module for a${h}: all ${audit.checked} zero relations pass; ${audit.centralZero?'uM=0':'u²M=0, uM≠0'}.\n${audit.description}\nTrained/fixed numerical carrier: relation compatibility is not asserted.`;
  $('surfacePosition').textContent=`${stage+1} / ${steps.length} · ${steps[stage]}`;
  $('surfacePrevious').disabled=stage===0;$('surfaceNext').disabled=stage===steps.length-1;
  for(const b of $('surfaceSteps').children)b.setAttribute('aria-current',String(Number(b.dataset.stage)===stage));
  const selectedDescription=`Selected edge [${selected}] pairs darts ${d.edges[selected].join(' and ')}; attached arrows ${d.edges[selected].map(h=>'a'+h).join(', ')}.`;
  $('surfaceSelection').textContent=[`Numerical operation: ${node.id}`,mapping.labels.join(' · '),mapping.note,selectedDescription].filter(Boolean).join('\n');
  $('surfaceSceneCaption').textContent=profile.auxiliary&&$('surfaceView').value==='carrier'?`${profile.kind==='clock'?'Forward':'Backward'} Weyl torus: auxiliary finite basis sites; no dessin embedding claimed.`:($('surfaceView').value==='quiver'?'Quiver embedded schematically at dessin edge midpoints; arrows turn around black vertices.':'Black = σ-orbit · white = α-paired midpoint · thick color = numerical support · ring = selected edge')+(profile.geometry==='sheet'?' · branched-sheet projection':'');
 }
 function geometry(){
  const d=profile.d,curves=[],mesh=[],black=[];
  if(profile.geometry==='interval'){
   for(let j=1;j<9;j++){const v=-Math.PI/2+Math.PI*j/9;mesh.push(sample(t=>[1.5*Math.cos(v)*Math.cos(2*Math.PI*t),1.5*Math.cos(v)*Math.sin(2*Math.PI*t),1.5*Math.sin(v)]));}
   curves.push(sample(t=>[-1.4+2.8*t,0,0]));black.push([-1.4,0,0],[1.4,0,0]);
  }else if(profile.geometry==='sheet'){
   const m=d.edges.length,sheet=(r,t,sign)=>{const a=r**m*Math.cos(m*t)-1,b=r**m*Math.sin(m*t),abs=Math.hypot(a,b),re=Math.sqrt(Math.max(0,(abs+a)/2)),im=Math.sqrt(Math.max(0,(abs-a)/2))*(b<0?-1:1);return [1.6*r*Math.cos(t),1.6*r*Math.sin(t),sign*.65*(im+.3*re)];};
   for(const sign of [-1,1])for(let j=0;j<24;j++)mesh.push(sample(t=>sheet(t,2*Math.PI*(j+.21)/24,sign)));
   for(let e=0;e<m;e++){const angle=2*Math.PI*e/m;curves.push(sample(t=>{const r=t<=.5?2*t:2-2*t,sign=t<=.5?1:-1;return [1.6*r*Math.cos(angle),1.6*r*Math.sin(angle),sign*.65*Math.sqrt(Math.max(0,1-r**m))];}));}black.push([0,0,.65],[0,0,-.65]);
  }else{
   for(let j=0;j<16;j++){mesh.push(sample(t=>torus(t,j/16)));mesh.push(sample(t=>torus(j/16,t)));}
   if(profile.geometry==='square'){curves.push(sample(t=>torus(t,0)),sample(t=>torus(0,t)));black.push(torus(0,0));}
   else{for(const [a,b] of [[1/3,1/3],[-2/3,1/3],[1/3,-2/3]])curves.push(sample(t=>torus(a*t,b*t)));black.push(torus(0,0),torus(1/3,1/3));}
  }
  return {curves,mesh,black};
 }
 function draw(){
  if(!profile)return;
  const r=canvas.getBoundingClientRect(),ratio=Math.min(devicePixelRatio||1,2),w=r.width,h=r.height;if(w===0||h===0)return;
  canvas.width=w*ratio;canvas.height=h*ratio;ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,w,h);
  const dark=document.documentElement.dataset.theme==='biomech'||document.body.classList.contains('night')||document.documentElement.getAttribute('data-night')==='true'||getComputedStyle(document.body).backgroundColor==='rgb(7, 12, 18)';
  const colors=dark?['#f5ad7b','#83c5f1','#6be0bc','#c6a5f4','#f2cd76','#ee9aba','#80d4df','#afb5ef','#d6d18b']:palette;
  const ink=dark?'#d2e1e6':'#182c2b',meshColor=dark?'#415a65':'#b7c6ba';ctx.font='11px ui-monospace,monospace';
  const project=p=>{const x=p[0]*Math.cos(yaw)-p[1]*Math.sin(yaw),z=p[0]*Math.sin(yaw)+p[1]*Math.cos(yaw),y=p[2]*Math.cos(pitch)-z*Math.sin(pitch),depth=p[2]*Math.sin(pitch)+z*Math.cos(pitch),s=Math.min(w/5.5,h/4.2)*zoom*7/(7+depth);return [w/2+x*s,h/2-y*s,depth];};
  const path=(points,color,width=1,dash=[],arrow=false)=>{const ps=points.map(project);ctx.beginPath();ctx.setLineDash(dash);ps.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();ctx.setLineDash([]);if(arrow){const i=Math.floor(ps.length*.68),a=ps[i-2],b=ps[i],angle=Math.atan2(b[1]-a[1],b[0]-a[0]);ctx.beginPath();ctx.moveTo(b[0],b[1]);ctx.lineTo(b[0]-8*Math.cos(angle-.45),b[1]-8*Math.sin(angle-.45));ctx.lineTo(b[0]-8*Math.cos(angle+.45),b[1]-8*Math.sin(angle+.45));ctx.closePath();ctx.fillStyle=color;ctx.fill();}};
  const dot=(point,color,size,label,edge=null)=>{const p=project(point);if(edge===selected){ctx.beginPath();ctx.arc(p[0],p[1],size+4,0,2*Math.PI);ctx.strokeStyle=ink;ctx.lineWidth=1.5;ctx.stroke();}ctx.beginPath();ctx.arc(p[0],p[1],size,0,2*Math.PI);ctx.fillStyle=color;ctx.fill();ctx.strokeStyle=ink;ctx.lineWidth=1;ctx.stroke();if(label){ctx.fillStyle=ink;ctx.fillText(label,p[0]+size+3,p[1]-size-3);}if(edge!==null)hits.push({x:p[0],y:p[1],edge});};
  const g=geometry();for(const m of g.mesh)path(m,meshColor,.65);hits=[];
  const mode=$('surfaceView').value;
  if(mode==='carrier'&&profile.auxiliary){const dim=profile.kind==='clock'?trace.input.dimension:4;for(let j=0;j<dim;j++){const selected=mapping.sites.includes(j);dot(torus(j/dim,0),selected?'#dc8430':colors[j%colors.length],selected?10:6,`|${j}⟩`);}path(sample(t=>torus(t,0)),colors[1],2,[],true);return;}
  const active=new Set(mapping.edges);
  g.curves.forEach((c,e)=>path(c,active.has(e)?colors[e%colors.length]:meshColor,active.has(e)?3:1.4));
  if(profile.kind==='rg'){
   if(mapping.roles.includes('J+'))for(const c of g.curves)path(c.slice(0,41),colors[0],4);
   if(mapping.roles.includes('J−'))g.curves.forEach((c,e)=>{path(c.slice(40),colors[1],4,e%2?[4,3]:[]);dot(c[60],ink,1,e%2?'−J−':'+J−');});
   if(mapping.roles.includes('b')){dot(g.black[0],colors[2],10,'b');dot(g.black[1],colors[2],10,'−0.6b');}
   if(mapping.roles.length&&!mapping.roles.includes('b')){dot(g.black[0],ink,6,'black +');dot(g.black[1],ink,6,'black −');}
  }
  if(mode==='quiver'){
   for(const a of profile.d.arrows){const curve=g.curves[a.source],target=g.curves[a.target],sourcePoint=curve[40],targetPoint=target[40],vertex=a.dart<profile.d.sigma.length/2?g.black[0]:g.black.at(-1),bend=profile.geometry==='square'?g.black[0]:vertex;
    const points=sample(t=>sourcePoint.map((v,i)=>(1-t)**2*v+2*t*(1-t)*bend[i]+t*t*targetPoint[i]+(i===2?.12*Math.sin(Math.PI*t)*(a.dart%2?1:-1):0)));
    if(a.source===a.target){const center=sourcePoint;for(let i=0;i<points.length;i++){const t=i/80;points[i]=[center[0]+.45*Math.sin(2*Math.PI*t),center[1]+(a.dart?-.5:.5)*(1-Math.cos(2*Math.PI*t)),center[2]+.25*Math.sin(Math.PI*t)];}}
    path(points,mapping.arrows.includes(a.dart)?'#dd842c':colors[a.source%colors.length],mapping.arrows.includes(a.dart)?4:1.6,a.dart>=profile.d.sigma.length/2?[4,3]:[],true);
    dot(points[25],ink,1,`a${a.dart}`);
   }
  }else for(const p of g.black)dot(p,ink,6,'');
  g.curves.map((c,e)=>({c,e,depth:project(c[40])[2]})).sort((a,b)=>b.depth-a.depth).forEach(({c,e})=>dot(c[40],active.has(e)?colors[e%colors.length]:'#ffffff',active.has(e)?8:5,`[${e}]`,e));
 }
 function refresh(){facts();draw();}
 function setEdge(e){selected=e;$('surfaceEdge').value=String(e);refresh();}
 function changeStage(s){stage=Math.max(0,Math.min(4,s));refresh();}
 steps.forEach((name,i)=>{const b=document.createElement('button');b.textContent=`${i+1}. ${name}`;b.dataset.stage=i;b.onclick=()=>changeStage(i);$('surfaceSteps').append(b);});
 $('surfacePrevious').onclick=()=>changeStage(stage-1);$('surfaceNext').onclick=()=>changeStage(stage+1);
 $('surfaceEdge').onchange=()=>setEdge(Number($('surfaceEdge').value));$('surfaceView').onchange=refresh;
 $('surfaceOrbitLeft').onclick=()=>{yaw-=.25;draw();};$('surfaceOrbitRight').onclick=()=>{yaw+=.25;draw();};$('surfaceReset').onclick=()=>{yaw=-.5;pitch=.65;zoom=1;$('surfaceZoom').value='1';draw();};$('surfaceZoom').oninput=()=>{zoom=Number($('surfaceZoom').value);draw();};
 canvas.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,moved:false};canvas.setPointerCapture(e.pointerId);});
 canvas.addEventListener('pointermove',e=>{if(!drag)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>2)drag.moved=true;yaw+=dx*.008;pitch=Math.max(-1.3,Math.min(1.3,pitch+dy*.008));drag.x=e.clientX;drag.y=e.clientY;draw();});
 canvas.addEventListener('pointerup',e=>{if(drag&&!drag.moved){const r=canvas.getBoundingClientRect(),hit=hits.find(h=>Math.hypot(h.x-e.clientX+r.left,h.y-e.clientY+r.top)<18);if(hit)setEdge(hit.edge);}drag=null;});canvas.addEventListener('pointercancel',()=>drag=null);
 canvas.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.5,Math.min(2.4,zoom*Math.exp(-e.deltaY*.001)));$('surfaceZoom').value=String(zoom);draw();},{passive:false});
 canvas.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)){e.preventDefault();if(e.key==='ArrowLeft')yaw-=.15;if(e.key==='ArrowRight')yaw+=.15;if(e.key==='ArrowUp')pitch+=.1;if(e.key==='ArrowDown')pitch-=.1;draw();}});
 new ResizeObserver(draw).observe(canvas);new MutationObserver(draw).observe(document.documentElement,{attributes:true,attributeFilter:['class','data-theme','data-night']});new MutationObserver(draw).observe(document.body,{attributes:true,attributeFilter:['class','data-theme','data-night']});
 return {update(t,n,indices=[]){const changed=t!==trace,changedNode=n!==node;trace=t;node=n;lastIndices=indices;profile=surfaceProfile(t);mapping=selectionMapping(t,n,indices);
  if(changedNode&&!changed){selected=mapping.edges[0]??selected;$('surfaceEdge').value=String(selected);}
  if(changed){selected=0;stage=0;$('surfaceEdge').replaceChildren();profile.d.edges.forEach((c,e)=>$('surfaceEdge').add(new Option(`[${e}] = {${c.join(', ')}}`,e)));$('surfaceView').querySelector('[value="carrier"]').hidden=!profile.auxiliary;$('surfaceView').value=profile.auxiliary?'carrier':'dessin';}
  refresh();},snapshot:()=>({trace:trace?.id,node:node?.id,kind:profile?.kind,genus:profile?.d.genus,edges:profile?.d.edges.length,rank:profile?.d.rank,selected,stage,mapping,indices:lastIndices,yaw,zoom})};
}
