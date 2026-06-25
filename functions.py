"""Topic 2: functions, parameters, and return values."""


def calculate_total(price, quantity, discount=0):
    # Function thinking:
    # 1. Put repeatable logic behind a clear name.
    # 2. Use parameters for the values that may change.
    # 3. Return the answer instead of locking the function to one print style.
    subtotal = price * quantity
    discount_amount = subtotal * discount
    final_total = subtotal - discount_amount
    return final_total


def is_passing(score, passing_score=70):
    # Boolean helper thinking:
    # If a question has a yes/no answer, return True or False.
    # The default passing score is 70, but the caller can override it.
    return score >= passing_score


# The arguments are copied into the function's parameters.
total = calculate_total(12.50, 3, discount=0.10)
print(f"Total after discount: ${total:.2f}")
print(f"Score passes? {is_passing(82)}")
print(f"Harder class passes? {is_passing(82, passing_score=85)}")

# `return` sends a value back; `print` only displays a value.
# If you can describe a chunk of code with a useful verb phrase,
# it may be a good candidate for a function.
# Tiny functions are not silly when they make the main program easier to read.
