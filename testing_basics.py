"""Topic 29: testing basics with assert."""


def add_tax(price, rate):
    return price * (1 + rate)


def is_even(number):
    return number % 2 == 0


# Testing thinking:
# A test is a small promise about what your code should do.
# `assert` means "this must be True, or the program should complain."
assert add_tax(100, 0.06) == 106
assert is_even(4) is True
assert is_even(5) is False


def test_discount_math():
    # Putting tests in functions lets you group related checks.
    original_price = 50
    discount = 0.20
    final_price = original_price * (1 - discount)

    assert final_price == 40


test_discount_math()
print("All basic tests passed.")

# Testing habit:
# 1. Pick a simple input.
# 2. Decide the expected output by hand.
# 3. Assert that the function returns that output.
