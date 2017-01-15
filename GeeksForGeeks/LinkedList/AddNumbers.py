from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
from GeeksForGeeks.LinkedList.AddTwoNumbers import add

"""
Add two numbers represented by linked lists | Set 2

Given two numbers represented by two linked lists, write a function that returns sum list.
The sum list is linked list representation of addition of two input numbers. It is not allowed to modify
the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).

Example

Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405


"""
def reverse(head):
    if not head :
        return
    else :
        prev = None
        current = head
        while current :
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


def add_numbers(head1,head2):
    """
    If the algorithm is allowed to modify the lists.
    :param head1:
    :param head2:
    :return:
    """
    if not head2 and head1 :
        return head1
    elif not head1 and head2 :
        return head2
    elif not head1 and not head2 :
        return head2
    else :
        return reverse(add(reverse(head1),reverse(head2)))

def print_ll(head):
    if not head :
        return
    else :
        current = head
        while current :
            print(current.data)
            current = current.next

def length(head):
    if not head :
        return 0
    else :
        count = 0
        current = head
        while current:
            current = current.next
            count +=1
        return count


def addnumbers(head1,head2):
    if not head2 and head1 :
        return head1
    elif not head1 and head2 :
        return head2
    elif not head1 and not head2 :
        return head2
    else :
        len1 = length(head1)
        len2 = length(head2)

        cur1 = head1
        cur2 = head2

        if len1 > len2 :
            diff = len1 - len2
            count  = 0
            while count < diff :
                count += 1
                cur1  = cur1.next

        elif  len1 < len2 :
            diff  = len2  - len1
            count = 0
            while count < diff :
                count +=1
                cur2  = cur2.next

        root, carry = addsamesize(cur1,cur2)
        """
        if carry ==1 :
            node = Node(carry)
            node.next = root
            root = node
        return root
        """
        if len1 > len2 :
            cur1 = head1


def add_remaining(head,carry):
    if not head :
        return 




class Node :
    def __init__(self,data=None):
        self.data = data
        self.next = None

def addsamesize(head1,head2):
    if not head1 and not head2 :
        return None,0
    else :
        node = Node()
        node.next,carry = addsamesize(head1.next,head2.next)
        _sum = head1.data + head2.data + carry
        carry = _sum // 10
        _sum = _sum % 10
        node.data = _sum
        return node,carry


if __name__=='__main__':
    l1 = LinkedList()
    l1.insert_at_ending(5)
    l1.insert_at_ending(6)
    l1.insert_at_ending(3)
    l1.insert_at_ending(3)

    l2 = LinkedList()
    l2.insert_at_ending(8)
    l2.insert_at_ending(4)
    l2.insert_at_ending(2)

    #head = add_numbers(l1.head,l2.head)
    #print_ll(head)

    root = addnumbers(l1.head,l2.head)
    print_ll(root)