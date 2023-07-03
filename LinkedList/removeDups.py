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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

    def remove_duplicates(self):
        if self.head is None:
            return
        data_set = set()
        previous = None
        current = self.head
        while current is not None:
            if current.data in data_set:
                previous.next = current.next
            else:
                data_set.add(current.data)
                previous = current
            current = current.next

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.prepend(4)
    linked_list.display()
    linked_list.remove_duplicates()
    linked_list.display()
