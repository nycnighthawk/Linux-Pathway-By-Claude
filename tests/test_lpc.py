"""Unit tests for parsers, tagging and the licence gate. Run: PYTHONPATH=tools pytest -q"""
from pathlib import Path

from lpc import extract
from lpc.tag import Tagger, _literal


def _parse(tmp_path: Path, name: str, text: str):
    p = tmp_path / name
    p.write_text(text)
    return extract.parse_file(p, name)


def test_markdown_front_matter_hugo_and_anchors(tmp_path):
    doc = _parse(tmp_path, "np.md", '---\ntitle: Network Policies\n---\nIntro {{< glossary_tooltip text="Pod" term_id="pod" >}} <!-- c -->\n'
                 "## Default deny {#default-deny}\nbody\n```\n# not a heading\n```\n#### deep stays inline\n")
    assert doc["title"] == "Network Policies"
    heads = [s["heading"] for s in doc["sections"]]
    assert heads == ["Network Policies", "Default deny"]
    assert doc["sections"][1]["anchor"] == "default-deny"
    assert "# not a heading" in doc["sections"][1]["text"] and "deep stays inline" in doc["sections"][1]["text"]
    assert "Pod" in doc["sections"][0]["text"] and "<!--" not in doc["sections"][0]["text"]


def test_markdown_link_headings_are_cleaned(tmp_path):
    doc = _parse(tmp_path, "g.md", "# Guide\n## [Chapter 1. Start](#start) {#start .title}\ntext\n")
    assert doc["sections"][1]["heading"] == "Chapter 1. Start"


def test_rst_levels(tmp_path):
    doc = _parse(tmp_path, "a.rst", "=====\nTitle\n=====\n\nIntro\n\nSection\n-------\nText\n\nSub\n~~~\nMore\n")
    assert [(s["level"], s["heading"]) for s in doc["sections"]] == [(1, "Title"), (2, "Section"), (3, "Sub")]


def test_tex_sections_and_cleanup(tmp_path):
    doc = _parse(tmp_path, "k.tex", "\\section{Kernel modules}\n\\begin{frame}{Loading}\n\\begin{itemize}\\item \\code{insmod} loads\\end{itemize}\\end{frame}\n")
    assert doc["sections"][0]["heading"] == "Kernel modules"
    assert "insmod loads" in doc["sections"][0]["text"] and "\\code" not in doc["sections"][0]["text"]


def test_docbook_nesting(tmp_path):
    doc = _parse(tmp_path, "c.xml", '<chapter id="c1"><title>APT</title><para>intro</para>'
                 '<section id="s1"><title>Sources</title><para>sources.list</para></section></chapter>')
    assert [(s["level"], s["heading"], s["anchor"]) for s in doc["sections"]] == [(1, "APT", "c1"), (2, "Sources", "s1")]


def test_cac_rule(tmp_path):
    d = tmp_path / "sshd_disable_root_login"
    d.mkdir()
    (d / "rule.yml").write_text("title: Disable SSH Root Login\ndescription: |-\n  Set {{{ xccdf_value('x') }}} PermitRootLogin no\n"
                                "severity: medium\nreferences:\n  nist: AC-6(2)\n  stigid@rhel9: RHEL-09-255045\n")
    doc = extract.parse_file(d / "rule.yml", "sshd_disable_root_login/rule.yml")
    assert doc["title"] == "Disable SSH Root Login"
    assert "RHEL-09-255045" in doc["sections"][0]["text"]


def test_literal_prefilter():
    assert _literal(r"\broutes?\b") == "route"
    assert _literal(r"\bgolang\b|\bgo\b") is None


def test_tagger_assigns_expected_courses():
    t = Tagger()
    sel = t.tag({"id": "x", "source": "rhel-10-docs", "path": "using_selinux.md", "title": "Using SELinux",
                 "section": "Managing SELinux booleans"}, "Use setsebool and semanage to change SELinux booleans. " * 3)
    assert sel["courses"][0]["code"] == "LNX-204"
    k8s = t.tag({"id": "y", "source": "kubernetes-docs", "path": "content/en/docs/tasks/administer-cluster/configure-upgrade-etcd.md",
                 "title": "Operating etcd clusters for Kubernetes", "section": "Backing up an etcd cluster"}, "etcdctl snapshot save")
    assert k8s["courses"][0]["code"] == "LNX-311" and "CN" in k8s["pathways"]


def test_gate_passes_on_repo():
    from lpc import gate
    assert gate.run() == 0


