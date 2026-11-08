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
            lines.append(f"- {t['name']} | {t['party']} | {t['days_late']} days late")
    else:
        lines.append("- None")

    lines.append("\nUpcoming tasks (next 7 days):")
    if upcoming:
        for t in upcoming:
            lines.append(f"- {t['name']} | {t['party']} | {t['days_left']} days left")
    else:
        lines.append("- None")

    data = "\n".join(lines)

    # 2. Instructions for Claude + the data
    prompt = f"""You are the operations manager of a commercial real estate investment firm.
Write the weekly status of an acquisition deal for the COO.

Rules:
- Use exactly three sections with these headings: Summary, Risks, Next steps.
- Keep it under 300 words so the COO can read it in 2 minutes.
- Use only the data below. Do not invent dates, names, numbers or events.
- If there are no overdue tasks, say so in Risks and focus on upcoming deadlines.
- Executive tone: clear, direct, no filler.

Deal data:
{data}
"""
    return prompt


if __name__ == "__main__":
    tasks = load_tasks()
    prompt = build_prompt(progress_by_phase(tasks), overdue_tasks(tasks), upcoming_tasks(tasks))
    status = ask_claude(prompt)
    if status is None:
        print("Could not generate the status. Check the error above.")
    else:
        print(status)