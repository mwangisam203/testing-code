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


# Example 2: find the strongest subject for each student.
# When nested data has named values, loop through `.items()` so you get both
# the subject name and the score together.
for student in students:
    best_subject = None
    best_score = 0

    for subject, score in student["scores"].items():
        if score > best_score:
            best_subject = subject
            best_score = score

    print(f"{student['name']}'s best subject is {best_subject}.")


# Example 3: safely read optional nested data with `.get()`.
# Some real data is incomplete, so `.get()` lets us provide a default instead
# of crashing with a KeyError.
students[0]["contact"] = {"email": "maya@example.com"}

for student in students:
    contact = student.get("contact", {})
    email = contact.get("email", "no email listed")
    print(f"{student['name']} email: {email}")


# Extra example: flatten nested data into simple rows.
# This is useful before saving to CSV or displaying a table.
rows = []
for student in students:
    for subject, score in student["scores"].items():
        rows.append({"name": student["name"], "subject": subject, "score": score})

print(rows)

# How to read nested access:
# student["scores"]["math"]
# means:
# 1. Get the student's scores dictionary.
# 2. From that dictionary, get the math score.
#
# Do not rush nested data. Read one layer at a time.
