from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Reverse a Linked List in groups of given size
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.
"""

def reverse(head):
    if not head :
        return
    else :
        current = head
        prev = None
        while current :
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

def reverse_in_groups(head,k):
    if not head  :
        return
    else :
        current = head
        count = 0
        prev = None
        next = None
        while current  and count < k :
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next :
            head.next = reverse_in_groups(next,k)
        return prev


if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,3):
        ll.insert_at_ending(i)

    ll.head = reverse(ll.head)
    #ll.print_list()
    ll.head = reverse(ll.head)


    ll.head = reverse_in_groups(ll.head,1)
    ll.print_list()






