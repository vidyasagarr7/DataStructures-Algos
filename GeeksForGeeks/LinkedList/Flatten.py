
"""
Flatten a multilevel linked list


Given a linked list where in addition to the next pointer, each node has a child pointer,
which may or may not point to a separate list. These child lists may have one or more children of their own,
 and so on, to produce a multilevel data structure, as shown in below figure.You are given the head of the
  first level of the list. Flatten the list so that all the nodes appear in a single-level linked list.
   You need to flatten the list in way that all nodes at first level should come first, then nodes of
    second level, and so on.

Each node is a C struct with the following definition.

struct list
{
    int data;
    struct list *next;
    struct list *child;
};
Run on IDE

"""

# check the correctness of the algorithm again.


class Node :
    def __init__(self,data=None):
        self.data = data
        self.next  = None
        self.child = None

def flatten_ll(head):
    if not head :
        return
    else :
        current = head
        while current.next :
            current = current.next
        tail = current

        current = head
        while current != tail :
            if current.child :
                tail.next = current.child

                temp = current.child
                while temp.next :
                    temp = temp.next
                tail = temp
            current = current.next






def print_ll(head):
    if not head :
        return
    else:
        current = head
        while current :
            print(current.data)
            current = current.next

if __name__=='__main__':
    head = Node(10)
    head.next = Node(5)
    head.next.next = Node(12)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(11)

    head.child = Node(4)
    head.child.next = Node(20)
    head.child.next.next = Node(13)

    head.next.next.next.child = Node(17)
    head.next.next.next.child.next = Node(6)

    head.child.next.child = Node(2)

    head.child.next.next.child = Node(16)
    flatten_ll(head)

    print_ll(head)










