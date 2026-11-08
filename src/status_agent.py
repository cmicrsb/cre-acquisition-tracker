import json
from read_monday import load_tasks, progress_by_phase, overdue_tasks, upcoming_tasks
from claude_client import ask_claude


def build_prompt(progress, overdue, upcoming):
    # 1. Turn the deal data into plain text lines
    lines = ["Progress by phase:"]
    for p in progress:
        lines.append(f"- {p['phase']}: {p['done']} of {p['total']} tasks done ({p['percent']}%)")

    lines.append("\nOverdue tasks:")
    if overdue:
        for t in overdue:
            line = f"- {t['name']} | {t['party']} | {t['days_late']} days late"
            if t["depends_on"] != "":
                line = line + f" | depends on: {t['depends_on']}"
            lines.append(line)
    else:
        lines.append("- None")

    lines.append("\nUpcoming tasks (next 7 days):")
    if upcoming:
        for t in upcoming:
            line = f"- {t['name']} | {t['party']} | {t['days_left']} days left"
            if t["depends_on"] != "":
                line = line + f" | depends on: {t['depends_on']}"
            lines.append(line)
    else:
        lines.append("- None")

    data = "\n".join(lines)

    # 2. Instructions for Claude + the data
    prompt = f"""You are the operations manager of a commercial real estate investment firm.
Write the weekly status of an acquisition deal for the COO.

Rules:
- Return ONLY a JSON object with exactly these keys: "summary" (a string), "risks" (a list of strings), "next_steps" (a list of strings).
- Do not add any text, explanation or code block before or after the JSON.
- Keep it under 300 words so the COO can read it in 2 minutes.
- Use only the data below. Do not invent dates, names, numbers or events.
- Only mention or imply a dependency between tasks if it is listed as "depends on" in the data. Do not say a task is at risk because of another task unless that dependency is listed in the data.
- Do not repeat the same fact in more than one bullet or section, except a short mention in the Summary.
- If there are no overdue tasks, say so in Risks and focus on upcoming deadlines.
- Executive tone: clear, direct, no filler.

Deal data:
{data}
"""
    return prompt


def parse_report(text):
    try:
        report = json.loads(text)
    except json.JSONDecodeError:
        print("Error: Claude did not return valid JSON.")
        return None
    for key in ["summary", "risks", "next_steps"]:
        if key not in report:
            print(f"Error: missing key '{key}'.")
            return None

    if not isinstance(report["summary"], str):
        print("Error: 'summary' should be a string.")
        return None

    for key in ["risks", "next_steps"]:
        if not isinstance(report[key], list):
            print(f"Error: '{key}' should be a list.")
            return None
    return report


if __name__ == "__main__":
    tasks = load_tasks()
    prompt = build_prompt(progress_by_phase(tasks), overdue_tasks(tasks), upcoming_tasks(tasks))
    status = ask_claude(prompt)
    if status is None:
        print("Could not generate the status. Check the error above.")
    else:
        report = parse_report(status)
        if report is not None:
            print(json.dumps(report, indent=2))