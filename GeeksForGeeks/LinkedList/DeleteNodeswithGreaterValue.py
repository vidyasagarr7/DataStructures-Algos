from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
import sys
"""
Delete nodes which have a greater value on right side
Given a singly linked list, remove all the nodes which have a greater value on right side.


- 12->15->10->11->5->6->2->3->NULL should be changed to 15->11->6->3->NULL.

Note that 12, 10, 5 and 2 have been deleted because there is a greater value on the right side.

"""
def reverse(head):
    if not head :
        return
    else :
        current = head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


### REVISIT the code - check logic again.


def delete_nodes(head):
    if not head :
        return
    else :
        new_head = reverse(head)

        current = new_head
        _max = current.data
        while current and current.next :
            if current.next.data < _max and current.next :
                current.next = current.next.next
            else :
                _max = current.data
            current = current.next

        head1 = reverse(new_head)
        return head1

if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_ending(12)
    ll.insert_at_ending(15)
    ll.insert_at_ending(10)
    ll.insert_at_ending(11)
    ll.insert_at_ending(5)
    ll.insert_at_ending(6)
    ll.insert_at_ending(2)
    ll.insert_at_ending(3)
    ll.head = delete_nodes(ll.head)
    ll.print_list()