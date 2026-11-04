// Original lightweight Canvas2D tensor scene; no upstream renderer or assets.
import {flatTensor,sliceTensor} from './architecture-model.mjs';
import {operationRole,coordinateMask,architectureLayout,operationLayout,planeSlices,planeCells,cellDependencies} from './architecture-layout.mjs';
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
const same=(a,b)=>a?.length===b?.length&&a.every((v,i)=>v===b[i]);
const scales=new WeakMap();
function magnitudeScale(t){if(!scales.has(t)){let s=1e-12;const f=flatTensor(t);for(let i=0;i<f.real.length;i++)s=Math.max(s,Math.hypot(f.real[i],f.imag?.[i]??0));scales.set(t,s);}return scales.get(t);}
export function mountTensorViewport({canvas,state,controls,onSelect,onCell,onHover}){
 let layout=null,fullLayout=null,trace=null,nodes=null,selection=null,camera=null,target=null,frame=0,transition=0,lastTime=0,pan={x:0,y:0},hover=null,drag=null,painted=[],world=[];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),ctx=canvas.getContext('2d');
 const dark=()=>['dark','biomech'].includes(document.documentElement.dataset.theme)||document.body.classList.contains('night-engaged')||document.documentElement.classList.contains('theme-night')||getComputedStyle(document.body).backgroundColor==='rgb(6, 13, 18)';
 function projectRaw(x,y,z){const yaw=controls.flat.checked?0:state.yaw,pitch=controls.flat.checked?Math.PI/2:state.pitch,rx=x*Math.cos(yaw)-z*Math.sin(yaw),rz=x*Math.sin(yaw)+z*Math.cos(yaw);return {x:rx,y:y*Math.sin(pitch)-rz*Math.cos(pitch),depth:y*Math.cos(pitch)+rz*Math.sin(pitch)};}
 function desired(width,height){
  const chosen=layout.items;
  const points=chosen.flatMap(n=>[-n.width/2,n.width/2+40].flatMap(x=>[-n.height/2-30,n.height/2+30].flatMap(y=>[0,n.depth+45].map(z=>projectRaw(n.x+x,n.y+y,z)))));
  const x0=Math.min(...points.map(p=>p.x)),x1=Math.max(...points.map(p=>p.x)),y0=Math.min(...points.map(p=>p.y)),y1=Math.max(...points.map(p=>p.y));
  return {x:(x0+x1)/2,y:(y0+y1)/2,scale:Math.min((width-110)/Math.max(150,x1-x0),(height-120)/Math.max(100,y1-y0),2.6)};
 }
 function render(time=performance.now()){
  if(!state.node)return;
  if(trace!==state.trace||nodes!==state.nodes){trace=state.trace;nodes=state.nodes;fullLayout=architectureLayout(trace,nodes);camera=null;selection=null;pan={x:0,y:0};}
  layout=controls.range.value==='all'?fullLayout:operationLayout(fullLayout,state.node.id);
  const r=canvas.getBoundingClientRect(),width=r.width,height=r.height;if(!width||!height)return;
  const ratio=Math.min(devicePixelRatio||1,2);if(canvas.width!==Math.round(width*ratio)||canvas.height!==Math.round(height*ratio)){canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);}
  ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,width,height);
  const isDark=dark(),ink=isDark?'#d2e6e2':'#28423d',muted=isDark?'#8ba8aa':'#6b817b';
  ctx.fillStyle=isDark?'#111e25':'#f1f3ed';ctx.fillRect(0,0,width,height);
  const next=desired(width,height),changed=selection!==state.node.id;
  if(!camera)camera={...next};
  if(changed){selection=state.node.id;target=next;transition=reduced.matches?0:1;pan={x:0,y:0};}
  else if(!transition){camera=next;target=next;}
  if(transition){const dt=Math.min(50,time-(lastTime||time)),a=reduced.matches?1:1-Math.exp(-dt/75);for(const k of ['x','y','scale'])camera[k]+=(target[k]-camera[k])*a;if(Math.abs(camera.x-target.x)+Math.abs(camera.y-target.y)+Math.abs(camera.scale-target.scale)<.15){camera={...target};transition=0;}}
  lastTime=time;
  const scale=camera.scale*Number(controls.zoom.value);
  const project=(x,y,z)=>{const p=projectRaw(x,y,z);return [width/2+(p.x-camera.x)*scale+pan.x,height/2+(p.y-camera.y)*scale+pan.y];};
  const polygon=(points,fill,stroke,line=1)=>{ctx.beginPath();points.forEach((p,i)=>i?ctx.lineTo(...p):ctx.moveTo(...p));ctx.closePath();if(fill){ctx.fillStyle=fill;ctx.fill();}if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=line;ctx.stroke();}};
  const active=state.node.id,parents=new Set(state.node.inputs),children=new Set(layout.links.filter(l=>l.from===active).map(l=>l.to));
  const deps=state.selectedIndices?cellDependencies(trace,state.node,state.selectedIndices):null;
  // Subtle fixed grid is spatial context, never a scientific animation.
  ctx.strokeStyle=isDark?'#24333a':'#e2e7de';ctx.lineWidth=1;for(let x=width/2%40;x<width;x+=40){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,height);ctx.stroke();}for(let y=height/2%40;y<height;y+=40){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(width,y);ctx.stroke();}
  for(const l of layout.links){
   const a=layout.byId.get(l.from),b=layout.byId.get(l.to),diagnostic=operationRole(trace,a.node).diagnostic||operationRole(trace,b.node).diagnostic,p=project(a.x,a.y+a.height/2,a.depth),q=project(b.x,b.y-b.height/2,b.depth),emphasis=l.to===active||l.from===active;
   if(Math.max(p[1],q[1])<0||Math.min(p[1],q[1])>height)continue;
   ctx.setLineDash(diagnostic?[4,5]:[]);ctx.strokeStyle=diagnostic?muted:emphasis?'#bd8b35':isDark?'#4f6865':'#c4d2c5';ctx.globalAlpha=emphasis?.9:.45;ctx.lineWidth=emphasis?2:1;
   ctx.beginPath();ctx.moveTo(...p);const middle=(p[1]+q[1])/2;ctx.bezierCurveTo(p[0],middle,q[0],middle,...q);ctx.stroke();
   if(emphasis){ctx.beginPath();ctx.moveTo(q[0]-3,q[1]-7);ctx.lineTo(...q);ctx.lineTo(q[0]+3,q[1]-7);ctx.stroke();}
  }ctx.globalAlpha=1;ctx.setLineDash([]);
  painted=[];world=[];
  for(const item of layout.items){
   const selected=item.id===active,prefix=selected?state.leading:[],planes=planeSlices(item.node.tensor,prefix);
   planes.forEach((plane,i)=>world.push({...item,plane,planeIndex:i,selected,cameraDepth:projectRaw(item.x,item.y,item.depth+i*30).depth}));
  }
  world.sort((a,b)=>b.cameraDepth-a.cameraDepth);
  const sectionLabels=new Set();
  for(const item of world){
   const {node,selected}=item,w=item.width,h=item.height,x=item.x+item.planeIndex*14,y=item.y,z=item.depth+item.planeIndex*30;
   const top=[[-w/2,-h/2],[w/2,-h/2],[w/2,h/2],[-w/2,h/2]].map(([a,b])=>project(x+a,y+b,z)),xs=top.map(p=>p[0]),ys=top.map(p=>p[1]);
   const x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
   if(x1<-80||x0>width+80||y1<-80||y0>height+80)continue;
   const role=operationRole(trace,node),relevant=selected||parents.has(item.id)||children.has(item.id),isWeight=node.id.startsWith('weight.')||['parameters','head'].includes(node.id),hue=isWeight?234:node.id.includes('scores')||node.id.includes('logits')?40:155;
   ctx.globalAlpha=role.diagnostic&&!selected?.45:controls.range.value==='window'&&!relevant?.42:1;
   if(!controls.flat.checked){for(const edge of [[0,1],[1,2]]){const [i,j]=edge,co=[[-w/2,-h/2],[w/2,-h/2],[w/2,h/2],[-w/2,h/2]],bottom=co.map(([a,b])=>project(x+a,y+b,z-item.depth));polygon([top[i],top[j],bottom[j],bottom[i]],isDark?'#273d46':isWeight?'#c4c8e1':'#c8d8c8',isDark?'#445766':'#abc1ac');}}
   polygon(top,isDark?'#24453e':isWeight?'#dce0f2':'#d9e7d7',selected?'#c69238':isDark?'#718b85':'#8aa58e',selected?2:1);
   const grid=planeCells(node.tensor,item.plane.prefix),max=magnitudeScale(node.tensor),cellWidth=w/grid.columns,cellHeight=h/grid.rows;
   const screenCell=Math.min(Math.abs(cellWidth*scale),Math.abs(cellHeight*scale*Math.sin(state.pitch)));
   for(const cell of grid.cells){
    const u=(cell.c-grid.c0)/grid.cstep,v=(cell.r-grid.r0)/grid.rstep,xx=x-w/2+u*cellWidth,yy=y-h/2+v*cellHeight;
    const points=[[0,0],[cellWidth,0],[cellWidth,cellHeight],[0,cellHeight]].map(([a,b])=>project(xx+a,yy+b,z+.1));
    const masked=coordinateMask(trace,node,cell.indices),value=cell.real,weight=Math.min(1,Math.hypot(value,cell.imag)/max),source=deps?.refs.some(ref=>ref.id===node.id&&same(ref.indices,cell.indices)),chosen=selected&&same(state.selectedIndices,cell.indices),underMouse=hover?.id===item.id&&same(hover.indices,cell.indices);
    const fill=masked?isDark?'#3b4244':'#c7cec5':`hsl(${value<0?22:hue} ${isDark?36:34}% ${isDark?25+weight*30:91-weight*38}%)`;
    polygon(points,fill,source||chosen||underMouse?'#e9ab3d':screenCell>3?isDark?'#23383299':'#ffffffaa':null,source||chosen||underMouse?2:Math.min(.6,screenCell/6));
    if(masked&&screenCell>5){ctx.beginPath();ctx.moveTo(...points[0]);ctx.lineTo(...points[2]);ctx.strokeStyle='#788b7d';ctx.stroke();}
    if(screenCell>23&&relevant){const p=project(xx+cellWidth/2,yy+cellHeight/2,z+.1);ctx.fillStyle=isDark?'#e2efdf':'#244333';ctx.font='9px ui-monospace,monospace';ctx.textAlign='center';ctx.fillText(masked?'×':Number(value.toPrecision(2)).toString(),p[0],p[1]+3,Math.abs(cellWidth*scale)-2);}
   }
   ctx.globalAlpha=1;
   const hit={id:item.id,depth:item.cameraDepth,points:top,x0,x1,y0,y1,grid,plane:item.plane,geometry:item};painted.push(hit);
   if(item.planeIndex===0){
    const label=project(x-w/2,y-h/2-10,z);ctx.fillStyle=selected?'#a96c1a':ink;ctx.font=`${selected?'600 ':''}${clamp(10*scale,9,13)}px ui-monospace,monospace`;ctx.textAlign='left';
    ctx.fillText(node.id,label[0],label[1],Math.max(100,w*scale+80));
    ctx.font='9px ui-monospace,monospace';ctx.fillStyle=muted;
    const footer=project(x-w/2,y+h/2+14,z);const shape=node.tensor.shape.length?node.tensor.shape.join(' × '):'scalar';
    ctx.fillText(shape+(grid.sampled?` · sampled Δr${grid.rstep}, Δc${grid.cstep}`:item.folded?' · folded basis':''),footer[0],footer[1]);
    if(role.diagnostic){ctx.fillStyle=muted;ctx.fillText(role.label,footer[0],footer[1]+13);}
    if(node.gate){ctx.fillText(`${node.gate}  q[${node.wires.join(',')}]`,footer[0],footer[1]+13);}
    if(!sectionLabels.has(item.section)&&controls.range.value==='all'){
     sectionLabels.add(item.section);const p=project(-1170,y,z);if(p[0]>-50&&p[0]<width-100){ctx.font='11px system-ui';ctx.fillText(item.section,p[0],p[1]);}
    }
   }
   if(item.plane.label){const p=project(x+w/2+5,y-h/2,z);ctx.fillStyle=muted;ctx.font='9px ui-monospace,monospace';ctx.textAlign='left';ctx.fillText(item.plane.label,p[0],p[1]);}
  }
  if(controls.lens?.checked){
   const t=state.node.tensor,slice=sliceTensor(t,state.leading,state.row,state.col,8),cols=slice.cells[0].length,rows=slice.cells.length,size=Math.min(27,(width-70)/Math.max(cols,5)),lw=Math.max(190,cols*size+24),lh=rows*size+59,lx=width-lw-16,ly=65;
   ctx.fillStyle=isDark?'#12272ef5':'#fbfcf5f5';ctx.fillRect(lx,ly,lw,lh);ctx.strokeStyle=isDark?'#5d786d':'#bacbb5';ctx.strokeRect(lx,ly,lw,lh);
   ctx.fillStyle=ink;ctx.font='10px ui-monospace,monospace';ctx.textAlign='left';ctx.fillText('CELL LENS · exact selected slice',lx+12,ly+17);
   const gx=lx+12,gy=ly+29,max=magnitudeScale(t);
   for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){
    const cell=slice.cells[r][c];if(!cell)continue;const x=gx+c*size,y=gy+r*size,masked=coordinateMask(trace,state.node,cell.indices),chosen=same(cell.indices,state.selectedIndices),under=hover?.id===active&&same(hover.indices,cell.indices);
    ctx.fillStyle=masked?isDark?'#3e4946':'#cbd3c7':`hsl(${cell.real<0?22:155} 35% ${isDark?30+25*Math.min(1,Math.hypot(cell.real,cell.imag)/max):91-35*Math.min(1,Math.hypot(cell.real,cell.imag)/max)}%)`;ctx.fillRect(x,y,size,size);ctx.strokeStyle=chosen||under?'#d69a30':isDark?'#567468':'#f6faf0';ctx.lineWidth=chosen||under?2:1;ctx.strokeRect(x,y,size,size);
    if(size>=20){ctx.fillStyle=isDark?'#e1eee3':'#234437';ctx.font='8px ui-monospace,monospace';ctx.textAlign='center';ctx.fillText(masked?'×':Number(cell.real.toPrecision(2)).toString(),x+size/2,y+size/2+3,size-2);}
   }
   ctx.fillStyle=muted;ctx.font='9px ui-monospace,monospace';ctx.textAlign='left';ctx.fillText(t.real?'Real component · full complex value on hover':'Literal stored values · click to pin',lx+12,ly+lh-12,lw-22);
   const grid={cells:slice.cells.flat().filter(Boolean).map((c,i)=>({...c,r:Math.floor(i/cols)+slice.rowStart,c:i%cols+slice.columnStart})),r0:slice.rowStart,c0:slice.columnStart,rstep:1,cstep:1,rows,columns:cols,sampled:false};
   const points=[[gx,gy],[gx+cols*size,gy],[gx+cols*size,gy+rows*size],[gx,gy+rows*size]];
   painted.push({id:active,depth:-1e20,points,x0:gx,x1:gx+cols*size,y0:gy,y1:gy+rows*size,grid,plane:{prefix:slice.leading},lens:true});
  }
  if(state.node.gate){
   const group=state.node.id.split('.')[0],input=trace.nodes.find(n=>n.id===group+'.input'),n=input?Math.round(Math.log2(input.tensor.shape[0])):Math.max(...state.node.wires)+1,gx=22,gy=78,gw=Math.min(240,width*.33);
   ctx.fillStyle=isDark?'#14242ce8':'#fafcf2ec';ctx.fillRect(gx-8,gy-19,gw+16,n*19+40);ctx.font='10px ui-monospace,monospace';ctx.fillStyle=muted;ctx.textAlign='left';ctx.fillText('SAVED GATE SUPPORT',gx,gy-3);
   for(let q=0;q<n;q++){const y=gy+17+q*19;ctx.fillStyle=ink;ctx.fillText('q'+q,gx,y+3);ctx.strokeStyle=state.node.wires.includes(q)?'#c28a32':isDark?'#5f7c76':'#b3c4b1';ctx.beginPath();ctx.moveTo(gx+25,y);ctx.lineTo(gx+gw,y);ctx.stroke();}
   const ys=state.node.wires.map(q=>gy+17+q*19),x=gx+gw*.6;ctx.strokeStyle='#bd8b35';ctx.lineWidth=2;if(ys.length>1){ctx.beginPath();ctx.moveTo(x,Math.min(...ys));ctx.lineTo(x,Math.max(...ys));ctx.stroke();}
   for(const y of ys){ctx.fillStyle=isDark?'#203b34':'#e2ebd7';ctx.fillRect(x-17,y-8,34,16);ctx.strokeRect(x-17,y-8,34,16);ctx.fillStyle=ink;ctx.textAlign='center';ctx.font='9px ui-monospace,monospace';ctx.fillText(state.node.gate,x,y+3);}
  }
  state.hits=painted;
  const familyLabels={attention:'ATTENTION / PARALLEL Q · K · V',quantum:'UNITARY GATES → STATE → MEASUREMENT',gaussian:'SYMPLECTIC MAPS → COVARIANCE',critic:'LATENT INTERVENTION → CODE CRITIC',gflownet:'CONTINUOUS PATH → TRAJECTORY BALANCE',carrier:'FINITE CLOCK / SHIFT',dataflow:'RECORDED NUMERICAL DATAFLOW'};
  ctx.fillStyle=muted;ctx.font='10px system-ui';ctx.textAlign='left';ctx.fillText(familyLabels[layout.family],18,25);
  ctx.fillText(`${fullLayout.items.length} model tensors · ${layout.items.length} in view · ${layout.links.length} recorded dependencies · ${controls.range.value==='all'?'model overview':'operation focus'}`,18,43);
  ctx.fillText('Activation  ■     Weight  ■     Reduction  ■     Selected dependency  ━',18,height-17);
  controls.caption.textContent=state.node.id+' · '+layout.byId.get(state.node.id)?.section;
  canvas.setAttribute('aria-label',`${layout.family} tensor architecture. Selected ${state.node.id}. Hover or select tensor cells; Shift-drag to pan, drag to orbit, scroll to zoom. F fits, O shows overview, Enter focuses, arrows step.`);
  cancelAnimationFrame(frame);frame=0;if(transition)frame=requestAnimationFrame(render);
 }
 function pick(x,y){
  for(const hit of [...painted].reverse()){
   if(x<hit.x0||x>hit.x1||y<hit.y0||y>hit.y1)continue;
   const [o,b,,d]=hit.points,ux=b[0]-o[0],uy=b[1]-o[1],vx=d[0]-o[0],vy=d[1]-o[1],det=ux*vy-uy*vx;if(Math.abs(det)<1e-9)continue;
   const u=((x-o[0])*vy-(y-o[1])*vx)/det,v=(ux*(y-o[1])-uy*(x-o[0]))/det;if(u<0||u>=1||v<0||v>=1)continue;
   const col=Math.floor(u*hit.grid.columns),row=Math.floor(v*hit.grid.rows),cell=hit.grid.cells.find(c=>Math.round((c.r-hit.grid.r0)/hit.grid.rstep)===row&&Math.round((c.c-hit.grid.c0)/hit.grid.cstep)===col);
   if(cell)return {id:hit.id,...cell,prefix:hit.plane.prefix,sampled:hit.grid.sampled,screen:{x,y}};
  }return null;
 }
 const pointer=e=>{const r=canvas.getBoundingClientRect();return {x:e.clientX-r.left,y:e.clientY-r.top};};
 canvas.onpointerdown=e=>{const p=pointer(e);drag={...p,yaw:state.yaw,pitch:state.pitch,pan:{...pan},mode:e.shiftKey||e.button===1?'pan':'orbit',moved:false};canvas.setPointerCapture(e.pointerId);};
 canvas.onpointermove=e=>{const p=pointer(e);if(drag){const dx=p.x-drag.x,dy=p.y-drag.y;if(Math.hypot(dx,dy)>3)drag.moved=true;if(drag.mode==='pan')pan={x:drag.pan.x+dx,y:drag.pan.y+dy};else{state.yaw=drag.yaw+dx*.007;state.pitch=clamp(drag.pitch+dy*.004,.3,1.55);}transition=0;render();return;}const hit=pick(p.x,p.y);hover=hit;canvas.style.cursor=hit?'crosshair':'grab';onHover?.(hit);render();};
 canvas.onpointerup=e=>{if(drag&&!drag.moved){const p=pointer(e),hit=pick(p.x,p.y);if(hit)onCell(hit);}drag=null;};
 canvas.onpointercancel=()=>drag=null;canvas.onpointerleave=()=>{if(!drag){hover=null;onHover?.(null);render();}};
 canvas.addEventListener('wheel',e=>{e.preventDefault();controls.zoom.value=clamp(Number(controls.zoom.value)*Math.exp(-e.deltaY*.001),.25,5);render();},{passive:false});
 canvas.onkeydown=e=>{if(['f','F','0'].includes(e.key)){e.preventDefault();fit();}if(['o','O'].includes(e.key)){e.preventDefault();controls.range.value='all';fit();}if(e.key==='Enter'){e.preventDefault();controls.range.value='window';fit();}if(e.shiftKey&&e.key.startsWith('Arrow')){e.preventDefault();pan.x+=e.key==='ArrowLeft'?35:e.key==='ArrowRight'?-35:0;pan.y+=e.key==='ArrowUp'?35:e.key==='ArrowDown'?-35:0;render();}else if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();onSelect(e.key==='ArrowLeft'?-1:1);}if(e.key==='+'||e.key==='='){controls.zoom.value=clamp(Number(controls.zoom.value)*1.2,.25,5);render();}if(e.key==='-'){controls.zoom.value=clamp(Number(controls.zoom.value)/1.2,.25,5);render();}};
 function fit(){pan={x:0,y:0};camera=null;transition=0;controls.zoom.value=1;render();}
 new MutationObserver(()=>render()).observe(document.documentElement,{attributes:true,attributeFilter:['class','data-theme','data-living-theme']});
 return {render,fit,layout:()=>layout,pan:(x,y)=>{pan.x+=x;pan.y+=y;render();},snapshot:()=>({family:layout?.family,visiblePlanes:painted.length,pan:{...pan},cellPlanes:painted.map(h=>({id:h.id,depth:h.depth,prefix:h.plane.prefix,sampled:h.grid.sampled,lens:Boolean(h.lens),rows:h.grid.rows,columns:h.grid.columns,points:h.points}))})};
}
