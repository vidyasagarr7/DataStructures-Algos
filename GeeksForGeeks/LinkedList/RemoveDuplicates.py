from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
def remove_duplicates(head):
    if not head :
        return
    else :
        current = head

        while current  and current.next :
            if current.data == current.next.data :
                current.next = current.next.next
            current = current.next

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.sorted_insert(i)
    for i in range(1,10):
        ll.sorted_insert(i)
    ll.print_list()

    print('break')

    remove_duplicates(ll.head)
    ll.print_list()
    


