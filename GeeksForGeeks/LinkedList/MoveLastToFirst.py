from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Move last element to front of a given Linked List
Write a C function that moves last element to front in a given Singly Linked List. For example, if the given Linked
List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.
"""

def move_nth(head):
    if not head :
        return
    else :
        current = head
        prev = head
        while current.next is not None :
            prev = current
            current = current.next
        prev.next = None
        current.next = head
        head = current
        return head

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    ll.head = move_nth(ll.head)
    ll.print_list()

