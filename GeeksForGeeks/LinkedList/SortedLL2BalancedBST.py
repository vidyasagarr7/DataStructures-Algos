

"""
Sorted Linked List to Balanced BST


Given a Singly Linked List which has data members sorted in ascending order.
Construct a Balanced Binary Search Tree which has same data members as the given Linked List.

Examples:

Input:  Linked List 1->2->3
Output: A Balanced BST
     2
   /  \
  1    3


Input: Linked List 1->2->3->4->5->6->7
Output: A Balanced BST
        4
      /   \
     2     6
   /  \   / \
  1   3  4   7

Input: Linked List 1->2->3->4
Output: A Balanced BST
      3
    /  \
   2    4
 /
1

Input:  Linked List 1->2->3->4->5->6
Output: A Balanced BST
      4
    /   \
   2     6
 /  \   /
1   3  5

"""
class BTNode :
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


def list2bbt(input_list,start,end):

    if not input_list or start > end:
        return
    else:
        mid = start + (end-start)//2

        root = BTNode(input_list[mid])

        root.left = list2bbt(input_list,start,mid-1)
        root.right = list2bbt(input_list,mid+1,end)

        return root

def preorder(node):
    if not node :
        return
    else :
        print(node.data)
        preorder(node.left)
        preorder(node.right)


class LLNode :
    def __init__(self,value):
        self.data = value
        self.next = None

class LL :
    def __init__(self,head=None):
        self.head  = head

    def add_node(self,value):
        if not self.head :
            self.head = LLNode(value)
        else:
            current = self.head
            while current and current.next :
                current = current.next
            current.next = LLNode(value)

    def print_ll(self):
        if not self.head :
            return
        else :
            current = self.head
            while current :
                print(current.data)
                current = current.next

    def count_nodes(self):
        if not self.head :
            return 0
        else :
            count = 0
            current = self.head
            while current :
                count += 1
                current = current.next
            return count

    def convert_bt(self):
        length = self.count_nodes()
        return self.convert_btrecur(length)

    def convert_btrecur(self,length):
        if length <= 0 :
            return
        else :
            left = self.convert_btrecur(length//2)
            root = BTNode(self.head.data)
            self.head = self.head.next

            root.left = left
            root.right = self.convert_btrecur(length - length//2 -1)
            return root

if __name__=='__main__':

    test = [1,2,3,4,5,6,7]
    root = list2bbt(test,0,len(test)-1)
    #preorder(root)

    ll = LL()
    for i in range(1,11):
        ll.add_node(i)
    #ll.print_ll()
    root = ll.convert_bt()
    preorder(root)






