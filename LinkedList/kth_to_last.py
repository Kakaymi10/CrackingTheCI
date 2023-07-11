'''This solution is recursive, meaning that it calls itself to solve the problem. 
The base case is when the head of the linked list is None. In this case, the function returns None.
Otherwise, the function recursively calls itself to find the k - 1 to last element of the linked list. 
The return value of the recursive call is then the k to last element of the linked list.'''

def kth_to_last_recursive(head, k):
    if head is None:
        return None

    if k == 1:
        return head

    return kth_to_last_recursive(head.next, k - 1)


'''This solution is non-recursive, meaning that it does not call itself to solve the problem. 
The function first initializes two variables, count and curr. The variable count keeps track of the number of nodes in the linked list, 
and the variable curr points to the current node in the linked list.

The function then iterates through the linked list, incrementing the count variable for each node. 
When the count variable reaches k, the function knows that it has reached the k to last element of the linked list. 
The function then sets the curr variable to the head of the linked list and iterates through the linked list k - 1 more times. 
The return value of the function is the k to last element of the linked list.'''

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

    return curr
