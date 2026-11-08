from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / "planning/ramified-book-20261106/root"
BOOK_ROOT = '/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, text):
    with path.open("x") as handle:
        handle.write(text)

def change(text, before, after, count=1):
    assert text.count(before) == count, before
    return text.replace(before, after)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", type=Path)
    parser.add_argument("--figure-receipt", type=Path, required=True)
    args = parser.parse_args()
    stage = args.stage.resolve()
    receipt = json.loads(args.figure_receipt.read_text())
    assert receipt["status"] == "pass" and sha(args.figure_receipt) == "e5f0ff39bc316c4907934165bf75dc30a7d2d11abdbbf855539134564a1004d7"
    baseline = sha(stage/"native-baseline.json")
    asset_dir = stage/"book/figures"
    figures = {
        file.name: {"bytes": file.stat().st_size, "sha256": sha(file)}
        for file in sorted(asset_dir.glob("paired-cutoff-regimes.*"))
    }
    assert set(figures) == {f"paired-cutoff-regimes.{suffix}" for suffix in ("pdf","svg","py")}
    gate = {"passed": True, "staging_assets": figures, "semantic_review_sha256": sha(args.figure_receipt)}
    write(stage/"figure-gate.json", json.dumps(gate, indent=2)+"\n")
    builder = (INPUTS/"build_book_pdf_v1.py").read_text()
    builder = change(builder, f"ROOT = Path('{BOOK_ROOT}')", "ROOT = Path(__file__).resolve().parents[1]")
    builder = change(builder, "new_reviewed_sections=(4 if args.consume_book else 0)", "new_reviewed_sections=(2 if args.consume_book else 0)")
    write(stage/"scripts/build_cutoff_book.py", builder)
    renderer = (INPUTS/"render_native_v1.py").read_text()
    renderer = change(renderer, f'ROOT=Path("{BOOK_ROOT}")', "ROOT=Path(__file__).resolve().parents[1]")
    renderer = renderer.replace("ramified-gauss-", "paired-cutoff-").replace("ramified-cusp-prefix", "paired-cutoff-regimes")
    renderer = renderer.replace("rg:workflow", "pca:regime").replace("rg:", "pca:").replace("rg-auto-", "pca-auto-")
    renderer = renderer.replace("Rational cusp construction, pure angular Mellin identity and original full-coefficient finite-prefix estimate",
        "Pure cutoff cross regime diagram in physical erasure and insertion exponents. Filled areas meet the target over all divisors. The dashed curve depends on fixed residual labels.")
    renderer = renderer.replace("Ramified-cusp cutoff partition; horizontal scrolling on small screens",
        "Paired cutoff regime diagram with horizontal scrolling on small screens")
    renderer = renderer.replace("Ramified-cusp proof table; horizontal scrolling","Paired cutoff proof table with horizontal scrolling")
    renderer = renderer.replace('[".svg",".pdf",".tex"]', '[".svg",".pdf",".py"]')
    renderer = renderer.replace("paired-cutoff-regimes.tex","paired-cutoff-regimes.py").replace("Original figure TeX","Figure generator")
    renderer = change(renderer, 'figure_gate_rel="outputs/checks/2026-11-06-ramified-book/root/figure-acceptance-v1.json"', 'figure_gate_rel="figure-gate.json"')
    renderer = renderer.replace("outputs/checks/2026-11-06-ramified-book/root/integration-before-v1.json","native-baseline.json")
    renderer = change(renderer,"7c7ddaf75e9f6f6309d9ebc7d45e7159b76e5a26d900d6d2cc8959705fe5e26f",baseline)
    renderer = change(renderer,"(10299,389,14,31)","(10858,389,14,32)")
    renderer = renderer.replace("==10299","==10858").replace("old_literal_math_subtrees=10299","old_literal_math_subtrees=10858")
    renderer = change(renderer,"len(oldrefs)==31 and newrefs[:31]==oldrefs and len(newrefs)==32",
        "len(oldrefs)==32 and newrefs[:32]==oldrefs and len(newrefs)==33")
    renderer = change(renderer, "old_svg_refs=31,svg_refs=32", "old_svg_refs=32,svg_refs=33")
    renderer = change(renderer, "len(old_assets)==92", "len(old_assets)==98")
    start = renderer.index(" nav='<nav")
    end = renderer.index("\n",start)
    renderer = renderer[:start]+""" nav='<nav aria-label="Paired cutoffs and divisor signs"><strong>Chapter 40 proof appendix</strong><p>Exact ordered cutoff signs and proved regions for the selected equality–complement cross. The coherent divisor estimate remains open.</p><p><a href="#pca:core">Results and scope</a> · <a href="#pca:regime">Regime diagram</a> · <a href="#pca:details">Complete proofs</a> · <a href="../book.pdf">Complete book PDF</a></p></nav>'"""+renderer[end:]
    renderer = change(renderer, "Arithmetic Ramified cusps and finite-cutoff reductions", "Paired cutoffs, exact divisor signs and proved regimes")
    write(stage/"scripts/render_cutoff_native.py", renderer)
    print(json.dumps({"passed": True, "figure_gate_sha256": sha(stage/"figure-gate.json"),
        "builder_sha256": sha(stage/"scripts/build_cutoff_book.py"),
        "renderer_sha256": sha(stage/"scripts/render_cutoff_native.py")}, indent=2))

if __name__ == "__main__":
    main()
