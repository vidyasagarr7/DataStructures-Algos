from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""

Identical Linked Lists

Two Linked Lists are identical when they have same data and arrangement of data is also same.
For example Linked lists a (1->2->3) and b(1->2->3) are identical.
Write a function to check if the given two linked lists are identical.

"""

def check_identical(head1,head2):
    if not head2 and not head1 :
        return True
    if head2 and not head1 or head1 and not head2 :
        return False
    else  :
        return head1.data==head2.data and check_identical(head1.next,head2.next)

def is_identical(head1,head2):
    if not head1 and not head2  :
        return True
    if (not head1 and head2) or (head1 and not head2) :
        return False
    else :
        cur1 = head1
        cur2 = head2
        while cur1 and cur2 :
            if cur1.data != cur2.data :
                return False
            else :
                cur1 = cur1.next
                cur2 = cur2.next
        if cur1 :
            return False
        if cur2 :
            return False
        return True

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    l2 = LinkedList()
    for i in range(1,10):
        l2.insert_at_ending(i)
    l3 = LinkedList()
    for j in range(1,5):
        l3.insert_at_ending(j)
    print(check_identical(ll.head,l2.head))
    print(check_identical(l2.head,l3.head))

    print(is_identical(ll.head,l2.head))
    print(is_identical(l2.head,l3.head))


