#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
python3 scripts/assemble_book.py
python3 - <<'PY'
from pathlib import Path
p=Path('papers/dessin-references.tex').read_text()
add='\n'.join(Path(f'book/chapters/{n}-references.tex').read_text() for n in ['ar','physics','toricgt'])
p=p.replace('\\end{thebibliography}',add+'\n\\end{thebibliography}')
Path('book/chapters/references.tex').write_text('% Generated from pinned shared and book references.\n'+p)
PY
cd book
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=surface-orders-book -outdir=../outputs/book main.tex
