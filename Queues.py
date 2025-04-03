##!/usr/bin/env python3
## coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The Queue class creates a queue structure that can be used to perform
# basic queueing tasks. It uses Linked List nodes as the base. 
#
# Note:
#   Lists of nodes can be made of any length, limited only by the amount of
#   free memory in the heap. 
#
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "Leo Platti"
__version__ = 90000000

from Node import *

class Queue:

    ###
    # Initialize an empty queue.
    # Argument: 
    #   None
    # Postcondition:
    #   Queue created, this queue is empty.
    # Exception: MemoryError
    #   Indicates insufficient memory for the new queue.    
    ### 

    def __init__(self):
        try:
            self.head = None                                                                                
            self.tail = None
        except MemoryError:
            print("Insufficient memory for a new Queue.")


    ###
    # Add a new element to the queue.
    # Argument: 
    #    data - the element data to be added
    # Postcondition:
    #   Queue has been increased by one item.
    # Exception: MemoryError
    #   Indicates insufficient memory for the new sequence.    
    ### 
    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.link = Node(data)
            self.tail = self.tail.link
    ###
    # Remove an element from the queue.
    # Argument: 
    #    None
    # Postcondition:
    #   Queue has been decreased by one item.
    # Exception: TypeError
    #   Indicates that there is no elements, so 
    #   dequeue may not be called.    
    ### 
    def dequeue(self):
        self.head = self.head.link
        self.tail = self.head

    

    ###
    # Check to see if the queue is empty.
    # Argument: 
    #    None
    # Returns:
    #   True/False - if the queue is empty or not.
    ### 
    def isEmpty(self):
        if self == None:
            return True
        else:
            return False

    ###
    # Print out a string representation of the queue
    # Argument: 
    #    None
    # Returns:
    #   A string containing all of the elements in the queue
    ### 
    def __str__(self):
        stryng = ""
        cursor = self.head
        while cursor != None:
            cursor = cursor.link
        toprint = stryng, + cursor
        print(toprint)

    ###
    # Check to see if the queue is empty.
    # Argument: 
    #    None
    # Returns:
    #   True/False - if the queue is empty or not.
    ### 
    def contains(self, target):
        if self == target:
            return True
        else:
            return False

    ###
    # Remove an element from the queue.
    # Argument: 
    #    None
    # Returns:
    #   The data in the head element.
    ### 
    def peek(self):
        self.head = self.head.link

    ###
    # Add a new element to the queue.
    # Argument: 
    #    data - the element data to be added
    # Returns:
    #    a new queue item.
    # Exception: TypeError
    #   One of the arguments is None.  
    # Exception: MemoryError
    #   Insufficient memory to create a new sequence.   
    ### 
    def __add__(self, q2):
        self.tail.link = q2.head
        self.tail = q2.tail




    ###
    # Remove all elements from the queue
    # Argument: 
    #    None
    # Postcondition:
    #   All elements have been removed. 
    ### 
    def clear(self):  
        self.head = None
        self.tail = None      
