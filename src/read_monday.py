import csv
from datetime import date, timedelta

PHASES = ["LOI", "Due Diligence", "Financing", "Closing"]
VALID_STATUSES = ["Done", "In Progress", "Not Started"]

def load_tasks():
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
            due_text = row[3].strip()
            if due_text == "":
                due_date = None
            else:
                due_date = date.fromisoformat(due_text)
            task = {
                "name": row[0],
                "owner": row[1],
                "status": row[2].strip(),
                "due_date": due_date,
                "party": row[4],
                "depends_on": row[5],
                "phase": current_phase,
            }
            if task["status"] not in VALID_STATUSES:
                print("Warning: unknown status", task["status"], "in", task["name"])
            tasks.append(task)

    return tasks


tasks = load_tasks()

print(len(tasks), "tasks")
for task in tasks:
    print(task["phase"], "|", task["name"])

def progress_by_phase(tasks):
    progress = []
    for phase in PHASES:
        total = 0
        done = 0
        for task in tasks:
            if task["phase"] == phase:
                total = total + 1
                if task["status"] == "Done":
                    done = done + 1
        if total == 0:
            percent = 0
        else:
            percent = round(done / total * 100)
        progress.append({"phase": phase, "done": done, "total": total, "percent": percent})
    return progress


for p in progress_by_phase(tasks):
    print(f"{p['phase']}: {p['done']} of {p['total']} - {p['percent']}%")

# CSA-12: overdue tasks
def overdue_tasks(tasks):
    today = date.today()
    overdue = []
    for task in tasks:
        if task["due_date"] is not None and task["due_date"] < today and task["status"] != "Done":
            days_late = (today - task["due_date"]).days
            overdue.append({"name": task["name"], "party": task["party"], "days_late": days_late})
    return overdue


print("\nOverdue tasks:")
for t in overdue_tasks(tasks):
    print(f"- {t['name']} | {t['party']} | {t['days_late']} days late")


# CSA-14: upcoming tasks (next 7 days)
def upcoming_tasks(tasks):
    today = date.today()
    limit = today + timedelta(days=7)
    upcoming = []
    for task in tasks:
        due = task["due_date"]
        if due is not None and today <= due <= limit and task["status"] != "Done":
            days_left = (due - today).days
            upcoming.append({"name": task["name"], "party": task["party"], "days_left": days_left})
    return upcoming


print("\nUpcoming tasks (next 7 days):")
for t in upcoming_tasks(tasks):
    print(f"- {t['name']} | {t['party']} | {t['days_left']} days left")