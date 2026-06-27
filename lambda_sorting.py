"""Topic 38: lambda functions and sorting decisions."""


tasks = [
    {"title": "study Python", "priority": 2, "minutes": 45},
    {"title": "reply to email", "priority": 3, "minutes": 10},
    {"title": "exercise", "priority": 1, "minutes": 30},
]

# Lambda thinking:
# A lambda is a small unnamed function.
# It is useful when Python needs a tiny rule right now, like a sorting key.
by_priority = sorted(tasks, key=lambda task: task["priority"])

print("Tasks by priority:")
for task in by_priority:
    print(f"- {task['title']}")


# Sorting by more than one value:
# Return a tuple from the key. Python compares the first item, then the second.
by_priority_then_time = sorted(
    tasks,
    key=lambda task: (task["priority"], task["minutes"]),
)

print("Tasks by priority, then time:")
for task in by_priority_then_time:
    print(f"- {task['title']} ({task['minutes']} minutes)")

# Lambda is not better than `def`; it is just shorter.
# If the logic needs comments, use a normal named function.
