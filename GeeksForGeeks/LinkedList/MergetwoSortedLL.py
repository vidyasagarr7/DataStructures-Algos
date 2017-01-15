from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order,
 and merges the two together into one list which is in increasing order. SortedMerge() should return the new list.
 The new list should be made by splicing
together the nodes of the first two lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20,
 then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

"""

def merge_sortedlists(a,b):
    if not a and not b :
        return
    if not a and b :
        return b
    if not b and a :
        return a
    else :
        cur1 = a
        cur2 = b
        new = None

        while cur1 and cur2 :
            if cur1.data <= cur2.data :
                if not new :
                    head = cur1
                    new = cur1
                else :
                    new.next = cur1
                    new = new.next
                cur1 = cur1.next

            else :
                if not new :
                    head = cur2
                    new = cur2
                else :
                    new.next = cur2
                    new = new.next
                cur2 = cur2.next

        """
        while cur1 and cur2 :
            if cur1.data <= cur2.data :
                if not new :
                    head = cur1
                    new = cur1
                else :
                    new = insert_at_ending(new,cur1)
                cur1 = cur1.next
            else :
                if not new  :
                    head = cur2
                    new = cur2
                else :
                    new = insert_at_ending(new,cur2)
                cur2 = cur2.next
        """


        while cur1 :
            new.next = cur1
            cur1 = cur1.next
            new = new.next

        while cur2 :
            new.next = cur2
            cur2 = cur2.next
            new = new.next
        new.next = None
        return head

def insert_at_ending(last,node):
    if not last  :
        return node
    else :
        last.next = node
        return node

if __name__=='__main__':
    ll1 = LinkedList()
    for i in range(1,15):
        ll1.insert_at_ending(i)
    ll2 = LinkedList()
    for j in range(11,19):
        ll2.insert_at_ending(j)
    head = merge_sortedlists(ll2.head,ll1.head)
    current = head
    while current :
        print(current.data)
        current = current.next
