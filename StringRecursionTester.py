##!/usr/bin/env python3
## coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The StringRecursion class tests different 
# common structures of recursive functions, demonstrating how different
# setups of recursion functions can perform the same computation.
#
# Note:
#   The functions tested all take a string as a parameter.
#
# Functions:
#   main - Mainline for the module
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

from RecursionMethod import *

class StringRecursion:

        def main():    

                print("")  # Print statement 
                print("This a base check of all functions in Recursion Method: ") # Print statement           
                # Create a1
                print(a1.number("")) # Empty string 
                # Create a2
                print(a2.number("A")) # Case A only
                # Create a3
                print(a3.number("B")) # Case no As 
                # Create a4
                print(a4.number("ABC")) # Case 1 A at begining
                # Create a5
                print(a5.number("BCA")) # Case 1 A at end
                # Create a6
                print(a6.number("ABCACB")) # Case A at begining and in middle (exact position not relevant)
                
                print("") # Print statement 
                print("This is with the clearCount method: ") # Print statement 
        
                # Create a7
                print(a7.number2("")) # Empty string 
                # Clear count
                print(a7.number2("A")) # Case A only 
                # Clear count
                print(a7.number2("B")) # Case no As  
                # Clear count
                print(a7.number2("ABC")) # Case 1 A at begining 
                # Clear count
                print(a7.number2("BCA")) # Case 1 A at end 
                # Clear count
                print(a7.number2("ABCACB")) # Case A at begining and in middle (exact position not relevant) 

                #------------------------------------------------------------------------ Optimization begins 
                
                print("") # Print statement 
                print("This is with the counter being manipulated with a static recursive method: ") # Print statement 
                print("The reduction is split into three different parts.") # Print statement 
                print("One for each half of the string, and one for the new combined string.: ") # Print statement 
                
                print(RecursionMethod.number3("")) # Empty string 
                print(RecursionMethod.number3("A")) # Case A only 
                print(RecursionMethod.number3("B")) # Case no As  
                print(RecursionMethod.number3("ABC")) # Case 1 A at begining 
                print(RecursionMethod.number3("BCA")) # Case 1 A at end
                print(RecursionMethod.number3("ABCACB")) # Case A at begining and in middle (exact position not relevant)
                
                print("") # Print statement 
                print("This is with the counter being manipulated in the recursive method.") # Print statement 
                print("The reduction is put on one line.") # Print statement        
                print(RecursionMethod.number4("")) # Empty string
                print(RecursionMethod.number4("A")) # Case A only
                print(RecursionMethod.number4("B")) # Case no As 
                print(RecursionMethod.number4("ABC")) # Case 1 A at begining
                print(RecursionMethod.number4("BCA")) # Case 1 A at end
                print(RecursionMethod.number4("ABCACB")) # Case A at begining and in middle (exact position not relevant)
                
                print("")
                print("This is with the counter being manipulated in the recursive method: ")
                print("The reduction is included in the recursion.")
        
                print(RecursionMethod.number5("")) # Empty string
                print(RecursionMethod.number5("A")) # Case A only
                print(RecursionMethod.number5("B")) # Case no As 
                print(RecursionMethod.number5("ABC")) # Case 1 A at begining
                print(RecursionMethod.number5("BCA")) # Case 1 A at end
                print(RecursionMethod.number5("ABCACB")) # Case A at begining and in middle (exact position not relevant)
                
                print("")
                print("This is with the counter else ommited in the recursive method: ")
                print("The reduction is included in the recursion.")
        
                print(RecursionMethod.number6("")) # Empty string
                print(RecursionMethod.number6("A")) # Case A only
                print(RecursionMethod.number6("B")) # Case no As 
                print(RecursionMethod.number6("ABC")) # Case 1 A at begining
                print(RecursionMethod.number6("BCA")) # Case 1 A at end
                print(RecursionMethod.number6("ABCACB")) # Case A at begining and in middle (exact position not relevant)
              

        if __name__ == "__main__":
                main()
