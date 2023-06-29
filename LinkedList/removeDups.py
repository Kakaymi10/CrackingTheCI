"""Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed? 

In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table 
will work well here. 
In the below solution, we simply iterate through the linked list, adding each element to a hash table. When 
we discover a duplicate element, we remove the element and continue iterating. We can do this all in one 
pass since we are using a linked list. """

def delete_duplicates(head):
    if head is None:
        return

    seen_values = set()
    previous = None
    current = head

    while current is not None:
        if current.data in seen_values:
            previous.next = current.next
        else:
            seen_values.add(current.data)
            previous = current

        current = current.next
