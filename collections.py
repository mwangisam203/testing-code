"""Topic 3: lists, dictionaries, and loops."""


scores = [82, 95, 71, 88]
student = {"name": "Maya", "scores": scores}

total = 0
for score in student["scores"]:
    total += score

average = total / len(student["scores"])
print(f"{student['name']}'s average is {average:.1f}")

# A list stores ordered items. A dictionary labels values with keys.
