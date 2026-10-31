task = "Order ALTA survey"
phase = "Due Diligence"
days_left = 9

print(task)
print(phase)
print(days_left + 2)
print("task")

phases = ["LOI", "Due Diligence", "Financing", "Closing"]

print(phases)
print(phases[0])
print(phases[1])
print(len(phases))
print(phases[3])


# CSA-9 Session 2 — Dictionaries — timebox: 60 min — start 4:00pm

task_info = {
    "name": "Order ALTA survey",
    "phase": "Due Diligence",
    "owner": "Title Company",
    "status": "Working on it"
}

print(task_info["name"])
print(task_info["owner"])
print(len(task_info))
task_info["status"] = "Done"
task_info["due_date"] = "2026-11-15"

print(task_info["status"])
print(task_info)
print(len(task_info))
# print(task_info["deadline"])
print(task_info.get("deadline"))
print(task_info.get("deadline", "No deadline set"))

# NOTES — Dictionaries
# A dictionary stores keys and their values.
# I read a value with task_info["key"].
# If the key already exists, = changes its value. If it doesn't exist, = adds it.
# len() on a dictionary counts how many keys it has.
# KeyError means the key is not in the dictionary.
# .get() is safer because instead of crashing, Python returns a default value
#   (the message I wrote as an alternative), or None if I didn't write one.
# Python only knows what I wrote in the code, nothing else.

# CSA-9 Session 3 — for loops, if, functions — timebox: 90 min — start 8:55pm

tasks = [
    {"name": "Order ALTA survey", "phase": "Due Diligence", "status": "Working on it"},
    {"name": "Review loan documents", "phase": "Financing", "status": "Not Started"},
    {"name": "Wire closing funds to escrow", "phase": "Closing", "status": "Not Started"},
]

for row in tasks:
    if row["status"] == "Working on it":
        print(row["name"])

def print_tasks_by_status(status):
    for row in tasks:
        if row["status"] == status:
            print(row["name"])

print_tasks_by_status("Working on it")
print_tasks_by_status("Not Started")

# NOTES — for loops, if, functions
# A for loop repeats the same code for each item in a list, without having to write it again.
# Indentation matters after a line that ends with ":" — 4 spaces tell Python that line is inside the block.
# == asks "is it equal to?" / = assigns a value.
# IndentationError means a line that should be indented isn't, so Python finds an empty block after the "for".
# def creates a function but doesn't run it. It only runs when you call it.
# A parameter is an empty slot that gets filled when you call the function.

# CSA-9 Session 4 — import + solo exercise — timebox: 45 min — start 10:25pm

import datetime

today = datetime.date.today()
print(today)

def print_tasks_by_phase(phase):
    for row in tasks:
        if row["phase"] == phase:
            print(row["name"])

print_tasks_by_phase("LOI")
print_tasks_by_phase("Due Diligence")