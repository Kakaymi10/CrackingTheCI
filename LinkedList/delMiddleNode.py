'''Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but 
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
that node. 
EXAMPLE 
lnput:the node c from the linked lista->b->c->d->e->f 
Result: nothing is returned, but the new linked list looks like a->b->d->e->f 
'''

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

            
    def delMiddleNode(self, data):
        if self.head.data == data:
            return
        current = self.head
        previous = None
        while current.next is not None:
            if current.data == data:
                previous.next = current.next
            else:
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
    linked_list.delMiddleNode(2)
    linked_list.delMiddleNode(1)
    linked_list.display()
