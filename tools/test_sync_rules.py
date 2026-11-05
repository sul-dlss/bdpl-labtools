"""Tests for tools/sync-rules.py: the block extraction and the apply path.

Run from the hub root:  python3 -m unittest tools/test_sync_rules.py

The `gh` calls are replaced by a recorder, so the apply path is exercised
without opening a real pull request. The first live run is recorded in the
PR that enrolls the first application repository.
"""

import base64
import importlib.util
import json
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sync_rules", HERE / "sync-rules.py")
sync_rules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_rules)

HUB_BLOCK = (
    "<!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN — source: hub -->\n"
    "\n## Working rules\n\n1. New rule.\n\n"
    "<!-- BDPL-LABTOOLS-SHARED-RULES:END -->\n"
)
HUB_TEXT = "# Hub intro\n\n## Who merges\n\nhub phase\n\n" + HUB_BLOCK + "\n## Hub-specific\n"
APP_TEXT = (
    "# App intro\n\n## Who merges\n\napp phase\n\n"
    "<!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN — source: hub -->\n"
    "\n## Working rules\n\n1. Old rule.\n\n"
    "<!-- BDPL-LABTOOLS-SHARED-RULES:END -->\n"
    "\n## App-specific\n\n- keep me\n"
)


class ExtractBlock(unittest.TestCase):
    def test_block_runs_from_begin_line_to_end_of_end_line(self):
        self.assertEqual(sync_rules.extract_block(HUB_TEXT, "hub"), HUB_BLOCK)

    def test_missing_marker_is_not_enrolled(self):
        self.assertEqual(sync_rules.extract_block("# nothing here\n", "x"), "")

    def test_reversed_markers_raise(self):
        with self.assertRaises(RuntimeError):
            sync_rules.extract_block(
                "<!-- BDPL-LABTOOLS-SHARED-RULES:END -->\n"
                "<!-- BDPL-LABTOOLS-SHARED-RULES:BEGIN -->\n", "x")

    def test_catalog_links_are_the_repo_list(self):
        catalog = HERE / "README.md"
        repos = sync_rules.catalog_repos(catalog)
        self.assertIn("sul-dlss/bdpl-labtools-dedupe", repos)
        self.assertIn("sul-dlss/bdpl-labtools-da-capture", repos)
        self.assertEqual(len(repos), len(set(repos)))

    def test_hub_claude_md_has_exactly_one_block(self):
        text = (HERE.parent / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertEqual(text.count(sync_rules.BEGIN), 1)
        self.assertEqual(text.count(sync_rules.END), 1)
        self.assertTrue(sync_rules.extract_block(text, "hub"))


class ApplyPath(unittest.TestCase):
    """Drive main(--apply) against a fake gh and check what it would do."""

    def fake_gh(self, calls):
        def _gh(*args, input=None):
            calls.append((args, input))
            if args[:2] == ("api", "repos/sul-dlss/bdpl-labtools-x/contents/CLAUDE.md") and len(args) == 2:
                return json.dumps({
                    "content": base64.b64encode(APP_TEXT.encode()).decode(),
                    "sha": "filesha",
                })
            if args[0] == "repo" and args[1] == "view":
                return "main\n"
            if args[0] == "pr" and args[1] == "list":
                return ""
            if "git/ref/heads/main" in args[1]:
                return "basesha\n"
            if args[0] == "pr" and args[1] == "create":
                return "https://github.com/sul-dlss/bdpl-labtools-x/pull/1\n"
            return ""
        return _gh

    def run_main(self, tmp, argv):
        hub_file = tmp / "CLAUDE.md"
        hub_file.write_text(HUB_TEXT, encoding="utf-8")
        calls = []
        with mock.patch.object(sync_rules, "gh", self.fake_gh(calls)), \
             mock.patch.object(sync_rules.subprocess, "run") as run:
            def fake_git(cmd, **kw):  # rev-parse → a sha; status → clean
                out = "abcdef1234567890\n" if "rev-parse" in cmd else ""
                return mock.Mock(stdout=out, returncode=0)
            run.side_effect = fake_git
            rc = sync_rules.main(
                ["--hub-file", str(hub_file), "--repo", "sul-dlss/bdpl-labtools-x", *argv])
        return rc, calls

    def test_report_mode_opens_nothing(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            rc, calls = self.run_main(Path(d), [])
        self.assertEqual(rc, 0)
        self.assertFalse(any(c[0][0] == "pr" and c[0][1] == "create" for c in calls))
        self.assertFalse(any("--method" in c[0] for c in calls))

    def test_apply_replaces_only_the_block_and_opens_one_pr(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            rc, calls = self.run_main(Path(d), ["--apply"])
        self.assertEqual(rc, 0)
        puts = [c for c in calls if "PUT" in c[0]]
        self.assertEqual(len(puts), 1)
        payload = json.loads(puts[0][1])
        new_text = base64.b64decode(payload["content"]).decode()
        self.assertEqual(new_text, APP_TEXT.replace("Old rule", "New rule"))
        self.assertIn("## App-specific\n\n- keep me", new_text)
        self.assertEqual(payload["sha"], "filesha")
        self.assertEqual(payload["branch"], "rules/sync-abcdef1")
        creates = [c for c in calls if c[0][:2] == ("pr", "create")]
        self.assertEqual(len(creates), 1)
        # never a merge, never a close
        for args, _ in calls:
            self.assertNotIn("merge", args)
            self.assertNotIn("close", args)


if __name__ == "__main__":
    unittest.main()
