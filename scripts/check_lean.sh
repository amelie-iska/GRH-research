#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
# Pass --toolchain PATH, or set GRH_LEAN_TOOLCHAIN, for an existing pinned toolchain.
exec python3 "$root/extension/lean/verify_inherited.py" --package arithmetic "$@"
