#!/usr/bin/env python3
"""Original editable SVG + searchable LaTeX picture for the ramified/full-AU construction."""
from pathlib import Path
import html,json,hashlib,datetime,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'outputs/checks/2026-11-06-ramified-book/lane-a/figure-v6'
OUT.mkdir(parents=True,exist_ok=True)
W,H=350,503
C={'ink':'173C39','teal':'0C6E73','blue':'314D72','amber':'A25018',
   'muted':'53676D','pale':'E6F2F2','soft':'EDF1F7','warm':'F5E5D1','line':'A8BCBF'}
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="700" height="1006" viewBox="0 0 700 1006" role="img" tabindex="0" focusable="true" aria-labelledby="ramified-title ramified-desc">',
'<title id="ramified-title">Rational cusps and the original full-coefficient pure finite prefix</title>',
'<desc id="ramified-desc">Two linked construction lanes. The actual primary index x equals lambda cubed mu congruent to one modulo three, with all raw fixed prime exclusions retained after conductor drop. Fixed finite residue data become rational theta translates and known integral cusp states: nine have a nonzero constant term and eighteen have zero constant term; all twenty-seven have nonconstant coefficients. Pure angular derivatives of order plus or minus one remove radial constants, retaining the literal Kubota multiplier and angular unit, giving an exact Mellin factor NC to the power one minus two s and coarse moving dual cost R to the power three halves. Ell zero residues remain. The lower lane opens B_U equals mu A_U on Nm greater than U, groups the two original short factors, five truncated mu factors and four free Heath Brown factors, and classifies fixed scales before any a,b triangle. Balanced boxes, large complete prefixes and small complete prefixes meet at Z equals D to the power two ninths. Original prefix zeros stay outside the long-variable Q mask; the original finite k and actual phases remain. The small branch retains Nk to the three eighths; only its positive Nk to the minus thirteen eighths plus epsilon majorant is summed to infinity. At critical A1 comparable to H equals D to the power three quarters and X equals D to the power three eighths, the normalized pure finite prefix has leading power 101 over 144. Jacobi rho is not finite order. The remaining frequency complement, other sectors and GRH are open. This is a schematic proof construction, not counts of ideals or measured energies.</desc>',
'<style>text{font-family:"DejaVu Sans",Arial,sans-serif} .math{font-family:"DejaVu Sans",Arial,sans-serif} svg:focus{outline:3px solid #0C6E73;outline-offset:2px}</style>',
'<rect width="700" height="1006" fill="white"/>']
tex=[r'\documentclass{article}',r'\usepackage[paperwidth=350pt,paperheight=503pt,margin=0pt]{geometry}',r'\usepackage{xcolor,amsmath,amssymb,lmodern}',r'\pagestyle{empty}\pagecolor{white}',r'\setlength{\parindent}{0pt}\setlength{\topskip}{0pt}\setlength{\unitlength}{1pt}']
for k,v in C.items():tex.append(r'\definecolor{'+k+r'}{HTML}{'+v+'}')
tex += [r'\begin{document}\noindent\begin{picture}(350,503)']
def text(x,y,sv,tx=None,size=9,color='ink',bold=False,anchor='start',math=False):
 if tx is None:tx=sv
 attrs=f'x="{2*x}" y="{2*y}" font-size="{2*size}" fill="#{C[color]}" text-anchor="{anchor}"'
 if bold:attrs+=' font-weight="700"'
 if math:attrs+=' class="math"'
 svg.append('<text '+attrs+'>'+sv+'</text>')
 pos={'start':'l','middle':'c','end':'r'}[anchor]
 weight=r'\bfseries ' if bold else ''
 tex.append(r'\put('+str(x)+','+str(H-y)+r'){\makebox(0,0)['+pos+r']{\color{'+color+r'}\sffamily\fontsize{'+str(size)+'}{'+str(size*1.15)+r'}\selectfont '+weight+tx+r'}}')
def line(x1,y1,x2,y2,color='ink',width=.7,dash=False):
 attrs=f'x1="{2*x1}" y1="{2*y1}" x2="{2*x2}" y2="{2*y2}" stroke="#{C[color]}" stroke-width="{2*width}"'
 if dash:attrs+=' stroke-dasharray="5 4"'
 svg.append('<line '+attrs+'/>')
 # Generic straight segment via picture qbezier, avoiding limited slope vocabulary.
 tex.append(r'{\color{'+color+r'}\linethickness{'+str(width)+r'pt}\qbezier('+str(x1)+','+str(H-y1)+')('+str((x1+x2)/2)+','+str(H-(y1+y2)/2)+')('+str(x2)+','+str(H-y2)+')}')
