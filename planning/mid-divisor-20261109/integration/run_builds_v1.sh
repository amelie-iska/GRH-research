#!/usr/bin/env bash
set -euC
s=$(realpath "$1")
cd "$s"
mkdir outputs/cutoff
export PYTHONDONTWRITEBYTECODE=1
result=0
python3 scripts/build_cutoff_book.py --consume-book --output "$s/outputs/cutoff/book-pdf" > "$s/outputs/cutoff/book-build.txt" 2>&1 &
book=$!
python3 scripts/build_remote_articles.py --edition concise --output "$s/outputs/cutoff/focused-concise" > "$s/outputs/cutoff/focused-concise.txt" 2>&1 &
concise=$!
python3 scripts/build_remote_articles.py --edition extended --output "$s/outputs/cutoff/focused-extended" > "$s/outputs/cutoff/focused-extended.txt" 2>&1 &
extended=$!
notes=(--root-go --physical-core-sha "$(sha256sum papers/physical-sieve-core.tex | cut -d' ' -f1)" --physical-details-sha "$(sha256sum papers/physical-sieve-details.tex | cut -d' ' -f1)" --coherent-core-sha "$(sha256sum papers/coherent-main-core.tex | cut -d' ' -f1)" --coherent-details-sha "$(sha256sum papers/coherent-main-details.tex | cut -d' ' -f1)")
for part in core details; do
  notes+=(--joint-"$part"-sha "$(sha256sum "papers/joint-cutoff-$part.tex" | cut -d' ' -f1)")
done
for ed in concise extended; do
  python3 planning/physical-sieve-20261105/builds/build_notes_v1.py "${notes[@]}" --edition "$ed" --output "$s/outputs/cutoff/notes-$ed" > "$s/outputs/cutoff/notes-$ed.txt" 2>&1 &
  if [ "$ed" = concise ]; then notes_concise=$!; else notes_extended=$!; fi
done
if wait "$book"; then
  if ! python3 scripts/render_cutoff_native.py --output "$s/outputs/cutoff/native" --pdf-build "$s/outputs/cutoff/book-pdf" > "$s/outputs/cutoff/native-build.txt" 2>&1; then result=1; fi
else
  result=1
fi
for pid in "$concise" "$extended" "$notes_concise" "$notes_extended"; do
  wait "$pid" || result=1
done
for log in outputs/cutoff/*.txt; do echo "$log"; tail -n 12 "$log"; done
exit "$result"
