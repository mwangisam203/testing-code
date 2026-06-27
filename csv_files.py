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

    for row in reader:
        # CSV values are read as strings, so convert numbers when needed.
        score = int(row["score"])
        print(f"{row['name']} scored {score}")

# CSV habit:
# Use dictionaries when column names matter.
# Convert text values back into numbers before doing math.
