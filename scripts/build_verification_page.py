from theme_assets import install_theme
from pathlib import Path
import html
root=Path(__file__).resolve().parents[1]
text=(root/'book/VERIFICATION.md').read_text()
(root/'web/verification.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Verification coverage</title><link rel="stylesheet" href="/style.css"></head><body><main><section><h1>Verification and inclusion</h1><p><a href="/book/main.html">On-page book</a> · <a href="/source-volumes.html">Complete original sources</a></p><pre>'+html.escape(text)+'</pre></section></main></body></html>')

install_theme(root/"web/verification.html")
