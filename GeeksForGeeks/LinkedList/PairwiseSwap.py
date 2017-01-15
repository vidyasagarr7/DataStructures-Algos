from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Pairwise swap elements of a given linked list

Given a singly linked list, write a function to swap elements pairwise.
For example, if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5,
and if the linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5.

"""

def pairwise_swap(head):
    """
    exchange the data in adjacent nodes - O(n) time
    :param head:
    :return:
    """
    if not head:
        return
    else   :
        current = head
        while current.next :
            current.data,current.next.data  = current.next.data,current.data
            current = current.next.next
    return head

def _pairwise_swap(node):
    """
    Changing the nodes links  - O(n) time
    :param node:
    :return:
    """
    if not node or not node.next :
        return node

    current = node.next
    prev = node
    node = current

    while prev and current :
        next = current.next
        current.next = prev

        if not next or not next.next :
            prev.next = next
            break
        prev.next = next.next
        prev = next
        current = prev.next

    return node



if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    #ll.print_list()
    #pairwise_swap(ll.head)
    #ll.print_list()

    ll.head = _pairwise_swap(ll.head)
    ll.print_list()