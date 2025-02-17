##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
      A bank account can be of type Savings Account.
   Functions:
      init, addInterest, withdrawals
   Constants:
      self, rate, initialBalance, amount      
"""
from BankAccount import *
from TimeDepositAccount import *
from TimeDepoTester import * 
from SavingsTester import *
from sys import *

__author__ =  "Leo Platti"
__version__ = "1.0" 

class SavingsAccount():

    # Description:
    #    main function, creates objects
    # INPUT:
    #    self, rate, initialBalance
    # OUTPUT
    #    none
    def __init__(self, rate, initialBalance):
        self.rate = rate
        self.balance = initialBalance
   
    # Description:
    #    adds interest to balance, also does calculation of balance and rate, creates object for interest
    # INPUT:
    #    self, rate
    # OUTPUT
    #    none  
    def addInterest(self):
       interest = self.balance * self.rate / 100
       self.balance += interest

    # Description:
    #    used to withdraw and subtract from balance
    # INPUT:
    #    self, amount
    # OUTPUT
    #    none or withdrawal stop message
    #"Withdrawals must stop if the account reaches minimum balance"
    def withdraw(self, amount): 
        a = self.balance - amount
        if a <= self.balance:
            print("Minimum Balance Reached Withdrawals Stopped")