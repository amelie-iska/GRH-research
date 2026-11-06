"""Original exact short-divisor partition figure; fresh staged outputs only."""
from pathlib import Path
import json,hashlib,subprocess,os,re
R=Path(__file__).resolve().parents[3]
O=R/"outputs/checks/2026-11-06-gauss-book/figure/run-v4"
assert not O.exists();O.mkdir(parents=True)
assert (R/"outputs/checks/2026-11-06-gauss-book/build-admin/marker-receipt-v1.json").is_file()
tex=[r"\documentclass{article}",r"\usepackage[paperwidth=180mm,paperheight=149mm,margin=3mm]{geometry}",
r"\usepackage{xcolor,amsmath,amssymb}",r"\pagestyle{empty}\pagecolor{white}",
r"\setlength{\parindent}{0pt}\setlength{\topskip}{0pt}\setlength{\unitlength}{1mm}",
r"\definecolor{ink}{HTML}{173C39}\definecolor{small}{HTML}{E4F1F4}",
r"\definecolor{one}{HTML}{F2D4B3}\definecolor{two}{HTML}{D3E7CF}\definecolor{open}{HTML}{8F3535}",
r"\begin{document}\noindent\begin{picture}(174,141)"]
def text(x,y,s,size=10,bold=False,anchor="bl",color="ink"):
 tex.append(r"\put("+str(x)+","+str(y)+r"){\makebox(0,0)["+anchor+r"]{\color{"+color+r"}\sffamily\fontsize{"+str(size)+"}{"+str(size*1.18)+r"}\selectfont"+(r"\bfseries "if bold else" ")+s+"}}")
def line(x,y,dx,dy,length):tex.append(r"\put("+str(x)+","+str(y)+r"){\color{ink}\line("+str(dx)+","+str(dy)+"){"+str(length)+"}}")
def fill(x,y,w,h,color):tex.append(r"\put("+str(x)+","+str(y)+r"){\color{"+color+r"}\rule{"+str(w)+"mm}{"+str(h)+"mm}}")
text(1,136,"TWO REGIONS, ONE CUBIC INTERACTION",13,True)
text(1,129,"Good squarefree assignment factors; schematic norms, not ideal counts.",9)
fill(14,52,26,26,"small")
fill(40,52,42,68,"one")
fill(14,78,26,42,"two")
tex.append(r"\put(14,52){\color{ink}\framebox(68,68){}}")
line(40,52,0,1,68);line(14,78,1,0,68)
tex.append(r"\put(12,50){\color{ink}\vector(1,0){73}}")
tex.append(r"\put(12,50){\color{ink}\vector(0,1){73}}")
for x,s in [(14,"$1$"),(40,"$Y$"),(82,"$U$")]:text(x,46,s,9,anchor="c")
for y,s in [(52,"$1$"),(78,"$Y$"),(120,"$U$")]:text(8,y,s,9,anchor="r")
text(86,49,r"$Na$",10)
text(11,124,r"$Nb$",10,anchor="c")
text(27,66,r"\shortstack{small\\$Na,Nb\leq Y$}",9,anchor="c")
text(61,89,r"\shortstack{\textbf{I}\\$Y<Na\leq U$\\$Nb\leq U$}",10,anchor="c")
text(27,99,r"\shortstack{\textbf{II}\\$Na\leq Y$\\$Y<Nb\leq U$}",9,anchor="c")
text(92,117,"Fold II by swapping a and b",10,True)
text(92,109,r"$z=bc,\qquad Y<Na\leq U$",11)
text(92,90,r"$T_L(z)=\displaystyle\sum_{\substack{b\mid z\\Nb\leq L}}\mu(z/b)$",11)
text(92,82,r"Both disjoint regions give $T_U(z)+T_Y(z)$.",9)
tex.append(r"\put(94,59){\color{ink}\framebox(76,19){\shortstack{\sffamily Actual physical cubic matrix\\[2pt]$\chi_{3,a}(\alpha_z),\quad Na\asymp A,\quad Nz\asymp D/A$}}}")
text(94,54,r"Shared prime: the matrix entry is exactly zero.",8.7)
text(1,36,r"$\overline{G_{az}}=\overline{G_a}\,\overline{G_z}\,\chi_{3,a}(\alpha_z),\quad(a,z)=1$",12)
text(92,36,r"$\|K\|_{\rm op}^2\ll D^\epsilon(A+D/A+D^{2/3})$",10)
line(1,31,1,0,172)
text(1,24,r"Gauss-moment tail $\ll B\,\mathcal{M}(W)D^\epsilon\!\left(Y^{-1/2}+D^{-1/6}\right)$",12,True)
text(1,15,r"$Y=D^{1/8},\quad X=D^{3/8},\quad A_1\asymp H=D^{3/4}$",11)
text(1,5,r"With $A_1X^{1/6}$: this part fits the target budget.",9.5)
text(102,15,r"$\mathcal{L}_0[A_Y,A_Y]$ remains open.",10,True,color="open")
text(102,5,"No whole signed or GRH conclusion.",9.5,color="open")
tex.extend([r"\end{picture}\end{document}"])
p=O/"gauss-tail-partition.tex";p.open("x").write("\n".join(tex)+"\n")
env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1","OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1"}
with (O/"build.stdout.log").open("x")as log:
 subprocess.run(["nice","-n","15","pdflatex","-interaction=nonstopmode","-halt-on-error",p.name],cwd=O,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
log=(O/"gauss-tail-partition.log").read_text()
bad=[l for l in log.splitlines()if re.search(r"Overfull|undefined|Missing character:|^!",l)]
assert not bad,bad
pdf=O/"gauss-tail-partition.pdf";info=subprocess.check_output(["pdfinfo",str(pdf)],text=True)
assert int(re.search(r"Pages:\s+(\d+)",info)[1])==1
svg=O/"gauss-tail-partition.svg"
subprocess.run(["pdftocairo","-svg",str(pdf),str(svg)],check=True,capture_output=True)
subprocess.run(["pdftoppm","-r","120","-png","-singlefile",str(pdf),str(O/"preview")],check=True,capture_output=True)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec={"passed":True,"author":"root","visual_acceptance_pending":True,
"semantics":"Exact disjoint norm-assignment regions and physical cubic cross; schematic axes, not counts or measured energies",
"geometry":{"box":[14,52,68,68],"Y_splits":[40,78],"regions":{"small":[14,52,26,26],"I":[40,52,42,68],"II":[14,78,26,42]}},
"proof_inputs":{"large_tail":"ed8b92c48812ada0dfe92c2bd7e314d8f4432b1952011da72236d4959f14aef7","finite_k":"816ff565c81e7ff486dc205ff92d3d4484e78226de87d3789fd4d564cc31e7eb"},
"outputs":{str(z.relative_to(R)):{"sha256":h(z),"bytes":z.stat().st_size}for z in [p,pdf,svg,O/"preview.png"]},"producer_sha256":h(Path(__file__)),
"old_assets_edited":False,"canonical_promoted":False,"new_Lean":False}
assert 26*26+42*68+26*42==68*68
rp=O/"author-receipt-v1.json";rp.open("x").write(json.dumps(rec,indent=2)+"\n")
print(json.dumps({"passed":True,"receipt_sha256":h(rp),"output":str(O),"preview_bytes":(O/"preview.png").stat().st_size}))
