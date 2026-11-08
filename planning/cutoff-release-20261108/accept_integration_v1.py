from pathlib import Path
from hashlib import sha256
import argparse
import json
import re
import subprocess
import unicodedata

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"outputs/checks/2026-11-08-cutoff-release"
OLD=ROOT/"outputs/checks/2026-11-08-cutoff-appendix"

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def ref(path):
    path=path.resolve()
    return {"path":str(path.relative_to(ROOT)),"sha256":digest(path),"bytes":path.stat().st_size}

def normal(text):
    return "".join(c.lower() for c in unicodedata.normalize("NFKD",text) if c.isascii() and c.isalnum())

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--stage",type=Path,required=True)
    p.add_argument("--review",type=Path,required=True)
    p.add_argument("--review-sha",required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    stage=a.stage.resolve()
    assert stage.is_relative_to(OUT)
    manifest=stage.parent/"source-stage-v1.json"
    sources=json.loads(manifest.read_text())
    review=json.loads(a.review.read_text())
    assert digest(a.review)==a.review_sha and review["passed"]
    assert sources["wide_sha256"]==review["wide_sha256"]
    assert all(digest(stage/name)==sha for name,sha in sources["staged_input_sha256"].items())
    old=json.loads((OLD/"STAGE_ACCEPTED-v1.json").read_text())
    builds=stage/"outputs/cutoff"
    entries={
        "book":("book-pdf","main","book.pdf"),
        "focused-concise":("focused-concise","resolutions-concise","concise.pdf"),
        "focused-extended":("focused-extended","resolutions-extended","extended.pdf"),
        "notes-concise":("notes-concise","validated-oracle-concise","validated-oracle-concise.pdf"),
        "notes-extended":("notes-extended","validated-oracle-extended","validated-oracle-extended.pdf"),
    }
    records={}
    for kind,(folder,stem,target) in entries.items():
        place=builds/folder
        record_path=place/"build-record.json"
        record=json.loads(record_path.read_text())
        assert record["passed"] and not record["production_promoted"]
        assert all(digest(stage/name)==sha for name,sha in record["source_sha256"].items())
        pdf=place/f"{stem}.pdf"
        pdf_info=subprocess.check_output(["pdfinfo",str(pdf)],text=True)
        pages=int(re.search(r"Pages:\s+(\d+)",pdf_info)[1])
        assert pages==record.get("pdf_pages",record.get("pages"))
        assert digest(pdf)==record["pdf_sha256"]
        body=normal(subprocess.check_output(["pdftotext",str(pdf),"-"],text=True))
        assert normal("Paired cutoffs, exact divisor signs and proved regimes") in body
        assert normal(review["core_heading"]) in body
        prefix="book/chapters" if kind=="book" else "papers"
        assert record["source_sha256"][f"{prefix}/wide-cutoff-core.tex"]==review["wide_sha256"]["core"]
        if not kind.endswith("-concise"):
            assert normal(review["details_heading"]) in body
            assert record["source_sha256"][f"{prefix}/wide-cutoff-details.tex"]==review["wide_sha256"]["details"]
        log=place/f"{stem}.log"
        assert not re.search(r"Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!",log.read_text(),re.M)
        records[kind]={"artifact":ref(pdf),"build":ref(record_path),"log":ref(log),"pages":pages,"site_path":target}
    native=builds/"native/native-build-record.json"
    nr=json.loads(native.read_text())
    assert nr["passed"] and nr["old_HTML_restored_exactly"] and nr["old_math_byte_identical"]
    assert nr["PDF_build_record_sha256"]==records["book"]["build"]["sha256"]
    assert all(digest(stage/name)==sha for name,sha in nr["source_sha256"].items())
    assert [nr[k] for k in ("chapter_count","old_literal_math_subtrees","tables","canonical_labs","svg_refs")]==[40,10858,389,14,33]
    assert not any(nr[k] for k in ("new_Lean_declarations","raw_TeX_nodes","conversion_warnings"))
    assert nr["math_nodes"]>11505
    book=builds/"native/book/main.html"
    assert digest(book)==nr["new_HTML_sha256"]
    previous=ROOT/old["native_book"]["path"]
    assert digest(previous)==old["native_book"]["sha256"]
    pattern=r"<math\b[^>]*>.*?</math>"
    prev=re.findall(pattern,previous.read_text(),re.S)
    math=re.findall(pattern,book.read_text(),re.S)
    assert len(prev)==11505 and len(math)==nr["math_nodes"]
    cursor=iter(math)
    assert all(any(other==x for other in cursor) for x in prev)
    assert "The dotted curve depends on fixed residual labels." in book.read_text()
    mapping={"book/main.html":ref(book)}
    wrapper=stage/"book/chapters/weighted-cutoff.tex"
    mapping["book/sources/weighted-cutoff.tex"]=ref(wrapper)
    for name in (
        "sources/paired-cutoff-core.tex","sources/paired-cutoff-figure.tex","sources/paired-cutoff-details.tex",
        "sources/wide-cutoff-core.tex","sources/wide-cutoff-details.tex",
        "figures/paired-cutoff-regimes.svg","figures/paired-cutoff-regimes.pdf","figures/paired-cutoff-regimes.py"):
        mapping[f"book/{name}"]=ref(builds/"native/book"/name)
    assert all(sha==digest(ROOT/name) for name,sha in json.loads((ROOT/old["source_stage"]["path"]).read_text())["source_input_sha256"].items())
    record={"passed":True,"publication_pending":True,"stage":str(stage.relative_to(ROOT)),
            "source_stage":ref(manifest),"wide_review":ref(a.review),"pdfs":records,"native_build":ref(native),
            "native_book":ref(book),"native_site_mapping":mapping,"prior_staged_literal_math_subtrees":11505,
            "mathml":nr["math_nodes"],"chapters":40,"tables":389,"canonical_iframes":14,"svg_refs":33}
    with a.output.open("x") as f:
        json.dump(record,f,indent=2)
        f.write("\n")
    print(json.dumps({"pages":[x["pages"] for x in records.values()],"MathML":nr["math_nodes"],"receipt_sha256":digest(a.output)}))

if __name__=="__main__":
    main()
