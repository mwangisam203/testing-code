"""Topic 9: local and global scope."""


tax_rate = 0.06


def add_tax(price):
    total = price * (1 + tax_rate)
    return total


print(f"Total: ${add_tax(20):.2f}")

# `tax_rate` is global. `price` and `total` exist only inside the function.
