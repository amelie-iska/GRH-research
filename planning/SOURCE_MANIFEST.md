# Source manifest

The machine-readable [SOURCES.json](SOURCES.json) records all three Git commit pins, relevant tracked files, byte sizes and SHA256 hashes. `.gitmodules` and Git tree entries pin the same commits. Each original clone remains a separate local Git repository with its own original history and license.

- `math/`: `4eaee87548250b2682affda7d05d947c05554bae`, Apache2.0. Selected original research family003:7/8 and11/12 zero-free half-planes, and Landau–Siegel exclusion. See the actual solution entry points under `lean/OAI/NumberTheory/`; comparator challenge files are specifications containing intentional placeholders.
- `GRH/`: `0c77122d3cff5b737fc56730f54045ef185e3df1`, MIT. The only paper is the223 pagePDF; no matching TeX source is tracked.
- `Surface-Orders-Hilbert-Polya/`: `212ff730cdfe5d9ab2dee17c11c7f83061fa0bf2`, CC0. TeX and PDF are separate tracked artifacts; only the TeX received full end-to-end textual review.

All source licenses stay in their submodules. No new blanket license is imposed on the new research text. Confirm authorship and licensing before public submission.

The search candidates and exact review scope are in [math-search-candidates.txt](math-search-candidates.txt) and [COVERAGE.md](COVERAGE.md). Submodule URLs contain no credentials. Existing local `.git` directories were retained in place rather than absorbed/moved.
