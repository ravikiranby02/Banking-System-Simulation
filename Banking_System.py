class Account:
    def __init__(self,acc_no,holder_name):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = 0

    def deposit(self,amount):
        if amount >0:
            self.__balance += amount
            print(f"Deposited Successfully. Updated Balance {self.__balance}")
        else:
            print("Invalacc_no input")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw successfully. Updated Balance {self.__balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Account Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


class SavingAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.4
        interest = INTEREST_RATE * self.get_balance()
        print(f"Intrest: {interest}")

class CurrentAccount(Account):
    def withdraw(self, amount):
        OVERDRAFT_LIMIT = 1000
        if amount <= self.__balance + OVERDRAFT_LIMIT:
            self.__balance -= amount
            print(f"Withdraw Successfully. Updated Balance {self.__balance}")
        else:
            print("Ask is over limit")

class Bank:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.__account  = {}

    def create_account(self,acc_no,holder_name,type):
        if type == "Saving":
            new_account = SavingAccount(acc_no,holder_name)
        elif type == "Current":
            new_account = CurrentAccount(acc_no,holder_name)
        self.__account[acc_no] = new_account
        print("Account created successfully")
        return new_account
    
    def get_account(self,acc_no):
        if acc_no  not in self.__account:
            print("Accout not found")
            return None
        else:
            account = self.__account[acc_no]
            print(f"Account acc_no: {account.acc_no}\nHolder_Name: {account.holder_name}")
            return account


def menu():
    print("\n=====Bankind  System  Menu=====")
    print()
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Calculate Interest (Saving Account Only)")
    print("6. Show Account Details")
    print("7. Exit")

bank = Bank("RKBI","K R Nagara")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_no = int(input("Enter your acc_no number: "))
        holder_name = input("Enter your name: ")
        type = input("Enter the type (Saving/Current): ")
        bank.create_account(acc_no,holder_name,type)

    elif choice == 2:
        acc_no = int(input("Enter Account acc_no: "))
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)

    elif choice == 3:
        acc_no = int(input("Enter your acc_no Number: "))
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)

    elif choice == 4:
        acc_no = int(input("Enter your acc_no Number: "))
        acc = bank.get_account(acc_no)
        if acc:
            acc.check_balance()

    elif choice == 5:
        acc_no = int(input("Enter your acc_no Number: "))
        acc = bank.get_account(acc_no)
        if isinstance(acc,SavingAccount):
            acc.calculate_interest()
        else:
            print("Interest calculation is only for Saving Accounts.")

    elif choice == 6:
        acc_no = int(input("Enter your acc_no Number: "))
        bank.get_account(acc_no)

 
    elif choice == 7:
        print("Thank you for using the Bank System!")
        break

    else:
        print("Invalacc_no choice. Please try again.")