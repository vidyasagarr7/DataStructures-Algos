from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""

Split a Circular Linked List into two halves

"""

def split_circular_ll(ll):
    if not ll.head :
        return
    else :
        slow = ll.head
        fast = ll.head
        while fast != ll.head or fast.next != ll.head :
            fast = fast.next.next
            slow = slow.next
        mid = slow
        head2 = mid.next
        head1 = ll.head

        fast.next = head2
        mid.next = head1

        return head1,head2

if __name__=='__main__':

    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    
