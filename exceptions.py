"""Topic 11: raising and catching exceptions."""


def divide(total, people):
    # Exception thinking:
    # Some inputs make the operation impossible.
    # Dividing by zero people would crash or give a meaningless answer.
    if people <= 0:
        raise ValueError("The number of people must be positive.")

    return total / people


try:
    # Put the risky action in `try`.
    share = divide(45, 0)
    print(f"Each person pays ${share:.2f}")
except ValueError as error:
    # Put the recovery plan in `except`.
    print(f"Could not divide the bill: {error}")


try:
    # `else` and `finally` make the flow more specific:
    # - `try` is the risky action.
    # - `except` runs only when the chosen error happens.
    # - `else` runs only when no exception happened.
    # - `finally` always runs, even if there was an error.
    share = divide(45, 3)
except ValueError as error:
    print(f"Could not divide the bill: {error}")
else:
    print(f"Clean split: ${share:.2f}")
finally:
    print("Finished division attempt.")


try:
    number = int("not a number")
except ValueError:
    print("Could not convert text to an integer.")

# `raise` reports a problem; `except` decides how to handle it.
# A good error message should explain what was wrong, not just that it failed.
# Use `else` for success-only work. Use `finally` for cleanup work, such as
# closing files or releasing resources.

try:
    divide(10, -1)
except ValueError as error:
    print(f"Extra check caught: {error}")

def parse_integer(text):
    try:
        return int(text)
    except ValueError:
        return None

print(f"Parsed value: {parse_integer('42')}")

print(f"Invalid parsed value: {parse_integer('oops')}")

print(f"Bad input result: {parse_integer('hello')}")

print(f"Parsed zero: {parse_integer('0')}")

print(f"Parsed negative number: {parse_integer('-7')}")

print(f"Parsed year: {parse_integer('2026')}")

print(f"Parsed decimal input: {parse_integer('3.14')}")
