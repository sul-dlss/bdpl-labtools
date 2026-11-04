#!/usr/bin/env python3
"""Carry the hub's shared-rules block to every application repository.

The shared working rules live in this repository's CLAUDE.md between two
marker lines:

    <!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN ... -->
    <!-- BDPL-LABTOOLS-SHARED-RULES:END -->

Every `bdpl-labtools-<app>` repository carries the same block between the
same markers. This script compares each one with the hub's and, with
`--apply`, opens ONE pull request per repository whose block differs. It
never merges, never closes, never pushes to `main`: every change arrives as
a PR that Michael merges, so each repository's record shows the rule
arriving.

Usage, from a checkout of the hub on `main`:

    python3 tools/sync-rules.py            # report only
    python3 tools/sync-rules.py --apply    # open the PRs
    python3 tools/sync-rules.py --repo sul-dlss/bdpl-labtools-dedupe

Repositories come from the catalog table in tools/README.md (the links of
the form https://github.com/sul-dlss/bdpl-labtools-<app>), or from --repo.
Standard library plus the `gh` command-line tool; nothing to install.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path

HUB = "sul-dlss/bdpl-labtools"
BEGIN = "<!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN"
END = "<!-- BDPL-LABTOOLS-SHARED-RULES:END"
CATALOG_LINK = re.compile(r"https://github\.com/(sul-dlss/bdpl-labtools-[a-z0-9-]+)")

ROOT = Path(__file__).resolve().parent.parent


def gh(*args: str, input: str | None = None) -> str:
    """Run `gh` and return stdout; raise with stderr on failure."""
    proc = subprocess.run(
        ["gh", *args], capture_output=True, text=True, input=input
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed:\n{proc.stderr.strip()}")
    return proc.stdout


def extract_block(text: str, where: str) -> str:
    """Return the shared block, markers included, or '' when a marker is missing.

    The block runs from the start of the BEGIN marker's line to the end of
    the END marker's line, newline included, so a sync replaces exactly the
    lines between (and including) the markers and nothing around them.
    """
    begin = text.find(BEGIN)
    end = text.find(END)
    if begin < 0 or end < 0:
        return ""
    if end < begin:
        raise RuntimeError(f"{where}: END marker comes before BEGIN marker")
    end_eol = text.find("\n", end)
    end_eol = len(text) if end_eol < 0 else end_eol + 1
    return text[begin:end_eol]


def catalog_repos(catalog: Path) -> list[str]:
    seen: list[str] = []
    for repo in CATALOG_LINK.findall(catalog.read_text(encoding="utf-8")):
        if repo not in seen:
            seen.append(repo)
    return seen


def fetch_claude_md(repo: str) -> tuple[str, str]:
    """Return (text, blob sha) of the repo's CLAUDE.md on its default branch."""
    raw = gh("api", f"repos/{repo}/contents/CLAUDE.md")
    data = json.loads(raw)
    text = base64.b64decode(data["content"]).decode("utf-8")
    return text, data["sha"]


def default_branch(repo: str) -> str:
    return gh("repo", "view", repo, "--json", "defaultBranchRef",
              "--jq", ".defaultBranchRef.name").strip()


def existing_sync_pr(repo: str, branch: str) -> str:
    out = gh("pr", "list", "--repo", repo, "--head", branch, "--state", "open",
             "--json", "url", "--jq", ".[0].url // empty")
    return out.strip()


