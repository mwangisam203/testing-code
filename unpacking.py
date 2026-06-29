"""Topic 10: unpacking values."""


person = ("Jordan", 24, "Kentucky")

# Unpacking thinking:
# The left side must match the shape of the data on the right side.
# Here, the tuple has 3 values, so we give Python 3 variable names.
name, age, state = person

numbers = [10, 20, 30, 40]

# `*middle` collects everything that is not first or last.
# This is helpful when you care about the edges more than the center.
first, *middle, last = numbers

print(f"{name} is {age} and lives in {state}.")
print(f"First: {first}, middle: {middle}, last: {last}")

# Unpacking assigns several values at once; `*` gathers the extras.
# A common use is swapping values without a temporary variable:
left = "tea"
right = "coffee"
left, right = right, left
print(f"After swap: left={left}, right={right}")

students = [("Maya", 95), ("Leo", 88), ("Ari", 91)]

# Unpacking in a loop:
# Each item is a tuple with two values, so the loop can unpack them directly.
for student_name, score in students:
    print(f"{student_name} scored {score}")

# This is cleaner than writing:
# for student in students:
#     print(student[0], student[1])

defaults = {"theme": "light", "notifications": True}
overrides = {"theme": "dark"}

# Dictionary unpacking:
# `**defaults` copies the key/value pairs into a new dictionary.
# If the same key appears later, the later value wins.
settings = {**defaults, **overrides}
print(settings)


def create_user(name, role="member", active=True):
    print(f"{name} is an active {role}: {active}")


user_data = {"name": "Sam", "role": "admin"}
create_user(**user_data)


nested_person = ("Maya", ("Python", "CSV"))
person_name, (first_skill, second_skill) = nested_person
print(f"{person_name} knows {first_skill} and {second_skill}.")
