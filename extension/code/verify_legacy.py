#!/usr/bin/env python3
"""Verify the generated legacy bundle's hashes, size limits and static delivery."""

# Otherwise -O can bypass the source/hash assertions and still publish a pass.
if not __debug__:
    raise RuntimeError("Verification requires assertions; run without -O or PYTHONOPTIMIZE")

from concurrent.futures import ThreadPoolExecutor
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
from threading import Thread
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'extension/site'
REVIEW = ROOT / 'extension/review'
LIMIT = 25 * 1024 * 1024


def sha(data):
    return hashlib.sha256(data).hexdigest()


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    manifest_path = REVIEW / 'legacy-build.json'
    manifest = json.loads(manifest_path.read_text())
    assert not manifest['missing_originals']
    assert not manifest['static_audit']['unresolved_references']
    for row in manifest['assets']:
        served = (SITE / 'legacy' / row['path']).read_bytes()
        assert len(served) == row['served_bytes'] and sha(served) == row['served_sha256'], row['path']
        if 'source' in row:
            assert sha((ROOT / row['source']).read_bytes()) == row['source_sha256'], row['source']
    oversized = [str(p.relative_to(SITE)) for p in SITE.rglob('*') if p.is_file() and p.stat().st_size > LIMIT]
    assert not oversized, oversized
    adapter = json.loads(subprocess.check_output(
        ['node', str(ROOT / 'extension/code/verify_legacy_runtime.cjs')], text=True))
    paths = sorted('/legacy/' + row['path'] for row in manifest['assets'])
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(SITE)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def check(path):
        url = f'http://127.0.0.1:{server.server_port}' + quote(path, safe='/')
        with urlopen(Request(url, method='HEAD'), timeout=10) as response:
            return {'path': path, 'status': response.status,
                    'bytes': int(response.headers['Content-Length']),
                    'type': response.headers.get_content_type()}

    try:
        with ThreadPoolExecutor(max_workers=8) as executor:
            checks = list(executor.map(check, paths))
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    failures = [row for row in checks if row['status'] != 200 or row['bytes'] > LIMIT]
    result = {'method': 'Source/served SHA256 checks and HTTP HEAD against a local static server',
              'build_manifest_sha256': sha(manifest_path.read_bytes()),
              'assets_checked': len(checks), 'passed': not failures and adapter['passed'],
              'failures': failures, 'site_files_over_25_MiB': oversized,
              'runtime_adapter_checks': adapter,
              'pdf_downloads': [row for row in checks if row['path'].endswith('.pdf')],
              'video_assets': [row for row in checks if row['path'].endswith('.mp4')],
              'runtime_adapter': next(row for row in checks if row['path'].endswith('/legacy-base.js'))}
    (REVIEW / 'legacy-http-check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ['assets_checked', 'passed', 'site_files_over_25_MiB', 'runtime_adapter_checks']}))
    assert result['passed'], failures


if __name__ == '__main__':
    main()
