# Tool catalog

Each BDPL LabTools application lives in its own repository under the `sul-dlss` org,
named `bdpl-labtools-<app>` and tagged with the `bdpl-labtools` GitHub topic.
Browse them all at https://github.com/search?q=org%3Asul-dlss+topic%3Abdpl-labtools

| Tool | Repository | Purpose | Status |
|------|------------|---------|--------|
| Dedupe | [bdpl-labtools-dedupe](https://github.com/sul-dlss/bdpl-labtools-dedupe) | Find duplicate files within and across accessions | Scaffolding |
| DA Capture | [bdpl-labtools-da-capture](https://github.com/sul-dlss/bdpl-labtools-da-capture) | Media capture and ingest: imaging, read-only mount, ClamAV, Brunnhilde, BagIt; distributed to the bench as the BDPL LabKit | In production (private; transferred from mgolsonguildor/da-capture-macos 2026-11-01) |

## Adding a tool

1. Create `sul-dlss/bdpl-labtools-<app>` with the Apache-2.0 license and `.gitignore` from this repo.
2. Add the `bdpl-labtools` and `digital-preservation` topics to the repo.
3. Add a row to the table above.
