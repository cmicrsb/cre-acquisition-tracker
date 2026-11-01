import csv

PHASES = ["LOI", "Due Diligence", "Financing", "Closing"]

tasks = []
current_phase = None

with open("data/monday_export.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        first = row[0]

        # Rule 1: phase row -> remember the phase, then skip the row
        if first in PHASES:
            current_phase = first
            continue

        # Rule 2: skip empty, summary, header and title rows
        if first == "" or first == "Name" or current_phase is None:
            continue

        # Rule 3: it's a task -> save it with its phase
        task = {
            "name": row[0],
            "owner": row[1],
            "status": row[2],
            "due_date": row[3],
            "party": row[4],
            "depends_on": row[5],
            "phase": current_phase,
        }
        tasks.append(task)

print(len(tasks), "tasks")
for task in tasks:
    print(task["phase"], "|", task["name"])