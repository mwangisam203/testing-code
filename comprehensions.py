"""Topic 8: list comprehensions."""


numbers = [1, 2, 3, 4, 5, 6]
squares_of_even_numbers = [number**2 for number in numbers if number % 2 == 0]

print(squares_of_even_numbers)

# Read it as: square each number, but only when the number is even.
