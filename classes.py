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

    def transfer_to(self, other_account, amount):
        # Transfer thinking:
        # A transfer is really two actions that must happen in the right order:
        # 1. Try to withdraw money from this account.
        # 2. If that worked, deposit the same amount into the other account.
        #
        # We reuse `withdraw` and `deposit` instead of rewriting the same
        # validation rules here. Reusing your own methods keeps bugs smaller.
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True

        return False

    def show_balance(self):
        # This method does not change data; it only displays current state.
        print(f"{self.owner} has ${self.balance:.2f}")

    def get_balance(self):
        # Example 2: return data when another part of the program needs it.
        # Printing is for people; returning is for code.
        return self.balance

    def summary(self):
        # Example 3: methods can return formatted text too.
        # This keeps display wording close to the object that owns the data.
        return f"Account(owner={self.owner}, balance=${self.balance:.2f})"


account = BankAccount("Alex", 50)
account.deposit(25)
account.deposit(-10)
if account.withdraw(30):
    print("Withdrawal worked.")
account.show_balance()

savings = BankAccount("Savings", 200)
checking = BankAccount("Checking", 25)

if savings.transfer_to(checking, 75):
    print("Transfer worked.")

savings.show_balance()
checking.show_balance()
print(f"Checking balance as a value: {checking.get_balance()}")
print(checking.summary())

# The class is the blueprint; `account` is one object made from it.
# Good class design usually asks:
# 1. What data does this object remember?
# 2. What actions should be allowed?
# 3. What bad inputs should be blocked?
# Returning True/False from a method is useful when the caller needs to know
# whether the action succeeded.
# Objects become more useful when they can work together, like one account
# transferring money into another account.