def arrow(x1,y1,x2,y2,color='teal',width=.8):
 line(x1,y1,x2,y2,color,width)
 import math
 dx,dy=x2-x1,y2-y1;n=math.hypot(dx,dy);ux,uy=dx/n,dy/n
 for sg in [-1,1]:
  bx=x2-4*ux+sg*2*uy;by=y2-4*uy-sg*2*ux
  line(x2,y2,bx,by,color,width)
def circle(x,y,r,color='teal',fill=False,ident=None):
 svg.append(f'<circle id="{ident}" cx="{2*x}" cy="{2*y}" r="{2*r}" fill="#{C[color]}" fill-opacity="{1 if fill else 0}" stroke="#{C[color]}" stroke-width="1.4"/>')
 tex.append(r'\put('+str(x)+','+str(H-y)+r'){\color{'+color+r'}\circle'+('*' if fill else '')+'{'+str(2*r)+'}}')
def rect(x,y,w,h,fill,stroke='line',ident=None):
 svg.append(f'<rect id="{ident}" x="{2*x}" y="{2*y}" width="{2*w}" height="{2*h}" rx="3" fill="#{C[fill]}" stroke="#{C[stroke]}" stroke-width="1.1"/>')
 tex.append(r'\put('+str(x)+','+str(H-y-h)+r'){\color{'+fill+r'}\rule{'+str(w)+r'pt}{'+str(h)+r'pt}}')
 tex.append(r'\put('+str(x)+','+str(H-y-h)+r'){\color{'+stroke+r'}\linethickness{.55pt}\framebox('+str(w)+','+str(h)+'){}}')
