"""Topic 2: functions, parameters, and return values."""


def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    return subtotal * (1 - discount)


# The arguments are copied into the function's parameters.
total = calculate_total(12.50, 3, discount=0.10)
print(f"Total after discount: ${total:.2f}")

# `return` sends a value back; `print` only displays a value.
