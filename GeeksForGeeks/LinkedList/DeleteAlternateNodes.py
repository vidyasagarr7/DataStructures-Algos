from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Delete alternate nodes of a Linked List

Given a Singly Linked List, starting from the second node delete all alternate nodes of it.
For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5,
and if the given linked list is 1->2->3->4 then convert it to 1->3.

"""

def delete_alt(head):
    if not head :
        return
    else :
        node = head
        while node and node.next :
            node.next = node.next.next
            node = node.next

def _del_alt(node):
    if not node or not node.next :
        return
    else :
        node.next = node.next.next
        _del_alt(node.next)

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    #delete_alt(ll.head)
    _del_alt(ll.head)
    ll.print_list()

    ll2 = LinkedList()
    ll2.insert_at_ending(1)
    #delete_alt(ll2.head)
    _del_alt(ll2.head)
    ll2.print_list()

    ll3 = LinkedList()
    ll3.insert_at_ending(3)
    ll3.insert_at_ending(4)
    #delete_alt(ll3.head)
    _del_alt(ll3.head)
    ll3.print_list()

