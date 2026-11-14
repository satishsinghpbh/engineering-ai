#!/usr/bin/env python3
"""Heuristic first-pass catalog generator. Review every classification with owners."""
import json, sys, yaml
from datetime import datetime, timezone

if len(sys.argv) != 2:
    raise SystemExit("Usage: classify-repos.py /path/to/repos.json")

with open(sys.argv[1], encoding="utf-8") as f:
    raw = json.load(f)

def stack_for(repo):
    langs = {x.lower() for x in repo.get("languages", [])}
    primary = (repo.get("primary_language") or "unknown").lower()
    all_langs = langs | {primary}
    if "typescript" in all_langs or "javascript" in all_langs:
        return "javascript-typescript (verify framework)"
    if "python" in all_langs: return "python"
    if "go" in all_langs: return "go"
    if "java" in all_langs or "kotlin" in all_langs: return "jvm"
    if "c#" in all_langs: return "dotnet"
    if "ruby" in all_langs: return "ruby"
    if "rust" in all_langs: return "rust"
    if "swift" in all_langs: return "swift"
    if "kotlin" in all_langs: return "kotlin"
    return primary or "unknown"

repos = []
for r in raw:
    archived = bool(r.get("archived", False))
    repos.append({
        "name": r["name"],
        "full_name": r["full_name"],
        "url": r["url"],
        "visibility": r.get("visibility", "unknown"),
        "archived": archived,
        "lifecycle": "archived" if archived else "unknown",
        "owner": "unknown",
        "tier": "unknown",
        "primary_stack": stack_for(r),
        "languages": sorted(set(r.get("languages", []))),
        "topics": r.get("topics", []),
        "has_ci": "unknown",
        "has_codeowners": "unknown",
        "notes": "Auto-generated; verify lifecycle, owner, tier, stack, CI and CODEOWNERS."
    })

doc = {
    "organization": "REPLACE_WITH_ORG",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "repositories": repos
}
yaml.safe_dump(doc, sys.stdout, sort_keys=False, allow_unicode=True)
