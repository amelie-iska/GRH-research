"""Bind the four governing PDFs to current ACTUAL inputs; disclose unused historical guards."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
CHECK = ROOT / 'outputs/checks/2026-11-05-physical-sieve/builds'
PINS = {
    'papers/physical-sieve-core.tex': 'df49c3f938ab80f80e4c0bb2efb4f71004a2d311dc21f952ecd45077dd35f939',
    'papers/physical-sieve-details.tex': '4713c2c4e8496a87a8678406d2d43f02ab0bf82e4152fed15938aef52b3b9bf4',
    'papers/coherent-main-core.tex': '5b3ab5c38b5c9130867793ac2e21c7dbc60560bc7d4eadbcc40fb1f334659f6c',
    'papers/coherent-main-details.tex': '92dfe3077dffa048471b0705539bd82b2648c2e4b021c331c2753b6fb655176f',
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def expand(path, stack=()):
    path = path.resolve()
    assert path not in stack
    def replace(match):
        name = match[1] if match[1].endswith('.tex') else match[1] + '.tex'
        return expand(ROOT / 'papers' / name, stack + (path,))
    return re.sub(r'\\input\{([^}]+)\}', replace, path.read_text())
def main():
    before = CHECK / 'run-v1/four-builds-v1.json'
    latest = CHECK / 'run-v2/extended-builds-v2.json'
    assert sha(before) == '4b3277d722299f769e89f509523577a8c1a2c06fce710d463474030028240f99'
    assert sha(latest) == '44db95d9d8e1303e704a45f3e42ae834a711c133d318fec2a90f7a3b0bf11a4e'
    old = json.loads(before.read_bytes())
    new = json.loads(latest.read_bytes())
    assert old['passed'] and new['passed']
    builds = {name: old['builds'][name] for name in ['concise-v1', 'notes-concise-v1']}
    builds.update(new['builds'])
    disclosures = []
    source_inputs = {}
    for name, data in builds.items():
        record_path = ROOT / data['build_record']
        assert sha(record_path) == data['build_record_sha256']
        record = json.loads(record_path.read_bytes())
        assert record['passed']
        for path, digest in record['source_sha256'].items():
            assert sha(ROOT / path) == digest, (name, path)
        source_inputs[name] = record['source_sha256']
        edition = 'extended' if 'extended' in name else 'concise'
        notes = name.startswith('notes-')
        stem = ('validated-oracle-' if notes else 'resolutions-') + edition
        wrapper = ROOT / 'papers' / (stem + '.tex')
        expanded_path = record_path.parent / (stem + '.expanded.tex' if notes else 'expanded-original.tex')
        assert expanded_path.read_text() == expand(wrapper), ('Current actual expansion differs', name)
        data['current_original_expanded_source_sha256'] = sha(expanded_path)
        assert sha(ROOT / data['pdf']) == data['pdf_sha256']
        assert sha(record_path.parent / (stem + '.log')) == data['log_sha256']
        for path, digest in record.get('canonical_guard_sha256', {}).items():
            current = sha(ROOT / path)
            if current != digest:
                assert name == 'notes-concise-v1' and path == 'papers/coherent-main-details.tex' and path not in record['source_sha256']
                assert digest == '20098c4210a24b0893662fe0020c6c8daf204f154bb071118f2ff207a63ac94e'
                assert current == PINS[path]
                disclosures.append(dict(build=name, path=path, historical_guard_sha256=digest, current_sha256=current, actually_compiled=False, reason='Root/C-approved native alignment-only edit after concise build; actual concise source inputs unchanged'))
    assert len(disclosures) == 1
    assert all(sha(ROOT / path) == digest for path, digest in PINS.items())
    states = json.loads((ROOT / 'outputs/checks/2026-11-05-prime-fibre/lane-b/source-and-state-pins-v1.json').read_bytes())['protected11states']
    for state in states:
        head = subprocess.check_output(['git', '-C', state['path'], 'rev-parse', 'HEAD'], env=dict(os.environ, GIT_OPTIONAL_LOCKS='0'), text=True).strip()
        assert head == state['HEAD'] and sha(Path(state['index_path'])) == state['index_sha256']
    gate = ROOT / 'outputs/checks/2026-11-05-physical-sieve/review/canonical-acceptance-v3.json'
    result = dict(passed=True, scope='Four governing PDFs only: concisev1/notesconcisev1 unchanged actual inputs, extendedv2/notesextendedv2 current native-portable alignment; intermediates preserved', aggregator_sha256=sha(Path(__file__)), initial_four_receipt_sha256=sha(before), extended_v2_receipt_sha256=sha(latest), canonical_layout_acceptance_sha256=sha(gate), final_canonical_guard_sha256=PINS, all_ACTUAL_compiled_source_bindings_current=True, actual_compiled_inputs_by_build=source_inputs, current_original_expansions_exact=True, unused_historical_guard_metadata=disclosures, builds=builds, protected11states_unchanged=True, production_edited=False, production_promoted=False, builds_rerun_by_aggregator=False)
    output = CHECK / 'four-builds-v2.json'
    with output.open('x') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps(dict(passed=True, sha256=sha(output), pages={name: data['pages'] for name, data in builds.items()})))
if __name__ == '__main__':
    main()
