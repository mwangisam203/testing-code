"""Topic 4: classes and objects."""


class BankAccount:
    def __init__(self, owner, balance=0):
        # Step 1: `__init__` runs when we create a new BankAccount.
        # Step 2: store the starting information on `self`, which means
        # "this specific account object".
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Problem thinking:
        # A deposit should change the account only when the amount makes sense.
        # If the amount is 0 or negative, doing nothing is safer than silently
        # creating a bad balance.
        if amount <= 0:
            print("Deposit ignored: amount must be positive.")
            return

        # `+=` means: take the old balance, add amount, then save it back.
        self.balance += amount

    def withdraw(self, amount):
        # Withdraw thinking:
        # There are two bad cases to guard against before changing the balance.
        # 1. The amount must be positive.
        # 2. The account must have enough money.
        if amount <= 0:
            print("Withdrawal ignored: amount must be positive.")
            return False

        if amount > self.balance:
            print("Withdrawal denied: not enough money.")
            return False

        self.balance -= amount
        return True

    def show_balance(self):
        # This method does not change data; it only displays current state.
        print(f"{self.owner} has ${self.balance:.2f}")


account = BankAccount("Alex", 50)
account.deposit(25)
account.deposit(-10)
if account.withdraw(30):
    print("Withdrawal worked.")
account.show_balance()

# The class is the blueprint; `account` is one object made from it.
# Good class design usually asks:
# 1. What data does this object remember?
# 2. What actions should be allowed?
# 3. What bad inputs should be blocked?
# Returning True/False from a method is useful when the caller needs to know
# whether the action succeeded.
