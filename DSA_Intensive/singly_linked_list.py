#!/usr/bin/python3

"""this script creates a linked lists by creating a class called
Node and instantiating several Node objects to store as a linked list"""


class Node: #creates a node(singular object) of a Linked List
    #data = None #the data
    next_node = None #the reference to the next noe on the list

    def __init__(self, data): #this method is a constructor method for inserting data
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"

class LinkedList:
    """singly linked list"""
    def __init__(self):
        self.head = None #key note here: in a SLL we always point to the head and traverse from that position
    
    def is_empty(self):
        return self.head == None #returns True if it is empty
    
    def size(self):
        """this operation runs in linear time"""
        current = self.head
        count = 0 #size of the list

        while current:
            count += 1
            current = current.next_node
        """returns the number of nodes in the list"""
        return count
    
    def add(self, data):
        """this method creates nodes and adds them at the head of the linked list
        This is a constant time operation"""

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def node_at_idex(self, index):
        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0
            while (position < index):
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """we are creating a string representation of our
        linked list. The out put resembles a visual representation
        of our created linked list"""

        nodes = [] #this is the physical casing of our nodes
        current = self.head #this is the data we are pointing to
        while current:
            if current is self.head: #if the content is the head
                nodes.append(f"[Head: {current.data}]") #append it to the list in this style
            elif current.next_node is None: #if the content is the tail
                nodes.append(f"[Tail: {current.data}]") #print like this
            else:
                nodes.append(f"[{current.data}]") #print every other node on the list

        return "-->".join(nodes)

    def search(self, key):
        """this function searches the SLL and returns the first
        node containing the data that matches the key
        
        Returns None if it is not found
        
        This takes O(n), or linear time"""

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

#proving node creation was a success
n1 = Node(10) #does not work
n2 = Node(20) #does not work

#n1.next_node(n2) #gives reference to a None type

print(n1)
print(n2)

#proving LinkedList creation was a success
l1 = LinkedList() #created a linked list object
N1 = Node(10) #created a node object to add to our LinkedList
l1.head = N1 #setting that first node to be our head
l1.add(1) #adding a new head and rotating our other content
l1.add(2)
l1.add(3)
print(l1.size()) #the current count of our size is 4
print(l1.head) #this prints the data in the head
found_node = l1.search(5)
print(found_node)

#print(repr(l1)) does not print the linked list. Will be back for more
