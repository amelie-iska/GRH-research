# Local Windows clone preparation

**Checkpoint:** 13 November 2026, before publication of the consolidated extension.

Remote Desktop Commander confirmed the authorized desktop hostname as **DESKTOP-784UBID**. A public filtered clone was created at:

```text
C:\Users\LIZ\Documents\GRH-research
```

The clone contains all 4,852 tracked paths from the preparation snapshot. The `blob:none` filter reduces transferred history; it does not make the checked-out working tree sparse. Repository-local `core.autocrlf=false` preserves source line endings for subsequent synchronization.

| Item | Observed value |
|---|---|
| Origin | `https://github.com/amelie-iska/GRH-research.git` |
| Branch | `main` |
| Preparation commit | `dbd954eede479a5129831e4e7c30537389ae973d` |
| Preparation tree | `69d00e6804881a931305804390f9b1701a8e97d1` |
| Working-tree changes | 0 |
| Preparation README SHA-256 | `93d66aad52e0ab05c3120aca090b90b6a8f869fb32364b3abad0ba0ebf1b04c9` |

The three inherited gitlinks (`GRH`, `Surface-Orders-Hilbert-Polya`, and `math`) retain their pinned revisions and were not recursively initialized during this preparation. This record does not claim that separate dependency repositories have been vendored.

RustDesk was already running. Its stored entry for the independently identified Iska peer describes hostname **iska**, platform **Linux**. SSH host declarations include `iska-linux`, `iska-linux-10`, and `iska-ms-7e70-1`; the exact alias `iska-linux-vscode` was not found in the inspected SSH configuration or VS Code settings. These identity checks do not establish that an interactive RustDesk session was connected. No access permissions, passwords, or authentication settings were changed.

The existing GitHub CLI session is valid but has only **READ** permission on this repository. It can fetch the published work but is not a publication route.

**Next checkpoint:** once the consolidated commit is published, check that the local working tree remains clean, fetch `origin/main`, apply only a fast-forward update, and compare its commit/tree hashes and selected artifact hashes with the published release. The older preparation commit above must not be reported as the completed synchronization result.
