---
name: zedong-t3-threads
description: How to look through the user's T3 Code threads. Use when asked to see, search or summarize their T3 Code threads or conversations.
---

Read-only. T3 Code keeps its state in a local SQLite file; open it read-only and never write to it, or ask T3 itself.

The schema changes between versions: list tables and columns before querying, and prefer T3's own message search for keyword questions.

Start with a short listing, the latest twenty or so threads with title, project and last update, then open the one the user picks. Times are stored in UTC; report them in the user's time zone.

Summarize in plain words and quote only the lines that matter. No whole transcripts unless asked.
