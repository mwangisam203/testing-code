"""Topic 12: generators and yield."""


def countdown(start):
    # Generator thinking:
    # Use `yield` when you want to produce a sequence gradually.
    # The function pauses after each yield and continues from the same spot
    # during the next loop cycle.
    while start > 0:
        yield start
        start -= 1


for number in countdown(3):
    print(number)


# Tip: generator expressions are compact one-time generators.
even_squares = (number**2 for number in range(6) if number % 2 == 0)
print(list(even_squares))

# `yield` produces one value at a time and pauses the function between values.
# This is useful when a full list would be too large or unnecessary.

countdown_values = list(countdown(2))
print(f"Countdown values: {countdown_values}")
