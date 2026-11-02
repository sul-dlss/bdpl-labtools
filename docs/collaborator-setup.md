# Collaborator setup guide

How to get set up to work on BDPL LabTools, and how the repositories are
arranged and protected. Written for digital archivists who may be new to
GitHub; every terminal command is complete and ready to paste.

## 1. How the repositories are arranged

- **`sul-dlss/bdpl-labtools`** (this repo) is the hub. It holds the catalog
  of applications, the working rules (`CLAUDE.md`), the contributing guide,
  the security policy and the shared CI workflow. Nothing in it runs on the
  bench.
- **`sul-dlss/bdpl-labtools-<app>`** is one repository per application, for
  example `bdpl-labtools-dedupe`. Each is tagged with the GitHub topics
  `bdpl-labtools` and `digital-preservation`, so this search lists them all:
  <https://github.com/search?q=org%3Asul-dlss+topic%3Abdpl-labtools>
- The catalog table in [`tools/README.md`](../tools/README.md) is the index
  of applications. Add a row when you add an app.

All repositories live in the **sul-dlss** organization on **github.com**,
not on Stanford's GitHub Enterprise (github.stanford.edu). Keep the two
apart; they have separate accounts and sign-ins.

## 2. Accounts you need

| What | Why | Notes |
|------|-----|-------|
| A github.com account linked to your Stanford identity | Membership in the sul-dlss org | Many people keep a personal account too. Use the Stanford one for this work. |
| sul-dlss org membership | Write access to the repos | An org owner adds you. Ask Michael Olson (`mgolson-stanford`). |
| Cardinal Key (Stanford device certificate) | Stanford single sign-on may require it on this org | See section 3. |

**Signed-in check.** On a pull request page, the avatar next to
"Add a comment" is the account GitHub thinks you are. If the green merge box
is missing while checks are green, you are almost certainly signed in to a
personal account without org access. Click your avatar top right, then
**Switch account** or **Sign out**, and sign in with the Stanford account.

## 3. Cardinal Key

Cardinal Key is a certificate Stanford installs in your Mac's keychain. On
the Stanford Login page it replaces password plus Duo. The login page only
offers it when your browser presents the certificate, so if you see the
plain SUNet ID and password form, the certificate is missing or expired in
that browser.

1. In Chrome or Safari, open <https://cardinalkey.stanford.edu>.
2. Sign in with SUNet ID, password and Duo.
3. Follow the install step. It adds the certificate to your keychain.
4. Quit and reopen the browser, then return to the Stanford Login page.
   A certificate picker appears: choose your Cardinal Key and, when macOS
   asks, choose **Always Allow**.

Firefox keeps its own certificate store and does not see Cardinal Key.
Use Chrome or Safari for Stanford sign-ins.

## 4. Tools on your Mac

Git is already on every Mac (open Terminal from Applications → Utilities).
Install the GitHub command line tool with Homebrew:

```bash
brew install gh
```

Sign it in to github.com with your Stanford GitHub account. Choose
**HTTPS** and **Login with a web browser** when asked:

```bash
gh auth login --hostname github.com
```

Check which account is active:

```bash
gh auth status
```

If you also use a personal account with `gh`, switch between them with:

```bash
gh auth switch --user <github-username>
```

## 5. Get the code and set your identity

```bash
git clone https://github.com/sul-dlss/bdpl-labtools.git ~/projects/bdpl-labtools
```

Set a **repo-local** git identity so your commits are attributed to your
Stanford GitHub account even if your global git config points at a personal
one. Use GitHub's no-reply address, which you can read from
<https://github.com/settings/emails> (it looks like
`12345678+username@users.noreply.github.com`):

```bash
cd ~/projects/bdpl-labtools && git config user.name "Your Name" && git config user.email "12345678+username@users.noreply.github.com"
```

Repeat the clone and identity steps for each application repository you
work on.

## 6. The working rules

Read [`CLAUDE.md`](../CLAUDE.md) before your first change. It is the
binding set of working rules for people and for Claude alike, carried over
from the BDPL LabKit project with the reasons each rule exists. The short
version:

