

"""
Segregate even and odd nodes in a Linked List

Given a Linked List of integers, write a function to modify the linked list such that
all even numbers appear before all the odd numbers in the modified linked list.
 Also, keep the order of even and odd numbers same.

Examples:
Input: 17->15->8->12->10->5->4->1->7->6->NULL
Output: 8->12->10->4->6->17->15->5->1->7->NULL

Input: 8->12->10->5->4->1->6->NULL
Output: 8->12->10->4->6->5->1->NULL

// If all numbers are even then do not change the list
Input: 8->12->10->NULL
Output: 8->12->10->NULL

// If all numbers are odd then do not change the list
Input: 1->3->5->7->NULL
Output: 1->3->5->7->NULL
"""

def insert_at_end(last,node) :
    if not last :
        return node
    else :
        last.next = node
        node.next = None
        last = node
        return last

def segregate(head):
    if not head :
        return
    else :
        node = head
        while node.next :
            node = node.next
        last = node
        node = head
        prev = None
        while node.data & 1 :
            



