#!/bin/bash
cd "$(dirname "$0")" || exit 1
if [ -z "$(git status --porcelain)" ]; then
  echo "Nothing to commit — working tree clean."
  exit 0
fi
git add -A
MSG="DSA: $(date '+%Y-%m-%d %H:%M')"
git commit -m "$MSG"
git push
echo "Pushed: $MSG"
