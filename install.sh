#!/bin/sh
# Link each skill of this repo into a Claude Code skills directory.
# Usage: ./install.sh [skills-dir]   (default: ~/.claude/skills)
set -e
repo=$(cd "$(dirname "$0")" && pwd)
dest=${1:-$HOME/.claude/skills}
mkdir -p "$dest"
for skill in "$repo"/*/SKILL.md; do
  dir=$(dirname "$skill")
  name=$(basename "$dir")
  if [ -e "$dest/$name" ] && [ ! -L "$dest/$name" ]; then
    echo "$dest/$name exists and is not a link: move it away first" >&2
    exit 1
  fi
  ln -sfn "$dir" "$dest/$name"
  echo "$dest/$name -> $dir"
done
