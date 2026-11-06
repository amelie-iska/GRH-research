from pathlib import Path
import json,subprocess,hashlib,runpy,xml.etree.ElementTree as ET
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
OUT=ROOT/'outputs/checks/2026-11-06-ramified-book/lane-a/figure-v6'
runs=[]
def run(args):
 r=subprocess.run(args,cwd=OUT,capture_output=True,text=True);runs.append({'command':args,'returncode':r.returncode,'stdout':r.stdout[-2000:],'stderr':r.stderr[-1000:]});assert r.returncode==0,(args,r.stderr);return r.stdout
run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','ramified-cusp-prefix.tex'])
info=run(['pdfinfo','ramified-cusp-prefix.pdf'])
run(['pdftotext','ramified-cusp-prefix.pdf','ramified-cusp-prefix.txt'])
run(['pdftoppm','-png','-singlefile','-scale-to','1400','ramified-cusp-prefix.pdf','ramified-cusp-prefix-pdf-preview'])
renderer=ROOT/'scripts/build_remote_articles.py'
runpy.run_path(str(renderer),run_name='not_main')['svg_pdf']((OUT/'ramified-cusp-prefix.svg').read_bytes(),OUT/'ramified-cusp-prefix-svg-preview.pdf')
run(['pdftoppm','-png','-singlefile','-scale-to','1400','ramified-cusp-prefix-svg-preview.pdf','ramified-cusp-prefix-svg-preview'])
log=(OUT/'ramified-cusp-prefix.log').read_text()
assert not any(x in log for x in ['Warning','Overfull','Underfull'])
pdftext=(OUT/'ramified-cusp-prefix.txt').read_text()
assert all(x in pdftext for x in ['RATIONAL CUSPS','27 integral cusp states','WHOLE ELEVEN','prefix zeros','PURE FINITE TOP PREFIX','101/144','OPEN'])
s=(OUT/'ramified-cusp-prefix.svg').read_text();node=ET.fromstring(s);ns={'s':'http://www.w3.org/2000/svg'}
assert node.attrib['tabindex']=='0' and node.attrib['focusable']=='true'
assert node.find('s:title',ns) is not None and node.find('s:desc',ns) is not None
circles=node.findall('.//s:circle',ns);assert len(circles)==27
slots=[x for x in node.findall('.//s:rect',ns) if 'factor' in x.attrib.get('id','')];assert len(slots)==11
for x in node.iter():
 assert x.tag.rsplit('}',1)[-1] not in ['script','foreignObject']
 assert not any(k.rsplit('}',1)[-1].lower()=='href' or k.lower().startswith('on') for k in x.attrib)
assert 'url(' not in s
assert '3/8' in s and '−13/8+ε' in s and 'u_{a,\\ell}' in (OUT/'ramified-cusp-prefix.tex').read_text()
assert 'Pages:           1' in info
files=[]
for name in ['ramified-cusp-prefix.svg','ramified-cusp-prefix.tex','ramified-cusp-prefix.pdf','ramified-cusp-prefix-pdf-preview.png','ramified-cusp-prefix-svg-preview.png']:
 p=OUT/name;files.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
receipt={'passed':True,'runs':runs,'warnings':[],'safe_svg':True,'accessible_svg':True,'cusps':27,'factor_slots':11,'searchable_pdf_markers':True,'source_pdf_method':'existing pdflatex/lmodern standard picture; searchable text','svg_preview_method':'existing librsvg/cairo ctypes svg_pdf only; no builder main','renderer_sha256':hashlib.sha256(renderer.read_bytes()).hexdigest(),'files':files}
p=OUT/'checks-v6.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'passed':True,'receipt':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'files':files}))
