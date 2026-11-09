from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import json
import posixpath
import re
import shutil
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "outputs/checks/2026-11-09-mid-divisor"
PREV = ROOT / "outputs/checks/2026-11-08-cutoff-release"
STAGE = OUT / "stage-v6/inputs"
BUILDS = STAGE / "outputs/cutoff"
BASE = "/GRH-research/"
FILES = {
    "book.pdf": ("book-pdf", "main"),
    "concise.pdf": ("focused-concise", "resolutions-concise"),
    "extended.pdf": ("focused-extended", "resolutions-extended"),
    "validated-oracle-concise.pdf": ("notes-concise", "validated-oracle-concise"),
    "validated-oracle-extended.pdf": ("notes-extended", "validated-oracle-extended"),
}

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def ref(path):
    return {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": digest(path)}

def read(path):
    return json.loads(path.read_text())

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data.encode() if isinstance(data, str) else data)

def normal(value):
    return "".join(x.lower() for x in unicodedata.normalize("NFKD", value) if x.isascii() and x.isalnum())

def adapt(value):
    marker = '<script src="/GRH-research/public-base.js"></script>'
    assert marker not in value and value.count("<head>") == 1
    value = value.replace("http://127.0.0.1:8765/", BASE)
    value = re.sub(r"""((?:href|src|poster|data-source)=["'])/(?!/|GRH-research/)""",
                   lambda match: match[1]+BASE, value)
    return value.replace("<head>", "<head>"+marker, 1)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for name,value in attrs:
            if name in {"href","src","poster","data-source"} and value:
                self.targets.append(value)

