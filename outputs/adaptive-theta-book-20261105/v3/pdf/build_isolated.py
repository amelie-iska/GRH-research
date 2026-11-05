#!/usr/bin/env python3
"""Build an isolated complete book using exact source-matched diagram assets.

No package installation or production edit. Existing diagram geometry is reused,
not recompiled. Output is a candidate and is never promoted by this script.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess

ROOT = Path(__file__).resolve().parents[2]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--svg-only',action='store_true',help='Never read preserved standalone-PDF caches; render all19 accepted source-matched public SVGs with existing librsvg/cairo')
    parser.add_argument('--consume-book',action='store_true',help='Use actual integrated book inputs; do not append supplemental chapters')
    args = parser.parse_args()
    out = args.output.resolve()
    if out.exists():
        raise FileExistsError('Preserve all prior build attempts; choose a new output')
    out.mkdir(parents=True)
    producer_at_start=Path(__file__).read_bytes()
    (out/'build_isolated.py').write_bytes(producer_at_start)
    sources = {}
    def source(path):
        data = path.read_bytes()
        sources[str(path.relative_to(ROOT))] = sha(data)
        return data.decode()
    def expand(text, base, stack=()):
        def include(match):
            path = (base / (match[1]+'.tex')).resolve()
            if path in stack:
                raise ValueError('Recursive TeX input')
            return expand(source(path), base, stack+(path,))
        return re.sub(r'\\input\{([^}]+)\}', include, text)
    original = expand(source(ROOT/'book/main.tex'), ROOT/'book')
    manifest = json.loads(source(ROOT/'outputs/book/diagram-exports.json'))
    by_hash = {x['source_sha256']:x for x in manifest}
    diagram_records = []
    compiled = out/'compiled-diagrams'
    compiled.mkdir()
    def replace_diagram(match):
        expression = match[0]
        source_hash = sha(expression.encode())
        entry = by_hash[source_hash]
        index = len(diagram_records)
        assert entry['index']==index, 'Diagram order changed from accepted source manifest'
        svg = ROOT/'web/book'/('main'+str(index)+'x.svg')
        svg_data = svg.read_bytes()
        assert sha(svg_data)==entry['sha256'] and len(svg_data)==entry['bytes']
        cache = ROOT/'outputs/html-diagrams'/source_hash[:16]
        pdf = cache/'diagram.pdf'
        target = compiled/(source_hash+'.pdf')
        if not args.svg_only and pdf.exists():
            cache_source = (cache/'diagram.tex').read_text()
            assert expression in cache_source
            assert r'\documentclass[border=5pt]{standalone}' in cache_source
            target.write_bytes(pdf.read_bytes())
            method='source-matched preserved standalone PDF'
        else:
            # Existing native runtime; the optional GI/pycairo foreign bridge
            # is absent, so call the same stable C API using stdlib ctypes.
            import ctypes as C, ctypes.util
            import xml.etree.ElementTree as ET
            tree=ET.fromstring(svg_data)
            def points(value):
                if value.endswith('pt'):
                    return float(value[:-2])
                assert re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',value), 'Unexpected SVG units'
                # Poppler unitless dimensions equal original PDF bp coordinates.
                return float(value)
            width,height=points(tree.attrib['width']),points(tree.attrib['height'])
            class Rectangle(C.Structure):
                _fields_=[('x',C.c_double),('y',C.c_double),('width',C.c_double),('height',C.c_double)]
            rsvg=C.CDLL(C.util.find_library('rsvg-2'))
            cairo=C.CDLL(C.util.find_library('cairo'))
            gobject=C.CDLL(C.util.find_library('gobject-2.0'))
            rsvg.rsvg_handle_new_from_data.argtypes=[C.c_void_p,C.c_size_t,C.POINTER(C.c_void_p)]
            rsvg.rsvg_handle_new_from_data.restype=C.c_void_p
            rsvg.rsvg_handle_render_document.argtypes=[C.c_void_p,C.c_void_p,C.POINTER(Rectangle),C.POINTER(C.c_void_p)]
            rsvg.rsvg_handle_render_document.restype=C.c_int
            cairo.cairo_pdf_surface_create.argtypes=[C.c_char_p,C.c_double,C.c_double]
            cairo.cairo_pdf_surface_create.restype=C.c_void_p
            cairo.cairo_create.argtypes=[C.c_void_p];cairo.cairo_create.restype=C.c_void_p
            for name in ['cairo_destroy','cairo_surface_finish','cairo_surface_destroy']:
                getattr(cairo,name).argtypes=[C.c_void_p]
            gobject.g_object_unref.argtypes=[C.c_void_p]
            error=C.c_void_p();buffer=C.create_string_buffer(svg_data)
            handle=rsvg.rsvg_handle_new_from_data(buffer,len(svg_data),C.byref(error))
            assert handle and not error.value, 'SVG loading failed'
            surface=cairo.cairo_pdf_surface_create(str(target).encode(),width,height)
            context=cairo.cairo_create(surface)
            viewport=Rectangle(0,0,width,height)
            success=rsvg.rsvg_handle_render_document(handle,context,C.byref(viewport),C.byref(error))
            cairo.cairo_destroy(context);cairo.cairo_surface_finish(surface);cairo.cairo_surface_destroy(surface)
            gobject.g_object_unref(handle)
            assert success and not error.value, 'SVG rendering failed'
            method='accepted source-matched vector SVG via existing system librsvg/cairo'
        assert target.read_bytes().startswith(b'%PDF')
        diagram_records.append(dict(index=index,source_sha256=source_hash,
            accepted_svg_sha256=entry['sha256'],pdf_sha256=sha(target.read_bytes()),
            method=method,trim='5pt each edge removes the standalone preamble border',
            source_environment=match[1]))
        return r'\includegraphics[trim=5pt 5pt 5pt 5pt,clip]{compiled-diagrams/'+source_hash+'.pdf}'
    text = re.sub(r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}', replace_diagram, original, flags=re.S)
    assert len(diagram_records)==len(manifest)==19
    assert text.count(r'\usepackage{microtype,graphicx,tikz,tikz-cd,fancyhdr}')==1
    text=text.replace(r'\usepackage{microtype,graphicx,tikz,tikz-cd,fancyhdr}',r'\usepackage{microtype,graphicx,xcolor,fancyhdr}')
    text,n=re.subn(r'^\\usetikzlibrary\{[^}]+\}\s*\n','',text,flags=re.M);assert n==1
    assert not re.search(r'\\(?:tikz|pgf|usetikz|foreach|node\b)',text)
    # Copy only existing figure assets referenced by the complete expanded book.
    figure_records=[]
    for name in sorted(set(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text))):
        if name.startswith('compiled-diagrams/'):
            continue
        src=ROOT/'book'/name
        if not src.suffix:
            src=src.with_suffix('.pdf')
        dest=out/src.relative_to(ROOT/'book');dest.parent.mkdir(parents=True,exist_ok=True)
        data=src.read_bytes();dest.write_bytes(data)
        figure_records.append(dict(path=str(src.relative_to(ROOT)),sha256=sha(data)))
    if not args.consume_book:
        additions=[]
        for chapter,names in [
            ('Validated completed Dirichlet targets and rational readouts',['validated-oracle-core','validated-oracle-details']),
            ('The original-family Hecke moment and full masked remainder',['masked-moment-core','masked-moment-details'])]:
            additions.append('\\chapter{'+chapter+'}\n')
            for name in names:
                additions.append(expand(source(ROOT/'papers'/(name+'.tex')),ROOT/'papers'))
        # Avoid a duplicate chapter/section label; every new source label is unique.
        new_text='\n'.join(additions)
        old_labels=set(re.findall(r'\\label\{([^}]+)\}',text))
        new_labels=re.findall(r'\\label\{([^}]+)\}',new_text)
        assert len(set(new_labels))==len(new_labels) and not old_labels.intersection(new_labels)
        part='\\part{Certified analytic targets and the arithmetic moment frontier}\n'+new_text+'\n'
        assert text.count(r'\backmatter')==1
        text=text.replace(r'\backmatter',part+r'\backmatter')
    (out/'main.tex').write_text(text)
    (out/'source-expansion-before-diagram-replacement.tex').write_text(original)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    for turn in [1,2,3]:
        with (out/f'build-pass{turn}.log').open('w') as log:
            run=subprocess.run(['nice','-n','15','pdflatex','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=out,env=env,stdout=log,stderr=subprocess.STDOUT)
        if run.returncode:
            raise RuntimeError('PDF build failed; preserved log '+str(out/f'build-pass{turn}.log'))
    final_log=(out/'main.log').read_text()
    bad=[line for line in final_log.splitlines() if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined',line)]
    if bad:
        raise RuntimeError('Build not acceptable; retained warnings '+repr(bad))
    assert all(sha((ROOT/name).read_bytes())==value for name,value in sources.items()), 'Source changed during build'
    info=subprocess.check_output(['pdfinfo',str(out/'main.pdf')],text=True)
    pages=int(re.search(r'Pages:\s+(\d+)',info)[1])
    html=(ROOT/'web/book/main.html').read_bytes()
    assert Path(__file__).read_bytes()==producer_at_start, 'Builder changed during run'
    record=dict(passed=True,builder_sha256=sha(producer_at_start),pdf_pages=pages,pdf_sha256=sha((out/'main.pdf').read_bytes()),
        source_sha256=sources,diagram_records=diagram_records,figure_records=figure_records,
        original_expanded_source_sha256=sha(original.encode()),new_chapters=(3 if args.consume_book else 2),
        consume_actual_integrated_book=args.consume_book,diagram_asset_mode=('accepted-public-SVG-only' if args.svg_only else 'preserved-PDF-cache-with-accepted-SVG-fallback'),diagram_cache_reads=sum(x['method']=='source-matched preserved standalone PDF' for x in diagram_records),
        production_edited=False,production_promoted=False,
        original_HTML_sha256=sha(html),canonical_labs=html.count(b'class="reader-lab"'),
        native_HTML_rebuilt=False,new_Lean_declarations=0,
        scope='Complete source expansion and reviewed new chapters;19 source-matched diagrams reused as vector assets. No TikZ/MathML/Lean toolchain installation or theorem-proving claim.')
    assert record['canonical_labs']==13
    (out/'build-record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(passed=True,pages=pages,new_chapters=record['new_chapters'],diagrams=19,promoted=False,record=str(out/'build-record.json')),indent=2))

if __name__=='__main__':
    main()
