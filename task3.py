class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount % 100 == 0 and 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid amount. Withdrawals must be in hundreds and within balance.")

    def display_balance(self):
        print(f"Account {self.account_number} owned by {self.owner} has a balance of ${self.balance:.2f}")

# Creating a bank account
account = BankAccount("123456789", "Nikka Jane Senado", 500.00)

while True:
    print("\nOptions: deposit, withdraw, balance, exit")
    action = input("Choose an option: ").strip().lower()
    
    if action == "deposit":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw (hundreds only): "))
        account.withdraw(amount)
    elif action == "balance":
        account.display_balance()
    elif action == "exit":
        print("Exiting. Have a great day!")
        break
    else:
        print("Invalid option. Please try again.")
