---
name: zedong-ci
description: How the user wants a failing GitHub Actions workflow diagnosed. Use when a workflow, CI check or scheduled job keeps failing, or CI failure mail piles up.
---

Find when it started failing, which jobs fail, and whether every trigger fails or only `schedule`. Read the first real error in the log, not the cascade after it.

Name the cause before fixing anything:

- A fork or stale schedule: a cron job inherited from upstream that the fork does not need. Remove the `schedule:` triggers or disable the workflow; do not repair upstream's job.
- External breakage: a dead link, a moved dependency, an API change, an expired secret.
- A real code or type error: reproduce it locally with the same command, then make the smallest diff.
- Flaky or infra: a runner timeout or network blip. A re-run that passes settles it.

Report in two or three sentences: what fails, why, and the smallest fix. After a fix lands, the next run, or the absence of scheduled runs, confirms it.
