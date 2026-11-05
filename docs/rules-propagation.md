# How a rule reaches every repository

The working rules in `CLAUDE.md` are learned as we go. A rule learned in one
repository has to reach all of them, and a repository must not be able to
fall behind quietly. This document says how that works and what to do.

## The shape

- **One block.** In every repository's `CLAUDE.md`, the shared rules sit
  between two marker lines:

  ```
  <!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN ... -->
  ...
  <!-- BDPL-LABTOOLS-SHARED-RULES:END -->
  ```

  The block is byte-identical everywhere. Above it, each repository has its
  own introduction, "What this project is" and "Who merges" (the merge
  phase differs per repository). Below it, the repository's own section.
- **The hub is the source of truth.** `sul-dlss/bdpl-labtools/CLAUDE.md` is
  where a rule changes, always by pull request.
- **The sync opens pull requests.** `tools/sync-rules.py --apply`, run from
  a checkout of the hub on `main` after the rules PR has merged, reads the
  application repositories from the catalog (`tools/README.md`), compares
  each one's block with the hub's, and opens one PR per repository that
  differs, on a branch named `rules/sync-<hub commit>`. It never merges and
  never closes. Michael merges each PR, so each repository's history shows
  the rule arriving, with the hub commit it came from.
- **The drift check keeps it honest.** Each application repository runs the
  hub's reusable workflow `rules-drift.yml` on every PR and push to `main`.
  It fetches the hub's `CLAUDE.md` from the public raw URL and fails when
  the blocks differ. A drifted repository is red until its sync PR merges.
  The workflow's logic lives in the hub, so a change to the check also
  propagates by itself.

## Changing a rule

1. Branch in the hub, edit the block in `CLAUDE.md`, open the PR, Michael
   merges.
2. On `main` in the hub:

   ```bash
   python3 tools/sync-rules.py
   ```

   prints `in sync`, `DRIFTED` or `NOT ENROLLED` per repository. Then

   ```bash
   python3 tools/sync-rules.py --apply
   ```

   opens the PRs and prints their links. Hand the links to Michael in the
   order to merge them.
3. Michael merges each. The "Rules drift" check on each repository turns
   green with the merge.

Edits between the markers in an application repository are overwritten by
the next sync. If an app needs a rule the others don't, it goes below the
END marker, in the app's own section.

## Enrolling a repository (once, by hand)

A new repository made from the hub template already has the markers and the
caller workflow. An older repository is enrolled by one hand-made PR:

1. In its `CLAUDE.md`, replace the rules it copied from the hub with the
   hub's current block, markers included, verbatim. Move anything the
   repository added inside those rules to its own section below the END
   marker.
2. Add `.github/workflows/rules-drift.yml`:

   ```yaml
   name: Rules drift
   on:
     pull_request:
     push:
       branches: [main]
   permissions:
     contents: read
   jobs:
     drift:
       uses: sul-dlss/bdpl-labtools/.github/workflows/rules-drift.yml@main
   ```

3. Open the PR; its own "Rules drift" check proves the enrollment.

## What the sync does not do

- It does not touch anything outside the markers.
- It does not merge, close, or push to `main`.
- It does not run on a schedule; a person runs it after a rules change.
- It does not reach repositories that are not in the catalog; `--repo` names
  one explicitly.