def open_sync_pr(repo: str, new_text: str, file_sha: str, hub_sha: str,
                 branch: str, summary: str) -> str:
    base = default_branch(repo)
    base_sha = gh("api", f"repos/{repo}/git/ref/heads/{base}",
                  "--jq", ".object.sha").strip()
    gh("api", f"repos/{repo}/git/refs", "--method", "POST",
       "-f", f"ref=refs/heads/{branch}", "-f", f"sha={base_sha}")
    message = (
        f"rules: carry the shared rules block from the hub at {hub_sha[:12]}\n\n"
        f"Source: https://github.com/{HUB}/blob/{hub_sha}/CLAUDE.md\n"
        "Opened by tools/sync-rules.py in the hub; everything outside the\n"
        "markers is untouched.\n"
    )
    payload = json.dumps({
        "message": message,
        "content": base64.b64encode(new_text.encode("utf-8")).decode("ascii"),
        "sha": file_sha,
        "branch": branch,
    })
    gh("api", f"repos/{repo}/contents/CLAUDE.md", "--method", "PUT",
       "--input", "-", input=payload)
    body = (
        "The hub's shared rules changed; this PR carries the new block into this\n"
        "repository's CLAUDE.md. Nothing outside the two marker lines is touched.\n\n"
        f"- Source: https://github.com/{HUB}/blob/{hub_sha}/CLAUDE.md "
        f"(hub `main` at `{hub_sha[:12]}`)\n"
        f"- Opened by `tools/sync-rules.py` in the hub.\n\n"
        "## What changed in the block\n\n"
        f"{summary}\n\n"
        "## Docs steward\n\n"
        "The block is the document; the sync carries it verbatim. The app's own\n"
        "sections below the END marker are untouched. The 'Rules drift' check\n"
        "on this PR compares the branch with the hub and should be green.\n\n"
        "Merging is Michael's act. This script never merges and never closes.\n"
    )
    url = gh("pr", "create", "--repo", repo, "--base", base, "--head", branch,
             "--title", f"rules: sync shared rules from the hub ({hub_sha[:7]})",
             "--body", body)
    return url.strip()


def diff_summary(old: str, new: str) -> str:
    import difflib
    lines = list(difflib.unified_diff(
        old.splitlines(), new.splitlines(), "app (before)", "hub (after)",
        lineterm="", n=1))
    if not lines:
        return "(no textual difference)"
    body = "\n".join(lines[2:])  # drop the ---/+++ header
    if len(body) > 6000:
        body = body[:6000] + "\n… (truncated)"
    return "```diff\n" + body + "\n```"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true",
                    help="open a PR per drifted repository (default: report only)")
    ap.add_argument("--repo", action="append", default=[],
                    help="repository to check (repeatable); default: the catalog")
    ap.add_argument("--hub-file", default=str(ROOT / "CLAUDE.md"),
                    help="hub CLAUDE.md to read the block from")
    ap.add_argument("--catalog", default=str(ROOT / "tools" / "README.md"))
    args = ap.parse_args(argv)

    hub_text = Path(args.hub_file).read_text(encoding="utf-8")
    hub_block = extract_block(hub_text, "hub CLAUDE.md")
    if not hub_block:
        print("hub CLAUDE.md has no shared-rules markers; nothing to sync",
              file=sys.stderr)
        return 2

    hub_sha = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        capture_output=True, text=True).stdout.strip() or "worktree"
    dirty = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain", "CLAUDE.md"],
        capture_output=True, text=True).stdout.strip()
    if args.apply and dirty:
        print("hub CLAUDE.md has uncommitted changes; commit and merge them "
              "first, then sync from main", file=sys.stderr)
        return 2

    repos = args.repo or catalog_repos(Path(args.catalog))
    if not repos:
        print("no repositories found in the catalog", file=sys.stderr)
        return 2

    branch = f"rules/sync-{hub_sha[:7]}"
    drifted = 0
    for repo in repos:
        try:
            text, file_sha = fetch_claude_md(repo)
        except RuntimeError as exc:
            print(f"{repo}: cannot read CLAUDE.md — {exc.splitlines()[-1]}")
            continue
        block = extract_block(text, repo)
        if not block:
            print(f"{repo}: NOT ENROLLED — CLAUDE.md has no shared-rules markers; "
                  "add them by hand once (see docs/rules-propagation.md)")
            continue
        if block == hub_block:
            print(f"{repo}: in sync")
            continue
        drifted += 1
        print(f"{repo}: DRIFTED")
        if not args.apply:
            continue
        url = existing_sync_pr(repo, branch)
        if url:
            print(f"    sync PR already open: {url}")
            continue
        new_text = text.replace(block, hub_block, 1)
        url = open_sync_pr(repo, new_text, file_sha, hub_sha, branch,
                           diff_summary(block, hub_block))
        print(f"    opened {url}")

    if drifted and not args.apply:
        print(f"\n{drifted} drifted; re-run with --apply to open the PRs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
