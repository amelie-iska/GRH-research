#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root/papers"
for edition in concise extended resolutions-concise resolutions-extended; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../outputs/paper-build-staging "$edition.tex"
done
cd "$root"
python3 - <<'PY'
from pathlib import Path
import re,shutil
stage=Path('outputs/paper-build-staging');live=Path('outputs/papers')
for edition in ['concise','extended','resolutions-concise','resolutions-extended']:
    log=(stage/(edition+'.log')).read_text()
    assert not re.search(r'undefined references|Citation .* undefined|Reference .* undefined|Overfull|^!',log,re.M),edition
    assert (stage/(edition+'.pdf')).read_bytes().startswith(b'%PDF')
# Validate all editions before promoting; old live outputs survive failures.
for edition in ['concise','extended','resolutions-concise','resolutions-extended']:
    for ext in ['pdf','log']:
        source=stage/(edition+'.'+ext);target=live/source.name;pending=target.with_suffix(target.suffix+'.pending')
        shutil.copyfile(source,pending);pending.replace(target)
print('Promoted four verified article editions from staging')
PY
