#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
python3 scripts/assemble_book.py
python3 - <<'PY'
from pathlib import Path
p=Path('papers/dessin-references.tex').read_text()
add='\n'.join(Path(f'book/chapters/{n}-references.tex').read_text() for n in ['ar','physics','toricgt','persistence'])
p=p.replace('\\end{thebibliography}',add+'\n\\end{thebibliography}')
Path('book/chapters/references.tex').write_text('% Generated from pinned shared and book references.\n'+p)
PY
cd book
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=surface-orders-book -outdir=../outputs/book-build-staging main.tex
cd "$root"
python3 - <<'PY'
from pathlib import Path
import re,shutil
staging=Path('outputs/book-build-staging');live=Path('outputs/book');live.mkdir(exist_ok=True)
log=(staging/'surface-orders-book.log').read_text()
assert not re.search(r'undefined references|Citation .* undefined|Reference .* undefined|Overfull|^!',log,re.M)
assert (staging/'surface-orders-book.pdf').read_bytes().startswith(b'%PDF')
for ext in ['pdf','log','toc']:
    source=staging/('surface-orders-book.'+ext)
    if source.exists():
        target=live/source.name;pending=live/(source.name+'.pending')
        shutil.copyfile(source,pending);pending.replace(target)
print('Promoted verified book build; previous live PDF was preserved throughout compilation')
PY
