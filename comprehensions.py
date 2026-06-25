"""Topic 8: list comprehensions."""


numbers = [1, 2, 3, 4, 5, 6]

# Comprehension thinking:
# Read from left to right after the first expression:
# "for each number in numbers, if the number is even, keep number squared."
squares_of_even_numbers = [number**2 for number in numbers if number % 2 == 0]

print(squares_of_even_numbers)

# Read it as: square each number, but only when the number is even.
# The same idea as a loop:
# 1. Visit each item.
# 2. Optionally filter items.
# 3. Transform the items you keep.
