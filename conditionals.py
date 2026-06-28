"""Topic 5: conditionals and comparison order."""


temperature = 28

# Conditional thinking:
# Start with the most specific or strict condition first.
# If we checked `temperature >= 20` before `temperature >= 30`,
# then 35 would be called "warm" and Python would never reach "hot".
if temperature >= 30:
    message = "It is hot."
elif temperature >= 20:
    message = "It is warm."
else:
    message = "It is cold."

print(message)

has_umbrella = True
is_raining = True

# Combining conditions:
# `and` means both sides must be True.
# This reads like plain English: if it is raining and we have an umbrella...
if is_raining and has_umbrella:
    print("Walk outside with the umbrella.")
elif is_raining and not has_umbrella:
    print("Wait or find cover.")
else:
    print("Enjoy the weather.")


def can_enter_event(age, has_ticket):
    # Early-return thinking:
    # Instead of nesting many `if` blocks, handle each rejection first.
    # Once a return happens, the function stops immediately.
    if age < 18:
        return "Denied: must be at least 18."

    if not has_ticket:
        return "Denied: ticket required."

    return "Allowed: enjoy the event."


print(can_enter_event(20, True))
print(can_enter_event(16, True))


def shipping_cost(order_total):
    # Example 2: conditionals often encode business rules.
    # Put the most generous/specific rule first so it wins immediately.
    if order_total >= 100:
        return 0

    if order_total >= 50:
        return 5

    return 10


print(f"Shipping: ${shipping_cost(72)}")


def letter_grade(score):
    # Example 3: grade boundaries are another place where order matters.
    # Check from highest to lowest so each score lands in the right bucket.
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"

    return "F"


print(f"Grade: {letter_grade(87)}")

# Python stops at the first condition that is True.
# A useful pattern is:
# 1. Handle the strongest case.
# 2. Handle the next case.
# 3. Use `else` for everything left over.
# Use `and`, `or`, and `not` when one decision depends on multiple facts.
# Early returns are useful when you want to avoid a staircase of nested code.
