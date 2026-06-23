"""Topic 14: recursion and base cases."""


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print(f"5 factorial is {factorial(5)}")

# The base case stops the calls. Without it, recursion never finishes.
