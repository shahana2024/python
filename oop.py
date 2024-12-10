class BankAccount:
    def __init__(self,acc_no,name,acc_type,balance):
        self.account_number=acc_no
        self.name=name
        self.account_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        if amount <= 0:
            print("deposit amount must be positive!")
        else:
            self.balance+=amount
            print(f"deposited:{amount}")
            print(f"updated balance:{self.balance}")
    def withdraw(self,amount):
        if amount <= 0:
            print("withdravel amount must be positive")
        elif self.balance < amount:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print(f"withdraw:{amount}")
            print(f"updated balace:{self.balance}")
    def display(self):
        print("account details:")
        print(f"account number:{self.account_number}")
        print(f"account holder:{self.name}")
        print(f"account type:{self.account_type}")
        print(f"account balance:{self.balance}")
acc_no=int(input("enter the account number:"))
name=input("enter the account holder name:")
acc_type=input("enter the account type:")
balance=int(input("enter initial balance"))
account=BankAccount(acc_no,name,acc_type,balance)
account.display()
deposit_amount=int(input("enter the amount to deposit:"))
account.deposit(deposit_amount)
withdraw_amount=int(input("enter the amount to withdraw"))
account.withdraw(withdraw_amount)