def main():
    stage_manifest = STAGE.parent/"source-stage-v1.json"
    stage = read(stage_manifest)
    assert all(digest(STAGE/name)==sha for name,sha in stage["stage_inputs_sha256"].items())
    build_refs = {}
    for site_path,(folder,stem) in FILES.items():
        record = BUILDS/folder/"build-record.json"
        b = read(record)
        assert b["passed"] and not b["production_promoted"]
        assert all(digest(STAGE/name)==sha for name,sha in b["source_sha256"].items())
        pdf = BUILDS/folder/(stem+".pdf")
        assert digest(pdf)==b["pdf_sha256"]
        info = subprocess.check_output(["pdfinfo",str(pdf)],text=True)
        pages = int(re.search(r"Pages:\s+(\d+)",info)[1])
        assert pages==b.get("pdf_pages",b.get("pages"))
        body = normal(subprocess.check_output(["pdftotext",str(pdf),"-"],text=True))
        assert normal("Joint moments for the wide cutoff pairing") in body
        assert (normal("Proofs of the joint cutoff estimates") in body) == ("concise" not in folder)
        assert normal("Paired cutoffs, exact divisor signs and proved regimes") in body
        log = BUILDS/folder/(stem+".log")
        assert not re.search(r"Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!",log.read_text(),re.M)
        build_refs[site_path]={"artifact":ref(pdf),"record":ref(record),"log":ref(log),"pages":pages}
    npath = BUILDS/"native/native-build-record.json"
    n=read(npath)
    assert n["passed"] and not n["production_promoted"]
    assert n["PDF_build_record_sha256"]==build_refs["book.pdf"]["record"]["sha256"]
    assert all(digest(STAGE/name)==sha for name,sha in n["source_sha256"].items())
    assert [n[k] for k in ("chapter_count","old_literal_math_subtrees","tables","canonical_labs","svg_refs")]==[40,11657,389,14,33]
    assert not any(n[k] for k in ("new_Lean_declarations","raw_TeX_nodes","conversion_warnings"))
    book = BUILDS/"native/book"
    assert digest(book/"main.html")==n["new_HTML_sha256"]
    old = PREV/"bundle/bundle-v1/site"
    assert digest(PREV/"PUBLIC_RELEASE_VERIFIED.json")=="c1a146daabe2c169781253ae5decafd8ce5e85866c47b3864839db4a42237ab5"
    old_files={str(p.relative_to(old)):digest(p) for p in old.rglob("*") if p.is_file()}
    assert len(old_files)==649
    canonical_index=(ROOT/"web/index.html").read_text()
    source = 'This edition has <strong>363 pages · 40 chapters · 11,657 MathML expressions</strong>. The focused articles have 88 and 257 pages. The notes have 46 and 146 pages.'
    counts=[build_refs[k]["pages"] for k in FILES]
    pages,pc,pe,nc,ne=counts
    target=f'This edition has <strong>{pages} pages · 40 chapters · {n["math_nodes"]:,} MathML expressions</strong>. The focused articles have {pc} and {pe} pages. The notes have {nc} and {ne} pages.'
    assert canonical_index.count(source)==1
    canonical_index=canonical_index.replace(source,target)
    anchor='<section id="reading">'
    insert=('<p class="small">The <a href="/book/main.html#pca:joint-core">joint cutoff proofs</a> '
            'give a target estimate on the pure full-frequency unit-pair contribution for small intermediate divisors '
            'and separate bounds for selected partner frequencies and the equality-wide correction.</p>')
    assert canonical_index.count(anchor)==1
    canonical_index=canonical_index.replace(anchor,anchor+insert)
    bundle=OUT/"bundle-v2"
    site=bundle/"site"
    write(bundle/"canonical-index.html",canonical_index)
    overlay={
        "index.html":adapt(canonical_index).encode(),
        "book/main.html":adapt((book/"main.html").read_text()).encode(),
    }
    for leaf in ("weighted-cutoff.tex","joint-cutoff-core.tex","joint-cutoff-details.tex"):
        overlay["book/sources/"+leaf]=(book/"sources"/leaf).read_bytes()
    overlay.update({name:(ROOT/row["artifact"]["path"]).read_bytes() for name,row in build_refs.items()})
    for path in sorted(old.rglob("*")):
        if path.is_file():
            rel=path.relative_to(old).as_posix()
            assert not path.is_symlink()
            if rel in overlay:
                continue
            dest=site/rel
            dest.parent.mkdir(exist_ok=True,parents=True)
            shutil.copyfile(path,dest)
    for name,data in overlay.items():
        write(site/name,data)
    observed={str(p.relative_to(site)):digest(p) for p in site.rglob("*") if p.is_file()}
    assert set(observed)==set(old_files)|set(overlay)
    assert all(observed[name]==h for name,h in old_files.items() if name not in overlay)
    assert all(observed[name]!=old_files.get(name) for name in overlay)
    link_count=0
    for name in ("index.html","book/main.html"):
        parser=Links()
        parser.feed((site/name).read_text())
        for raw in parser.targets:
            parsed=urlsplit(raw)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path=unquote(parsed.path)
            if path.startswith(BASE):
                rel=path.removeprefix(BASE) or "index.html"
            elif not path.startswith("/"):
                rel=posixpath.normpath(posixpath.join(posixpath.dirname(name),path))
            else:
                raise AssertionError((name,raw))
            assert not rel.startswith("../"), (name,raw)
            dest=site/rel
            assert dest.is_file() or (dest/"index.html").is_file(), (name,raw,rel)
            link_count+=1
    result={"passed":True,"source_stage":ref(stage_manifest),"native_build":ref(npath),
        "pdfs":build_refs,"canonical_index":ref(bundle/"canonical-index.html"),
        "candidate_site":str(site.relative_to(ROOT)),
        "files":len(observed),"byte_identical_prior_leaves":len(set(old_files)-set(overlay)),
        "overlays":{name:ref(site/name) for name in sorted(overlay)},
        "local_links_checked":link_count,"MathML":n["math_nodes"],"old_math_preserved":11657,
        "live_promoted":False,"publication_pending":True}
    write(bundle/"CANDIDATE-v1.json",json.dumps(result,indent=2)+"\n")
    print(json.dumps({"book_pages":pages,"focused":[pc,pe],"notes":[nc,ne],
        "mathml":n["math_nodes"],"links":link_count,"overlays":len(overlay)}))

if __name__=="__main__":
    main()
