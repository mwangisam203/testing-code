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

# `yield` produces one value at a time and pauses the function between values.
# This is useful when a full list would be too large or unnecessary.
