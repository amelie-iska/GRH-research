#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
mathlib="$root/.tools/mathlib4-v4.24.0"
lean_bin="$root/.tools/lean-4.24.0-darwin_aarch64/bin"
expected=f897ebcf72cd16f89ab4577d0c826cd14afaafc7
[ "$(git -C "$mathlib" rev-parse HEAD)" = "$expected" ]
cmp "$mathlib/lake-manifest.json" "$root/lean-analytic/mathlib-manifest.json"
export PATH="$lean_bin:$PATH"
cd "$mathlib"
for source in "$root"/lean-analytic/*.lean; do
  lake env lean -DwarningAsError=true "$source"
done
