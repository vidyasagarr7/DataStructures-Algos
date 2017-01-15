from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""

Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order,
and merges the two together into one list which is in increasing order. SortedMerge() should return the new list.
The new list should be made by splicing together the nodes of the first two lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20,
then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during processing either ‘a’ or ‘b’
may run out first, and finally there’s the problem of starting the result list empty, and building it up while
going through ‘a’ and ‘b’.

"""

def merge_two_ll(head1,head2):
    if not head1 and not head2 :
        return
    if not head1 and head2 or not head2 and head1:
        return head2 if not head1 else head1
    else  :
        cur1 = head1
        cur2 = head2
        head = None
        if cur1.data < cur2.data:
            head = cur1
            cur1 = cur1.next
        else :
            head = cur2
            cur2 = cur2.next
        current = head
        while cur1.next and cur2.next :
            if cur1.data < cur2.data :
                current.next = cur1
                cur1 = cur1.next
            else :
                current.next = cur2
                cur2 = cur2.next
            current = current.next
        while cur1 :
            current.next = cur1
            cur1 = cur1.next
            current = current.next
        while cur2 :
            current.next = cur2
            cur2  = cur2.next
            current = current.next

        return head

if __name__=='__main__':
    l1 = LinkedList()
    for i in range(1,10):
        l1.insert_at_ending(i)
    l2 = LinkedList()
    for i in range(1,15,2):
        l2.insert_at_ending(i)
    head = merge_two_ll(l1.head,l2.head)

    current = head
    while current :
        print(current.data)
        current = current.next




