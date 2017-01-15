

"""
In-place conversion of Sorted DLL to Balanced BST

Given a Doubly Linked List which has data members sorted in ascending order.
Construct a Balanced Binary Search Tree which has same data members as the given Doubly Linked List.
 The tree must be constructed in-place (No new node should be allocated for tree conversion)

Examples:

Input:  Doubly Linked List 1  2  3
Output: A Balanced BST
     2
   /  \
  1    3


Input: Doubly Linked List 1  2 3  4 5  6  7
Output: A Balanced BST
        4
      /   \
     2     6
   /  \   / \
  1   3  4   7

Input: Doubly Linked List 1  2  3  4
Output: A Balanced BST
      3
    /  \
   2    4
 /
1

Input:  Doubly Linked List 1  2  3  4  5  6
Output: A Balanced BST
      4
    /   \
   2     6
 /  \   /
1   3  5

"""

class LLNode :
    def __init__(self,value=None):
        self.data = value
        self.prev = None
        self.next = None


class DLL :
    def __init__(self):
        self.head = None
        self.last = None

    def add_node_end(self, value):
        if not self.head:
            self.head = LLNode(value)
            self.last = self.head
        else:
            new_node = LLNode(value)
            self.last.next = new_node
            self.last = new_node

    def count_nodes(self):
        if not self.head :
            return 0
        else :
            current = self.head
            count = 0
            while current :
                current = current.next
                count += 1
            return count

    def convert_bst(self):
        length = self.count_nodes()
        return self.convert_bstrecur(length)

    def convert_bstrecur(self,length):
        if length <= 0 :
            return
        else :
            left = self.convert_bstrecur(length//2)
            root = self.head
            self.head = self.head.next
            root.prev = left
            root.next = self.convert_bstrecur(length - length//2 - 1)
            return root

def preorder(node):
    if not node :
        return
    else :
        print(node.data)
        preorder(node.prev)
        preorder(node.next)

if __name__=='__main__' :
    ll = DLL()
    for i in range(1,10):
        ll.add_node_end(i)
    root = ll.convert_bst()
    preorder(root)