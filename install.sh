#!/bin/sh
# Link each skill of this repo into the user skill directories of Claude Code,
# Codex and Gemini (Antigravity), or only into the directory given as argument.
# Usage: ./install.sh [skills-dir]
set -e
repo=$(cd "$(dirname "$0")" && pwd)
dests=${1:-"$HOME/.claude/skills $HOME/.codex/skills $HOME/.gemini/config/skills"}
for dest in $dests; do
  mkdir -p "$dest"
  for skill in "$repo"/*/SKILL.md; do
    dir=$(dirname "$skill")
    name=$(basename "$dir")
    if [ -e "$dest/$name" ] && [ ! -L "$dest/$name" ]; then
      echo "$dest/$name exists and is not a link: move it away first" >&2
      exit 1
    fi
    ln -sfn "$dir" "$dest/$name"
  done
  echo "linked into $dest"
done
