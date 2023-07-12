'''Partition: Write code to partition a linked list around a value x, such that all nodes less than x come 
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need 
to be after the elements less than x (see below). The partition element x can appear anywhere in the 
"right partition"; it does not need to appear between the left and right partitions. 
EXAMPLE 
Input: 
Output: 
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5] 
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8'''


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
    
def partition(Llist, data):
    before_linked = LinkedList()
    after_linked = LinkedList()
    current = Llist.head
    while current is not None:
        if current.data < data:
            before_linked.append(current.data)
        else:
            after_linked.append(current.data)
        current = current.next

    afte_curr = after_linked.head
    while afte_curr is not None:
        before_linked.append(afte_curr.data)
        afte_curr = afte_curr.next
    
    return(before_linked.display())

if __name__ == "__main__":
    linked_listA = LinkedList()
    linked_listA.append(7)
    linked_listA.append(1)
    linked_listA.append(6)
    linked_listA.append(8)
    linked_listA.append(2)
    linked_listA.append(3)
    linked_listA.append(4)
    linked_listA.append(5)
    linked_listA.display()
    
    partition(linked_listA, 5)
