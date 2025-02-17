##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
      A customer has details and has a boat.
   Functions:
      init, setname. set address, setboat. getName, get address, getphone#, getboat
   Constants:
      self
"""

__author__ = "Leo Platti"
__version__ = "1.0"

# You will need to import classes from the Boat file
from Boat import *

class Customer:

	# constructor with parameters
    def __init__(self, aName, anAddress, aPhoneNo):
        # invoke accessors to populate attributes
        self.setName(aName)
        self.setAddress(anAddress)
        self.setPhoneNo(aPhoneNo)
        # initially no Boat
        self.setBoat(None)				 
	
    # set accessors
    def setName(self, newName):
        self.name=newName
        
    def setAddress(self, newAddress):
        self.address=newAddress

    def setPhoneNo(self, newPhoneNo):
        self.phone=newPhoneNo

    def setBoat(self, aBoat):
        self.boat=aBoat

    # get accessors
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhoneNo(self):
        return self.phone
        
    def getBoat(self):
        return self.boat


 
