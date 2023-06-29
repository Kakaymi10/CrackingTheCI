"""Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed? 

In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table 
will work well here. 
In the below solution, we simply iterate through the linked list, adding each element to a hash table. When 
we discover a duplicate element, we remove the element and continue iterating. We can do this all in one 
pass since we are using a linked list. """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None
    def prepend(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        new_data.next = self.head
        self.head = new_data
        current = self.head

    def append(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_data
        
    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)
        
    def removeDups(self):
        if self.head == None:
            return
        HashSet = set()
        previous = None
        
        current = self.head
        while current is not None:
            if current.data in HashSet:
                previous.next = current.next
            else:
                HashSet.add(current.data)
                previous = current
                
            current = current.next
            
            
node = LinkedList()
node.append(1)
node.append(2)
node.append(3)
node.append(4)
node.append(1)
node.prepend(7)
node.prepend(2)
node.prepend(4)
node.prepend(8)

node.display()
node.removeDups()
node.display()
