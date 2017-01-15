from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""

Intersection of two Sorted Linked Lists

Given two lists sorted in increasing order, create and return a new list representing the intersection of the two
lists. The new list should be made with its own memory — the original lists should not be changed.

For example, let the first linked list be 1->2->3->4->6 and second linked list be 2->4->6->8,
then your function should create and return a third list as 2->4->6.

"""

def intersection_list(head1,head2):

    ll = LinkedList()

    cur1 = head1
    cur2 = head2

    while cur1 and cur2 :
        if cur1.data < cur2.data :
            cur1 = cur1.next
        elif cur1.data > cur2.data :
            cur2 = cur2.next
        else :
            ll.insert_at_ending(cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next

    return ll

if __name__=='__main__':
    l1 = LinkedList()
    for i in range(1,10) :
        l1.insert_at_ending(i)
    l2 = LinkedList()
    for j in range(5,10):
        l2.insert_at_ending(j)
    l3 = intersection_list(l1.head,l2.head)
    l3.print_list()
