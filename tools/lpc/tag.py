"""Rule-based auto-tagging of chunks to courses, pathways and certifications.

Scoring per course (see taxonomy/courses.yaml):
  * document title match: 2 (strong keyword: 4), counted once per keyword
  * section heading path match: 3 (strong: 6), counted once per keyword
  * body matches: 1 per hit (strong: 2), at most 4 hits per keyword
  * plus the source prior, if any
Manual overrides in review/overrides.yaml win over automatic tags, except entries with
`only_if: [none, low]`, which apply only when the automatic confidence is in that list.
"""
from __future__ import annotations

import fnmatch
import re

import yaml

from .common import REVIEW, load_taxonomy

ALL_PATHS = list(load_taxonomy()["pathways"])  # TRUNK expands to every pathway


def _literal(pat: str):
    """Longest literal run (>=3 chars) that every match must contain, or None if unsure."""
    if "|" in re.sub(r"\([^)]*\)", "", pat):
        return None
    q = pat.replace("\\b", "")
    q = re.sub(r"\([^)]*\)[?*]?", "\0", q)
    q = re.sub(r"\[[^\]]*\][?*+]?", "\0", q)
    q = re.sub(r".[?*]", "\0", q)
    q = re.sub(r"\\.", "\0", q)
    runs = re.findall(r"[a-z0-9]{3,}", q.lower())
    return max(runs, key=len) if runs else None


class Tagger:
    def __init__(self):
        tx = load_taxonomy()
        self.courses = tx["courses"]
        self.priors = tx.get("source_priors", {})
        self.t = tx["thresholds"]
        # One regex per keyword, plus a required literal used as a cheap substring prefilter
        # (most keywords are absent from most chunks, so this skips most regex work).
        self.rules = {}
        for code, c in self.courses.items():
            rs = []
            for kw in c.get("keywords", []):
                strong = kw.startswith("!")
                pat = kw.lstrip("!")
                if not pat.startswith("\\b") and re.match(r"\w", pat):
                    pat = r"\b" + pat
                if not pat.endswith("\\b") and re.search(r"[\w?)]$", pat):
                    pat = pat + r"\b"
                rs.append((re.compile(pat, re.I), _literal(pat), 2 if strong else 1))
            self.rules[code] = rs
        ov = REVIEW / "overrides.yaml"
        self.overrides = (yaml.safe_load(ov.read_text()) or {}).get("overrides", []) if ov.exists() else []

    def score(self, source: str, title: str, heading_path: str, body: str) -> dict[str, float]:
        out = {}
        pri = self.priors.get(source, {})
        body = body[:60000]
        lt, lh, lb = title.lower(), (heading_path or "").lower(), body.lower()
        for code, rs in self.rules.items():
            s = float(pri.get(code, 0))
            for rx, lit, w in rs:
                if lit is None or lit in lt:
                    if rx.search(title):
                        s += 2 * w
                if lh and (lit is None or lit in lh):
                    if rx.search(heading_path):
                        s += 3 * w
                if lb and (lit is None or lit in lb):
                    n = 0
                    for _ in rx.finditer(body):
                        n += 1
                        if n == 4:
                            break
                    s += n * w
            if s:
                out[code] = s
        return out

    def tag(self, chunk: dict, body: str) -> dict:
        # The file path is extra title context: CAC rule dirs, doc folders and guide slugs are meaningful.
        path_ctx = re.sub(r"[/_.-]+", " ", re.sub(r"\.(md|rst|tex|xml|yml)$", "", chunk.get("path", "")))
        sc = self.score(chunk["source"], f"{chunk['title']} {path_ctx}", chunk["section"], body)
        ranked = sorted(sc.items(), key=lambda kv: -kv[1])
        top = ranked[0][1] if ranked else 0
        chosen = [(c, s) for c, s in ranked if s >= self.t["assign"] and s >= self.t["relative"] * top][: self.t["max_courses"]]
        conf = "none" if not chosen else ("high" if top >= self.t["high"] else "medium" if top >= self.t["medium"] else "low")
        if conf == "low" and self.priors.get(chunk["source"], {}).get(chosen[0][0], 0) >= self.t["assign"]:
            conf = "medium"   # whole-source prior (e.g. kernel process docs) is itself evidence
        manual = self._override(chunk, conf)
        if manual is not None:
            chosen = [(c, 99.0) for c in manual]
            conf = "manual" if manual else "out-of-scope"
        courses = [{"code": c, "score": round(s, 1)} for c, s in chosen]
        paths, certs = set(), set()
        for c, _ in chosen:
            meta = self.courses.get(c, {})
            for p in meta.get("pathways", {}):
                paths.update(ALL_PATHS if p == "TRUNK" else [p])
            certs.update(meta.get("certs", []))
        best = {"code": ranked[0][0], "score": round(top, 1)} if ranked else None
        return {"courses": courses, "pathways": sorted(paths), "certs": sorted(certs), "confidence": conf, "best_guess": best}

    def _override(self, chunk, conf=None):
        for o in self.overrides:
            m = o.get("match", {})
            if o.get("only_if") and conf not in o["only_if"]:
                continue          # gap-filling rule: leave chunks the keywords already tagged confidently
            if m.get("source") and m["source"] != chunk["source"]:
                continue
            if m.get("path") and not fnmatch.fnmatch(chunk["path"], m["path"]):
                continue
            if m.get("section") and not re.search(m["section"], chunk["section"], re.I):
                continue
            if m.get("id") and m["id"] != chunk["id"]:
                continue
            return o["courses"]
        return None
