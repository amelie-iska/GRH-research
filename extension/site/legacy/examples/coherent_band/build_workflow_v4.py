#!/usr/bin/env python3
"""Readable 2+1 source-bound workflow. Fresh-output reproduction is the default."""
from pathlib import Path
import argparse,colorsys,hashlib,json,math,shutil,subprocess,html
ROOT=Path(__file__).resolve().parents[2];PAYLOAD=ROOT/'web/data/coherent-band-schur-v1.json'
EXPECTED='e540ac344bbf3d4d07d1ac9fcb8c5cd336a6195c7130a602567242c33bc73171'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def value(e,stage):
 if not e['support']:return 0j
 z=complex(*{0:(1,0),2:(-.5,math.sqrt(3)/2),4:(-.5,-math.sqrt(3)/2)}[e['phase6']])
 if stage==0:return z
 z*=e['A_U'];return z if stage==1 else z*complex(*map(float,e['W']))
def rgb(z):return ''.join(f'{round(x*255):02X}' for x in colorsys.hls_to_rgb(((190+math.degrees(math.atan2(z.imag,z.real)))%360)/360,.43,.53))
def escape(s):
 for a,b in [('&',r'\&'),('%',r'\%'),('#',r'\#'),('_',r'\_')]:s=s.replace(a,b)
 return s
