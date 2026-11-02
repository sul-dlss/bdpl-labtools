# Contributing

This repository is the hub for the BDPL LabTools family. Each application
has its own repository (see [tools/README.md](tools/README.md)); the
conventions below apply to all of them.

## The one rule that governs everything

**Nothing reaches `main` except through a pull request.** No one pushes
directly to `main`, and GitHub enforces this for everyone, admins
included. Once collaborators join, an approving review from a code
owner will be required as well.

## Workflow

1. Create a branch from `main` with a short, descriptive name
   (for example `catalog/add-dedupe`).
2. Make your change and commit it. Keep each pull request to one topic.
3. Open a pull request. CI runs lint and security checks; a red check
   means the PR is not ready.
4. Once a pull request has been offered for review, do not push more
   commits to it. New work gets a new pull request. If something must be
   added, say so in the PR before pushing.
5. After merging, confirm the merge commit's CI run on `main` is green.

## Never commit

Imaging outputs and collection data: `*.dd`, `*.E01`, `*.iso`, imaging
logs, or anything derived from an accession. Secrets of any kind;
push protection will reject them, but do not rely on it.

## License

By contributing you agree your work is released under the Apache-2.0
license in [LICENSE](LICENSE).
