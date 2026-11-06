#!/usr/bin/env python3
"""Guarded source integration only, no assembler rerun or output promotion."""
from pathlib import Path
import argparse, hashlib, json, re
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument("--math-review",required=True,type=Path);p.add_argument("--review-sha",required=True);p.add_argument("--figure-receipt",required=True,type=Path);p.add_argument("--figure-receipt-sha",required=True);a=p.parse_args()
 out=ROOT/"outputs/checks/2026-11-06-coherent-book/root/source-integration-v1.json";assert not out.exists()
 raw=a.math_review.read_bytes();assert sha(raw)==a.review_sha;review=json.loads(raw);assert review["accepted"] is True and not review.get("unresolved_findings",[])
 for n in ["papers/coherent-band-core.tex","papers/coherent-band-details.tex"]:
  assert sha((ROOT/n).read_bytes())==review["reviewed_sources"][n]
 figraw=a.figure_receipt.read_bytes();assert sha(figraw)==a.figure_receipt_sha
 fig=json.loads(figraw);assert fig.get("passed",fig.get("accepted")) is True
 for suffix in [".svg",".pdf",".tex"]:
  name="book/figures/coherent-band-workflow"+suffix;data=(ROOT/name).read_bytes();assert sha(data)==fig["outputs"][name]["sha256"] and len(data)==fig["outputs"][name]["bytes"]
 visual=json.loads((ROOT/"outputs/checks/2026-11-06-coherent-book/root/figure-visual-v1.json").read_text());assert visual["accepted"] and visual["author_receipt_sha256"]==a.figure_receipt_sha
 before=json.loads((ROOT/"outputs/checks/2026-11-06-coherent-book/root/integration-before-v1.json").read_text())
 edits=[];pending={}
 def edit(name,transform):
  path=ROOT/name;old=path.read_bytes();assert sha(old)==before["source_and_live_before"][name]["sha256"],("Concurrent change",name)
  new=transform(old.decode()).encode();assert new!=old
  edits.append(dict(path=name,before=sha(old),after=sha(new)));pending[name]=new
 for name in ["coherent-band-core","coherent-band-details"]:
  target=ROOT/("book/chapters/"+name+".tex");assert not target.exists()
  data=b"% Generated shared reviewed material.\n"+(ROOT/("papers/"+name+".tex")).read_bytes();pending[str(target.relative_to(ROOT))]=data;edits.append(dict(path=str(target.relative_to(ROOT)),before=None,after=sha(data)))
 figure=ROOT/"book/chapters/coherent-band-figure.tex";assert not figure.exists()
 figtex=r"""\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/coherent-band-workflow.pdf}
\caption{A source-bound finite Schur replay. All three cases retain the full
$14\times29$ matrix and every support zero; the workflow distinguishes
saved numerical consistency values from analytic uniform bounds.
The full signed unequal-norm kernel remains open.}
\label{cbk:workflow}
\end{figure}
"""
 pending[str(figure.relative_to(ROOT))]=figtex.encode();edits.append(dict(path=str(figure.relative_to(ROOT)),before=None,after=sha(figtex.encode())))
 addition="\n"+r"\input{chapters/coherent-band-core}"+"\n"+r"\input{chapters/coherent-band-figure}"+"\n"+r"\input{chapters/coherent-band-details}"+"\n"
 edit("book/chapters/weighted-cutoff.tex",lambda t:t+addition)
 def assemble(t):
  old="'physical-sieve-core','physical-sieve-details']:"
  new="'physical-sieve-core','physical-sieve-details','coherent-band-core','coherent-band-details']:"
  assert t.count(old)==1;return t.replace(old,new)
 edit("scripts/assemble_book.py",assemble)
 def maintex(t):
  assert t.count(r"\date{November 5, 2026}")==1;return t.replace(r"\date{November 5, 2026}",r"\date{November 6, 2026}")
 edit("book/main.tex",maintex)
 abstract=" Primitive root normalization, all-component finite dual prefixes, actual-cutoff Schur transfer and a full equal-norm localization retain the coherent unequal-norm target as an open problem."
 for name in ["resolutions-concise","resolutions-extended","validated-oracle-concise","validated-oracle-extended"]:
  def wrapper(t,name=name):
   old=r"\input{physical-sieve-details}" if name.endswith("extended") else r"\input{physical-sieve-core}"
   assert t.count(old)==1
   new=old+"\n"+r"\input{coherent-band-core}"+("\n"+r"\input{coherent-band-details}" if name.endswith("extended") else "")
   t=t.replace(old,new)
   assert t.count(r"\end{abstract}")==1;t=t.replace(r"\end{abstract}",abstract+r"\end{abstract}")
   date_before,date_after=("5 November 2026","6 November 2026") if name.startswith("validated-oracle") else ("November 5, 2026","November 6, 2026")
   assert t.count(date_before)==1;t=t.replace(date_before,date_after)
   return t
  edit("papers/"+name+".tex",wrapper)
 def prepare(t):
  old="assert count==13, 'Expected thirteen unique canonical laboratories, including complementary physical datasets'"
  assert t.count(old)==1
  panel="""def coherent_band_panel(m):
 global count
 heading=m[0];text=' '.join(re.sub('<[^>]+>',' ',heading).lower().split())
 if 'coherent dual bands, actual cutoffs and arithmetic localization' not in text:return heading
 count+=1
 return heading+'<aside class="reader-lab" id="lab-coherent-band"><h3>Finite Schur matrix inspector</h3><p>All three saved 14 × 29 auxiliary matrices retain generators, factors, actual cutoff coefficients, complex values and raw zeros. Saved 55-digit values are numerical consistency checks, not interval certificates or a full signed-kernel estimate.</p><p><a href="/coherent-band.html">Open the matrix inspector separately</a></p><iframe loading="lazy" src="/coherent-band.html?embed=book" title="Actual finite Schur matrices and state values" height="1120"></iframe></aside>'
s=re.sub(r'<h3 class="sectionHead">.*?</h3>',coherent_band_panel,s,flags=re.S)
assert count==14, 'Expected fourteen unique canonical laboratories, including the finite Schur replay'
"""
  return t.replace(old,panel.rstrip())
 edit("scripts/prepare_book_html.py",prepare)
 # The old general assembler has intentionally not been executed.
 for n in ["scripts/assemble_book.py","scripts/prepare_book_html.py"]:compile(pending[n].decode(),n,"exec")
 def expand(name,base):
  t=pending[name].decode() if name in pending else (ROOT/name).read_text()
  return re.sub(r"\\input\{([^}]+)\}",lambda m:expand(str((Path(base)/(m[1]+".tex")).as_posix()),base),t)
 checks={}
 for name in ["resolutions-concise","resolutions-extended","validated-oracle-concise","validated-oracle-extended"]:
  text=expand("papers/"+name+".tex","papers")
  labels=re.findall(r"\\label\{([^}]+)\}",text);assert len(labels)==len(set(labels))
  refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",text);assert set(refs)<=set(labels),(name,set(refs)-set(labels))
  checks[name]=dict(labels=len(labels),references=len(refs),expanded_sha256=sha(text.encode()),core=True,details=name.endswith("extended"))
 book=expand("book/main.tex","book");labels=re.findall(r"\\label\{([^}]+)\}",book);assert len(labels)==len(set(labels))
 assert len(re.findall(r"\\chapter(?:\[[^\]]*\])?\{",book))==40
 assert all(n in book for n in [r"\label{cbk:core}",r"\label{cbk:details}",r"\label{cbk:workflow}"])
 checks["book"]=dict(labels=len(labels),chapter_count=40,expanded_sha256=sha(book.encode()))
 for item in edits:
  path=ROOT/item["path"];current=sha(path.read_bytes()) if path.exists() else None;assert current==item["before"],("Concurrent change before write",item["path"])
 for name,data in pending.items():(ROOT/name).write_bytes(data)
 record=dict(passed=True,producer_sha256=sha(Path(__file__).read_bytes()),edits=edits,closure=checks,math_review_sha256=a.review_sha,figure_receipt_sha256=a.figure_receipt_sha,general_assembler_executed=False,old_live_outputs_edited=False,index_edited=False,new_Lean_declarations=0)
 out.write_text(json.dumps(record,indent=2)+"\n");print(json.dumps(dict(passed=True,edits=len(edits),record=str(out),sha256=sha(out.read_bytes()))))
if __name__=="__main__":main()
