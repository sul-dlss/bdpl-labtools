# Reviewing a pull request

For Sally, Annie, Sabrina and anyone who joins later. This is the one
skill the team needs first. You do not have to write code to do it; you
have to read carefully and say what you think.

## Why your review matters

Since 2026-11-01 nothing reaches `main` in a LabTools repository until a
collaborator other than the author has approved it. The AI assistant that
writes most of the code cannot approve or merge; Michael cannot approve his
own work. GitHub enforces this for everyone, administrators included. Your
approval is the human judgment the whole workflow is built around.

A review is not a test of your coding. It asks three questions: does this
change do what the summary says, does it do anything the summary does not
say, and would I be comfortable if it were live in the lab tomorrow.

## Before you start

- You need a GitHub account that is a member of the sul-dlss organization
  and has write access to the repository. If you see no **Review changes**
  button on a pull request, you are either signed in to the wrong account
  or not yet added; see the [setup guide](collaborator-setup.md), section 2.
- Sign in with your Stanford GitHub account, not a personal one. The avatar
  at the top right of GitHub tells you which you are in.

## The six steps

1. **Open the pull request.** From the repository, click **Pull requests**,
   then the one you were asked to review. Or follow the link you were sent.
2. **Read the Conversation tab first.** The author's Summary says what the
   change is for. The **Not verified** section says what was not tested; read
   it closely. The **Docs steward** section lists the documents the change
   touched and checked. If any of these is missing, ask for it before going
   further; a PR without them is not ready under our rules.
3. **Check the checks.** Near the bottom of the Conversation tab, a green
   check means the automated lint and security checks passed. Red means
   something failed; do not approve a red PR. Yellow means still running.
4. **Open Files changed.** This is the actual change, file by file. Green
   lines were added, red lines removed. Read every file. For documents, read
   the prose as a reader would. For code, read it as a procedure: what does
   it do, in what order, what happens if the input is wrong.
5. **Comment on anything you want to say.** Hover a line, click the blue
   plus sign, type, choose **Start a review**. Questions are as useful as
   objections: "What happens if the folder is empty?" is a review comment.
   Comments stay attached to the change forever, so they are also the
   record of why things are the way they are.
6. **Finish with Review changes**, the green button at the top right of
   Files changed. Pick one:
   - **Approve**: you read it, it does what it says, you would be happy for
     it to be live. The author can now merge.
   - **Request changes**: something must change before it can merge. Say
     what. The author fixes it and asks again.
   - **Comment**: you have remarks but are not blocking or approving. Use
     this when you are unsure and want a second reviewer.

That is the whole job. A small PR takes five minutes. A large one may take
thirty; if it would take longer, say so and ask for it to be split.

## What to look for

| Look at | Ask |
|---|---|
| Summary versus diff | Does the change do more, or less, than the summary claims? |
| Not verified | Is anything listed there something you would want tested before it runs on real media? |
| Anything that touches source media or collection data | Does it only read? Our rules forbid tools from modifying sources; a person takes any action on a collection. |
| Deletions, removals, "cleanup" | Is anything removed that something else still depends on? |
| New dependencies or tools | Is there a reason given for each? |
| Documents | Would a new archivist understand this? Is any claim stated as fact that is really a guess? |
| Dates and versions | Is every version claim dated? |

If you are not sure whether something matters, comment and ask. Nobody has
ever been wrong to ask on a review.

## After you approve

The author, usually Michael, merges. GitHub squashes the branch into one
commit on `main`, deletes the branch, and runs the checks once more on
`main`. Your approval is recorded on the pull request permanently, with
your name and the time.

## Asking for a change yourself

You do not have to wait for someone else to open a pull request. Three
ways, from least to most involved:

- **Fix a sentence in a document.** Open the file on GitHub, click the
  pencil icon, change the text, and follow the prompts. GitHub makes the
  branch and the pull request for you. Someone else then reviews it.
- **Ask the assistant to make a change.** In a Claude Code session on the
  repository, describe the problem and what done looks like, in plain
  words: *"Add a glossary of GitHub terms for archivists as
  docs/glossary.md and open a PR."* The assistant branches, writes, runs
  the docs steward, opens the PR and gives you the link. You review it, or
  ask a colleague to. The assistant follows the repository's `CLAUDE.md`
  automatically, so it will never merge, never push to `main`, and never
  touch anything outside the repository.
- **Write it yourself.** The [setup guide](collaborator-setup.md), section
  7, has the commands.

Whichever way, the review step is the same, and it is always a person.

## Things that are not your problem

- You cannot break `main` by reviewing. Approve and Request changes only
  affect the pull request.
- You cannot approve your own pull request; GitHub hides the option.
- If the checks are red or the branch has conflicts, that is the author's
  to fix, not yours. Say so and wait.
- If you are asked to review something you do not feel able to judge, say
  that; it is a useful review comment and the author can find another
  reader or explain further.

## For Sabrina and anyone not yet in the organization

You can read every public LabTools repository today without an account.
To review and approve you need two things, in this order: a GitHub account
(github.com, five minutes, use your Stanford email) and membership in the
sul-dlss organization, which an organization owner grants once you give
Michael your GitHub username. Membership also lets you be added to the
private LabKit repository, which outside collaborators cannot join.
