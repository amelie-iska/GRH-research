"""Three-pass staging notes build; all four new fragments are guarded before writing.
The root already executed its five-PDF edit marker once. This helper does not invoke it.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
FRAGMENTS = {
    'physical-core': ('physical-sieve-core.tex', 'phy:core', 'A sieve comparison indexed by the physical radicand'),
    'physical-details': ('physical-sieve-details.tex', 'phy:details', 'Proof of the physical-row sieve application'),
    'coherent-core': ('coherent-main-core.tex', 'cmr:core', 'The coherent signed main and its remaining inputs'),
    'coherent-details': ('coherent-main-details.tex', 'cmr:details', 'Proofs for the coherent main reductions'),
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalize(text):
    return ''.join(c.lower() for c in unicodedata.normalize('NFKD', text) if c.isascii() and c.isalnum())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--edition', choices=['concise', 'extended'], required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--root-go', action='store_true')
    for key in FRAGMENTS:
        parser.add_argument('--' + key + '-sha', required=True)
    args = parser.parse_args()
    assert args.root_go, 'Await explicit root source-integration GO'
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    out = args.output.resolve()
    assert out.is_relative_to(ROOT / 'outputs') and not out.exists(), 'Use a fresh staging output; preserve prior attempts'
    guarded = {}
    fragment_markers = {}
    for key, (name, label, marker) in FRAGMENTS.items():
        path = ROOT / 'papers' / name
        digest = getattr(args, key.replace('-', '_') + '_sha')
        assert sha(path) == digest, 'Canonical source changed: ' + name
        text = path.read_text()
        assert '\\label{' + label + '}' in text and marker in text, 'Required source marker missing: ' + name
        guarded[str(path.relative_to(ROOT))] = digest
        fragment_markers[name] = marker
    sources = {}
    base = ROOT / 'papers'
    wrapper = base / ('validated-oracle-' + args.edition + '.tex')
    def expand(path, stack=()):
        path = path.resolve()
        assert path not in stack, 'Recursive input cycle'
        name = str(path.relative_to(ROOT))
        digest = sha(path)
        if name in sources:
            assert sources[name] == digest
        sources[name] = digest
        text = path.read_text()
        def replace(match):
            name = match[1] if match[1].endswith('.tex') else match[1] + '.tex'
            return expand(base / name, stack + (path,))
        return re.sub(r'\\input\{([^}]+)\}', replace, text)
    text = expand(wrapper)
    relevant = [key for key in FRAGMENTS if key.endswith('core') or args.edition == 'extended']
    for key in relevant:
        name, label, marker = FRAGMENTS[key]
        assert sources['papers/' + name] == guarded['papers/' + name]
        assert '\\label{' + label + '}' in text
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    assert len(labels) == len(set(labels)), 'Duplicate source labels'
    def unchanged():
        return all(sha(ROOT / name) == digest for name, digest in {**sources, **guarded}.items())
    assert unchanged()
    snapshot = Path(__file__).read_bytes()
    out.mkdir(parents=True)
    (out / 'builder.py').write_bytes(snapshot)
    try:
        stem = 'validated-oracle-' + args.edition
        target = out / (stem + '.expanded.tex')
        target.write_text(text)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
        for turn in (1, 2, 3):
            with (out / f'build-pass{turn}.txt').open('x') as log:
                subprocess.run(['nice', '-n', '15', 'pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-jobname=' + stem, '-output-directory=' + str(out), str(target)], cwd=out, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
        log_path = out / (stem + '.log')
        log = log_path.read_text()
        bad = [line for line in log.splitlines() if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!', line)]
        assert not bad, bad
        pdf = out / (stem + '.pdf')
        assert pdf.read_bytes().startswith(b'%PDF')
        info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
        pages = int(re.search(r'Pages:\s+(\d+)', info)[1])
        extract = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
        (out / 'extracted-text.txt').write_text(extract)
        checked_markers = []
        for key in relevant:
            marker = FRAGMENTS[key][2]
            assert normalize(marker) in normalize(extract), 'PDF proof marker missing: ' + marker
            checked_markers.append(marker)
        assert unchanged() and Path(__file__).read_bytes() == snapshot
        record = dict(passed=True, builder_sha256=hashlib.sha256(snapshot).hexdigest(), canonical_guard_sha256=guarded, guarded_fragment_markers=fragment_markers, source_sha256=sources, pdf_sha256=sha(pdf), pdf_pages=pages, log_sha256=sha(log_path), expanded_source_sha256=sha(target), source_unchanged=True, PDF_markers_checked=checked_markers, all_four_canonical_sources_guarded=True, CPU_affinity_count=len(os.sched_getaffinity(0)), pdflatex_nice_increment=15, PDF_skill_marker_invoked=False, production_edited=False, production_promoted=False, new_Lean_declarations=0)
        with (out / 'build-record.json').open('x') as output:
            json.dump(record, output, indent=2)
            output.write('\n')
        print(json.dumps(dict(passed=True, edition=args.edition, output=str(out), pages=pages)))
    except Exception as error:
        failure = dict(passed=False, error_type=type(error).__name__, error=str(error), source_sha256=sources, canonical_guard_sha256=guarded, source_unchanged=unchanged(), builder_sha256=hashlib.sha256(snapshot).hexdigest(), production_edited=False, production_promoted=False, PDF_skill_marker_invoked=False)
        with (out / 'failure-record.json').open('x') as output:
            json.dump(failure, output, indent=2)
            output.write('\n')
        raise

if __name__ == '__main__':
    main()
