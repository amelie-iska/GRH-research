#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
# Explicit --toolchain/--mathlib paths or GRH_LEAN_TOOLCHAIN/GRH_MATHLIB are portable.
exec python3 "$root/extension/lean/verify_inherited.py" --package analytic "$@"
