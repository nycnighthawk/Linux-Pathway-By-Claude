"""Export the build plan from web/playbook.html.

The playbook computes every prompt in the browser. This script renders it headless (Playwright + Chromium),
then writes the same plan two ways so agents can read it without running JavaScript:
  * a JSON block <script type="application/json" id="build-plan"> inside web/playbook.html
  * docs/BUILD-PLAN.md (the canonical copy that project threads read from the repo)

Usage: python3 tools/export_plan.py      (run after editing web/playbook.html)
"""
import json
import pathlib
import re

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = ROOT / "web" / "playbook.html"
MD = ROOT / "docs" / "BUILD-PLAN.md"

JS = """() => ({
  version: 1,
  max_threads: MAX,
  start: P.start(),
  instructions: P.instructions(),
  items: ITEMS.map(i => ({id: i.id, label: i.label, kind: i.kind, course: i.course || null,
                          deps: i.deps, prompt: promptFor(i)})),
  steering: STEER.map(([title, desc, f]) => ({title, desc, prompt: f()}))
})"""


def render():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.goto(HTML.as_uri())
        plan = pg.evaluate(JS)
        b.close()
    if errors:
        raise SystemExit(f"playbook has script errors: {errors}")
    return plan


def to_md(plan):
    out = ["# Build plan", "",
           "Generated from web/playbook.html by tools/export_plan.py. Do not edit by hand.", "",
           f"At most {plan['max_threads']} worker threads. Each work item is one thread and one PR "
           "(capstones: two PRs), started with its prompt verbatim once every dependency is merged.", "",
           "## Start prompt", "", "Paste into the project conversation.", "", "```text", plan["start"], "```", "",
           "## Project instructions", "", "```text", plan["instructions"], "```", "",
           "## Work items", "", "| # | Id | Work item | Waits for |", "|---:|---|---|---|"]
    for n, i in enumerate(plan["items"], 1):
        deps = "all other items" if i["id"] == "R" else (", ".join(i["deps"]) or "—")
        out.append(f"| {n} | `{i['id']}` | {i['label']} | {deps} |")
    out.append("")
    for i in plan["items"]:
        out += [f"### {i['id']} · {i['label']}", "", "```text", i["prompt"], "```", ""]
    out += ["## Steering", ""]
    for s in plan["steering"]:
        out += [f"### {s['title']}", "", s["desc"], "", "```text", s["prompt"], "```", ""]
    return "\n".join(out)


def main():
    plan = render()
    html = HTML.read_text()
    block = json.dumps(plan, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html, n = re.subn(r'(<script type="application/json" id="build-plan">).*?(</script>)',
                      lambda m: m.group(1) + block + m.group(2), html, flags=re.S)
    assert n == 1, "build-plan block missing from playbook.html"
    HTML.write_text(html)
    MD.write_text(to_md(plan))
    print(f"exported {len(plan['items'])} work items to {MD.relative_to(ROOT)} and the playbook's build-plan block")


if __name__ == "__main__":
    main()
