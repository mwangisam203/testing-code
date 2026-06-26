"""Topic 24: modules and imports."""


from modules_helpers import calculate_average, format_money


scores = [90, 84, 100]
average = calculate_average(scores)

print(f"Average score: {average:.1f}")
print(f"Wallet balance: {format_money(42.5)}")

# Module thinking:
# When one file gets too crowded, move reusable functions into another file.
# Then import only the names you need.
#
# In this example:
# - `modules_helpers.py` stores reusable helper functions.
# - `modules_imports.py` uses those helpers to solve a small problem.
#
# This is one of the first steps toward organizing bigger projects.
