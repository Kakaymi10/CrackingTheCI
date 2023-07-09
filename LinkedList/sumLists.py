'''igit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912. '''

'''Nodes class'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''Linked List class'''
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
            elements.append(str(current.data))
            current = current.next
        print("Linked List:", ('->').join(elements))



'''Sum list function'''
def sumList(a, b):
    current_a = a.head
    current_b = b.head
    num_a = ''
    num_b = ''
    while current_a is not None:
        num_a = str(current_a.data)+num_a
        current_a = current_a.next
    while current_b is not None:
        num_b = str(current_b.data)+num_b
        current_b = current_b.next
        
    sums = str(int(num_a) + int(num_b))
    summedList = LinkedList()
    for i in sums:
        summedList.prepend(int(i))
    return summedList.display()


        
# Example usage:
if __name__ == "__main__":
    linked_listA = LinkedList()
    linked_listA.append(7)
    linked_listA.append(1)
    linked_listA.append(6)
    linked_listA.display()
    
    linked_listB = LinkedList()
    linked_listB.append(5)
    linked_listB.append(9)
    linked_listB.append(2)
    linked_listB.display()
    
    sumList(linked_listA, linked_listB)
