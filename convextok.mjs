/** Original live segmenter. LP/IP numbers and rational witnesses are saved CPU results. */
export const tokenKey = t => JSON.stringify(t);
export const fraction = s => {const [a,b=1]=String(s).split('/').map(Number);return a/b;};
export function segment(word, vocabulary, greedy=false) {
  const tokens=[...new Map([...vocabulary,...word.map(s=>[s])].map(t=>[tokenKey(t),t])).values()];
  const match=(t,i)=>i+t.length<=word.length&&t.every((s,j)=>s===word[i+j]);
  const cmp=(a,b)=>a.length-b.length||JSON.stringify(a).localeCompare(JSON.stringify(b),'en');
  if(greedy){const out=[];for(let i=0;i<word.length;){const t=tokens.filter(t=>match(t,i)).sort((a,b)=>b.length-a.length||tokenKey(a).localeCompare(tokenKey(b),'en'))[0];out.push(t);i+=t.length;}return out;}
  const best=Array(word.length+1);best[word.length]=[];
  for(let i=word.length-1;i>=0;i--)best[i]=tokens.filter(t=>match(t,i)).map(t=>[t,...best[i+t.length]]).sort(cmp)[0];
  return best[0];
}
export const tokenCount=(words,vocab,greedy=false)=>words.reduce((n,w)=>n+segment(w,vocab,greedy).length,0);

