from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Intersection of two Sorted Linked Lists

Given two lists sorted in increasing order, create and return a new list representing the intersection
of the two lists. The new list should be made with its own memory — the original lists should not be changed.

For example, let the first linked list be 1->2->3->4->6 and second linked list be 2->4->6->8,
then your function should create and return a third list as 2->4->6.

"""
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

def intersection(head1,head2):
    if not head1 or not head2 :
        return
    else :
        cur1 = head1
        cur2 = head2
        head = None
        temp = None

        while cur1 and cur2 :

            #print('cur1 : {} and cur2 : {}'.format(cur1.data,cur2.data))
            if cur1.data == cur2.data :
                if not temp :
                    temp = Node(cur1.data)
                    head = temp
                else:
                    temp.next = Node(cur1.data)
                    temp = temp.next
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1.data < cur2.data :
                cur1 = cur1.next
            else  :
                cur2 = cur2.next

        current = head
        while current :
            print(current.data)
            current = current.next

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10) :
        ll.insert_at_ending(i)
    ll2 = LinkedList()
    for i in range(2,30,2) :
        ll2.insert_at_ending(i)
    intersection(ll.head,ll2.head)