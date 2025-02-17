##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Description:
      A service record contains details about the customer and boat.
   Functions:
      init, printform(), getinvoice, getservicedate, getserviceType, getTotalCharges
   Constants:
      invoice #, service date, service type, boat info, total charge

"""

__author__ = "Leo Platti"
__version__ = "1.0"

# You will need to import classes from the Boat and Customer file
from Boat import *
from Customer import * 
 

#Creating class for boats records
class BoatServiceRecord:
    
    def __init__(self, theInvoiceNumber,theServiceDate, theServiceType, theTotalCharges, aBoat):
        self.invoiceNumber = theInvoiceNumber
        self.theServiceDate = theServiceDate
        self.theServiceType = theServiceType
        self.theTotalCharges = theTotalCharges
        self.boat = aBoat
        aBoat.addServiceRecord(self)
        
#creating way to display information of boats while also keeping them attatched to an object
    def printForm(self):
            print("The invoice number is: " + str(self.InvoiceNumber))
            print("The service date is is: " + str(self.serviceDate))
            print("The service type is: " + str(self.serviceType))
            print("The boat information is: " + str(self.boat.tellAboutSelf()))         
            print("The total charge is: " + str(self.totalCharges))
		
#Pulling information and setting self to the actual object we want to call on
    def getInvoiceNumber(self, theInvoiceNumber):    
        return self.invoiceNumber == theInvoiceNumber
    def getServiceDate(self, theServiceDate):
        return self.theServiceDate == theServiceDate
    def getServiceType(self, theServiceType):
        return self.theServiceType == theServiceType
    def getTotalCharges(self, theTotalCharges):
        return self.theTotalCharges == theTotalCharges
	   


