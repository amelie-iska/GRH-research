# Preserved diagnostic attempts

An initial Lean file failed warnings-as-errors on two unused simp arguments;
removing those arguments produced the accepted20-component file. No linter
was disabled. The full282-report suite and independently reviewed final hash
are the accepted formal evidence.

The first staged book candidate had an overfull line in the theta dimension
list. Staging validation refused promotion. A proper comparison table removed
the overfull line and final PDF/HTML builds passed. TeX4ht's intermediate
image-alt DOM warning is handled by the existing escaped-alt preparation;
final native-MathML XML is valid.

The first companion regression found an accidental test expectation change
from six models to seven during update of the book's tool count. The model
expectation was restored to six; all other updated comparisons were inspected.
The failure and corrected passing regression are preserved. No saved models
were changed. DG browser/model regressions and literal Lean source checks pass.

A current diagram export initially touched the historical book-check manifest.
The new manifest was retained separately, the historical bytes were restored
from the unchanged baseline, and the renderer's current output path was fixed
to outputs/book/diagram-exports.json. Sixteen current SVG hashes and unchanged
historical bytes were verified. No previous artifact was deleted or cleaned.
