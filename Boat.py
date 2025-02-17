##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
      A boat is owned by a customer and has related details attached.
   Functions:
      init, tellAboutSelf, AssignBoattoCustomer, printrecord, setstateregistration, getlength, setyear, getserviceregistration,  setlength, setmanufacturer, setcustomer,  getyear, getmanufacturer
   Constants:
      self, AStateRegistration, ALength, Ayear, AManufacturer, Acustomer
"""

__author__ = "Leo Platti"
__version__ = "1.0"

from Customer import *
from BoatServiceRecord import *

class Boat:

    # Description:
    #    A boat, with attributes "self, state registration, length, manufcaturer,year and customer"
    # INPUT:
    #    state registration, length, manufacturer, year
    # OUTPUT
    #   none
    def __init__(self, aStateRegistrationNo, aLength, aManufacturer, aYear, aCustomer):
    
        # You will need to save the data that is being passed to the function
        # in variables that can be accessed throughout the class
        self.setStateRegistrationNo(aStateRegistrationNo)
        self.setLength(aLength)
        self.setManufacturer(aManufacturer)
        self.setYear(aYear)
        # association between boat and customer done here
        self.assignBoatToCustomer(aCustomer)
        self.serviceRecord = []      
    
    # Description:
    #    Used to display information after input for boat
    # INPUT:
    #    String pulled from arguments from the function above that describe said boats (init)
    # OUTPUT
    #    string stating information about the boats
    def tellAboutSelf(self):
    
        boatDetails = "I am a Boat" +\
            " state reg number " + str(self.getStateRegistrationNo()) +\
            " length " + str(self.getLength()) +\
            " Manufacturer " + str(self.getManufacturer()) +\
            " Year " + str(self.getYear())
        customerDetails = "\n and Owner is " + str(self.customer.getName()) +\
            " living in " + str(self.customer.getAddress()) +\
            " with phone " + str(self.customer.getPhoneNo())
        return boatDetails + customerDetails
    
    # Description:
    #    Function to assign a particular boat to a customer via name
    # INPUT:
    #    self, aCustomer
    # OUTPUT
    #    none    
    def assignBoatToCustomer(self, aCustomer):
        self.customer = aCustomer
    
    
    # Description:
    #    Pulling service record from file
    # INPUT:
    #    self, record
    # OUTPUT
    #   writes/appends record
    def addServiceRecord(self, record):
        self.serviceRecord.append(record)
     
    # Description:
    #    Print out records pulled from other files
    # INPUT:
    #    self, record
    # OUTPUT
    #    prints record     
    def printRecord(self):
        for i in self.serviceRecord:
            BoatServiceRecord.self.printForm()
                
    # Description:
    #    Function to set the state registration number
    # INPUT: 
    #    self, aStateRegistrationNo
    # OUTPUT
    #   none  
    def setStateRegistrationNo(self, aStateRegistrationNo):
        self.stateRegistrationNo = aStateRegistrationNo

    # Description:
    #    function to set the length
    # INPUT:
    #    self, aLength
    # OUTPUT
    #    none
    def setLength(self, aLength):
        self.length = aLength

    # Description:
    #    function to set manufacturer name
    # INPUT:
    #    self, aManufacturer
    # OUTPUT
    #    none
    def setManufacturer(self, aManufacturer):
        self.manufacturer = aManufacturer

    # Description:
    #    Function to set year of boat model
    # INPUT
    #    self, aYear
    # OUTPUT
    #    none
    def setYear(self, aYear):
        self.year = aYear

    # Description:
    #    Function to set customers name via string
    # INPUT:
    #    self, Acustomer
    # OUTPUT
# none
    def setCustomer(self, aCustomer):
        self.customer = aCustomer



    def getStateRegistrationNo(self):
        return self.stateRegistrationNo 
    def getLength(self):
        return self.length 
    def getManufacturer(self):
        return self.manufacturer 
    def getYear(self):
        return self.year 
    def getCustomer(self):
        return self.customer 
 