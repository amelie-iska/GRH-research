"""Serve only the named reviewed paper fragments, never arbitrary research files."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
names=['holomorphic-learning-core','holomorphic-learning-details','quantum-games-core','quantum-games-details','hubs-spokes-core','hubs-spokes-boundaries','electron-clouds']
out=ROOT/'web/data/synthetic-training/methods';out.mkdir(exist_ok=True)
manifest={}
for name in names:
    source=ROOT/'papers'/f'{name}.tex';target=out/source.name
    shutil.copyfile(source,target)
    manifest[source.name]={'source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Prepared',len(manifest),'explicit source fragments')
