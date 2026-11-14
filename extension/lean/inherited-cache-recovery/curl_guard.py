#!/usr/bin/env python3
"""Per-invocation cache transport: sequential requests, no retries, stop on 429.

Used only in an isolated MATHLIB_CACHE_DIR; no global curl settings are changed.
The stop marker prevents a cache-client fallback from repeating a throttled request.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys

marker = Path(__file__).resolve().parent / "http-429-stop"
if marker.exists():
    raise SystemExit("bounded-cache-stop: prior HTTP 429 in this attempt")
filtered = []
arguments = iter(sys.argv[1:])
for argument in arguments:
    if argument in {"--parallel", "--parallel-immediate"}:
        continue
    if argument in {"--retry", "--parallel-max"}:
        next(arguments, None)
        continue
    filtered.append(argument)
command = [shutil.which("curl") or "/usr/bin/curl", *filtered,
           "--retry", "0", "--rate", "2/s", "--connect-timeout", "10", "--max-time", "20"]
process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
throttled = False
for line in process.stdout:
    print(line, end="", flush=True)
    try:
        status = json.loads(line).get("http_code")
    except (json.JSONDecodeError, AttributeError):
        continue
    if status == 429:
        marker.write_text("HTTP 429: this bounded cache attempt stopped without retry.\n")
        print("bounded-cache-stop: HTTP 429", file=sys.stderr, flush=True)
        process.terminate()
        throttled = True
        break
raise SystemExit(88 if throttled else process.wait())
