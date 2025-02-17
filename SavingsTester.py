##!/usr//bin/python3

#author - Leo Platti
#Version - 1.0

from SavingsAccount import *

class SavingsAccountTester:
#class for Tester, creates bank acct object with a balance of 1000
    def main():
        Bank = BankAccount(1000)
    #doing balance changes and printing balance after
        print("Balance is", Bank.getBalance)
        Bank.deposit(4000)
        print(Bank.getBalance)
        Bank.withdraw(1000)
        print(Bank.getBalance)
        Bank.deposit(5000)
        print(Bank.getBalance)
        Bank.withdraw(5000)
        print(Bank.getBalance)
        print("_________________")
    #creating savings object
        saving = SavingsAccount(0.005, 1000)
        saving.balance
        saving.addInterest()
        saving.withdraw(1000)
        saving.withdraw(-1000)
        print("Deposited $1000)")
        saving.withdraw(-1000)
        print("Deposited $1000")
        saving.withdraw(1000)
        saving.addInterest()
        saving.withdraw(3000)
        saving.withdraw(3000)

        if __name__ == "__main__":
            main()

    



    

    