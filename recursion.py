"""Topic 14: recursion and base cases."""


def factorial(number):
    # Recursion thinking:
    # 1. Find the smallest version of the problem.
    #    1! and 0! are both 1, so we can stop there.
    if number <= 1:
        return 1

    # 2. Shrink the problem toward the base case.
    #    factorial(5) becomes 5 * factorial(4).
    #    factorial(4) becomes 4 * factorial(3), and so on.
    return number * factorial(number - 1)


print(f"5 factorial is {factorial(5)}")


def count_down(number):
    # This smaller recursion example is easier to trace in your head.
    # First print the current number, then call the function with a smaller one.
    if number == 0:
        print("Done")
        return

    print(number)
    count_down(number - 1)


count_down(3)

# The base case stops the calls. Without it, recursion never finishes.
# When stuck on recursion, ask:
# - What is the stopping point?
# - How does each call get closer to that point?
# - What value is returned when the calls unwind?
# Recursion is not always the easiest answer. If a normal loop is clearer,
# use the loop. Clarity beats cleverness.
