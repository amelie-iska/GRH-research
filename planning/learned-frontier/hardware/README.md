# Hardware research: evidence and executable contracts

Private local research, retrieved 2026-11-04 UTC. This survey connects circuit
design automation, superconducting-device geometry, classical control of quantum
experiments, and tropical/hybrid arithmetic. It does not infer a GRH result,
quantum advantage, general training speedup, or fabricated chip from a software
example.

- [Source-based review](REVIEW.md): what the tools actually do and what is missing.
- [Architecture candidates and evaluation campaign](ARCHITECTURES.md): five
  candidates, three executable integer references, and measured-evidence gates.
- [Pinned repositories](REPOSITORIES.md): twenty verified public repositories,
  including two direct tropical sources and a repository-move negative result.
- [Repository manifest](sources-2026-11-04.json): exact Git commit, retrieval time,
  public API license classification, immutable URLs, document SHA256 and exact
  line ranges reviewed. A metadata license classification is not a complete
  dependency, PDK, patent, or commercial-tool license review.
- [Paper manifest](papers-2026-11-04.json): primary paper abstract/metadata audit,
  with retrieval timestamps and response hashes; no claim of full-paper audit.
- [Paper reading ledger](PAPERS.md): versioned sources, relevance and retrieval
  limitations, including an inaccessible AlphaChip publisher page.
- [Runnable references](../../../examples/learned_frontier/hardware/README.md)
  and [saved evidence](../../../examples/learned_frontier/hardware/evidence-2026-11-04.json).

Only public read-only HTTPS was used. No account, credential, MCP server,
installation, environment change, remote compute, device connection, publishing,
or Git mutation was required. Source snapshots are represented by immutable
URLs and hashes; large upstream trees and copied README texts are not vendored.
The existing research, datasets, checkpoints and environments remain intact.

The exact public identity of `baremetalQiskit` is **unresolved**. Public GitHub
repository search returned zero matches for that spelling at the recorded time.
That is not evidence that a private, differently spelled or unindexed project
does not exist. The conditional extension contract in ARCHITECTURES.md avoids
assigning it invented APIs or a fabricated commit.

Offline integrity check (no upstream downloads):

```sh
python3 -B planning/learned-frontier/hardware/check_research_manifest.py
```
