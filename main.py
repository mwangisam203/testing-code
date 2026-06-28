"""Topic 1: loops and input validation."""

import math


def explain_square_root_rule(value):
    # Example 2: isolate one rule in a helper function.
    # This makes the main loop easier to read because the explanation has a
    # clear name and one small job.
    if value < 0:
        return "A square root needs a non-negative number."

    return "This number can be square-rooted."


while True:
    try:
        number = float(input("Enter a number that is 0 or greater: "))

        if number < 0:
            print(explain_square_root_rule(number))
            continue

        break
    except ValueError:
        print("Please enter numbers only.")

square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root:.2f}")
