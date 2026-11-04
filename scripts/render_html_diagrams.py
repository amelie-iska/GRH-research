#!/usr/bin/env python3
"""Export each actual book TikZ diagram through PDF to preserve its geometry.

The system DVI SVG exporter lacks a PostScript interpreter, which can flatten
TikZ node positions. Standalone PDF compilation plus Poppler preserves them.
"""
from pathlib import Path
import re,subprocess,json,hashlib,sys
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'web/book'
def expand_book(text, stack=()):
 def include(match):
  path=(ROOT/'book'/(match[1]+'.tex')).resolve()
  if path in stack:raise ValueError('Recursive book input: '+str(path))
  return expand_book(path.read_text(),stack+(path,))
 return re.sub(r'\\input\{([^}]+)\}',include,text)
# Follow the actual TeX input order, including newly added chapters. A fixed
# chapter list shifts SVG indices when a new diagram is inserted.
text=expand_book((ROOT/'book/main.tex').read_text())
expressions=[m[0] for m in re.finditer(r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}',text,re.S)]
assert len(expressions)>=1
preamble=r'''\documentclass[border=5pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,mathtools,tikz,tikz-cd}
\usetikzlibrary{arrows.meta,positioning,calc,decorations.markings}
\newcommand{\C}{\mathbb C}\newcommand{\R}{\mathbb R}\newcommand{\Z}{\mathbb Z}
\newcommand{\gshift}[2]{#1\langle #2\rangle}
\begin{document}
'''
def render(pair):
 i,expression=pair
 source_hash=hashlib.sha256(expression.encode()).hexdigest()
 # Retain all historical numeric work directories and compile each new source
 # in its own content-addressed directory. Live SVG names follow TeX4ht order.
 work=ROOT/'outputs/html-diagrams'/source_hash[:16];work.mkdir(parents=True,exist_ok=True)
 source=work/'diagram.tex';source.write_text(preamble+expression+'\n\\end{document}\n')
 with (work/'compile.log').open('wb') as log:
  subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','diagram.tex'],cwd=work,stdout=log,stderr=subprocess.STDOUT,check=True)
 output=OUT/f'main{i}x.svg'
 subprocess.run(['pdftocairo','-svg',str(work/'diagram.pdf'),str(output)],check=True)
 return dict(index=i,source_sha256=source_hash,sha256=hashlib.sha256(output.read_bytes()).hexdigest(),bytes=output.stat().st_size)
with ThreadPoolExecutor(max_workers=2) as executor:rows=list(executor.map(render,enumerate(expressions)))
(ROOT/'outputs/book/diagram-exports.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Exported',len(rows),'actual compiled book diagrams with preserved geometry')
