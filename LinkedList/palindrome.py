'''Palindrome: Implement a function to check if a linked list is a palindrome'''
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
            elements.append(str(current.data))
            current = current.next
        print("Linked List:", ('->').join(elements))

def palindrome(List):
    init = ""
    reverse = ""
    current = List.head
    while current is not None:
        init = current.data + init
        reverse = reverse + current.data
        current = current.next
    print(init == reverse)
        
# Example usage:
if __name__ == "__main__":
    linked_listA = LinkedList()
    linked_listA.append('b')
    linked_listA.append('a')
    linked_listA.append('m')
    linked_listA.append('a')
    linked_listA.append('b')
    linked_listA.display()
    
    palindrome(linked_listA)
