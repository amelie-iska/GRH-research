"""Shared theme head assets; no changes to document bodies or research sources."""
from pathlib import Path
import re
ASSETS='<link rel="stylesheet" href="/theme.css" data-site-theme="palette" />\n<script src="/theme.js" data-site-theme="controller"></script>\n'
def attach_theme(text):
    text=re.sub(r'<link\b[^>]*data-site-theme="palette"[^>]*>\s*','',text)
    text=re.sub(r'<script\b[^>]*data-site-theme="controller"[^>]*>\s*</script>\s*','',text)
    if '</head>' not in text:raise ValueError('HTML document has no head')
    return text.replace('</head>',ASSETS+'</head>',1)
def install_theme(path):
    path=Path(path);old=path.read_text();new=attach_theme(old)
    if old!=new:
        pending=path.with_name(path.name+'.theme-pending');pending.write_text(new);pending.replace(path)
