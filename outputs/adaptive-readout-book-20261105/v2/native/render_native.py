#!/usr/bin/env python3
"""Append reviewed native-MathML chapters without rewriting old subtrees.

Uses existing Pandoc3.10 in tokengt. Fails on warnings/raw TeX/missing refs.
Never promotes production. Numbering comes from the complete PDF aux.
"""
from pathlib import Path
import argparse, collections, hashlib, html, json, re, shutil, subprocess
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
PANDOC=Path('/home/iska/miniconda3/envs/tokengt/bin/pandoc')
MATHNS='{http://www.w3.org/1998/Math/MathML}'
THEOREMS={'theorem','proposition','lemma','corollary','definition','example','remark'}
def sha(x):return hashlib.sha256(x).hexdigest()
def normalizations(t):
    counts={}
    t,counts['old_rm']=re.subn(r'\\rm\s+([A-Za-z]+)',lambda m:r'\mathrm{'+m[1]+'}',t)
    counts['hbox']=t.count(r'\hbox{');t=t.replace(r'\hbox{',r'\text{')
    counts['notag']=t.count(r'\notag');t=t.replace(r'\notag','')
    counts['atop']=0
    while r'\atop' in t:
        at=t.index(r'\atop');stack=[];pos=0
        while pos<at:
            if t[pos]=='\\':pos+=2;continue
            if t[pos]=='{':stack.append(pos)
            elif t[pos]=='}':stack.pop()
            pos+=1
        left=stack[-1];depth=1;pos=left+1
        while depth:
            if t[pos]=='\\':pos+=2;continue
            if t[pos]=='{':depth+=1
            elif t[pos]=='}':depth-=1
            pos+=1
        right=pos-1;top=t[left+1:at];bottom=t[at+len(r'\atop'):right]
        t=t[:left]+r'{\substack{'+top+r'\\'+bottom+'}}'+t[right+1:];counts['atop']+=1
    return t,counts

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',required=True,type=Path);ap.add_argument('--pdf-build',required=True,type=Path);ap.add_argument('--baseline-book',type=Path);a=ap.parse_args()
    out=a.output.resolve();pdf=a.pdf_build.resolve()
    if out.exists():raise FileExistsError('Preserve prior attempts')
    out.mkdir(parents=True);producer=Path(__file__).read_bytes();(out/'render_native.py').write_bytes(producer)
    sources={}
    def read(p):
        data=p.read_bytes();sources[str(p.relative_to(ROOT))]=sha(data);return data.decode()
    def expand(t):return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(read(ROOT/'book'/(m[1]+'.tex'))),t)
    main_source=read(ROOT/'book/main.tex');preamble=main_source.split(r'\begin{document}')[0]
    wrappers=['validated-oracle','masked-moment','weighted-cutoff']
    body='\n'.join(expand(read(ROOT/'book/chapters'/(n+'.tex'))) for n in wrappers)
    raw_source=preamble+'\\begin{document}\n'+body+'\n\\end{document}\n'
    normalized,changes=normalizations(raw_source);(out/'supplement-original.tex').write_text(raw_source);(out/'supplement-normalized.tex').write_text(normalized)
    base=['nice','-n','15',str(PANDOC),'--from=latex',str(out/'supplement-normalized.tex')]
    run=subprocess.run(base+['--to=json'],capture_output=True,text=True,check=True)
    if run.stderr.strip():raise RuntimeError('AST conversion warnings: '+run.stderr)
    ast=json.loads(run.stdout);(out/'supplement.ast.json').write_text(json.dumps(ast,indent=2)+'\n')
    raw=[];math_nodes=[]
    def walk(x):
        if isinstance(x,dict):
            if x.get('t') in {'RawBlock','RawInline'}:raw.append(x)
            if x.get('t')=='Math':math_nodes.append(x['c'][1].strip())
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(ast)
    if raw:raise RuntimeError('Raw TeX AST fallback: '+repr(raw[:5]))
    run=subprocess.run(base+['--to=html5','--mathml','--wrap=none','--number-sections','--number-offset=37','-o',str(out/'fragment-unresolved.html')],capture_output=True,text=True,check=True)
    (out/'conversion.log').write_text(run.stdout+run.stderr)
    if run.stderr.strip():raise RuntimeError('Native conversion warnings: '+run.stderr)
    fragment=(out/'fragment-unresolved.html').read_text()
    assert 'class="math inline"' not in fragment and 'class="math display"' not in fragment
    tree=ET.fromstring('<div>'+fragment+'</div>')
    actual_math=[x for x in tree.iter(MATHNS+'math')]
    assert len(actual_math)==len(math_nodes)>0
    annotations=[''.join(x.find('.//'+MATHNS+'annotation').itertext()).strip() for x in actual_math]
    assert collections.Counter(annotations)==collections.Counter(math_nodes),'Math AST/annotation mismatch'
    aux=(pdf/'main.aux').read_text();labels=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',aux))
    source_labels=re.findall(r'\\label\{([^}]+)\}',body)
    assert len(set(source_labels))==len(source_labels)
    assert set(source_labels)<=labels.keys()
    section_numbers={}
    for m in re.finditer(r'<h([1-6])\b([^>]*)>.*?</h\1>',fragment,re.S):
        attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[2]));ident=attrs.get('id')
        if ident in source_labels:
            assert attrs.get('data-number')==labels[ident],(ident,attrs,labels[ident])
            section_numbers[ident]=labels[ident]
    existing_ids=set(re.findall(r'\bid="([^"]+)"',fragment));equation_numbers={}
    def equation(m):
        tex=html.unescape(re.search(r'<annotation encoding="application/x-tex">(.*?)</annotation>',m[0],re.S)[1])
        found=re.findall(r'\\label\{([^}]+)\}',tex)
        if not found:return m[0]
        assert len(set(found))==len(found)
        for x in found:assert x not in existing_ids;existing_ids.add(x);equation_numbers[x]=labels[x]
        aliases=''.join('<span id="'+html.escape(x,quote=True)+'" class="equation-alias"></span>' for x in found[1:])
        tag=', '.join('('+labels[x]+')' for x in found)
        return '<span class="reader-equation" id="'+html.escape(found[0],quote=True)+'">'+aliases+m[0]+'<span class="reader-equation-number">'+html.escape(tag)+'</span></span>'
    fragment=re.sub(r'<math\b[^>]*display="block".*?</math>',equation,fragment,flags=re.S)
    chapters=[(m.start(),int(m[1])) for m in re.finditer(r'<h1 data-number="(\d+)"',fragment)]
    assert [x[1] for x in chapters]==[38,39,40]
    counters=collections.defaultdict(int);theorem_records=[]
    def theorem(m):
        block=m[0];attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[1]));cls=attrs.get('class','')
        if cls not in THEOREMS:return block
        chapter=max(number for pos,number in chapters if pos<m.start());counters[chapter]+=1
        number=str(chapter)+'.'+str(counters[chapter]);ident=attrs.get('id')
        if ident:assert labels[ident]==number,(ident,labels[ident],number)
        block,n=re.subn(r'(<strong>[^<]*?)[0-9]+\.[0-9]+(</strong>)',lambda x:x[1]+number+x[2],block,count=1);assert n==1
        theorem_records.append(dict(kind=cls,id=ident,number=number));return block
    fragment=re.sub(r'<div\b([^>]*)>.*?</div>',theorem,fragment,flags=re.S)
    references=[]
    def reference(m):
        attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[1]));ident=html.unescape(attrs['data-reference'])
        number=labels[ident];kind=attrs['data-reference-type'];value='('+number+')' if kind=='eqref' else number
        references.append(dict(id=ident,number=number,kind=kind));return '<a'+m[1]+'>'+html.escape(value)+'</a>'
    fragment=re.sub(r'<a([^>]*data-reference-type="(?:eqref|ref)"[^>]*)>.*?</a>',reference,fragment,flags=re.S)
    def heading(m):
        level=int(m[1])+1;attrs=m[2];content=m[3];cls={2:'chapterHead',3:'sectionHead',4:'subsectionHead',5:'subsubsectionHead'}.get(level,'paragraphHead')
        if level>=6:
            # PDF paragraph headings are unnumbered; Pandoc otherwise emits40.5.0.0.2.
            attrs=re.sub(r' data-number="[^"]*"','',attrs)
            content=re.sub(r'<span class="header-section-number">.*?</span>\s*','',content,count=1,flags=re.S)
        return '<h'+str(level)+' class="'+cls+'"'+attrs+'>'+content+'</h'+str(level)+'>'
    fragment=re.sub(r'<h([1-6])\b([^>]*)>(.*?)</h\1>',heading,fragment,flags=re.S)
    baseline=a.baseline_book.resolve() if a.baseline_book else ROOT/'web/book/main.html'
    old_original=baseline.read_text();(out/'baseline-book.html').write_text(old_original)
    assert len(re.findall(r'<h2 class="chapterHead">',old_original))==37, 'Expected pinned37-chapter baseline; use --baseline-book after promotion'
    old=old_original
    old_guide='The private\nrepository remains the authoritative source.'
    new_guide='The public repository and its project page provide the authoritative source and hosted companion.'
    assert old.count(old_guide)==1
    old=old.replace(old_guide,new_guide)
    assert old.count('November 3, 2026')==1
    edition_date=re.search(r'\\date\{([^}]+)\}',main_source).group(1)
    old=old.replace('November 3, 2026',edition_date)
    editorial_changes=[{'old':old_guide,'new':new_guide},{'old':'November 3, 2026','new':edition_date}]
    old_ids=set(re.findall(r'\bid="([^"]+)"',old));new_ids=re.findall(r'\bid="([^"]+)"',fragment)
    assert len(set(new_ids))==len(new_ids)
    for ident in sorted(set(new_ids)&old_ids):
        assert ident not in source_labels,'New explicit label collides with old document'
        fragment=fragment.replace('id="'+ident+'"','id="new-'+ident+'"').replace('href="#'+ident+'"','href="#new-'+ident+'"')
    ids=set(re.findall(r'\bid="([^"]+)"',fragment))
    assert set(source_labels)<=ids,'Lost explicit TeX labels: '+repr(set(source_labels)-ids)
    assert not old_ids.intersection(ids)
    for ident in re.findall(r'href="#([^"]+)"',fragment):assert html.unescape(ident) in ids|old_ids, 'Missing reference '+ident
    assert not re.search(r'\[(?:mm|rc|wc):[^\]]+\]',re.sub(r'<annotation.*?</annotation>','',fragment,flags=re.S))
    source_count=len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|definition|example|remark)\}',body));assert source_count==len(theorem_records)
    proof_count=len(re.findall(r'\\begin\{proof\}',body));assert proof_count==len(re.findall(r'<em>Proof',fragment))
    css='<style>.reader-display-math{display:block;min-width:0;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}.reader-display-math:focus-visible{outline:2px solid #078b96;outline-offset:3px}.new-reviewed-chapters{margin-top:3rem}.reader-equation{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:.5rem;max-width:100%;position:relative}.reader-equation>math{min-width:0;max-width:100%;overflow-x:auto}.reader-equation-number{font-size:.85em;white-space:nowrap}.equation-alias{position:absolute;width:0;height:0}.new-reviewed-chapters nav{padding:1rem;border:1px solid currentColor;border-radius:.5rem}.new-reviewed-chapters table{max-width:100%}.new-reviewed-chapters .source-links{font-size:.85em}.new-reviewed-chapters .paragraphHead{font-size:1em;font-weight:700}</style>'
    chapter_links=[]
    for match in re.finditer(r'<h2 class="chapterHead"([^>]*)>(.*?)</h2>',fragment,re.S):
        ident=re.search(r'\bid="([^"]+)"',match[1])[1]
        title=' '.join(html.unescape(re.sub(r'<[^>]+>',' ',match[2])).split())
        chapter_links.append((ident,title))
    assert len(chapter_links)==3
    nav='<nav aria-label="New reviewed chapters"><strong>New reviewed chapters38–40</strong><p>Finite interval certificates and scoped prose arithmetic results; selected older Lean checks do not formalize these new theorems. GRH remains open.</p><ul>'+''.join('<li><a href="#'+ident+'">Chapter '+html.escape(title)+'</a></li>' for ident,title in chapter_links)+'</ul><p><a href="../book.pdf">Complete book PDF</a> · <a href="../learned.html#certified-learning">Canonical analytic learning laboratory</a></p></nav>'
    part_match=re.search(r'\\part\{([^}]+)\}\s*\\input\{chapters/validated-oracle\}',main_source)
    assert part_match
    part_header='<h1 class="partHead" id="new-certified-analytic-targets">Part VI: '+html.escape(part_match[1])+'</h1>'
    toc_addition='<br /><span class="partToc"><a href="#new-certified-analytic-targets">VI '+html.escape(part_match[1])+'</a></span>'+''.join('<br /><span class="chapterToc"><a href="#'+ident+'">'+html.escape(title)+'</a></span>' for ident,title in chapter_links)

    source_links='<p class="source-links">Shared TeX sources: '+ ' · '.join('<a href="sources/'+Path(name).name+'">'+html.escape(Path(name).name)+'</a>' for name in sources if name.startswith('book/chapters/') and Path(name).name not in [x+'.tex' for x in wrappers])+'</p>'
    insertion='<section class="new-reviewed-chapters" id="new-reviewed-chapters">'+css+'<script defer="defer" src="reviewed-math-scroll.js"></script>'+part_header+nav+source_links+fragment+'</section>\n'
    headings=list(re.finditer(r'<h2\b[^>]*>.*?</h2>',old,re.S))
    matches=[m for m in headings if ' '.join(html.unescape(re.sub(r'<[^>]+>',' ',m[0])).split())=='Bibliography']
    assert len(matches)==1;marker=matches[0]
    old_numbered=[m for m in headings if m[0].startswith('<h2 class="chapterHead">')]
    assert len(old_numbered)==37 and marker.start()>old_numbered[-1].end()
    combined=old[:marker.start()]+insertion+old[marker.start():]
    toc=re.search(r'<div class="tableofcontents">.*?</div>',combined,re.S);assert toc
    combined=combined[:toc.end()-6]+toc_addition+combined[toc.end()-6:]
    restored=combined.replace(insertion,'',1).replace(toc_addition,'',1)
    assert restored==old
    for change in reversed(editorial_changes):restored=restored.replace(change['new'],change['old'],1)
    assert restored==old_original
    parsed=ET.fromstring(combined);old_tree=ET.fromstring(old_original)
    chapter_sequence=[]
    for el in parsed.iter('h2'):
        if el.attrib.get('class')!='chapterHead':continue
        title=' '.join(el.itertext()).strip()
        chapter_sequence.append(int(re.search(r'(?:Chapter\s*)?(\d+)',title)[1]))
    assert chapter_sequence==list(range(1,41)),chapter_sequence

    new_frames=[x.attrib.get('src') for x in parsed.iter('iframe')];old_frames=[x.attrib.get('src') for x in old_tree.iter('iframe')]
    assert new_frames==old_frames and len(new_frames)==len(set(new_frames))==13
    preservation={}
    for tag in ['math','table','iframe']:
        before=[ET.tostring(x,encoding='unicode') for x in old_tree.iter() if x.tag.split('}')[-1]==tag]
        after=[ET.tostring(x,encoding='unicode') for x in parsed.iter() if x.tag.split('}')[-1]==tag]
        pos=0
        for value in before:
            while pos<len(after) and after[pos]!=value:pos+=1
            assert pos<len(after),'Old subtree changed: '+tag
            pos+=1
        preservation[tag]={'old_count':len(before),'new_count':len(after),'old_subtrees_unchanged':True,'old_serialized_sha256':sha('\n'.join(before).encode())}
    target=out/'book';shutil.copytree(ROOT/'web/book',target);(target/'main.html').write_text(combined);srcdir=target/'sources';srcdir.mkdir(exist_ok=True)
    responsive=(Path(__file__).parent/'reviewed-math-scroll.js').read_bytes();(target/'reviewed-math-scroll.js').write_bytes(responsive)
    for name in sources:
        if name.startswith('book/chapters/'):(srcdir/Path(name).name).write_bytes((ROOT/name).read_bytes())
    (out/'fragment-resolved.html').write_text(fragment)
    assert all(sha((ROOT/name).read_bytes())==value for name,value in sources.items()),'Source changed during conversion'
    assert Path(__file__).read_bytes()==producer
    record=dict(passed=True,new_chapters=[38,39,40],math_nodes=len(math_nodes),raw_TeX_nodes=0,conversion_warnings=0,source_sha256=sources,normalizations=changes,
        explicit_labels=len(source_labels),equation_numbers=equation_numbers,theorems=theorem_records,resolved_references=references,proof_environments=proof_count,
        old_HTML_sha256=sha(old_original.encode()),new_HTML_sha256=sha(combined.encode()),preservation=preservation,canonical_labs=13,
        baseline=str(baseline),intentional_old_prose_changes=editorial_changes,numbered_chapter_sequence=chapter_sequence,new_toc_entries=3,
        pdf_aux_sha256=sha((pdf/'main.aux').read_bytes()),pandoc_path=str(PANDOC),pandoc_sha256=sha(PANDOC.read_bytes()),renderer_sha256=sha(producer),
        responsive_runtime_sha256=sha(responsive),responsive_runtime='Additive HTML scroll containers for overflow measured by MathML scrollWidth; preserves all old static subtrees/runtime and full math font sizes.',native_MathML=True,new_Lean_declarations=0,production_promoted=False,
        scope='Only new reviewed chapter syntax is normalized for existing Pandoc. Old document subtrees remain unchanged; equations/theorems/refs use full PDF aux. Candidate only.')
    (out/'native-build-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:record[k] for k in ['passed','math_nodes','raw_TeX_nodes','conversion_warnings','explicit_labels','proof_environments','canonical_labs','production_promoted']},indent=2))

if __name__=='__main__':main()
