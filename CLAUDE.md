# zedong-skill

- The repo is public: no secrets, no machine details (absolute paths, user or host names, thread or session IDs), nothing from other people's projects.
- A skill holds the user's taste, not patches. Models keep getting stronger, so a rule that corrects today's model soon goes stale; taste does not. Test each line: would a much stronger model, without it, still do what the user wants? Then delete it. A rule for one project goes in that project's `CLAUDE.md`. Prefer deleting to adding.
- A skill sets taste, not every choice. What the work should decide, such as a paper's sections or a talk's format, stays with the model or the user.
- Skills split by what the user does, one dimension, named `zedong-<action>`: think, research, write. A medium of an action, such as a talk, is a sub-skill its parent points to.
- Threads on several machines invoke the skills by name: keep each directory name and its `name:` field.
- Skills are installed as links (`install.sh`), so a pushed commit takes effect in the next session; other machines pull.
- Commit and push to main.
