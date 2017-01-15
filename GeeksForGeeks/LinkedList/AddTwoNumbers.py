from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList,Node
"""
Add two numbers represented by linked lists | Set 1

Given two numbers represented by two lists, write a function that returns sum list.
 The sum list is list representation of addition of two input numbers.

Example 1

Input:
  First List: 5->6->3  // represents number 365
  Second List: 8->4->2 //  represents number 248
Output
  Resultant list: 3->1->6  // represents number 613
Example 2

Input:
  First List: 7->5->9->4->6  // represents number 64957
  Second List: 8->4 //  represents number 48
Output
  Resultant list: 5->0->0->5->6  // represents number 65005
"""


def add(head1,head2):
    if not head1 and not head2 :
        return head2
    elif not head1 and head2 :
        return head2
    elif not head2 and head1 :
        return head1
    else :

        carry = 0
        cur1 = head1
        cur2 = head2
        new_head = None
        while cur1 and cur2 :
            _sum = cur1.data + cur2.data + carry
            if _sum > 9:
                carry = 1
            else :
                carry = 0
            _sum = _sum % 10
            if not new_head :
                new_head = Node(_sum)
                current = new_head
            else :
                current.next = Node(_sum)
                current = current.next
            cur1 = cur1.next
            cur2 = cur2.next


        while cur1 :
            _sum = cur1.data + carry
            carry = _sum // 10
            _sum = _sum % 10
            current.next = Node(_sum)
            cur1 = cur1.next
            current = current.next

        while cur2 :
            _sum = cur2.data + carry
            carry = _sum // 10
            _sum = _sum % 10
            current.next = Node(_sum)
            cur2 = cur2.next
            current = current.next

        if carry == 1 :
            current.next = Node(carry)

        return new_head





if __name__=='__main__' :
    ll1 = LinkedList()
    ll1.insert_at_ending(3)
    ll1.insert_at_ending(6)
    ll1.insert_at_ending(5)

    ll2 = LinkedList()
    ll2.insert_at_ending(2)
    ll2.insert_at_ending(4)
    ll2.insert_at_ending(8)

    ll = LinkedList()
    ll.head = add(ll1.head,ll2.head)
    ll.print_list()


