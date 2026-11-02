#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root/papers"
for edition in concise extended; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../outputs/papers "$edition.tex"
done
