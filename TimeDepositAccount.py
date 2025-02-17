##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
      An account where monies are deposited based on time.
   Functions:
      init, addInterest, withdraw, main
   Constants:
      self, rate, initialBalance, monthNumber
"""

__author__ = "Leo Platti"
__version__ = "1.0"

class TimeDepositAccount:
    PENALTY_FEE = 20

    # Description:
    #    main function, used to create objects
    # INPUT:
    #    self, rate, initialBalance, monthNumber
    # OUTPUT
    #    none
    def __init__(self, rate, initialBalance, monthNumber):
        self.rate = rate
        self.initalBalance = initialBalance
        self.monthNumber = monthNumber
    # Description:
    #    function to add interest
    # INPUT:
    #    self, rate
    # OUTPUT
    #    none
    def addInterest(self, rate, initialBalance):
        self = initialBalance * rate

    # Description:
    #    accesses balance of account, and is capable of withdrawing from balance
    # INPUT:
    #    self, amount
    # OUTPUT
    #    "Penalty of (amount) withdrawn"
    def withdraw(self, amount):
        if (amount >= 0):
                self.amount = self.monthNumber - TimeDepositAccount.PENALTY_FEE
                print("Penalty of " + str(TimeDepositAccount.PENALTY_FEE) + " withdrawn.")   

def main(getbalance, rate):
    bob = TimeDepositAccount(.5, 1000.00, 12)
    for i in range(10):
        print(i)
        bob.addInterest(getbalance, rate)
        print("Your balance is " + str(bob.getBalance()))
    bob.withdraw(100)
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()) + " dollars.")
    bob.withdraw(100)
    print("Your balance is " + str(bob.getBalance()))

    if __name__ == "__main__":
        main()