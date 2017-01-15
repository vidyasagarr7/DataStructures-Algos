from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Pairwise swap elements of a given linked list

Given a singly linked list, write a function to swap elements pairwise.

For example, if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5,
 and if the linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5.

"""

def pairwise_swap(head):
    if not head :
        return
    else :
        current = head
        while current and current.next :
            current.data, current.next.data = current.next.data,current.data
            current = current.next.next

def _pairwiseswap(node):
    if not node :
        return
    else :
        if node and node.next :
            node.data, node.next.data = node.next.data, node.data
            _pairwiseswap(node.next.next)

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    pairwise_swap(ll.head)
    #ll.print_list()

    _pairwiseswap(ll.head)
    ll.print_list()