from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

def remove_element(head,value):
    if not head :
        return
    else :
        current = head
        prev = head
        while current :
            if current.data != value :
                current = current.next
                prev = current
            else :
                prev.next = current.next
                current = prev.next
        if head.data == value :
            head = head.next
        return head

def _remove_element(head,value):
    if not head :
        return
    else :
        current = head
        while current and current.next :
            if current.next.data != value  :
                current = current.next
            else  :
                current.next = current.next.next
                current = current.next
        if head.data == value :
            head = head.next
        return head


if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_ending(1)
    ll.insert_at_ending(1)
    ll.insert_at_ending(1)
    ll.insert_at_ending(1)
    _remove_element(ll.head,value=1)
    ll.print_list()