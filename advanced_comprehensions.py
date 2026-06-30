"""Topic 37: advanced comprehensions."""


scores = [92, 67, 81, 45, 100]

# Comprehension thinking:
# A comprehension can transform values and filter values in one readable line.
# Read this as: "keep each score, but only if the score is passing."
passing_scores = [score for score in scores if score >= 70]
print(f"Passing scores: {passing_scores}")


# You can also choose one value or another with an inline conditional.
# Read this as: "write Pass if the score is high enough, otherwise Fail."
labels = ["Pass" if score >= 70 else "Fail" for score in scores]
print(f"Labels: {labels}")


students = ["maya", "leo", "ari"]

# Dictionary comprehensions build dictionaries.
# Here, each lowercase name becomes a key, and the capitalized name becomes
# the value.
name_lookup = {name: name.title() for name in students}
print(name_lookup)


# Set comprehensions keep only unique results.
first_letters = {name[0] for name in students}
print(first_letters)

# Good taste rule:
# Use comprehensions when they stay readable.
# If the line gets too clever, write a normal loop.

score_labels = {score: ("pass" if score >= 70 else "fail") for score in scores}
print(score_labels)
