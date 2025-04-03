##!/usr/bin/env python3
## coding: utf-8

from sys import version
from math import sqrt

"""
    File: PostfixDouble.py
    Description: 
        File that creates a stack, adds to and removes from stack, can select and do math with stack inputs as well"
    Fuctions:
        init. infixeqtopostfix, push, divide, subtract, conversion, power, powersuper,negative,square
    Constants:
        self, data, a, b, n, convert
"""

__author__ = "Leo Platti"
__version__ = "1.0"

# Prints the system's version of the Python to the terminal for programer checking.
# Switch statements were put in Python 3.10 - this file is 
#   backwards compatible. It must run on earlier versions of Python.
print(version)

class PostfixDouble:
    
    def __init__(self, data):
        self.operands = []
        self.postfix = data.replace("\n", "")


    def infixEquationToPostfix(self):   
        print("The value of [" + self.postfix + "] is ", end = "")
        express = self.postfix
        fullNumber = None
        if(len(self.postfix) <= 0):
            print("The postfix can not be less than 1")
        else:
            while:
                if +:
                    self.operands.pop()
                    
                if -:
                    subtract
            return 
        
#adding onto stack
    def push(self,a):
        self.operands.append(a)
#dividing two items from stack
    def divide(a, b):
        return a/b

#subtracting two items from stack
    def subtract(a, b):
        return a-b

#converting capabilities for int to str or operand to int
    def conversion(self, convert):

        if (convert == None):
            print("The string is None.")
        else: 
            return int(self)

    def power(a, b):
        if a == 0:
            print("Error zero as value")
        else:
            PostfixDouble.powerSuper(a,b)


#Helper function used on function above
    def powerSuper(x, n):
        return x**n


    def negative(a):
        return -a


    def square(a):
        return a**2

