class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdraw amount!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# 🔹 Testing
account1 = BankAccount("Shrutika", 5000)
account1.deposit(1000)
account1.withdraw(2000)
account1.display_balance()
