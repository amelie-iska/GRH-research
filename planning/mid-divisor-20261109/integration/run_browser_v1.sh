#!/usr/bin/env bash
set -euC
q=$PWD/planning/mid-divisor-20261109/integration
server_script=$PWD/planning/cutoff-release-20261108/serve_public_candidate_v2.py
o=$PWD/outputs/checks/2026-11-09-mid-divisor
phase=$1
tag=$2
site=$(realpath "$3")
test "$phase" = stage || test "$phase" = live
test "$tag" = v1 || test "$tag" = v2 || test "$tag" = v3
s=$o/stage-v6/inputs
b=$s/outputs/cutoff
mkdir "$o/firefox-$phase-$tag"
server=
browser=
finish() {
  if [ -n "$browser" ]; then
    if kill -0 "$browser" 2>/dev/null; then kill -TERM "$browser"; fi
    wait "$browser" 2>/dev/null || true
  fi
  if [ -n "$server" ]; then
    if kill -0 "$server" 2>/dev/null; then kill -TERM "$server"; fi
    wait "$server" 2>/dev/null || true
  fi
  printf '{"server_pid":%s,"browser_pid":%s,"owned_processes_waited":true}\n' "${server:-null}" "${browser:-null}" > "$o/PROCESS-EXIT-$phase-$tag.json"
}
trap finish EXIT
if [ "$phase" = stage ]; then
  python3 "$server_script" --bundle "$site" --receipt "$o/SERVER-$tag.json" > "$o/server-$tag.log" 2>&1 &
  server=$!
  for n in $(seq 1 40); do
    if test -s "$o/SERVER-$tag.json"; then break; fi
    sleep .25
  done
  base=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["base"])' "$o/SERVER-$tag.json")
else
  base=https://amelie-iska.github.io/GRH-research
fi
test -z "$(ss -H -ltn '( sport = :9337 )')"
MOZ_HEADLESS=1 LIBGL_ALWAYS_SOFTWARE=1 firefox --headless --no-remote -profile "$o/firefox-$phase-$tag" --remote-debugging-port 9337 about:blank > "$o/firefox-$phase-$tag.log" 2>&1 &
browser=$!
for n in $(seq 1 80); do
  if grep -q 'WebDriver BiDi listening' "$o/firefox-$phase-$tag.log"; then break; fi
  sleep .25
done
n=$b/native/native-build-record.json
p=$b/book-pdf/build-record.json
CUTOFF_STAGE_ROOT="$s" node "$q/check_browser_v1.mjs" --phase "$phase" --base "$base" --out "$o/browser-$phase-$tag" --native-record "$n" --native-record-sha256 "$(sha256sum "$n" | cut -d' ' -f1)" --pdf-record "$p" --pdf-record-sha256 "$(sha256sum "$p" | cut -d' ' -f1)" --hosted-html-sha256 "$(sha256sum "$site/book/main.html" | cut -d' ' -f1)" > "$o/browser-$phase-$tag.txt" 2>&1
cat "$o/browser-$phase-$tag.txt"
