(function () {
  'use strict';
  const M = window.ResearchMath;
  if (!M) return;
  const $ = id => document.getElementById(id);
  const C = {teal: '#14695e', ochre: '#a65b19', ink: '#182b29', muted: '#596b64', line: '#d4ddd5', pale: '#e6efea', gold: '#f7e9d5'};
  const controls = [...document.querySelectorAll('[data-lab]')];
  const defaults = new Map(controls.map(c => [c.id, c.type === 'checkbox' ? c.checked : c.value]));
  const reports = {};
  const value = id => Number($(id).value);
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const fmt = (n, digits = 3) => {
    if (Math.abs(n) < 5e-13) n = 0;
    return Number(n.toFixed(digits)).toString().replace('-', '−');
  };
  const scientific = n => n === 0 ? '0' : n.toExponential(2).replace('e-', ' × 10⁻').replace('e+', ' × 10^');
  const tiny = n => n === 0 ? '0' : (Math.abs(n) < 0.001 ? n.toExponential(3) : fmt(n, 6));
  const set = (id, text) => { $(id).textContent = text; };
  const degrees = new Set(['torusYaw','torusPitch','coneXW','coneYZ','coneAlpha','coneBeta','coneYaw','conePitch']);
  function syncOutputs(lab) {
    controls.filter(c => c.dataset.lab === lab).forEach(c => {
      const out = $(c.id + 'Out');
      if (out) out.textContent = fmt(Number(c.value)) + (degrees.has(c.id) ? '°' : '');
    });
  }
  function saveState() {
    const changed = {};
    for (const c of controls) {
      const v = c.type === 'checkbox' ? c.checked : c.value;
      if (v !== defaults.get(c.id)) changed[c.id] = v;
    }
    return changed;
  }
  function readURL() {
    for (const c of controls) {
      if (c.type === 'checkbox') c.checked = defaults.get(c.id);
      else c.value = defaults.get(c.id);
    }
    try {
      const raw = new URL(location.href).searchParams.get('state');
      if (!raw || raw.length > 12000) return;
      const data = JSON.parse(raw);
      if (!data || typeof data !== 'object' || Array.isArray(data)) return;
      for (const c of controls) {
        if (!Object.hasOwn(data, c.id)) continue;
        if (c.type === 'checkbox') { if (typeof data[c.id] === 'boolean') c.checked = data[c.id]; }
        else if (c.tagName === 'SELECT') {
          if ([...c.options].some(o => o.value === String(data[c.id]))) c.value = String(data[c.id]);
        } else {
          const n = Number(data[c.id]);
          if (Number.isFinite(n)) c.value = String(clamp(n, Number(c.min), Number(c.max)));
        }
      }
    } catch (_) { /* Invalid shared state retains the documented defaults. */ }
  }
  function writeURL(push = true) {
    const url = new URL(location.href), state = saveState();
    if (Object.keys(state).length) url.searchParams.set('state', JSON.stringify(state));
    else url.searchParams.delete('state');
    if (url.href !== location.href) history[push ? 'pushState' : 'replaceState']({}, '', url);
  }

  function canvasContext(canvas) {
    const rect = canvas.getBoundingClientRect();
    const width = Math.max(1, rect.width), height = Math.max(1, rect.height);
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    const bw = Math.round(width * dpr), bh = Math.round(height * dpr);
    if (canvas.width !== bw || canvas.height !== bh) { canvas.width = bw; canvas.height = bh; }
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, width, height);
    return {ctx, width, height};
  }
  function surfaceLines(surface, fixed = 20, samples = 72) {
    const lines = [];
    for (let family = 0; family < 2; family++) for (let i = 0; i < fixed; i++) {
      for (let j = 0; j < samples; j++) {
        const a = i / fixed, b = j / samples, next = (j + 1) / samples;
        lines.push({a: family === 0 ? surface(b, a) : surface(a, b),
          b: family === 0 ? surface(next, a) : surface(a, next), family});
      }
    }
    return lines;
  }
  const torusLines = surfaceLines((u, v) => M.torusPoint(u, v), 18, 64);
  const coneLines = surfaceLines((a, b) => M.conePoint(M.TAU * a, M.TAU * b), 22, 64);
  function drawGeometry(canvas, lines, options) {
    const {ctx, width, height} = canvasContext(canvas);
    const yaw = M.radians(options.yaw), pitch = M.radians(options.pitch);
    const ca = Math.cos(yaw), sa = Math.sin(yaw), ce = Math.cos(pitch), se = Math.sin(pitch);
    const scale = options.kind === 'torus' ? Math.min(width * 0.165, height * 0.25)
      : Math.min(width * 0.31, height * (options.hero ? 0.39 : 0.35)) / Math.max(1, options.radius || 1);
    function project(p) {
      const horizontal = ca * p[0] - sa * p[1];
      const depth0 = sa * p[0] + ca * p[1];
      const vertical = se * depth0 - ce * p[2];
      const depth = ce * depth0 + se * p[2];
      const perspective = 8 / (8 - depth);
      return {x: width / 2 + scale * perspective * horizontal,
        y: height * 0.48 + scale * perspective * vertical, depth};
    }
    const transformed = lines.map(l => ({...l, p: project(l.a), q: project(l.b)}));
    transformed.sort((a, b) => a.p.depth + a.q.depth - b.p.depth - b.q.depth);
    for (const line of transformed) {
      const depth = (line.p.depth + line.q.depth) / 2;
      ctx.globalAlpha = clamp(0.58 + depth * 0.15, 0.2, 0.95);
      ctx.strokeStyle = line.family === 0 ? C.teal : C.ochre;
      ctx.lineWidth = options.hero ? 0.76 : 0.85;
      ctx.setLineDash(line.family === 1 ? [2.2, 1.9] : []);
      ctx.beginPath(); ctx.moveTo(line.p.x, line.p.y); ctx.lineTo(line.q.x, line.q.y); ctx.stroke();
    }
    ctx.globalAlpha = 1; ctx.setLineDash([]);
    if (options.axes) {
      const origin = project([0, 0, 0]);
      const length = options.kind === 'torus' ? 1.05 : 0.58;
      const basis = [[length,0,0],[0,length,0],[0,0,length]];
      basis.forEach((p, i) => {
        const end = project(p);
        ctx.strokeStyle = '#8da398'; ctx.lineWidth = 0.8;
        ctx.beginPath(); ctx.moveTo(origin.x, origin.y); ctx.lineTo(end.x, end.y); ctx.stroke();
        ctx.font = '10px Arial'; ctx.fillStyle = C.muted;
        ctx.fillText(['X','Y','Z'][i] + (options.kind === 'cone' ? '′' : ''), end.x + 4, end.y - 4);
      });
    }
    if (options.point) {
      const p = project(options.point);
      ctx.fillStyle = '#fff';ctx.beginPath();ctx.arc(p.x,p.y,7,0,M.TAU);ctx.fill();
      ctx.fillStyle = C.ochre;ctx.strokeStyle = C.ink;ctx.lineWidth = 1;
      ctx.beginPath();ctx.arc(p.x,p.y,4.5,0,M.TAU);ctx.fill();ctx.stroke();
      if (options.pointLabel) {
        ctx.font = '11px Arial'; ctx.fillStyle = C.ink;
        const w = ctx.measureText(options.pointLabel).width;
        const x = clamp(p.x + 12, 8, width - w - 8), y = clamp(p.y - 10, 18, height - 10);
        ctx.fillStyle = 'rgba(255,255,255,.93)';ctx.fillRect(x-4,y-13,w+8,19);
        ctx.fillStyle = C.ink;ctx.fillText(options.pointLabel,x,y);
      }
    }
    return project;
  }
  function projectConeLines(xw, yz, radius, projection) {
    const transform = p => M.coneProjection(p.map(x => radius * x), xw, yz, projection);
    return coneLines.map(l => ({...l, a: transform(l.a), b: transform(l.b)}));
  }
  function drawHero() {
    drawGeometry($('heroCanvas'), projectConeLines(M.radians(37), M.radians(-17), 1, 'perspective'),
      {yaw:-28,pitch:20,kind:'cone',hero:true,radius:1});
  }
  function svgSize(id, height) {
    const el = $(id), width = Math.max(310, el.getBoundingClientRect().width || 660);
    el.setAttribute('viewBox', `0 0 ${width} ${height}`);
    return {el, width, height};
  }
  const svgText = (x, y, text, size = 11, attrs = '') => `<text x="${x}" y="${y}" font-size="${size}" ${attrs}>${text}</text>`;

  function renderTorus() {
    syncOutputs('torus');
    const a = value('tauReal'), b = value('tauImag'), u = value('torusU'), v = value('torusV');
    const ub = M.mod(u,1), vb = M.mod(v,1);
    drawGeometry($('torusCanvas'), torusLines, {yaw:value('torusYaw'),pitch:value('torusPitch'),kind:'torus',axes:true,
      point:M.torusPoint(u,v),pointLabel:`(${fmt(ub,2)}, ${fmt(vb,2)}) mod ℤ²`});
    set('torus-summary', `z = ${fmt(u + a*v)} ${b*v >= 0 ? '+' : '−'} ${fmt(Math.abs(b*v))}i; representative (${fmt(ub)}, ${fmt(vb)}) in the lattice basis.`);
    set('torusArea', `${fmt(b)} = Im τ`);
    set('torusGram', `[[1, ${fmt(a)}], [${fmt(a)}, ${fmt(a*a+b*b)}]]`);
    const residual = M.torusSeamResidual();
    set('torusResidual', tiny(residual));
    const {el, width} = svgSize('periodSvg', 230);
    const s = Math.min(76, width/4), ox = width/2 - s/2 - a*s/2, oy = 194;
    const p = (x,y) => [ox+s*(x+a*y),oy-s*b*y];
    let body = '<title>Period parallelogram for the current tau</title>';
    const corners = [p(0,0),p(1,0),p(1,1),p(0,1)];
    body += `<polygon points="${corners.map(q=>q.join(',')).join(' ')}" fill="${C.pale}" stroke="${C.teal}" stroke-width="1.6"/>`;
    for (let t=.25;t<1;t+=.25) {
      const A=p(t,0),B=p(t,1),D=p(0,t),E=p(1,t);
      body += `<path d="M${A}L${B}M${D}L${E}" stroke="#b4c9bf" fill="none" stroke-width=".7"/>`;
    }
    const q = p(ub,vb), first=p(1,0), second=p(0,1);
    body+=`<circle cx="${q[0]}" cy="${q[1]}" r="5" fill="${C.ochre}" stroke="#fff" stroke-width="2"/>`;
    body+=svgText(ox-13,oy+17,'0',11)+svgText(first[0]+5,first[1]+17,'1',12)+svgText(second[0]-15,second[1]-10,'τ',15);
    body+=svgText(width/2,20,`τ = ${fmt(a)} + ${fmt(b)}i`,12,'text-anchor="middle" class="mono"');
    el.innerHTML=body;
    reports.torus = {tau:[a,b],coordinates:[u,v],representative:[ub,vb],area:b,seamResidual:residual};
  }
  function renderCone() {
    syncOutputs('cone');
    const radius=value('coneRadius'),alpha=M.radians(value('coneAlpha')),beta=M.radians(value('coneBeta'));
    const xw=M.radians(value('coneXW')),yz=M.radians(value('coneYZ')),projection=$('coneProjection').value;
    const original=M.conePoint(alpha,beta,radius), d=M.coneDiagnostics(original);
    drawGeometry($('coneCanvas'),projectConeLines(xw,yz,radius,projection),
      {yaw:value('coneYaw'),pitch:value('conePitch'),kind:'cone',radius,axes:true,
        point:M.coneProjection(original,xw,yz,projection),pointLabel:radius===0?'cone vertex':`ranks (${d.ranks.join(', ')})`});
    let maximum=0;
    for(const l of coneLines) maximum=Math.max(maximum,Math.abs(M.coneDiagnostics(l.a.map(x=>radius*x)).residual));
    set('cone-summary',`x = (${d.x.map(x=>fmt(x,4)).join(', ')}); y = (${d.y.map(x=>fmt(x,4)).join(', ')}). Squared radius = ${fmt(d.squaredRadius,5)}.`);
    set('coneResidual',tiny(Math.abs(d.residual)));set('coneMaxResidual',tiny(maximum));
    set('coneRanks',`(${d.ranks.join(', ')})`);set('coneHomology',`(${d.homology.join(', ')})`);
    reports.cone={...d,maxSampleResidual:maximum,projection,coordinateConvention:'diagnostics before view rotations'};
  }
  const curvePoints=M.ecPoints(), cyclic=Array.from({length:19},(_,k)=>M.ecMultiply(k,[5,1]));
  function additionExplanation(P) {
    const Q=[5,1], sum=M.ecAdd(P,Q);
    if(P===null)return 'Next addition: 𝒪 + P = P = (5, 1).';
    if(sum===null)return `Next addition: ${M.pointText(P)} + (5, 1) = 𝒪, because these points are inverses.`;
    const doubling=P[0]===5&&P[1]===1;
    const numerator=doubling?M.mod(3*P[0]*P[0]+2,17):M.mod(1-P[1],17);
    const denominator=doubling?M.mod(2*P[1],17):M.mod(5-P[0],17);
    const inv=M.inverse(denominator,17), slope=M.mod(numerator*inv,17);
    return `Next addition: λ = ${numerator} / ${denominator} = ${numerator}·${inv} = ${slope} mod 17; ${M.pointText(P)} + P = ${M.pointText(sum)}.`;
  }
  function renderElliptic() {
    syncOutputs('elliptic');const k=value('ecK'),selected=cyclic[k];
    const initialWidth=$('ecSvg').getBoundingClientRect().width||660, mobile=initialWidth<510;
    const {el,width}=svgSize('ecSvg',mobile?365:430), size=mobile?width-78:Math.min(350,width-240);
    const left=48,top=mobile?44:32,step=size/16,bottom=top+size;
    let body='<title>Elliptic curve points modulo seventeen</title><desc>E has eighteen affine points and one point at infinity. The selected point is '+M.pointText(selected)+'.</desc>';
    for(let n=0;n<=16;n++) {
      const x=left+n*step,y=bottom-n*step;
      body+=`<path d="M${x},${top}V${bottom}M${left},${y}H${left+size}" class="chart-grid"/>`;
      if(n%2===0){body+=svgText(x,bottom+19,n,10,'text-anchor="middle" class="muted"');body+=svgText(left-12,y+3,n,10,'text-anchor="end" class="muted"');}
    }
    body+=svgText(left+size+15,bottom+4,'x',13)+svgText(left-3,top-15,'y',13);
    for(const P of curvePoints) if(P){const x=left+P[0]*step,y=bottom-P[1]*step,is=selected&&P[0]===selected[0]&&P[1]===selected[1];body+=`<circle cx="${x}" cy="${y}" r="${is?7:3.8}" fill="${is?C.ochre:C.teal}" stroke="${is?C.ink:'#fff'}" stroke-width="${is?1.4:1}"/>`;}
    const bx=mobile?width-128:left+size+38,by=mobile?3:38,bw=mobile?112:Math.max(120,width-bx-10),bh=mobile?30:70;
    body+=`<rect x="${bx}" y="${by}" width="${bw}" height="${bh}" rx="2" fill="${selected===null?C.gold:C.pale}" stroke="${selected===null?C.ochre:C.line}"/>`;
    body+=svgText(bx+bw/2,by+(mobile?20:29),'𝒪 · infinity',mobile?11:15,'text-anchor="middle"');
    if(!mobile){body+=svgText(bx+bw/2,by+51,selected===null?'selected':'identity element',10,'text-anchor="middle" class="muted"');
      const cx=bx+bw/2,cy=260,r=48;
      body+=`<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${C.line}"/>`;
      for(let n=0;n<19;n++){const angle=M.TAU*n/19-Math.PI/2,x=cx+r*Math.cos(angle),y=cy+r*Math.sin(angle);body+=`<circle cx="${x}" cy="${y}" r="${n===k?5:2.4}" fill="${n===k?C.ochre:C.teal}"/>`;}
      body+=svgText(cx,cy+5,`k = ${k}`,15,'text-anchor="middle" class="mono"')+svgText(cx,cy+75,'cycle of scalar multiples',10,'text-anchor="middle" class="muted"');
      body+=svgText(cx,150,`${k}P = ${M.pointText(selected)}`,14,'text-anchor="middle" class="mono"');
    }
    body+=svgText(left+size/2,bottom+40,'residue coordinates in 𝔽₁₇',10,'text-anchor="middle" class="muted"');
    el.innerHTML=body;
    set('ec-summary',`[${k}]P = ${M.pointText(selected)}. Adding P gives [${(k+1)%19}]P = ${M.pointText(cyclic[(k+1)%19])}.`);
    set('ecAddition',additionExplanation(selected));
    $('ecTable').innerHTML=cyclic.map((P,n)=>`<tr${n===k?' class="selected"':''}><td>${n}</td><td>${M.pointText(P)}</td><td>${P?M.mod(P[1]**2-P[0]**3-2*P[0]-2,17):'point at infinity'}</td></tr>`).join('');
    reports.elliptic={k,point:selected,curveSize:curvePoints.length,order:19,field:17};
  }
  function renderFourier() {
    syncOutputs('fourier');const d=value('fourierD'),selectedU=value('fourierU'),data=M.fourierDistribution(d),selectedV=M.mod(d*selectedU,7);
    const rawWidth=$('fourierSvg').getBoundingClientRect().width||660,mobile=rawWidth<510;
    const {el,width}=svgSize('fourierSvg',mobile?330:390),cell=mobile?Math.min(36,(width-78)/7):42,left=48,top=mobile?36:29,size=7*cell;
    let body='<title>Fourier probabilities on the annihilator of the hidden subgroup</title><desc>Seven cells have probability one seventh; all other cells have probability zero.</desc>';
    for(const c of data.cells){const x=left+c.u*cell,y=top+(6-c.v)*cell,selected=c.u===selectedU&&c.v===selectedV;
      body+=`<rect x="${x+1}" y="${y+1}" width="${cell-2}" height="${cell-2}" rx="1" fill="${c.supported?C.teal:'#edf1eb'}" stroke="${selected?C.ochre:'#d4ddd5'}" stroke-width="${selected?3:0.5}"/>`;
      body+=svgText(x+cell/2,y+cell/2+4,c.supported?'1/7':'0',mobile?10:11,`text-anchor="middle" style="fill:${c.supported?'#fff':'#7a8c82'}"`);
    }
    for(let n=0;n<7;n++){body+=svgText(left+(n+.5)*cell,top+size+19,n,11,'text-anchor="middle"');body+=svgText(left-12,top+(6-n+.5)*cell+4,n,11,'text-anchor="end"');}
    body+=svgText(left+size+12,top+size+19,'u',13)+svgText(left-12,top-11,'v',13,'text-anchor="end"');
    if(!mobile){const x=left+size+33;body+=svgText(x,70,'ANNIHILATOR SUPPORT',9,`style="fill:${C.teal}" letter-spacing="1.2"`)+svgText(x,103,`v = ${d}u mod 7`,17,'class="mono"')+svgText(x,151,'Selected frequency',11,'class="muted"')+svgText(x,179,`(${selectedU}, ${selectedV})`,22,'class="mono"')+svgText(x,212,'Probability = 1/7',12);body+=svgText(x,263,selectedU===0?'Origin: no slope information':`d = ${selectedV} · ${M.inverse(selectedU,7)} mod 7`,11,'class="mono"');}
    body+=svgText(left+size/2,top+size+44,'frequency coordinates in 𝔽₇ × 𝔽₇',10,'text-anchor="middle" class="muted"');el.innerHTML=body;
    set('fourier-summary',selectedU===0?`At (u,v) = (0,0), probability = 1/7. This sample gives no information about d.`:`At (u,v) = (${selectedU},${selectedV}), probability = 1/7. Since ${selectedU}⁻¹ = ${M.inverse(selectedU,7)}, d = ${selectedV}·${M.inverse(selectedU,7)} = ${d} mod 7.`);
    set('fourierTotal',data.total.toFixed(12));set('fourierLeak',tiny(data.offSupportMax));reports.fourier=data;
  }
  function renderHodge() {
    syncOutputs('hodge');const zero=$('hodgeZero').checked,epsilon=zero?0:10**value('hodgeLog'),data=M.hodge(epsilon);
    $('hodgeLog').disabled=zero;
    const rawWidth=$('hodgeSvg').getBoundingClientRect().width||660,mobile=rawWidth<510;
    const {el,width,height}=svgSize('hodgeSvg',mobile?270:340),left=43,right=width-26,top=36,bottom=height-52;
    const px=x=>left+(right-left)*x,py=y=>bottom-(bottom-top)*y;
    let body='<title>The middle Hodge Laplacian eigenvalues are epsilon squared and one</title>';
    for(const t of [0,.25,.5,.75,1]){body+=`<path d="M${px(t)},${top}V${bottom}M${left},${py(t)}H${right}" class="chart-grid"/>`;body+=svgText(px(t),bottom+20,fmt(t),10,'text-anchor="middle"')+svgText(left-10,py(t)+4,fmt(t),10,'text-anchor="end"');}
    const path=Array.from({length:101},(_,i)=>`${i?'L':'M'}${px(i/100)},${py((i/100)**2)}`).join('');
    body+=`<path d="${path}" fill="none" stroke="${C.teal}" stroke-width="2.6"/><path d="M${left},${top}H${right}" fill="none" stroke="${C.ochre}" stroke-width="2" stroke-dasharray="6 4"/>`;
    body+=`<path d="M${px(epsilon)},${top}V${bottom}" stroke="#8ca092" stroke-width="1" stroke-dasharray="3 4"/><circle cx="${px(epsilon)}" cy="${py(epsilon*epsilon)}" r="5.5" fill="${C.ochre}" stroke="#fff" stroke-width="2"/>`;
    body+=svgText(left,top-15,'eigenvalue λ',11,'class="muted"')+svgText(right,bottom+39,'ε',14,'text-anchor="end"')+svgText(px(.58),py(.58**2)-16,'λ₁ = ε²',14,`style="fill:${C.teal}"`)+svgText(right-9,top+21,'λ₂ = 1',13,`text-anchor="end" style="fill:${C.ochre}"`);
    el.innerHTML=body;
    set('hodge-summary',`ε = ${tiny(epsilon)}; Δ₁ = diag(${tiny(data.least)}, 1). Cohomology dimensions: (${data.homology.join(', ')}).`);
    set('hodgeMin',tiny(data.least));set('hodgePositive',tiny(data.smallestPositive));set('hodgeKernel',data.kernelDimension);reports.hodge=data;
  }
  function renderGauge() {
    syncOutputs('gauge');const flux=value('gaugeFlux'),vertex=value('gaugeVertex'),lambda=value('gaugeLambda'),data=M.gaugePlaquette(flux,vertex,lambda);
    const {el,width}=svgSize('gaugeSvg',365),mobile=width<510,left=mobile?76:width*.27,right=mobile?width-76:width*.73,top=65,bottom=290,cx=(left+right)/2,cy=(top+bottom)/2;
    const vertices=[[left,top],[right,top],[right,bottom],[left,bottom]];
    let body='<title>Gauge invariance of a U(1) plaquette</title><defs><marker id="gaugeArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#8ca092"/></marker></defs>';
    for(let i=0;i<4;i++){const A=vertices[i],B=vertices[(i+1)%4];body+=`<path d="M${A}L${B}" stroke="#8ca092" stroke-width="1.5" fill="none" marker-end="url(#gaugeArrow)"/>`;}
    const positions=[[cx,top-28],[right+37,cy-8],[cx,bottom+28],[left-37,cy-8]];
    for(let i=0;i<4;i++){const [x,y]=positions[i],wrap=a=>M.mod(a+Math.PI,M.TAU)-Math.PI;body+=svgText(x,y,fmt(wrap(data.original[i]),2),11,`text-anchor="middle" style="fill:${C.teal}"`)+svgText(x,y+16,fmt(wrap(data.transformed[i]),2),11,`text-anchor="middle" style="fill:${C.ochre}"`);}
    for(let i=0;i<4;i++){const [x,y]=vertices[i],active=i===vertex;body+=`<circle cx="${x}" cy="${y}" r="${active?8:6}" fill="${active?C.ochre:C.teal}" stroke="#fff" stroke-width="2"/>`;const dy=i<2?19:-14;body+=svgText(x,y+dy,`${i}: λ=${fmt(data.gauge[i],2)}`,10,'text-anchor="middle" class="mono"');}
    const r=mobile?29:37;
    body+=`<circle cx="${cx}" cy="${cy-7}" r="${r}" fill="none" stroke="${C.line}"/><path d="M${cx-r},${cy-7}H${cx+r}M${cx},${cy-r-7}V${cy+r-7}" stroke="#e3e9e2"/>`;
    body+=`<path d="M${cx},${cy-7}L${cx+r*data.W[0]},${cy-7-r*data.W[1]}" stroke="${C.teal}" stroke-width="4"/><path d="M${cx},${cy-7}L${cx+r*data.Wprime[0]},${cy-7-r*data.Wprime[1]}" stroke="${C.ochre}" stroke-width="1.5" stroke-dasharray="3 2"/>`;
    body+=svgText(cx,cy+r+18,'W′ = W',14,'text-anchor="middle"')+svgText(cx,cy+r+37,`Φ = ${fmt(flux,2)} rad`,10,'text-anchor="middle" class="muted"');el.innerHTML=body;
    set('gauge-summary',`W = ${fmt(data.W[0],6)} ${data.W[1]>=0?'+':'−'} ${fmt(Math.abs(data.W[1]),6)}i. Transforming vertex ${vertex} by λ=${fmt(lambda)} leaves W unchanged.`);
    set('gaugeResidual',tiny(data.residual));set('gaugeAction',fmt(data.action,8));
    $('gaugeTable').innerHTML=data.original.map((a,i)=>`<tr><td>${i} → ${(i+1)%4}</td><td>${fmt(a,6)}</td><td>${fmt(data.transformed[i],6)}</td></tr>`).join('');reports.gauge=data;
  }
  const renderers={torus:renderTorus,cone:renderCone,elliptic:renderElliptic,fourier:renderFourier,hodge:renderHodge,gauge:renderGauge};
  function renderAll(){drawHero();Object.values(renderers).forEach(render=>render());}
  for(const control of controls){control.addEventListener('input',()=>renderers[control.dataset.lab]());control.addEventListener('change',()=>{renderers[control.dataset.lab]();writeURL(true);});}
  function setControl(id,n){$(id).value=String(n);}
  document.querySelectorAll('[data-cone-preset]').forEach(button=>button.addEventListener('click',()=>{
    const kind=button.dataset.conePreset;setControl('coneRadius',kind==='vertex'?0:1);setControl('coneAlpha',0);
    setControl('coneBeta',kind==='xzero'?180:kind==='yzero'?0:90);renderCone();writeURL(true);
  }));
  $('ecPrevious').addEventListener('click',()=>{setControl('ecK',M.mod(value('ecK')-1,19));renderElliptic();writeURL(true);});
  $('ecNext').addEventListener('click',()=>{setControl('ecK',M.mod(value('ecK')+1,19));renderElliptic();writeURL(true);});
  $('resetAll').addEventListener('click',()=>{for(const c of controls){if(c.type==='checkbox')c.checked=defaults.get(c.id);else c.value=defaults.get(c.id);}renderAll();writeURL(true);set('shareStatus','All laboratory parameters reset.');});
  $('shareView').addEventListener('click',async()=>{writeURL(false);try{await navigator.clipboard.writeText(location.href);set('shareStatus','Link copied with the current parameters.');}catch(_){set('shareStatus','The address bar now contains this view. Copy its URL to share.');}});
  window.addEventListener('popstate',()=>{readURL();renderAll();});
  function cameraInteraction(canvasId,yawId,pitchId,lab){
    const canvas=$(canvasId);let drag=null;
    const move=(dx,dy)=>{setControl(yawId,M.mod(value(yawId)+dx+180,360)-180);setControl(pitchId,clamp(value(pitchId)+dy,-80,80));renderers[lab]();};
    canvas.addEventListener('keydown',event=>{const moves={ArrowLeft:[-6,0],ArrowRight:[6,0],ArrowUp:[0,5],ArrowDown:[0,-5]};if(moves[event.key]){event.preventDefault();move(...moves[event.key]);writeURL(true);}else if(event.key==='Home'){event.preventDefault();setControl(yawId,defaults.get(yawId));setControl(pitchId,defaults.get(pitchId));renderers[lab]();writeURL(true);}});
    canvas.addEventListener('pointerdown',event=>{if(event.pointerType!=='mouse'||event.button!==0)return;drag={x:event.clientX,y:event.clientY};canvas.setPointerCapture(event.pointerId);});
    canvas.addEventListener('pointermove',event=>{if(!drag)return;move((event.clientX-drag.x)*.45,(event.clientY-drag.y)*.35);drag={x:event.clientX,y:event.clientY};});
    const end=()=>{if(drag){drag=null;writeURL(true);}};canvas.addEventListener('pointerup',end);canvas.addEventListener('pointercancel',end);canvas.addEventListener('lostpointercapture',end);
  }
  cameraInteraction('torusCanvas','torusYaw','torusPitch','torus');cameraInteraction('coneCanvas','coneYaw','conePitch','cone');
  let resizeScheduled=false;
  window.addEventListener('resize',()=>{if(resizeScheduled)return;resizeScheduled=true;requestAnimationFrame(()=>{resizeScheduled=false;renderAll();});});
  if('IntersectionObserver' in window){const nav=[...document.querySelectorAll('.lab-nav a')];const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting)nav.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+entry.target.id));},{rootMargin:'-10% 0px -65% 0px',threshold:0});document.querySelectorAll('.lab-card').forEach(card=>observer.observe(card));}
  readURL();renderAll();
  window.ResearchCompanion=Object.freeze({getState:saveState,getReport:()=>JSON.parse(JSON.stringify(reports)),renderAll});
})();
