class BalanceException(Exception):
    pass

# Initializing the BankAccount

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance}")

# Get Balance  Methode
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance}")

# Deposite Methode
    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposite Complete")
        self.getBalance()
###

    def ViableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

# Withdraw Methode
    def withdraw(self, amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
                print(f"\n Withdraw interrupted: {error}")
                

##Transfer Methode____
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 👻')
            self.ViableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f"\n Transfer Interrupted: ❌ {error}")
            

class InterestRewardsAcct(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite Complete..")
        self.getBalance()
        
        
class SavingACCT(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5 
    
    def withdraw(self, amount):
        try:
            self.ViableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete..")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")