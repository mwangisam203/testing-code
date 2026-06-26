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

# `raise` reports a problem; `except` decides how to handle it.
# A good error message should explain what was wrong, not just that it failed.
# Use `else` for success-only work. Use `finally` for cleanup work, such as
# closing files or releasing resources.
