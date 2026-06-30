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


def add_custom_tax(price, rate):
    # This version is more flexible because it does not depend on the global
    # `tax_rate`. The caller chooses the rate each time.
    return price * (1 + rate)


print(f"Custom total: ${add_custom_tax(20, 0.08):.2f}")


def make_multiplier(multiplier):
    # Closure thinking:
    # The inner function "remembers" the multiplier even after the outer
    # function has finished running.
    def multiply(number):
        return number * multiplier

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())
print(counter())

# `tax_rate` is global. `price` and `total` exist only inside the function.
# If a function changes too many global variables, it becomes harder to trust.
# Prefer passing data in and returning data out.
# This habit makes functions easier to test because the answer depends only on
# the arguments you pass in.
# Closures are one reason decorators work: a returned function can remember
# values from the function that created it.
# `nonlocal` lets an inner function update a variable from the outer function.

quadruple = make_multiplier(4)
print(f"Quadruple 5: {quadruple(5)}")
