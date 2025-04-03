##!/usr/bin/env python3
## coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The RecursivePosition class contains functions which show different 
# common structures of recursive functions. 
#
# Note:
#   These functions all use integers to complete calculations.
#
# Functions:
#   cheersincrement. cheersdecrement. Cheersdivide. Before. after. beforeandafter
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic, Leo Platti"
__version__ = 1.0 

class RecursivePosition:

    # Description: prints n+3 "idy"s before "Tally ho!"
    #     (In the case of n = 4 or higher, the function only prints "Tally ho!")
    # Parameter: n, integer.  
    # Interval: Increase by 1  
    # Base Case: n must be greater than 3 
    # Note: do not check for data type using if or try-catch - enforce this by using int()     
    def cheersIncrement(n):
        if n > 3:
            print("Tally Ho!")
        else:
            print("idy's")
            RecursivePosition.cheersIncrement(n+1)

                 

    # Description: prints n+1 "idy"s before "Tally ho!"
    #     (In the case of n = 1 or lower, the function only prints "Tally ho!")
    # Parameter: n, integer.  
    # Interval: Decrease by 1  
    # Base Case: n must be less than or eq to 1
    # Note: do not check for data type using if or try-catch - enforce this by using int()     
    def cheersDecrement(n):
        if n <= 1:
            print("Tally Ho!")
        else:
            print("idys")
            RecursivePosition.cheersDecrement(n-1)
               


    # Description: prints n/2 "idy"s before "Tally ho!" (rounded up)
    #     (In the case of n = 0 or lower, the function only prints '"Tally ho!"')
    #     (In the case of n = 3 or lower, the function prints "idy" and '"Tally ho!"')
    # Parameter: n, integer. 
    # Interval: Divide by 2  
    # Base Case: n must be less than or eq to 1 
    # Note: do not check for data type using if or try-catch - enforce this by using int()         
    def cheersDivide(n):
        if n >= 1:
            print("Tally Ho!")
        else:
            print("idys")
            RecursivePosition.cheersDivide(n/2)

    # Parameter: n, integer.
    # Description: Print the number before a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implcit 
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int()
    def before(n):
        print(n)
        if n > 1:
            RecursivePosition.before(n-1)

    # Parameter: n, integer.
    # Description: Print the number after a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implcit 
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int() 
    def after(n):
        if n > 1:
            print(int(n))
        else:
            RecursivePosition.after(n-1)


    # Parameter: n, integer.
    # Description: Print the number before and after a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implcit 
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int()  
    def beforeAndAfter(n):
        print(n)
        if n > 1:
            RecursivePosition.before(n-1)
        print(int(n))

