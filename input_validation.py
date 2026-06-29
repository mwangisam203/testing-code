"""Topic 21: input validation."""


raw_age = "19"

# Validation thinking:
# Never trust raw input immediately.
# First check whether it has the shape you expect.
if raw_age.isdigit():
    age = int(raw_age)

    # After converting, check whether the value makes sense for the problem.
    if age >= 18:
        print("You can create an adult account.")
    else:
        print("You need a youth account.")
else:
    print("Age must contain numbers only.")


def get_discount_rate(member_type):
    # Normalize text first so "Student", "student", and " STUDENT "
    # are treated the same.
    cleaned_type = member_type.strip().lower()

    if cleaned_type == "student":
        return 0.20
    if cleaned_type == "senior":
        return 0.15
    if cleaned_type == "regular":
        return 0.00

    # Returning None means "I could not find a valid discount."
    return None


discount = get_discount_rate(" Student ")
if discount is None:
    print("Unknown member type.")
else:
    print(f"Discount: {discount:.0%}")


def is_valid_username(username):
    # Tip: validation rules should be easy to read and easy to change.
    return username.isidentifier() and len(username) >= 3


print(f"Username valid? {is_valid_username('maya_1')}")

# Validation usually has two steps:
# 1. Can this value be converted?
# 2. Does this value make sense for this program?