# Header.
text(14,21,'RATIONAL CUSPS → AN ACTUAL FINITE PREFIX',r'RATIONAL CUSPS $\to$ AN ACTUAL FINITE PREFIX',11.1,bold=True)
text(14,36,'Primary index x = λ³μ ≡ 1 (mod 3) → rational translates',r'Primary index $x=\lambda^3\mu\equiv1\pmod3$ $\to$ rational translates',8.7,color='muted')
line(14,44,336,44,'line',.6)
# Geometry lane.
text(14,58,'I  EXACT SOURCE GEOMETRY',size=9.6,color='teal',bold=True)
text(14,79,'raw finite κ',r'raw finite $\kappa$',8.8,bold=True)
text(14,92,'ν fixed, finite order',r'$\nu$ fixed, finite order',8,color='muted')
text(14,105,'Jacobi ρ is not finite',r'Jacobi $\rho$ is not finite',8,color='muted')
text(14,125,'a = A/C',r'$a=A/C$',11.3,math=True)
text(14,139,'NC ≤ fixed · R',r'$NC\ll_{\rm fixed}R$',8.3,color='muted',math=True)
arrow(94,114,115,114)
text(127,78,'27 integral cusp states',size=8.8,bold=True)
for group,base_x in enumerate([132,174,216]):
 for j in range(9):
  circle(base_x+11*(j%3),91+11*(j//3),2.6,'teal',group==0,f'cusp-{group*9+j+1:02d}')
text(127,130,'9 with a constant term',size=7.9,color='muted')
text(127,142,'18 with zero constant term',size=7.9,color='muted')
arrow(247,113,268,113)
text(276,91,'angular',size=8.5,bold=True)
text(276,104,'Mellin',size=8.5,bold=True)
text(276,125,'ℓ = ±1',r'$\ell=\pm1$',10,math=True)
text(14,159,'Λ<tspan baseline-shift="sub" font-size="12">a</tspan>(s,ℓ) = u<tspan baseline-shift="sub" font-size="12">a,ℓ</tspan> · (NC)<tspan baseline-shift="super" font-size="12">1−2s</tspan> Λ<tspan baseline-shift="sub" font-size="12">j,−D/C</tspan>(1−s,−ℓ)',
 r'$\Lambda_a(s,\ell)=u_{a,\ell}(NC)^{1-2s}\Lambda_{j,-D/C}(1-s,-\ell)$',9.1,math=True)
text(14,172,'u<tspan baseline-shift="sub" font-size="10">a,ℓ</tspan> = χ(δ<tspan baseline-shift="sub" font-size="10">a</tspan>)(−1)<tspan baseline-shift="super" font-size="10">|ℓ|</tspan>(C/C̄)<tspan baseline-shift="super" font-size="10">ℓ</tspan>',
 r'$u_{a,\ell}=\chi(\delta_a)(-1)^{|\ell|}(C/\bar C)^\ell$',7.8,math=True)
text(14,185,'coarse R<tspan baseline-shift="super" font-size="12">3/2</tspan> → sharp H(3/4, 3/8)',
 r'coarse $R^{3/2}\ \longrightarrow\ $ sharp $H(3/4,3/8)$',9.1,color='teal',bold=True)
text(14,198,'ℓ = 0: retain residues at 1/6 and 5/6.',
 r'$\ell=0$: retain residues at $1/6$ and $5/6$.',8.0,color='amber')
line(14,204,336,204,'line',.6)
# Source input visibly enters the small-prefix branch.
line(334,175,341,175,'teal',.8)
line(341,175,341,344,'teal',.8)
arrow(341,344,323,344,'teal',.8)
# Coefficient lane.
text(14,220,'II  WHOLE ELEVEN-FACTOR PARTITION',size=9.6,color='blue',bold=True)
text(14,241,'B<tspan baseline-shift="sub" font-size="12">U</tspan> = μ A<tspan baseline-shift="sub" font-size="12">U</tspan> = ∑<tspan baseline-shift="sub" font-size="11">abc=m; Na,Nb≤U</tspan> μ(c)',
 r'$B_U=\mu A_U=\sum_{\substack{abc=m\\Na,Nb\le U}}\mu(c)$',9.5,math=True)
text(262,233,'Nm &gt; U',r'$Nm>U$',8.2,color='muted',math=True)
text(262,246,'B<tspan baseline-shift="sub" font-size="11">U</tspan> ≠ C<tspan baseline-shift="sub" font-size="11">U</tspan>',r'$B_U\ne C_U$',8.2,color='amber',math=True)
factors=[('a','a','warm'),('b','b','warm')]+[(f'm{i}',rf'$m_{i}$','soft') for i in range(1,6)]+[(f'v{i}',rf'$v_{i}$','pale') for i in range(1,5)]
for i,(nm,tx,col) in enumerate(factors):
 x=14+29*i
 rect(x,258,22,14,col,'line','factor-'+nm)
 sv=nm[0]+('<tspan baseline-shift="sub" font-size="11">'+nm[1:]+'</tspan>' if len(nm)>1 else '')
 text(x+11,268,sv,tx,8.3,anchor='middle')
text(39.5,285,'Na,Nb ≤ U',r'$Na,Nb\le U$',7.9,color='muted',anchor='middle')
text(141,285,'5 truncated μ factors',r'5 truncated $\mu$ factors',7.9,color='muted',anchor='middle')
text(271,285,'4 free factors',size=7.9,color='muted',anchor='middle')
text(14,300,'classify fixed scales (schematic J = 5 slots)',r'classify fixed scales (schematic $J=5$ slots)',7.9,color='muted')
# Exact classification forks, with the mean as an input only for small TypeI.
line(176,290,176,307,'blue',.8)
arrow(176,307,62,321,'blue',.8)
arrow(176,307,248,321,'blue',.8)
text(17,331,'balanced subset',size=8.5,color='blue',bold=True)
text(54,350,'D<tspan baseline-shift="super" font-size="13">1/3</tspan>',r'$D^{1/3}$',11.5,color='blue',anchor='middle',math=True)
text(177,331,'one free long v; m = pv',r'one free long $v$; $m=pv$',8.5,color='blue',bold=True)
arrow(248,336,201,345,'blue',.8)
arrow(248,336,299,345,'blue',.8)
text(181,358,'Np &gt; Z',r'$Np>Z$',8.3,color='blue')
text(280,358,'Np ≤ Z',r'$Np\le Z$',8.3,color='blue')
text(201,376,'D<tspan baseline-shift="super" font-size="11">1/3</tspan> + √(D/Z)',r'$D^{1/3}+\sqrt{D/Z}$',9.3,color='blue',anchor='middle',math=True)
text(287,376,'D<tspan baseline-shift="super" font-size="10">1/4</tspan>(Nk)<tspan baseline-shift="super" font-size="10">3/8</tspan>Z<tspan baseline-shift="super" font-size="10">5/8</tspan>',r'$D^{1/4}(Nk)^{3/8}Z^{5/8}$',8.1,color='blue',anchor='middle',math=True)
text(14,389,'freeze n first; prefix zeros stay outside Q',r'freeze $n$ first; prefix zeros stay outside $Q$',8.4,color='muted')
text(14,401,'Q = rad<tspan baseline-shift="sub" font-size="11">good</tspan>(p n k s w); all original finite k retained',
 r'$Q=\operatorname{rad}_{\rm good}(pnksw)$; all original finite $k$ retained',8.4,color='muted',math=True)
text(14,413,'positive bound only: ∑<tspan baseline-shift="sub" font-size="10">k</tspan>(Nk)<tspan baseline-shift="super" font-size="10">−13/8+ε</tspan> &lt; ∞',
 r'positive bound only: $\sum_k(Nk)^{-13/8+\epsilon}<\infty$',7.8,color='muted',math=True)
line(14,420,336,420,'line',.6)
text(175,435,'Z = D<tspan baseline-shift="super" font-size="12">2/9</tspan>:  √(D/Z) = D<tspan baseline-shift="super" font-size="12">1/4</tspan>Z<tspan baseline-shift="super" font-size="12">5/8</tspan> = D<tspan baseline-shift="super" font-size="12">7/18</tspan>',
 r'$Z=D^{2/9}:\quad \sqrt{D/Z}=D^{1/4}Z^{5/8}=D^{7/18}$',9.1,anchor='middle',math=True)
# Outcome and explicit open boundary.
text(14,450,'PURE FINITE TOP PREFIX',size=8.2,color='teal',bold=True)
text(14,469,'D<tspan baseline-shift="super" font-size="18">101/144+ε</tspan>',r'$D^{101/144+\epsilon}$',16.5,color='teal',bold=True,math=True)
text(165,447,'normalized P<tspan baseline-shift="sub" font-size="12">X</tspan>[A<tspan baseline-shift="sub" font-size="12">U</tspan>, A<tspan baseline-shift="sub" font-size="12">U</tspan>]',
 r'normalized $P_X[A_U,A_U]$',9.3,color='teal',math=True)
text(165,459,'A₁ ≍ H = D<tspan baseline-shift="super" font-size="11">3/4</tspan>; X = D<tspan baseline-shift="super" font-size="11">3/8</tspan>',r'$A_1\asymp H=D^{3/4}$; $X=D^{3/8}$',8.1,color='muted',math=True)
text(165,471,'margin 7/144; fixed W seminorms',r'margin $7/144$; fixed $W$ seminorms',8.1,color='muted')
# Boundary is put in the accessible footer and PDF as a compact last line inside crop.
# Footer on extended artboard, using newH mapping for this final pair.
svg.append(f'<line x1="28" y1="955" x2="672" y2="955" stroke="#{C["amber"]}" stroke-width="1.2" stroke-dasharray="5 4"/>')
svg.append(f'<text x="28" y="982" font-size="16.6" fill="#{C["amber"]}">OPEN: frequency complement · other sectors · GRH</text>')
tex.append(r'{\color{amber}\linethickness{.6pt}\qbezier(14,25.5)(175,25.5)(336,25.5)}')
tex.append(r'\put(14,12){\makebox(0,0)[l]{\color{amber}\sffamily\fontsize{8.3}{9.6}\selectfont OPEN: frequency complement; other sectors; GRH}}')
tex.append(r'\end{picture}\end{document}')
svg.append('</svg>')
svgtext='\n'.join(svg)+'\n'
textext='\n'.join(l+'%' if l and not l.lstrip().startswith('%') else l for l in tex)+'\n'
for name,data in [('ramified-cusp-prefix.svg',svgtext),('ramified-cusp-prefix.tex',textext)]:
 f=OUT/name
 if f.exists():raise RuntimeError('Refuse overwrite '+str(f))
 f.write_text(data)
root=ET.fromstring(svgtext)
ns={'s':'http://www.w3.org/2000/svg'}
assert len(root.findall('.//s:circle',ns))==27
assert len([e for e in root.findall('.//s:rect',ns) if e.get('id','').startswith('factor-')])==11
assert root.get('tabindex')=='0' and root.get('role')=='img'
assert root.find('s:title',ns) is not None and root.find('s:desc',ns) is not None
for e in root.iter():
 for k,v in e.attrib.items():
  assert not(k.endswith('href') or k.lower().startswith('on')), (k,v)
assert '<script' not in svgtext and '<foreignObject' not in svgtext and 'url(' not in svgtext
print(json.dumps({'stage':str(OUT),'svg_bytes':len(svgtext.encode()),'tex_bytes':len(textext.encode()),'cusps':27,'factors':11,'native_pt':[350,503],'safe_svg':True}))
