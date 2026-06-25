"""Topic 3: lists, dictionaries, and loops."""


scores = [82, 95, 71, 88]
student = {"name": "Maya", "scores": scores}

total = 0

# Loop thinking:
# `total` starts at 0 because no scores have been counted yet.
# Each loop adds one more score to the running total.
for score in student["scores"]:
    total += score

average = total / len(student["scores"])
print(f"{student['name']}'s average is {average:.1f}")

# Updating collections:
# Lists are useful when the number of items can grow over time.
student["scores"].append(100)
new_average = sum(student["scores"]) / len(student["scores"])
print(f"After one more test: {new_average:.1f}")

# Dictionaries can also grow by adding a new key.
student["grade"] = "A"
print(f"{student['name']} currently has grade {student['grade']}.")

# A list stores ordered items. A dictionary labels values with keys.
# Use a dictionary when names make the data easier to understand:
# `student["scores"]` is clearer than remembering that scores are item 1.
