// Local structural viewer: wwPDB3.3 atoms/secondary records, no external runtime.
// HELIX/SHEET are source annotations; inferred display bonds are not new labels.
const numbers={H:1,C:6,N:7,O:8,F:9,NA:11,MG:12,P:15,S:16,CL:17,K:19,CA:20,FE:26,CU:29,ZN:30,BR:35,I:53};
const radius={1:.31,6:.76,7:.71,8:.66,9:.57,15:1.07,16:1.05,17:1.02};
const sidechains={ALA:'CA-CB',ARG:'CA-CB CB-CG CG-CD CD-NE NE-CZ CZ-NH1 CZ-NH2',ASN:'CA-CB CB-CG CG-OD1 CG-ND2',ASP:'CA-CB CB-CG CG-OD1 CG-OD2',CYS:'CA-CB CB-SG',GLN:'CA-CB CB-CG CG-CD CD-OE1 CD-NE2',GLU:'CA-CB CB-CG CG-CD CD-OE1 CD-OE2',GLY:'',HIS:'CA-CB CB-CG CG-ND1 ND1-CE1 CE1-NE2 NE2-CD2 CD2-CG',ILE:'CA-CB CB-CG1 CB-CG2 CG1-CD1',LEU:'CA-CB CB-CG CG-CD1 CG-CD2',LYS:'CA-CB CB-CG CG-CD CD-CE CE-NZ',MET:'CA-CB CB-CG CG-SD SD-CE',PHE:'CA-CB CB-CG CG-CD1 CD1-CE1 CE1-CZ CZ-CE2 CE2-CD2 CD2-CG',PRO:'CA-CB CB-CG CG-CD CD-N',SER:'CA-CB CB-OG',THR:'CA-CB CB-OG1 CB-CG2',TRP:'CA-CB CB-CG CG-CD1 CD1-NE1 NE1-CE2 CE2-CD2 CD2-CG CD2-CE3 CE3-CZ3 CZ3-CH2 CH2-CZ2 CZ2-CE2',TYR:'CA-CB CB-CG CG-CD1 CD1-CE1 CE1-CZ CZ-CE2 CE2-CD2 CD2-CG CZ-OH',VAL:'CA-CB CB-CG1 CB-CG2'};
const sub=(a,b)=>a.map((v,i)=>v-b[i]),add=(a,b)=>a.map((v,i)=>v+b[i]),scale=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),norm=a=>Math.hypot(...a),unit=a=>scale(a,1/Math.max(norm(a),1e-12));
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const residueKey=(chain,seq,icode,segment)=>[segment,chain,seq,icode].join(':');
const ordered=(a,b)=>a.seq-b.seq||a.icode.localeCompare(b.icode);
export function parsePDB(text){
 const lines=text.split(/\r?\n/),atoms=[],residues=[],secondary=[],byResidue=new Map(),serial=new Map(),bonds=[],seen=new Set();let segment=0,finished=false;
 for(const line of lines){
  if(line.startsWith('HELIX '))secondary.push({kind:'helix',chain:line[19],endChain:line[31],start:{seq:+line.slice(21,25),icode:line[25]},end:{seq:+line.slice(33,37),icode:line[37]},helixClass:+line.slice(38,40),id:line.slice(11,14).trim()});
  if(line.startsWith('SHEET '))secondary.push({kind:'sheet',chain:line[21],endChain:line[32],start:{seq:+line.slice(22,26),icode:line[26]},end:{seq:+line.slice(33,37),icode:line[37]},sheet:line.slice(11,14).trim(),sense:+line.slice(38,40),strand:+line.slice(7,10)});
  if(line.startsWith('ENDMDL'))finished=true;
  if(line.startsWith('TER'))segment++;
  if(finished||(!line.startsWith('ATOM  ')&&!line.startsWith('HETATM'))||![' ','A'].includes(line[16])||+line.slice(54,60)<=0)continue;
  const name=line.slice(12,16).trim(),resname=line.slice(17,20).trim();if(['HOH','WAT','DOD'].includes(resname))continue;
  const chain=line[21],seq=+line.slice(22,26),icode=line[26],key=residueKey(chain,seq,icode,segment),unique=key+':'+name;if(seen.has(unique))continue;seen.add(unique);
  let element=line.slice(76,78).trim().toUpperCase();if(!element)element=name.replace(/^\d+/,'')[0];
  const atom={serial:+line.slice(6,11),name,resname,chain,seq,icode,segment,element,atomicNumber:numbers[element]??0,position:[+line.slice(30,38),+line.slice(38,46),+line.slice(46,54)]};
  if(!byResidue.has(key)){const r={key,name:resname,chain,seq,icode,segment,atoms:{},secondary:'coil'};byResidue.set(key,r);residues.push(r);}
  atom.residue=residues.indexOf(byResidue.get(key));byResidue.get(key).atoms[name]=atoms.length;serial.set(atom.serial,atoms.length);atoms.push(atom);
 }
 const bondKeys=new Set(),distance=(a,b)=>norm(sub(atoms[a].position,atoms[b].position));
 function bond(a,b,kind){if(a===undefined||b===undefined||a===b||distance(a,b)<.2||distance(a,b)>2.5)return;const key=[Math.min(a,b),Math.max(a,b)].join(':');if(bondKeys.has(key))return;bondKeys.add(key);bonds.push({a,b,kind,order:1});}
 for(const r of residues){
  const pairs=('N-CA CA-C C-O C-OXT '+(sidechains[r.name]??'')).trim().split(/\s+/);
  for(const pair of pairs){const [a,b]=pair.split('-');bond(r.atoms[a],r.atoms[b],'residue template');}
  const ids=Object.values(r.atoms);
  for(const i of ids){if(atoms[i].atomicNumber!==1)continue;let best=null,d=Infinity;for(const j of ids){if(atoms[j].atomicNumber===1)continue;const n=distance(i,j);if(n<d){d=n;best=j;}}if(best!==null&&d<1.35)bond(i,best,'hydrogen proximity');}
  // Unknown ligands use explicitly labelled distance-based display connectivity.
  if(!(r.name in sidechains))for(const i of ids)for(const j of ids)if(i<j&&radius[atoms[i].atomicNumber]&&radius[atoms[j].atomicNumber]&&distance(i,j)<1.2*(radius[atoms[i].atomicNumber]+radius[atoms[j].atomicNumber]))bond(i,j,'inferred ligand proximity');
  for(const s of secondary)if(r.chain===s.chain&&s.chain===s.endChain&&ordered(r,s.start)>=0&&ordered(r,s.end)<=0){r.secondary=s.kind==='sheet'?'strand':s.helixClass===1?'alpha':s.helixClass===5?'310':'helix';r.annotation=s;}
 }
 for(let i=1;i<residues.length;i++){const a=residues[i-1],b=residues[i];if(a.chain===b.chain&&a.segment===b.segment&&a.atoms.C!==undefined&&b.atoms.N!==undefined&&distance(a.atoms.C,b.atoms.N)<1.9)bond(a.atoms.C,b.atoms.N,'peptide');}
 for(const line of lines)if(line.startsWith('CONECT')){const ids=line.slice(6).match(/.{1,5}/g)?.map(x=>serial.get(+x))??[];for(const j of ids.slice(1))bond(ids[0],j,'CONECT');}
 const backbone=residues.filter(r=>r.atoms.CA!==undefined).map(r=>({...r,index:r.atoms.CA,position:atoms[r.atoms.CA].position,guide:r.atoms.O===undefined?null:sub(atoms[r.atoms.O].position,atoms[r.atoms.C??r.atoms.CA].position)}));
 return {atoms,residues,secondary,bonds,backbone,source:'PDB first model; alternate blank/A; solvent omitted; wwPDB HELIX/SHEET annotations',serial};
}
export function parseSDF(text){
 const lines=text.split(/\r?\n/),na=+lines[3].slice(0,3),nb=+lines[3].slice(3,6),atoms=[],bonds=[];
 for(const line of lines.slice(4,4+na)){const element=line.slice(31,34).trim().toUpperCase();atoms.push({element,atomicNumber:numbers[element]??0,position:[+line.slice(0,10),+line.slice(10,20),+line.slice(20,30)]});}
 for(const line of lines.slice(4+na,4+na+nb))bonds.push({a:+line.slice(0,3)-1,b:+line.slice(3,6)-1,order:+line.slice(6,9),kind:'SDF explicit'});
 const adjacent=atoms.map(()=>[]);for(const b of bonds){adjacent[b.a].push(b.b);adjacent[b.b].push(b.a);}
 const backbone=[];
 atoms.forEach((a,i)=>{if(a.atomicNumber!==6||bonds.some(b=>(b.a===i||b.b===i)&&b.order!==1))return;const ns=adjacent[i].filter(j=>atoms[j].atomicNumber===7),cs=adjacent[i].filter(j=>atoms[j].atomicNumber===6&&bonds.some(b=>(b.a===j&&atoms[b.b].atomicNumber===8||b.b===j&&atoms[b.a].atomicNumber===8)&&b.order===2));if(ns.length&&cs.length)backbone.push({index:i,position:a.position,nitrogen:ns[0],carbonyl:cs[0],secondary:'unassigned',chain:'synthetic',segment:0,seq:backbone.length+1,icode:' '});});
 // Directed peptide connectivity supplies sequence order; geometry alone does not.
 const next=r=>backbone.find(s=>bonds.some(b=>b.a===r.carbonyl&&b.b===s.nitrogen||b.b===r.carbonyl&&b.a===s.nitrogen));
 const orderedBackbone=[],visited=new Set();for(const start of backbone.filter(r=>!backbone.some(s=>next(s)===r)).concat(backbone)){let r=start;while(r&&!visited.has(r)){visited.add(r);orderedBackbone.push({...r,seq:orderedBackbone.length+1});r=next(r);}}
 return {atoms,bonds,backbone:orderedBackbone,residues:[],secondary:[],source:'Explicit SDF bonds; recognized peptide backbone; secondary structure unassigned'};
}
function catmull(p0,p1,p2,p3,t){return p1.map((_,i)=>.5*((2*p1[i])+(-p0[i]+p2[i])*t+(2*p0[i]-5*p1[i]+4*p2[i]-p3[i])*t*t+(-p0[i]+3*p1[i]-3*p2[i]+p3[i])*t*t*t));}
export function backboneMesh(structure,positions=null){
 const rows=structure.backbone.map(r=>({...r,position:positions?.[r.index]??r.position})),patches=[];let previous=null;
 const linked=(a,b)=>{if(!a||!b||a.chain!==b.chain||a.segment!==b.segment||norm(sub(a.position,b.position))>4.8)return false;const c=a.carbonyl??a.atoms?.C,n=b.nitrogen??b.atoms?.N;return c!==undefined&&n!==undefined&&structure.bonds.some(bond=>bond.a===c&&bond.b===n||bond.b===c&&bond.a===n);};
 for(let i=0;i<rows.length-1;i++){
  const a=rows[i],b=rows[i+1];if(!linked(a,b)){previous=null;continue;}
  const p0=linked(rows[i-1],a)?rows[i-1].position:a.position,p3=linked(b,rows[i+2])?rows[i+2].position:b.position;
  const kind=a.secondary,tip=kind==='strand'&&b.secondary!=='strand';let last=null;
  for(let k=0;k<=10;k++){
   const t=k/10,point=catmull(p0,a.position,b.position,p3,t),ahead=catmull(p0,a.position,b.position,p3,Math.min(1,t+.002)),behind=catmull(p0,a.position,b.position,p3,Math.max(0,t-.002)),tangent=unit(sub(ahead,behind));
   let frame=a.guide??previous??cross(tangent,Math.abs(tangent[2])<.8?[0,0,1]:[0,1,0]);frame=unit(sub(frame,scale(tangent,dot(frame,tangent))));if(previous&&dot(frame,previous)<0)frame=scale(frame,-1);previous=frame;
   let width=['alpha','310','helix'].includes(kind)?.9:kind==='strand'?.8:.16;if(tip)width=t<.25?.8:1.35*(1-t)/.75;
   const left=add(point,scale(frame,width)),right=add(point,scale(frame,-width));
   if(last)patches.push({vertices:[last.left,last.right,right,left],kind,chain:a.chain,residue:a.seq,sheet:a.annotation?.sheet??null,normal:unit(cross(tangent,frame))});last={left,right};
  }
 }
 return patches;
}
export function bondGeometry(a,b,r1,r2){return {atomRadiusFraction:.14,segments:Array.from({length:8},(_,i)=>({a:add(a,scale(sub(b,a),i/8)),b:add(a,scale(sub(b,a),(i+1)/8)),colorEnd:i<4?0:1})),radius:Math.min(r1,r2)*.12};}
