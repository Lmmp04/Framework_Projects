#!/Bin/Python3
#Author = Leo Platti
#3/30/2025

from Queues import *

def test():
    #setting que object and adding first values for variables
    q = Queue
    q1 = Queue
    q.enqueue(1)
    q.enqueue(2)
    #testing for empty queue
    q.isEmpty()
    #testing peek function
    q.peek()
    #testing dequeue
    q.dequeue(1,3,5)
    questr = str(q)
    #printing to terminal with 1 element as requested
    print(questr)
    #Testing cointains function
    q.contains()
    #Testing function to add to que
    q1.enqueue(5)
    q1.enqueue(4)
    combine = q1 + q
    combine()
    #initiating clear function
    q.clear()