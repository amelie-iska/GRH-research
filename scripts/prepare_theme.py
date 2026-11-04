#!/usr/bin/env python3
"""Install the shared visual theme on current local HTML pages, idempotently."""
from pathlib import Path
from theme_assets import install_theme
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    paths=list((ROOT/'web').rglob('*.html'))
    for path in paths:install_theme(path)
    print('Shared local theme installed on',len(paths),'HTML documents')
