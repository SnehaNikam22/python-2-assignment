# to create a class of named bankAccount :
class bankAccount:
    def __init__(self,account_number,balance=0):      # taking the formal parameters
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount) :                       # taking the actual parameters for the deposite
        if amount > 0 :
            self.balance += amount 
            print(f"deposited Rs{amount}. New balance: Rs{self.balance}")
        else :
            print("Invalid deposite amount.")

    def withdraw (self,amount):                        # taking actual parameter for withdrwal 
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrawn Rs{amount}. New balance: Rs{self.balance}")

    def check_balance(self):                            # checking the bank balance
        print (f"account balance: Rs{self.balance}")

# creating the object

print("total summary of your account:")
account = bankAccount(2000,500)
account.deposit(400)
account.withdraw(200)
account.check_balance()