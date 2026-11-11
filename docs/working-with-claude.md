# Working with Claude on BDPL LabTools

For Sally, Annie, and anyone who joins later: how the AI assistant works
in this project, what it never does, how to steer it, and the lessons it
has learned here that would otherwise stay on one machine. It lives in the
hub and applies in every LabTools repository.

Three points are marked **[DECISION n]** with Michael's options and a
recommendation. They are open until he settles them in review of the pull
request that adds this document; the text is then rewritten to say what
was decided, with the date.

---

## 1. What Claude is here

Claude is a collaborator who works through the same door as you do:
GitHub pull requests. It reads the repository, builds and tests changes,
drives the application, writes the record, and hands each piece of work to
a person as a pull request with its evidence. It is good at the long
careful parts — running a suite, validating a bag with an independent tool,
writing the PROGRESS entry — and it will tell you what it did not verify.

Four things Claude never does, however it is asked and however small the
case looks:

- **Merge** a pull request, or treat silence as approval.
- **Close** a pull request or an issue. Superseded work stays open and is
  named for a person to close.
- **Install** software on a machine (`brew`, `pip`, `pipx`, an installer).
  It writes the command; a person runs it.
- **Write to source media or to an archival object** — a disc, a captured
  image, a sealed bag. Anything that could is read-only or runs on a copy.

Michael merges every pull request (see §8 for how that changes as
collaborators join). Decisions about the collection — rights, access,
retention, identifiers, what counts as done — are a person's. Claude
proposes and then stops; that pause is deliberate.

## 2. Your first week

In this order; each item is a link in the hub.

1. **[`docs/how-this-project-works.md`](how-this-project-works.md)** — the
   five-minute overview.
2. **[`docs/collaborator-setup.md`](collaborator-setup.md)** — accounts,
   Cardinal Key, `gh`, git identity, security settings.
3. **[`CLAUDE.md`](../CLAUDE.md)** in any LabTools repository — the working rules. The
   block between the two marker lines is identical in every repository
   and changes only in the hub; the sections below it are that project's own.
4. **Install Claude Code** on your machine *(see **[DECISION 2]**)*. Open it
   in your clone of a LabTools repository; `CLAUDE.md` loads by itself.
   You do not need to tell Claude the rules.
5. **Your first session is an exercise** *(see **[DECISION 3]**)*: a real,
   small piece of work taken through the whole cycle — branch, pull
   request, review, merge — with Michael as reviewer.
6. **Your first review:** read one of Claude's pull requests with
   [`docs/reviewing-pull-requests.md`](reviewing-pull-requests.md) beside you. The PR body tells you what
   was verified by driving and what only by reading; look at the second list
   first.

## 3. How a session goes

- **One branch per piece of work**, from `main`, named `feat/…`, `fix/…`
  or `docs/…`. **A branch is declared** when a pull request exists for it
  (a draft is fine) and the PR body names the session that made it. A
  branch left without a PR is an orphan; in DA Capture,
  `tools/branch-ledger.py` lists them and draws the picture
  (`docs/branch-ledger/`). The hub has no ledger yet.
- **Pull requests are based on `main`, never on another PR's branch.**
  Stacked PRs merge into the wrong place; it has happened three times.
- **Done means four things**, and the PR body says which were skipped:
  the suite and linters green locally; every page of the app still loads
  clean; the exact artifact handed over was driven once (with a screenshot
  for anything browser-driven); and the record names what was *not*
  verified.
- **An offered PR is sealed.** Once Claude tells you a PR is ready, nothing
  more is pushed to its branch. New work gets a new PR.
- **Every PR runs the docs-steward** before it is offered, and its report
  sits in the PR body under "Docs steward". A PR without that section is
  not ready.
- **Bookkeeping** at the end of a working stretch: a PROGRESS section,
  the BACKLOG moves, WORKSTREAMS brought current, the ledger refreshed —
  one docs PR, by the `bookkeeper` agent from a brief. (The `bookkeeper`
  agent is DA Capture's; the hub carries only `docs-steward`, see
  [`.claude/agents/README.md`](../.claude/agents/README.md).)

## 4. What a Claude pull request looks like

When Claude hands you a PR, the message carries the direct link, the title,
and the CI state, and PRs are listed in the order to merge them. The body has:

- what changed and why, with the date and the incident that taught it;
- **Done means** — the four lines above, filled in;
- **Not verified** — stated plainly;
- **Docs steward** — what moved with the behavior;
- the line *"Further testing is optional — but if you plan to test, don't
  merge until you're done."*

If a PR is red, Claude says so; it does not hand you a red PR silently.
After you merge, Claude runs the **four-count check**: that the merge
happened, that it took the branch's real head, that CI on `main` passed for
that commit, and that one distinctive string from the diff is on `main`.

## 5. How to steer

- **Decide in words.** When Claude proposes an approach and stops, the next
  move is yours; "yes, build it" or "change X" is enough.
- **Name things as the screen shows them** — `MEDIA-MTXT_2026-004_CM001`,
  not "the Samplers disk" — and Claude will too.
