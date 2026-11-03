#!/usr/bin/env python3
"""Export numerical architecture traces into staging; promote after all checks.

Use the existing .tools/book-quantum-cpu/bin/python, not the system Python.
Writes only named architecture data. Does not train or change checkpoints.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import tempfile
import numpy as np
import scipy
from trace_schema import ROOT, source
import quantum_traces
import classical_traces


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"web/data/architecture")
    args=parser.parse_args()
    traces=list(quantum_traces.all_traces())+list(classical_traces.all_traces())
    # Validate/export all records before changing any live file.
    bodies={t["id"]:json.dumps(t,allow_nan=False,separators=(",",":"))+"\n" for t in traces}
    filenames={key:"records/"+key+"-"+hashlib.sha256(body.encode()).hexdigest()[:16]+".json" for key,body in bodies.items()}
    serialized={filenames[key]:body for key,body in bodies.items()}
    if len(serialized)!=len(traces):raise ValueError("Duplicate trace IDs")
    manifest=dict(schema_version=1,seed_classical=classical_traces.SEED,
        dependencies=dict(numpy=np.__version__,scipy=scipy.__version__),
        sources=[source(__file__),source(ROOT/"examples/architecture/trace_schema.py"),
                 source(ROOT/"examples/architecture/quantum_traces.py"),source(ROOT/"examples/architecture/classical_traces.py"),
                 source(ROOT/"examples/quantum/surface_models.py"),source(ROOT/"examples/quantum/requirements-cpu.lock")],
        traces=[dict(id=t["id"],title=t["title"],category=t["category"],kind=t["provenance"]["kind"],
                     file=filenames[t["id"]],sha256=hashlib.sha256(bodies[t["id"]].encode()).hexdigest(),
                     nodes=len(t["nodes"]),checks=len(t["checks"])) for t in traces],
        interface_status="Numerical trace layer complete; step-through architecture inspector is a separate queued task",
        unavailable="No GPU, upstream ToricGT checkpoint training, full infinite-order simulation, full-book Lean verification or GRH proof claimed")
    args.output.mkdir(parents=True,exist_ok=True)
    serialized["manifest.json"]=json.dumps(manifest,indent=2)+"\n"
    # Use same-directory temporaries for atomic per-file replacement; manifest last.
    for filename,body in serialized.items():
        target=args.output/filename
        target.parent.mkdir(parents=True,exist_ok=True)
        if filename != "manifest.json" and target.exists():
            if target.read_text()!=body:raise ValueError("Content-addressed record collision")
            continue
        with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",dir=target.parent,prefix=".staged-",suffix=".json",delete=False) as staged:
            staged.write(body)
            staged_name=staged.name
        os.replace(staged_name,target)
    print(json.dumps(dict(output=str(args.output),traces=len(traces),
        nodes=sum(len(t["nodes"]) for t in traces),checks=sum(len(t["checks"]) for t in traces)),indent=2))


if __name__=="__main__":main()
