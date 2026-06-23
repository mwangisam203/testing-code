"""Topic 11: raising and catching exceptions."""


def divide(total, people):
    if people <= 0:
        raise ValueError("The number of people must be positive.")
    return total / people


try:
    share = divide(45, 0)
    print(f"Each person pays ${share:.2f}")
except ValueError as error:
    print(f"Could not divide the bill: {error}")

# `raise` reports a problem; `except` decides how to handle it.
