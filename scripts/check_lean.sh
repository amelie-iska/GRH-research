#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
lean_bin="$root/.tools/lean-4.24.0-darwin_aarch64/bin"
if [ ! -x "$lean_bin/lean" ]; then
  echo "Pinned local Lean missing; see lean/README.md" >&2
  exit 1
fi
export PATH="$lean_bin:$PATH"
cd "$root/lean"
lake build
lake env lean GRHResearch.lean
