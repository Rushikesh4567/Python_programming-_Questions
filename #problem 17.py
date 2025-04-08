#problem 17
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
        self.check_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
        self.check_balance()

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

b = BankAccount("Digvijay", 10000)

while True:
    print("\n1. Deposit money\n2. Withdraw money\n3. Exit")
    
    try:
        ch = int(input("Enter your choice: "))

        if ch == 1:
            d = int(input("Enter deposit amount: "))
            b.deposit(d)
        elif ch == 2:
            w = int(input("Enter withdraw amount: "))
            b.withdraw(w)
        elif ch == 3:
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter a number.")
