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

# `raise` reports a problem; `except` decides how to handle it.
# A good error message should explain what was wrong, not just that it failed.
