#!/bin/bash
# push.sh — stage everything, commit with date + time, and push.
# Usage: ./push.sh   (or bind to a VS Code shortcut)

# Move to the directory this script lives in, so it works no matter where it's called from
cd "$(dirname "$0")" || exit 1

# If there's nothing to commit, say so and exit cleanly
if [ -z "$(git status --porcelain)" ]; then
  echo "Nothing to commit — working tree clean."
  exit 0
fi

# Stage all changes (new + modified files)
git add -A

# Commit message: e.g. "DSA: 2026-06-28 19:42"
MSG="DSA: $(date '+%Y-%m-%d %H:%M')"
git commit -m "$MSG"

# Push to the current branch
git push

echo "Pushed: $MSG"
