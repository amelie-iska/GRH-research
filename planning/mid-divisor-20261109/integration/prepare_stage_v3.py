from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PREV = ROOT / "outputs/checks/2026-11-08-cutoff-release"
OUT = ROOT / "outputs/checks/2026-11-09-mid-divisor"
JOINT = ROOT / "outputs/checks/2026-11-09-joint-unit-pair"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(p, value):
    p.parent.mkdir(exist_ok=True, parents=True)
    with p.open("xb") as h:
        h.write(value.encode() if isinstance(value, str) else value)

def replace(value, old, new):
    assert value.count(old) == 1, old
    return value.replace(old, new, 1)

def adapt_renderer(raw):
    renderer = raw[:raw.index(" figure_gate_rel=")]
    renderer = replace(renderer, "Append only the reviewed ramified-gauss continuation", "Append only the reviewed joint cutoff proofs")
    renderer = replace(renderer, ';ap.add_argument("--figure-gate-sha",required=True)', '')
    renderer = replace(renderer,
        ' names=["book/chapters/paired-cutoff-core.tex","book/chapters/paired-cutoff-figure.tex","book/chapters/paired-cutoff-details.tex","book/chapters/wide-cutoff-core.tex","book/chapters/wide-cutoff-details.tex"]',
        ' names=["book/chapters/joint-cutoff-core.tex","book/chapters/joint-cutoff-details.tex"]')
    renderer = replace(renderer,
        ' for n in ["book/main.tex"]+names:',
        ' read("book/chapters/weighted-cutoff.tex")\n for n in ["book/main.tex","book/chapters/weighted-cutoff.tex"]+names:')
    renderer += r''' source_count=len(re.findall(r"\\begin\{(?:theorem|lemma|proposition|corollary|definition|example|remark)\}",body))
 assert source_count==len(theorem_records),(source_count,len(theorem_records))
 oldbytes=(ROOT/"web/book/main.html").read_bytes();baseline=oldbytes.decode()
 (out/"baseline-book.html").write_bytes(oldbytes)
 gate=json.loads((ROOT/"joint-native-baseline.json").read_text())
 assert gate["html"]==sha(oldbytes)
 assert gate["html"]==pdf_record["original_HTML_sha256"]
 old_ids=set(re.findall(r'\bid="([^"]+)"',baseline));new_ids=re.findall(r'\bid="([^"]+)"',fragment)
 assert len(new_ids)==len(set(new_ids)),[x for x,c in collections.Counter(new_ids).items() if c>1]
 for ident in sorted(set(new_ids)&old_ids):
  assert ident not in source_labels
  fragment=fragment.replace('id="'+ident+'"','id="joint-auto-'+ident+'"').replace('href="#'+ident+'"','href="#joint-auto-'+ident+'"')
 ids=set(re.findall(r'\bid="([^"]+)"',fragment))
 assert set(source_labels)<=ids,("Lost labels",set(source_labels)-ids)
 assert not old_ids&ids
 for ident in re.findall(r'href="#([^"]+)"',fragment):assert html.unescape(ident) in ids|old_ids,ident
 links='<p class="source-links">Joint cutoff TeX sources: '+' · '.join('<a href="sources/'+Path(n).name+'">'+Path(n).name+'</a>' for n in names)+'</p>'
 insertion='<div id="joint-cutoff-proof">'+links+fragment+"</div>\n"
 cutoff_end=re.compile(r'</section>\n(?=<h2 class="likechapterHead"><a\s+id="[^"]+"></a>Bibliography</h2>)')
 matches=list(cutoff_end.finditer(baseline));assert len(matches)==1
 where=matches[0].start()
 combined=baseline[:where]+insertion+baseline[where:]
 assert combined.replace(insertion,"",1)==baseline
 tree=ET.fromstring(combined);oldtree=ET.fromstring(baseline)
 pattern=r"<math\b[^>]*>.*?</math>"
 oldmath=re.findall(pattern,baseline,re.S);allmath=re.findall(pattern,combined,re.S)
 assert len(oldmath)==11657 and len(allmath)==len(oldmath)+len(maths)
 index=iter(allmath)
 assert all(any(other==x for other in index) for x in oldmath)
 oldframes=[ET.tostring(e) for e in oldtree.iter("iframe")];frames=[ET.tostring(e) for e in tree.iter("iframe")]
 assert len(oldframes)==14 and frames==oldframes
 oldtables=re.findall(r"<table\b[^>]*>.*?</table>",baseline,re.S)
 assert len(oldtables)==389 and re.findall(r"<table\b[^>]*>.*?</table>",combined,re.S)==oldtables
 assets=r'(?:src|data)="([^"]+\.svg)"'
 oldrefs=re.findall(assets,baseline)
 assert len(oldrefs)==33 and re.findall(assets,combined)==oldrefs
 malformed=[]
 for elem in ET.fromstring("<div>"+fragment+"</div>").iter():
  tag=elem.tag.rsplit("}",1)[-1]
  if tag in {"msub","msup","munder","mover"} and len(elem)!=2:malformed.append(tag)
  if tag in {"msubsup","munderover"} and len(elem)!=3:malformed.append(tag)
 assert not malformed,malformed
 target=out/"book";shutil.copytree(ROOT/"web/book",target)
 (target/"main.html").write_text(combined)
 wrapper="sources/weighted-cutoff.tex"
 (target/wrapper).write_bytes((ROOT/"book/chapters/weighted-cutoff.tex").read_bytes())
 for n in names:
  with (target/"sources"/Path(n).name).open("xb") as stream:
   stream.write((ROOT/n).read_bytes())
 unchanged={}
 for name,digest in gate["book_asset_sha256"].items():
  if name not in {"main.html",wrapper}:
   assert sha((target/name).read_bytes())==digest,name
   unchanged[name]=digest
 (out/"fragment-resolved.html").write_text(fragment)
 assert all(sha((ROOT/n).read_bytes())==digest for n,digest in sources.items())
 assert Path(__file__).read_bytes()==producer
 rec=dict(passed=True,native_MathML=True,chapter_count=40,math_nodes_added=len(maths),math_nodes=len(allmath),
  old_literal_math_subtrees=len(oldmath),old_math_byte_identical=True,old_HTML_restored_exactly=True,
  tables=389,canonical_labs=14,svg_refs=33,old_assets_unchanged=unchanged,headings=heading_records,
  theorems=theorem_records,equations=equation_records,references=references,source_sha256=sources,
  pdf_aux_sha256=sha(aux),PDF_build_record_sha256=sha((pdf/"build-record.json").read_bytes()),
  pandoc_sha256=sha(PANDOC.read_bytes()),old_HTML_sha256=sha(oldbytes),new_HTML_sha256=sha(combined.encode()),
  renderer_sha256=sha(producer),production_promoted=False,new_Lean_declarations=0,raw_TeX_nodes=0,
  conversion_warnings=0)
 (out/"native-build-record.json").write_text(json.dumps(rec,indent=2)+"\n")
 print(json.dumps({k:rec[k] for k in ["passed","math_nodes","math_nodes_added","tables","canonical_labs","svg_refs","production_promoted"]}))
if __name__=="__main__":main()
'''
    return renderer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--fragments", type=Path, default=HERE)
    a = parser.parse_args()
    assert re.fullmatch(r"stage-v[1-9][0-9]*", a.attempt)
    a.fragments = a.fragments.resolve()
    assert a.fragments.is_relative_to(HERE)
    stage = OUT / a.attempt / "inputs"
    assert not stage.parent.exists()
    gate = PREV / "INTEGRATION_ACCEPTED-v1.json"
    assert sha(gate.read_bytes()) == "3639402fbec2c85a3073c467f270ba41736575446aeb374f13c7d4ac33d64d93"
    accept = json.loads(gate.read_text())
    assert accept["passed"]
    receipt = JOINT / "RESEARCH_ACCEPTED-v1.json"
    assert sha(receipt.read_bytes()) == "0d53232b6c9c9563acb60444e219a1dd86a439e6a1078a71054edbc29f1648e7"
    base = ROOT / accept["stage"]
    prev = ROOT / accept["source_stage"]["path"]
    assert sha(prev.read_bytes()) == accept["source_stage"]["sha256"]
    source = json.loads(prev.read_text())
    inventory = source["staged_input_sha256"]
    assert len(inventory) == 532
    old_html = (ROOT/"web/book/main.html").read_bytes()
    assert sha(old_html) == accept["native_book"]["sha256"]
    native_source = PREV/"bundle/bundle-v1/site/book"
    old_book = {str(p.relative_to(native_source)):p.read_bytes() for p in sorted(native_source.rglob("*")) if p.is_file()}
    assert (base/"outputs/cutoff/native/book/main.html").read_bytes() == old_html
    old_book["main.html"] = old_html
    assert all((ROOT/"web/book"/name).read_bytes()==data for name,data in old_book.items())
    fragments = {f"joint-cutoff-{part}.tex":(a.fragments/f"joint-cutoff-{part}.tex").read_bytes() for part in ("core","details")}
    modified = {}
    for name in source["wrappers"]:
        path = base/name
        text = path.read_text()
        assert (ROOT/name).read_bytes() == path.read_bytes(), ("Concurrent canonical source",name)
        location = "chapters/" if name.startswith("book/") else ""
        full = not name.endswith("-concise.tex")
        marker = "\\input{"+location+"wide-cutoff-"+("details" if full else "core")+"}\n"
        lines = [f"\\input{{{location}{Path(fragment).stem}}}\n" for fragment in fragments if full or fragment.endswith("-core.tex")]
        modified[name] = replace(text,marker,marker+"".join(lines))
    name = "scripts/build_cutoff_book.py"
    modified[name] = replace((base/name).read_text(), "new_reviewed_sections=(4 if args.consume_book else 0)", "new_reviewed_sections=(6 if args.consume_book else 0)")
    name = "scripts/render_cutoff_native.py"
    modified[name] = adapt_renderer((base/name).read_text())
    name = "planning/physical-sieve-20261105/builds/build_notes_v1.py"
    notes = (base/name).read_text()
    notes = replace(notes, "}\n\ndef sha", """    'joint-core': ('joint-cutoff-core.tex', 'pca:joint-core', 'Joint moments for the wide cutoff pairing'),
    'joint-details': ('joint-cutoff-details.tex', 'pca:joint-details', 'Proofs of the joint cutoff estimates'),
}

def sha""")
    modified[name] = notes.replace("all_four_canonical_sources_guarded=True", "all_six_canonical_sources_guarded=True")
    for name,digest in inventory.items():
        data = (base/name).read_bytes()
        assert sha(data)==digest, ("Accepted staging changed",name)
        if name.startswith("web/book/"):
            assert name.removeprefix("web/book/") in old_book, name
            continue
        write(stage/name, modified.get(name, data))
    for name,data in old_book.items():
        write(stage/"web/book"/name,data)
    for dest in ("book/chapters","papers"):
        for name,data in fragments.items():
            write(stage/dest/name,data)
    write(stage/"joint-native-baseline.json", json.dumps({"html":sha(old_html),
        "book_asset_sha256":{p:sha(b) for p,b in old_book.items()}},indent=2)+"\n")
    inputs = {str(p.relative_to(stage)):sha(p.read_bytes()) for p in sorted(stage.rglob("*")) if p.is_file()}
    record={"passed":True,"prior_integration_sha256":sha(gate.read_bytes()),
        "prior_release_native_html_sha256":sha(old_html),"research_receipt_sha256":sha(receipt.read_bytes()),
        "fragments_sha256":{k:sha(v) for k,v in fragments.items()},"wrappers":source["wrappers"],
        "stage_inputs_sha256":inputs,"producer_sha256":sha(Path(__file__).read_bytes()),"production_promoted":False}
    write(stage.parent/"source-stage-v1.json",json.dumps(record,indent=2)+"\n")
    print(stage)

if __name__=="__main__":
    main()
