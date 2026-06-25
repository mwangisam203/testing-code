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
