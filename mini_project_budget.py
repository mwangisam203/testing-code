"""Topic 27: mini project - simple budget tracker."""


transactions = [
    {"description": "paycheck", "amount": 800, "category": "income"},
    {"description": "groceries", "amount": -95.50, "category": "food"},
    {"description": "internet bill", "amount": -60, "category": "bills"},
    {"description": "coffee", "amount": -4.75, "category": "food"},
]


def calculate_balance(items):
    # Project thinking:
    # Start with the smallest useful question:
    # "Given a list of transactions, what is the final balance?"
    balance = 0

    for item in items:
        balance += item["amount"]

    return balance


def show_transactions(items):
    # Separate display logic from calculation logic.
    # That keeps each function easier to understand.
    for item in items:
        amount = item["amount"]

        if amount >= 0:
            label = "income"
        else:
            label = "expense"

        print(f"{item['description']}: ${amount:.2f} ({label})")


def total_by_category(items):
    # Deeper project thinking:
    # A balance answers "How much money is left?"
    # Category totals answer "Where did the money go?"
    totals = {}

    for item in items:
        category = item["category"]

        # If this category is new, start it at 0 before adding to it.
        if category not in totals:
            totals[category] = 0

        totals[category] += item["amount"]

    return totals


show_transactions(transactions)
balance = calculate_balance(transactions)
print(f"Final balance: ${balance:.2f}")

category_totals = total_by_category(transactions)
print("Totals by category:")
for category, amount in category_totals.items():
    print(f"- {category}: ${amount:.2f}")

# Mini-project habit:
# 1. Store data in a simple shape.
# 2. Write one function for one job.
# 3. Print the result in a readable way.
# 4. Improve the project one small feature at a time.
# This is how projects grow: first make it work, then ask a better question.
