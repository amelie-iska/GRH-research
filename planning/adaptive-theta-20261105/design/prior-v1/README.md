# Adaptive theta parameter design

Read DESIGN.md for the mathematical contract, exact error allocation, termination proof, point/circle input distinction and practical parameter tables. The two TeX files are shared core/details proposals; they have not been installed into production papers.

The exact checker uses Python standard-library Fraction arithmetic and no producer arithmetic or special-function oracle. Six practical configurations at eta1e-24/1e-32, first-success choices, exact five-term slack, panel coverage, source pins and67 structural/negative controls pass. The exact successful report is outputs/checks/2026-11-05-adaptive-theta/design/exact-parameters-v2.json. A first attempt reached serialization but hit the Python3.11 integer decimal-digit limit; the retained failure note records it, and the checker now changes only its own process limit for exact large-denominator serialization.

The two proposals compile together using the existing Linux pdflatex, two passes, to outputs/checks/2026-11-05-adaptive-theta/design/proposal-check-v1.pdf (3pages). The second pass has no overfull, underfull, undefined-reference or LaTeX warnings. Full proposal wrapper/log/stdout files are preserved there. No production paper build or interval sampler execution was performed by this design lane.

All writes and checks took place on iska-linux-vscode in the assigned fresh design/check namespaces. Existing fixed theta/dyadic producers and final-v5 certificate hashes match the accepted pins. Original readouts and the independent arithmetic/determinant bridge are not changed. This parameter/proof check is not independent acceptance of an executable, full Lean formalization or a GRH theorem.
