from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Alternating split of a given Singly Linked List

Write a function AlternatingSplit() that takes one list and divides up its nodes to make
two smaller lists ‘a’ and ‘b’. The sublists should be made from alternating elements in the original list.
So if the original list is 0->1->0->1->0->1 then one sublist should be 0->0->0 and the other should be 1->1->1.
"""

def split(head):
    if not head :
        return
    else :
        a = head

        if not head.next :
            return a,None
        else :
            b = head.next
            head.next = b.next
        last_a = a
        last_b = b
        current = head.next
        while current and current.next :
            last_a = insert_at_end(last_a,current)
            last_b = insert_at_end(last_b,current.next)
            current = current.next.next
        # if there are odd number of nodes, adding the last node to the first list
        if current :
            last_a = insert_at_end(last_a,current)
        last_a.next = None
        last_b.next = None
        return a,b

def insert_at_end(last,node):
    if not last :
        return node
    else :
        #node = Node(data)
        last.next = node
        return node

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    a,b = split(ll.head)

    cur1 = a
    while cur1 :
        print(cur1.data)
        cur1 = cur1.next
    cur2 = b
    while cur2 :
        print(cur2.data)
        cur2 = cur2.next






