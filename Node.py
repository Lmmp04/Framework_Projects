##By: Christine Mikijanic
## File: LinkedSeq.py, based on DoubleLinkedSeq from edu.colorado.collections
## This is an assignment for students to complete

###############################################################################
# A Node provides a node for a linked list with 
# double data in each node.
#
# Note:
#   Lists of nodes can be made of any length, limited only by the amount of
#   free memory in the heap. But beyond Integer.MAX_VALUE,
#   the answer from listLength is incorrect because of arithmetic
#   overflow. 
#
#
# ChangeLog: Michael Main 
#   (main@colorado.edu)
#            C. Mikijanic
#
# Version
#   January 1, 2024
#
##############################################################################/
class Node:

   ## Invariant of the Node class:
   ##   1. The node's double data is in the instance variable data.
   ##   2. For the final node of a list, the link part is None.
   ##      Otherwise, the link part is a reference to the
   ##      next node of the list. 


   ###
   # Initialize a node with a specified initial data and link to the next
   # node. Note that the initialLink may be the None reference, 
   # which indicates that the new node has nothing after it.
   # Argument: initialData
   #   the initial data of this new node
   # Argument: initialLink
   #   a reference to the node after this new node--this reference may be None
   #   to indicate that there is no node after this new node.
   # Post Condition:
   #   This node contains the specified data and link to the next node.
   ##/   
   def __init__(self, initialData, initialLink=None):
      # Instance variable, will contain data of any type
      # Careful when processing to make sure handling is consistent
      self.data = initialData
      # Pointer to next node in the chain
      self.link = initialLink
   


   ###
   # Modification method to add a new node after this node.   
   # Argument: item
   #   the data to place in the new node
   # Post Condition:
   #   A new node has been created and placed after this node.
   #   The data for the new node is item. Any other nodes
   #   that used to be after this node are now after the new node.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for a new 
   #   Node. 
   ##/
   def addNodeAfter(self, item):  
      #Try
      try: 
         # Create new node and link it to item after self
         # Link self to new node
         self.link = Node(item, self.link)
      # Catch memory error -- issues in storage   
      except MemoryError:
         # Context message
         print("There is insufficient memory for a new Node")
             
   
   
   ###
   # Accessor method to get the data from this node.   
   # Argument: - none
   # Returns
   #   the data from this node
   ##/
   def getData(self):
      #Return contents   
      return self.data
   
   
   
   ###
   # Accessor method to get a reference to the next node after this node. 
   # Argument: - none
   # Returns
   #   a reference to the node after this node (or the None reference if there
   #   is nothing after this node)
   ##/
   def getLink(self):
      # Return the next node or none
      return self.link                                               
    
    
    
   ###
   # Copy a list.
   # Argument: source
   #   the head of a linked list that will be copied (which may be
   #   an empty list in where source is None)
   # Returns
   #   The method has made a copy of the linked list starting at 
   #   source. The return value is the head reference for the
   #   copy. 
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.   
   ##/ 
   def listCopy(source):
      try:
      ## Handle the special case of the empty list.
         if (source is None):
            # No list = None
            return None
            
         ## Make the first node for the newly created list.
         copyHead = Node(source.data, None)
         # Initialize tail pointer, and set to the copy's head
         copyTail = copyHead
         
         ## Make the rest of the nodes for the newly created list.
         while (source.link is not None):
            # Move the source down to the next node in the list
            source = source.link
            # Add a node containing source data onto the copy's tail
            copyTail.addNodeAfter(source.data)
            # Shift the tail pointer down to the new tail
            copyTail = copyTail.link
      # Catch memory space error 
      except MemoryError:
         # Context message
         print("There is insufficient memory for the new list")
      ## Return the head reference for the new list.
      return copyHead
   
   
   
   ###
   # Copy a list, returning both a head and tail reference for the copy.
   # Argument: source
   #   the head of a linked list that will be copied (which may be
   #   an empty list in where source is None)
   # Returns
   #   The method has made a copy of the linked list starting at 
   #   source.  The return value is an
   #   array where the [0] element is a head reference for the copy and the [1]
   #   element is a tail reference for the copy.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.   
   ##/
   def listCopyWithTail(source):
      # Initialize a python list with only two elements, both set to None
      answer = [None] * 2
     
      ## Handle the special case of the empty list.   
      if (source is None):
         return answer ## The answer has two None references .
      # Try
      try: 
         ## Make the first node for the newly created list.
         copyHead = Node(source.data, None)
         # Initialize tail pointer, and set to the copy's head
         copyTail = copyHead
         
         ## Make the rest of the nodes for the newly created list.
         while (source.link is not None):
            # Move the source down to the next node in the list
            source = source.link
            # Add a node containing source data onto the copy's tail
            copyTail.addNodeAfter(source.data)
            # Shift the tail pointer down to the new tail
            copyTail = copyTail.link
         
         
         ## Return the head and tail references.
         # Head
         answer[0] = copyHead
         # Tail
         answer[1] = copyTail
      # Catch memory space error     
      except MemoryError:
         # Context message
         print("Insufficient memory for the new list")
      return answer
   
   
   
   ###
   # Compute the number of nodes in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list
   #   with a None head)
   # Returns
   #   the number of nodes in the list with the given head 
   # Note:
   #   A wrong answer occurs for lists longer than the max value of integers in Python.     
   ##/   
   def listLength(self, head):
      # Set the cursor at the head of the linked list
      cursor = head
      # Start counting at 0
      answer = 0
      # While there is a node in the chain
      while (cursor is not None):
         # Increase number
         answer += 1
         # Move to next node
         cursor = cursor.link
      # Return number of items  
      return answer
   
   

   ###
   # Copy part of a list, providing a head and tail reference for the new copy. 
   # Argument: start/end
   #   references to two nodes of a linked list
   # Argument: copyHead/copyTail
   #   the method sets these to refer to the head and tail node of the new
   #   list that is created
   # @precondition
   #   start and end are non-None references to nodes
   #   on the same linked list,
   #   with the start node at or before the end node. 
   # Returns
   #   The method has made a copy of the part of a linked list, from the
   #   specified start node to the specified end node. The return value is an
   #   array where the [0] component is a head reference for the copy and the
   #   [1] component is a tail reference for the copy.
   # Exception: TypeError
   #   Indicates that start and end are not references
   #   to nodes on the same list.
   # Exception: TypeError
   #   Indicates that start is None.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.    
   ##/   
   def listPart(self, start, end):
      # If a list part exists
      if (start is not None):
         # Initialize a python list with only two elements, both set to None
         answer = [None] * 2
         try:
            ## Make the first node for the newly created list. Notice that this will
            ## cause a TypeError if start is None.
            copyHead = Node(start.data, None)
            # Initialize tail pointer, and set to the copy's head
            copyTail = copyHead
            # Set the cursor to the start of the list part
            cursor = start
            
            ## Make the rest of the nodes for the newly created list.
            while (cursor is not end):
               # Move the cursor down to the next item
               cursor = cursor.link
               # If the cursor is None at this point
               if (cursor is None):
                  # Context message
                  raise TypeError("end node was not found on the list")
               # Add another node onto the copy's tail   
               copyTail.addNodeAfter(cursor.data)
               # Shift the tail pointer to the new tail
               copyTail = copyTail.link
         # Catch memory space error 
         except MemoryError:
            print("Insufficient memory for the new list")
      # Catch the error with an else
      else:
         # Context message
         raise TypeError("start is None")
      
      ## Return the head and tail references
      # Head
      answer[0] = copyHead
      # Tail
      answer[1] = copyTail
      # Return list part copy
      return answer
           
   
   
   ###
   # Find a node at a specified position in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list in
   #   which case the head is None)
   # Argument: position
   #   a node number
   # @precondition
   #   position > 0.
   # Returns
   #   The return value is a reference to the node at the specified position in
   #   the list. (The head node is position 1, the next node is position 2, and
   #   so on.) If there is no such position (because the list is too short),
   #   then the None reference is returned.
   # Exception: TypeError
   #   Indicates that position is not positive.    
   ##/   
   def listPosition(head, position):
      # If the position s not a positive number, generate error
      if (position <= 0):
            # Context message
           print("TypeError: position is not positive")
      # Set the cursor to the head of the list
      cursor = head
      # Create a new index counter
      i = 1
      # While the counter is less than the search position and the cursor is pointing to a node
      while ((i < position) and (cursor is not None)):
         # Move the cursor to the next item
         cursor = cursor.link
         # Increase the counter
         i+= 1
      # Return the cursor which is pointing to the target object
      return cursor
   


   ###
   # Search for a particular piece of data in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list in
   #   which case the head is None)
   # Argument: target
   #   a piece of data to search for
   # Returns
   #   The return value is a reference to the first node that contains the
   #   specified target. If there is no such node, the None reference is 
   #   returned.     
   ##/   
   def listSearch(head, target):
      # Set the cursor to the head of the list 
      cursor = head
      # While the cursor is pointing to a node and the cursor is not pointing at the target
      while(cursor is not None and target is not cursor.data):
         # Move to the next node in the list
         cursor = cursor.link
      # If the node is not there, it will return None, else, return the pointer to the target  
      return cursor
   

   
   ###
   # Modification method to remove the node after this node.   
   # Argument: - none
   # @precondition
   #   This node must not be the tail node of the list.
   # Post Condition:
   #   The node after this node has been removed from the linked list.
   #   If there were further nodes after that one, they are still
   #   present on the list.
   # Exception: TypeError
   #   Indicates that this was the tail node of the list, so there is nothing
   #   after it to remove.
   ##/
   def removeNodeAfter(self):   
      # If there is a subsequent node
      if (self.link is not None):
         # Attach to this node, the one 2 links down
         self.link = self.link.link
      # Catch memory error   
      else:
         # Raise exception, context message
         raise TypeError("Tail node of the list, nothing to remove.")
             
   
   
   ###
   # Modification method to set the data in this node.   
   # Argument: newData
   #   the new data to place in this node
   # Post Condition:
   #   The data of this node has been set to newData.
   ##/
   def setData(self, newData):   
      # Set the contents of a node
      self.data = newData
                                                                  
   
   
   ###
   # Modification method to set the link to the next node after this node.
   # Argument: newLink
   #   a reference to the node that should appear after this node in the linked
   #   list (or the None reference if there is no node after this node)
   # Post Condition:
   #   The link to the node after this node has been set to newLink.
   #   Any other node (that used to be in this link) is no longer connected to
   #   this node.
   ##/
   def setLink(self, newLink):    
      # Set the link of a node         
      self.link = newLink
   

           
