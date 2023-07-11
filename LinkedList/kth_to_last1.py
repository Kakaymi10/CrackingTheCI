'''Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
pg223 
SOLUTION 
We will approach this problem both recursively and non-recursively. Remember that recursive solutions are 
often cleaner but less optimal. For example, in this problem, the recursive implementation is about half the 
length of the iterative solution but also takes 0( n) space, where n is the number of elements in the linked 
list. 
Note that for this solution, we have defined k such that passing ink = 1 would return the last element, k 
2 would return to the second to last element, and so on. It is equally acceptable to define k such that k 
= 0 would return the last element. '''

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


def kth_to_last_iterative(head, k):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    if k > count:
        return None

    curr = head
    for i in range(count - k):
        curr = curr.next

    return curr.data





if __name__ == "__main__":
    linked_listA = LinkedList()
    linked_listA.append(7)
    linked_listA.append(1)
    linked_listA.append(6)
    linked_listA.append(8)
    linked_listA.append(9)
    linked_listA.append(10)
    linked_listA.display()

    print(kth_to_last_iterative(linked_listA.head, 2))
