"""Topic 15: getting an index with enumerate."""


tasks = ["Study Python", "Take a break", "Practice"]

# Step 1: Normally, looping over `tasks` gives us only each task string.
# Step 2: enumerate creates pairs such as (1, "Study Python").
# Step 3: start=1 controls the first number; its default would be 0.
for position, task in enumerate(tasks, start=1):
    # Step 4: Python unpacks each pair into `position` and `task`.
    # The loop repeats once for every item in the list.
    print(f"{position}. {task}")
