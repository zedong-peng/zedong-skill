# zedong-skill

- The repo is public: no secrets, no machine details (absolute paths, user or host names, thread or session IDs), nothing from other people's projects.
- A skill holds only what a strong model would not infer and what applies across the user's projects. A rule for one project goes in that project's `CLAUDE.md`. Prefer deleting to adding.
- Threads on several machines invoke the skills by name: keep each directory name and its `name:` field.
- Skills are installed as links (`install.sh`), so a pushed commit takes effect in the next session; other machines pull.
- Commit and push to main.
