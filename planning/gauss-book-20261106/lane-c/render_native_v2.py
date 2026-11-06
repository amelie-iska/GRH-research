#!/usr/bin/env python3
"""Append only the reviewed gauss-tail continuation to the pinned native book.
Candidate output only. All old literal HTML/math/table/tool bytes are preserved.
"""
from pathlib import Path
import argparse, collections, hashlib, html, json, re, shutil, subprocess
import xml.etree.ElementTree as ET
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
PANDOC=Path("/home/iska/miniconda3/envs/tokengt/bin/pandoc")
NS="{http://www.w3.org/1998/Math/MathML}"
THEOREMS={"theorem","proposition","lemma","corollary","definition","example","remark"}
def sha(b): return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True);ap.add_argument("--pdf-build",type=Path,required=True);a=ap.parse_args()
 out=a.output.resolve();pdf=a.pdf_build.resolve()
 assert out.is_relative_to(ROOT/"outputs") and not out.exists()
 out.mkdir(parents=True)
 producer=Path(__file__).read_bytes();(out/"renderer.py").write_bytes(producer)
 sources={}
 def read(name):
  b=(ROOT/name).read_bytes();sources[name]=sha(b);return b.decode()
 maintex=read("book/main.tex")
 names=["book/chapters/gauss-tail-core.tex","book/chapters/gauss-tail-figure.tex","book/chapters/gauss-tail-details.tex"]
 body="\n".join(read(n) for n in names)
 assert r"\input" not in body
 original=maintex.split(r"\begin{document}")[0]+"\n"+r"\begin{document}"+"\n"+body+"\n"+r"\end{document}"+"\n"
 # Established display-only normalization for Pandoc; shared source bytes stay pinned.
 (out/"supplement-original.tex").write_text(original)
 normalized,old_rm=re.subn(r"\\rm\s+([A-Za-z]+)",lambda m:r"\mathrm{"+m[1]+"}",original)
 (out/"supplement.tex").write_text(normalized)
 cmd=["nice","-n","15",str(PANDOC),"--from=latex",str(out/"supplement.tex")]
 ast_run=subprocess.run(cmd+["--to=json"],capture_output=True,text=True,check=True)
 assert not ast_run.stderr.strip(),ast_run.stderr
 ast=json.loads(ast_run.stdout);(out/"supplement.ast.json").write_text(json.dumps(ast,indent=2)+"\n")
 raws=[];maths=[]
 def walk(x):
  if isinstance(x,dict):
   if x.get("t") in {"RawBlock","RawInline"}:raws.append(x)
   if x.get("t")=="Math":maths.append(x["c"][1].strip())
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(ast);assert not raws,raws[:5]
 run=subprocess.run(cmd+["--to=html5","--mathml","--wrap=none","--number-sections"],capture_output=True,text=True,check=True)
 (out/"conversion.log").write_text(run.stdout+run.stderr);assert not run.stderr.strip(),run.stderr
 fragment=run.stdout;(out/"fragment-unresolved.html").write_text(fragment)
 ft=ET.fromstring("<div>"+fragment+"</div>")
 native=list(ft.iter(NS+"math"));assert len(native)==len(maths)>0
 annotations=["".join(x.find(".//"+NS+"annotation").itertext()).strip() for x in native]
 assert annotations==maths,"New MathML source order mismatch"
 pdf_record=json.loads((pdf/"build-record.json").read_text())
 assert pdf_record["passed"] and pdf_record["consume_actual_integrated_book"]
 for n in ["book/main.tex"]+names:assert pdf_record["source_sha256"][n]==sources[n],("PDF/native source mismatch",n)
 pdf_figure={x["path"]:x["sha256"] for x in pdf_record["figure_records"]}
 assert pdf_figure["book/figures/gauss-tail-partition.pdf"]==sha((ROOT/"book/figures/gauss-tail-partition.pdf").read_bytes())
 aux=(pdf/"main.aux").read_bytes()
 labels=dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}",aux.decode()))
 source_labels=re.findall(r"\\label\{([^}]+)\}",body)
 assert len(source_labels)==len(set(source_labels)) and all(x.startswith("gtl:") for x in source_labels)
 assert set(source_labels)<=labels.keys()
 heading_records=[]
 def heading(m):
  attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[2]));ident=attrs.get("id");level=int(m[1])
  assert ident in source_labels,("Unlabelled new heading",m[0])
  number=labels[ident];content=re.sub(r'<span class="header-section-number">.*?</span>\s*',"",m[3],count=1,flags=re.S)
  cls={1:"sectionHead",2:"subsectionHead",3:"subsubsectionHead"}.get(level,"paragraphHead")
  heading_records.append(dict(id=ident,number=number,title=re.sub("<[^>]+>","",content)))
  return '<h'+str(min(6,level+2))+' class="'+cls+'" id="'+ident+'">'+(('<span class="header-section-number">'+number+"</span> ") if level<=3 else "")+content+"</h"+str(min(6,level+2))+">"
 fragment=re.sub(r"<h([1-6])\b([^>]*)>(.*?)</h\1>",heading,fragment,flags=re.S)
 equation_records={}
 existing=set(re.findall(r'\bid="([^"]+)"',fragment))
 def equation(m):
  ann=re.search(r'<annotation encoding="application/x-tex">(.*?)</annotation>',m[0],re.S)
  assert ann
  found=re.findall(r"\\label\{([^}]+)\}",html.unescape(ann[1]))
  if not found:return m[0]
  for ident in found:
   assert ident not in existing;existing.add(ident);equation_records[ident]=labels[ident]
  aliases="".join('<span class="equation-alias" id="'+ident+'"></span>' for ident in found[1:])
  number=", ".join("("+labels[x]+")" for x in found)
  return '<span class="reader-equation" id="'+found[0]+'">'+aliases+m[0]+'<span class="reader-equation-number">'+number+"</span></span>"
 fragment=re.sub(r'<math\b[^>]*display="block".*?</math>',equation,fragment,flags=re.S)
 theorem_records=[]
 def theorem(m):
  attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[1]));kind=attrs.get("class","")
  if kind not in THEOREMS:return m[0]
  ident=attrs.get("id");assert ident in source_labels,("Unlabelled theorem",m[0][:200])
  number=labels[ident]
  block,n=re.subn(r"(<strong>[^<]*?)[0-9]+(?:\.[0-9]+)*(</strong>)",lambda x:x[1]+number+x[2],m[0],count=1)
  assert n==1,(ident,m[0][:200]);theorem_records.append(dict(id=ident,kind=kind,number=number))
  return block
 fragment=re.sub(r"<div\b([^>]*)>.*?</div>",theorem,fragment,flags=re.S)
 references=[]
 def reference(m):
  attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',m[1]));ident=html.unescape(attrs["data-reference"]);kind=attrs["data-reference-type"]
  number=labels[ident];references.append(dict(id=ident,kind=kind,number=number))
  return "<a"+m[1]+">"+("("+number+")" if kind=="eqref" else number)+"</a>"
 fragment=re.sub(r'<a([^>]*data-reference-type="(?:eqref|ref)"[^>]*)>.*?</a>',reference,fragment,flags=re.S)
 figure_gate_rel="outputs/checks/2026-11-06-gauss-book/figure-review-c/acceptance-v1.json"
 figure_gate_bytes=(ROOT/figure_gate_rel).read_bytes()
 assert sha(figure_gate_bytes)=="504fe65c551a510868d78de5961b08c7f66c995bae98ce85d34d3c2d69a5337d"
 figure_gate=json.loads(figure_gate_bytes);assert figure_gate["passed"]
 accepted_figures={Path(n).suffix:row for n,row in figure_gate["staging_assets"].items()}
 fig_assets=[]
 for suffix in [".svg",".pdf",".tex"]:
  name="book/figures/gauss-tail-partition"+suffix;b=(ROOT/name).read_bytes();sources[name]=sha(b)
  assert sha(b)==accepted_figures[suffix]["sha256"] and len(b)==accepted_figures[suffix]["bytes"],"Unreviewed new figure asset"
  if suffix==".pdf":assert b.startswith(b"%PDF")
  if suffix==".svg":
   svg=ET.fromstring(b);assert svg.tag.rsplit("}",1)[-1]=="svg"
   for e in svg.iter():
    assert e.tag.rsplit("}",1)[-1]!="script"
    assert not any(k.lower().startswith("on") for k in e.attrib)
    assert not any(k.rsplit("}",1)[-1]=="href" and not v.startswith("#") for k,v in e.attrib.items())
  fig_assets.append(dict(source=name,target="figures/"+Path(name).name,sha256=sha(b),bytes=len(b)))
 def figure(m):
  tag=m[0].replace("<embed","<img",1).replace('src="figures/gauss-tail-partition.pdf"','src="figures/gauss-tail-partition.svg"')
  tag=re.sub(r'\s+type="application/pdf"',"",tag)
  alt="Exact short-divisor cutoff partition, physical cubic interaction and open small-cutoff moment"
  if re.search(r'\balt="[^"]*"',tag):tag=re.sub(r'\balt="[^"]*"','alt="'+alt+'"',tag,count=1)
  else:tag=tag.replace("<img ",'\x3cimg alt="'+alt+'" ',1)
  # Preserve the exact new SVG palette under the inherited global night filter.
  # This callback runs only for the hash-bound new Gauss-tail figure.
  style=re.search(r'\bstyle="([^"]*)"',tag)
  extra="filter:none!important;background-color:#fff;"
  if style:
   value=html.unescape(style[1]).rstrip("; ")+";"+extra
   tag=tag[:style.start(1)]+html.escape(value,quote=True)+tag[style.end(1):]
  else:tag=tag.replace("<img ",'<img style="'+extra+'" ',1)
  assert len(re.findall(r'\bstyle=',tag))<=1,"Duplicate new figure style attribute"
  return '<span class="reader-figure-scroll" role="region" tabindex="0" aria-label="Gauss-tail cutoff partition; horizontal scrolling on small screens">'+tag+'</span><span class="source-links"><a href="figures/gauss-tail-partition.tex">Original figure TeX</a> · <a href="figures/gauss-tail-partition.pdf">Source-matched figure PDF</a></span>'
 fragment,nfig=re.subn(r'<(?:img|embed)\b[^>]*\bsrc="figures/gauss-tail-partition\.pdf"[^>]*>',figure,fragment)
 assert nfig==1,nfig
 figure_number=labels["gtl:partition"]
 fragment,ncaption=re.subn(r"<figcaption>",'<figcaption><strong>Figure '+figure_number+'.</strong> ',fragment)
 assert ncaption==1 and ('<figcaption><strong>Figure '+figure_number+'.</strong> ') in fragment
 # Pandoc represents figure labels on figure containers; the PDF number is authoritative.
 for ident in re.findall(r"\\label\{([^}]+)\}",read("book/chapters/gauss-tail-figure.tex")):
  assert ident in labels
 source_count=len(re.findall(r"\\begin\{(?:theorem|lemma|proposition|corollary|definition|example|remark)\}",body))
 assert source_count==len(theorem_records),(source_count,len(theorem_records))
 proofs=len(re.findall(r"\\begin\{proof\}",body));assert proofs==len(re.findall(r"<em>Proof",fragment)),(proofs,len(re.findall(r"<em>Proof",fragment)))
 oldbytes=(ROOT/"web/book/main.html").read_bytes();baseline=oldbytes.decode();(out/"baseline-book.html").write_bytes(oldbytes)
 before=json.loads((ROOT/"outputs/checks/2026-11-06-gauss-book/root/integration-before-v1.json").read_text())
 assert sha(oldbytes)==before["source_and_live_before"]["web/book/main.html"]["sha256"]
 assert sha((ROOT/"outputs/checks/2026-11-06-gauss-book/root/integration-before-v1.json").read_bytes())=="a8953053d4296a0c699611945a8f870b65967a8c63cacff48a5c3d06cd1036b5"
 assert (before["old_math"],before["old_tables"],before["old_labs"],before["old_svg_refs"])==(9810,389,14,30)
 assert ".reader-figure-scroll{" in baseline and "min-width:720px" in baseline,"Missing preserved mobile figure scrolling rule"
 old_ids=set(re.findall(r'\bid="([^"]+)"',baseline));new_ids=re.findall(r'\bid="([^"]+)"',fragment)
 assert len(new_ids)==len(set(new_ids)),[x for x,c in collections.Counter(new_ids).items() if c>1]
 for ident in sorted(set(new_ids)&old_ids):
  assert ident not in source_labels
  fragment=fragment.replace('id="'+ident+'"','id="gtl-auto-'+ident+'"').replace('href="#'+ident+'"','href="#gtl-auto-'+ident+'"')
 ids=set(re.findall(r'\bid="([^"]+)"',fragment))
 assert set(source_labels)<=ids,("Lost labels",set(source_labels)-ids)
 assert not old_ids&ids
 for ident in re.findall(r'href="#([^"]+)"',fragment):assert html.unescape(ident) in ids|old_ids,("Missing reference",ident)
 tables=re.findall(r"<table\b[^>]*>.*?</table>",fragment,re.S)
 assert not tables,"Unexpected new table outside the reviewed Gauss-tail source"
 fragment=re.sub(r"<table\b[^>]*>.*?</table>",lambda m:'<div class="reader-table-scroll" tabindex="0" aria-label="Gauss-tail proof table; horizontal scrolling">'+m[0]+"</div>",fragment,flags=re.S)
 assert re.findall(r"<table\b[^>]*>.*?</table>",fragment,re.S)==tables
 nav='<nav aria-label="Reviewed Gauss-tail continuation"><strong>Chapter 40 continuation: arithmetic Gauss tails</strong><p>Actual short-divisor tail bounds and original finite-cutoff reductions; the remaining small-cutoff moment and full signed kernel stay open.</p><p><a href="#gtl:core">Results and scopes</a> · <a href="#gtl:details">Complete proofs</a> · <a href="../book.pdf">Complete book PDF</a></p></nav>'
 links='<p class="source-links">Shared TeX sources: '+' · '.join('<a href="sources/'+Path(n).name+'">'+Path(n).name+'</a>' for n in names)+'</p>'
 insertion='<section class="new-reviewed-chapters" id="gauss-tail-section">'+nav+links+fragment+"</section>\n"
 headings=list(re.finditer(r"<h2\b[^>]*>.*?</h2>",baseline,re.S))
 bib=[m for m in headings if " ".join(html.unescape(re.sub("<[^>]+>"," ",m[0])).split())=="Bibliography"];assert len(bib)==1
 date=re.search(r"\\date\{([^}]+)\}",maintex)[1]
 assert date=="November 6, 2026" and baseline.count(date)==1,"Unexpected existing date; never rewrite old HTML"
 combined=baseline[:bib[0].start()]+insertion+baseline[bib[0].start():]
 toc_add='<br /><span class="sectionToc"><a href="#gtl:core">40 · Arithmetic Gauss tails and finite-cutoff reductions</a></span>'
 toc=re.search(r'<div class="tableofcontents">.*?</div>',combined,re.S);assert toc
 combined=combined[:toc.end()-6]+toc_add+combined[toc.end()-6:]
 restored=combined.replace(insertion,"",1).replace(toc_add,"",1)
 assert restored==baseline,"Non-additive old HTML change"
 tree=ET.fromstring(combined);oldtree=ET.fromstring(baseline)
 oldmath=re.findall(r"<math\b[^>]*>.*?</math>",baseline,re.S);allmath=re.findall(r"<math\b[^>]*>.*?</math>",combined,re.S)
 assert len(oldmath)==9810
 pos=0
 for value in oldmath:
  while pos<len(allmath) and allmath[pos]!=value:pos+=1
  assert pos<len(allmath),"Old literal MathML changed"
  pos+=1
 assert len(list(oldtree.iter("table")))==389
 assert re.findall(r"<table\b[^>]*>.*?</table>",combined,re.S)==re.findall(r"<table\b[^>]*>.*?</table>",baseline,re.S),"Old literal table bytes/order changed"
 oldframes=[ET.tostring(e) for e in oldtree.iter("iframe")];frames=[ET.tostring(e) for e in tree.iter("iframe")]
 assert len(oldframes)==14 and frames==oldframes
 oldrefs=re.findall(r'(?:src|data)="([^"]+\.svg)"',baseline);newrefs=re.findall(r'(?:src|data)="([^"]+\.svg)"',combined)
 assert len(oldrefs)==30 and newrefs[:30]==oldrefs and len(newrefs)==31
 malformed=[]
 for e in ET.fromstring("<div>"+fragment+"</div>").iter():
  tag=e.tag.rsplit("}",1)[-1]
  if tag in {"msub","msup","munder","mover"} and len(e)!=2:malformed.append(tag)
  if tag in {"msubsup","munderover"} and len(e)!=3:malformed.append(tag)
 assert not malformed,malformed
 target=out/"book";shutil.copytree(ROOT/"web/book",target);(target/"main.html").write_text(combined)
 for n in names:(target/"sources"/Path(n).name).write_bytes((ROOT/n).read_bytes())
 for item in fig_assets:
  p=target/item["target"];p.parent.mkdir(exist_ok=True,parents=True);p.write_bytes((ROOT/item["source"]).read_bytes())
 old_assets=before["old_book_assets_sha256"]
 assert len(old_assets)==86
 assert {str(p.relative_to(ROOT)) for p in (ROOT/"web/book").rglob("*") if p.is_file()}==set(old_assets),"Old asset inventory changed"
 unchanged={}
 for name,digest in old_assets.items():
  # The snapshot uses paths relative to web/book (or the repository).
  rel=name.removeprefix("web/book/")
  if rel=="main.html":continue
  assert sha((target/rel).read_bytes())==digest,(name,"Changed old asset")
  unchanged[name]=digest
 (out/"fragment-resolved.html").write_text(fragment)
 assert all(sha((ROOT/n).read_bytes())==digest for n,digest in sources.items())
 assert Path(__file__).read_bytes()==producer
 rec=dict(passed=True,native_MathML=True,new_chapters=0,chapter_count=40,math_nodes_added=len(maths),math_nodes=len(allmath),old_literal_math_subtrees=9810,old_math_byte_identical=True,old_HTML_restored_exactly=True,date_unchanged=True,old_tables=389,tables=len(list(tree.iter("table"))),canonical_labs=14,old_canonical_labs=14,old_svg_refs=30,svg_refs=31,old_assets_unchanged=unchanged,figure_assets=fig_assets,figure_semantic_gate_sha256=sha(figure_gate_bytes),new_figure_theme_filter="none!important;whitecanvas",headings=heading_records,theorems=theorem_records,equations=equation_records,proof_environments=proofs,references=references,source_sha256=sources,pdf_aux_sha256=sha(aux),PDF_build_record_sha256=sha((pdf/"build-record.json").read_bytes()),figure_number=figure_number,pandoc_sha256=sha(PANDOC.read_bytes()),old_HTML_sha256=sha(oldbytes),new_HTML_sha256=sha(combined.encode()),renderer_sha256=sha(producer),production_promoted=False,new_Lean_declarations=0,raw_TeX_nodes=0,conversion_warnings=0,normalizations={"old_rm":old_rm},source_formula_impact="Only new display syntax rm-to-mathrm; all old literal MathML preserved.")
 (out/"native-build-record.json").write_text(json.dumps(rec,indent=2)+"\n")
 print(json.dumps({k:rec[k] for k in ["passed","math_nodes","math_nodes_added","tables","canonical_labs","svg_refs","production_promoted"]}))
if __name__=="__main__":main()
