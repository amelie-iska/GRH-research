(function () {
  'use strict';
  const Q=QuantumCore,$=id=>document.getElementById(id),NS='http://www.w3.org/2000/svg';
  const C={ink:'#182b29',teal:'#14695e',ochre:'#a65b19',muted:'#596b64',line:'#d4ddd5',paper:'#f7f7f0'};
  let cases=[],model=null,worker=null,ready=false,busy=false,busyMode=null,selected=0,check=null,circuit=[],cursor=0;
  let theta=Q.initialTheta.slice(),history=[],yaw=-25,pitch=35,points=[],loadVersion=0,latestRecords={},workerError=null;
  function elem(tag,text,attrs={}) {const e=document.createElement(tag);if(text!=null)e.textContent=text;for(const[k,v]of Object.entries(attrs))e.setAttribute(k,v);return e;}
  function sv(tag,attrs={},text) {const e=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,v);if(text!=null)e.textContent=text;return e;}
  function txt(svg,x,y,text,attrs={}) {svg.append(sv('text',{x,y,'font-size':11,...attrs},text));}
  function line(svg,x1,y1,x2,y2,attrs={}) {svg.append(sv('line',{x1,y1,x2,y2,stroke:C.line,...attrs}));}
  function number(x,d=6) {if(!Number.isFinite(x))return '—';return Math.abs(x)<5*10**(-d)?'0':x.toFixed(d);}
  function status(s) {$('qStatus').textContent=s;}
  function post(type,data={}) {if(worker)worker.postMessage({type,...data});}
  function controls() {
    document.querySelectorAll('[data-live]').forEach(e=>e.disabled=!ready||busy);
    $('stopCircuit').disabled=!busy;
    $('stopTraining').disabled=!busy||busyMode!=='train';
    $('surfaceCase').disabled=busy;
    for(let i=0;i<4;i++)$('theta'+i).disabled=busy;
    $('resetTheta').disabled=busy;
    document.querySelectorAll('[data-parameter-action]').forEach(e=>e.disabled=busy);
  }
  function clearStateDisplay() {
    ['stateNorm','stateFidelity','stateSupport','stateEntropy'].forEach(id=>$(id).textContent='—');
    $('checkRows').replaceChildren();$('amplitudeRows').replaceChildren();
    drawWeights([]);$('gateStatus').textContent='Circuit data loaded; no live state for this case.';
  }
  function wireName(q) {return 'q'+q;}
  function selectQubit(q) {
    selected=Number(q);$('selectedQubit').value=String(selected);$('gateTarget').value=String(selected);
    const edge=model.edges[selected],a=model.x_checks.filter(c=>c.qubits.includes(selected)),b=model.z_checks.filter(c=>c.qubits.includes(selected));
    $('qubitInfo').textContent=`${wireName(selected)} connects vertices ${edge.u} and ${edge.v}. X checks: ${a.map(c=>c.id).join(', ')}. Z checks: ${b.map(c=>c.id).join(', ')}.`;
    drawSurface();drawCircuit();
  }
  function setTheta(values,clear=false) {
    theta=values.slice();theta.forEach((v,i)=>{$('theta'+i).value=v;$('theta'+i+'Out').textContent=number(v,4);});
    if(clear){history=[];drawLoss();renderPredictions([]);$('predictionStatus').textContent='Angles changed. Run a sample to compute the new prediction.';}
  }
  async function loadCase(id) {
    const token=++loadVersion,item=cases.find(c=>c.id===id)||cases[0];
    ready=false;busy=false;workerError=null;if(worker){worker.terminate();worker=null;}controls();clearStateDisplay();status('Loading exact surface data…');
    try {
      const res=await fetch(item.path);if(!res.ok)throw new Error(`Surface file unavailable (${res.status}).`);
      const data=Q.normalizeModel(await res.json());if(token!==loadVersion)return;model=data;
      selected=0;check=null;circuit=model.prepare_circuit.slice();cursor=0;
      const qubitLabel=' · '+model.n+' qubits';
      $('qModelTitle').textContent=model.label.endsWith(qubitLabel)?model.label:model.label+qubitLabel;
      $('qMode').textContent=item.browserLive?'LIVE BROWSER · FLOAT64':'COMBINATORIAL CASE · RECORDED RUNS';
      $('executionBadge').textContent=item.browserLive?'18-qubit live worker':'No dense browser allocation';
      $('recordedOnlyNotice').hidden=item.browserLive;
      $('modelDownload').href=item.path;
      for(const id of ['selectedQubit','gateTarget','gateControl']) {
        $(id).replaceChildren(...model.edges.map(e=>elem('option',wireName(e.id)+' · '+e.label,{value:e.id})));
      }
      $('gateControl').value='1';
      const metadata=model.metadata,dist=model.distance_certificate;
      const stats=[['Data qubits n',model.n],['Genus g',model.genus],['Logical qubits k',metadata.k],['V − E + F',metadata.chi],['Ranks X / Z',metadata.rankX+' / '+metadata.rankZ],['Faces / vertices',metadata.F+' / '+metadata.V]];
      $('topologyStats').replaceChildren(...stats.map(([k,v])=>{const d=elem('div');d.append(elem('span',k),elem('strong',v));return d;}));
      $('dessinSummary').textContent=`This connected clean dessin has ${metadata.dessin_degree} darts, ${metadata.V} black vertices, ${model.n} white vertices and ${metadata.F} faces. Rank method: ${metadata.rank_method}. The generated data check closed oriented incidences, connectedness, single-cycle vertex links, and HX HZᵀ = 0.`;
      const p=model.permutations||{};
      $('permutationData').textContent=JSON.stringify({convention:p.composition,meaning:p.meaning,sigma0_cycles:p.black_cycles,sigma1_cycles:p.white_cycles,face_cycles:p.face_cycles,distance_certificate:dist},null,2);
      const torus=model.kind==='square_torus';
      [...$('surfaceView').options].forEach(o=>o.disabled=!torus&&o.value!=='graph');
      $('surfaceView').value=torus?'torus':'graph';
      $('geometryCaveat').textContent=torus?'The 3D torus uses the explicit periodic map ((2 + 0.7 cos v) cos u, (2 + 0.7 cos v) sin u, 0.7 sin v). The drawing preserves the graph incidences and surface topology. It is not a computed conformal metric or Belyi map.':'The displayed graph is a combinatorial layout with crossings; those crossings do not create vertices. Genus is established by the oriented rotation system and Euler characteristic, not by this planar drawing. The paired polygon is a topological schema, not an analytic uniformization or an explicit Belyi map.';
      $('selectedCheck').textContent='Select a stabilizer below to highlight its qubits.';
      drawPolygon();selectQubit(0);drawCircuit();
      $('timelineStart').max=Math.max(0,circuit.length-12);$('timelineStart').value='0';
      if(!item.browserLive) {
        status('Exact topology and circuit loaded. This case does not allocate a dense browser state vector.');
        $('trainingStatus').textContent='The trainable browser circuit uses the 18-qubit case. Select the 3 × 3 torus to execute it.';
        renderPredictions([]);controls();return;
      }
      status('Preparing a reference state and checking all 18 stabilizers in the worker…');
      worker=new Worker(new URL('quantum-worker.js',location.href));
      worker.onmessage=onWorker;
      worker.onerror=e=>{ready=false;busy=false;status('Worker error: '+e.message);controls();};
      post('init',{model});
      $('trainingStatus').textContent='Training uses four fixed examples, step size 0.2 and exact parameter-shift derivatives.';
    } catch(error) {status(error.message);ready=false;controls();}
  }
  function onWorker(event) {
    const m=event.data;
    if(m.type==='ready') {
      ready=true;status(`Ready. Reference preparation residual ${m.baseResidual.toExponential(2)}. Current state is |0⟩⊗18; prepare or step the circuit.`);
      $('patchLabel').textContent=m.patch.map(wireName).join(', ');controls();
    }
    if(m.type==='busy') {busy=true;busyMode=m.mode;workerError=null;controls();status(m.mode==='train'?'Computing parameter-shift gradients in the worker…':'Executing circuit gates in the worker…');}
    if(m.type==='idle') {busy=false;busyMode=null;controls();if(!workerError)status(ready?'Ready. Displayed quantities were computed from the current state vector.':'The worker has not completed initialization.');}
    if(m.type==='error') {workerError=m.message;status('Computation stopped: '+m.message);$('trainingStatus').textContent=m.message;}
    if(m.type==='snapshot') {
      cursor=m.cursor;circuit=m.circuit;
      const windowStart=Number($('timelineStart').value);
      if(cursor<windowStart||cursor>windowStart+12)$('timelineStart').value=Math.min(Math.max(0,cursor-6),Math.max(0,circuit.length-12));
      $('timelineStart').max=Math.max(0,circuit.length-12);
      $('gateStatus').textContent=`Applied ${cursor} / ${circuit.length} gates${cursor<circuit.length?' · next: '+gateLabel(circuit[cursor]):' · circuit complete'}.`;
      $('stateNorm').textContent=number(m.stats.norm2,10);$('stateFidelity').textContent=number(m.fidelity,8);
      $('stateSupport').textContent=m.stats.support.toLocaleString();$('stateEntropy').textContent=number(m.stats.entropy,5)+' bits';
      renderChecks(m.checks);drawWeights(m.stats.hamming);drawCircuit();
      $('amplitudeRows').replaceChildren(...m.stats.top.map(r=>{const tr=elem('tr');tr.append(elem('td',r.basis),elem('td',number(r.probability,8)),elem('td',number(r.phase,5)));return tr;}));
    }
    if(m.type==='prediction')$('predictionStatus').textContent=`Measured ⟨Z⟩ = ${number(m.value,8)} · target ${m.target>0?'+1':'−1'} · input (${m.signs.map(x=>x>0?'+':'−').join(', ')}).`;
    if(m.type==='training') {
      setTheta(m.theta);history=m.history;drawLoss();renderPredictions(m.rows);
      $('trainingStatus').textContent=`Step ${m.epoch} / ${m.steps}: measured training MSE ${m.loss.toExponential(4)}.`;
    }
    if(m.type==='trained') {
      setTheta(m.theta);history=m.history;drawLoss();renderPredictions(m.rows);
      const held=m.rows.filter(r=>!r.training),heldMSE=Q.mse(held);
      $('trainingStatus').textContent=`${m.stopped?'Stopped after':'Completed'} ${history.length-1} updates in ${(m.elapsedMs/1000).toFixed(2)} s. Held-out MSE over 12 inputs: ${heldMSE.toExponential(4)}.`;
      $('predictionStatus').textContent='Angles updated. Run a sample to display its full circuit and current state.';
    }
  }
  function renderChecks(rows) {
    $('checkRows').replaceChildren(...rows.map(r=>{
      const tr=elem('tr');if(r.value<-.999999)tr.classList.add('check-negative');if(check&&check.id===r.id)tr.classList.add('check-highlight');
      const td=elem('td'),b=elem('button',r.id+' · '+r.kind,{type:'button','aria-label':`Highlight ${r.id}, ${r.kind} on qubits ${r.qubits.join(', ')}`});
      b.addEventListener('click',()=>{check=r;$('selectedCheck').textContent=`${r.id} = ${r.qubits.map(q=>r.kind+wireName(q)).join(' · ')}. Highlighted edges are its support.`;drawSurface();renderChecks(rows);});td.append(b);
      const state=Math.abs(r.value-1)<1e-7?'+1 eigenstate':Math.abs(r.value+1)<1e-7?'−1 eigenstate':'mixed outcomes';
      tr.append(td,elem('td',number(r.value,6)),elem('td',number(Math.max(0,Math.min(1,(1-r.value)/2)),6)),elem('td',state));return tr;
    }));
  }
  function gateLabel(g) {const qs=Q.gateQubits(g);return `${g.gate} ${qs.map(wireName).join(' → ')}${g.angle==null?'':` (${number(g.angle,3)} rad)`}`;}
  function drawCircuit() {
    if(!model)return;const svg=$('circuitSvg');svg.replaceChildren();
    if(model.n>64||!circuit.length) {svg.setAttribute('viewBox','0 0 850 150');txt(svg,30,60,'Topology-only case: no dense preparation circuit is bundled.',{'font-size':16});txt(svg,30,92,`n = ${model.n}; inspect the checked incidence and permutation data above.`);return;}
    const start=Number($('timelineStart').value)||0,count=12,row=23,left=67,top=43,w=850,h=top+model.n*row+27;
    svg.setAttribute('viewBox',`0 0 ${w} ${h}`);$('timelineStartOut').textContent=`${start+1}–${Math.min(start+count,circuit.length)}`;
    for(let q=0;q<model.n;q++) {const y=top+q*row;if(q===selected)svg.append(sv('rect',{x:0,y:y-10,width:w,height:21,fill:'#f7e9d5'}));line(svg,left,y,w-18,y);txt(svg,18,y+4,wireName(q),{'font-family':'monospace',fill:q===selected?C.ochre:C.ink});}
    circuit.slice(start,start+count).forEach((g,i)=>{
      const index=start+i,x=left+31+i*59,qs=Q.gateQubits(g),target=qs[qs.length-1],y=top+target*row,done=index<cursor;
      txt(svg,x,18,String(index+1),{'text-anchor':'middle','font-size':9,fill:done?C.teal:C.muted});
      if(index===cursor)svg.append(sv('rect',{x:x-24,y:25,width:48,height:model.n*row+13,fill:'#e6efea',opacity:.7}));
      const color=done?C.teal:C.ink;
      if(qs.length===2) {const yc=top+qs[0]*row;line(svg,x,yc,x,y,{stroke:color,'stroke-width':1.5});svg.append(sv('circle',{cx:x,cy:yc,r:3.5,fill:color}));}
      if(g.gate==='CX'||g.gate==='CNOT') {svg.append(sv('circle',{cx:x,cy:y,r:8,fill:'#fff',stroke:color,'stroke-width':1.5}));line(svg,x-6,y,x+6,y,{stroke:color});line(svg,x,y-6,x,y+6,{stroke:color});}
      else {svg.append(sv('rect',{x:x-17,y:y-9,width:34,height:18,rx:2,fill:done?'#e6efea':'#fff',stroke:color}));txt(svg,x,y+3.5,g.gate==='CZ'?'Z':g.gate,{'text-anchor':'middle','font-size':10,fill:color});}
      const title=sv('title',{},gateLabel(g));svg.lastChild.append(title);
    });
    txt(svg,18,h-7,`Window ${start+1}–${Math.min(start+count,circuit.length)} / ${circuit.length} gates. Green gates have been applied.`,{'font-size':9,fill:C.muted});
  }
  function canvasSetup() {
    const canvas=$('surfaceCanvas'),r=canvas.getBoundingClientRect(),dpr=Math.min(2,devicePixelRatio||1);
    canvas.width=Math.round(r.width*dpr);canvas.height=Math.round(r.height*dpr);
    const ctx=canvas.getContext('2d');ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,r.width,r.height);
    return {ctx,w:r.width,h:r.height};
  }
  function drawSurface() {
    if(!model)return;const {ctx,w,h}=canvasSetup();if(!w||!h)return;points=[];
    const mode=$('surfaceView').value;const is3=mode==='torus';$('cameraControls').hidden=!is3;
    $('geometryLabel').textContent=is3?'Explicit periodic torus embedding':mode==='domain'?'Opposite sides are identified':'Combinatorial layout; crossings are not vertices';
    const edgeColor=e=>e.id===selected?C.ochre:check&&check.qubits.includes(e.id)?C.teal:'#8ba79b';
    const edgeWidth=e=>e.id===selected?3.4:check&&check.qubits.includes(e.id)?2.7:1.1;
    function point(x,y,id,white,depth=0) {
      const active=id===selected&&white,r=active?6:model.n>100?(white?1.8:2.1):(white?4.5:3.4);
      ctx.beginPath();ctx.arc(x,y,r,0,2*Math.PI);ctx.fillStyle=white?'#fff':C.ink;ctx.fill();ctx.strokeStyle=active?C.ochre:white?C.teal:C.ink;ctx.lineWidth=active?2.8:1.3;ctx.stroke();
      if(white){points.push({x,y,id});if(model.n<=46||active){ctx.font=active?'bold 10px Arial':'9px Arial';ctx.fillStyle=active?C.ochre:C.muted;ctx.fillText('q'+id,x+7,y-7);}}
    }
    if(is3) {
      const [lx,ly]=model.dimensions,cy=Math.cos(yaw*Math.PI/180),sy=Math.sin(yaw*Math.PI/180),cp=Math.cos(pitch*Math.PI/180),sp=Math.sin(pitch*Math.PI/180),scale=Math.min(w/7,h/5.4);
      const T=(x,y)=>{const u=2*Math.PI*x/lx,v=2*Math.PI*y/ly,R=2+.7*Math.cos(v);return[R*Math.cos(u),R*Math.sin(u),.7*Math.sin(v)];};
      const project=p=>{const x=p[0]*cy-p[1]*sy,y=p[0]*sy+p[1]*cy,z=y*sp+p[2]*cp,k=8/(8-z);return{x:w/2+x*scale*k,y:h/2+(y*cp-p[2]*sp)*scale*k,z};};
      const parts=[];
      for(const e of model.edges) for(let i=0;i<10;i++) {
        const horizontal=e.orientation==='h',t0=(i/10-.5),t1=((i+1)/10-.5);
        const a=project(T(e.x+(horizontal?t0:0),e.y+(horizontal?0:t0))),b=project(T(e.x+(horizontal?t1:0),e.y+(horizontal?0:t1)));
        parts.push({a,b,e,z:(a.z+b.z)/2});
      }
      parts.sort((a,b)=>a.z-b.z);
      for(const s of parts){ctx.beginPath();ctx.moveTo(s.a.x,s.a.y);ctx.lineTo(s.b.x,s.b.y);ctx.strokeStyle=edgeColor(s.e);ctx.lineWidth=edgeWidth(s.e);ctx.globalAlpha=s.e.id===selected?1:.4+.6*(s.z+3)/6;ctx.stroke();}ctx.globalAlpha=1;
      const marks=model.vertices.map(v=>({...project(v.position3d),id:v.id,white:false})).concat(model.edges.map(e=>({...project(e.position3d),id:e.id,white:true}))).sort((a,b)=>a.z-b.z);
      marks.forEach(p=>point(p.x,p.y,p.id,p.white,p.z));
    } else if(mode==='domain') {
      const [lx,ly]=model.dimensions,pad=35,scale=Math.min((w-2*pad)/lx,(h-2*pad)/ly),ox=(w-scale*lx)/2,oy=(h-scale*ly)/2;
      const P=(x,y)=>[ox+x*scale,oy+y*scale];
      ctx.strokeStyle=C.ochre;ctx.setLineDash([5,4]);ctx.strokeRect(ox,oy,lx*scale,ly*scale);ctx.setLineDash([]);
      for(const e of model.edges){const hor=e.orientation==='h',a=P(e.x-(hor?.5:0),e.y-(hor?0:.5)),b=P(e.x+(hor?.5:0),e.y+(hor?0:.5));ctx.beginPath();ctx.moveTo(...a);ctx.lineTo(...b);ctx.strokeStyle=edgeColor(e);ctx.lineWidth=edgeWidth(e);ctx.stroke();}
      for(let y=0;y<=ly;y++)for(let x=0;x<=lx;x++){const p=P(x,y);ctx.globalAlpha=(x===lx||y===ly)?.4:1;point(...p,(y%ly)*lx+x%lx,false);}ctx.globalAlpha=1;
      model.edges.forEach(e=>point(...P(e.x,e.y),e.id,true));
      ctx.font='10px Arial';ctx.fillStyle=C.muted;ctx.fillText('u = 0',ox,oy-14);ctx.fillText('u = 1',ox+lx*scale-27,oy-14);ctx.fillText('Opposite boundary sites represent the same vertices.',12,h-5);
    } else {
      const R=Math.min(w,h)*.37,vertices=model.vertices.map((v,i)=>({x:w/2+R*Math.cos(2*Math.PI*i/model.vertices.length-Math.PI/2),y:h/2+R*Math.sin(2*Math.PI*i/model.vertices.length-Math.PI/2),id:v.id}));
      for(const e of model.edges){const a=vertices[e.u],b=vertices[e.v],dx=b.x-a.x,dy=b.y-a.y,L=Math.hypot(dx,dy)||1,offset=(e.id%5-2)*9,mx=(a.x+b.x)/2-dy/L*offset,my=(a.y+b.y)/2+dx/L*offset;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.quadraticCurveTo(mx,my,b.x,b.y);ctx.strokeStyle=edgeColor(e);ctx.lineWidth=edgeWidth(e);ctx.stroke();point(.25*a.x+.5*mx+.25*b.x,.25*a.y+.5*my+.25*b.y,e.id,true);}
      vertices.forEach(v=>point(v.x,v.y,v.id,false));
    }
  }
  function drawPolygon() {
    const svg=$('polygonSvg');svg.replaceChildren();const n=4*model.genus,cx=155,cy=110,R=75;
    const ps=Array.from({length:n},(_,i)=>[cx+R*Math.cos(2*Math.PI*i/n-Math.PI/2),cy+R*Math.sin(2*Math.PI*i/n-Math.PI/2)]);
    svg.append(sv('polygon',{points:ps.map(p=>p.join(',')).join(' '),fill:'#edf1eb',stroke:C.line}));
    for(let i=0;i<n;i++){const a=ps[i],b=ps[(i+1)%n],handle=Math.floor(i/4)+1,j=i%4,label=(j%2?'b':'a')+handle+(j>=2?'⁻¹':'');line(svg,a[0],a[1],b[0],b[1],{stroke:j%2?C.ochre:C.teal,'stroke-width':2});const mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2,dx=mx-cx,dy=my-cy,L=Math.hypot(dx,dy);txt(svg,mx+dx/L*18,my+dy/L*18+4,label,{'text-anchor':'middle','font-size':11});}
    txt(svg,cx,cy+4,'g = '+model.genus,{'text-anchor':'middle','font-size':17,fill:C.teal});
    $('polygonCaption').textContent=`Canonical ${n}-gon with word ${Array.from({length:model.genus},(_,i)=>`a${i+1} b${i+1} a${i+1}⁻¹ b${i+1}⁻¹`).join(' ')}. This is a topological schema.`;
  }
  function drawWeights(values) {
    const svg=$('weightSvg');svg.replaceChildren();if(!values.length){txt(svg,30,110,'Execute a live circuit to populate the distribution.',{'font-size':12,fill:C.muted});return;}
    const max=Math.max(.05,...values),left=43,top=25,bottom=210,width=442;
    for(let i=0;i<=4;i++){const p=max*i/4,y=bottom-(bottom-top)*i/4;line(svg,left,y,495,y);txt(svg,left-7,y+3,number(p,2),{'text-anchor':'end','font-size':9,fill:C.muted});}
    values.forEach((p,i)=>{const bw=width/values.length,x=left+i*bw+2,h=(bottom-top)*p/max;svg.append(sv('rect',{x,y:bottom-h,width:bw-4,height:Math.max(0,h),fill:C.teal}));if(i%2===0)txt(svg,x+(bw-4)/2,bottom+17,String(i),{'text-anchor':'middle','font-size':9});});
    txt(svg,265,244,'Number of 1 bits',{'text-anchor':'middle','font-size':10,fill:C.muted});txt(svg,43,13,'Probability',{'font-size':10,fill:C.muted});
  }
  function drawLoss() {drawLossSeries($('lossSvg'),history,'Measured training MSE');}
  function drawLossSeries(svg,rows,label) {
    svg.replaceChildren();if(!rows.length){txt(svg,35,130,'Run training to compute a loss trajectory.',{'font-size':13,fill:C.muted});return;}
    const data=rows.map(r=>({epoch:r.epoch??r.step,loss:r.loss}));
    const left=50,right=490,top=30,bottom=225,max=Math.max(.001,...data.map(r=>r.loss))*1.08,last=Math.max(1,data[data.length-1].epoch);
    for(let i=0;i<=4;i++){const y=bottom-(bottom-top)*i/4;line(svg,left,y,right,y);txt(svg,left-8,y+4,number(max*i/4,3),{'text-anchor':'end','font-size':9,fill:C.muted});}
    const points=data.map(r=>[left+(right-left)*r.epoch/last,bottom-(bottom-top)*r.loss/max]);svg.append(sv('polyline',{points:points.map(p=>p.join(',')).join(' '),fill:'none',stroke:C.teal,'stroke-width':2.5}));points.forEach(p=>svg.append(sv('circle',{cx:p[0],cy:p[1],r:3.3,fill:C.teal})));
    for(let i=0;i<=last;i++)if(last<13||i%2===0)txt(svg,left+(right-left)*i/last,bottom+17,String(i),{'text-anchor':'middle','font-size':9});
    txt(svg,270,268,'Gradient updates',{'text-anchor':'middle','font-size':10,fill:C.muted});txt(svg,50,16,label,{'font-size':10,fill:C.muted});
  }
  function renderPredictions(rows) {
    const all=Q.allSigns();$('predictionRows').replaceChildren(...all.map(signs=>{
      const row=rows.find(r=>r.signs.every((v,i)=>v===signs[i])),training=Q.trainingSigns.some(s=>s.every((v,i)=>v===signs[i])),tr=elem('tr');
      tr.append(elem('td',signs.map(x=>x>0?'+':'−').join(' ')),elem('td',training?'train':'held out'),elem('td',Q.parityLabel(signs)>0?'+1':'−1'),elem('td',row?number(row.prediction,6):'—'));return tr;
    }));
  }
  function renderRecorded() {
    const entries=Object.entries(latestRecords);
    $('runRecord').textContent=entries.length?JSON.stringify(latestRecords,null,2):'No GPU execution record is bundled yet. The live browser worker can still run the 18-qubit case.';
    $('recordLinks').replaceChildren(...entries.map(([name])=>{const p=elem('p');p.append(elem('a','Download '+name,{href:'data/'+name}));return p;}));
    $('recordedStatus').textContent=entries.length?`${entries.length} execution record${entries.length>1?'s':''} loaded. Values below come from those files; inspect the complete records for method and limitations.`:'No GPU run record has been bundled with this page yet. No GPU timing or success claim is shown.';
    const gpu=latestRecords['gpu-results.json'];$('gpuSummary').replaceChildren();
    const memory=b=>b>=2**30?number(b/2**30,3)+' GiB':b>=2**20?number(b/2**20,3)+' MiB':Number(b).toLocaleString()+' bytes';
    const seconds=s=>Number(s).toFixed(6)+' s';
    const addFields=(card,fields)=>{const dl=elem('dl');for(const[k,v]of fields)if(v!=null)dl.append(elem('dt',k),elem('dd',String(v)));card.append(dl);};
    if(gpu) {
      const runs=gpu.experiments||[],env=gpu.environment||{},passed=runs.filter(r=>r.passed===true).length;
      $('recordedStatus').textContent=`The saved GPU run reports ${passed} / ${runs.length} experiment checks passed on ${env.gpu||'the recorded GPU'}. Dense amplitudes and Pauli-error frames are shown as separate representations.`;
      $('gpuSummary').append(elem('p',`${gpu.utc_started} to ${gpu.utc_finished} · cuQuantum ${env.packages?.['cuquantum-python-cu12']||'version in record'} · script SHA-256 ${env.script_sha256||'not recorded'}`,{class:'q-small'}));
      const dense=runs.filter(r=>String(r.representation||'').startsWith('dense'));
      if(dense.length){
        $('gpuSummary').append(elem('h3','Dense state-vector execution',{class:'q-run-heading'}),elem('p','These experiments allocate the full complex64 amplitude vector. Their state storage grows exponentially with the total register size. The reported checks compare measured stabilizer expectations with the exact Pauli-error prediction.',{class:'q-small'}));
        const grid=elem('div',null,{class:'q-run-grid'});
        for(const r of dense){const card=elem('article',null,{class:'q-run-card'});card.append(elem('span',r.passed?'RECORDED CHECKS PASSED':'RECORDED CHECKS FAILED',{class:'status-tag'}),elem('h3',r.total_qubits+' qubits · dense'),elem('p',r.backend));addFields(card,[['Register',`${r.data_qubits} data + ${r.ancillas} ancilla${r.ancillas===1?'':'s'}`],['Amplitude storage',memory(r.state_bytes)+' · complex64'],['Gates applied',`${r.gates_applied} (${r.preparation_gates} preparation)`],['Preparation time',seconds(r.preparation_seconds)],['Recorded experiment time',seconds(r.total_wall_seconds)],['Largest stabilizer discrepancy',r.max_stabilizer_error.toExponential(3)],['Measured ancilla ⟨Z⟩',r.syndrome_ancilla_Z==null?null:number(r.syndrome_ancilla_Z,8)]]);grid.append(card);}
        $('gpuSummary').append(grid);
      }
      const frames=runs.filter(r=>String(r.representation||'').startsWith('Pauli-error frames'));
      if(frames.length){
        $('gpuSummary').append(elem('h3','Clifford Pauli-error-frame execution',{class:'q-run-heading'}),elem('p','These runs propagate sampled Pauli errors relative to a known encoded stabilizer reference. They do not allocate a full amplitude vector or execute the non-Clifford variational model at these register sizes. Each run uses independent X and Z error probability 0.001 and checks every reported syndrome byte.',{class:'q-small'}));
        const grid=elem('div',null,{class:'q-run-grid q-frame-grid'});
        for(const r of frames){const card=elem('article',null,{class:'q-run-card'});card.append(elem('span',r.passed?'RECORDED CHECKS PASSED':'RECORDED CHECKS FAILED',{class:'status-tag'}),elem('h3',r.data_qubits.toLocaleString()+' data qubits'),elem('p',`${r.backend} · genus ${r.genus} · ${r.case}`));addFields(card,[['Register',`${r.data_qubits.toLocaleString()} data + ${r.ancilla_qubits.toLocaleString()} ancillas = ${r.total_qubits.toLocaleString()} total`],['Sampled shots',r.shots.toLocaleString()],['Estimated packed tables',memory(r.bit_table_bytes)],['Setup / synchronized apply',seconds(r.setup_seconds)+' / '+seconds(r.simulation_seconds)],['Recorded experiment time',seconds(r.total_wall_seconds)],['Syndrome events',r.syndrome_events.toLocaleString()],['Syndrome event fraction',number(r.syndrome_rate,8)],['Syndrome bytes checked',memory(r.all_syndrome_bytes_checked)],['Byte mismatches',r.syndrome_byte_mismatches]]);card.append(elem('p',r.claim_limit,{class:'q-small'}));grid.append(card);}
        $('gpuSummary').append(grid);
      }
      const bell=runs.find(r=>r.name==='bell_smoke');
      if(bell)$('gpuSummary').append(elem('p',`A separate ${bell.n}-qubit Bell smoke check ${bell.passed?'passed':'failed'}; its amplitudes and XX/ZZ expectations are retained in the raw record. Apply times are synchronized wall intervals including host dispatch, not isolated CUDA kernel timings. Setup and the timed experiment body are distinct; estimated packed tables are not measured peak memory.`,{class:'q-small'}));
    }
    const capacity=latestRecords['capacity-results.json'];
    if(capacity) {
      const runs=Array.isArray(capacity.experiments)?capacity.experiments:[],frameRuns=runs.filter(r=>r.data_qubits!=null&&r.total_qubits!=null);
      $('gpuSummary').append(elem('h3','Separate capacity follow-up',{class:'q-run-heading'}),elem('p','This later run retains its own provenance and memory-budget selection. It reports additional higher-genus and large torus Pauli-error-frame workloads. A largest tested workload is not a universal hardware qubit limit. Table storage is estimated, not a measured peak. The synchronized apply interval includes host dispatch; the full call additionally includes topology and cleanup.',{class:'q-small'}));
      const passed=frameRuns.filter(r=>r.passed===true),largest=passed.reduce((a,b)=>!a||b.total_qubits>a.total_qubits?b:a,null);
      if(largest)$('gpuSummary').append(elem('p',`Largest tested Pauli-frame workload in this follow-up: ${largest.data_qubits.toLocaleString()} data + ${(largest.ancilla_qubits??largest.ancillas??0).toLocaleString()} ancillas = ${largest.total_qubits.toLocaleString()} total qubits, at ${Number(largest.shots).toLocaleString()} shots.`,{class:'q-notice'}));
      const grid=elem('div',null,{class:'q-run-grid q-frame-grid'});
      for(const r of frameRuns){const card=elem('article',null,{class:'q-run-card'});card.append(elem('span',r.passed?'RECORDED CHECKS PASSED':'RECORDED STATUS: '+(r.status||'NOT PASSED'),{class:'status-tag'}),elem('h3',r.data_qubits.toLocaleString()+' data qubits'),elem('p',`${r.backend||'Backend in raw record'} · genus ${r.genus??'in record'} · ${r.case||r.name||''}`));addFields(card,[['Register',`${r.data_qubits.toLocaleString()} data + ${(r.ancilla_qubits??r.ancillas??0).toLocaleString()} ancillas = ${r.total_qubits.toLocaleString()} total`],['Representation',r.representation],['Shots',r.shots?.toLocaleString()],['Estimated packed tables',r.bit_table_bytes==null?null:memory(r.bit_table_bytes)],['Setup time',r.setup_seconds==null?null:seconds(r.setup_seconds)],['Synchronized apply interval',r.simulation_seconds==null?null:seconds(r.simulation_seconds)],['Timed body',r.total_wall_seconds==null?null:seconds(r.total_wall_seconds)],['Full call including topology / cleanup',r.call_wall_seconds_including_topology_and_cleanup==null?null:seconds(r.call_wall_seconds_including_topology_and_cleanup)],['Syndrome bytes checked',r.all_syndrome_bytes_checked==null?null:memory(r.all_syndrome_bytes_checked)],['Byte mismatches',r.syndrome_byte_mismatches],['Seed',r.seed??capacity.seed]]);if(r.claim_limit)card.append(elem('p',r.claim_limit,{class:'q-small'}));grid.append(card);}
      $('gpuSummary').append(grid,elem('p','Download capacity-results.json below for the available-memory snapshot, selection rationale, run intervals and exact source identifiers.',{class:'q-small'}));
    }
    const trained=latestRecords['qnn-training.json'];$('gpuTraining').replaceChildren();
    if(trained) {
      const box=elem('div',null,{class:'q-notice'});box.append(elem('strong','Recorded GPU training · 18-qubit dense state'));
      const initial=trained.initial_theta??trained.initialTheta,final=trained.final_theta??trained.finalTheta;
      if(initial)box.append(elem('p','Initial θ: '+initial.map(x=>number(x,6)).join(', ')));
      if(final)box.append(elem('p','Final θ: '+final.map(x=>number(x,6)).join(', ')));
      const first=trained.history?.[0],last=trained.history?.[trained.history.length-1];
      if(first&&last)box.append(elem('p',`${trained.steps} updates · training MSE ${number(first.loss,8)} → ${number(last.loss,8)} · recorded wall time ${seconds(trained.wall_seconds)} · largest analytic-reference discrepancy ${trained.max_analytic_prediction_error.toExponential(3)}.`));
      const p=elem('p','The initial sign accuracy is already 100% on this tiny truth table. Training calibrates the expectation magnitude; the reported improvement is in mean squared error. This recorded GPU session remains separate from your browser session.');box.append(p);
      if(final&&final.length===4){const b=elem('button','Load recorded angles into the live controls',{class:'button secondary',type:'button','data-parameter-action':''});b.disabled=busy;b.addEventListener('click',()=>{if(!busy)setTheta(final,true);});box.append(b);}
      $('gpuTraining').append(elem('h3','Recorded variational-circuit training',{class:'q-run-heading'}),box);
      if(trained.history?.length){const layout=elem('div',null,{class:'q-measure-grid'}),plot=elem('div'),chart=sv('svg',{viewBox:'0 0 510 280',role:'img','aria-label':'Recorded GPU training mean squared error over twenty-four gradient updates'});plot.append(chart);drawLossSeries(chart,trained.history,'Recorded GPU training MSE');plot.append(elem('p','The displayed points are the saved GPU history, not the live worker trajectory.',{class:'q-small'}));const summary=elem('div');summary.append(elem('h3','Complete sixteen-input check'));const table=elem('table'),thead=elem('thead'),hr=elem('tr');['Input','Split','Target','GPU prediction'].forEach(x=>hr.append(elem('th',x)));thead.append(hr);const tbody=elem('tbody');for(const r of trained.truth_table||[]){const tr=elem('tr');tr.append(elem('td',r.signs.map(s=>s>0?'+':'−').join(' ')),elem('td',r.used_in_training?'train':'held out'),elem('td',String(r.target)),elem('td',number(r.prediction,8)));tbody.append(tr);}table.append(thead,tbody);const scroll=elem('div',null,{class:'q-table-scroll'});scroll.append(table);summary.append(scroll);layout.append(plot,summary);$('gpuTraining').append(layout);}
    }
  }
  async function loadRecords() {
    await Promise.all(['gpu-results.json','qnn-training.json','capacity-results.json'].map(async name=>{try{const r=await fetch('data/'+name);if(r.ok)latestRecords[name]=await r.json();}catch(_){/* Explicit pending state is rendered below. */}}));renderRecorded();
  }
  $('surfaceCase').addEventListener('change',e=>loadCase(e.target.value));
  $('surfaceView').addEventListener('change',drawSurface);$('selectedQubit').addEventListener('change',e=>selectQubit(e.target.value));
  $('gateTarget').addEventListener('change',e=>selectQubit(e.target.value));
  $('clearCheck').addEventListener('click',()=>{check=null;$('selectedCheck').textContent='Check highlight cleared.';document.querySelectorAll('.check-highlight').forEach(e=>e.classList.remove('check-highlight'));drawSurface();});
  for(const [id,key]of [['qYaw','yaw'],['qPitch','pitch']])$(id).addEventListener('input',e=>{if(key==='yaw')yaw=Number(e.target.value);else pitch=Number(e.target.value);$(id+'Out').textContent=e.target.value+'°';drawSurface();});
  $('timelineStart').addEventListener('input',drawCircuit);
  $('prepareCode').addEventListener('click',()=>post('prepare'));
  for(const[id,type]of [['stepGate','step'],['playCircuit','play'],['runCircuit','run'],['resetCircuit','reset'],['stopCircuit','stop']])$(id).addEventListener('click',()=>post(type));
  $('insertGate').addEventListener('click',()=>{
    const gate=$('gateKind').value.trim(),target=Number($('gateTarget').value),control=Number($('gateControl').value),angle=Number($('gateAngle').value),two=gate==='CX'||gate==='CZ';
    if(two&&target===control){status('Choose different qubits for the control and target.');return;}
    if(!Number.isFinite(angle)){status('Enter a finite rotation angle.');return;}
    post('append',{gate:{gate,target,...(two?{control}:{}),qubits:two?[control,target]:[target],...(gate==='RY'||gate==='RZ'?{angle}:{})}});
  });
  $('gateKind').addEventListener('change',()=>{const op=$('gateKind').value.trim();$('gateControl').disabled=op!=='CX'&&op!=='CZ';$('gateAngle').disabled=op!=='RY'&&op!=='RZ';});
  $('gateKind').dispatchEvent(new Event('change'));
  Q.allSigns().forEach((s,i)=>$('qnnSample').append(elem('option',s.map(x=>x>0?'+':'−').join(' ')+' · target '+(Q.parityLabel(s)>0?'+1':'−1'),{value:i})));
  for(let i=0;i<4;i++)$('theta'+i).addEventListener('input',e=>{const values=theta.slice();values[i]=Number(e.target.value);setTheta(values,true);});
  $('resetTheta').addEventListener('click',()=>setTheta(Q.initialTheta,true));
  $('runSample').addEventListener('click',()=>post('qnnRun',{theta,signs:Q.allSigns()[Number($('qnnSample').value)]}));
  $('trainQnn').addEventListener('click',()=>post('train',{theta,steps:Number($('trainSteps').value)}));
  $('stopTraining').addEventListener('click',()=>post('stop'));
  let drag=null;
  $('surfaceCanvas').addEventListener('pointerdown',e=>{if(e.pointerType==='mouse'){drag={x:e.clientX,y:e.clientY,startX:e.clientX,startY:e.clientY,moved:false};e.currentTarget.setPointerCapture(e.pointerId);}});
  $('surfaceCanvas').addEventListener('pointermove',e=>{if(!drag||$('surfaceView').value!=='torus')return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(e.clientX-drag.startX)+Math.abs(e.clientY-drag.startY)>4)drag.moved=true;if(drag.moved){yaw=((yaw+dx*.5+540)%360)-180;pitch=Math.max(-80,Math.min(80,pitch+dy*.4));$('qYaw').value=yaw;$('qPitch').value=pitch;$('qYawOut').textContent=Math.round(yaw)+'°';$('qPitchOut').textContent=Math.round(pitch)+'°';drawSurface();}drag.x=e.clientX;drag.y=e.clientY;});
  $('surfaceCanvas').addEventListener('pointerup',e=>{if(!drag||!drag.moved){const r=e.currentTarget.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;const p=points.reduce((best,p)=>Math.hypot(p.x-x,p.y-y)<(best?Math.hypot(best.x-x,best.y-y):14)?p:best,null);if(p)selectQubit(p.id);}drag=null;});
  for(const type of ['pointercancel','lostpointercapture'])$('surfaceCanvas').addEventListener(type,()=>{drag=null;});
  $('surfaceCanvas').addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)||$('surfaceView').value!=='torus')return;e.preventDefault();if(e.key==='ArrowLeft')yaw-=5;if(e.key==='ArrowRight')yaw+=5;if(e.key==='ArrowUp')pitch-=5;if(e.key==='ArrowDown')pitch+=5;yaw=((yaw+540)%360)-180;pitch=Math.max(-80,Math.min(80,pitch));$('qYaw').value=yaw;$('qPitch').value=pitch;$('qYawOut').textContent=yaw+'°';$('qPitchOut').textContent=pitch+'°';drawSurface();});
  if(typeof ResizeObserver!=='undefined')new ResizeObserver(()=>drawSurface()).observe($('surfaceCanvas'));
  window.addEventListener('resize',drawSurface);
  renderPredictions([]);drawLoss();drawWeights([]);controls();loadRecords();
  fetch('data/surface-cases.json').then(r=>{if(!r.ok)throw new Error('Case manifest unavailable.');return r.json();}).then(data=>{
    cases=data.cases;$('surfaceCase').replaceChildren(...cases.map(c=>elem('option',c.label+' · n='+c.n,{value:c.id})));return loadCase('torus3x3');
  }).catch(error=>status(error.message));
})();
