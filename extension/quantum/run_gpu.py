#!/usr/bin/env python3
"""Launch a recorded GPU experiment using only this Python environment's libraries.

Example:
  .venv-quantum/bin/python extension/quantum/run_gpu.py experiments --mode all
  .venv-quantum/bin/python extension/quantum/run_gpu.py capacity
"""
import os
from pathlib import Path
import site
import sys

if len(sys.argv) < 2 or sys.argv[1] not in {"experiments","capacity"}:
    raise SystemExit("Usage: run_gpu.py {experiments|capacity} [experiment arguments]")
libraries=[]
for package_dir in site.getsitepackages():
    root=Path(package_dir)
    for pattern in ("nvidia/*/lib","cuquantum/lib","cutensor/lib"):
        libraries.extend(str(p) for p in root.glob(pattern) if p.is_dir())
environment=os.environ.copy()
inherited=environment.get("LD_LIBRARY_PATH","")
environment["LD_LIBRARY_PATH"]=":".join(libraries+([inherited] if inherited else []))
filename={"experiments":"gpu_experiments.py","capacity":"gpu_capacity.py"}[sys.argv[1]]
script=Path(__file__).resolve().with_name(filename)
os.execvpe(sys.executable,[sys.executable,str(script),*sys.argv[2:]],environment)

