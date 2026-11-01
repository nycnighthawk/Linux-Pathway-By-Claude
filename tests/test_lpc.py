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
