from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil

ROOT=Path(__file__).resolve().parents[2]
NOTES=ROOT/"planning/cutoff-appendix-20261108"
OUT=ROOT/"outputs/checks/2026-11-08-cutoff-appendix"
OLD_NATIVE="dc80699b472bfc53d6836f7b14c3df7de1416df05b48eab95fe68154f27f2108"
FIGURE="paired-cutoff-regimes"

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path,data):
    with path.open("xb") as handle:
        handle.write(data)

def copy(path,dest):
    dest.parent.mkdir(parents=True,exist_ok=True)
    write(dest,path.read_bytes())

def insert(path,marker,addition):
    content=path.read_text()
    assert content.count(marker)==1,(path,marker)
    path.write_text(content.replace(marker,marker+addition,1))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--attempt",required=True)
    parser.add_argument("--core",type=Path,required=True)
    parser.add_argument("--details",type=Path,required=True)
    parser.add_argument("--figure",type=Path,required=True)
    parser.add_argument("--figure-generator",type=Path,required=True)
    args=parser.parse_args()
    assert re.fullmatch(r"stage-v[1-9][0-9]*",args.attempt)
    assert digest(ROOT/"web/book/main.html")==OLD_NATIVE
    assert json.loads((OUT/"PDF-MARKER-v1.json").read_text())["returncode"]==0
    run=OUT/args.attempt
    run.mkdir()
    stage=run/"inputs"
    stage.mkdir()
    source_paths={}
    def inherited(rel):
        source=ROOT/rel
        assert not source.is_symlink()
        copy(source,stage/rel)
        source_paths[rel]=digest(source)
    for group in ("book/chapters","book/figures","papers","web/book","outputs/html-diagrams"):
        for path in sorted((ROOT/group).rglob("*")):
            if path.is_file():
                inherited(str(path.relative_to(ROOT)))
    for rel in (
        "book/main.tex","outputs/book/diagram-exports.json","scripts/build_remote_articles.py",
        "planning/physical-sieve-20261105/builds/build_notes_v1.py"):
        inherited(rel)

    # Only staged entry points gain the new material.
    additions={}
    def fresh(source,rel):
        source=source.resolve()
        assert source.is_relative_to(NOTES)
        copy(source,stage/rel)
        additions[rel]={"source":str(source.relative_to(ROOT)),"sha256":digest(source)}
    for source,kind in ((args.core,"core"),(args.details,"details")):
        name=f"paired-cutoff-{kind}.tex"
        fresh(source,"papers/"+name)
        fresh(source,"book/chapters/"+name)
    fresh(NOTES/"paired-cutoff-figure-v2.tex","book/chapters/paired-cutoff-figure.tex")
    for suffix in ("svg","pdf"):
        fresh(args.figure/(FIGURE+"."+suffix),"book/figures/"+FIGURE+"."+suffix)
    fresh(args.figure_generator,"book/figures/"+FIGURE+".py")

    book_wrapper="book/chapters/weighted-cutoff.tex"
    book_addition="\n".join(r"\input{chapters/paired-cutoff-"+kind+"}" for kind in ("core","figure","details"))
    insert(stage/book_wrapper,r"\input{chapters/ramified-gauss-details}"+"\n","\n"+book_addition+"\n")
    wrappers=[book_wrapper]
    abstract_addition=(" The paired cutoff analysis gives target-size estimates on stated pure and "
        "mixed selections of the signed equality--complement cross, with an exact ordered divisor identity.")
    for family in ("resolutions","validated-oracle"):
        for edition in ("concise","extended"):
            rel=f"papers/{family}-{edition}.tex"
            prefix="details" if edition=="extended" else "core"
            include=r"\input{paired-cutoff-core}"+"\n"
            if edition=="extended":
                include+=r"\input{paired-cutoff-details}"+"\n"
            insert(stage/rel,r"\input{ramified-gauss-"+prefix+"}"+"\n",include)
            content=(stage/rel).read_text()
            assert content.count(r"\end{abstract}")==1
            (stage/rel).write_text(content.replace(r"\end{abstract}",abstract_addition+"\n"+r"\end{abstract}",1))
            wrappers.append(rel)
    wrappers=[{"path":p,"old_sha256":source_paths[p],"stage_sha256":digest(stage/p)} for p in wrappers]
    assert all(digest(ROOT/p)==h for p,h in source_paths.items())
    before={
        "source_and_live_before":{"web/book/main.html":{"sha256":OLD_NATIVE}},
        "old_math":10858,"old_tables":389,"old_labs":14,"old_svg_refs":32,
        "old_book_assets_sha256":{p:h for p,h in source_paths.items() if p.startswith("web/book/")}
    }
    assert len(before["old_book_assets_sha256"])==98
    write(stage/"native-baseline.json",(json.dumps(before,indent=2)+"\n").encode())
    record={"passed":True,"source_input_sha256":source_paths,"wrappers":wrappers,"additions":additions,
            "native_baseline_sha256":digest(stage/"native-baseline.json"),"source_HEAD_index_untouched":True}
    write(run/"source-stage-v1.json",(json.dumps(record,indent=2)+"\n").encode())
    print(str(stage))

if __name__=="__main__":
    main()
