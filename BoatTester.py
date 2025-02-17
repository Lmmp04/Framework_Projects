##!/usr/bin/env python
## coding: utf-8

##!/usr/bin/env python3

""""
   Tester for the boat class   
"""

__author__ = "Leo Platti"
__version__ = "1.0"

from Boat import *
from Customer import *
from BoatServiceRecord import *

#Actual class which tests and pulls information from different scripts to make sure the code all runs properly

class BoatTester:

    firstCustomer = Customer("Eleanor", "Atlanta", "123-4567")
    firstBoat = Boat("MO34561", 28, "Tartan", 2002, firstCustomer)				
   
    a = BoatServiceRecord( 1, "Jan 21, 2010", "Engine repair", 1000.00, firstBoat)
    b = BoatServiceRecord( 2, "Jan 31, 2010", "Paint Stripping", 600.00, firstBoat)
   
    firstBoat.printRecord()