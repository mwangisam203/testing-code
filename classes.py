"""Topic 4: classes and objects."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.balance:.2f}")


account = BankAccount("Alex", 50)
account.deposit(25)
account.show_balance()

# The class is the blueprint; `account` is one object made from it.
