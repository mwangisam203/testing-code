"""Topic 27: mini project - simple budget tracker."""


transactions = [
    {"description": "paycheck", "amount": 800},
    {"description": "groceries", "amount": -95.50},
    {"description": "internet bill", "amount": -60},
    {"description": "coffee", "amount": -4.75},
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


show_transactions(transactions)
balance = calculate_balance(transactions)
print(f"Final balance: ${balance:.2f}")

# Mini-project habit:
# 1. Store data in a simple shape.
# 2. Write one function for one job.
# 3. Print the result in a readable way.
# 4. Improve the project one small feature at a time.
