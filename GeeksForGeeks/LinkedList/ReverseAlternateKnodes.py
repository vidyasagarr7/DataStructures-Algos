from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Reverse alternate K nodes in a Singly Linked List

Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function)
in an efficient way. Give the complexity of your algorithm.

Example:
Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
"""
def reverse_alt_knodes(head,k):
    if not head :
        return
    else :
        current = head
        next = None
        prev = None
        count = 0
        while current and count < k :
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next  :
            head.next = current

        count = 0
        while current and count < k-1 :
            current = current.next
            count += 1

        if current :
            current.next = reverse_alt_knodes(current.next,k)
        return prev



if __name__=='__main__':
    ll = LinkedList( )
    for i in range(1,10):
        ll.insert_at_ending(i)
    ll.head = reverse_alt_knodes(ll.head,3)
    ll.print_list()
