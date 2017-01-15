from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
function a revervse a linkedlist
"""

def reverse_ll(head) :
    """
    reversing the pointers for every node - Single traveral - O(n) time.
    :param head
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

if __name__=='__main__':
    ll = LinkedList()
    for i in range(5,9):
        ll.insert_at_ending(i)

    ll.print_list()

    ll.head = reverse_ll(ll.head)
    ll.print_list()