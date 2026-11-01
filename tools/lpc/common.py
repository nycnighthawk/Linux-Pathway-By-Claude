"""Shared paths, loaders and small helpers for the lpc toolchain."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("LPC_ROOT", Path(__file__).resolve().parents[2]))
RAW = ROOT / "raw"
CACHE = ROOT / ".cache"
CATALOG = ROOT / "catalog"
BUILD = ROOT / "build"
REVIEW = ROOT / "review"
SITE = ROOT / "site"
DECISIONS = ROOT / "decisions"

# Licences that may never be stored as text (decision D-004).
DENY_LICENCE = re.compile(r"\bNC\b|-NC-|\bND\b|-ND-", re.I)


def today() -> str:
    return _dt.date.today().isoformat()


def load_sources() -> list[dict]:
    data = yaml.safe_load((ROOT / "sources.yaml").read_text())
    return data["sources"]


def source_map() -> dict[str, dict]:
    return {s["id"]: s for s in load_sources()}


def load_taxonomy() -> dict:
    return yaml.safe_load((ROOT / "taxonomy" / "courses.yaml").read_text())


def sha1(*parts: str) -> str:
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode("utf-8", "replace"))
        h.update(b"\0")
    return h.hexdigest()[:16]


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)[:80]


def words(text: str) -> int:
    return len(re.findall(r"\w+", text))


def excerpt(text: str, n: int = 30) -> str:
    toks = re.sub(r"\s+", " ", text).strip().split(" ")
    out = " ".join(toks[:n])
    return out + (" …" if len(toks) > n else "")


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def read_provenance(source_id: str) -> dict:
    p = RAW / source_id / "SOURCE.yaml"
    return yaml.safe_load(p.read_text()) if p.exists() else {}


def write_provenance(source_id: str, data: dict) -> None:
    p = RAW / source_id / "SOURCE.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
