// Original local crosswalk; derives the order from permutations, never from spins.
export function cycles(p){
 const unseen=new Set(p.map((_,i)=>i)),result=[];
 while(unseen.size){let i=Math.min(...unseen),c=[];while(unseen.has(i)){unseen.delete(i);c.push(i);i=p[i];}result.push(c);}
 return result;
}
export function permutation(orbits){
 const p=Array(orbits.flat().length);
 for(const c of orbits)for(let i=0;i<c.length;i++){if(p[c[i]]!==undefined)throw Error('Repeated dart');p[c[i]]=c[(i+1)%c.length];}
 if(Array.from(p).some(x=>!Number.isInteger(x))||new Set(p).size!==p.length)throw Error('Invalid dart permutation');
 return p;
}
export function dessin(sigmaCycles,alphaCycles){
 const sigma=permutation(sigmaCycles),alpha=permutation(alphaCycles),n=sigma.length;
 if(n!==alpha.length||alpha.some((a,h)=>a===h||alpha[a]!==h))throw Error('Alpha must pair all darts');
 const tau=sigma.map((_,h)=>sigma.indexOf(h)),phi=tau.map(h=>alpha[h]);
 const edges=cycles(alpha),edgeOf=Array(n);edges.forEach((c,e)=>c.forEach(h=>edgeOf[h]=e));
 const visited=new Set([0]);for(let changed=true;changed;){changed=false;for(const h of [...visited])for(const j of [sigma[h],alpha[h]])if(!visited.has(j)){visited.add(j);changed=true;}}
 if(visited.size!==n)throw Error('Disconnected dessin');
 const arrows=sigma.map((_,h)=>({dart:h,source:edgeOf[h],target:edgeOf[tau[h]],permitted:tau[h],forbidden:phi[h]}));
 for(const a of arrows)if(a.target!==arrows[a.forbidden].source||a.target!==arrows[a.permitted].source||a.forbidden===a.permitted)throw Error('Invalid locally gentle successors');
 const faces=cycles(phi),genus=(2-sigmaCycles.length+edges.length-faces.length)/2;
 if(!Number.isInteger(genus)||genus<0)throw Error('Invalid surface genus');
 return {sigma,alpha,tau,phi,edges,edgeOf,arrows,faces,genus,rank:sigmaCycles.reduce((s,c)=>s+c.length*c.length,0),passport:[sigmaCycles.map(c=>c.length),edges.map(c=>c.length),faces.map(c=>c.length)]};
}
export function oddDessin(m){
 if(!Number.isInteger(m)||m<3||m%2!==1)throw Error('Odd dessin requires an odd integer m≥3');
 return dessin([Array.from({length:m},(_,i)=>i),Array.from({length:m},(_,i)=>i+m)],Array.from({length:m},(_,i)=>[i,i+m]));
}
const theta=()=>oddDessin(3);
export function architectureCollection(key){
 const allowed={rg:'/data/rg/',qtoken:'/data/quantum-tokengt/',frontier:'/data/learned-frontier/'};
 const id=Object.hasOwn(allowed,key)?key:'architecture';
 const base=allowed[id]??'/data/architecture/';
 return {id,base,manifest:base+'manifest.json'};
}
export function surfaceProfile(trace){
 const stateFlow=trace.category==='quantum-state-flow-rg',generative=trace.category==='quantum-generative-rg'||stateFlow,rg=trace.category==='quantum-full-action-rg',rgToken=trace.category==='quantum-tokengt-rg',m=(rg||rgToken||generative)?trace.input?.surface_m??5:9;
 const classical=trace.category.startsWith('classical-'),nine=trace.id.startsWith('qcnn-9'),square=trace.id.startsWith('qcnn-4'),photon=trace.category==='photonic-gaussian',clock=trace.id==='clock-carrier',harper=trace.category==='quantum-classical-toricgt';
 let kind=generative?'generative':rg?'rg':rgToken?'rg-token':classical?'tokens':nine?'nine':square?'square':photon?'node':clock?'clock':harper?'harper':trace.category==='quantum-convolution'?'convolution':'attention';
 let d=(rg||rgToken||generative)?oddDessin(m):photon?dessin([[0],[1]],[[0,1]]):square?dessin([[0,1,2,3]],[[0,2],[1,3]]):nine?oddDessin(9):classical?dessin(trace.surface_context.sigma,trace.surface_context.alpha):theta();
 const titles={generative:`Genus ${d.genus} / ${stateFlow?'coherent purification control':'learned reduced-Gibbs field'}`,rg:`Genus ${d.genus} full-action RG / three parameter registers`,'rg-token':`Genus ${d.genus} / quantum-token RG surface context`,tokens:'Stored elliptic theta → finite token cycle',nine:'Genus four → nine edge-labelled spins',square:'Elliptic square → four dart-labelled spins',node:'Nodal interval → auxiliary two-mode analogy',clock:'Elliptic theta order / auxiliary forward Weyl torus',harper:'Elliptic theta order / auxiliary Harper torus',convolution:'Elliptic theta → a two-edge feature patch',attention:'Elliptic theta → three overlapping quantum patches'};
 const curves={generative:`y²=x^${m}−1, β=x^${m}`,rg:`y²=x^${m}−1, β=x^${m}`,'rg-token':`y²=x^${m}−1, β=x^${m}`,node:'ℙ¹, β(z)=4z(1−z)',square:'y²=x³−x, β=x²',nine:'y²=x⁹−1, β=x⁹',tokens:'y²=x³−1, β=x³',clock:'y²=x³−1, β=x³',harper:'y²=x³−1, β=x³',convolution:'y²=x³−1, β=x³',attention:'y²=x³−1, β=x³'};
 const rgLimit=`The physical clean dessin is K₂,${m}: two black and ${m} white spin sites, ${m+2} physical spins in total. Decimating the two black spins retains ${m} white boundary spins and their full ${2**m}-configuration action. The order quiver instead has ${m} vertices (paired darts); these are not physical spin sites. A three-qubit feature circuit encodes the coupling parameters J+, J−, b, not the ${m} boundary spins. Learned channels/readout weights are global. The actual parameter support is V=J+ s+ Σⱼtⱼ + J− s− Σⱼ(−1)^j tⱼ + b s+ − 0.6 b s− + Σⱼhⱼtⱼ, with fixed white fields hⱼ. No faithful A/Λ action or order-linear learned map is asserted.`;
 const limits={generative:stateFlow?'Two retained physical black spins form the two-qubit system; two further qubits purify it. A trained unitary4qubit control path prepares a known density family with ideal target-state supervision. Ancillas permit subsystem entropy change. These physical spin/ancilla wires are not a faithful surface-order module, a universal noise inverse or a GRH construction.':'The actual K2,5 clean-dessin quantum-matter teacher has seven physical spins. Exact white-spin partial trace retains two black spins. The learned field describes their noisy Z-measurement coordinates. Four auxiliary feature qubits are not the seven physical spins or five order vertices. No coherent tomography, faithful order action or GRH theorem is inferred.',rg:rgLimit,'rg-token':`The exact parent is the same K₂,${m} clean dessin and rank-${d.rank} completed order. Its two black and ${m} white physical spin sites differ from the ${m} edge/quiver vertices. This generic inspector displays the saved tensors but has no audited token-to-dart dictionary for this new model; use its dedicated quantum-token RG interface for that mapping. No old elliptic-theta fixture relabelling or faithful order action is asserted.`,tokens:'Explicit relabelling: node positions 0,1,2 ↦ quiver vertices [0],[2],[1]; position 3 is padding. Edge tokens 4,5,6 ↦ arrows a₀,a₂,a₁. The saved 0→1→2→0 endpoints then follow τ. Token channels, attention and expert slots forget the other permitted branch and α-gluing; they do not define a faithful A- or Λ-module.',nine:'Wire q ↦ dessin edge [q]={q,q+9}, q=0,…,8. CZ ring adjacency is auxiliary Hamiltonian adjacency. The 512-dimensional spin space and its gates have not been checked as an A-module. Pooling retains wires 0,…,4 and traces out 5,…,8; it does not contract this genus-four dessin.',square:'This dessin has four darts/arrows but TWO edges/quiver vertices: [0]={0,2}, [1]={1,3}. Four qubit wires are labelled by darts 0,…,3; two wires share each edge. This labels a finite physical model; it supplies no faithful algebra action or induced map of orders. Pooling keeps wires 0,1.',node:'Only an auxiliary analogy: modes 0,1 are labelled by the two nodal branches x,y. The actual polynomial order is k[x,y]/(xy), completed at (x,y). Beamsplitter mixing is symplectic evolution on quadratures, not a proved functor of nodal modules or a representation with xy=0.',clock:'The d-level forward clock uses Ueⱼ=ζʲeⱼ, Veⱼ=eⱼ₊₁ and UV=ζVU. Its basis sites live on an auxiliary Weyl torus, not on the three dessin edges. Invertible U,V cannot represent a forbidden pair: their product cannot vanish. No faithful map from this locally gentle order is claimed.',harper:'Saved Harper uses d=4, U=diag(iʲ), Veⱼ=eⱼ₋₁, hence VU=iUV. H=U+U*+λ(V+V*) is an auxiliary Weyl operator, not an action of the theta order; invertible U,V fail its zero relations. The two-qubit learned feature circuit is also auxiliary. Rational PSD certificates apply only to this finite H.',convolution:'Original explicit labelling for this panel: the two inputs k₁,k₂ label theta edges [0],[1], and feature wires 0,1 label these inputs. This is a patch of the theta scheme, not a saved surface-module map. The exact Ising target is atanh(tanh k₁ tanh k₂); its scalar decimation does not establish an order functor.',attention:'Original explicit labelling: the three couplings label theta edges [0],[1],[2]. Saved patch pairs are (0,1),(1,2),(2,0); local wire r maps to the rth edge in its pair. Softmax weights mix patch features. This is a numerical patch construction, not an algebra-linear push-down or an order representation.'};
 return {kind,d,title:titles[kind],curve:curves[kind],limit:limits[kind],geometry:(nine||rg||rgToken||generative)?'sheet':photon?'interval':square?'square':'theta',auxiliary:clock||harper};
}
export function selectionMapping(trace,node,indices=[]){
 const p=surfaceProfile(trace),edges=new Set(),arrows=new Set(),sites=new Set(),labels=[],roles=[];let note='';
 const axis=(name)=>node.tensor.axes.indexOf(name),value=name=>axis(name)<0?null:indices[axis(name)];
 const addToken=t=>{if(t===3){labels.push('token 3 = padding (no geometry)');return;}if(t>=0&&t<3){const e=[0,2,1][t];edges.add(e);labels.push(`node token ${t} ↦ [${e}]`);}else if(t>=4&&t<=6){const h=[0,2,1][t-4];arrows.add(h);edges.add(p.d.edgeOf[h]);edges.add(p.d.arrows[h].target);labels.push(`edge token ${t} ↦ a${h}`);}};
 if(p.kind==='generative'){
  if(value('retained_spin')!==null){sites.add(value('retained_spin'));labels.push(`retained physical black spin ${value('retained_spin')}`);}
  if(node.wires){if(trace.category==='quantum-state-flow-rg'){for(const q of node.wires){if(q<2)sites.add(q);labels.push(q<2?`retained physical black spin ${q}`:`purification ancilla ${q-2}`);}}else labels.push(`auxiliary feature wires ${node.wires.join(', ')}; no quiver-vertex identification`);}
  if(value('basis')!==null)labels.push(`${trace.category==='quantum-state-flow-rg'?'system+ancilla':'auxiliary feature'}4qubit basis |${value('basis').toString(2).padStart(4,'0')}⟩`);
  note='The physical Gibbs marginal is tied to this genus-two incidence graph; neural channels and auxiliary wires have no faithful surface-order module action.';
 }else if(p.kind==='rg'||p.kind==='rg-token'){
  const boundary=value('boundary_configuration'),m=p.d.edges.length;
  if(boundary!==null){for(let e=0;e<m;e++)edges.add(e);labels.push(`white-spin boundary configuration ${boundary}: binary index ${boundary.toString(2).padStart(m,'0')}`);note='All retained white spin sites contribute to this configuration; binary-to-spin signs follow the saved record convention. These are physical spin configurations, not quiver-idempotent coordinates.';}
  if(p.kind==='rg'){
   if(node.wires)for(const q of node.wires){const role=['J+','J−','b'][q];if(role){roles.push(role);labels.push(`feature gate wire ${q} ↦ coupling register ${role} (not a physical boundary spin or quiver vertex)`);}}
   if(node.id==='couplings'){const q=indices.at(-1)??0,role=['J+','J−','b'][q];if(role){roles.push(role);labels.push(`input coupling ${q} = ${role}`);}}
   if(value('basis')!==null)labels.push(`three-feature-qubit basis |${value('basis').toString(2).padStart(3,'0')}⟩; register order (J+, J−, b)`);
   if(roles.length)note+=' Geometry marks the physical Hamiltonian support of each selected parameter: J+ on the upper black-to-white half-edges; J− on the lower half-edges with alternating signs (−1)^j; b on the two black spins with coefficients +1 and −0.6. White fields are fixed separately. It does not identify a feature wire with a surface vertex.';
   if(!labels.length)note='Global feature channels, head weights and readout operations have no unique dessin edge. The trained output approximates the full boundary action, not a compressed physical quantum state.';
  }else if(boundary===null)note='Exact genus/edge/order context only: this quantum-token RG tensor has no audited geometric index dictionary in the generic inspector. Dedicated token/gate semantics are supplied by its own interface.';
 }else if(p.kind==='tokens'){
  for(const name of ['token','query_token','key_token','node'])if(value(name)!==null)addToken(value(name));
  if(value('edge')!==null)addToken(value('edge')+4);
  if(!labels.length)note='Global channels, weights, pooled readouts and expert slots have no unique dessin edge. Inspect an actual token axis to locate its support.';
  if(node.id.includes('.moe.'))note+=' Expert/slot indices are learned aggregation slots, not additional quiver vertices. Strict prefix slots use earlier token indices.';
  if(node.id.includes('winners')||node.mode?.startsWith('tropical'))note+=' Tropical maximizing keys are numerical witnesses; max-plus aggregation imposes no new order relation.';
 }else if(p.kind==='node'){
  for(const name of ['quadrature','quadrature_prime'])if(value(name)!==null){const q=value(name),mode=q%2;arrows.add(mode);edges.add(0);labels.push(`${['x₀','x₁','p₀','p₁'][q]} ↦ auxiliary mode ${mode} / branch ${mode?'y':'x'}`);}
 }else if(p.auxiliary){
  if(['U','V','harper'].includes(node.id)||p.kind==='clock')for(const name of ['row','column','basis'])if(value(name)!==null){sites.add(value(name));labels.push(`auxiliary basis site ${value(name)}`);}
  note=p.kind==='harper'&&node.id.startsWith('patch')?'Learned two-qubit feature wires do not label the dessin quiver.':!sites.size?'This scalar/spectrum/readout has no unique dessin edge.':'';
 }else{
  const patchMatch=node.id.match(/^patch(\d+)/),patch=patchMatch?Number(patchMatch[1]):value('patch')??value('pair'),pairs=trace.input?.pairs??[[0,1],[1,2],[2,0]];
  const wireEdge=q=>p.kind==='square'?p.d.edgeOf[q]:p.kind==='attention'?pairs[patch??0][q]:q;
  if(node.wires)for(const q of node.wires){const e=wireEdge(q);edges.add(e);labels.push(`gate wire ${q}${patch!==null?` in patch ${patch}`:''} ↦ [${e}]${p.kind==='square'?` via dart ${q}`:''}`);}
  if(p.kind==='attention'&&patch!==null&&!node.wires)for(const e of pairs[patch])edges.add(e);
  if(p.kind==='convolution'&&!node.wires){edges.add(0);edges.add(1);}
  if(p.kind==='attention'&&patch===null&&!node.wires)note='The patch reduction combines all three overlapping pairs; no single edge is singled out.';
  const basis=value('basis');
  if(basis!==null){const n=p.kind==='nine'?9:p.kind==='square'?4:2,bits=basis.toString(2).padStart(n,'0');labels.push(`basis |${bits}⟩ (q0 most significant)`);if(!node.wires)for(let q=0;q<n;q++)edges.add(wireEdge(q));note+=' Each bit is an edge/dart-labelled spin factor, not a quiver idempotent coordinate.';}
  if(node.id==='retained_density'){const n=p.kind==='nine'?5:2;if(!node.wires)for(let q=0;q<n;q++)edges.add(wireEdge(q));note+=` Reduced density coordinates label ${n} retained spin factors; discarded factors were traced out.`;}
 }
 return {edges:[...edges],arrows:[...arrows],sites:[...sites],roles,labels,note:note.trim()};
}
export const cycleText=p=>cycles(p).map(c=>'('+c.join(' ')+')').join('');
// Two-dimensional path module: only one arrow is 1, all other arrows are 0.
// Every arrow is non-loop in theta/square/odd hyperelliptic examples, so all
// quadratic relations are zero. For the nodal loop use nilpotent E12 instead.
const multiply=(a,b)=>a.map((r,i)=>r.map((_,j)=>a[i].reduce((s,v,k)=>s+v*b[k][j],0)));
const equal=(a,b)=>a.every((r,i)=>r.every((v,j)=>v===b[i][j]));
export function checkRepresentation(d,idempotents,matrices){
 const n=matrices[0].length,zero=Array.from({length:n},()=>Array(n).fill(0)),identity=zero.map((r,i)=>r.map((_,j)=>Number(i===j)));
 let idempotentFailures=0,endpointFailures=0;
 const sum=zero.map((r,i)=>r.map((_,j)=>idempotents.reduce((s,p)=>s+p[i][j],0)));
 if(!equal(sum,identity))idempotentFailures++;
 for(let i=0;i<idempotents.length;i++)for(let j=0;j<idempotents.length;j++)if(!equal(multiply(idempotents[i],idempotents[j]),i===j?idempotents[i]:zero))idempotentFailures++;
 for(const a of d.arrows)if(!equal(multiply(idempotents[a.target],multiply(matrices[a.dart],idempotents[a.source])),matrices[a.dart]))endpointFailures++;
 // Column actions reverse the order of multiplication of travel-order paths.
 const relationFailures=d.arrows.filter(a=>!equal(multiply(matrices[a.forbidden],matrices[a.dart]),zero)).map(a=>a.dart);
 return {checked:d.arrows.length,idempotentFailures,endpointFailures,relationFailures};
}
export function relationAudit(d,h){
 const matrices=d.arrows.map((_,j)=>j===h?[[0,0],[1,0]]:[[0,0],[0,0]]),arrow=d.arrows[h];
 const idempotents=d.edges.map((_,e)=>[[Number(e===arrow.source),0],[0,Number(e===arrow.target)]]);
 const check=checkRepresentation(d,idempotents,matrices),centralZero=d.sigma[h]!==h;
 return {checked:check.checked,failures:check.relationFailures.length+check.idempotentFailures+check.endpointFailures,dimension:2,continuous:true,centralZero,description:'M has basis v_source,v_target (two distinct basis vectors even for a loop); selected a_h sends v_source to v_target, every other arrow is zero. Idempotents project to the indicated vertex summands. All idempotent, endpoint and length-two relations are checked exactly. This actual A/J²-module extends continuously to Λ, with central u acting nilpotently (u²=0). It is a finite torsion module, not an R-free order lattice or the trained carrier.'};
}
