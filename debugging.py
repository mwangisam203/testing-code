"""Topic 25: debugging by tracing values."""


cart = [
    {"item": "notebook", "price": 4.50, "quantity": 2},
    {"item": "pen", "price": 1.25, "quantity": 3},
]

total = 0

for product in cart:
    line_total = product["price"] * product["quantity"]

    # Debugging thinking:
    # When a result feels wrong, print the small pieces before blaming the
    # whole program. This helps you locate the exact step that changed badly.
    print(f"DEBUG: {product['item']} line total is {line_total}")

    total += line_total

print(f"Cart total: ${total:.2f}")


# Example 2: check assumptions before continuing.
# If this condition fails, Python stops right here with a helpful clue.
assert total > 0, "Cart total should be positive."
print("DEBUG: cart total passed the positive check")

# A simple debugging routine:
# 1. What did I expect?
# 2. What actually happened?
# 3. Which variable first becomes wrong?
# 4. What line changed it?
