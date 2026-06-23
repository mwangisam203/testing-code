"""Topic 12: generators and yield."""


def countdown(start):
    while start > 0:
        yield start
        start -= 1


for number in countdown(3):
    print(number)

# `yield` produces one value at a time and pauses the function between values.
