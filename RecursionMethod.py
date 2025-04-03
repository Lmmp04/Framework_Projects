##!/usr/bin/env python3
## coding: utf-8
##By: Professor Mikijanic

###############################################################################
# This class is a lab assignment.
# The RecursionMethod class contains functions which show different 
# common structures of recursive functions, demonstrating how different
# setups of recursion functions can perform the same computation.
# The function is simplified/compressed until there are only 3 lines of code.
#
# Note:
#   These functions all take a string as a parameter.
#   These functions all use integers internally to complete calculations.
#
# Functions:
#   init, clearcount, number, number2, number2_call, number3, number4, number5 number6
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

class RecursionMethod:

    """
    Description: Consructor for the RecursionMethod class
    Parameters: self
    Notes: One instance variable, called count. 
    Count will be used throughout RecursionMethod.
        Initially, count is set to 0.
    """ 
    def __init__(self):
        count = 0

    """
    Description: Mutator method for the RecursionMethod class
    Parameters: self
    Notes: Resets count to 0.
    """   
    def clearCount(self):
        count = 0




    #------------------------------------------------------------------------ Most readable methods




    
    """
    Description: Most readable form of the recursive method.
    Parameters: self, (string) s
    Returns: (integer) self.count
    Notes: Takes in a string, and parses the string so that 
        it can be broken down and counted.
    """
    def number(self, s):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        if s[0:1] == "A":
            self.count += 1
        if len(s) != 1:
            return self.count
        # If the section of the string from 0 to 1 
        # is equal to "A"
            # Increase self.count by 1 
        # If the length of s is not equal to 1         
            # Call self.number with the parameter of the string,
            # from 1 to the length of s
        # Return self.count    



    """
    Description: Takes in a string s, uses a helper function
    Parameters: self, (string) s
    Returns: (integer) self.count
    Notes: Takes in a string, and parses the string so that 
        it can be broken down and counted.
        """ 
    def number2(self, s):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        return self.number2(self,s)
        
    


    """
    Description: Helper function for number2
    Parameters: self, (string) s, aNumber
    Returns: (integer) self.count
    Notes: Takes in a string, and parses the string so that 
        it can be broken down and counted.
    """ 
    def number2_call(self, s, aNumber):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        if s == None:
            return aNumber
        if s[0:1] == "A":
            
            
            # Return aNumber
        # If the section of the string from 0 to 1 
        # is equal to "A"    
            # Increment aNumber by 1           
        # Return self.number2_call with the parameters: 
        # string section of s from 1 to length of s
        # and aNumber




    #------------------------------------------------------------------------ Optimization begins 




    """
    Description: Third version of the counting function,
       a 'static' function that is called via the class.
    Parameters: (string) s
    Returns: (integer) 
    Notes: Takes in a string, and parses the string so that 
      it can be broken down and counted. 
    """
    def number3(self):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        # If "A" is not in s or the length of s equal to 0
            # Return 0
        # Else
            # a equals the section of s [0 to s.index of "A"]
            # b equals the section of s [s.index of "A" plus 1 to lenght of s]
            # s equals a plus b
            # Return 1 plus RecursionMethod.number3, with the parameter of s
                 

    """
    Description: Fourth version of the counting function,
       a 'static' function that is called via the class.
       Compression has reached 5 lines.
    Parameters: (string) s
    Returns: (integer) 
    Notes: Takes in a string, and parses the string so that 
      it can be broken down and counted. 
    """
    def number4(self):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        # If "A" is not in s or the length of s equal to 0
            # Return 0
        # Else  
            "Note: The line below has been completed (remove this comment)"  
            # s equals:
            # subsection of s, from 0 to the index of "A" plus...
            # subsection of s, from index of "A" plus one to length of s
            s = s[0: s.index("A") ] + s[s.index("A") + 1: len(s)]
            # Return 1 plus RecursionMethod.number4 with the parameter of s
            "Return statement has not been completed..."



    """
    Description: Fifth version of the counting function,
       a 'static' function that is called via the class.
       Compression has reached 4 lines.
    Parameters: (string) s
    Returns: (integer) 
    Notes: Takes in a string, and parses the string so that 
      it can be broken down and counted. 
    """        
    def number5(self):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
        # If "A" is not in s or the length of s equal to 0
            # Return 0
        # Else    
            "Note: The section below has been completed (remove this comment)"
            # One line call --            
            # Return:
            # One plus a call to the RecursionMethod.number5 with the parameters of...
            # subsection of s, from 0 to the index of "A" plus...
            # subsection of s, from index of "A" plus one to length of s            
            return 1 + RecursionMethod.number5(s[0: s.index("A") ] + s[s.index("A") + 1: len(s)]) 



    """
    Description: Sixth version of the counting function,
       a 'static' function that is called via the class.
       Compression has reached 3 lines.
    Parameters: (string) s
    Returns: (integer) 
    Notes: Takes in a string, and parses the string so that 
      it can be broken down and counted. 
    """                 
    def number6(self):
        "Question marks need to be filled, and pseudocode needs to be translated into python code..."
       
        # If "A" is not in s or the length of s equal to 0
            # Return 0
            return 0
        "Note: The section below has been completed (remove this comment)"
        # Fall through the if to the one line call, no else needed based on program flow --
        # Return:
        # One plus a call to the RecursionMethod.number5 with the parameters of...
        # subsection of s, from 0 to the index of "A" plus...
        # subsection of s, from index of "A" plus one to length of s              
        return 1 + RecursionMethod.number6(s[0: s.index("A") ] + s[s.index("A") + 1: len(s)] )   
