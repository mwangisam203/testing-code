"""Topic 17: custom sorting with a key function."""


students = [("Mia", 96), ("Noah", 84), ("Ava", 91)]

# Step 1: Each tuple contains (name, score), so index 1 is the score.
# Step 2: the lambda receives one tuple and returns that score.
# Step 3: sorted uses the returned scores when comparing the tuples.
# Step 4: reverse=True changes the order from lowest-first to highest-first.
# sorted returns a new list, meaning the original `students` list is unchanged.
ranked_students = sorted(students, key=lambda student: student[1], reverse=True)

# Step 5: unpack and print each tuple from the newly ordered list.
for name, score in ranked_students:
    print(f"{name}: {score}")

# Sorting thinking:
# First decide what "best" or "first" means.
# Here, "best" means the highest score, so the key must return the score.


# Tip: `min` and `max` can use the same key idea as `sorted`.
top_student = max(students, key=lambda student: student[1])
print(f"Top student: {top_student[0]}")
