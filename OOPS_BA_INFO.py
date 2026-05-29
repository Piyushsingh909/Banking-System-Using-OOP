from BankACCOUNT import *

PIYUSH = BankAccount(5000,"Piyush")
MANGAL = BankAccount(10000,"Mangal")


PIYUSH.getBalance()
MANGAL.getBalance()

PIYUSH.deposite(800)


PIYUSH.withdraw(100)


PIYUSH.transfer(200, MANGAL)
PIYUSH.getBalance()

Jim = InterestRewardsAcct(3000, "Jim")
Jim.getBalance()
Jim.deposite(100)
Jim.transfer(100, PIYUSH)


ANI = SavingACCT(7000, "ANI")
ANI.getBalance()
ANI.deposite(100)
ANI.transfer(10000, MANGAL)