def main():
 p=argparse.ArgumentParser();p.add_argument('--work',required=True);p.add_argument('--asset-dir');p.add_argument('--replace-manifest');a=p.parse_args();work=Path(a.work);work=work if work.is_absolute() else ROOT/work;work.mkdir(parents=True,exist_ok=False)
 assets=Path(a.asset_dir) if a.asset_dir else work/'assets';assets=assets if assets.is_absolute() else ROOT/assets;assets.mkdir(parents=True,exist_ok=True)
 targets={ext:assets/f'coherent-band-workflow.{ext}' for ext in ['svg','tex','pdf']}
 replaced={}
 if any(x.exists() for x in targets.values()):
  assert a.replace_manifest and assets==ROOT/'book/figures'
  old=json.loads((ROOT/a.replace_manifest).read_text());before=work/'before';before.mkdir()
  for x in targets.values():
   expected=old['outputs'][str(x.relative_to(ROOT))]['sha256'];assert sha(x)==expected;shutil.copyfile(x,before/x.name);replaced[str(x.relative_to(ROOT))]=expected
 assert sha(PAYLOAD)==EXPECTED;j=json.loads(PAYLOAD.read_text());c=j['cases'][0];assert c['D']==121
 H=186;svg=['<svg xmlns="http://www.w3.org/2000/svg" width="179mm" height="190mm" viewBox="-12 -12 1074 1140" role="img" aria-labelledby="title desc"><title id="title">Actual auxiliary coefficient workflow</title><desc id="desc">Readable two-plus-one arrangement of three exact saved fourteen by twenty-nine matrix patterns. Raw cubic K, integer AU times K, and common complex W times AU times K. Norm numbers are saved fifty-five-digit numerical SVD consistency values, not interval certificates or physical-row-family data.</desc><rect x="-12" y="-12" width="1074" height="1140" fill="white"/>']
 tex=[r'\documentclass{article}',r'\usepackage[paperwidth=179mm,paperheight=190mm,margin=2mm]{geometry}',r'\usepackage{xcolor,amsmath}',r'\pagestyle{empty}\setlength{\parindent}{0pt}\setlength{\topskip}{0pt}\setlength{\unitlength}{1mm}',r'\begin{document}\noindent',r'\begin{picture}(175,186)'];colors={}
 def color(h):
  if h not in colors:colors[h]=f'cb{len(colors)}';tex.append(f'\\definecolor{{{colors[h]}}}{{HTML}}{{{h}}}')
  return colors[h]
 def text(x,y,s,tx=None,pt=12,bold=False):
  svg.append(f'<text x="{x*6:.4f}" y="{y*6:.4f}" fill="#203A36" font-family="Arial,sans-serif" font-size="{pt*25.4/72.27*6:.5f}"'+(' font-weight="700"' if bold else '')+'>'+html.escape(s)+'</text>')
  tex.append(f'\\put({x:.4f},{H-y:.4f}){{\\makebox(0,0)[bl]{{\\color{{{color("203A36")}}}\\sffamily\\fontsize{{{pt}}}{{{pt*1.2:.2f}}}\\selectfont'+('\\bfseries ' if bold else ' ')+(tx if tx is not None else escape(s))+'}}')
 def rect(x,y,w,h,fill,alpha=1,stroke=None):
  svg.append(f'<rect x="{x*6:.4f}" y="{y*6:.4f}" width="{w*6:.4f}" height="{h*6:.4f}" fill="#{fill}" fill-opacity="{alpha:.6f}"'+(f' stroke="#{stroke}" stroke-width="1.8"' if stroke else '')+'/>')
  tex.append(f'\\put({x:.4f},{H-y-h:.4f}){{\\color{{{color(fill)}!{alpha*100:.4f}!white}}\\rule{{{w:.4f}mm}}{{{h:.4f}mm}}}}')
  if stroke:tex.append(f'\\put({x:.4f},{H-y-h:.4f}){{\\color{{{color(stroke)}}}\\linethickness{{.3mm}}\\framebox({w:.4f},{h:.4f}){{}}}}')
 def line(x1,y1,x2,y2,fill='315C51',width=.3):
  svg.append(f'<path d="M{x1*6} {y1*6}L{x2*6} {y2*6}" stroke="#{fill}" stroke-width="{width*6}" fill="none"/>')
  tex.append(f'{{\\color{{{color(fill)}}}\\linethickness{{{width}mm}}\\qbezier({x1:.4f},{H-y1:.4f})({(x1+x2)/2:.4f},{H-(y1+y2)/2:.4f})({x2:.4f},{H-y2:.4f})}}')
 text(3,5,'ONE COUPLED COEFFICIENT',pt=14.4,bold=True)
 text(3,12,'D=121 / U=11 / X=242 / T=1936',r'$D=121$, $U=11$, $X=242$, $T=1936$.',pt=12)
 selected=next(e for e in c['entries'] if e['support'] and e['A_U'] and float(e['W'][0])!=0)
 specs=[(3,28,23,68,75,'01 / RAW CUBIC','K',r'$K$','K_norm'),(94,28,23,68,75,'02 / ACTUAL CUTOFF','A_U ◦ K',r'$A_U\circ K$','AU_K_norm'),(48.5,96,91,136,143,'03 / COMMON PROFILE','W ◦ A_U ◦ K',r'$W\circ A_U\circ K$','W_AU_K_norm')]
 for stage,(x0,y0,hy,fy,ny,label,formula,tx,nkey) in enumerate(specs):
  text(x0,hy,label,pt=12,bold=True);maximum=max(abs(value(e,stage)) for e in c['entries']);cw=2.4
  for e in c['entries']:
   x=x0+e['j']*cw;y=y0+e['i']*cw;z=value(e,stage);m=abs(z);rect(x,y,2.18,2.18,rgb(z) if m else 'DCE3DA',.25+.75*math.sqrt(m/maximum) if m else .65,'1A332D' if(e['i'],e['j'])==(selected['i'],selected['j']) else None)
   if not e['support']:
    if'product_cutoff'in e['mask_causes']:line(x+.5,y+1.7,x+1.7,y+.5,'A3AFA4',.12)
    if'shared_ideal_prime'in e['mask_causes']:rect(x+.85,y+.85,.5,.5,'8C9B90')
  text(x0,fy,formula,tx,pt=12);text(x0,ny,f'‖·‖₂ ≈ {float(c["norms"][nkey]):.10g}',r'$\|\cdot\|_2\approx '+f'{float(c["norms"][nkey]):.10g}'+r'$',pt=14.4)
 line(77,44,89,44);line(86,41,89,44);line(86,47,89,44)
 line(128,78,128,84);line(128,84,119,90);line(120,86,119,90);line(123,90,119,90)
 text(3,155,f'Finite Perron: ‖A_T◦K‖₂ ≈ {float(c["norms"]["AU_T_K_norm"]):.10g}',r'Finite Perron: $\|A_T\circ K\|_2\approx '+f'{float(c["norms"]["AU_T_K_norm"]):.10g}'+r'$.',pt=12)
 text(3,163,f'Residual: ‖(A_U−A_T)◦K‖₂ ≈ {float(c["norms"]["residual_norm"]):.10g}',r'Residual: $\|(A_U-A_T)\circ K\|_2\approx '+f'{float(c["norms"]["residual_norm"]):.10g}'+r'$.',pt=12)
 text(3,172,'14×29 entries: 74 supported; 332 source-masked.',r'$14\times29$ entries: $74$ supported; $332$ source-masked.',pt=12)
 text(3,179,'Saved 55-digit numerical consistency; selected entry outlined.',pt=12)
 text(3,186,'Auxiliary ideals; not physical rows or interval certificates.',pt=12)
 svg.append('</svg>');tex.extend([r'\end{picture}',r'\end{document}']);targets['svg'].write_text('\n'.join(svg)+'\n');targets['tex'].write_text('\n'.join(tex)+'\n')
 run=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory',str(work),str(targets['tex'])],cwd=work,capture_output=True,text=True,timeout=60);(work/'pdflatex.stdout.txt').open('x').write(run.stdout+run.stderr)
 if run.returncode:raise RuntimeError(f'pdflatex failed; preserved {work}')
 log=(work/'coherent-band-workflow.log').read_text();assert not any(x in log for x in ['Overfull','Missing character','LaTeX Warning','LaTeX Font Warning'])
 shutil.copyfile(work/'coherent-band-workflow.pdf',targets['pdf']);info=subprocess.check_output(['pdfinfo',str(targets['pdf'])],text=True);(work/'pdfinfo.txt').open('x').write(info);assert'Pages:           1'in info
 subprocess.run(['pdftoppm','-scale-to','1600','-png','-singlefile',str(targets['pdf']),str(work/'workflow')],check=True,capture_output=True,timeout=30)
 rec=dict(passed=True,scope='Readable2+1 source-bound auxiliary matrix workflow; no numerical norm/control rerun',payload_sha256=sha(PAYLOAD),producer_sha256=sha(Path(__file__)),case_D=121,shape=[14,29],selected_entry=[selected['i'],selected['j']],outputs={str(p.relative_to(ROOT)):dict(sha256=sha(p),bytes=p.stat().st_size) for p in targets.values()},replaced_source_hashes_preserved=replaced,pdf_pages=1,minimum_source_label_pt=12,minimum_label_pt_at_6inch_width=12*152.4/179,overfull_missing_glyph_or_font_warning=False,render=str((work/'workflow.png').relative_to(ROOT)),root_PDF_marker_already_executed=True)
 (work/'figure-receipt-v1.json').open('x').write(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(json.dumps(rec))
if __name__=='__main__':main()
