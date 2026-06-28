"""Topic 32: reading and writing CSV files."""


import csv


filename = "students.csv"
students = [
    {"name": "Maya", "score": 92},
    {"name": "Leo", "score": 81},
    {"name": "Ari", "score": 95},
]

# CSV thinking:
# CSV is a spreadsheet-friendly text format.
# Each row is one record, and each column has a name.
with open(filename, "w", encoding="utf-8", newline="") as file:
    fieldnames = ["name", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)


with open(filename, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    loaded_students = []

    for row in reader:
        # CSV values are read as strings, so convert numbers when needed.
        score = int(row["score"])
        loaded_students.append({"name": row["name"], "score": score})
        print(f"{row['name']} scored {score}")


# Bonus CSV thinking:
# Once CSV rows are loaded into normal dictionaries, you can use the same
# list/dictionary patterns from the rest of the project.
total_score = 0
highest_student = None

for student in loaded_students:
    total_score += student["score"]

    if highest_student is None or student["score"] > highest_student["score"]:
        highest_student = student

average_score = total_score / len(loaded_students)
print(f"Average score: {average_score:.1f}")
print(f"Highest score: {highest_student['name']} with {highest_student['score']}")


# Example 2: filter CSV data after reading it.
# Once rows are converted into dictionaries, filtering works like any list of
# dictionaries in Python.
honor_roll = []
for student in loaded_students:
    if student["score"] >= 90:
        honor_roll.append(student["name"])

print(f"Honor roll: {honor_roll}")


# Example 3: group CSV-style rows into buckets.
# Here we group names by pass/fail status.
students_by_status = {"pass": [], "needs practice": []}

for student in loaded_students:
    if student["score"] >= 70:
        students_by_status["pass"].append(student["name"])
    else:
        students_by_status["needs practice"].append(student["name"])

print(students_by_status)

# CSV habit:
# Use dictionaries when column names matter.
# Convert text values back into numbers before doing math.
# After loading CSV data, ask a real question about it: average, highest,
# lowest, filtered rows, grouped rows, and so on.
