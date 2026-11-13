"""Export the build plan from web/playbook.html.

The playbook computes its prompts in the browser. This script renders it headless (Playwright + Chromium) and writes
the plan where agents read it without a browser:
  * web/playbook.html: the plain-text agent guide (<pre id="agent-guide">) and the JSON block (id="build-plan")
  * plan/build-plan.json: read by `bin/lpc plan`
  * docs/BUILD-PLAN.md: the same plan for people

Usage: python3 tools/export_plan.py      (run after editing web/playbook.html)
"""
import html as _html
import json
import pathlib
import re

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = ROOT / "web" / "playbook.html"
JSON = ROOT / "plan" / "build-plan.json"
MD = ROOT / "docs" / "BUILD-PLAN.md"


def render():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.goto(HTML.as_uri())
        plan = pg.evaluate("() => buildPlan()")
        b.close()
    if errors:
        raise SystemExit(f"playbook has script errors: {errors}")
    return plan


def to_md(plan):
    fence = lambda s: ["```text", s, "```", ""]
    out = ["# Build plan", "", "Generated from web/playbook.html by tools/export_plan.py. Do not edit by hand.", "",
           "## Start", "", "Claude Code project: upload web/playbook.html to the Library and say:", "", *fence(plan["say"]["project"]),
           "Claude Code on your machine, in a clone of the repo:", "", *fence(plan["say"]["local"]),
           "## Agent guide", "", *fence(plan["agent_guide"]),
           "## Work items", "", "| # | Id | Work item | Phases | Waits for |", "|---:|---|---|---|---|"]
    for n, i in enumerate(plan["items"], 1):
        ph = ", ".join(f"{k} {len(v)}" if v else k for k, v in i["phases"].items())
        deps = "all other items" if i["id"] == "R" else (", ".join(i["deps"]) or "—")
        out.append(f"| {n} | `{i['id']}` | {i['label']} | {ph} | {deps} |")
    out.append("")
    for i in plan["items"]:
        out += [f"### {i['id']} · {i['label']}", "", *fence(i["prompt"])]
    out += ["## Steering", ""]
    for s in plan["steering"]:
        out += [f"### {s['title']}", "", s["desc"], "", *fence(s["prompt"])]
    return "\n".join(out)


def main():
    plan = render()
    page = HTML.read_text()
    block = json.dumps(plan, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page, n1 = re.subn(r'(<script type="application/json" id="build-plan">).*?(</script>)',
                       lambda m: m.group(1) + block + m.group(2), page, flags=re.S)
    page, n2 = re.subn(r'(<pre id="agent-guide">).*?(</pre>)',
                       lambda m: m.group(1) + _html.escape(plan["agent_guide"], quote=False) + m.group(2), page, flags=re.S)
    assert n1 == n2 == 1, "playbook.html lost its build-plan or agent-guide block"
    HTML.write_text(page)
    JSON.parent.mkdir(exist_ok=True)
    JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=1) + "\n")
    MD.write_text(to_md(plan))
    print(f"exported {len(plan['items'])} work items: plan/build-plan.json, docs/BUILD-PLAN.md, playbook blocks")


if __name__ == "__main__":
    main()
