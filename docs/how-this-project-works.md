# How this project works, in five minutes

For anyone joining BDPL LabTools: an archivist, a student, a colleague from
another unit, a reviewer. Read this first. Everything else is detail.

## What it is

BDPL LabTools is a set of applications that run on workstations in
Stanford Libraries' Born-Digital Preservation Lab and solve the lab's own
problems: capturing media with full provenance, finding duplicate files
across an accession, and whatever comes next. The applications are built by
the lab's digital archivists, with an AI assistant doing most of the typing,
under rules that keep every decision with a person.

There is one hub and one repository per application:

| Repository | What it is |
|---|---|
| **bdpl-labtools**, this one | the hub: the catalog of applications, the working rules, the guides |
| **bdpl-labtools-da-capture** | LabKit, the capture-and-ingest application already running in the lab |
| **bdpl-labtools-dedupe** | the deduplication tool, in design |

A repository is a folder with a memory: every change to it is recorded
with who, when and why, and nothing is ever lost. Think of it as the
accession register for the software.

## Who does what

| Role | Who | What they do |
|---|---|---|
| Archivists | Sally DeBauche, Annie Schweikert, Sabrina Gunn, and colleagues as they join | decide what the lab needs, direct the building, review every change, use the tools |
| Design lead | Michael Olson | built the framework, keeps the rules, owns the code, reviews what he did not write |
| AI assistant | Claude (Anthropic), in Claude Code sessions | writes code, tests and documents under direction; never decides, never approves, never merges |

The assistant reads the same rules you do. They are in every repository's
`CLAUDE.md`, and it follows them automatically each session.

## How a change happens

Every change, from fixing a typo to adding a tool, takes the same five
steps. This is the loop, and it is the whole method.

1. **Someone decides.** An archivist names a problem and what done looks
   like. "Find files that are duplicated across the drives in an accession
   and list them; never delete anything."
2. **Someone builds.** Usually the assistant, directed by the archivist,
   working in a branch: a private copy where nothing it does can affect the
   real thing. Sometimes the archivist edits a document directly.
3. **A pull request is opened.** That is the proposal: the change, a plain
   description of what it does, a note of what was not tested, and a
   report that the documents were kept current.
4. **A colleague reviews.** Someone other than the author reads the
   description, looks at the result, and clicks Approve or asks for
   changes. Nothing can be merged without this; GitHub enforces it for
   everyone, including the design lead and the assistant.
5. **It is merged.** The change becomes part of `main`, the published
   version, with its reasoning attached forever.

You never need the command line for steps 1, 4 or 5, and the assistant
handles step 2 and 3 when you ask it to.

## The rules that matter most

The full set is in `CLAUDE.md`. These seven are the ones to know on day one.

- **Nothing reaches `main` except through a reviewed pull request.** No
  exceptions, for anyone.
- **Tools never modify source media.** They read and report. A person takes
  any action on a collection, deliberately and with a record.
- **The description carries the change.** A pull request must be
  understandable from its summary alone. If it is not, send it back.
- **Say what was not verified.** Every pull request names what was proven
  by trying and what only by reading.
- **Ask before anything irreversible.** Deleting, rewriting history,
  changing settings: the assistant stops and asks a person.
- **Documents move with the code.** Every pull request runs a documentation
  check so the guides never fall behind.
- **Every commit names its co-author.** AI assistance is recorded as
  provenance; authorship and copyright stay with the University and its
  staff.

## Three ways to take part

You choose, per task, how much of the building you do yourself.

| | You | The assistant |
|---|---|---|
| **Hands-on** | write the change, learning as you go | explains, suggests, catches mistakes |
| **Directed** | describe the problem and what done looks like, then steer | writes it, tests it, opens the pull request |
| **Review-first** | write the requirement, then judge the result | builds the whole thing in a session you can leave |

Most work is directed. Reviewing, which everyone does, needs no code at
all.

## Where to go next

1. [Collaborator setup guide](collaborator-setup.md): accounts, access, the
   first sign-in.
2. [Reviewing a pull request](reviewing-pull-requests.md): the one skill the
   team needs first, in six steps.
3. [CLAUDE.md](../CLAUDE.md): the full working rules.
4. [Working with Claude](working-with-claude.md): what the assistant never
   does, how a session and a Claude pull request go, how to steer it.
5. [Tool catalog](../tools/README.md): what exists and what is planned.
6. The Dedupe repository's `docs/research/`: the research behind the first
   tool, if you want to see what the assistant produces and a person
   reviews.

If something here is unclear, that is a finding: open the file, click the
pencil, and propose a better sentence. That is a pull request, and someone
will review it.
