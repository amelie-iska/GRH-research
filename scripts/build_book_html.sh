#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
mkdir -p outputs/html-work outputs/html-staging/figures
python3 - <<'PY'
from pathlib import Path
import shutil
root=Path('.').resolve();work=root/'outputs/html-work'
shutil.copyfile(root/'book/main.tex',work/'main.tex')
for name in ['chapters','figures']:
    if not (work/name).exists():(work/name).symlink_to(root/'book'/name,target_is_directory=True)
PY
mkdir -p outputs/html-work/bin
cat > outputs/html-work/bin/pdf2svg <<'WRAPPER'
#!/bin/sh
exec pdftocairo -svg "$1" "$2"
WRAPPER
chmod +x outputs/html-work/bin/pdf2svg
export PATH="$root/outputs/html-work/bin:$PATH"
cd outputs/html-work
make4ht -f html5+mathml -d ../html-staging main.tex 'mathml,svg'
cd "$root"
for name in dessin-carriers training-curves photonic-angle learned-generative learned-width-flow learned-covers; do
  pdftocairo -svg "book/figures/$name.pdf" "outputs/html-staging/figures/$name-.svg"
done
python3 scripts/render_html_diagrams.py outputs/html-staging
python3 scripts/prepare_book_html.py outputs/html-staging
python3 scripts/build_verification_page.py
python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET,shutil
src=Path('outputs/html-staging');live=Path('web/book');tree=ET.fromstring((src/'main.html').read_text())
frames=[x.attrib['src'] for x in tree.iter('iframe')]
assert len(frames)==len(set(frames)), 'Duplicate embedded tools'
for x in tree.iter('img'):
    assert (src/x.attrib['src']).is_file(), 'Missing image '+x.attrib['src']
for path in src.rglob('*'):
    if path.is_file() and path.name!='main.html':
        target=live/path.relative_to(src);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path,target)
pending=live/'main.html.pending';shutil.copyfile(src/'main.html',pending);pending.replace(live/'main.html')
print('Promoted validated HTML/assets; previous live book was preserved throughout compilation')
PY
