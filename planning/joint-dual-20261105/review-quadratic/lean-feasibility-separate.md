# Separate Lean feasibility evidence

2026-11-05, Linux via ssh iska-linux-vscode; no installation was authorized or performed by this reviewer.

* Project pin: leanprover/lean4:v4.24.0. Both verification scripts explicitly select .tools/lean-4.24.0-darwin_aarch64/bin.
* uname -s -m: Linux x86_64.
* file .tools/lean-4.24.0-darwin_aarch64/bin/lean: Mach-O 64-bit arm64 executable.
* Direct .tools/lean-4.24.0-darwin_aarch64/bin/lean --version: cannot execute binary file: Exec format error; exit 126.
* ~/.elan/toolchains contained only leanprover--lean4---v4.30.0-rc2 and leanprover--lean4---v4.29.lock. The former binary is ELF x86-64, a different version that was not substituted.
* PATH lean is /home/iska/.local/bin/lean -> /home/iska/.elan/bin/lean. The elan shim was not invoked.
* Pinned mathlib 4.24 source and olean cache existed; neither supplies the missing compatible compiler.
* No downloads, upgrades, authentication, installation, or Lean production edits were performed. No proposed analytic theorem was passed off as compiled.
* Protected HEAD remained dba37ffaa78c82ade1385f7ee56c907ab0c67d3a; index SHA256 remained 0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c.
