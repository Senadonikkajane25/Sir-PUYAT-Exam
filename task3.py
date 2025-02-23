class BankAccount:
    def __init__(self,account_number,owner,balance):
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited: ₱{amount}.00 \nNew Balance ₱{self.balance}.00")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw: ₱{amount}.00")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account balance: ₱{self.balance}.00")
        
my_account = BankAccount(987654321, "Bhabyniks", 10500)

my_account.deposit(1500)
my_account.withdraw(1000)
my_account.display_balance()
