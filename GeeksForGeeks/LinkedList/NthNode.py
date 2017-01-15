from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList

"""
Write a function to get Nth node in a Linked List

"""


def get_Nth_node(head,idx):
    if not head :
        return
    else :
        current = head
        count = 1
        while count != idx :
            current = current.next
            count += 1
        return current.data

if __name__=='__main__' :
    ll = LinkedList()
    for i in range(0,10):
        ll.insert_at_ending(i)
    print(get_Nth_node(ll.head,4))