if(typeof document!=='undefined'){
  if(new URLSearchParams(location.search).get('embed')==='book')document.documentElement.dataset.embed='book';
  const $=id=>document.getElementById(id);
  const dom={};for(const key of ['Case','Budget','Scheme','Reset','Status','Metrics','Context','Word','Overlay','Dag','Segments','Certificate','Colours','Manual'])dom[key]=$('ct'+key);
  let data, current, result, chosen=new Set(), manual=false;
  const el=(tag,text,cls)=>{const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;};
  const options=(select,entries,value)=>{select.replaceChildren(...entries.map(([v,label])=>{const o=el('option',label);o.value=v;return o;}));if(value!==undefined)select.value=value;};
  const label=t=>current?.context?.genus?t.join(' → '):t.join('');
  const vocab=()=>current.tokens.filter(t=>chosen.has(tokenKey(t)));
  function resetVocabulary(){
    const scheme=dom.Scheme.value;
    const vs=scheme==='integer'?result.integer.vocabulary:result.lp.rounded[scheme].vocabulary;
    chosen=new Set(vs.map(tokenKey));manual=false;dom.Manual.textContent='';render();
  }
  function chooseBudget(){
    result=current.results.find(r=>r.budget===Number(dom.Budget.value));resetVocabulary();
  }
  function chooseCase(){
    current=data.cases.find(c=>c.id===dom.Case.value);
    options(dom.Budget,current.results.map(r=>[r.budget,String(r.budget)]),current.max_budget);
    options(dom.Word,current.words.map((w,i)=>[i,`${i+1} · ${label(w)}`]),0);
    chooseBudget();
  }
  function render(){
    const vs=vocab(), cost=tokenCount(current.words,vs), greedy=tokenCount(current.words,vs,true);
    const metrics=[['LP lower bound',result.lp.value],['Integer optimum',result.integer.value],['Selected · shortest',cost],['Selected · greedy',greedy],['BPE merge output',result.bpe?.merge_count??'—']];
    dom.Metrics.replaceChildren(...metrics.map(([name,value])=>{const tile=el('div');tile.append(el('strong',String(value)),el('span',name));return tile;}));
    const gap=cost-fraction(result.lp.value);
    dom.Status.textContent=`${manual?'Manual vocabulary':dom.Scheme.selectedOptions[0].textContent}: ${vs.length}/${result.budget} extra token types · ${cost} tokens · ${gap.toFixed(2)} above the certified LP bound.`;
    dom.Context.textContent=current.context.genus?`m = ${current.context.m}, genus ${current.context.genus}; completed order rank ${current.context.order_rank} over k[[u]]. ${current.tokens.length} candidate subpaths of length 2–3; repeated words retain their multiplicity. The bound concerns this restricted candidate set.`:`${current.words.length} words, ${current.tokens.length} distinct candidate substrings; ${current.words.reduce((s,w)=>s+w.length,0)} mandatory-symbol uses before compression.`;
    dom.Colours.replaceChildren(...current.tokens.map((t,i)=>{
      const row=el('tr'), check=el('input');check.type='checkbox';check.checked=chosen.has(tokenKey(t));check.setAttribute('aria-label',`Use token ${label(t)}`);
      check.addEventListener('change',()=>{
        if(check.checked&&chosen.size>=result.budget){check.checked=false;dom.Manual.textContent=`Budget ${result.budget} is full. Uncheck another token first.`;return;}
        if(check.checked)chosen.add(tokenKey(t));else chosen.delete(tokenKey(t));manual=true;dom.Manual.textContent='Manual choice: bounds still refer to the saved corpus and budget.';render();
      });
      const a=el('td');a.append(check);const b=el('td');b.append(el('code',label(t)));
      row.append(a,b,el('td',result.lp.colours[i]),el('td',(fraction(result.lp.colours[i])/t.length).toFixed(4)));return row;
    }));
    dom.Segments.replaceChildren(...current.words.map((w,i)=>{
      const row=el('div',undefined,'ct-row');row.append(el('strong',`${i+1}. ${label(w)}`));const line=el('p');
      for(const t of segment(w,vs))line.append(el('span',label(t),'ct-piece'));
      row.append(line,el('p',`Shortest: ${segment(w,vs).length} · longest-first: ${segment(w,vs,true).length} · detokenization recovers all ${w.length} symbols.`, 'small'));return row;
    }));
    const cert=result.lp.certificate;
    dom.Certificate.textContent=`Exact primal = dual = ${cert.value}\n${result.lp.variables} variables · ${result.lp.equality_rows} flow equations · ${result.lp.inequality_rows} capacity/budget/upper-bound rows\n${result.integer.subsets_checked} integer vocabularies exhausted\nNonzero colour weights: ${current.tokens.map((t,i)=>[label(t),cert.x[result.lp.edges.length+i]]).filter(([,c])=>fraction(c)>0).map(([t,c])=>`${t}: ${c}`).join('; ')}\nNo floating tolerance enters the certificate check. The solver only proposes these rational witnesses.`;
    renderDag();
  }
  function renderDag(){
    const n=Number(dom.Word.value), w=current.words[n], width=900, baseline=230;
    const ns='http://www.w3.org/2000/svg';
    const svg=(tag,attrs,text)=>{const e=document.createElementNS(ns,tag);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=text;return e;};
    const x=i=>45+i*(width-90)/w.length;
    const path=segment(w,vocab());let cursor=0;const active=new Set();
    for(const t of path){active.add(`${cursor}:${cursor+t.length}`);cursor+=t.length;}
    const edges=result.lp.edges.filter(e=>e.word===n);
    dom.Dag.replaceChildren();
    dom.Dag.append(svg('text',{x:20,y:24},dom.Overlay.value==='lp'?`Saved fractional unit flow · word ${n+1}`:`Live shortest path · word ${n+1}`));
    for(const e of edges){
      const isLp=dom.Overlay.value==='lp',flow=fraction(e.flow), on=isLp?flow>0:active.has(`${e.start}:${e.end}`);
      const className=`ct-edge ${on?(isLp?'flow':'active'):''}`;
      const height=e.end-e.start===1?0:35+((e.end-e.start)/w.length)*220;
      const d=`M ${x(e.start)} ${baseline} Q ${(x(e.start)+x(e.end))/2} ${baseline-height} ${x(e.end)} ${baseline}`;
      const edge=svg('path',{d,class:className,tabindex:on?0:-1});
      edge.append(svg('title',{},`${label(e.token)}; positions ${e.start}→${e.end}; LP flow ${e.flow}; capacity ${e.colour===null?'1 (mandatory)':result.lp.colours[e.colour]}`));dom.Dag.append(edge);
    }
    for(let i=0;i<=w.length;i++){
      dom.Dag.append(svg('circle',{cx:x(i),cy:baseline,r:5}),svg('text',{x:x(i),y:baseline+23,'text-anchor':'middle'},i));
      if(i<w.length)dom.Dag.append(svg('text',{x:(x(i)+x(i+1))/2,y:baseline+49,'text-anchor':'middle'},w[i]));
    }
  }
  dom.Case.addEventListener('change',chooseCase);dom.Budget.addEventListener('change',chooseBudget);dom.Scheme.addEventListener('change',resetVocabulary);dom.Reset.addEventListener('click',resetVocabulary);dom.Word.addEventListener('change',renderDag);dom.Overlay.addEventListener('change',renderDag);
  fetch('/data/convextok.json').then(r=>{if(!r.ok)throw Error(`Data HTTP ${r.status}`);return r.json();}).then(d=>{
    if(d.schema!=='grh-convextok-v1'||d.cases.length!==5)throw Error('Unexpected ConvexTok data schema');data=d;
    options(dom.Case,data.cases.map(c=>[c.id,c.label]),'gap');chooseCase();window.convexTokReady=true;
  }).catch(e=>{dom.Status.textContent=`Cannot load verified examples: ${e.message}`;console.error(e);});
}
