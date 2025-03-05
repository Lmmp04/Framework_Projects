##!/usr/bin/env python3
## coding: utf-8

"""
    File: arrays.py
    An Array is like a list, but the client can use
    only [], len, iter, and str.
     
    To instantiate, use
    <variable> = Array(<capacity>, <optional fill value>)
     
    The fill value is None by default.

    Fuctions:
        init, len, str, iter, getitem, seittem
    Constants:
        self, capacity, fillvalue, index, Newitem
"""

__author__ = "Leo Platti"
__version__ = "1.0"

# REMEMBER TO PUT IN DETAILED COMMENTS!
capacity = 10
def start():
    class Array(object):
        """Represents an array."""
#creates array with ten positions, and gives capacity a value. Also fills array with 1-10
    def __init__(self):
        """Capacity is the static size of the array. fillValue is placed at each position."""
        self.items = list()
        for count in (1,2,3,4,5,6,7,8,9,10):
            self.items.append(count)
        print(self.items)
        __init__(self.items)
#gets length and returns it
    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)
#gets string content of the actual items in the array and prints it
    def __str__(self):
        print(str(self.items))
#Acceses first item and prints it
    def __iter__(self):
        """Supports traversal with a for loop."""
        print("First Item: ", self)
        return iter(self.items)

#acceses last item and prints it
    def __getitem__(self, index):
        """Subscript operator for access at index."""
        print("Last item: ", self, index)
        return(self,index(10))
#Creates new array, copies old array with new variable
#Sets number 11 into position 2 of the list
    def __setitem__(self, index, newItem):
        self.items.append(self,index,newItem)
#Creating 10x10 grid with two for loops
start()