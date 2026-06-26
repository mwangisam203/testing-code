"""Topic 26: nested data structures."""


students = [
    {
        "name": "Maya",
        "scores": {"math": 92, "reading": 88},
    },
    {
        "name": "Leo",
        "scores": {"math": 81, "reading": 95},
    },
]

# Nested-data thinking:
# Real data often has layers:
# - a list of students
# - each student is a dictionary
# - each student's scores are another dictionary
for student in students:
    name = student["name"]
    math_score = student["scores"]["math"]
    reading_score = student["scores"]["reading"]
    average = (math_score + reading_score) / 2

    print(f"{name}'s average is {average:.1f}")

# How to read nested access:
# student["scores"]["math"]
# means:
# 1. Get the student's scores dictionary.
# 2. From that dictionary, get the math score.
#
# Do not rush nested data. Read one layer at a time.