- Nothing reaches `main` except through a pull request. GitHub enforces
  this for everyone, admins included.
- Until collaborators are added, Michael merges every PR, including his
  own. After that, every PR needs his approving review.
- An offered PR is sealed: once it is declared ready, no more pushes to
  that branch. New work gets a new PR.
- A red CI check means the PR is not ready.
- Every PR offered for merge is presented with a direct link to its page.
- After a merge, verify it: the PR is merged, the merge took the branch's
  real head, CI on `main` is green for the merge commit, and one
  distinctive string from the diff is present on `main`.

## 7. Day-to-day workflow

1. Start from a fresh `main`:

```bash
cd ~/projects/bdpl-labtools && git switch main && git pull
```

2. Create a branch named for the work (`feat/…`, `fix/…`, `docs/…`):

```bash
git switch -c docs/my-change
```

3. Make the change and commit it with a descriptive message.
4. Push the branch and open a pull request:

```bash
git push -u origin docs/my-change
```

```bash
gh pr create --fill
```

5. Wait for CI (lint and security checks) to go green. Fix anything red.
6. Hand the PR to Michael with its link. He merges with **Squash and
   merge**; the branch is deleted automatically.

To merge from the terminal rather than the website (Michael only, for now):

```bash
gh pr merge <number> --squash --delete-branch
```

## 8. What protects the repositories

These settings are on for `bdpl-labtools` and are applied to every new
`bdpl-labtools-<app>` repo on creation. They mirror the BDPL LabKit
security posture and need no action from contributors; they are listed so
you know why something was refused.

- **Protect main ruleset.** Pull request required; force pushes and
  deletions blocked; linear history; all review threads resolved; squash or
  merge commit only. No bypass for anyone. Required approvals is 0 during
  the solo phase and becomes 1 the day the first collaborator is added.
- **Secret scanning with push protection.** A push containing something
  that looks like a key or password is rejected before it lands.
- **Dependabot alerts and security updates.** Vulnerable dependencies get
  an automatic PR.
- **Private vulnerability reporting.** Security → Report a vulnerability.
- **Read-only workflow tokens.** CI cannot push or approve PRs.
- **CI on every PR.** ruff, shellcheck, bandit and gitleaks. The gitleaks
  step runs the open-source binary directly because the gitleaks GitHub
  Action demands a paid license on organization repos.
- Wiki off; branches deleted on merge; "Update branch" offered on PRs.

## 9. Adding a new application repository

1. Scaffold it locally with the hub's `LICENSE` and `.gitignore`, a README
   that links back to the hub, a `CLAUDE.md` copied from the hub with an
   app-specific section added, and a first commit.
2. Create the repository in the org and push:

```bash
gh repo create sul-dlss/bdpl-labtools-<app> --public --description "BDPL LabTools: <what it does>" --source=. --remote=origin --push
```

3. Tag it:

```bash
gh repo edit sul-dlss/bdpl-labtools-<app> --add-topic bdpl-labtools --add-topic digital-preservation
```

4. Apply the security settings from section 8. The simplest way is to ask
   Claude in the hub repo to "apply the bdpl-labtools security baseline to
   sul-dlss/bdpl-labtools-<app>"; the settings are all reachable through
   `gh api`.
5. Add a row to [`tools/README.md`](../tools/README.md) via a PR.

## 10. Where things are

| Item | Location |
|------|----------|
| Hub repository | <https://github.com/sul-dlss/bdpl-labtools> |
| Working rules | [`CLAUDE.md`](../CLAUDE.md) |
| Contributing guide | [`CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Security policy | [`SECURITY.md`](../SECURITY.md) |
| Application catalog | [`tools/README.md`](../tools/README.md) |
| Ruleset and security settings | Repo → Settings → Rules → Rulesets, and Settings → Code security |
| Origin of the rules | BDPL LabKit (`da-capture-macos`), CLAUDE.md and the DLSS migration plan |
