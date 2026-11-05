# Tool catalog

Each BDPL LabTools application lives in its own repository under the `sul-dlss` org,
named `bdpl-labtools-<app>` and tagged with the `bdpl-labtools` GitHub topic.
Browse them all at https://github.com/search?q=org%3Asul-dlss+topic%3Abdpl-labtools

| Tool | Repository | Purpose | Status |
|------|------------|---------|--------|
| Dedupe | [bdpl-labtools-dedupe](https://github.com/sul-dlss/bdpl-labtools-dedupe) | Find duplicate files within and across accessions | Scaffolding |
| DA Capture | [bdpl-labtools-da-capture](https://github.com/sul-dlss/bdpl-labtools-da-capture) | Media capture and ingest: imaging, read-only mount, ClamAV, Brunnhilde, BagIt; distributed to the bench as the BDPL LabKit | In production (private; transferred from mgolsonguildor/da-capture-macos 2026-11-01) |

## Adding a tool

1. Create `sul-dlss/bdpl-labtools-<app>` from this repository's template ("Use this template" on GitHub; the hub has been a template repository since 2026-11-03). In the new repo's first PR, delete what belongs only to the hub (`tools/README.md`, `docs/open-source-release.md`, `tools/sync-rules.py`) and rewrite `CLAUDE.md`'s introduction, "What this project is" and "Who merges" for the app — leaving the shared block between the markers untouched.
2. Add the `bdpl-labtools` and `digital-preservation` topics to the repo.
3. Add a row to the table above. The row's link is what `tools/sync-rules.py` reads, so the repository receives rule updates from this step on.
4. Add the "Rules drift" caller workflow (`docs/rules-propagation.md`, "Enrolling a repository").
