# Sprint Log — CRE Status Agent

## Sprint 1 (Oct 27 – Nov 10, 2026)

**Goal:** My script reads the Monday CSV, cleans it and shows progress for each of the 4 phases.

### Notes
- Oct 27: I opened the Monday export in TextEdit and found the data wasn't clean: the headers repeat for each phase, and there are title, summary and empty rows mixed in. Good news: names with commas are wrapped in quotes, so Python's csv module can handle them. Cleaning this is my first code challenge.

### Review
- Result: Goal met. The script reads 18 tasks and shows the progress for each phase.
- Done: CSA-8, CSA-9, CSA-10, CSA-11, CSA-13
- Not done (and why): CSA-12 (stretch) — not started. I had 3 days off, so I focused on the sprint goal first.
- Demo: When I run read_monday.py, it cleans the data: it skips the title, the phase rows, the repeated headers, and the empty rows. No status warnings were displayed, so the data passed validation. During the demo I found a format bug (50 % instead of 50%), and I fixed it with an f-string.

### Retro
- What worked: Predicting the output before running the code, breaking the code on purpose to learn how to read a traceback, checking the data before cleaning it, and adding a warning instead of fixing bad data silently.
- What didn't work: My estimates. CSA-9 part 1 took twice its timebox, and CSA-8 and CSA-10 had no timebox at all. Small mistakes also slipped through (unsaved files, indentation, wrong working directory).
- What I'll change in Sprint 2: (1) Set a timebox for every ticket and log the actual time; if I go 30 minutes over, I stop and split the ticket. (2) Use a quick checklist before running code: Cmd+S, cd into the project, check the file name.