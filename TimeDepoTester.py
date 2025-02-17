#!/usr/bin/python3

#author - Leo Platti
#Version - 1.0
from SavingsTester import *
from TimeDepositAccount import *

class TimeDepoTester:
#creating main function, and objects, inserting parameters also
    def main():
        depoaccount = TimeDepositAccount(0.005, 1000, 12)
        print(depoaccount.monthNumber)
    #starting for loop, to accurately calculate rate over months
        for month in range(10):
            print(month)
            depoaccount.addInterest(0.005, month)
            print(depoaccount)
    #print statements following balance changes
            depoaccount.withdraw(10)
            print(depoaccount)
    #adding interest and printing balance
            depoaccount.addInterest(0.005, month)
            print(depoaccount)
    #Repeating
            depoaccount.addInterest(0.005, month)
            print(depoaccount)
    #withdrawing 
            depoaccount.withdraw(500)
            print(depoaccount)
    #adding interest
            depoaccount.addInterest(0.005, month)
            print(depoaccount, "dollars")
    #withdraw
            depoaccount.withdraw(1000)
            print(depoaccount)

    if __name__ == "__main__":
        main()