from pathlib import Path
import hashlib,json
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');p=R/'planning/book-integration-20261104/render_native.py';s=p.read_text()
needle="    fragment=(out/'fragment-unresolved.html').read_text()\n"
assert s.count(needle)==1
patch=r'''    # One explicitly source-bound reviewed workflow image; no generic PDF-image fallback.
    figure_assets=[]
    figure_pdf='figures/signed-divisor-workflow.pdf'
    if figure_pdf in raw_source:
        receipt_path=ROOT/'outputs/checks/2026-11-05-signed-divisor/ui/figure-receipt-v1.json'
        receipt=json.loads(read(receipt_path));assert receipt['passed'] is True
        expected={'book/figures/signed-divisor-workflow.pdf',
                  'book/figures/signed-divisor-workflow-.svg',
                  'book/figures/signed-divisor-workflow.tex'}
        assert set(receipt['files'])==expected
        for name,meta in receipt['files'].items():
            data=(ROOT/name).read_bytes();assert sha(data)==meta['sha256'] and len(data)==meta['bytes'],name
            sources[name]=sha(data)
            if name.endswith('.pdf'):assert data.startswith(b'%PDF')
            if name.endswith('.svg'):
                svg=ET.fromstring(data);assert svg.tag.rsplit('}',1)[-1]=='svg'
                for el in svg.iter():
                    assert el.tag.rsplit('}',1)[-1]!='script'
                    assert all(not k.lower().startswith('on') for k in el.attrib)
                    assert all(not (k.rsplit('}',1)[-1]=='href' and not v.startswith('#')) for k,v in el.attrib.items())
            figure_assets.append(dict(source=name,sha256=sha(data),bytes=len(data),native_target='figures/'+Path(name).name))
        figure_svg='figures/signed-divisor-workflow-.svg'
        pattern=r'<img\b[^>]*\bsrc="figures/signed-divisor-workflow\.pdf"[^>]*>'
        # Raw regex backslashes above are literal because this is generated Python source.
        pattern=pattern.replace('\\\\','\\')
        def reviewed_figure(m):
            img=m[0].replace('src="'+figure_pdf+'"','src="'+figure_svg+'"')
            return '<span class="reader-figure-scroll" tabindex="0" aria-label="Exact divisor workflow; horizontal scrolling on small screens">'+img+'</span><span class="source-links"><a href="figures/signed-divisor-workflow.tex">Original figure TeX</a> · <a href="'+figure_pdf+'">Source-matched figure PDF</a></span>'
        fragment,nfig=re.subn(pattern,reviewed_figure,fragment);assert nfig==1,('Expected one reviewed workflow image',nfig)
'''
s=s.replace(needle,needle+patch)
needle="    css='<style>";assert s.count(needle)==1;s=s.replace(needle,"    css='<style>.reader-figure-scroll{display:block;min-width:0;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}.reader-figure-scroll>img{display:block;min-width:720px;width:100%;max-width:none;height:auto}.reader-figure-scroll:focus-visible{outline:2px solid #078b96;outline-offset:3px}",1)
needle="    responsive=(Path(__file__).parent/'reviewed-math-scroll.js').read_bytes();(target/'reviewed-math-scroll.js').write_bytes(responsive)\n";assert s.count(needle)==1;s=s.replace(needle,needle+"    for item in figure_assets:\n        dest=target/item['native_target'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((ROOT/item['source']).read_bytes());assert sha(dest.read_bytes())==item['sha256']\n")
needle="        explicit_labels=len(source_labels),";assert s.count(needle)==1;s=s.replace(needle,"        accepted_figure_assets=figure_assets,\n"+needle)
p.write_text(s);compile(s,str(p),'exec')
O=R/'outputs/checks/2026-11-05-signed-divisor/root/integration-v1';(O/'native-figure-patch-v1.json').write_text(json.dumps({'scope':'Exact whitelist three-file source-bound workflow figure; strict PDF→SVG mapping/copy, responsive scroll and source links; no old subtree/preservation/numbering relaxations','renderer_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'figure_receipt_sha256':hashlib.sha256((R/'outputs/checks/2026-11-05-signed-divisor/ui/figure-receipt-v1.json').read_bytes()).hexdigest()},indent=2)+'\n');print('PATCHED',hashlib.sha256(p.read_bytes()).hexdigest())
