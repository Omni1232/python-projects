class Account:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_holder = account_name
        self.balance = balance

    def deposit(self, amount):
        while amount <= 0:
            print("Deposit amount must be positive.")
            amount = float(input("Enter a valid deposit amount: "))
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        while amount <= 0:
            print("Withdrawal amount must be positive.")
            amount = float(input("Enter a valid withdrawal amount: "))
        while amount > self.balance:
            print("Insufficient balance.")
            amount = float(input("Enter a valid withdrawal amount: "))
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def display(self):
        return f"Account Number: {self.account_number},\nAccount Holder: {self.account_holder},\nBalance: {self.balance}"
    
class CurrentAccount(Account):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def withdraw(self, amount):
        print("Current account withdrawl")
        super().withdraw(amount)
            

class SavingsAccount(Account):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def withdraw(self, amount):
        print("Savings account withdrawl")
        super().withdraw(amount)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_type = input("Enter account type (current/savings): ").lower()
        account_number = input("Enter account number: ")
        account_name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))

        if account_type == "current":
            account = CurrentAccount(account_number, account_name, initial_deposit)
        elif account_type == "savings":
            account = SavingsAccount(account_number, account_name, initial_deposit)
        else:
            print("Invalid account type. Account creation failed.")

        self.accounts[account_number] = account
        print(f"Account created successfully for {account_name} with account number {account_number}.")

        def deposit(self):
            account_number = input("Enter account number: ")
            if account_number in self.accounts:
                amount = float(input("Enter deposit amount: "))
                self.accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        def withdraw(self):
            account_number = input("Enter account number: ")
            if account_number in self.accounts:
                amount = float(input("Enter withdrawal amount: "))
                self.accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        def display_balance(self):
            account_number = input("Enter account number: ")
            if account_number in self.accounts:
                balance = self.accounts[account_number].display()
                print(f"Current balance for account {account_number}: {balance}")
            else:
                print("Account not found.")

bank = Bank()

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Display Balance\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.deposit()
    elif choice == '3':
        bank.withdraw()
    elif choice == '4':
        bank.display_balance()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