- **Ask for text before a PR** when you want to read words first ("draft
  X" means text, not a PR).
- **Your words in the record are yours.** Claude paraphrases you in
  PROGRESS and PR bodies; a quotation is marked *(verbatim)*; personal,
  trust or security remarks never enter the record.
- **Expect to be told what you cannot see.** Long runs come with a
  progress line every 30 seconds and a live view in a Terminal tab; every
  window Claude opens comes with what it is, what to do, and when it
  closes.

## 6. Standing lessons

Each was learned here on a real object, with a date. They are the part of
Claude's memory that does not travel with the repository unless written
down — which is what this section is for.

| Lesson | Learned |
|---|---|
| **Never mount an archival image.** `hmount`, `hdiutil` read-write, anything that can write: inspect a scratch copy. Re-validate the bag after any tool has touched a package. | 2026-11-05: hfsutils rewrote 6 bytes of a sealed bag's image; caught by `bagit.py`, restored from the capture copy |
| **No HEIC in a package.** Convert photographs to JPEG before they ride in. | 2026-08-26 |
| **Check the record before asserting.** Registers, sessions, PROVENANCE and docs first; look for the existing artifact before building one. | 2026-09-02, three corrections in one morning |
| **Test the handed artifact itself** — the link, button, command or file — not just its machinery. | 2026-08-23 |
| **A half-check that reads as thorough is worse than none.** Seven merges ran red for hours because nobody looked at the checks. | 2026-08-08 |
| **Platform choices go in `docs/portability-log.md`** in the same change: the apps must run under other operating systems. | 2026-09-18 |
| **Image type and format vocabularies are verbatim** from the institution's template; when a value is missing (an Apple GCR disk), record the controlled value and put the fact in the register. | 2026-11-05 |
| **A resource-fork application is invisible to a data-fork extraction**; the scan and survey verdicts describe the extraction, and the register must say so. | 2026-11-05 |
| **Session rows and custody lines go with the object**, never with whatever the Capture page happens to name. | 2026-11-05, fixed #632 |
| **A flux capture is format-agnostic**: when the sector decode is grey, decode again from the streams with the right image type; no second read of the disk. | 2026-11-05 |

## 7. The record and the memory

Three layers hold what this project knows:

1. **The repository** — code, `CLAUDE.md`, `docs/`, `PROGRESS.md`,
   `BACKLOG.md`, the registers inside each accession. Everyone's Claude
   reads this. It is the record of authority.
2. **GitHub** — pull requests with their bodies, evidence (in DA Capture,
   screenshots on the `pr-evidence` branch), the rulesets.
3. **Claude's memory** — per machine, per person: a folder of short notes
   it keeps between sessions. Useful, not shared, not the record.

The rule: **if it matters to anyone else, it goes in layer 1.** A lesson
that is only in Claude's memory on Michael's Mac is not transferred. This
document, and the rules block in `CLAUDE.md`, are where layer 3 is turned
into layer 1.

## 8. Roles — [DECISION 1]

Today Michael is the only code owner and merges every PR, including his
own. The hub's "Protect main" ruleset has required zero approvals since
2026-11-04, because GitHub does not let an author approve their own pull
request and he is the only approver; the hub's `CLAUDE.md` ("Who merges")
records that the solo phase continues until a second code owner exists.

**Options:**

- **(a) Annie (`aeschweik`) becomes the second code owner** *(recommended:
  she already has Write on the hub and on DA Capture, read from GitHub
  2026-11-11)*. The ruleset goes back to one required approval, without
  the code-owner requirement; either of them can approve the other's PR;
  Claude's PRs need one of them. (Note: the hub's `CLAUDE.md` "Who merges"
  paragraph today says code-owner review and last-push approval are turned
  back on the day a second code owner is named; choosing (a) as written
  means rewriting that sentence too.)
- **(b) Sally (`SallyDeBauche`)** — has Write on the hub but not on DA
  Capture (read from GitHub 2026-11-11); Write there is an org owner's act.
- **(c) Nobody yet** — the solo phase continues; the ruleset stays at zero.

Whichever it is, the "Who merges" paragraph in each repository's
`CLAUDE.md` is rewritten to match the ruleset as it stands, with the date.

## 9. Where your Claude runs — [DECISION 2]

- **(a) On your own machine, with your own Claude Code** *(recommended)*:
  clone the repository, open Claude Code in it, the rules load. The
  LabKit's own setup (`SETUP-mac.md` in the DA Capture repository) applies
  only if you capture media.
- **(b) On the lab Mac, in turns**: one person at a time; the session is
  yours while you sit there; the branch ledger shows what the last person
  left.

Either way: **one writer per checkout.** Two sessions editing the same
clone step on each other; the app gives a session its own worktree when
asked.

## 10. The first collaborator task — [DECISION 3]

Recommended: **the 21 undeclared branches** in DA Capture (counted
2026-11-09). The ledger there (`docs/branch-ledger/ledger.md`) names every
branch with commits not on `main` and no pull request. For each: *keep* (say why, in a line), *revive*
(open the PR), or *delete*. It is reading plus decisions, it teaches the PR
cycle end to end, and it ends with a visible result in the picture. Claude
drafts the list with a line of context per branch; the decisions are the
collaborator's, reviewed by Michael; the deletions are run by a person.

---

## Appendix — additions proposed for the shared rules block

To go into the hub's `CLAUDE.md` between the markers, then to every
repository by `tools/sync-rules.py`:

1. Under rule 2 (*never write to source media*): **"nor to a captured image
   or a sealed bag: anything that inspects an archival file does so on a
   scratch copy, and the bag is validated again after any tool has touched
   a package."**
2. Under rule 7 (git workflow): **"Live branches are declared: a pull
   request exists before the session that made the branch ends, the PR
   body names its session, and every PR is based on `main`. The branch
   ledger runs at every bookkeeping."** (DA Capture has this since #633;
   the shared wording is shorter.)
3. Under rule 8: **"Photographs enter a package as JPEG, never HEIC."**
4. A new line in *Who merges*, per **[DECISION 1]**.
