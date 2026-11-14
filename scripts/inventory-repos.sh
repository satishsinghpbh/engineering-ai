#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <github-org>" >&2
  exit 2
fi

ORG="$1"
command -v gh >/dev/null || { echo "GitHub CLI (gh) is required" >&2; exit 1; }
command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }

gh auth status >/dev/null
# Read-only metadata inventory. No clone, writes, or repository configuration changes.
gh repo list "$ORG" --limit 1000 \
  --json name,nameWithOwner,url,visibility,isArchived,isFork,description,primaryLanguage,languages,repositoryTopics,defaultBranchRef,updatedAt \
  | jq 'map({
      name: .name,
      full_name: .nameWithOwner,
      url: .url,
      visibility: (.visibility | ascii_downcase),
      archived: .isArchived,
      fork: .isFork,
      description: (.description // ""),
      primary_language: (.primaryLanguage.name // "unknown"),
      languages: ([.languages[].name] // []),
      topics: ([.repositoryTopics[].name] // []),
      default_branch: (.defaultBranchRef.name // null),
      updated_at: .updatedAt
    })'
