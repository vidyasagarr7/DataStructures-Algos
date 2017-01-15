from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList,Node

def reverse_ll(head) :
    """
    reversing the next pointers at each node
    :param head:
    :return:
    """
    prev = None
    current = head
    while current :
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def _reverse_ll(current,prev):

    if not current.next :
        current.next = prev
        return current
    next = current.next
    current.next = prev
    return _reverse_ll(next,current)


if __name__=="__main__":
    ll = LinkedList()

    for i in range(1,10):
        ll.insert_at_ending(i)

    #ll.print_list()

    #ll.head = _reverse_ll(ll.head,None)
    #ll.print_list()

    ll.head = reverse_ll(ll.head)
    ll.print_list()