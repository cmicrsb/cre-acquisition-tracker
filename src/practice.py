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