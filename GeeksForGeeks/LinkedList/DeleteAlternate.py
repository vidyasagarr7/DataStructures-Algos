from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Delete alternate nodes of a Linked List

Given a Singly Linked List, starting from the second node delete all alternate nodes of it.
For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5,
and if the given linked list is 1->2->3->4 then convert it to 1->3.

"""

def delete_alternate_node(node):
    if not node  :
        return
    else  :
        current = node
        while current.next :
            current.next = current.next.next
            current = current.next


if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,6):
        ll.insert_at_ending(i)
    delete_alternate_node(ll.head)
    ll.print_list()