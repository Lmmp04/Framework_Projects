##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
        A bank account has a balance that can be changed by 
        deposits and withdrawals.
   Functions:
      init, init, withdraw, deposit, getBalance
   Constants:
      self, initialBalance, amount  
"""

from SavingsAccount import *
from TimeDepositAccount import *
from TimeDepoTester import * 
from SavingsTester import *

__author__ =  "Leo Platti"
__version__ =  "1.0"

class BankAccount():
  
    #Constructs a bank account with a zero balance.
    # INPUT:
    #    self
    # OUTPUT
    #    none
    def __init__(self):
        self.balance = 0
    

    #Constructs a bank account with a given balance.
    # INPUT:
    #    self, initialBalance
    # OUTPUT
    #    none
    def __init__(self, initialBalance):
        self.initialBalance = initialBalance
    

    #Deposits money into the bank account.
    # INPUT:
    #    self, amount
    # OUTPUT
    #    none
    def deposit(self, amount):    
        self.amount = amount
    

    #Withdraws money from the bank account.
    # INPUT:
    #    self, amount
    # OUTPUT
    #    none
    def withdraw(self, amount): 
        self.amount = amount
        


    #Gets the current balance of the bank account.
    # INPUT:
    #    self
    # OUTPUT
    #    prints current balance
    def getBalance(self, amount):
        print(amount)
        return(amount)


    