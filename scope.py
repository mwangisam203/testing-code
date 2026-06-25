"""Topic 9: local and global scope."""


tax_rate = 0.06


def add_tax(price):
    # Scope thinking:
    # `price` is local because it is created as a parameter.
    # `tax_rate` is global because it was created outside the function.
    total = price * (1 + tax_rate)

    # Returning `total` is cleaner than printing inside this function because
    # the caller can decide what to do with the answer.
    return total


print(f"Total: ${add_tax(20):.2f}")

# `tax_rate` is global. `price` and `total` exist only inside the function.
# If a function changes too many global variables, it becomes harder to trust.
# Prefer passing data in and returning data out.
