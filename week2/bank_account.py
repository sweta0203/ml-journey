class BankAccount:
    bank_name = "Python National Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"${amount:.2f} deposited into {self.owner}'s account.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"${amount:.2f} withdrawn from {self.owner}'s account.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (
            f"BankAccount(Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f})"
        )


account1 = BankAccount("John", 1000)
account2 = BankAccount("Alice", 2500)
account3 = BankAccount("Bob", 500)

print(account1)
print(account2)
print(account3)

account1.deposit(300)
account2.withdraw(700)
account3.withdraw(900)

print()

print(account1)
print(account2)
print(account3)
