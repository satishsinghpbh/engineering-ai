#!/usr/bin/env python3
"""Lightweight catalog validator. Requires PyYAML."""
import sys, yaml

if len(sys.argv) != 2:
    raise SystemExit("Usage: validate-catalog.py repo-catalog/repositories.yaml")

with open(sys.argv[1], encoding="utf-8") as f:
    doc = yaml.safe_load(f)

errors = []
if not isinstance(doc, dict): errors.append("root must be a mapping")
else:
    if not doc.get("organization") or doc["organization"] == "YOUR_GITHUB_ORG":
        errors.append("set organization to your GitHub org")
    repos = doc.get("repositories")
    if not isinstance(repos, list): errors.append("repositories must be a list")
    else:
        seen = set()
        required = ["name","full_name","url","visibility","archived","lifecycle","owner","tier","primary_stack"]
        for i, r in enumerate(repos):
            if not isinstance(r, dict):
                errors.append(f"repositories[{i}] must be a mapping"); continue
            for k in required:
                if k not in r: errors.append(f"repositories[{i}] missing {k}")
            full = r.get("full_name")
            if full in seen: errors.append(f"duplicate full_name: {full}")
            seen.add(full)
            if r.get("owner") == "unknown":
                errors.append(f"{full}: owner is unknown")
            if r.get("tier") == "unknown":
                errors.append(f"{full}: tier is unknown")

if errors:
    print("Catalog validation failed:")
    print("\\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)
print(f"Catalog looks structurally valid ({len(doc.get('repositories', []))} repos).")