def test_robots_longest_match_and_empty_disallow():
    from lpc.crawl import Robots
    r = Robots("User-agent: *\nDisallow: /\nAllow: /en/stable\n")
    assert r.can_fetch("https://x/en/stable/a/") and not r.can_fetch("https://x/en/v1.0/")
    assert Robots("User-agent: *\nDisallow: # allow all\n").can_fetch("https://x/anything")
    assert not Robots("User-agent: *\nDisallow: *.license.html\n").can_fetch("https://x/a/b.license.html")
    assert not Robots(None, disallow_all=True).can_fetch("https://x/")


def test_crawl_clean_md_and_paths():
    from lpc.crawl import clean_md, _out_path
    md = "nav junk\n| table |\n\n# Title\n\n## [](#NAME)NAME [top](#top_of_page)\n\n\n\ntext"
    out = clean_md(md)
    assert out.startswith("# Title") and "top_of_page" not in out and "\n\n\n" not in out
    assert _out_path({}, "https://docs.docker.com/engine/network/") == "docs.docker.com/engine/network/index.md"
    assert _out_path({}, "https://man7.org/linux/man-pages/man2/epoll_wait.2.html") == "man7.org/linux/man-pages/man2/epoll_wait.2.md"


# ------------------------------------------------------------------ synthesis guardrails
import sqlite3

from lpc import synth

_SRC = ("The quick brown fox jumps over the lazy dog while seven sleepy cats watch from the warm "
        "kitchen window every single afternoon")
_GOOD = """---
id: T
---
## Define the problem
Foxes leap. Dogs nap. A cat observes all of it with mild interest from indoors.
## History and approaches
Agile animals have always outpaced idle ones.
## Current state
Our own wording throughout, with `inline code the quick brown fox jumps over the lazy dog` ignored.
## Related and opposing views
Some say dogs are merely resting.
## Future direction
More naps.
## References
- [src: demo 0123456789abcdef] Demo chunk
- [web: example.org] Another publisher <https://example.org>
"""


def _synth_db():
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.execute("CREATE TABLE chunks (id TEXT PRIMARY KEY, source TEXT)")
    db.execute("CREATE VIRTUAL TABLE chunks_fts USING fts5(id UNINDEXED, body)")
    db.execute("INSERT INTO chunks VALUES ('0123456789abcdef', 'demo')")
    db.execute("INSERT INTO chunks_fts VALUES ('0123456789abcdef', ?)", [_SRC])
    return db


def test_synth_check_passes_original_text(tmp_path):
    p = tmp_path / "ok.md"
    p.write_text(_GOOD)
    assert synth.check_file(p, _synth_db()) == []


def test_synth_check_flags_copied_run_quotes_sources_and_order(tmp_path):
    bad = (_GOOD.replace("Foxes leap.", "Indeed the quick brown fox jumps over the lazy dog while seven cats.")
                .replace("More naps.", 'He said "never a half written object in sight here".')
                .replace("- [web: example.org] Another publisher <https://example.org>\n", "")
                .replace("## Future direction\n", "").replace("## References", "## Future direction\n## References"))
    bad = bad.replace("## Related and opposing views", "## Tmp").replace("## Current state", "## Related and opposing views") \
             .replace("## Tmp", "## Current state")
    p = tmp_path / "bad.md"
    p.write_text(bad)
    errs = " | ".join(synth.check_file(p, _synth_db()))
    assert "8-word run also appears in demo" in errs
    assert "quoted passage" in errs
    assert "at least 2 independent sources" in errs
    assert "sections must be" in errs
    assert "5-grams shared" in errs


def test_pathways_and_topics_follow_the_taxonomy():
    from lpc.common import load_taxonomy
    from lpc.tag import ALL_PATHS
    tax = load_taxonomy()
    assert ALL_PATHS == list(tax["pathways"]) and "VIRT" in ALL_PATHS
    for code, c in tax["courses"].items():
        assert set(c["pathways"]) <= set(ALL_PATHS) | {"TRUNK"}, code
    courses = {t["course"] for t in synth.topics().values()}
    assert courses == set(tax["courses"]), courses ^ set(tax["courses"])


def test_build_plan_markdown_matches_playbook_block():
    import json, re
    root = Path(__file__).resolve().parents[1]
    html = (root / "web" / "playbook.html").read_text()
    block = re.search(r'id="build-plan">(.*?)</script>', html, re.S).group(1).replace("<\\/", "</")
    plan = json.loads(block)
    md = (root / "docs" / "BUILD-PLAN.md").read_text()
    ids = re.findall(r"^\| \d+ \| `([^`]+)` \|", md, re.M)
    assert ids == [i["id"] for i in plan["items"]], "run python3 tools/export_plan.py"
    assert plan["max_threads"] == 3 and len(plan["instructions"]) < 16000
    for i in plan["items"]:
        assert all(d in ids for d in i["deps"]), i["id"]
