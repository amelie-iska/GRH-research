#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
mkdir -p outputs/html-work web/book/figures
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
make4ht -f html5+mathml -d ../../web/book main.tex 'mathml,svg'
cd "$root"
for name in dessin-carriers training-curves photonic-angle; do
  pdftocairo -svg "book/figures/$name.pdf" "web/book/figures/$name-.svg"
done
python3 scripts/render_html_diagrams.py
python3 scripts/prepare_book_html.py
python3 scripts/build_verification_page.py
